#!/usr/bin/env python3
"""
ip_trace.py
-----------
Sub-Problem 2: Phishing & Spoofing Investigation.

Extracts originating/relay IP addresses from the Received header chain of
each .eml sample and cross-references them against a local simulated
threat-intelligence lookup table (standing in for live AbuseIPDB/VirusTotal
API queries, which require external network access and API keys not
available in this offline academic environment).

In a live investigation this script's output structure matches what you
would get by querying:
    - https://www.abuseipdb.com/check/<ip>
    - https://www.virustotal.com/gui/ip-address/<ip>
    - whois <ip>  /  whois <domain>

Usage:
    python3 ip_trace.py <email_samples_dir> <threat_intel.json> <output_report>
"""
import sys
import os
import re
import json
import email
from email import policy

IP_RE = re.compile(r"\[(\d{1,3}(?:\.\d{1,3}){3})\]|(?<!\d)(\d{1,3}(?:\.\d{1,3}){3})(?!\d)")

def extract_ips(msg):
    ips = set()
    for header_val in msg.get_all("Received", []) + [msg.get("X-Originating-IP", "")]:
        for m in IP_RE.finditer(header_val or ""):
            ip = m.group(1) or m.group(2)
            if ip and not ip.startswith(("10.", "127.", "192.168.")):
                ips.add(ip)
    return ips

def main(samples_dir, intel_path, out_path):
    with open(intel_path) as f:
        intel = json.load(f)

    files = sorted(f for f in os.listdir(samples_dir) if f.endswith(".eml"))
    with open(out_path, "w") as out:
        out.write("# IP Trace & Threat Intelligence Cross-Reference\n\n")
        out.write("*Simulated AbuseIPDB / VirusTotal / WHOIS lookups (offline reference table `threat_intel.json`)*\n\n")
        for fn in files:
            with open(os.path.join(samples_dir, fn), "rb") as f:
                msg = email.message_from_binary_file(f, policy=policy.default)
            ips = extract_ips(msg)
            out.write(f"## {fn}\n\n")
            if not ips:
                out.write("No external IPs found in headers.\n\n")
                continue
            for ip in sorted(ips):
                info = intel.get(ip, {"abuse_score": "unknown", "country": "unknown",
                                       "isp": "unknown", "reports": 0, "category": "unclassified"})
                out.write(f"- **{ip}** — Abuse Confidence: {info['abuse_score']}% | "
                          f"Country: {info['country']} | ISP: {info['isp']} | "
                          f"Reports: {info['reports']} | Category: {info['category']}\n")
            out.write("\n")
    print(f"IP trace complete -> {out_path}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 ip_trace.py <email_samples_dir> <threat_intel.json> <output_report>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2], sys.argv[3])
