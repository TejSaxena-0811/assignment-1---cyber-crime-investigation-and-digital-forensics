### Name: Tej Saxena

### Roll Number: 2301730297

### Course: B.Tech CSE (AI-ML)

### Semester: 7

### Section: E

### Subject: Cyber Crime and Digital Forensics Lab

### Professor: Mr. Anuj Tiwari

--------------------------------------------------------------------

# Assignment 1 (Operation Phantom Swipe)

This project is a digital forensics investigation repository designed to analyze cross-border financial threats, including physical ATM skimming, mobile credential harvesting, password-protected vaults, and international money laundering networks[cite: 1, 2, 7]. This project organizes raw evidence, technical artifacts, analysis scripts, and final reporting into a structured investigation framework[cite: 2, 3].

## Project Structure

* .github/ - Automated workflows for repository structure validation[cite: 3].
* artefacts/ - Extracted forensic artifacts, string search hit logs, and evidentiary findings[cite: 2, 3].
* chain_of_custody/ - Official evidence tracking form and custody transfer documentation[cite: 2, 3].
* cryptography/ - Password cracking simulation scripts, custom wordlists, attack logs, and forensic working copies[cite: 2, 3].
* docs/ - Cybercrime taxonomy and legal mapping (IT Act, IPC, Budapest Convention)[cite: 2, 3].
* evidence/ - Simulated physical and digital evidence (skimmer memory dumps, phone logs, APKs, encrypted archive)[cite: 2, 3].
* hashes/ - Master SHA-256 cryptographic hash manifest for integrity verification[cite: 2, 3].
* report/ - Comprehensive Legal and Technical Investigation Report in DOCX and PDF formats[cite: 2, 3].
* screenshots/ - Terminal verification images documenting script executions and analysis phases[cite: 2, 3].
* scripts/ - Automated forensic utilities for hash manifest generation and regex string searching[cite: 2, 3].

## Core Modules

### 1. Cybercrime Classification and Legal Mapping
This module categorizes observed criminal activities and maps them against relevant statutory frameworks[cite: 1, 2, 7].
* Scenario Identification: Identifies physical skimming, card cloning, CNP fraud, identity theft, and cross-border conspiracy[cite: 1, 2, 9].
* Statutory Provisions: Maps offenses to the Indian IT Act (2000), Indian Penal Code (1860), and Budapest Convention[cite: 1, 2, 9].
* Taxonomy Justification: Differentiates between cyber-dependent and cyber-enabled criminal operations[cite: 2, 9].

### 2. Evidence Handling and Chain of Custody
Ensures forensic integrity and legal admissibility under digital evidence standards (ISO/IEC 27037)[cite: 2, 7, 14].
* Seizure Protocols: Implements radio frequency shielding (Faraday isolation) and physical write-blockers[cite: 2, 7, 14].
* Custody Logging: Maintains timestamped records of exhibit transfers and handler details[cite: 2, 14].
* Cryptographic Hashing: Generates pre- and post-analysis SHA-256 hash digests to prove data immutability[cite: 2, 7, 14].

### 3. Media Search and Artefact Extraction
Parses unstructured memory dumps and structured phone logs to isolate actionable evidence[cite: 2, 4, 16].
* Automated Search: Executes regular expressions to scan for card numbers, phone numbers, GPS coordinates, and keywords[cite: 2, 4].
* Geographic & Communication Linking: Extracts coordinates placing the suspect at the scene and identifies overseas contact numbers[cite: 2, 7, 16].
* Software Inspection: Isolates malicious APK binaries used for credential harvesting and card data generation[cite: 2, 7, 16].

### 4. Cryptographic Analysis and Password Recovery
Performs lawful recovery of password-protected digital evidence[cite: 1, 2, 7].
* Dictionary Attack Simulation: Operates on isolated forensic copies using targeted case-informed wordlists[cite: 2, 7, 11, 12].
* Integrity Auditing: Logs execution attempts while verifying exhibit hash consistency before and after cracking[cite: 2, 11, 12, 13].
* Legal & Ethical Assessment: Compares technical brute-forcing against statutory decryption directives under IT Act Section 69[cite: 2, 7, 12].

## Getting Started

### Prerequisites
* Python 3.8 or higher[cite: 3]
* Standard bash environment (Linux/macOS or WSL for Windows)[cite: 3]

### Running Analysis Scripts

To generate evidence hashes, perform string search, and run password recovery:
```bash
bash scripts/generate_hashes.sh evidence hashes/sha256_hashes.txt
python3 scripts/string_search.py evidence artefacts/string_search_results.txt
python3 cryptography/dictionary_attack.py cryptography/forensic_copy/secure_vault_COPY.zip cryptography/wordlist_custom.txt
