# Starter Project

`hello_certifier.ebnf` is a minimal air-gapped grammar and certification request. A future native implementation should parse it, build the grammar AST, compute basic analysis, apply the `basic` profile, emit stable R12/MCRT evidence, and produce a certificate or a phase-specific diagnostic.

Expected structural properties:

- JA Certifier 0.3 header
- stable module identity
- no-network and no-unknown-code policies
- grammar declaration with tokens, productions, and start symbol
- explicit certification request
