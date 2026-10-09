# Conformance and Certification Framework

## Levels

1. **Lexical conformance** — token, literal, character-class, and lexical-mode behavior.
2. **Grammar conformance** — productions, composition, start symbols, imports, precedence, and recovery.
3. **Analysis conformance** — reachability, recursion, FIRST/FOLLOW, automata, conflicts, and ambiguity.
4. **Semantic and policy conformance** — AST binding, predicates, type judgments, validators, and policy gates.
5. **Transformation conformance** — normalization, compression, compatibility, and migration equivalence.
6. **Certification conformance** — evidence freshness, signatures, R12/MCRT replay, certificates, and bundles.

## Required evidence

A certification dossier should include source and semantic hashes, manifests, exact tool versions, all diagnostics, validator schedules, analysis witnesses, equivalence proofs, policy decisions, certificate signatures, R12/MCRT records, and replay results. Corpus expectations remain modeled until reproduced by a native implementation.
