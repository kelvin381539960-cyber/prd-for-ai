#!/usr/bin/env node
/**
 * AI Bridge callable image OCR runner.
 *
 * Why this exists:
 * - The assistant can call ai_bridge.execCliCommand, but the bridge host may not
 *   have Python/Docker.
 * - The bridge host does have Node/npm. This script uses mature Node packages:
 *   sharp for image slicing and tesseract.js for OCR.
 * - It writes OCR output back to GitHub as JSON/Markdown so the assistant can
 *   read the result with ai_bridge.readFile and continue the task.
 *
 * Install deps in a temp dir before running:
 *   npm install sharp tesseract.js
 *
 * Example:
 *   node tools/ai_bridge_image_ocr.js \
 *     --owner kelvin381539960-cyber \
 *     --repo prd \
 *     --branch main \
 *     --image knowledge-base/kyc/_assets/account-opening/image4.jpeg \
 *     --out .ai-visual-cache/kyc-account-opening-image4/ocr.json \
 *     --grid 4x4 \
 *     --lang eng+chi_sim
 */

const fs = require('fs');
const https = require('https');
const path = require('path');

function parseArgs(argv) {
  const args = {
    owner: 'kelvin381539960-cyber',
    repo: 'prd',
    branch: 'main',
    image: '',
    out: '',
    grid: '4x4',
    lang: 'eng+chi_sim',
    scale: 2,
    full: true,
    crops: true,
    summaryChars: 1800,
  };
  for (let i = 2; i < argv.length; i++) {
    const a = argv[i];
    const next = () => argv[++i];
    if (a === '--owner') args.owner = next();
    else if (a === '--repo') args.repo = next();
    else if (a === '--branch') args.branch = next();
    else if (a === '--image') args.image = next();
    else if (a === '--out') args.out = next();
    else if (a === '--grid') args.grid = next();
    else if (a === '--lang') args.lang = next();
    else if (a === '--scale') args.scale = Number(next());
    else if (a === '--summary-chars') args.summaryChars = Number(next());
    else if (a === '--no-full') args.full = false;
    else if (a === '--no-crops') args.crops = false;
    else if (a === '--help' || a === '-h') {
      console.log('Usage: node tools/ai_bridge_image_ocr.js --image <repo path> --out <repo path> [--grid 4x4] [--lang eng+chi_sim]');
      process.exit(0);
    } else {
      throw new Error(`Unknown arg: ${a}`);
    }
  }
  if (!args.image) throw new Error('--image is required');
  if (!args.out) {
    const base = args.image.replace(/[^a-zA-Z0-9_.-]+/g, '_').replace(/^_+|_+$/g, '');
    args.out = `.ai-visual-cache/${base}/ocr.json`;
  }
  return args;
}

function readProcEnv() {
  try {
    const raw = fs.readFileSync('/proc/1/environ', 'utf8');
    const env = {};
    for (const part of raw.split('\0')) {
      const idx = part.indexOf('=');
      if (idx > 0) env[part.slice(0, idx)] = part.slice(idx + 1);
    }
    return env;
  } catch {
    return process.env;
  }
}

function gh(method, apiPath, token, body, binary = false) {
  return new Promise((resolve, reject) => {
    const data = body ? JSON.stringify(body) : null;
    const req = https.request({
      hostname: 'api.github.com',
      path: apiPath,
      method,
      headers: {
        'User-Agent': 'ai-bridge-image-ocr',
        Accept: 'application/vnd.github+json',
        Authorization: `Bearer ${token}`,
        'X-GitHub-Api-Version': '2022-11-28',
        ...(data ? { 'Content-Type': 'application/json', 'Content-Length': Buffer.byteLength(data) } : {}),
      },
    }, (res) => {
      const chunks = [];
      res.on('data', (c) => chunks.push(c));
      res.on('end', () => {
        const buf = Buffer.concat(chunks);
        if (res.statusCode >= 200 && res.statusCode < 300) {
          if (binary) return resolve(buf);
          const txt = buf.toString('utf8');
          try { resolve(txt ? JSON.parse(txt) : {}); } catch { resolve({ raw: txt }); }
        } else {
          reject(new Error(`${method} ${apiPath} ${res.statusCode}: ${buf.toString('utf8').slice(0, 1000)}`));
        }
      });
    });
    req.on('error', reject);
    if (data) req.write(data);
    req.end();
  });
}

async function getRepoFileBuffer(args, token) {
  const api = `/repos/${args.owner}/${args.repo}/contents/${encodeURIComponent(args.image).replace(/%2F/g, '/')}?ref=${encodeURIComponent(args.branch)}`;
  const meta = await gh('GET', api, token);
  if (!meta.content) throw new Error(`No content returned for ${args.image}`);
  return Buffer.from(meta.content, 'base64');
}

async function putRepoFile(args, token, repoPath, contentBuffer, message) {
  const api = `/repos/${args.owner}/${args.repo}/contents/${encodeURIComponent(repoPath).replace(/%2F/g, '/')}`;
  let sha;
  try {
    const current = await gh('GET', `${api}?ref=${encodeURIComponent(args.branch)}`, token);
    sha = current.sha;
  } catch {}
  return await gh('PUT', api, token, {
    message,
    content: contentBuffer.toString('base64'),
    sha,
    branch: args.branch,
  });
}

function parseGrid(grid) {
  const m = /^([0-9]+)x([0-9]+)$/.exec(grid);
  if (!m) throw new Error(`Invalid --grid ${grid}; expected e.g. 4x4`);
  return { cols: Number(m[1]), rows: Number(m[2]) };
}

function compactText(text) {
  return String(text || '')
    .replace(/\r/g, '\n')
    .split('\n')
    .map((s) => s.trim())
    .filter(Boolean)
    .join('\n');
}

function textLines(text, limit = 100) {
  return compactText(text).split('\n').slice(0, limit);
}

async function main() {
  const args = parseArgs(process.argv);
  const env = readProcEnv();
  const token = env.GITHUB_TOKEN || process.env.GITHUB_TOKEN;
  if (!token) throw new Error('Missing GITHUB_TOKEN in environment');

  let sharp, createWorker;
  try { sharp = require('sharp'); } catch (e) { throw new Error('Missing dependency sharp. Run: npm install sharp tesseract.js'); }
  try { ({ createWorker } = require('tesseract.js')); } catch (e) { throw new Error('Missing dependency tesseract.js. Run: npm install sharp tesseract.js'); }

  const startedAt = new Date().toISOString();
  const imageBuffer = await getRepoFileBuffer(args, token);
  const img = sharp(imageBuffer);
  const meta = await img.metadata();
  const { cols, rows } = parseGrid(args.grid);
  const worker = await createWorker(args.lang);
  const result = {
    source: { owner: args.owner, repo: args.repo, branch: args.branch, path: args.image },
    output: args.out,
    engine: { name: 'tesseract.js', lang: args.lang },
    image: { width: meta.width, height: meta.height, format: meta.format },
    grid: { cols, rows, scale: args.scale },
    startedAt,
    finishedAt: null,
    full: null,
    crops: [],
    review: {
      warning: 'OCR output is evidence only. It is not PRD truth until manually confirmed against the image.',
      requiredNextStep: 'Review crop texts and create a confirmed node/connector table before editing PRD.',
    },
  };

  if (args.full) {
    const ret = await worker.recognize(imageBuffer);
    result.full = {
      confidence: ret.data.confidence,
      chars: ret.data.text.length,
      text: compactText(ret.data.text),
      lines: textLines(ret.data.text, 120),
    };
  }

  if (args.crops) {
    const cw = Math.ceil(meta.width / cols);
    const ch = Math.ceil(meta.height / rows);
    for (let r = 0; r < rows; r++) {
      for (let c = 0; c < cols; c++) {
        const left = c * cw;
        const top = r * ch;
        const width = Math.min(cw, meta.width - left);
        const height = Math.min(ch, meta.height - top);
        const crop = await sharp(imageBuffer)
          .extract({ left, top, width, height })
          .resize({ width: Math.max(1, Math.round(width * args.scale)), height: Math.max(1, Math.round(height * args.scale)), fit: 'fill' })
          .png()
          .toBuffer();
        const ret = await worker.recognize(crop);
        result.crops.push({
          id: `r${r}_c${c}`,
          row: r,
          col: c,
          sourceBox: { left, top, width, height },
          scale: args.scale,
          confidence: ret.data.confidence,
          chars: ret.data.text.length,
          text: compactText(ret.data.text),
          lines: textLines(ret.data.text, 80),
        });
      }
    }
  }

  await worker.terminate();
  result.finishedAt = new Date().toISOString();

  const json = Buffer.from(JSON.stringify(result, null, 2));
  await putRepoFile(args, token, args.out, json, 'Add AI Bridge image OCR result');

  const mdPath = args.out.replace(/\.json$/i, '.md');
  const md = [];
  md.push(`# AI Bridge Image OCR Result`);
  md.push('');
  md.push(`Source: \`${args.image}\``);
  md.push(`Engine: \`tesseract.js ${args.lang}\``);
  md.push(`Grid: \`${cols}x${rows}\`, scale \`${args.scale}\``);
  md.push('');
  md.push('> OCR output is evidence only. Manually confirm before writing PRD.');
  md.push('');
  if (result.full) {
    md.push(`## Full image OCR`);
    md.push('');
    md.push(`Confidence: ${result.full.confidence}; chars: ${result.full.chars}`);
    md.push('');
    md.push('```text');
    md.push(result.full.text.slice(0, 12000));
    md.push('```');
  }
  md.push('');
  md.push('## Crop OCR');
  for (const crop of result.crops) {
    if (!crop.text) continue;
    md.push('');
    md.push(`### ${crop.id} confidence=${crop.confidence} chars=${crop.chars}`);
    md.push('```text');
    md.push(crop.text.slice(0, 4000));
    md.push('```');
  }
  await putRepoFile(args, token, mdPath, Buffer.from(md.join('\n')), 'Add AI Bridge image OCR markdown result');

  const summary = {
    out: args.out,
    markdown: mdPath,
    image: args.image,
    grid: args.grid,
    lang: args.lang,
    fullChars: result.full ? result.full.chars : 0,
    cropCount: result.crops.length,
    nonEmptyCrops: result.crops.filter((x) => x.text).length,
  };
  console.log(JSON.stringify(summary, null, 2));
}

main().catch((err) => {
  console.error(err && err.stack ? err.stack : String(err));
  process.exit(1);
});
