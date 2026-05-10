# AIX Wallet V1.0【Asset】

# 1. 引言

1.1 **需求索引**

**\[同步块-无权限下载此内容\]**

1.2 **修订记录**

|        |      |                               |                    |
|:-------|:-----|:------------------------------|:-------------------|
| 日期   | 版本 | 说明                          | 作者               |
| Jan 27 | V1.1 | MVP不做单币种首页，后续再迭代 | @Xuemin Zhu 朱学敏 |

# 2. 全局说明

2.1 **交易说明**

<table style="width:88%;">
<colgroup>
<col style="width: 88%" />
</colgroup>
<tbody>
<tr>
<td><p>当前钱包仅做稳定币业务：FDUSD,USDC,USDT,WUSD；</p>
<p>开通钱包的用户，可以查看钱包资产、单币种余额及交易明细；</p></td>
</tr>
</tbody>
</table>

2.2 **接口范围**

|  |  |  |  |
|:---|:---|:---|:---|
| **接口** | 接口名称 | **接口地址** | **接口说明** |
| **查看全量币种余额** | Get Wallet Account Balance | \[GET\] /openapi/v1/wallet/balances |  |
| **查询单币种余额** | Get Balance | \[GET\] /openapi/v1/wallet/balance/{currency} |  |

# 3. 数据字典

# 4. AIX前端功能需求

4.1 **钱包首页 My Assets**

4.1.1 **需求背景**

|  |
|:---|
| 对于已经开通AIX钱包的用户，可以查看总资产、交易记录，并支持用户进行充值、转账、兑换等操作 |

4.1.2 **业务流程**

4.1.3 **页面交互**

<img src="assets/media/image1.png" style="width:5.75in;height:5.28125in" />

4.1.4 **功能需求**

<table style="width:89%;">
<colgroup>
<col style="width: 8%" />
<col style="width: 19%" />
<col style="width: 44%" />
<col style="width: 15%" />
</colgroup>
<tbody>
<tr>
<td style="text-align: center;"><strong>需求</strong></td>
<td style="text-align: center;"><strong>UI或UE</strong></td>
<td style="text-align: center;"><strong>页面说明</strong></td>
<td style="text-align: left;"><strong>备注</strong></td>
</tr>
<tr>
<td style="text-align: left;">钱包首页</td>
<td style="text-align: center;"><p><img src="assets/media/image2.png" style="width:1.125in;height:3.09375in" /></p>
<p><img src="assets/media/image3.png" style="width:1.125in;height:3.07292in" /></p>
<p><img src="assets/media/image4.png" style="width:1.11458in;height:3.625in" /></p>
<p><img src="assets/media/image5.png" style="width:1.125in;height:3.5in" /></p></td>
<td style="text-align: center;"><p><strong>顶部导航栏：</strong></p>
<p>标题：“MY Assets”</p>
<p>返回：点击 “←”可回到上一级页面；</p>
<p>眼睛：点击“眼睛”后可以全局显示或隐藏总资产和稳定币余额；</p>
<p><strong>全局刷新：</strong></p>
<p>用户进入该页面时，静默刷新获取最新的钱包资产、稳定币余额和最近交易记录；</p>
<p><strong>资产区：</strong></p>
<p>Total Asset：总资产：</p>
<p>Currency：默认显示括号内的USD（$）;</p>
<p>根据默认法币USD试算对应的金额，保留2位小数：如，8.88 USD</p>
<p><strong>Total Asset（当前法币预估资产）=USDT余额*Rate1 + USDC余额*Rate2 + WUSD余额*Rate3+ FDUSD余额*Rate4，</strong>试算结果按各个稳定币四舍五入处理并保留2位小数再相加；</p>
<p>根据用户持有的USDT、USDC、WUSD、FDUSD及当前默认法币USD，分别调用汇率接口【 /openapi/v1/otc/get-otc-rate】获得Rate1、Rate2、Rate3、Rate4</p>
<p>如果任一汇率获取异常，直接提示“Network abnormality. Please try again later.”</p>
<p>用户访问该页面时，要获取一次最新汇率（DTC汇率24h有效）；</p>
<p><strong>快捷功能入口：</strong></p>
<p>Deposit：加密币充值，点击“Deposit”进入充值页面Deposit；</p>
<p>Swap：兑换加密币，点击“Swap”进入兑换页面Swap</p>
<p>Send：P2P转账，点击“Send”进入转账页面Send；</p>
<p><strong>稳定币列表：</strong></p>
<p>用户进入钱包首页时，后端调用接口【 [GET] /openapi/v1/wallet/balances】获取全量币种最新钱包账户余额，并筛选稳定币【USDC、USDT、WUSD、FDUSD】的余额并展示给用户；</p>
<p>Title：“Stablecoin”</p>
<p>Currency：币种及图标：可配置</p>
<p>USDC</p>
<p>USDT</p>
<p>WUSD</p>
<p>FDUSD</p>
<p>按照USDC、USDT、WUSD、FDUSD固定排序（暂不按余额做降序），后端可配置要展示的币种可配置</p>
<p>点击“&gt;”跳转到当前币种首页；</p>
<p>Crypto Balance：当前币种的加密币余额，金额隐藏时显示“****”；</p>
<p>Fiat Balance：当前币种的法币余额：</p>
<p>Currency：默认显示USD</p>
<p>根据用户持有的USDT、USDC、WUSD、FDUSD及当前默认的法币USD，分别调用汇率接口【 /openapi/v1/otc/get-otc-rate】获得Rate；</p>
<p>Fiat Balance = Crypto Balance * Rate，试算结果按四舍五入处理并保留2位小数；</p>
<p>金额隐藏时显示“****”；</p>
<p><strong>最近交易展示：</strong></p>
<p>钱包资产页的最近钱包交易记录是聚合（<strong>加密币交易、兑换交易</strong>），后端调用加密币交易接口【/openapi/v1/crypto-txn/search】、OTC兑换记录接口【/openapi/v1/otc/search】查询交易记录，并按交易类型进行数据过滤后展示给用户：</p>
<p>① 加密币交易仅展示原始交易类型为【DEPOSIT】【TRANSFER_IN】【TRANSFER_OUT】【CARD_FEE_DEBIT】【CARD_FEE_REFUND】的记录给用户；</p>
<p>② 加密币兑换的展示全部记录给用户；</p>
<p>展示当前用户近<strong>近1年</strong>钱包交易（加密币交易、兑换交易）的最近6条记录给用户：</p>
<p>如果条数X为0就占位符显示“No transaction data”</p>
<p>如果条数1≤X＜6，就显示对应条数，页面自适应长度；</p>
<p>按照交易时间降序排列展示；</p>
<p>用户进入钱包首页时，静默拉取最新的交易记录；</p>
<p>Title：Recent transaction</p>
<p>点击“View all”跳转到全量交易记录页面Transactions；</p>
<p>Type：交易类型及对应图标可配置</p>
<p>Crypto Deposit加密币充值</p>
<p>Receive转入</p>
<p>Send转出</p>
<p>Swap兑换</p>
<p>Card Application 申卡扣费</p>
<p>Card Cancel申卡退费</p>
<p>Status：加密币交易状态可配置</p>
<p>Pending</p>
<p>Success</p>
<p>Refunded</p>
<p>Declined</p>
<p>Under Review</p>
<p>Cancelled</p>
<p><strong>单笔加密币交易记录展示逻辑：</strong></p>
<p>Type：交易类型及对应图标（对客显示为交易名称）</p>
<p>Crypto Deposit</p>
<p>Receive</p>
<p>Send</p>
<p>Card Application</p>
<p>Card Cancel</p>
<p>Indicator：交易方向：入金+、出金-：</p>
<p>Crypto Deposit加密币充值【+】</p>
<p>Receive转入【+】</p>
<p>Send转出【-】</p>
<p>Card Application 【-】</p>
<p>Card Cancel【+】</p>
<p>Amount&amp;Currency：交易金额及币种</p>
<p>Transaction time：交易时间</p>
<p>格式：年-月-日 时:分:秒</p>
<p>Status：加密币交易状态</p>
<p>Pending</p>
<p>Success</p>
<p>Refunded</p>
<p>Declined</p>
<p>Under Review</p>
<p>Cancelled</p>
<p><strong>单笔兑换交易记录展示逻辑：（不展示交易状态）</strong></p>
<p>Type：交易类型及对应图标（对客显示为交易名称）</p>
<p>Swap兑换</p>
<p>Indicator：交易方向：入金+、出金-：</p>
<p>Buy currency兑换买入【+】</p>
<p>Sell currency兑换卖出【-】</p>
<p>Buy amount&amp;currency：买入金额及币种</p>
<p>Sell amount&amp;currency：卖出金额及币种</p>
<p>Transaction time：交易时间</p></td>
<td style="text-align: left;">注：因合规问题充值用户无法正常操作Withdraw，只能按退款走人工处理，故先隐藏Withdraw入口，</td>
</tr>
</tbody>
</table>

# 5. DTC渠道接口需求

5.1 **获取指定币种钱包余额Get Balance**

5.1.1 **接口说明**

此接口用于获取特定货币钱包的余额和场外交易限额。

5.1.2 **接口地址**

\[GET\] /openapi/v1/wallet/balance/{currency}

5.1.3 **接口时序**

<img src="assets/media/image6.jpeg" style="width:5.75in;height:3.44792in" />

5.1.4 **接口请求**

5.1.5 **接口响应**

5.1.6 **错误码**

注：如果DTCPay接口返回当前错误码之外的其他错误，直接lark报警通知，以便产品和渠道确定后续的错误处理。

5.2 **获取全量币种钱包余额Get Wallet Account Balance**

5.2.1 **接口说明**

此接口用于查询经过身份验证的客户所有货币的所有钱包账户余额。

5.2.2 **接口地址**

\[GET\] /openapi/v1/wallet/balances

5.2.3 **接口时序**

<img src="assets/media/image7.jpeg" style="width:5.75in;height:3.44792in" />

5.2.4 **接口请求**

注：请求参数包含在请求头会提交MasterAccount或SubAccount，无其他请求字段。

5.2.5 **接口响应**

5.2.6 **错误码**

注：如果DTCPay接口返回当前错误码之外的其他错误，直接lark报警通知，以便产品和渠道确定后续的错误处理。

# 6. 非功能需求

# 7. 附录

7.1 **相关文档**

DTC接口文档 https://advancegroup.sg.larksuite.com/drive/folder/Q0dHfSY5ulRFR2dtJ7ullLpgg5g

7.2 **需求评审**

https://advancegroup.sg.larksuite.com/minutes/obsgh7271uikrh7hg3p435ix
