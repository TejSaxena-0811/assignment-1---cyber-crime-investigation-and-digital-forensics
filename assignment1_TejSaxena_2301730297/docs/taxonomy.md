# Cybercrime Decomposition & Legal Mapping
### Sub-Problem 1: Operation Hydra

## 1. Attack Decomposition

Operation Hydra is a multi-vector campaign chaining five distinct offences
into a single fraud lifecycle:

```
Operation Hydra
├── Stage 1: Spoofing            (forged sender domains/emails)
├── Stage 2: Phishing            (social-engineered emails, 4 samples)
├── Stage 3: Unauthorized Access  (macro dropper -> RAT/keylogger)
├── Stage 4: Malware Distribution (Trojan/RAT via document attachment)
└── Stage 5: Financial Fraud & Money Laundering (UPI/card fraud -> mule -> crypto)
```

## 2. Five Distinct Crimes Identified

| # | Crime | Evidence |
|---|---|---|
| 1 | **Email/Domain Spoofing** | Forged `From`/`Return-Path` headers, lookalike domains (`secure-trustbank.co`, `hdfcbank-secure.info`, etc.) — see `phishing_spoofing/` |
| 2 | **Phishing** | 4 social-engineered email samples using urgency, authority, and brand impersonation — see `phishing_spoofing/email_samples/` |
| 3 | **Unauthorized Access / Computer Intrusion** | Macro-triggered PowerShell stager and persistent RAT installed without consent — see `malware_analysis/sandbox_report.md` |
| 4 | **Malware Distribution (Trojan/RAT)** | Macro-enabled document weaponised as a dropper for a keylogging RAT — see `malware_analysis/ioc_list.md` |
| 5 | **Financial Fraud & Money Laundering** | UPI/card fraud totalling INR ~4,04,500, layered through mule accounts into crypto — see `financial_fraud/fraud_flow_trace.md` |

*(A sixth, related offence — spamming/bulk unsolicited messaging via
compromised/bulletproof mail infrastructure — is also present as an
aggravating factor across Stages 1–2, but is treated as ancillary to
Phishing/Spoofing rather than counted separately.)*

## 3. Legal Mapping — Indian Law

| Crime | IT Act, 2000 | IPC, 1860 |
|---|---|---|
| Email/Domain Spoofing | §66C (identity theft), §66D (cheating by personation) | §419 (cheating by personation), §465 (forgery) |
| Phishing | §66D, §43 | §420 (cheating), §468 (forgery for cheating) |
| Unauthorized Access | §43, §66 | §379 (theft, re: data), §406 (criminal breach of trust, where applicable) |
| Malware Distribution (Trojan/RAT) | §43(c) (introduction of computer contaminant), §66 | §268 (public nuisance, where widescale), §120B (conspiracy) |
| Financial Fraud & Laundering | §66C, §66D | §420, §411 (receiving stolen property — mule accounts), §120B; **Prevention of Money Laundering Act (PMLA), 2002** for the layering/crypto stage |

## 4. Legal Mapping — Global Frameworks

| Crime | CFAA (US) | GDPR (EU) | Budapest Convention |
|---|---|---|---|
| Email/Domain Spoofing | 18 U.S.C. §1030(a)(4) (access with intent to defraud) | Art. 5, 32 (unlawful processing/insecure processing of personal data obtained via spoofing) | Art. 7 (computer-related forgery) |
| Phishing | §1030(a)(4), (a)(2) (unauthorized access to obtain information) | Art. 33 (breach notification obligations triggered for affected EU data subjects, if any) | Art. 8 (computer-related fraud) |
| Unauthorized Access | §1030(a)(2), (a)(5) (damage from unauthorized access) | Art. 32 (security of processing failure) | Art. 2 (illegal access) |
| Malware Distribution | §1030(a)(5)(A) (knowing transmission causing damage) | Art. 5(1)(f) (integrity & confidentiality principle breached) | Art. 6 (misuse of devices) |
| Financial Fraud & Laundering | §1030(a)(4); wire fraud 18 U.S.C. §1343 | Not directly applicable (financial crime, not a data-protection matter) unless personal data is exfiltrated as part of the fraud | Art. 8; Art. 25 (mutual legal assistance for cross-border mule/crypto tracing) |

## 5. Why Multiple Frameworks Apply Simultaneously

This case is deliberately structured to show that a single campaign
triggers **overlapping domestic and international liability**:

- The **spoofing and phishing stages** are primarily an *identity and
  communications integrity* crime (IT Act §66C/D, CFAA §1030(a)(4)).
- The **malware stage** converts the case into a *computer intrusion and
  damage* crime, invoking §43/§66 IT Act and CFAA §1030(a)(5).
- The **financial fraud/laundering stage** invokes an entirely separate body
  of law — PMLA in India, wire fraud statutes in the US — because money
  laundering is prosecuted independently of the underlying predicate
  computer crime.
- The **crypto layering step** is the clearest cross-border trigger: no
  single domestic law fully addresses wallet-to-wallet tracing across
  jurisdictions, which is why Budapest Convention Art. 25 (mutual legal
  assistance) is the practical mechanism investigators rely on, even where
  (as with India) the state is not a signatory but cooperates bilaterally
  using the same template.

## 6. Summary Table

| Stage | Primary IT Act | Primary IPC | Primary Global Law |
|---|---|---|---|
| Spoofing | §66C, §66D | §419, §465 | CFAA §1030(a)(4); Budapest Art. 7 |
| Phishing | §66D, §43 | §420, §468 | CFAA §1030(a)(2); Budapest Art. 8 |
| Unauthorized Access | §43, §66 | §379 | CFAA §1030(a)(2)/(5); Budapest Art. 2 |
| Malware Distribution | §43(c), §66 | §120B | CFAA §1030(a)(5); Budapest Art. 6 |
| Financial Fraud/Laundering | §66C/D | §420, §411; PMLA 2002 | Wire fraud §1343; Budapest Art. 25 |
