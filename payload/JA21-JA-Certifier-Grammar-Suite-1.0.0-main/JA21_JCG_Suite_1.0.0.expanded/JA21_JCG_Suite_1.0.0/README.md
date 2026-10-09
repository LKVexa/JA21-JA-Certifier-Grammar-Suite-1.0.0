# JA21 JA Certifier Grammar Suite 1.0.0

> A standalone, air-gap-safe language suite for EBNF grammar definition, parser analysis, validator orchestration, evidence management, and language certification.

## Editorial lenses

| Lens | Responsibility |
|---|---|
| **SOPHIA** | semantic integrity, claim boundaries, certification truthfulness, and evidence discipline |
| **CHARLOTTE** | taxonomy, corpus architecture, terminology, navigation, and editorial coherence |
| **LANDON** | parser/compiler contracts, validators, R12/MCRT lowering, diagnostics, and release engineering |
| **Professor** | textbook, laboratories, curriculum, assessment, and learning progression |
| **Podium** | publication design, visual hierarchy, evidence cards, reader pathways, and institutional finish |

## At a glance

- **10,000** normalized technical records
- **1,000** curated source-faithful `.ebnf` programs
- **47** grammar and certification topics
- **6** proficiency tiers
- **60** certification holdouts, all included in the script pack
- **22-chapter** textbook
- Twelve-week curriculum, workbook, and instructor guide
- Grammar, compiler, runtime, semantic-operator, R12/MCRT, and conformance specifications
- Offline inspection and structural validation tools
- Preserved Smithson 8S annotations with explicit claim boundaries

## Suite map

```text
JA21_JCG_Suite_1.0.0/
├── corpus/          normalized records, shards, schemas, and indexes
├── scripts/         1,000 curated JA Certifier programs
├── catalogs/        topics, scripts, diagnostics, architecture, reading paths
├── textbook/        complete 22-chapter technical textbook
├── education/       curriculum, workbook, instructor guide
├── specifications/  grammar, compiler, runtime, R12/MCRT, conformance
├── starter/         minimal practical grammar project
├── design/          offline publication system and cover
├── tools/           corpus inspection and suite validation
├── reference_source/ reconstructed source and preserved wrapper
└── manifests/       inventory and SHA-256 evidence
```

## Validation boundary

No native JA Certifier compiler, parser generator, certificate signer, validator host, or R12/MCRT runtime was included. This release validates record integrity, source hashes, script structure, policy declarations, catalogs, provenance, path safety, and package consistency. It does not claim native parsing, benchmark performance, cryptographic authority, or production certification.

## Start here

1. Read `SUITE_CATALOG.md`.
2. Open `textbook/JA21_JA_CERTIFIER_GRAMMAR_TEXTBOOK.md`.
3. Copy `starter/hello_certifier.ebnf` into a test workspace.
4. Search `catalogs/SCRIPT_CATALOG.csv`.
5. Run `python tools/validate_suite.py`.

## Corpus and pack by tier

| Tier | Name | Corpus | Script pack |
|---:|---|---:|---:|
| 1 | Basic Syntax | 1,000 | 100 |
| 2 | Intermediate Grammar | 1,500 | 150 |
| 3 | Advanced Analysis | 2,500 | 250 |
| 4 | Expert Validation | 2,500 | 250 |
| 5 | Compiler Integration | 1,500 | 150 |
| 6 | Validation Certification | 1,000 | 100 |

## License and provenance

JA21-JA-Certifier-Grammar-Suite-1.0.0 (C) 2026 RUSSELL PHILIP SMITHSON

This published repository is licensed under the GNU General Public License, version 3 only (SPDX: GPL-3.0-only). See the repository LICENSE. Source provenance remains preserved.
