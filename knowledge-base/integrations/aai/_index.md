---
module: integrations
feature: aai
version: "1.0"
status: draft
source_doc: 历史prd / AIX Security 身份认证需求V1.0
source_section: TBD
last_updated: 2026-05-01
owner: 吴忆锋
depends_on: [_meta, security]
readers: [product, dev, qa, ai]
---

# AAI Integration

## 1. 模块定位

本文档用于沉淀 AAI 在证件识别、OCR、活体、人脸比对、POA 等身份验证场景中的外部能力事实。

## 2. 文件清单

| 文件 | 内容 | 状态 |
|------|------|------|
| kyc-and-face.md | KYC、证件、活体、人脸比对能力事实 | 待创建 |

## 3. 维护规则

- AAI 耗时、失败次数、signatureId、重试规则必须保留来源。
- 与 AIX 自有认证、DTC 活体识别的边界必须分开写。
- 不确定外部能力时必须标记待确认。
