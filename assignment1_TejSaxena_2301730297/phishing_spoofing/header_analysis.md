# Phishing Email Header Analysis Report

Samples analyzed: 4

## sample_01_invoice_scam.eml

- **Subject:** URGENT: Unpaid Invoice #INV-88213 - Account Suspension Notice
- **From:** SecureTrust Bank - Billing <billing@secure-trustbank.co>
- **Return-Path:** <billing@secure-trustbank.co>
- **Originating IP:** [185.220.101.47]
- **SPF:** fail | **DKIM:** none | **DMARC:** fail
- **Embedded links:** http://secure-trustbank.co.paynow-verify.info/invoice/88213
- **Has attachment:** True
- **Red flags:**
  - SPF FAIL - sending IP not authorised for this domain
  - DKIM NONE - message signature missing/invalid
  - DMARC FAIL - policy alignment failed, likely spoofed sender
  - Suspicious/lookalike link: http://secure-trustbank.co.paynow-verify.info/invoice/88213
  - Contains attachment - potential malware delivery vector

## sample_02_bank_alert.eml

- **Subject:** Suspicious Login Detected - Verify Your Identity Now
- **From:** HDFC Bank Security <alerts@hdfcbank-secure.info>
- **Return-Path:** <alerts@hdfcbank-secure.info>
- **Originating IP:** [103.224.182.19]
- **SPF:** fail | **DKIM:** fail | **DMARC:** fail
- **Embedded links:** http://hdfcbank-secure.info.verify-id-portal.top/login
- **Has attachment:** False
- **Red flags:**
  - SPF FAIL - sending IP not authorised for this domain
  - DKIM FAIL - message signature missing/invalid
  - DMARC FAIL - policy alignment failed, likely spoofed sender
  - Suspicious/lookalike link: http://hdfcbank-secure.info.verify-id-portal.top/login

## sample_03_hr_payroll.eml

- **Subject:** Updated Salary Structure - Action Required by Friday
- **From:** Nimbus HR Payroll <hr-payroll@nimbuslogistics-hr.net>
- **Return-Path:** <hr-payroll@nimbuslogistics-hr.net>
- **Originating IP:** [45.148.10.77]
- **SPF:** softfail | **DKIM:** none | **DMARC:** fail
- **Embedded links:** None
- **Has attachment:** True
- **Red flags:**
  - SPF SOFTFAIL - sending IP not authorised for this domain
  - DKIM NONE - message signature missing/invalid
  - DMARC FAIL - policy alignment failed, likely spoofed sender
  - Contains attachment - potential malware delivery vector

## sample_04_delivery_notice.eml

- **Subject:** Delivery Failed - Package #BD991234521 Awaiting Customs Fee
- **From:** BlueDart Express <tracking@bluedart-express.info>
- **Return-Path:** <tracking@bluedart-express.info>
- **Originating IP:** [176.113.115.204]
- **SPF:** fail | **DKIM:** none | **DMARC:** fail
- **Embedded links:** http://bluedart-express.info.pay-customs-fee.click/pay
- **Has attachment:** False
- **Red flags:**
  - SPF FAIL - sending IP not authorised for this domain
  - DKIM NONE - message signature missing/invalid
  - DMARC FAIL - policy alignment failed, likely spoofed sender
  - Suspicious/lookalike link: http://bluedart-express.info.pay-customs-fee.click/pay

