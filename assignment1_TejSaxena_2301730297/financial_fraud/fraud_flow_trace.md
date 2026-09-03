# Financial Fraud Flow Trace

## 1. UPI Flow: Victim -> Mule Accounts

- 2026-08-07 10:14:02: victim -> unknown123@paytm INR 45,000 (device IP 103.224.182.19)
- 2026-08-07 10:16:45: victim -> mule_ac1@ybl INR 62,500 (device IP 103.224.182.19)
- 2026-08-07 10:19:11: victim -> mule_ac1@ybl INR 38,000 (device IP 103.224.182.19)
- 2026-08-07 22:03:55: mule_ac1@ybl (mule) -> cryptoxch_44@oksbi INR 140,000
- 2026-08-08 03:11:20: mule_ac2@ybl (mule) -> cryptoxch_44@oksbi INR 98,000
- 2026-08-08 09:40:00: victim -> mule_ac2@ybl INR 29,500 (device IP 176.113.115.204)
- 2026-08-09 14:22:31: mule_ac1@ybl (mule) -> mule_ac3@ibl INR 50,000

**Total drained from victim account (rmehta@okhdfcbank): INR 175,000**

### Mule Account Aggregation

- mule_ac1@ybl: received INR 100,500 total
- mule_ac2@ybl: received INR 29,500 total
- mule_ac3@ibl: received INR 50,000 total

## 2. Card-Based Fraud (Card ending 4432)

- 2026-08-07 10:30:00: QuickBuy Electronics Online - INR 84500 [APPROVED] from IP 185.220.101.47 (Unknown/VPN)
- 2026-08-07 11:05:12: GlobalGiftCards.info - INR 25000 [APPROVED] from IP 185.220.101.47 (Unknown/VPN)
- 2026-08-07 23:58:40: CryptoBuy Exchange Top-up - INR 120000 [APPROVED] from IP 103.224.182.19 (Vietnam)
- 2026-08-08 02:14:09: GlobalGiftCards.info - INR 30000 [DECLINED (limit)] from IP 185.220.101.47 (Unknown/VPN)

**Total approved card fraud: INR 229,500**

## 3. Crypto Laundering Trace

- 2026-08-07 10:35:00: bc1qSIM_mule_wallet_a1 -> bc1qSIM_hydra_pool_01 (0.42 BTC ~= INR 140000) via CryptoXCH (simulated)
- 2026-08-08 03:15:00: bc1qSIM_mule_wallet_a2 -> bc1qSIM_hydra_pool_01 (0.29 BTC ~= INR 98000) via CryptoXCH (simulated)
- 2026-08-09 15:00:00: bc1qSIM_hydra_pool_01 -> bc1qSIM_mixer_exit_9 (0.68 BTC ~= INR 225000) via Mixer Service (simulated)

**Observation:** Both mule wallets consolidate into a single pooling wallet (`bc1qSIM_hydra_pool_01`) before being forwarded to a mixer-style exit wallet — a classic layering pattern to obscure the audit trail before final cash-out.

## 4. Structuring / Suspicious Pattern Flags

- 1 transaction(s) fall just under the INR 50,000 UPI per-transaction soft-review threshold used by several PSPs, consistent with deliberate structuring to avoid automated review.
- Multiple transfers to mule accounts occur within minutes of the initial victim debit, consistent with automated/scripted transaction execution rather than manual banking activity.
