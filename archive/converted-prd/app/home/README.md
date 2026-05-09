# AIX APP V1.0【Home】

# 1. 引言

1.1 **需求索引**

**\[同步块-无权限下载此内容\]**

1.2 **修订记录**

|  |  |  |  |
|:---|:---|:---|:---|
| 日期 | 版本 | 说明 | 作者 |
| Jan 27 | V1.1 | 首页增加Waitlist（仅限APP渠道）的面板，这类用户无法申请激活钱包-yifeng需求 | @Xuemin Zhu 朱学敏 |
| Jan 27 | V1.1 | 因MVP不做单币种首页，故首页点击单个币种的跳转逻辑先去掉 | @Xuemin Zhu 朱学敏 |
| Nov 28 | V1.1 | 暂不支持钱包提现（因牌照导致的合规问题），故入口先隐藏，由用户联系CS处理； | @Xuemin Zhu 朱学敏 |

1.3 **文档目的**

|  |
|:---|
| 本文档旨在阐述 AIX APP的相关功能需求，为开发团队提供清晰的功能定义和技术实现指导，确保AIX系统能够满足稳定币相关业务的需求。 |

1.4 **产品概述**

|  |
|:---|
| AIX APP开发，侧重用户对稳定币的钱包（开通、充值、提现、交易）、卡（申卡、卡管、卡交易）及支付（消费、撤销、退款、授权），为Atome用户使用稳定币进行日常消费和交易提供便利。 |

1.5 **名词解释**

|  |  |
|:--:|:--:|
| **术语** | **说明** |
| 稳定币 | 与特定资产（如美元等法定货币）挂钩，旨在保持价值稳定的加密货币，比如USDT、USDC、WUSD、FDUSD等 |
| 钱包 | 用户存储、管理稳定币资产的虚拟容器，比如AIX Wallet |
| 卡 | 与稳定币钱包关联，用于线下消费或其他特定场景的支付工具，比如AIX Card |

# 2. 项目概述

2.1 **项目背景**

<table style="width:88%;">
<colgroup>
<col style="width: 88%" />
</colgroup>
<tbody>
<tr>
<td><table style="width:86%;">
<colgroup>
<col style="width: 85%" />
</colgroup>
<tbody>
<tr>
<td><p>传统银行转账或跨境支付存在如<strong>手续费高</strong>、<strong>结算周期长</strong>、<strong>中间环节繁琐</strong>等问题；</p>
<p>加密货币<strong>价格波动剧烈</strong>，这种不稳定性限制了其在日常交易和价值存储方面的应用；</p>
<p>加密货币市场的<strong>匿名性和监管空白</strong>，引发了一系列金融风险和安全问题；</p>
<p>因此，稳定币应运而生，它通过与法定货币（如美元）或其他稳定资产挂钩，旨在保持相对稳定的价值，为 Web3 生态系统提供稳定的价值存储和交易媒介。</p></td>
</tr>
</tbody>
</table>
<p>同步自文档: <a href="https://advancegroup.sg.larksuite.com/docx/S9NqdpeEToPG19xpFyAlgcxmgbb#GX3SdAZkWsxw2mbM7xUlmyswg0f">https://advancegroup.sg.larksuite.com/docx/S9NqdpeEToPG19xpFyAlgcxmgbb#GX3SdAZkWsxw2mbM7xUlmyswg0f</a></p></td>
</tr>
</tbody>
</table>

2.2 **项目目标**

<table style="width:88%;">
<colgroup>
<col style="width: 88%" />
</colgroup>
<tbody>
<tr>
<td><table style="width:86%;">
<colgroup>
<col style="width: 85%" />
</colgroup>
<tbody>
<tr>
<td><p><strong>AIX APP</strong>：侧重满足用户注册钱包、充值、提现、开卡、卡管及交易等场景需求；</p>
<p><strong>AIX渠道对接</strong>：侧重集成DTCPay的钱包、卡及及支付等API接口，提供底层支持能力；</p>
<p><strong>AIX运营系统</strong>：侧重日常运营、渠道营销、报表统计；</p>
<p><strong>AIX官网</strong>：侧重品牌宣传。</p></td>
</tr>
</tbody>
</table>
<p>同步自文档: <a href="https://advancegroup.sg.larksuite.com/docx/S9NqdpeEToPG19xpFyAlgcxmgbb#ZwU6d712VsepfxbDlX0lr0ifgqf">https://advancegroup.sg.larksuite.com/docx/S9NqdpeEToPG19xpFyAlgcxmgbb#ZwU6d712VsepfxbDlX0lr0ifgqf</a></p></td>
</tr>
</tbody>
</table>

2.3 **项目价值**

<table style="width:88%;">
<colgroup>
<col style="width: 88%" />
</colgroup>
<tbody>
<tr>
<td><table style="width:86%;">
<colgroup>
<col style="width: 85%" />
</colgroup>
<tbody>
<tr>
<td><p>方便持有稳定币的Atome满足MY地区用户通过AIX Card进行消费，借助现有充足的商户体系给用户消费带来便利卡需求；</p>
<p>通过OTC提升GMV，并在开卡或交易中获得分润收益；</p>
<p>支持稳定币支付，并<strong>与美元锚定的 USDT、USDC、WUSD</strong>；</p>
<p>采用先进的加密技术和安全架构，确保用户的稳定币资产安全；</p>
<p><strong>与支持Visa卡消费或收单的商家和服务提供商合作</strong>，推动稳定币在日常消费（一期支持：OTC消费、ATM或便利店取现等）场景中的应用；</p>
<p>在日常消费场景中，用户可直接用稳定币完成支付，无需繁琐的银行转账流程，无需担心汇率波动及支付手续费过高，也不受到传统支付方式的限制；</p>
<p>支持<strong>7*24h交易</strong>、<strong>实时结算到账</strong>，<strong>减低交易Gas费</strong>（约节省90%），节省用户时间成本。</p></td>
</tr>
</tbody>
</table>
<p>同步自文档: <a href="https://advancegroup.sg.larksuite.com/docx/S9NqdpeEToPG19xpFyAlgcxmgbb#Rl2cdn25Fs7dcgbPW8UlbQn3gMc">https://advancegroup.sg.larksuite.com/docx/S9NqdpeEToPG19xpFyAlgcxmgbb#Rl2cdn25Fs7dcgbPW8UlbQn3gMc</a></p></td>
</tr>
</tbody>
</table>

# 3. 全局说明

3.1 **产品架构**

**\[同步块-无权限下载此内容\]**

3.2 **功能结构**

**\[同步块-无权限下载此内容\]**

3.3 **接口范围**

|  |  |  |  |  |
|:---|:---|:---|:---|:---|
| 模块 | **接口** | 接口名称 | **接口地址** | **接口说明** |
| Main-钱包 | 查看钱包账户余额 | Get Wallet Account Balance | \[GET\] /openapi/v1/wallet/balances |  |
| Main-卡片 | 查看卡基本信息 | Get Card Basic Info | \[POST\] /openapi/v1/card/inquiry-card-info |  |
| Main-卡片-邮寄 | 卡片送达通知 | Card Delivery Notification |  |  |

3.4 **开户状态机**

<img src="/tmp/prd-batch-convert/app-home/assets/media/image1.jpeg" style="width:5.75in;height:2.07292in" />

3.5 **卡状态映射**

**\[同步块-无权限下载此内容\]**

# 4. 整体流程

4.1 **Wallet Flow**

4.1.1 **Wallet Register**

<img src="/tmp/prd-batch-convert/app-home/assets/media/image2.jpeg" style="width:5.75in;height:1.48958in" />

4.1.2 **Whitelist Address**

<img src="/tmp/prd-batch-convert/app-home/assets/media/image3.jpeg" style="width:5.75in;height:1.77083in" />

4.1.3 **Wallet PayIn**

<img src="/tmp/prd-batch-convert/app-home/assets/media/image4.jpeg" style="width:5.75in;height:1.52083in" />

4.1.4 **Wallet Pay Out**

<img src="/tmp/prd-batch-convert/app-home/assets/media/image5.jpeg" style="width:5.75in;height:1.73958in" />

4.1.5 **Get Balance**

<img src="/tmp/prd-batch-convert/app-home/assets/media/image6.jpeg" style="width:5.75in;height:0.40625in" />

4.1.6 **Get Wallet Balance**

<img src="/tmp/prd-batch-convert/app-home/assets/media/image7.jpeg" style="width:5.75in;height:0.40625in" />

4.1.7 **Exchange（同钱包内不同币种）**

<img src="/tmp/prd-batch-convert/app-home/assets/media/image8.jpeg" style="width:5.75in;height:0.65625in" />

4.1.8 **Transfer（不同DTC账户之间同币种）**

<img src="/tmp/prd-batch-convert/app-home/assets/media/image9.jpeg" style="width:5.75in;height:0.65625in" />

4.1.9 **Get Wallet Transaction**

<img src="/tmp/prd-batch-convert/app-home/assets/media/image10.jpeg" style="width:5.75in;height:0.40625in" />

4.2 **Card Flow**

4.2.1 **Card Issue & Bind**

<img src="/tmp/prd-batch-convert/app-home/assets/media/image11.jpeg" style="width:5.75in;height:1.73958in" />

4.2.2 **Card Activation**

<img src="/tmp/prd-batch-convert/app-home/assets/media/image12.jpeg" style="width:5.75in;height:0.65625in" />

4.2.3 **Set Pin**

<img src="/tmp/prd-batch-convert/app-home/assets/media/image13.jpeg" style="width:5.75in;height:0.84375in" />

4.2.4 **Get Card info**

<img src="/tmp/prd-batch-convert/app-home/assets/media/image14.jpeg" style="width:5.75in;height:0.40625in" />

4.2.5 **Get Card Transaction**

<img src="/tmp/prd-batch-convert/app-home/assets/media/image15.jpeg" style="width:5.75in;height:0.40625in" />

4.2.6 **Card Transfer**

<img src="/tmp/prd-batch-convert/app-home/assets/media/image16.jpeg" style="width:5.75in;height:0.65625in" />

4.2.7 **Card Management**

<img src="/tmp/prd-batch-convert/app-home/assets/media/image17.jpeg" style="width:5.75in;height:1.52083in" />

4.3 **Payment Flow**

4.3.1 **Transaction（Auth）**

<img src="/tmp/prd-batch-convert/app-home/assets/media/image18.jpeg" style="width:5.75in;height:1.69792in" />

4.3.2 **Transaction（Unauth）**

<img src="/tmp/prd-batch-convert/app-home/assets/media/image19.jpeg" style="width:5.75in;height:1.69792in" />

4.3.3 **Refund**

<img src="/tmp/prd-batch-convert/app-home/assets/media/image20.jpeg" style="width:5.75in;height:1.77083in" />

# 5. 数据字典

5.1 **cardStatus卡状态**

# 6. AIX功能需求

6.1 **APP主页**

6.1.1 **需求背景**

<table style="width:88%;">
<colgroup>
<col style="width: 88%" />
</colgroup>
<tbody>
<tr>
<td style="text-align: left;"><p>用户对加密货币的需求呈现多元化，为提升用户一站式管理体验，需打造<strong>功能聚合、操作便捷的主页</strong>，实现稳定币资产、卡服务、邀请好友与帮助中心的直观展示与快速交互。</p>
<p>注：对于有开卡成功或在途的用户，页面展示所有已激活、已冻结、待激活、审核中的卡片。</p>
<p>对于无开卡成功或在途的用户，即未申请、申请失败展示默认申卡入口。</p></td>
</tr>
</tbody>
</table>

6.1.2 **业务流程**

6.1.3 **页面交互**

<img src="/tmp/prd-batch-convert/app-home/assets/media/image21.png" style="width:5.75in;height:4.75in" />

6.1.4 **展示逻辑**

6.1.4.1 **申卡入口展示逻辑**

**\[同步块-无权限下载此内容\]**

6.1.4.2 **当前卡片展示逻辑及操作权限**

**\[同步块-无权限下载此内容\]**

6.1.5 **功能需求**

<table style="width:89%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 20%" />
<col style="width: 46%" />
<col style="width: 12%" />
</colgroup>
<tbody>
<tr>
<td style="text-align: center;"><strong>需求</strong></td>
<td style="text-align: left;"><strong>UI或UX</strong></td>
<td style="text-align: center;"><strong>需求描述</strong></td>
<td style="text-align: center;"><strong>备注</strong></td>
</tr>
<tr>
<td style="text-align: left;"><strong>顶部操作栏</strong></td>
<td style="text-align: center;"><img src="/tmp/prd-batch-convert/app-home/assets/media/image22.png" style="width:1.14583in;height:1.47917in" /></td>
<td style="text-align: center;"><p><strong>快捷入口</strong>：</p>
<p>Profile：点击“三”进入个人中心页；</p>
<p>Gift：活动中心，点击图标进入邀请好友页Invite Friends；</p>
<p>Notice：通知：</p>
<p>有未读通知带红点</p>
<p>消息都已读则红点消失</p>
<p>点击“通知”进入通知中心。</p>
<p><strong>全局刷新</strong>：</p>
<p>用户手动下拉时，全局刷新获取最新的钱包状态、卡状态和钱包资产余额；</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Waitlist</strong></td>
<td style="text-align: center;"><img src="/tmp/prd-batch-convert/app-home/assets/media/image23.png" style="width:1.14583in;height:0.6875in" /></td>
<td style="text-align: center;"><p><strong>Waitlist展示逻辑：</strong></p>
<p>当该用户uid<strong>在waitlist清单</strong>(仅限来源渠道为APP)，将会显示该面板：</p>
<p>Title：You’re On the list!</p>
<p>Tips：Thank you for your interest!</p>
<p>Describe：AIX is expanding to more regions. We’ll notify you as soon as service becomes available in your country.</p>
<p>注：这类用户是没法操作申请开通钱包；</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><strong>钱包区域</strong></td>
<td style="text-align: left;"><p>未申请开通钱包</p>
<p><img src="/tmp/prd-batch-convert/app-home/assets/media/image24.png" style="width:1.13542in;height:1.16667in" /></p>
<p><img src="/tmp/prd-batch-convert/app-home/assets/media/image25.png" style="width:1.14583in;height:1.51042in" /></p>
<p>开通钱包审核中</p>
<p><img src="/tmp/prd-batch-convert/app-home/assets/media/image26.png" style="width:1.14583in;height:1.32292in" /></p>
<p>开通钱包审核失败</p>
<p><img src="/tmp/prd-batch-convert/app-home/assets/media/image27.png" style="width:1.14583in;height:1.53125in" /></p>
<p>开通钱包审核拒绝</p>
<p><img src="/tmp/prd-batch-convert/app-home/assets/media/image28.png" style="width:1.14583in;height:0.83333in" /></p>
<p>开通钱包审核通过</p>
<p><img src="/tmp/prd-batch-convert/app-home/assets/media/image29.png" style="width:1.14583in;height:0.67708in" /></p>
<p><img src="/tmp/prd-batch-convert/app-home/assets/media/image30.png" style="width:1.14583in;height:0.67708in" /></p></td>
<td style="text-align: center;"><p><strong>前置条件：</strong></p>
<p>已登录AIX APP</p>
<p>该用户uid<strong>不在waitlist清单</strong>(仅限来源渠道为APP)；</p>
<p>读取最近一笔钱包开通记录进行判断；</p>
<p><strong>未申请开通钱包：</strong></p>
<p>未申请开通钱包（无开户记录），或进入KYC页面但未完成身份验证，即<strong>KYC状态为Pending时</strong>，会显示该钱包面板；</p>
<p>当KYC为Pending时，会显示Tips：（注：KYC为空即无开户记录时，不会有Tips）</p>
<p>Tips title：Identity verification incomplete</p>
<p>Tips details：You’ve completed part of the identity verification. Please finish the remaining steps to continue.</p>
<p>Text：“You're almost there! ”</p>
<p>Describe：“You're ready to join the stablecoin world! ”；</p>
<p>进度条展示逻辑：（KYC状态为Pending时要做以下判断来显示剩余步骤）</p>
<p>① 如果passport/face/poa没有一项是<del>认证中或</del>认证成功，显示“3 Step remaining”</p>
<p>② 如果passport/face/poa有一项是<del>认证中或</del>认证成功，显示“2 Step remaining”</p>
<p>③ 如果passport/face/poa有2项是<del>认证中或</del>认证成功，显示“1 Step remaining”</p>
<p>poa:以用户提交成功节点为判断依据。</p>
<p>Activate wallet：开通钱包，点击 “Activate wallet”进入钱包开通页面；Button</p>
<p>如果用户去操作了开通钱包并走完了KYC，在KYC结果页返回首页时，钱包区域要进行系统局部静默刷新，以便获取最新钱包状态；</p>
<p><strong>开通钱包审核中：</strong></p>
<p>已申请开通钱包但DTC审核中，即KYC状态为Under Review时，会显示该钱包面板；</p>
<p>当KYC为Under Review时，会显示Tips：</p>
<p>Tips title：Verification is under reviewing</p>
<p>Tips details：Your identity is being confirmed. We'll notify you the moment your account is verified</p>
<p>Text：“You're almost there! ”</p>
<p>Describe：“You're ready to join the stablecoin world! ”；</p>
<p>进度条展示逻辑：</p>
<p>④ KYC状态为Under Review，显示“3 Steps Finished”</p>
<p><strong>静默刷新</strong>：如果当前钱包状态是审核中，用户进入该页面时，钱包区域要进行系统局部静默刷新，以便获取最新钱包状态；</p>
<p><strong>开通钱包审核失败：</strong></p>
<p>已申请开通钱包但DTC审核失败，即KYC状态为Failed，会显示该钱包面板；</p>
<p>当KYC为Failed时，会显示Tips：</p>
<p>Tips title：Verification failed</p>
<p>Tips details：读取后端映射失败原因</p>
<p>后端passport失败：那么展示<a href="https://advancegroup.sg.larksuite.com/wiki/ISjLwCKi5itjNXkpCLllQD5Qgle#share-HXrzdfM6aoOOnsxJdUils4XWgMe">Document Verification错误码</a>映射中的映射前端提示文案</p>
<p>后端face失败：那么展示<a href="https://advancegroup.sg.larksuite.com/wiki/ISjLwCKi5itjNXkpCLllQD5Qgle#share-P57KdHhAaoIkqqxiTr6lHCFhgPh">Face Comparison API错误码</a>映射中的映射前端提示文案</p>
<p>两者均失败，优先展示passport失败原因</p>
<p>后端POA失败：那么展示<a href="https://advancegroup.sg.larksuite.com/wiki/ISjLwCKi5itjNXkpCLllQD5Qgle#share-KgNydZw2zohnDLxTnCMl1MDrgPg">POA error code</a>映射中的映射前端提示文案</p>
<p>兜底文案：The verification was not successful. Please review your information and try again.</p>
<p>Text：“You're almost there! ”</p>
<p>Describe：“You're ready to join the stablecoin world! ”；</p>
<p>进度条展示逻辑：（KYC状态为Failed时要做以下判断来显示剩余步骤）</p>
<p>① 如果passport/face/poa没有一项是认证中或认证成功，显示“3 Step remaining”</p>
<p>② 如果passport/face/poa有一项是认证中或认证成功，显示“2 Step remaining”</p>
<p>③ 如果passport/face/poa有2项是认证中或认证成功，显示“1 Step remaining”</p>
<p>Reactivate Now：重新激活钱包Button</p>
<p>任一验证项失败(passport/face/poa)的用户可以重新开户，点击 “Reactivate Now”进入钱包开通页面；</p>
<p><strong>开通钱包审核拒绝：</strong></p>
<p>已申请开通钱包但DTC审核拒绝，即KYC状态为Rejected，会显示该钱包面板；</p>
<p>Title：Verification rejected</p>
<p>Describe：“Due to violation of high-risk rules, account opening is prohibited. For assistance, please contact support@aixpay.co”；（注：MVP邮箱做不同样式展示）</p>
<p>注：因某些风险被DTC审核拒绝的用户，会拦截开户且禁止再次提交（隐藏激活钱包入口）</p>
<p><strong>开通钱包审核通过：</strong></p>
<p>已申请开通钱包但DTC审核通过，即KYC状态为Approved时，会显示该钱包面板；</p>
<p>Total Asset：总资产：</p>
<p>默认USD，显示币种符号（$），如：$ 8.88；</p>
<p>用户进入首页时，后端调用接口【 [GET] /openapi/v1/wallet/balances】获取全量币种最新钱包账户余额，并筛选稳定币【USDC、USDT、WUSD、FDUSD】的余额；</p>
<p>根据用户持有的USDT、USDC、WUSD、FDUSD及当前默认法币USD，分别调用汇率接口【 /openapi/v1/otc/get-otc-rate】获得Rate1、Rate2、Rate3、Rate4；</p>
<p>Total Asset（当前法币预估资产）=USDT余额*Rate1 + USDC余额*Rate2 + WUSD余额*Rate3+ FDUSD余额*Rate4，试算结果按四舍五入处理并保留2位小数；</p>
<p>查看钱包，点击“&gt;”进入钱包首页Wallet</p>
<p>Crypto：加密币及图标：（仅做展示，不可点击）</p>
<p>USDC</p>
<p>USDT</p>
<p>WUSD</p>
<p>FDUSD</p>
<p>按照USDC、USDT、WUSD、FDUSD固定排序（暂不按余额做降序），后端可配置要展示的币种可配置</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: center;"><strong>申卡入口</strong></td>
<td style="text-align: left;"><p>Banner入口</p>
<p><img src="/tmp/prd-batch-convert/app-home/assets/media/image31.png" style="width:1.14583in;height:0.63542in" /></p>
<p>卡片入口</p>
<p><img src="/tmp/prd-batch-convert/app-home/assets/media/image32.png" style="width:1.14583in;height:0.60417in" /></p>
<p>常驻入口①</p>
<p>有申卡入口</p>
<p><img src="/tmp/prd-batch-convert/app-home/assets/media/image33.jpeg" style="width:1.14583in;height:0.58333in" /></p>
<p>常驻入口②</p>
<p>有申卡入口但不可点击（申卡小于5张且有审核中）</p>
<p><img src="/tmp/prd-batch-convert/app-home/assets/media/image34.jpeg" style="width:1.14583in;height:0.63542in" /></p>
<p>常驻入口③</p>
<p>无申卡入口（申卡5张）</p>
<p><img src="/tmp/prd-batch-convert/app-home/assets/media/image35.png" style="width:1.14583in;height:0.6875in" /></p></td>
<td style="text-align: left;"><p><strong>前置条件：</strong></p>
<p>已开通钱包且审核通过（即KYC状态为Approved）；</p>
<p><strong>展示逻辑</strong></p>
<p>用户申卡张数限制5张（待激活、已激活、审核中、已冻结之和）可配置</p>
<p>当前用户所有已激活、已冻结、待激活、审核中的卡之和≥5时，不显示申卡入口；</p>
<p>当前用户所有已激活、已冻结、待激活、审核中的卡之和＜5时，且<strong>有审核中</strong>的卡，申卡入口置灰不可点击；</p>
<p>当前用户所有已激活、已冻结、待激活、审核中的卡之和＜5时，且<strong>无审核中</strong>的卡，申卡入口高亮可点击；</p>
<p><strong>Banner申卡入口</strong>：</p>
<p>当前用户所有卡状态：待激活、已激活、审核中、已冻结之和X＜5张且无审核中的卡，会显示Banner入口：</p>
<p>Banner由运营自行配置（如图1）；</p>
<p>点击“Apply Now”校验用户是否首次申卡：</p>
<p>如果是，跳转到新用户选择卡片页面Select plan；</p>
<p>否则，跳转到老用户选择卡片页面Pick your card；</p>
<p><strong>卡片申卡入口</strong>：</p>
<p>当前用户所有卡状态：待激活、已激活、审核中、已冻结之和X=0张，即未申请、申请失败（注：后续会通过消息通知或直接弹窗告知申卡失败），会显示卡片入口（如图2）；</p>
<p>标题：“Get Your AlX card ”</p>
<p>描述：“Start your spending brand new journey today!”；</p>
<p>点击“Get card”，校验用户是否首次申卡：</p>
<p>如果是，跳转到新用户选择卡片页面Select plan；</p>
<p>否则，跳转到老用户选择卡片页面Pick your card；</p>
<p><strong>常驻申卡入口</strong>：</p>
<p>当前用户所有卡状态：待激活、已激活、审核中、已冻结之和1 ≤ X &lt; 5张且无审核中的卡，会显示可点击的申卡入口（常驻入口示例①）；</p>
<p>点击高亮“⊕”，直接跳转到老用户选择卡片页面Pick your card；</p>
<p>当前用户所有卡状态：待激活、已激活、审核中、已冻结之和1 ≤ X &lt; 5张且有审核中的卡，会显示不点击的申卡入口（常驻入口示例①）；</p>
<p>点击置灰“⊕”，会提示“You have a card that is currently under review and cannot apply for another one simultaneously.”</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><strong>卡管入口（已申请卡片展示）</strong></td>
<td style="text-align: left;"><p>审核中</p>
<p><img src="/tmp/prd-batch-convert/app-home/assets/media/image36.png" style="width:1.14583in;height:0.61458in" /></p>
<p>待激活</p>
<p><img src="/tmp/prd-batch-convert/app-home/assets/media/image37.png" style="width:1.14583in;height:0.61458in" /></p>
<p>已激活未设置PIN</p>
<p><img src="/tmp/prd-batch-convert/app-home/assets/media/image38.png" style="width:1.14583in;height:0.61458in" /></p>
<p>已激活已设置PIN</p>
<p><img src="/tmp/prd-batch-convert/app-home/assets/media/image39.png" style="width:1.13542in;height:0.625in" /></p>
<p>已冻结</p>
<p><img src="/tmp/prd-batch-convert/app-home/assets/media/image40.png" style="width:1.13542in;height:0.625in" /></p></td>
<td style="text-align: left;"><p><strong>当前卡片展示逻辑：（无修改PIN）</strong></p>
<p>Title：Cards</p>
<p>点击“&gt;”跳转到卡管首页My Card；</p>
<p>Card Type：Virtual Card、Physical Card；</p>
<p>Card Number：显示脱敏卡号后四位，如果是审核中的没有卡号就显示“······”</p>
<p>静默刷新：如果当前用户卡状态有“审核中”或“待激活”的，卡片区域要进行系统局部静默刷新，以便获取最新卡状态；</p>
<p>如果当前卡状态是“审核中”，即卡状态为Processing时，会显示该卡片：</p>
<p>点击后跳转到当前卡片（审核中）页面My Card</p>
<p>如果当前卡状态是“待激活”，即卡状态为Pending activation时，会显示该卡片</p>
<p>点击后跳转到当前卡片（待激活）页面My Card</p>
<p>如果当前卡状态是“已激活”即卡状态为Active且未设置PIN时，会显示该卡片；</p>
<p>点击后跳转到当前卡片首页My Card；</p>
<p>如果当前卡状态是“已激活”即卡状态为Active且已设置PIN时，会显示该卡片；</p>
<p>点击后跳转到当前卡片首页Card；</p>
<p>如果当前卡状态是“已冻结”即卡状态为Frozen时，会显示该卡片；</p>
<p>点击后跳转到当前卡片首页Card；</p>
<p><strong>多张卡片展示逻辑：</strong></p>
<p>如果当前用户申请了多张卡，且申卡张数＜5张（待激活、已激活、审核中、已冻结之和），按照申请时间降序展示所有卡片，最右边显示申卡入口“+”</p>
<p>如果当前用户申请了多张卡，且申卡张数＝5张（待激活、已激活、审核中、已冻结之和），按照申请时间降序展示所有卡片，屏蔽申卡入口“+”</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Banner</strong></td>
<td style="text-align: center;"><img src="/tmp/prd-batch-convert/app-home/assets/media/image41.png" style="width:1.14583in;height:0.59375in" /></td>
<td style="text-align: center;">首页固定一个Banner由@Bing Han 韩冰负责，具体需求看：<a href="https://advancegroup.sg.larksuite.com/wiki/LPahw9N9minPZWkwthclU5l6grH">[2025-11-27] AIX+PopUp+banner等能力接入【首页+MGM页面】</a></td>
<td style="text-align: left;">韩冰的需求</td>
</tr>
<tr>
<td style="text-align: left;"><strong>帮助中心区</strong></td>
<td style="text-align: center;"><img src="/tmp/prd-batch-convert/app-home/assets/media/image42.png" style="width:1.14583in;height:1.73958in" /></td>
<td style="text-align: center;"><p>Get Help问题列表：</p>
<p><del>FAQ暂未做OBoss可视化编辑Dashboard，先预设到数据库（<strong>问题 ID、标题、描述、关联场景、类型、超链接、创建时间</strong>）；</del></p>
<p><del>展示最新3条，根据关键场景“Home”、类型“Get Help”和最近时间筛选FAQ并展示给用户；</del></p>
<p><del>QA放在后端配置，先预设到数据库，无可视化编辑Dashboard；可配置</del></p>
<p>QA默认只显示问题折叠答案，点击任意一个问题只显示当前这条的答案；</p>
<p>FAQ默认只显示问题折叠答案，点击任意一个问题只显示当前这条的答案；</p>
<p>Title<strong>：Get Help</strong></p>
<p>body：配置到服务端的配置文件中，后续可能更改。</p>
<p><strong>What types of cards does AIX offer?</strong></p>
<blockquote>
<p>AIX offers two types of cards: a Physical Card and a Virtual Card. Each card has a unique number, works like a debit card, and lets you spend directly from your stable coin balance. Your card can be added to Google Pay or Apple Pay for easy tap-to-pay transactions.</p>
</blockquote>
<p><strong>Who is eligible to open an AIX account?</strong></p>
<p>You're eligible to open an AIX account when you can provide a passport and a proof of address document that matches your country of residence</p>
<p><strong>What documents do I need to provide when applying for AIX card?</strong></p>
<blockquote>
<p>To get your AIX card, you’ll need to submit a few documents as part of the onboarding and KYC process. Please prepare the following:</p>
<p>Required documents</p>
</blockquote>
<p>A valid passport with a clear photo.</p>
<p>Proof of residential address dated within the last 3 months (e.g., utility bill, telecom bill, or tax statement).</p>
<p>Any additional verification steps requested by AIX, such as liveness checks, face matching, or address verification.</p>
<blockquote>
<p>Additional notes</p>
</blockquote>
<p>These are the same documents used to open a dtcpay account.</p>
<p>Your account must be fully verified and in good standing to issue a physical or virtual card.</p>
<p>Make sure your documents are clear and readable to avoid delays.</p>
<p>more&gt;：点击“more&gt;”可查看更多FAQ，点击跳转至zendesk链接，链接由@Bing Han 韩冰提供，配置到服务端。（示例：<a href="https://aixpay.zendesk.com/hc/en-gb/sections/15087280899855-Card-Delivery-Activation">https://aixpay.zendesk.com/hc/en-gb/sections/15087280899855-Card-Delivery-Activation</a>）</p></td>
<td style="text-align: left;"><p>FAQ配置：<a href="https://advancegroup.sg.larksuite.com/docx/OlWEdynrboay1QxcpfhlYbJtgZg">AIX APP V1.0 【FAQ】</a></p>
<p>常见QA list<a href="https://advancegroup.sg.larksuite.com/sheets/PSJvsqPZOh9nTAtIueql2s94g8b?preview_comment_id=7577601505826524896">AIX Phase 1 FAQ</a> 由业务人员提供 @Reinaldo Gani</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>底部操作栏</strong></td>
<td style="text-align: center;"><p><img src="/tmp/prd-batch-convert/app-home/assets/media/image43.png" style="width:1.14583in;height:0.38542in" /></p>
<p><img src="/tmp/prd-batch-convert/app-home/assets/media/image44.png" style="width:1.14583in;height:2.48958in" /></p></td>
<td style="text-align: center;"><p><strong>前置条件</strong></p>
<p>已完成开通钱包的用户才显示核心交易操作入口</p>
<p><strong>底部操作栏</strong>：</p>
<p>Deposit：充值，点击“Deposit”进入充值的选择钱包页Select Wallet</p>
<p>Swap：兑换，点击“Swap”进入兑换页Swap</p>
<p>默认不显示功能弹出层；</p>
<p>点击“∧”拉起功能弹出层；</p>
<p>点击“∨”折叠功能弹出层；</p>
<p>Send：转账，点击“Send”进入钱包转账页Send；</p>
<p>Transaction：交易，点击“Transaction”进入全量交易页Transaction；</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><strong>首页弹窗</strong></td>
<td style="text-align: center;"><img src="/tmp/prd-batch-convert/app-home/assets/media/image45.png" style="width:1.14583in;height:1.67708in" /></td>
<td style="text-align: left;">首页弹窗，由@Bing Han 韩冰负责，具体需求看：<a href="https://advancegroup.sg.larksuite.com/wiki/LPahw9N9minPZWkwthclU5l6grH">[2025-11-27] AIX+PopUp+banner等能力接入【首页+MGM页面】</a></td>
<td style="text-align: left;">韩冰的需求</td>
</tr>
</tbody>
</table>

# 7. DTC渠道接口需求

7.1 **获取指定币种钱包余额Get Balance**

7.1.1 **接口说明**

此接口用于获取特定货币钱包的余额和场外交易限额。

7.1.2 **接口地址**

\[GET\] /openapi/v1/wallet/balance/{currency}

7.1.3 **接口时序**

<img src="/tmp/prd-batch-convert/app-home/assets/media/image46.jpeg" style="width:5.75in;height:3.44792in" />

7.1.4 **接口请求**

7.1.5 **接口响应**

7.1.6 **错误码**

注：如果DTCPay接口返回当前错误码之外的其他错误，直接lark报警通知，以便产品和渠道确定后续的错误处理。

7.2 **获取全量币种钱包余额Get Wallet Account Balance**

7.2.1 **接口说明**

此接口用于查询经过身份验证的客户所有货币的所有钱包账户余额。

7.2.2 **接口地址**

\[GET\] /openapi/v1/wallet/balances

7.2.3 **接口时序**

<img src="/tmp/prd-batch-convert/app-home/assets/media/image47.jpeg" style="width:5.75in;height:3.44792in" />

7.2.4 **接口请求**

注：请求参数包含在请求头会提交MasterAccount或SubAccount，无其他请求字段。

7.2.5 **接口响应**

7.2.6 **错误码**

注：如果DTCPay接口返回当前错误码之外的其他错误，直接lark报警通知，以便产品和渠道确定后续的错误处理。

# 8. 非功能需求

# 9. 附录

9.1 **相关文档**

DTC接口文档 https://advancegroup.sg.larksuite.com/drive/folder/Q0dHfSY5ulRFR2dtJ7ullLpgg5g

9.2 **需求评审**

https://advancegroup.sg.larksuite.com/minutes/obsgh7271uikrh7hg3p435ix
