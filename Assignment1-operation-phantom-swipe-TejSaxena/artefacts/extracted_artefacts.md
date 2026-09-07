# Extracted Artefacts Log
### Sub-Problem 3: Electronic Media Search and Analysis

Artefacts below were extracted from the forensic images/logical extractions of
Exhibits A, B, and C using the scripts in `/scripts` and `/cryptography`
(`string_search.py`, `dictionary_attack.py`). All source data is simulated for
academic purposes.

| # | Artefact | Source File | Evidentiary Significance |
|---|---|---|---|
| 1 | Simulated card numbers (masked, `4532XXXXXXXX0011` etc.) | `evidence/password_protected/secure_vault.zip` → `card_master_list.txt` | Suggests possession of a batch of cloned/skimmed card data — supports charge of possession of stolen financial instruments |
| 2 | Overseas contact number `+971-50-1234567` (UAE) appearing repeatedly | `evidence/suspect_phone/call_logs.csv`, `sms_logs.csv` | Establishes cross-border communication link relevant to Budapest Convention Art. 25 (mutual legal assistance) |
| 3 | GPS coordinates placing suspect at ATM location at time of skimmer installation (`28.4089, 77.3178`, 2026-08-09 21:40–22:40) | `evidence/suspect_phone/gps_logs.csv` | Places suspect device at crime scene during device-mount window — corroborates physical seizure |
| 4 | SMS referencing OTP forwarding ("otp: 114420 use fast card locks in 3 min") | `evidence/suspect_phone/sms_logs.csv` | Evidence of real-time OTP interception/social engineering — supports IT Act §66C/§66D and IPC §420 |
| 5 | Mule account references (`XXXXXX4432`, `XXXXXX8810`) and handler numbers | `evidence/password_protected/secure_vault.zip` → `cashout_network.txt` | Identifies money-mule network used for cash-out — relevant to IPC §411/§120B (conspiracy) and PMLA linkage |
| 6 | Fraudulent application binaries (`FakeBankLogin_v1.apk`, `CardGenPro_v3.apk`) | `evidence/suspect_phone/apps/` | Tools used to harvest credentials / generate card data — supports IT Act §66C, §43 |
| 7 | Skimmer device identifier `SKM-7734-XR` matching prior case database entries | `evidence/skimmer_device/device_metadata.txt` | Links suspect to a pattern of prior offences (series linkage) |

## File Search Strategy

1. **Triage pass** — `strings`-equivalent scan (`scripts/string_search.py`) run
   across all evidence directories to flag files containing phone-number,
   GPS-coordinate, card-number, and keyword patterns (`otp`, `cashout`, `clone`,
   `skimmer`, `mule`, `batch`).
2. **Targeted extraction** — Flagged files (`sms_logs.csv`, `call_logs.csv`,
   `gps_logs.csv`, `secure_vault.zip`) manually reviewed and cross-referenced
   against known fraud indicators.
3. **Encrypted container** — `secure_vault.zip` flagged as password-protected;
   handed to Sub-Problem 4 (cryptography) for lawful recovery before content
   review.
4. **Metadata review** — Device metadata (`device_metadata.txt`) checked
   against internal case-reference database for series linkage.

Full raw hit log: see `artefacts/string_search_results.txt` (30 pattern matches
across 8 files, timestamped).
