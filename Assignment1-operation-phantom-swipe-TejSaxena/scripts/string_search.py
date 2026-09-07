#!/usr/bin/env python3
"""
string_search.py
-----------------
Sub-Problem 3: Electronic Media Search and Analysis.

Performs a simple forensic string search (akin to `strings` + `grep`)
across seized evidence files, looking for patterns of interest:
card-number-like sequences, phone numbers, GPS coordinates, and
suspicious keywords. Logs every hit with source file + byte offset
for the evidence log.

Usage:
    python3 string_search.py <evidence_dir> <output_log>
"""
import sys
import os
import re
import time

PATTERNS = {
    "card_number_like": re.compile(rb"\d{4}X{6,8}\d{4}|\d{13,19}"),
    "phone_number": re.compile(rb"\+\d{1,3}-\d{2,3}-?\d{4,10}"),
    "gps_coordinate": re.compile(rb"-?\d{1,3}\.\d{4,6}"),
    "keyword_hit": re.compile(rb"(?i)(otp|cash-?out|clone|skimmer|mule|batch)"),
}

def search_file(path, logf):
    with open(path, "rb") as f:
        data = f.read()
    hits = 0
    for label, pattern in PATTERNS.items():
        for m in pattern.finditer(data):
            hits += 1
            snippet = data[max(0, m.start()-10):m.end()+10]
            logf.write(f"{path} | offset={m.start()} | type={label} | match={m.group().decode(errors='replace')}\n")
    return hits

def main(evidence_dir, out_log):
    ts = time.strftime("%Y-%m-%d %H:%M:%S")
    total_hits = 0
    total_files = 0
    with open(out_log, "w") as logf:
        logf.write(f"=== Forensic String Search Log - {ts} ===\n")
        logf.write(f"Target directory: {evidence_dir}\n\n")
        for root, _, files in os.walk(evidence_dir):
            for fn in files:
                path = os.path.join(root, fn)
                total_files += 1
                try:
                    total_hits += search_file(path, logf)
                except Exception as e:
                    logf.write(f"{path} | ERROR: {e}\n")
        logf.write(f"\n=== Summary: {total_files} files scanned, {total_hits} pattern matches found ===\n")
    print(f"Scanned {total_files} files, found {total_hits} matches. Log: {out_log}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 string_search.py <evidence_dir> <output_log>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
