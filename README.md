# Operation Hydra

Operation Hydra is a cybersecurity investigation repository designed to analyze multi-vector digital threats, including email phishing, malware payloads, and financial fraud networks. This project organizes raw evidence, technical artifacts, analysis scripts, and final reporting into a structured investigation framework.

## Project Structure

* .github/ - Automated workflows for repository validation and markdown linting.
* docs/ - Threat taxonomy and classification documentation.
* financial_fraud/ - Transaction logs (card, UPI, cryptocurrency) and fraud flow tracing scripts.
* hashes/ - Cryptographic hashes (SHA-256) for file verification and integrity checks.
* malware_analysis/ - Simulated payload descriptions, extracted Indicators of Compromise (IOCs), and sandbox reports.
* phishing_spoofing/ - Raw email samples (.eml), header analysis, WHOIS lookups, and authentication reports (SPF, DKIM, DMARC).
* report/ - Comprehensive Legal and Technical Impact Report in PDF and DOCX formats.
* screenshots/ - Image evidence documenting analysis phases.
* tools/ - Documentation covering the technical utility suite used during analysis.

## Core Modules

### 1. Phishing and Email Spoofing Analysis
This module processes suspicious email files to identify spoofing attempts and malicious infrastructure.
* Header Parsing: Extracts routing paths, sender domains, and authentication results.
* IP Tracing: Maps originating IP addresses to external infrastructure.
* Domain Intel: Performs WHOIS lookups to identify domain registration age and ownership data.

### 2. Malware Analysis and IOC Extraction
Analyzes executable behavior and isolates actionable threat intelligence.
* Behavioral Description: Documents simulated payload activity within isolated environments.
* Sandbox Parsing: Extracts file, registry, and network indicators.
* IOC Generation: Outputs structured JSON and Markdown lists for integration with threat intelligence platforms.

### 3. Financial Fraud Flow Tracking
Tracks illegal monetary movement across multiple payment systems.
* Log Correlation: Cross-references credit card, UPI, and crypto wallet activity logs.
* Tracing Utility: Visualizes money movement paths from initial compromise to laundering endpoints.

## Getting Started

### Prerequisites
* Python 3.8 or higher
* Standard bash environment (Linux/macOS or WSL for Windows)

### Running Analysis Scripts

To run header analysis and IP tracing utilities:
```bash
python3 phishing_spoofing/scripts/parse_headers.py
python3 phishing_spoofing/scripts/ip_trace.py
