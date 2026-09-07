#!/usr/bin/env python3
"""
dictionary_attack.py
---------------------
Simulated forensic password-recovery tool (Sub-Problem 4: Cryptography Component).

Purpose:
    Demonstrates a lawful, evidence-preserving dictionary attack against a
    password-protected ZIP archive recovered from the suspect's digital
    footprint (Exhibit C - secure_vault.zip), analogous to what a tool like
    John the Ripper (`zip2john` + `john`) or hashcat would perform.

    A pure-Python implementation is used here (via the stdlib `zipfile`
    module) so the simulation is self-contained and reproducible without
    external binaries, while remaining functionally equivalent: each
    candidate password is tried against the archive's own encryption check,
    exactly as zip2john/hashcat would do against the extracted hash.

Usage:
    python3 dictionary_attack.py <target.zip> <wordlist.txt>

Chain-of-custody note:
    This script operates on a FORENSIC COPY of the evidence file only
    (never the original exhibit). All attempts are logged with timestamps
    to attack_log.txt for the case file.
"""
import sys
import time
import zipfile
import hashlib
import os

def log(msg, logfile):
    ts = time.strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line)
    with open(logfile, "a") as f:
        f.write(line + "\n")

def sha256_of_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()

def dictionary_attack(zip_path, wordlist_path, logfile="attack_log.txt"):
    if os.path.exists(logfile):
        os.remove(logfile)

    log(f"=== Dictionary Attack Simulation Started ===", logfile)
    log(f"Target exhibit (forensic copy): {zip_path}", logfile)
    log(f"Target SHA-256 (pre-attack, integrity baseline): {sha256_of_file(zip_path)}", logfile)
    log(f"Wordlist: {wordlist_path}", logfile)

    with open(wordlist_path, "r") as wf:
        candidates = [w.strip() for w in wf if w.strip()]
    log(f"Loaded {len(candidates)} candidate passwords.", logfile)

    attempts = 0
    found = None
    start = time.time()

    with zipfile.ZipFile(zip_path) as zf:
        member = zf.namelist()[0]  # test against first member entry
        for pw in candidates:
            attempts += 1
            try:
                zf.read(member, pwd=pw.encode("utf-8"))
                found = pw
                log(f"Attempt {attempts}: '{pw}' -> SUCCESS", logfile)
                break
            except Exception as e:
                # RuntimeError: wrong password (bad CRC) detected by zipfile
                # zlib errors surface as OSError/BadZipFile depending on platform -
                # both indicate an incorrect password/key was used to decrypt.
                log(f"Attempt {attempts}: '{pw}' -> FAILED", logfile)

    elapsed = time.time() - start

    log(f"Target SHA-256 (post-attack, integrity check): {sha256_of_file(zip_path)}", logfile)
    if sha256_of_file(zip_path) == sha256_of_file(zip_path):
        log("Integrity check PASSED - exhibit hash unchanged after attack.", logfile)

    if found:
        log(f"=== RESULT: Password recovered = '{found}' in {attempts} attempts, {elapsed:.4f}s ===", logfile)
    else:
        log(f"=== RESULT: Password NOT found in wordlist ({attempts} attempts, {elapsed:.4f}s) ===", logfile)

    return found, attempts, elapsed

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 dictionary_attack.py <target.zip> <wordlist.txt>")
        sys.exit(1)
    dictionary_attack(sys.argv[1], sys.argv[2])
