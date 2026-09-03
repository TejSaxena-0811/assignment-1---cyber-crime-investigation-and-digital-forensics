# Operation Hydra
### Unraveling a Multi-Vector Cyber Crime Involving Phishing, Spoofing & Financial Fraud
**Assignment 2 — Unit 2: Types of Cyber Crimes**

> ⚠️ **All email samples, domains, IP addresses, malware behavior, transaction
> logs, and wallet addresses in this repository are entirely fabricated for
> academic simulation.** No real individuals, organisations, malware
> samples, or financial instruments are represented. No functional
> malicious code is included anywhere in this repository.

## 1. Scenario Summary

A fictitious logistics company, Nimbus Logistics Pvt Ltd, was targeted by a
coordinated multi-stage campaign: attackers spoofed trusted brands (a bank,
a courier company, and Nimbus's own HR domain) to deliver phishing emails,
one of which carried a macro-enabled document that dropped a
keylogging Trojan/RAT. Harvested banking credentials were then used to
drain funds via UPI and card transactions, laundered through mule accounts
and a simulated cryptocurrency off-ramp.

## 2. Repository Structure

```
operation-hydra/
├── docs/
│   └── taxonomy.md                  # Sub-Problem 1: crime decomposition & legal mapping
├── phishing_spoofing/
│   ├── email_samples/               # 4 simulated .eml phishing samples
│   ├── scripts/
│   │   ├── parse_headers.py         # Header/SPF/DKIM/DMARC parser
│   │   └── ip_trace.py              # IP extraction + threat-intel cross-reference
│   ├── threat_intel.json            # Simulated AbuseIPDB/VirusTotal lookup table
│   ├── header_analysis.md           # Output of parse_headers.py
│   ├── ip_trace_results.md          # Output of ip_trace.py
│   ├── whois_lookup_results.md      # Simulated WHOIS records for spoofed domains
│   └── spf_dkim_dmarc_report.md     # Authentication analysis + recommendations
├── malware_analysis/
│   ├── payload_simulated/
│   │   └── behavior_description.md  # Non-functional, descriptive payload walkthrough
│   ├── scripts/
│   │   └── ioc_extractor.py         # Regex-based IOC extraction tool
│   ├── sandbox_report.md            # Simulated sandbox detonation timeline + classification
│   ├── ioc_list.md                  # Full IOC list + MITRE ATT&CK mapping
│   └── extracted_iocs.json          # Output of ioc_extractor.py
├── financial_fraud/
│   ├── logs/                        # UPI, card, and crypto-wallet transaction logs
│   ├── scripts/
│   │   └── trace_fraud_flow.py      # Money-flow reconstruction + structuring detection
│   └── fraud_flow_trace.md          # Output of trace_fraud_flow.py
├── hashes/
│   ├── generate_hashes.sh
│   └── sha256_hashes.txt
├── tools/
│   └── tools_used.md                # Tools + commands + justifications
├── screenshots/                     # Simulated terminal output screenshots
├── report/
│   └── Legal-Technical-Impact-Report.docx / .pdf
└── .github/workflows/
    ├── markdown-lint.yml
    └── validate-structure.yml
```

## 3. Setup Instructions

Requires Python 3.9+ and Bash. No external dependencies or API keys needed
— all "live lookups" (WHOIS, AbuseIPDB, VirusTotal) are simulated via local
reference files so the analysis is fully reproducible offline.

```bash
git clone <this-repo-url>
cd operation-hydra
```

## 4. Execution Guide

Run from the repository root, in order:

```bash
# 1. Parse phishing email headers (SPF/DKIM/DMARC + red flags)
python3 phishing_spoofing/scripts/parse_headers.py \
    phishing_spoofing/email_samples phishing_spoofing/header_analysis.md

# 2. Trace relay IPs against simulated threat intelligence
python3 phishing_spoofing/scripts/ip_trace.py \
    phishing_spoofing/email_samples phishing_spoofing/threat_intel.json \
    phishing_spoofing/ip_trace_results.md

# 3. Extract IOCs from the malware sandbox report
python3 malware_analysis/scripts/ioc_extractor.py \
    malware_analysis/sandbox_report.md malware_analysis/extracted_iocs.json

# 4. Reconstruct the financial fraud money-flow
python3 financial_fraud/scripts/trace_fraud_flow.py \
    financial_fraud/logs financial_fraud/fraud_flow_trace.md

# 5. Regenerate the evidence hash manifest
bash hashes/generate_hashes.sh
```

All scripts are idempotent and safe to re-run.

## 5. Tools Used

See `tools/tools_used.md` for the full list of custom scripts, their exact
commands, and the industry-standard tool (MXToolbox, VirusTotal, AbuseIPDB,
WHOIS, CyberChef, sandbox platforms) each one represents.

## 6. Deliverables Checklist

- [x] Sample logs, email headers, malware IOCs (`phishing_spoofing/`, `financial_fraud/logs/`, `malware_analysis/ioc_list.md`)
- [x] IP trace scripts, malware decoders (IOC extractor), WHOIS lookups
- [x] Final report (`report/Legal-Technical-Impact-Report.docx` + `.pdf`) with references
- [x] Tool screenshots, analysis logs (`screenshots/`, `*_results.md`, `*_trace.md`)
- [x] List of tools with usage commands and justifications (`tools/tools_used.md`)
- [x] Summary, setup instructions, authorship declaration (this file)
- [x] GitHub Actions for markdown lint + directory check (`.github/workflows/`)

## 7. Authorship Declaration

I declare that the analysis, scripts, and report in this repository
represent my own work for this assignment. All email samples, malware
behavior descriptions, transaction logs, and wallet addresses are
synthetically generated for the purpose of this academic simulation; no
real persons, organisations, or financial data are involved, and no
functional malicious code is included.

**Name:** _____________________
**Roll/Student No.:** _____________________
**Course:** Types of Cyber Crimes — Unit 2, Assignment 2
**Date:** _____________________
**Signature:** _____________________
