# Validation Report

## Result: PASS

| Check | Result |
|---|---:|
| Technical records | 10,000 |
| Unique record IDs | 10,000 |
| Source hashes verified | 10,000 |
| Topics | 47 |
| Proficiency tiers | 6 |
| Positive corpus records | 7,727 |
| Negative corpus records | 2,213 |
| Certification corpus records | 60 |
| `.ebnf` scripts | 1,000 |
| Script catalog rows | 1,000 |
| Certification holdouts in pack | 60 of 60 |
| Textbook chapters | 22 |
| Textbook words | 14,141 |
| Maximum relative path | 93 characters |
| Manifest/checksum status | generated |

## Structural gates

- Required JA Certifier header, module, no-unknown-code policy, no-network policy, and grammar declaration were checked for every curated script. Certification, validation, analysis, normalization, lowering, and packaging commands remain source-specific and are indexed in the script catalog.
- Brace balance and source hashes were verified.
- All 47 topics and all six tiers are represented.
- The script pack contains exactly 750 positive, 190 negative, and 60 certification programs.
- Tier distribution is exactly 100/150/250/250/150/100.
- All 60 certification holdouts are included.
- Source, semantic, AST, compiler, runtime, validation, optimization, provenance, and coupling-mechanics layers are present in the normalized corpus.

## Native execution boundary

A native JA Certifier compiler, parser generator, validator host, certificate signer, and R12/MCRT runtime were not supplied. The report does not claim native compilation, parser performance, signature verification, benchmark results, or production certification authority.
