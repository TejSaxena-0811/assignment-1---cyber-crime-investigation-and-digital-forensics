# Cybercrime Classification & Legal Mapping
### Sub-Problem 1: Cybercrime Classification & Modelling

## 1. Crimes Identified in the Scenario

| # | Crime | Description in Scenario |
|---|---|---|
| 1 | ATM (Card) Skimming | Physical overlay skimmer + hidden camera installed on ATM to capture card track data and PIN |
| 2 | Credit/Debit Card Cloning | Captured track data used to produce cloned physical cards |
| 3 | Online / Card-Not-Present Fraud | Fraudulent app used for unauthorised online transactions using harvested card/OTP data |
| 4 | Identity Theft | Use of victims' card and personal data without authorisation |
| 5 | OTP/Phishing-style Social Engineering | SMS evidence shows OTPs being solicited/forwarded to complete fraudulent transactions |
| 6 | Money Laundering via Mule Accounts | Cash-out through third-party ("mule") bank accounts, cross-border coordination |
| 7 | Criminal Conspiracy | Coordinated roles: device planting, cloning, cash-out, overseas logistics |

## 2. Taxonomy of Cybercrimes Observed

```
Operation Phantom Swipe
├── Device-Based Crime
│   └── ATM Skimming (physical + electronic hybrid)
├── Data Crime
│   ├── Card Data Theft (skimming, cloning)
│   └── Identity Theft
├── Financial Crime (Cyber-enabled)
│   ├── Card-Not-Present Fraud
│   └── Money Laundering (mule network)
├── Social Engineering
│   └── OTP interception / phishing-style SMS
└── Organised Crime Element
    └── Cross-border conspiracy (India–UAE contact pattern)
```

**Justification for classification:** The scheme spans the full "cyber-physical"
spectrum — a purely physical act (mounting a skimmer) generates digital evidence
(track data) that is then exploited through purely cyber means (card-not-present
fraud, app-based fraud), and monetised through an organised, cross-border
laundering structure. This mixed-mode structure is why it maps to multiple,
overlapping statutory provisions rather than a single section.

## 3. Legal Mapping

### 3.1 Indian IT Act, 2000 (as amended)

| Section | Provision | Applicability |
|---|---|---|
| §43 | Penalty for damage to computer/computer system (unauthorised access, data theft) | Unauthorised extraction of card data via skimmer/fraud app |
| §66 | Computer-related offences (dishonestly/fraudulently doing an act referred in §43) | Overall fraudulent use of computer systems |
| §66C | Identity theft (fraudulent use of electronic signature, password, or unique identification) | Use of stolen card numbers/PINs |
| §66D | Cheating by personation using computer resource | Fake banking app used to impersonate legitimate bank |
| §72 | Breach of confidentiality and privacy | Unauthorised access/disclosure of card master list |

### 3.2 Indian Penal Code, 1860 (relevant provisions; IPC has since been
replaced by the Bharatiya Nyaya Sanhita, 2023 for new cases — both cited as the
assignment specifies IPC for the classification exercise)

| Section | Provision | Applicability |
|---|---|---|
| §420 | Cheating and dishonestly inducing delivery of property | Fraudulent withdrawal/transactions using cloned cards |
| §467/468/471 | Forgery of valuable security / forgery for cheating / using forged document | Cloned cards treated as forged financial instruments |
| §411 | Dishonestly receiving stolen property | Mule accounts receiving fraud proceeds |
| §120B | Criminal conspiracy | Coordinated multi-role fraud ring |
| §34 | Common intention | Joint liability of skimmer-planter, cloner, cash-out handlers |

### 3.3 International Framework — Budapest Convention on Cybercrime

| Article | Provision | Applicability |
|---|---|---|
| Art. 2 | Illegal access | Unauthorised access to card data systems |
| Art. 7 | Computer-related forgery | Cloned card data as forged electronic document |
| Art. 8 | Computer-related fraud | Card-not-present fraud via fake app |
| Art. 25 | Mutual legal assistance | Basis for India–UAE cooperation given overseas contact numbers in evidence |
| Art. 29–30 | Expedited preservation of stored data | Basis for requesting preservation of overseas telecom/exchange records |

> **Note on scope:** India is not a signatory to the Budapest Convention, but it
> is used here as the reference international framework because it is the most
> widely adopted cybercrime treaty and illustrates the *type* of cross-border
> cooperation mechanism (Art. 25, 29–30) that Indian agencies rely on via
> bilateral MLATs when a case has an international nexus, as this one does.

## 4. Summary Table — Crime-to-Law Mapping

| Crime | IT Act | IPC | Budapest Convention |
|---|---|---|---|
| ATM Skimming | §43, §66 | §420, §468 | Art. 2, 7 |
| Card Cloning | §66C | §467, §471 | Art. 7 |
| Online/CNP Fraud | §66D | §420 | Art. 8 |
| OTP Social Engineering | §66C, §66D | §420 | Art. 8 |
| Mule/Laundering | §72 (data misuse) | §411, §120B | Art. 25 (MLA) |
| Conspiracy | — | §120B, §34 | Art. 25 |
