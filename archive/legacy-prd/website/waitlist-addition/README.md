# \[2026-01-04\]AIX官网增加waitlist

**目录**

**\[同步块-无权限下载此内容\]**

# 1. 需求背景

目前我们已上线了仅用于投放的waitlist链接。随着官网的迭代升级，也希望可以在官网增加一个waitlist收集入口。待APP上线后再引导用户下载app。

waitlist的目标是：

为不在支持国家范围内的用户提供**加入候补名单**的入口；

收集用户的**邮箱地址（Email）与意向国家（Country）**，以便后续开放时可通知用户；

建立一套候补名单数据库，用于评估市场潜力、用户兴趣分布及后续拓展优先级。

详见：[\[BRD\] Aix Waitlist](https://advancegroup.sg.larksuite.com/wiki/FKtRwpAO8iD6tDkSeLTlioIVgFc)

# 2. 需求概况

<table style="width:89%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 76%" />
</colgroup>
<tbody>
<tr>
<td style="text-align: left;"><strong>类型</strong></td>
<td style="text-align: left;">明细</td>
</tr>
<tr>
<td style="text-align: left;">PM</td>
<td style="text-align: left;">@Bing Han 韩冰</td>
</tr>
<tr>
<td style="text-align: left;">需求方</td>
<td style="text-align: left;">@Teck Soon Ng Aloysius (TS)</td>
</tr>
<tr>
<td style="text-align: left;">UI/UX</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">前端</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">服务端</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">测试</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Figma</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">BRD</td>
<td style="text-align: left;"><a href="https://advancegroup.sg.larksuite.com/wiki/FKtRwpAO8iD6tDkSeLTlioIVgFc">[BRD] Aix Waitlist</a></td>
</tr>
<tr>
<td style="text-align: left;">期望上线时间</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Meggle</td>
<td style="text-align: left;"><a href="https://project.larksuite.com/atome_agile/story/detail/9583833?parentUrl=/atome_agile/story/homepage&amp;openScene=1">[Feature]官网增加waitlist</a></td>
</tr>
<tr>
<td style="text-align: left;">关联域PRD</td>
<td style="text-align: left;"><p><a href="https://advancegroup.sg.larksuite.com/wiki/NQ2EwGQ35iK5VPkq3AVlWrflgod">[2025-11-20]AIX-外部投放waitlist</a></p>
<p><a href="https://advancegroup.sg.larksuite.com/wiki/JMRmw7tT9iBUntknqVXlT9aNgHc">[2025-11-05]AIX-官网需求一期</a></p>
<p><a href="https://advancegroup.sg.larksuite.com/docx/ZUF6d6fNiouqB5xoxUSlCcGggGh">[2025-12-17]AIX-官网走查-优化版本</a></p></td>
</tr>
<tr>
<td style="text-align: left;">历史需求PRD</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">技术方案</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">支持语言</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">设备适配</td>
<td style="text-align: left;"><p>PC端</p>
<p>移动端直接弹窗提示用户通过电脑访问。</p></td>
</tr>
<tr>
<td style="text-align: left;">链接</td>
<td style="text-align: left;">官网链接：https://www.aixpay.co/</td>
</tr>
<tr>
<td style="text-align: left;">文案review</td>
<td style="text-align: left;"><a href="https://advancegroup.sg.larksuite.com/docx/TGqPds0LroPmdmxYqCLls3t9gag">AIX waitlist copy draft</a></td>
</tr>
<tr>
<td style="text-align: left;">Others</td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

# 3. Demo

# 4. 需求描述

<table style="width:89%;">
<colgroup>
<col style="width: 23%" />
<col style="width: 47%" />
<col style="width: 17%" />
</colgroup>
<tbody>
<tr>
<td style="text-align: left;"><strong>页面</strong></td>
<td style="text-align: left;"><strong>具体描述</strong></td>
<td style="text-align: left;">越南语版本</td>
</tr>
<tr>
<td style="text-align: center;"><img src="assets/media/image1.jpg" style="width:1.36458in;height:1.77083in" /></td>
<td style="text-align: left;"><p>标题：AIX官网+waitlist</p>
<p>显示逻辑：</p>
<p>官网的配置文件增加一个开关，可以随时控制官网中waitlist的入口的显示/隐藏。</p>
<p>若显示的话，可首屏吸引固定显示。在页面最底部注意留出间距，以保证页面底部的信息显示完整。</p>
<p>数据落库：</p>
<p>针对已提交预约的用户对应的邮箱、国家、most matters 、来源（外部投放、APP）、提交时间、渠道值、设备指纹ID等信息需要落库落表存储，并推送至数仓。以便运营同学分析。</p>
<p>若用户作答了多选题，其作答结果应一并落库，并推送至数仓。以便运营同学分析。</p>
<p>官网渠道填写的信息在数据落库的时候，单独标记为：website_home、website_card、website_wallet</p>
<p>频控：</p>
<p>将官网作为一个特殊的投放渠道，与其他投放渠道同等对待。相关频控与投放页面保持一致：</p>
<p>同一个邮箱、同一个国家，仅提交1次。再次提交，toast：Submitted, please do not resubmit</p>
<p>同一个设备指纹总次数限制（总次数 非单位时间），最多10次。超过后，toast提示：The system is busy, please try again later。</p>
<p>同一个ip <strong>单位时间</strong>内总次数限制 100/15min。超过后，toast提示：The system is busy, please try again later。锁定15分钟后可再提交。</p>
<p>接口总限流（研发定义）超过后，toast提示：The system is busy, please try again later。</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: center;"><p><img src="assets/media/image2.png" style="width:1.36458in;height:0.89583in" /></p>
<p><img src="assets/media/image3.png" style="width:1.36458in;height:0.55208in" /></p></td>
<td style="text-align: left;"><a href="https://advancegroup.sg.larksuite.com/wiki/NQ2EwGQ35iK5VPkq3AVlWrflgod">[2025-11-20]AIX-外部投放waitlist</a>可见</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: center;"><img src="assets/media/image4.jpeg" style="width:1.36458in;height:2.95833in" /></td>
<td style="text-align: left;"><p>页面：移动端</p>
<p>显示：一个整页</p>
<p>移动端访问官网页面，引导用户通过电脑端访问该页面。</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: center;"><img src="assets/media/image5.png" style="width:1.36458in;height:0.91667in" /></td>
<td style="text-align: left;"><p>优化国家显示的emoj显示。（以台湾为示例），全部国家或地区图标不显示❌</p>
<p>涉及：</p>
<p>waitlist 移动端、pc端；</p>
<p>官网的移动端和pc端；</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: center;"><img src="assets/media/image6.png" style="width:1.36458in;height:0.23958in" /></td>
<td style="text-align: left;">增加一个disclaimer入口</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: center;"><img src="assets/media/image7.png" style="width:1.36458in;height:0.8125in" /></td>
<td style="text-align: left;"><p>点击disclaimer，进入一个单独页面。</p>
<p><strong>Important Notice</strong><br />
This website is not directed to any person in any jurisdiction where (by reason of that person's nationality, residence or otherwise) the publication or availability of this website is prohibited. The information contained in this website does not constitute a distribution, an offer to sell or the solicitation of an offer to purchase or subscribe for any products or services, nor is the information directed at any jurisdiction in which such offer, sale or recommendation is not authorised.<br />
<br />
The materials/information contained in this website are for general informational purposes only. This website is not intended to offer access to any products or services. You may request access to such products and services on our App. Any expression of interest and/or request to access products or services must come from your own initiative. Not all products and services are offered at all locations.<br />
<br />
All payment cards and/or accounts shall be issued, distributed and powered by our commercial partner(s) who hold certain licences. More information would be made available nearer to the public launch date.</p>
<p>AIXPay is a fintech service provider and not a bank. Our Multi-Currency Wallet is provided by appropriately licensed financial institutions and AIXPay only facilitates your use of such Multi-Currency Wallet.</p>
<p><strong>If you do not agree to the disclaimers above‚ please do not access this website or any related pages.</strong></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

# 5. 数据埋点

待定

# 6. 数据分析需求（待定）

# 7. 参考资料
