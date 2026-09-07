# Cryptography Component
### Sub-Problem 4: Password Recovery Simulation & Discussion

## 1. Target

`evidence/password_protected/secure_vault.zip` (Exhibit C) — a standard
ZipCrypto-protected archive recovered from the suspect's storage, containing
the cloned-card master list and cash-out network notes.

## 2. Method

A dictionary attack was simulated using `cryptography/dictionary_attack.py`,
which is functionally equivalent to the real-world workflow of:

```
zip2john secure_vault.zip > vault.hash
john --wordlist=custom_wordlist.txt vault.hash
```

or the hashcat equivalent (`hashcat -m 17200 vault.hash wordlist.txt` for
legacy ZipCrypto, or `-m 13600` for WinZip AES). A pure-Python implementation
was used so the demonstration is fully reproducible in this environment
without external cracking binaries, while still performing a **real** attack
against the archive's own decryption check — each candidate is actually tried
against the ZIP's CRC/decryption mechanism, not just simulated with print
statements.

**Custom wordlist** (`wordlist_custom.txt`, 15 entries) was built from common
weak-password patterns plus scenario-relevant guesses (`skimmer1`,
`skimmer123`, `cardclone`, `cashout1`) — reflecting how real investigators
often seed wordlists with case-specific terms alongside generic breach lists
(e.g., `rockyou.txt`).

## 3. Result

```
Attempt 7: 'skimmer123' -> SUCCESS
RESULT: Password recovered = 'skimmer123' in 7 attempts, 0.0040s
```

Full run log: `cryptography/attack_log.txt`. The archive's SHA-256 hash was
verified identical before and after the attack, confirming the attack process
did not alter the evidence (see `hashes/sha256_hashes.txt`).

## 4. Ethical & Legal Implications: Brute-Forcing vs Lawful Decryption

| Aspect | Brute-force/Dictionary Attack | Lawful Decryption Request |
|---|---|---|
| **Legal basis** | Performed by law enforcement under a valid search/seizure warrant covering the specific device; still a self-help technical measure | Formal order under IT Act §69 (interception/decryption) directing the suspect or service provider to disclose the key |
| **When appropriate** | Weak, guessable passwords; time-critical investigation; suspect uncooperative | Strong passwords/proper encryption where brute-force is infeasible; compels a person legally obligated to comply |
| **Risk of overreach** | Can shade into compelled self-incrimination concerns if used to force a suspect to reveal a password rather than technically deriving it | Non-compliance may itself become an offence under IT Act §69(4) — but raises separate constitutional questions (right against self-incrimination, Art. 20(3)) |
| **Evidentiary integrity** | Must operate on a forensic copy only; original exhibit hash must remain unchanged (demonstrated above) | Password/key obtained directly; no risk to archive integrity from repeated attempts |
| **Practical limits** | Fails against strong, high-entropy passwords or salted/iterated KDFs within reasonable time | Depends on suspect/provider cooperation; can be slow (MLAT requests for overseas cooperation can take months) |

**Our position for this case:** because the recovered password (`skimmer123`)
was weak and guessable from a small, case-informed wordlist, dictionary attack
was a proportionate, low-cost first step. Had it failed, the appropriate
escalation would have been a formal §69 decryption direction rather than
resorting to more invasive extraction techniques.

## 5. Reflection on Password Strength in Criminal Scenarios

The recovered password (`skimmer123`) follows a common weak pattern seen in
real criminal casework: **a case-relevant word + short numeric suffix**. This
is consistent with published breach-analysis findings that weak, guessable
passwords remain widespread even among users handling sensitive/illicit data —
attackers (and here, investigators) frequently succeed precisely because
password choices leak context about the user (occupation, tools, environment)
rather than being random. This has two implications for investigators:

1. **Case-specific wordlists outperform generic ones** — seeding a wordlist
   with terms drawn from the case itself (device names, locations, jargon
   overheard in interviews) is often more efficient than a purely generic
   breach-corpus attack.
2. **It also cuts the other way** — the same weak-password tendency that
   helps investigators crack suspects' archives is a broader systemic risk;
   the same reasoning applies to protecting victims' own accounts, and should
   inform SOP recommendations around encouraging stronger authentication
   practices in consumer banking apps (see main report, Recommendations).
