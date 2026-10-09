# JA Certifier Grammar Technical Corpus

## Purpose

This directory is the normalized technical heart of the standalone JA21 JA Certifier Grammar Suite. It converts the uploaded 102-document wrapper into a searchable evidence system while preserving grammar source, AST structure, semantic interpretation, compiler and runtime representations, diagnostics, hashes, provenance, R12/MCRT identities, optimization constraints, and Smithson 8S annotations.

## Corpus profile

| Measure | Value |
|---|---:|
| Technical records | 10,000 |
| Grammar and certification topics | 47 |
| Proficiency tiers | 6 |
| Positive records | 7,727 |
| Negative/diagnostic records | 2,213 |
| Certification records | 60 |
| Expected stages | 6 |

## Contents

- `JA21_JCG_TECHNICAL_CORPUS_10000.jsonl.gz` — normalized master corpus.
- `jcg_01.jsonl.gz` through `jcg_20.jsonl.gz` — twenty 500-record shards.
- `DOCUMENT_METADATA.json` — document-level coupling-mechanics profile.
- `../schema/` — normalized record schema and preserved source coverage.
- `../index/technical_corpus_index.csv` — compact navigation index.

## Evidence discipline

A grammar is not certified because it parses a sample string. Certification must preserve source identity, namespace resolution, lexical and syntactic analysis, semantic judgments, policy gates, diagnostics, optimization equivalence, evidence freshness, signature state, R12 lowering, MCRT replay identity, and release provenance. Negative examples are first-class evidence because they define the boundaries a conforming implementation must reject.

## Native-evidence boundary

The records encode expected compiler, validator, and runtime behavior. No native JA Certifier compiler, parser generator, certificate signer, or R12/MCRT runtime was supplied. This release therefore validates corpus integrity and structural conformance, not native parsing performance or production certification authority.
