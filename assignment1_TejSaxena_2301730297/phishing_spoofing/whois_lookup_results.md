# WHOIS Lookup Results — Spoofed / Lookalike Domains

*Note: These are simulated WHOIS records constructed for academic analysis
(live `whois` queries against fictitious domains are not possible). Format
and fields mirror real WHOIS output structure.*

## 1. secure-trustbank.co (used in Sample 01)

```
Domain Name: SECURE-TRUSTBANK.CO
Registrar: NameCheap-Style Registrar (simulated)
Creation Date: 2026-07-29T02:14:00Z   <-- registered 5 days before campaign
Registrant Organization: REDACTED FOR PRIVACY
Registrant Country: PA (Panama)
Name Server: NS1.BULLETPROOF-DNS.NET
Name Server: NS2.BULLETPROOF-DNS.NET
DNSSEC: unsigned
```
**Analysis:** Domain registered days before the phishing campaign began —
classic indicator of a disposable phishing domain. Legitimate "SecureTrust
Bank" domain (securetrustbank.com) is a different TLD/spelling entirely;
`.co` + hyphen is a common typosquat pattern.

## 2. hdfcbank-secure.info (used in Sample 02)

```
Domain Name: HDFCBANK-SECURE.INFO
Registrar: Budget Registrar Inc. (simulated)
Creation Date: 2026-08-01T11:02:00Z   <-- registered 3 days before campaign
Registrant Organization: Privacy-protected
Registrant Country: Unknown (privacy proxy)
Name Server: NS1.FREEHOST-ASIA.NET
```
**Analysis:** Combines the real brand name "hdfcbank" with "-secure" and a
low-cost `.info` TLD — a textbook brand-impersonation pattern. The real
HDFC Bank domain is hdfcbank.com.

## 3. nimbuslogistics-hr.net (used in Sample 03 — internal brand impersonation)

```
Domain Name: NIMBUSLOGISTICS-HR.NET
Registrar: Budget Registrar Inc. (simulated)
Creation Date: 2026-08-02T06:40:00Z
Registrant Organization: Privacy-protected
Name Server: NS1.CHEAPBULKMAIL.BIZ
```
**Analysis:** This is the most dangerous sample — it impersonates the
victim organisation's *own* HR domain (nimbuslogistics.example.com) rather
than an outside brand, exploiting internal trust to distribute a
macro-enabled spreadsheet to employees directly.

## 4. bluedart-express.info (used in Sample 04)

```
Domain Name: BLUEDART-EXPRESS.INFO
Registrar: Budget Registrar Inc. (simulated)
Creation Date: 2026-08-04T18:55:00Z
Registrant Organization: Privacy-protected
Name Server: NS1.ROTATING-PROXY-FARM.NET
```
**Analysis:** Courier/delivery-fee scam pattern; real BlueDart domain is
bluedart.com. Low-value fee request (INR 349) is a deliberate social
engineering choice — small enough that victims often pay without scrutiny.

## Summary Pattern

All four domains share common infrastructure fingerprints:
- Registered within days of the phishing campaign (disposable domains)
- Privacy-protected or redacted registrant information
- Hosted on the same class of low-cost/bulletproof name servers
- Use hyphenation + brand name + trust-signal word ("secure", "verify") on
  low-cost TLDs (.info, .co, .net, .top, .click)

This pattern strongly suggests a single threat actor or affiliate group
operating a **domain-generation-as-a-service** style phishing kit, rather
than four unrelated campaigns.
