#!/bin/bash
# generate_hashes.sh
# Sub-Problem 2: Electronic Evidence Collection Simulation
# Generates SHA-256 hashes for all acquired evidence files as part of
# chain-of-custody / integrity verification (analogous to running
# `sha256sum` immediately after imaging, before any analysis).

EVIDENCE_DIR="${1:-evidence}"
OUTFILE="${2:-hashes/sha256_hashes.txt}"

echo "SHA-256 Hash Manifest - Operation Phantom Swipe" > "$OUTFILE"
echo "Generated: $(date -u +'%Y-%m-%d %H:%M:%S UTC')" >> "$OUTFILE"
echo "==================================================" >> "$OUTFILE"

find "$EVIDENCE_DIR" -type f | sort | while read -r f; do
    hash=$(sha256sum "$f" | awk '{print $1}')
    printf "%-70s %s\n" "$f" "$hash" >> "$OUTFILE"
done

echo "Hashes written to $OUTFILE"
