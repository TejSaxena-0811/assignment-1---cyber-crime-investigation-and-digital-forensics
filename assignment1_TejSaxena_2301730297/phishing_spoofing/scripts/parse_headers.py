#!/usr/bin/env python3
"""
parse_headers.py
-----------------
Sub-Problem 2: Phishing & Spoofing Investigation.

Parses .eml phishing samples and extracts key forensic header fields:
From, Return-Path, Received chain, Authentication-Results (SPF/DKIM/DMARC),
Originating IP, and any embedded links. This mirrors the manual header
analysis an investigator would perform via a mail client's "show original"
view or a tool like MXToolbox's header analyzer.

Usage:
    python3 parse_headers.py <email_samples_dir> <output_report>
"""
import sys
import os
import re
import email
from email import policy

def extract_links(msg):
    links = set()
    for part in msg.walk():
        if part.get_content_type() in ("text/html", "text/plain"):
            try:
                body = part.get_content()
            except Exception:
                continue
            links.update(re.findall(r'href="([^"]+)"', body))
            links.update(re.findall(r'https?://[^\s"<>]+', body))
    return links

def analyze_file(path):
    with open(path, "rb") as f:
        msg = email.message_from_binary_file(f, policy=policy.default)

    auth = msg.get("Authentication-Results", "NOT PRESENT")
    spf = re.search(r"spf=(\w+)", auth)
    dkim = re.search(r"dkim=(\w+)", auth)
    dmarc = re.search(r"dmarc=(\w+)", auth)

    result = {
        "file": os.path.basename(path),
        "from": msg.get("From", ""),
        "return_path": msg.get("Return-Path", ""),
        "subject": msg.get("Subject", ""),
        "originating_ip": msg.get("X-Originating-IP", "NOT PRESENT"),
        "spf": spf.group(1) if spf else "NOT FOUND",
        "dkim": dkim.group(1) if dkim else "NOT FOUND",
        "dmarc": dmarc.group(1) if dmarc else "NOT FOUND",
        "received_chain": msg.get_all("Received", []),
        "links": sorted(extract_links(msg)),
        "has_attachment": any(part.get_filename() for part in msg.walk()),
    }
    return result

def flag_indicators(r):
    flags = []
    from_domain = re.search(r"@([\w.-]+)", r["from"])
    from_domain = from_domain.group(1) if from_domain else ""
    return_domain = re.search(r"@([\w.-]+)", r["return_path"])
    return_domain = return_domain.group(1) if return_domain else ""

    if r["spf"] in ("fail", "softfail"):
        flags.append(f"SPF {r['spf'].upper()} - sending IP not authorised for this domain")
    if r["dkim"] in ("fail", "none"):
        flags.append(f"DKIM {r['dkim'].upper()} - message signature missing/invalid")
    if r["dmarc"] in ("fail",):
        flags.append("DMARC FAIL - policy alignment failed, likely spoofed sender")
    if from_domain and return_domain and from_domain != return_domain:
        flags.append(f"From/Return-Path domain mismatch: {from_domain} vs {return_domain}")
    for link in r["links"]:
        if any(susp in link for susp in [".info", ".top", ".click", "-verify", "-secure.", "paynow", "pay-customs"]):
            flags.append(f"Suspicious/lookalike link: {link}")
    if r["has_attachment"]:
        flags.append("Contains attachment - potential malware delivery vector")
    return flags

def main(samples_dir, out_path):
    files = sorted(f for f in os.listdir(samples_dir) if f.endswith(".eml"))
    with open(out_path, "w") as out:
        out.write("# Phishing Email Header Analysis Report\n\n")
        out.write(f"Samples analyzed: {len(files)}\n\n")
        for fn in files:
            r = analyze_file(os.path.join(samples_dir, fn))
            flags = flag_indicators(r)
            out.write(f"## {r['file']}\n\n")
            out.write(f"- **Subject:** {r['subject']}\n")
            out.write(f"- **From:** {r['from']}\n")
            out.write(f"- **Return-Path:** {r['return_path']}\n")
            out.write(f"- **Originating IP:** {r['originating_ip']}\n")
            out.write(f"- **SPF:** {r['spf']} | **DKIM:** {r['dkim']} | **DMARC:** {r['dmarc']}\n")
            out.write(f"- **Embedded links:** {', '.join(r['links']) if r['links'] else 'None'}\n")
            out.write(f"- **Has attachment:** {r['has_attachment']}\n")
            out.write(f"- **Red flags:**\n")
            for fl in flags:
                out.write(f"  - {fl}\n")
            out.write("\n")
    print(f"Analyzed {len(files)} email samples -> {out_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 parse_headers.py <email_samples_dir> <output_report>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
