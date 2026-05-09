# AIX Card交易【transaction】

# 1. 需求变更日志

|          |                   |          |      |
|:---------|:------------------|:---------|:-----|
| 变更时间 | 变更人            | 变更内容 | 备注 |
|          | @Yifeng Wu 吴忆锋 | 初稿     |      |
|          |                   |          |      |
|          |                   |          |      |

# 2. 引用资料

|          |                   |
|:---------|:------------------|
| **类型** | 链接              |
| PM       | @Yifeng Wu 吴忆锋 |
| Figma    |                   |
| BRD      | N/A               |
| 技术方案 |                   |

# 3. 需求索引

**\[同步块-无权限下载此内容\]**

# 2. 项目概述

2.1 **项目背景**

|  |
|:---|
| 为满足全球用户对一体化、便捷安全数字金融服务的需求，本项目旨在开发一款创新的移动应用。该应用将整合先进的支付与账户管理技术，致力于为用户提供全新的移动端金融管理体验。 |

2.2 **项目目的**

<table style="width:88%;">
<colgroup>
<col style="width: 88%" />
</colgroup>
<tbody>
<tr>
<td><p>构建基础​：建立安全、便捷的用户注册登录与账户体系。</p>
<p>核心功能​：实现充值、提现、转账、消费等关键支付功能。</p>
<p>安全保障​：通过多层验证与风控策略，确保用户资产与信息安全。</p>
<p>体验优化​：提供流畅直观的操作流程，提升用户留存。</p></td>
</tr>
</tbody>
</table>

2.3 **名词解释**

<table style="width:88%;">
<colgroup>
<col style="width: 88%" />
</colgroup>
<tbody>
<tr>
<td><table style="width:86%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr>
<td style="text-align: left;"><strong>名词/缩写</strong></td>
<td style="text-align: left;"><strong>说明</strong></td>
</tr>
<tr>
<td style="text-align: left;">DeviceID</td>
<td style="text-align: left;">用于唯一识别用户客户端的设备编号。用于实现设备绑定、可信设备判断及风险控制等。</td>
</tr>
<tr>
<td style="text-align: left;">IVS</td>
<td style="text-align: left;"><p>Identity Verification Service，身份验证服务。</p>
<p>通常指用于进行高强度实名验证的服务（如证件识别、人脸比对等），在注册或敏感操作流程中可能被调用。</p></td>
</tr>
<tr>
<td style="text-align: left;">Biometric</td>
<td style="text-align: left;">通过用户的生物特征（如指纹、面部信息）进行身份验证的技术。支持iOS Face ID/Android指纹/人脸</td>
</tr>
<tr>
<td style="text-align: left;">AIX Tag</td>
<td style="text-align: left;">用户在AIX平台上的身份标识符。用于在转账、社交等场景中代替复杂的钱包地址，使用户能够被轻松找到和支付。此标识一旦设置，通常不可更改。</td>
</tr>
<tr>
<td style="text-align: left;">DTC</td>
<td style="text-align: left;">AIX项目的合作伙伴，提供加密钱包、卡片发行和KYC服务的后端平台，支持OpenAPI接口，用于处理交易、认证和账户管理。</td>
</tr>
<tr>
<td style="text-align: left;">AAI</td>
<td style="text-align: left;">第三方身份验证服务提供商，用于KYC流程中的护照上传、活体检测和人脸比对。支持Webhook回调和URL生成。</td>
</tr>
<tr>
<td style="text-align: left;">Master Account</td>
<td style="text-align: left;">DTC侧的账户概念，主账户，可申请API Key管理多个Sub Account。敏感操作需Sub Account授权。</td>
</tr>
<tr>
<td style="text-align: left;">Sub Account</td>
<td style="text-align: left;">DTC侧的账户概念，子账户，由Master创建，用于分离用户资产。KYC需独立完成。</td>
</tr>
<tr>
<td style="text-align: left;">WalletConnect</td>
<td style="text-align: left;">通过Deeplink/QR链接外部钱包充值。自动加白名单、交易报备，直接到账。</td>
</tr>
<tr>
<td style="text-align: left;">PIN</td>
<td style="text-align: left;">Personal Identification Number，卡片PIN码，用于线下交易。4位数字，支持Set/Change/Reset。</td>
</tr>
<tr>
<td style="text-align: left;">稳定币类型</td>
<td style="text-align: left;">稳定币类型USDC, USDT, FDUSD, WUSD，支持在BASE/BSC/ETHEREUM/SOLANA网络充值/转账/兑换。</td>
</tr>
<tr>
<td style="text-align: left;">区块链网络</td>
<td style="text-align: left;">支持的区块链网络，各网络币种不同（e.g., BASE: USDC）。包括：BASE, BSC, ETHEREUM, SOLANA</td>
</tr>
<tr>
<td style="text-align: left;">Global Travel Rule</td>
<td style="text-align: left;">全球旅行规则，合规要求，仅支持如Binance的白名单钱包充值。自动报备，无需声明。</td>
</tr>
</tbody>
</table>
<p>同步自文档: <a href="https://advancegroup.sg.larksuite.com/docx/Sy4TdCxUFoCEWbxdcoQlBgzhgfh#WEeGd3rFjsp8Kjb59vLlbcdog1n">https://advancegroup.sg.larksuite.com/docx/Sy4TdCxUFoCEWbxdcoQlBgzhgfh#WEeGd3rFjsp8Kjb59vLlbcdog1n</a></p></td>
</tr>
</tbody>
</table>

# 3. 项目计划

[AIX项目管理表](https://advancegroup.sg.larksuite.com/sheets/RFR2sp4VGhbXVDtlnjTlwVsYgAb?from=from_copylink&sheet=z4hjo9)

# 4. 功能结构

<img src="/tmp/prd-one-card-transaction/assets/media/image1.jpeg" style="width:5.75in;height:5.6875in" />

# 5. 国家线

|        |        |        |
|:------:|:------:|:------:|
| **VN** | **PH** | **AU** |
|   ✅   |   ✅   |   ✅   |

# 6. 统一规则

略

# 7. 需求描述

<table style="width:88%;">
<colgroup>
<col style="width: 88%" />
</colgroup>
<tbody>
<tr>
<td style="text-align: left;"><p>DTC的知识点</p>
<p>Refund 场景：</p>
<p> - 无论退款交易的币种是否与原卡消费币种一致，<strong>退款金额均退回到卡余额。</strong></p>
<p> - 退款时，系统会<strong>根据交易发生时的汇率</strong>，将 USD 金额转换为 USDT 等值金额后再退回。</p>
<p> - <strong>退款仅退还净商品金额</strong>，不包含 FX 费用和 Transaction Fee。</p>
<p> - 退款过程中<strong>不收取额外手续费</strong>。</p></td>
</tr>
</tbody>
</table>

7.1 **功能概述**

**作为AIX用户**，希望在卡收到资金，自动回退到钱包账户。

7.2 **业务流程**

<img src="/tmp/prd-one-card-transaction/assets/media/image2.jpeg" style="width:5.75in;height:5.75in" />

7.3 **流程说明**

<table style="width:89%;">
<colgroup>
<col style="width: 15%" />
<col style="width: 7%" />
<col style="width: 65%" />
</colgroup>
<tbody>
<tr>
<td style="text-align: left;">关键节点</td>
<td style="text-align: left;">执行方</td>
<td style="text-align: left;">说明</td>
</tr>
<tr>
<td style="text-align: left;">触发通知</td>
<td style="text-align: left;">DTC</td>
<td style="text-align: left;">DTC检测发生交易，通过【<strong>Card Transaction Notification</strong>】接口，DTCPay 向 AIX 发送交易通知。</td>
</tr>
<tr>
<td style="text-align: left;">主动查询卡余额</td>
<td style="text-align: left;">AIX</td>
<td style="text-align: left;"><p><strong>AIX 收到交易通知后，先校验type是否为 <em>refund</em> 、 <em>reversal、<del>Top-up、</del>deposit；</em></strong></p>
<p>若不是则终止流程。</p>
<p>若匹配，则调用【<strong>Inquiry Card Basic Info</strong>】主动查询当前卡余额，DTCPay 返回最新卡 balance。记录接口字段：balance</p></td>
</tr>
<tr>
<td style="text-align: left;">请求资金回退钱包</td>
<td style="text-align: left;">AIX</td>
<td style="text-align: left;"><p><strong>判断卡余额：</strong></p>
<p>若卡当前余额 balance &gt; 0，AIX 调用【<strong>transfer to wallet</strong>】，请求将卡内余额归集到用户钱包，入参 amount = 返回字段balance。</p>
<p>若卡当前余额 balance = 0，则终止流程。</p></td>
</tr>
<tr>
<td style="text-align: left;">回退结果校验</td>
<td style="text-align: left;">AIX</td>
<td style="text-align: left;"><p><strong>AIX 校验回退接口返回结果。</strong></p>
<p>若失败，则发送异常告警至监控群，人工介入处理</p>
<p>失败原因为系统原因，则开发跟进处理；</p>
<p>失败原因为交易金额大于卡余额，则@Yifeng Wu 吴忆锋跟进处理；</p>
<p>若成功，资金已转入用户钱包，流程结束。</p></td>
</tr>
</tbody>
</table>

# 8. 外部接口依赖

8.1 **外部接口清单**

|  |  |  |  |
|:---|:---|:---|:---|
| 接口名称 | **接口地址** | 涉及功能模块 | **接口说明** |
| Card Transaction Notificatio |  |  |  |
| Card Balance History Inquiry | openapi/v1/card/inquiry-card-balance-history |  |  |
| Transfer Balance to Wallet | openapi/v1/card/transfer-to-wallet |  |  |

# 9. 待确认事项

~~跟DTC确认接口，确认每个接口的取值字段~~
