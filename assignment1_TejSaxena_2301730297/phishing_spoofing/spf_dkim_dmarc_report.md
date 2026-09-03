# SPF / DKIM / DMARC Analysis Report

## Background

SPF, DKIM, and DMARC are the three standard email-authentication mechanisms
used to detect spoofed sender addresses:

- **SPF (Sender Policy Framework):** checks whether the sending mail
  server's IP is authorised in the claimed domain's DNS `TXT` record.
- **DKIM (DomainKeys Identified Mail):** verifies a cryptographic signature
  in the message header against the sending domain's published public key.
- **DMARC (Domain-based Message Authentication, Reporting & Conformance):**
  builds on SPF/DKIM, declaring what a receiving server should do
  (`none` / `quarantine` / `reject`) when both checks fail, and requiring
  *alignment* between the visible `From:` domain and the domain that
  actually passed SPF/DKIM.

## Per-Sample Results

| Sample | SPF | DKIM | DMARC | Verdict |
|---|---|---|---|---|
| 01 — Invoice scam | FAIL | NONE | FAIL | Spoofed sender; message should have been rejected by a policy-enforcing mail gateway |
| 02 — Bank alert | FAIL | FAIL | FAIL | Fully spoofed; sending IP unauthorised AND signature invalid |
| 03 — HR payroll | SOFTFAIL | NONE | FAIL | Spoofed internal domain; SPF softfail means the record allows but flags this IP — weak SPF policy on victim's own domain is itself a finding |
| 04 — Delivery notice | FAIL | NONE | FAIL | Spoofed courier brand; no legitimate authentication present at all |

## Key Finding: Why These Emails Reached Inboxes

All four messages **failed at least SPF and DMARC**, meaning a properly
configured receiving mail server with `p=reject` DMARC enforcement should
have blocked or quarantined them before they reached any inbox. Two
explanations are consistent with the evidence:

1. **The recipient (Nimbus Logistics) mail gateway does not enforce DMARC
   policy** on inbound mail (common misconfiguration — DMARC protects your
   *own* domain from being spoofed *outbound*, but does not automatically
   protect *inbound* mail unless the receiving server is configured to
   honor senders' DMARC policies).
2. **Sample 03 reveals a second, more serious gap:** the victim
   organisation's own domain (`nimbuslogistics.example.com`) returned
   `dmarc=fail (p=none)` — meaning Nimbus Logistics' own DMARC record is
   set to monitor-only, not enforce. This allowed an internal-brand
   impersonation domain to be used against their own employees.

## Recommendation

- Move Nimbus Logistics' outbound DMARC policy from `p=none` to
  `p=quarantine` (with monitoring) and eventually `p=reject`.
- Configure the inbound mail gateway to explicitly action `Authentication-Results`
  headers (reject/quarantine on DMARC fail) rather than relying on end-user
  judgement.
- Enable BIMI (Brand Indicators for Message Identification) once DMARC is at
  `p=reject`, so verified Nimbus/partner mail displays a visible trust logo,
  making unauthenticated look-alikes more visibly suspicious to employees.
