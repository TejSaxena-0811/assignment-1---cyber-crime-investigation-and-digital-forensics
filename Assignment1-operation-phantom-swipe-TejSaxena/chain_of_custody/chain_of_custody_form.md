# Chain of Custody Form
### Case: Operation Phantom Swipe — Cross-Border ATM & Credit Card Fraud Ring
**Case Reference:** CC/2026/0147

---

## Section A — Case Information

| Field | Detail |
|---|---|
| Investigating Unit | Cyber Cell, Faridabad District (Simulated) |
| Case Reference No. | CC/2026/0147 |
| Date of Incident Report | 2026-08-09 |
| Investigating Officer | Cyber Cell Investigator, Badge No. CC-1145 |
| Forensic Examiner | Digital Forensics Analyst, Badge No. DF-0552 |

## Section B — Exhibit Log

| Exhibit No. | Description | Recovered From | Date/Time Seized | Seized By |
|---|---|---|---|---|
| A | ATM overlay skimmer device (SKM-7734-XR) | ATM vestibule, NCR Bank, Sector 21, Faridabad | 2026-08-10 22:40 IST | Inv. CC-1145 |
| A-1 | Micro-SD card (2GB), pinhole camera module | Internal to Exhibit A | 2026-08-10 22:45 IST | Inv. CC-1145 |
| B | Android smartphone (suspect device) | Rented flat, Sector 15, Gurugram | 2026-08-12 20:20 IST | Inv. CC-1145 |
| C | Password-protected archive `secure_vault.zip` (extracted from Exhibit B storage) | Logical extraction of Exhibit B | 2026-08-13 10:05 IST | DF Analyst DF-0552 |

## Section C — Custody Transfer Log

| # | Transferred From | Transferred To | Date/Time | Purpose | Signature |
|---|---|---|---|---|---|
| 1 | Field (Inv. CC-1145) | Evidence Custodian | 2026-08-10 23:15 IST | Intake, sealing in tamper-evident bag | [signed] |
| 2 | Evidence Custodian | Forensic Lab (DF-0552) | 2026-08-11 09:00 IST | Imaging & analysis | [signed] |
| 3 | Forensic Lab (DF-0552) | Evidence Custodian | 2026-08-13 18:00 IST | Return post-imaging, retained for trial | [signed] |
| 4 | Evidence Custodian | Secure Evidence Room, Rack 14 | 2026-08-13 18:10 IST | Long-term storage pending trial | [signed] |

## Section D — Evidence Handling Procedure

1. **Seizure:** Devices photographed in-place before removal. Evidence bagged in
   anti-static, tamper-evident bags; bag seal numbers recorded against each exhibit.
2. **Write-blocking:** All imaging of Exhibit A (skimmer flash) and Exhibit B
   (phone storage) performed using a certified hardware write-blocker to guarantee
   the original media is never mounted read-write.
3. **Imaging:** A bit-for-bit forensic image was taken of each device. The
   working copy used for analysis is a forensic image/logical extraction —
   analysis is never performed on the original exhibit.
4. **Hashing:** SHA-256 hash computed on the original exhibit and on the image
   immediately after acquisition, and re-verified after analysis (see
   `hashes/sha256_hashes.txt`). Matching hashes confirm no evidence tampering.
5. **Storage:** Original exhibits sealed and logged into the secure evidence
   room; access requires custodian sign-out logged in Section C.
6. **Access control:** Only the assigned forensic examiner may work with
   forensic copies; all tool runs are logged (see `cryptography/attack_log.txt`,
   `artefacts/string_search_results.txt`).

## Section E — Integrity Verification

| Exhibit | SHA-256 (at seizure) | SHA-256 (pre-analysis) | SHA-256 (post-analysis) | Match? |
|---|---|---|---|---|
| Skimmer memory dump | `edfb1f5d...8db33` | `edfb1f5d...8db33` | `edfb1f5d...8db33` | ✅ Yes |
| secure_vault.zip | `984b2536...80d08f` | `984b2536...80d08f` | `984b2536...80d08f` | ✅ Yes |

*(Full hash values in `hashes/sha256_hashes.txt`.)*

---
**Declaration:** I certify that the above record accurately reflects all individuals
who had custody of the listed evidence and that the evidence was preserved in the
condition described at each stage.

Examiner Signature: ___________________________  Date: ___________
