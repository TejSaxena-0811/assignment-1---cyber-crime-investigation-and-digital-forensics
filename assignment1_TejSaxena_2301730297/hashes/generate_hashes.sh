#!/bin/bash
# generate_hashes.sh
# Generates SHA-256 hashes for all evidence-like artefacts (email samples,
# logs, IOC files) for integrity verification / case file inclusion.

OUTFILE="hashes/sha256_hashes.txt"
echo "SHA-256 Hash Manifest - Operation Hydra" > "$OUTFILE"
echo "Generated: $(date -u +'%Y-%m-%d %H:%M:%S UTC')" >> "$OUTFILE"
echo "==================================================" >> "$OUTFILE"

for dir in phishing_spoofing/email_samples financial_fraud/logs malware_analysis; do
    find "$dir" -type f \( -name "*.eml" -o -name "*.csv" -o -name "*.md" -o -name "*.json" \) | sort | while read -r f; do
        hash=$(sha256sum "$f" | awk '{print $1}')
        printf "%-60s %s\n" "$f" "$hash" >> "$OUTFILE"
    done
done
echo "Hashes written to $OUTFILE"
