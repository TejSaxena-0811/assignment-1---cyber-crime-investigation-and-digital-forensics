# Operation Phantom Swipe
### Investigating a Cross-Border ATM & Credit Card Fraud Ring
**Assignment 1 — Unit 1: Foundations of Digital Forensics**

> ⚠️ **All evidence, device data, personal details, and card/account numbers in
> this repository are entirely fabricated for academic simulation.** No real
> individuals, accounts, or financial instruments are represented.

---

## 1. Repository Structure

```
operation-phantom-swipe/
├── evidence/                  # Simulated seized media (Sub-Problem 2)
│   ├── skimmer_device/        # Exhibit A - skimmer memory dump + metadata
│   ├── suspect_phone/         # Exhibit B - call/SMS/GPS logs, fraud apps
│   └── password_protected/    # Exhibit C - encrypted archive (Sub-Problem 4)
├── artefacts/                 # Extracted artefacts + search logs (Sub-Problem 3)
├── chain_of_custody/          # Chain-of-custody form (Sub-Problem 2)
├── hashes/                    # SHA-256 manifest of all evidence files
├── cryptography/              # Dictionary-attack script, wordlist, attack log,
│                               #   ethical discussion (Sub-Problem 4)
├── scripts/                   # Forensic tooling (hashing, string search)
├── screenshots/                # Simulated tool-run screenshots
├── docs/                      # Cybercrime taxonomy & legal mapping (Sub-Problem 1)
├── report/                    # Final legal-technical report (Sub-Problem 5)
└── .github/workflows/         # CI: repo structure validation
```

## 2. Execution Guide

Run from the repository root, in order:

```bash
# 1. Generate SHA-256 hash manifest of all evidence
bash scripts/generate_hashes.sh evidence hashes/sha256_hashes.txt

# 2. Run forensic string search across evidence
python3 scripts/string_search.py evidence artefacts/string_search_results.txt

# 3. Attempt lawful dictionary attack on the password-protected exhibit
#    (operates on a forensic COPY, never the original exhibit)
cp evidence/password_protected/secure_vault.zip cryptography/forensic_copy/secure_vault_COPY.zip
python3 cryptography/dictionary_attack.py cryptography/forensic_copy/secure_vault_COPY.zip cryptography/wordlist_custom.txt
```

All three scripts are idempotent and log their own output (`hashes/sha256_hashes.txt`,
`artefacts/string_search_results.txt`, `cryptography/attack_log.txt`).

## 3. Tools Used

| Tool | Purpose |
|---|---|
| Python 3.12 (`zipfile`, `hashlib`, `re`) | Dictionary attack simulation, hashing, pattern/string search |
| Bash / `sha256sum` | Evidence hash manifest generation |
| `zip` (ZipCrypto) | Simulated password-protected evidence container |
| GitHub Actions | CI validation of repository structure |
| `docx` (Node.js) | Generation of the final Word report |

*(In a real investigation, `zip2john` + John the Ripper, or `hashcat -m 17200`,
would be used in place of the custom Python cracker; the custom script is
functionally equivalent and used here for a self-contained, reproducible
academic simulation — see `cryptography/cracking_simulation.md` §2 for the
direct command-line equivalents.)*

## 4. Deliverables Checklist

- [x] Simulated media files, extracted artefacts, password-protected folder
- [x] Legal-technical report (`report/Legal-Technical-Report.docx`)
- [x] Cracking/analysis tools (`scripts/`, `cryptography/dictionary_attack.py`)
- [x] Tool usage screenshots (`screenshots/`)
- [x] Chain of custody form (`chain_of_custody/chain_of_custody_form.md`)
- [x] Hash values of collected artefacts (`hashes/sha256_hashes.txt`)
- [x] Execution guide, tools used, authorship declaration (this file)
- [x] GitHub Action for validating repo structure (`.github/workflows/validate-structure.yml`)

## 5. Authorship Declaration

I declare that the analysis, scripts, and report in this repository represent
my own work for this assignment. All evidence data is synthetically generated
for the purpose of this academic simulation; no real persons, devices, or
financial data are involved.

**Name:** _____________________
**Roll/Student No.:** _____________________
**Course:** Foundations of Digital Forensics — Unit 1, Assignment 1
**Date:** _____________________
**Signature:** _____________________
