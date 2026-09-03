# Tools Used — With Commands and Justifications

## Custom Scripts (this repository)

| Tool | Command | Justification |
|---|---|---|
| `phishing_spoofing/scripts/parse_headers.py` | `python3 parse_headers.py phishing_spoofing/email_samples phishing_spoofing/header_analysis.md` | Parses real `.eml` structure to extract SPF/DKIM/DMARC and flag spoofing indicators — reproducible, no external API dependency |
| `phishing_spoofing/scripts/ip_trace.py` | `python3 ip_trace.py phishing_spoofing/email_samples phishing_spoofing/threat_intel.json phishing_spoofing/ip_trace_results.md` | Extracts relay IPs from headers and cross-references a threat-intel table, mirroring an AbuseIPDB/VirusTotal bulk lookup workflow |
| `malware_analysis/scripts/ioc_extractor.py` | `python3 ioc_extractor.py malware_analysis/sandbox_report.md malware_analysis/extracted_iocs.json` | Same category of tool as CyberChef's "Extract IOCs" recipe — regex-based extraction of IPs, hashes, registry keys, and paths from analyst notes/logs |
| `financial_fraud/scripts/trace_fraud_flow.py` | `python3 trace_fraud_flow.py financial_fraud/logs financial_fraud/fraud_flow_trace.md` | Reconstructs victim→mule→crypto money flow from CSV transaction logs and flags structuring patterns |
| `hashes/generate_hashes.sh` | `bash hashes/generate_hashes.sh` | Generates a SHA-256 integrity manifest for all evidence-like files |

## Reference Tools (industry-standard equivalents)

These are the real-world tools this repository's custom scripts stand in
for, given the offline/sandboxed nature of this academic environment
(no external network access to live APIs):

| Tool | Purpose | Where it would be used |
|---|---|---|
| **MXToolbox** (mxtoolbox.com) | Live SPF/DKIM/DMARC record lookup and header analyzer | Would replace `parse_headers.py`'s authentication parsing with live DNS queries against the real domains |
| **VirusTotal** | File hash / URL / IP reputation lookup | Would replace the simulated `threat_intel.json` lookup table in `ip_trace.py` |
| **AbuseIPDB** | IP abuse-confidence scoring | Same role as VirusTotal above, specifically for IP reputation |
| **WHOIS (CLI or whois.domaintools.com)** | Domain registration lookup | Would replace the simulated records in `phishing_spoofing/whois_lookup_results.md` |
| **CyberChef** (gchq.github.io/CyberChef) | Recipe-based data decoding/IOC extraction | Equivalent function to `ioc_extractor.py`, and would be used to decode any real Base64/obfuscated macro content |
| **Any.Run / Joe Sandbox** | Live malware detonation sandbox | Would replace the simulated timeline in `malware_analysis/sandbox_report.md` with actual behavioral telemetry |
| **zip2john / John the Ripper / hashcat** | Password recovery | Referenced pattern from Assignment 1; not required for this assignment's scope |

## Why Custom Scripts Instead of Live Tools

This assignment is conducted in an isolated academic environment without
credentials for VirusTotal/AbuseIPDB APIs and without network access to
query live DNS/WHOIS records for domains that are themselves fictitious
(they do not exist in real DNS). The custom Python scripts reproduce the
**analytical logic** of each tool (regex-based IOC extraction, header
authentication parsing, money-flow graph reconstruction) so that the
methodology is transparent, reproducible, and directly gradable, while the
mapping table above shows exactly which live tool each script represents.
