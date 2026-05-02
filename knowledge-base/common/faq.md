---
module: common
feature: faq
version: "1.1"
status: active
source_doc: 用户上传/AIX Phase 1 FAQ.xlsx；IMPLEMENTATION_PLAN.md；knowledge-base/common/_index.md；knowledge-base/wallet/stage-review.md；knowledge-base/changelog/final-repository-review.md
source_section: AIX Phase 1 FAQ.xlsx / sheet `(v4) AIX FAQs - Isaac` / column C final answers；IMPLEMENTATION_PLAN v4.4；外部依赖收窄原则
last_updated: 2026-05-02
owner: 吴忆锋
depends_on:
  - common/_index
  - wallet/stage-review
  - changelog/final-repository-review
---

# FAQ 公共问答

## 1. 功能定位

FAQ 用于沉淀 AIX App 面向用户的问答口径。

本文件仅转写已有 FAQ 原文，不新增问题，不扩展答案，不根据接口文档或模型推理补充客服口径。

本次来源为用户上传的 `AIX Phase 1 FAQ.xlsx`，sheet 为 `(v4) AIX FAQs - Isaac`。优先采用 C 列最终答案；若 C 列为空且 B 列有答案，才采用 B 列。无答案的问题不写入 FAQ 正文，只进入缺口清单。

## 2. 使用限制

1. 本文件记录的是 FAQ 原文口径，不等同于功能上线状态确认。
2. 涉及 Send / Withdrawal / Swap 的 FAQ 原文存在，但当前实施计划中 Send / Swap 仍为 `deferred`，不得作为当前 active 能力发布依据。
3. 涉及 Deposit / WalletConnect / Risk Withheld 的内容，只能按 FAQ 原文引用，不得扩展为完整状态机、完整错误码、完整合规规则。
4. 不得把 FAQ 中的用户表达反推为 DTC / AAI / 后端实现事实。
5. 后续如 FAQ 原文更新，应以新版 FAQ 文件覆盖，不自行改写。

## 3. FAQ 原文清单


### 3.1 AIX Pay wallet Opening & Cards Application

#### Q1. What types of cards does AIX Pay Card offer?

Source row: `3`

AIX Pay Card offers two card types: a Physical Card for everyday in-store use and a Virtual Card for online and digital payments. Each card has its own unique number and works just like a debit card, letting you spend directly from your stablecoin balance. 

Getting started is simple, just Apply for an AIX Pay Card, deposit your preferred stablecoin into your AIX Pay wallet, and you're ready to spend.

For added convenience, you can easily add your card to Google Pay and enjoy seamless tap-to-pay transactions wherever you go.

#### Q2. Who are the parties involved in the AIX Pay Card, and what are their roles?

Source row: `4`

The AIX Pay App is brought to you by AIXPAY LIMITED, which oversees your App account and App experience. We are not a virtual asset service provider, card issuer, bank or payment institution, wallet operator, custodian or remittance business. 

The AIX Pay Card is issued by Digital Treasures Center Pte. Ltd. (“dtcpay”), and all Applications for the AIX Pay Card are subject to their review and assessment. All transactions, settlements and asset transfers in relation to the AIX Pay Card are solely the responsibility of dtcpay.

#### Q3. Who is eligible to open an AIX Pay Card?

Source row: `5`

You're eligible as long as you can provide a valid passport and a proof of address in your name.

For card applications, your passport must be valid for at least 3 months from the application date.

Once you’ve submitted the required documents, we’ll review your Application as quickly as possible.

#### Q4. How do I Apply for a AIX Pay Card?

Source row: `6`

Applying for your AIX Pay Card is simple! Just follow these steps based on either virtual or physical card:

Virtual Card
1. After passing KYC and receiving the notification, tap "Apply Now".
2. Choose to get a virtual card.
3. Select your preferred stablecoin account.
4. After that, your card will be displayed, and you can start using it for digital payments.

Physical Card
1. After passing KYC and receiving the notification, tap "Apply Now".
2. Choose to get a physical card.
3. Select your preferred stablecoin account.
4. Enter the shipping address for your physical card.
5. After that, your card will be displayed and processed for delivery.

Please note:
The selected stablecoin account cannot be changed after the card is issued.

#### Q5. What documents do I need to provide when Applying for AIX Pay Card?

Source row: `7`

To get your AIX Pay Card, you’ll need to submit a few documents as part of the onboarding and verification process:

1. A valid passport with at least 3 months validity remaining
2. Proof of address
3. A live selfie for verification purposes

Make sure all documents are clear and up to date.

Once submitted, we'll review everything as quickly as possible.

#### Q6. How long does it take to get the AIX Pay Card Approved?

Source row: `8`

Verification usually takes up to 2 business days while your identity and address documents are being reviewed.

Once you're approved, we'll notify you through the AIX Pay App, and you can start using your card right away.

#### Q7. Why can't I pay the card fee even though I have enough balance?

Source row: `9`

Your card fee can only be paid using the stablecoin that matches your card’s selected account.

For example, if your AIX Pay Card is linked to your USDT account, the card fee must be paid from your USDT balance. Other stablecoin balances in your wallet can’t be used for this payment.

#### Q8. How does the AIX Pay Wallet work in relation to the AIX Pay Card?

Source row: `10`

Your AIX Pay Wallet stores your crypto. Your AIX Pay Card spends it anywhere, just like a regular payment card.

After you deposit stablecoins into your wallet and Apply for your card, we’ll link your card to one specific stablecoin account. From then on, all payments made with that card will be deducted only from that linked account.

### 3.2 Card Delivery & Activation

#### Q1. Is there a fee to Apply for the card?

Source row: `13`

Yes, there's a small Application fee for both card types:
 - Physical Card: USD $10
 - Virtual Card: USD $5 (Google Pay compatible)

This fee covers card setup and processing. Once your card is ready, you can start using it right away!

#### Q2. Can I request someone else to collect my card on my behalf?

Source row: `15`

For security and personal data protection, we recommend that only the person who applied for the card collects it.

However, if you need someone else to collect it for you, a third-party authorization may be accepted if the person provides:
- A copy of your passport
- Their own passport
- A signed authorization letter from you

Please note that your AIX physical card is a sensitive financial instrument, so we strongly advise collecting it yourself whenever possible.

#### Q3. Can I change the card delivery address once the card has been Approved?

Source row: `16`

Once your card is Approved, the delivery address can’t be changed. Make sure your shipping address is correct before submitting your Application.

#### Q4. What hAppens if my card can’t be delivered to my address?

Source row: `17`

If the courier can’t deliver your card because the address isn’t serviceable, we’ll reach out via email or push notification to get an alternative address.

No extra shipping fee will be charged, and we’ll arrange the re-delivery once we have the updated information.

#### Q5. When can I expect my card to arrive?

Source row: `18`

Delivery time is 3-15 business days
 
Once your card arrives, you can activate it easily in the AIX Pay App.

#### Q6. How do I activate my card once I receive it?

Source row: `19`

Virtual Card 
Your virtual card doesn't need activation! Once your Application is Approved, it's ready to use right away.

Physical Card
You’ll need to activate it in the App:
1. Open the AIX Pay App and tap “My Cards”.
2. Select the physical card you want to activate.
3. Tap “Activate” and complete the quick identity verification.
4. Once verified, your card is ready to use.

#### Q7. I have ordered a physical card but I don't receive the card after the stipulated timeline

Source row: `20`

If your card hasn’t arrived on time, please reach out to our customer support team. We’ll check the delivery status and help resolve it as quickly as possible.

### 3.3 Card Features & Management

#### Q1. Can I use the card for online and in-store purchases?

Source row: `23`

Your AIX Pay Card runs on the Visa network, so you can use it anywhere Visa is accepted for both online and in-store purchases — except where local regulations, merchant category restrictions, or card programme rules Apply.

#### Q2. Can I use the card for subscription payments (Netflix, Spotify, etc.)

Source row: `24`

You can use your AIX Pay Card for most recurring payments and subscriptions, including Netflix, Spotify, and other major services. Some merchants may require authentication at sign-up.

#### Q3. Can the card be added to digital wallets (Apple Pay, Google Pay)?

Source row: `25`

You can currently link your AIX Pay Card to Google Pay, Samsung Pay and Apple Pay

#### Q4. How can I add my AIX Pay Card to Google Pay?

Source row: `26`

You can add your AIX Pay Card to Google Pay manually by following these steps:

1. Open the Google Wallet App on your phone.
2. Tap "Add to Wallet" and choose "Payment card".
3. Select "New credit or debit card".
4. Scan your card or enter the card details manually.
5. Follow the prompts to accept the terms and complete card verification.

Once verified, your AIX Pay Card will be added to Google Wallet and ready to use for contactless payments.

#### Q5. Does the card support contactless payments?

Source row: `27`

Your AIX Pay Card fully supports contactless payments.

Just tap your card on the payment terminal wherever contactless payments are accepted, no need to insert the card or enter a PIN for small transactions.

#### Q6. Can I use the card to withdraw cash from ATMs?

Source row: `28`

Yes, cash withdrawals are supported at ATMs. A 2% fee Applies, and some ATMs may charge additional fees.

#### Q7. Can I set alerts for my card?

Source row: `29`

You’ll get instant push notification via AIX Pay App for every purchase. This helps you monitor your card activity in real time and spot any suspicious transactions quickly.

#### Q8. How to reset the card pin ?

Source row: `30`

You can reset your AIX Pay Card PIN easily in the App by following these steps:
1. Log in to your AIX Pay App and go to the “My Cards” section.
2. Select the card you want to reset the PIN for.
3. Tap “Reset PIN”.
4. Verify your identity if prompted.
5. Follow the instructions to set a new PIN.

Once completed, your new PIN will be ready to use for your card transactions.

#### Q9. How I can set AIX Pay Card pin ?

Source row: `31`

You can set your AIX Pay Card PIN in just a few steps:
1. Log in to your AIX Pay App and go to "My Cards".
2. Select the card you want to set the PIN for.
3. Tap "Set PIN".
4. Follow the on-screen instructions to create your PIN.

Once set, you’ll use this PIN for card transactions that require it.

#### Q10. Will I need a PIN to use the card?

Source row: `32`

Yes, a PIN is required for certain transactions to help keep your account secure. This may include:
1. In-store purchases over the contactless payment limit
2. ATM withdrawals
3. Transactions where the merchant requests PIN verification

For smaller contactless payments, you usually won’t need to enter your PIN.

#### Q11. Can I use my AIX Pay Card to make transactions in any fiat currency?

Source row: `33`

Your card works at any Visa merchant worldwide and supports all fiat currencies accepted by the Visa network. The final amount will be automatically converted to match your account's currency.

#### Q12. What is the daily/monthly spending limit?

Source row: `34`

You can spend up to USD $5,000 per month using your AIX Pay Card.

Please note:
- This limit applies only to card transactions.
- Your AIX Pay wallet balance limit is also USD $5,000.
- Cash withdrawal limits depend on the ATM and may be lower than your card spending limit.

#### Q13. Can I transfer funds from AIX account to another AIX account?

Source row: `35`

Yes, you can easily transfer funds instantly between AIX accounts. Here's how:
1. Open the AIX Pay App and go to the "Transfer" section.
2. Choose "Transfer to AIX account".
3. Enter the recipient's AIX account details and the amount you’d like to send.
4. Review and confirm the transaction.

Funds will move instantly between AIX accounts, and you'll see the update in your account right away.

#### Q14. Will there be any fees when converting one stablecoin to another, for example USDT to USDC?

Source row: `36`

SwApping between stablecoins is instant with zero fees, and it uses the real-time exchange rate available at the time of the swAp.

#### Q15. Can I use the AIX Pay Card internationally?

Source row: `37`

Yes, your AIX Pay Card works worldwide wherever Visa is accepted, both online and in-store.

#### Q16. How many AIX Pay Cards can be Applied?

Source row: `38`

Each account can have up to five cards, in any combination of physical and virtual cards.

For example, you might choose one virtual card for online shopping, one physical card for daily use, and another card linked to a different stablecoin account.

#### Q17. Can I use a different phone number or email to receive OTP for each card?

Source row: `39`

For security reasons, OTPs can only be sent to the phone number registered to your account. The same phone number applies to all your cards.

#### Q18. Can I request a replacement card if damaged?

Source row: `40`

If your AIX Pay Card is lost, damaged, or not working, just reach out to our customer support team.

We’ll help you check the issue and arrange a replacement if needed. A replacement fee may Apply depending on the card type.

#### Q19. Can I download card transaction history or statements?

Source row: `41`

You can easily view and download your AIX Pay Card transaction history straight from the App. Just go to the "Transactions" section and choose the statement you need.

#### Q20. In case of refund, which account will the funds be refunded to?

Source row: `42`

Refunds will be sent to the crypto account that's linked to your card at the time of refund.

For example: If your refund is for a transaction made with the USDC card, the refund will be credited back to your USDC account.

The returned amount will be in stablecoins, converted based on the card scheme's exchange rate at the time the refund is processed.

### 3.4 Security & Support

#### Q1. What hAppens if my card is lost or stolen?

Source row: `45`

If your physical card is lost or stolen, you can immediately lock it in the App to protect your funds.

How to lock your card:
1. Open the AIX Pay App and go to "My Cards".
2. Select the card you want to lock and tap "Lock".
3. Review the on-screen notice: “Once locked, you won't be able to make payments with this card. You can unlock it anytime in the App."
4. Tap "Lock card" to confirm.

Your card will be successfully locked and ready to unlock whenever you need it.
Need a replacement card? Simply head to the AIX Pay Card tab and tap Get Card to order a new physical card.

Tips:
 - Once locked, your card cannot be used for spending until you unlock it
 - Your locked card can still receive refunds or fund reversals.

#### Q2. Can I unlock my card?

Source row: `46`

Yes, you can lock or unlock your card directly in the App.

How to unlock your card:
1. Open the AIX Pay App and go to "My Cards".
2. Select the card you want to unlock and tap "Unlock".
3. Complete the on-screen identity verification.
4. Your card will be successfully unlocked and ready to use.

#### Q3. How long can I lock my card for?

Source row: `47`

You can lock your card for as long as you need! Simply use the AIX Pay App to lock or unlock your card anytime.

#### Q4. Can I lock the card temporarily without cancelling it?

Source row: `48`

Yes, you can temporarily lock your card without cancelling it. Rest assured, locking your card will not affect your card balance.

How to lock your card:
1. Open the AIX Pay App and go to "My Cards".
2. Select the card you want to lock and tap "Lock".
3. Review the on-screen notice: “Once locked, you won't be able to make payments with this card. You can unlock it anytime in the App."
4. Tap "Lock card" to confirm.

Your card will be successfully locked and ready to unlock whenever you need it.

#### Q5. Can I terminate my card using the AIX Pay App?

Source row: `49`

We're unable to process card terminations directly through the App at this time. As an alternative, you can lock your card instantly in the AIX Pay App to block all transactions.

#### Q6. How do I report unauthorized transactions?

Source row: `50`

If you spot any unauthorized or suspicious transactions on your AIX Pay Card, please take action right away:

1. Lock your card through the AIX Pay App under Cards → Security Settings.
2. You can reach our support team via email at support@aixpay.co or by calling our hotline at +852 9290 4155
3. Share the transaction details, including date, amount, merchant name, and any screenshots or reference numbers.
 
Our team will investigate immediately and may temporarily block your card to keep your account protected.

*Please note that international calling rates may Apply if you are dialing from outside Hong Kong.

#### Q7. Will I be notified for every card transaction?

Source row: `51`

Yes, you will receive a push notification through the AIX Pay App for every transaction made with your card.

#### Q8. How do I contact the AIX Pay Customer Support team?

Source row: `52`

You can reach our support team via email at support@aixpay.co or by calling our hotline at +852 9290 4155*

We aim to respond within 24 hours. If you haven't heard back, please check your spam or junk folder. If so, kindly mark it as "Not Spam" to ensure future messages reach your inbox directly.

*Please note that international calling rates may Apply if you are dialing from outside Hong Kong.

### 3.5 Fees and Charges

#### Q1. Are there any crypto deposit fee?

Source row: `55`

We do not charge fees for crypto deposits into your AIX Pay wallet.

#### Q2. Are there any transaction fees when using my AIX Pay Visa Card?

Source row: `56`

- For transaction in USD, a 1% transaction fee
- For transactions in any currency other than USD, an additional 1.2% foreign exchange (FX) fee will be Applied based on current Visa exchange rate

#### Q3. Are ATM withdrawal fees different for local and international locations?

Source row: `57`

ATM withdrawals come with a 2% withdrawal fee, whether you're at home or overseas. Do keep in mind that some ATM operators may charge their own fees on top of this. You'll see these displayed on the ATM screen before you confirm your transaction.

Fees to note:
- USD withdrawals: additional 1% transaction fee
- Non-USD withdrawals: additional 1.2% foreign exchange (FX) fee, on top of the 1% transaction fee will be Applied based on current Visa exchange rate

#### Q4. Are there any fees for card reissuance?

Source row: `58`

A small fee will be charged for card replacements:
- Physical Card: USD $10
- Virtual Card: USD $5 (Google Pay compatible) 
 
These help cover production and processing costs. Once your new card is activated, you can start using it right away - both online and in-store.

### 3.6 Account & Balance

#### Q1. How many types of balances do I have in my AIX Pay wallet?

Source row: `61`

Your AIX Pay wallet has four separate balances, one for each stablecoin: USDT, USDC, WUSD, and FDUSD. Each balance is kept separate so you always know exactly how much you have in each account.

#### Q2. When I make a transaction with my AIX Pay Card, which balance will be deducted?

Source row: `62`

Your card is linked to one specific stablecoin balance. All transactions made with that card will come from that account, so you can easily track your spending.

#### Q3. Can I change the stablecoin balance linked to my AIX Pay?

Source row: `63`

At this time, the stablecoin account linked to your AIX Pay Card cannot be changed after issuance. If you'd like to spend from a different stablecoin account, you may Apply for a new AIX Pay Card and select your preferred stablecoin account during the Application process

#### Q4. Can I combine balances from different stablecoins to pay for a transaction?

Source row: `64`

Not at the moment. Each card can only use the funds from its linked account, so make sure that account has enough balance to cover your purchases. Stay tuned - we'll let you know if other options become available. 

#### Q5. When I deposit my account, which balance will be credited?

Source row: `65`

When you deposit, the funds go to the specific stablecoin account you choose, like USDT, USDC, WUSD, or FDUSD. Just select the account you want to deposit and follow the steps, and your balance will be updated.

#### Q6. What is the balance limit for an AIX Pay wallet?

Source row: `66`

You can hold up to USD $5,000 in your AIX Pay wallet. This total includes all stablecoins in your account, such as USDT, USDC, WUSD, and FDUSD.

Need a higher limit? Simply reach out to us with supporting documents such as payslips, tax returns, business bank statements, or employment contracts. We're happy to help!

#### Q7. Can I add local currencies to my AIX Pay wallet?

Source row: `67`

At the moment, AIX Pay only supports deposit with stablecoins. We’ll keep you updated if we add more ways to fund your account.

#### Q8. How can I deposit my AIX Pay wallet using stablecoins?

Source row: `68`

You have two simple ways to deposit:

Deposit from Self-custody Wallet (On-chain):
1. Select Deposit Method: Tap "Deposit" on the home screen and select "Self-custody wallet".
2. Select Asset: Choose the stablecoin you wish to deposit (USDC, USDT, etc.) and enter the amount.
3. Choose Network: Select the blockchain network (e.g., ETH Ethereum ERC-20)
    - Important: Ensure your sending wallet supports this specific network to avoid loss of funds.
4. Finalize via QR Code or Connection:
    - Method A: Scan QR Code (Highly Recommended for iOS): To ensure the funds are sent from your preferred wallet, use your wallet App to scan the QR code shown on the AIX Pay screen. > Note: For iOS users, we suggest taking a screenshot of the QR code and importing it into your specific wallet App to avoid random App switching.
     - Method B: Connect Wallet: Tap "Connect wallet" to link via WalletConnect.
        ⚠️ Warning for iOS Users: Due to iOS system limitations, tApping "Connect wallet" may automatically open a random wallet App on your device. If this hAppens, please switch back and use the QR Code method instead to ensure you are using the correct wallet.
5. Confirmation: Once you authorize the transaction in your wallet, the funds will Appear in your AIX Pay account after blockchain confirmation.

Deposit from Exchange
Deposits are currently supported from Binance. Please ensure your Binance account name exactly matches your AIX Pay account name
1. Select Deposit Method: Tap "Deposit" on the home screen and select "Exchange".
2. Select Platform: Currently, only "Binance" is supported. Tap to proceed.
3. Enter Details:
    - Input the amount you wish to deposit.
    - Select your preferred stablecoin and the corresponding blockchain network.
4. Identity Confirmation (Crucial):  You must confirm that you are using a personal Binance account registered in your own name.
⚠️ Warning: Deposits from third-party accounts or accounts with non-matching names will result in transaction failure and potential delays in refunding.
5. Get Address/QR Code: After confirming the identity notice, your unique deposit address and QR code will be generated.
6. Complete the transfer:
    - Open your Binance App and go to "Withdrawal"
    -  Scan the QR code provided by AIX Pay or copy the deposit address.
    - Double-check: Ensure the network selected in Binance matches the network selected in the AIX Pay App.
7. Confirmation: Once the transaction is confirmed on the blockchain, your AIX Pay balance will be updated automatically.

#### Q9. Which crypto wallet can I use to deposit my AIX Pay wallet?

Source row: `69`

With a Self-custody Wallet (On-chain), you can deposit from any crypto wallet, as long as the blockchain network matches your AIX Pay crypto address or QR code.

For linked accounts, we currently support: MetaMask, Trust Wallet, Phantom, Rainbow, Ledger Live, Binance Wallet, Rabby, OKX Wallet, Exodus, Bitget Wallet, Base Wallet, 1inch Wallet, BitPay, TokenPocket, SafePal, Uniswap Wallet, Fireblocks, Best Wallet

#### Q10. Which stablecoins and blockchain networks are supported for deposits into an AIX Pay wallet?

Source row: `70`

Here’s what you can deposit:
1. USDC: Base, BSC, Ethereum, Solana
2. USDT: BSC, Ethereum, Solana
3. FDUSD: BSC, Ethereum, Solana
4. WUSD: Ethereum

#### Q11. Can I deposit my AIX Pay stablecoin account from any crypto exchange or account?

Source row: `71`

Yes, but make sure the sender’s account details match your AIX Pay account (name, date of birth, passport info). Do ensure the accuracy of the account address and blockchain network so your funds arrive safely from any crypto exchange or account. 

#### Q12. How long does it take for my stablecoins deposit to be successful?

Source row: `72`

Stablecoin deposits typically complete within 1–15 minutes, depending on the blockchain network and current congestion levels.

For the latest updates, you can always check your latest balance in the AIX Pay App.

#### Q13. How do I check my stablecoins deposit status?

Source row: `73`

We'll notify you as soon as the deposit is complete and your funds are available in your account.

Tip: You can also track your deposits in real-time! Simply paste the transaction hash provided in your sending crypto wallet's transaction history into the Appropriate blockchain explorer to view the on-chain transfer status.

#### Q14. Are there any minimum or maximum limits for deposits into my AIX Pay stablecoin account?

Source row: `74`

The minimum deposit is 0.01 for all supported stablecoins (USDC, USDT, WUSD, and FDUSD)

You can deposit as much as you like, as long as your total account balance doesn't exceed USD $5,000. This limit is calculated across all your stablecoins combined.

Need a higher limit? Simply reach out to us with supporting documents such as payslips, tax returns, business bank statements, or employment contracts. We're hAppy to help!

#### Q15. Why has my stablecoin deposit not arrived?

Source row: `75`

Stablecoin deposits are usually processed within a few minutes, but delays or failures can hAppen due to blockchain conditions or verification requirements.

Common causes include:
- Network congestion during busy periods
- The blockchain network still needs more confirmations
- The deposit is under compliance review
- The sender’s account information does not match your AIX Pay account

If your deposit still hasn’t arrived:
- Check the transaction using a blockchain explorer
- Make sure the account address and blockchain network are correct
- Confirm that the sending account belongs to you and matches your AIX Pay account details
- Contact AIX Pay support with your transaction hash and deposit details.

#### Q16. What hAppens if I deposit using an unsupported blockchain network?

Source row: `76`

If you accidentally use a blockchain network that’s not supported, AIX Pay won’t be able to receive the funds. These transactions usually can’t be reversed, so please double-check the network before you send.

#### Q17. What hAppens if I deposit to wrong account address?

Source row: `77`

If you send funds to the wrong address, we won’t be able to receive them and the transaction usually can’t be reversed.

Always double-check the address before confirming your deposit.

#### Q18. My deposit status is stuck on "Under Review" or says it is "at risk of being refunded." Why?

Source row: `78`

If your deposit status is "Under Review," it was likely flagged because the sending account hasn’t been linked or verified with your AIX Pay account.

For your protection and to meet compliance requirements, deposits must come from an account you’ve verified and linked.

To resolve this, check the deposit details in your AIX Pay App and follow the instructions to verify or link the sending account.

#### Q19. What stablecoins are supported for stablecoins withdrawal?

Source row: `79`

We support the following stablecoins across multiple blockchain networks:
1. USDC: Base, BSC, Ethereum, Solana
2. USDT: BSC, Ethereum, Solana
3. FDUSD: BSC, Ethereum, Solana
4. WUSD: Ethereum

Make sure to select the correct network when withdrawing.

#### Q20. How can I withdraw stablecoins from AIX app?

Source row: `80`

Withdrawing stablecoins is easy! Just follow these steps:

1. Choose which stablecoin you want to withdraw
2. Enter or select your wallet address
3. Select the correct blockchain network
4. Enter the amount you want to withdraw
5. Check the details carefully and confirm

Your withdrawal will be processed on the blockchain.

#### Q21. What are the withdrawal fees for stablecoins?

Source row: `81`

Withdrawal fees vary based on the blockchain network you choose and current network conditions. You’ll see the exact fee in the App before confirming your withdrawal.

#### Q22. What is the minimum stablecoins withdrawal?

Source row: `82`

The minimum withdrawal amount for all stablecoins is 0.01

#### Q23. How can I cancel my stablecoin withdrawal?

Source row: `83`

Unfortunately, once you've initiated a withdrawal, we're unable to cancel it. Please make sure to double-check all the details before confirming.

#### Q24. How long does a stablecoin withdrawal usually take to complete?

Source row: `84`

Most stablecoin withdrawals complete within a few minutes, though timing depends on the blockchain network and congestion.

#### Q25. Why is my crypto withdrawal marked as successful but not showing in my destination wallet?

Source row: `85`

First, make sure the account address and blockchain network you entered match your destination wallet.

If everything looks correct, use the transaction hash shown in your AIX Pay App to check the transfer status on a blockchain explorer.

#### Q26. What happens if I enter the wrong account address?

Source row: `86`

We know this can be stressful, so here's what you need to know: If your withdrawal has been completed, we can’t reverse or recover it.

Crypto transactions are usually final, so please always double-check your account address before confirming.

#### Q27. What if I choose the wrong blockchain network for my withdrawal?

Source row: `87`

If you select a network that isn't supported by your destination account or exchange, your funds may be lost permanently.

To keep your funds safe, please always make sure the network you choose matches the one supported by your destination.

### 3.7 Transaction Issues （新增加）

#### Q1. Why was my transaction declined?

Source row: `91`

Please check the following common reasons for declined transactions:
1. Insufficient available balance in your AIX Pay Wallet.
2. Incorrect PIN or CVV entered at checkout
3. Platform risk controls were triggered (e.g., the merchant falls under a prohibited Merchant Category Code like gambling or unregulated financial brokers)
4. 3DS security verification failed (SMS OTP was not entered or timed out)

#### Q2. Why was my card charged more than my actual transaction amount?

Source row: `92`

For some merchants (e.g., hotel, taxi, car rental) an authorization hold may be placed for an amount higher than your expected transaction total to account for potential exchange rate fluctuations or final service charges. Don't worry, you will only ever be charged the actual transaction amount. Any excess held funds will be automatically released back to your available wallet balance once the transaction settles, typically within a few days

#### Q3. How do I dispute an unauthorized charge (Chargeback)?

Source row: `93`

You must submit a dispute within [X] days (e.g., 60 or 120 days) of the transaction date. You will be required to provide proof that you attempted to resolve the issue directly with the merchant and were refused a refund. Please note: Abusing the chargeback process will result in permanent account suspension.

## 4. FAQ 原文缺口

| Row | 问题 | 当前处理 |
|---|---|---|

| 14 | How can I check the delivery status of my physical card? | FAQ 原文无答案，暂不写入正文 |

## 5. 与当前知识库状态的冲突隔离

| FAQ 内容类型 | 当前处理 |
|---|---|
| Deposit / stablecoin deposit | 可引用 FAQ 原文，但不得补写完整状态机 |
| WalletConnect / self-custody wallet | 可引用 FAQ 原文，但不得补写 senderAddress 获取、Declare、Travel Rule |
| Exchange / Binance deposit | 可引用 FAQ 原文，但 GTR / Exchange 产品路径仍需独立确认 |
| Withdrawal / Send | FAQ 原文存在，但 Send / Withdrawal 当前仍按实施计划标记 `deferred` |
| Swap | FAQ 原文存在，但 Swap 当前仍按实施计划标记 `deferred` |
| Risk Withheld / Under Review | 可引用 FAQ 原文，不得等同 Wallet `REJECTED` / `PENDING` / `PROCESSING` |
| Chargeback / dispute | 可引用 FAQ 原文，但 `[X] days` 占位仍需业务确认 |

## 6. 不写入事实的内容

以下内容不得由 FAQ 反推出系统事实：

1. Send / Withdrawal 当前已上线。
2. Swap 当前已上线。
3. GTR 必然等同 `FIAT_DEPOSIT=6`。
4. WalletConnect 必然等同 `CRYPTO_DEPOSIT=10`。
5. Deposit success 必然等同 Wallet `COMPLETED`。
6. Risk Withheld 必然等同 Wallet `REJECTED` / `PENDING` / `PROCESSING`。
7. WalletConnect senderAddress 获取方式已确认。
8. Declare / Travel Rule 触发条件已确认。
9. FAQ 中未出现的问题或答案。

## 7. 来源引用

- (Ref: 用户上传 / AIX Phase 1 FAQ.xlsx / `(v4) AIX FAQs - Isaac`)
- (Ref: IMPLEMENTATION_PLAN.md / v4.4)
- (Ref: knowledge-base/changelog/final-repository-review.md / v1.3)
