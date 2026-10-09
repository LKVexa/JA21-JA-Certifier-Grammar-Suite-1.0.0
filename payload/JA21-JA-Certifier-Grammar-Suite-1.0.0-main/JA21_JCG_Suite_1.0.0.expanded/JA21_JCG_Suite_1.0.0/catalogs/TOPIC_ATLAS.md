# JA Certifier Grammar Topic Atlas

This atlas turns all 47 corpus topics into navigable engineering reference cards.

## Alternative

Declares choice among branches while retaining enough evidence to diagnose overlap or ambiguity.

- **Learning track:** EBNF composition
- **Corpus records:** 100
- **Positive / negative / certification:** 90 / 10 / 0
- **Expected stages:** runtime, semantic_validation
- **Tiers:** 1

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.

## Ambiguity

Represents evidence that one input admits multiple valid derivations under the declared grammar.

- **Learning track:** Formal grammar analysis
- **Corpus records:** 125
- **Positive / negative / certification:** 0 / 125 / 0
- **Expected stages:** semantic_validation
- **Tiers:** 6

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.

## Ambiguity Analysis

Searches, bounds, explains, and records ambiguity witnesses instead of reporting a vague warning.

- **Learning track:** Formal grammar analysis
- **Corpus records:** 187
- **Positive / negative / certification:** 0 / 187 / 0
- **Expected stages:** semantic_validation
- **Tiers:** 5

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.

## Annotation

Attaches typed metadata to grammar nodes without silently changing language acceptance.

- **Learning track:** Grammar structure
- **Corpus records:** 167
- **Positive / negative / certification:** 157 / 10 / 0
- **Expected stages:** runtime, semantic_validation
- **Tiers:** 2

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.

## Associativity

Controls grouping of repeated operators and must agree with AST shape and semantic evaluation.

- **Learning track:** Precedence & name analysis
- **Corpus records:** 167
- **Positive / negative / certification:** 147 / 20 / 0
- **Expected stages:** runtime, semantic_validation
- **Tiers:** 2

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.

## Ast Binding

Maps recognized structures to typed AST nodes while preserving source spans and origin hashes.

- **Learning track:** Grammar structure
- **Corpus records:** 167
- **Positive / negative / certification:** 153 / 14 / 0
- **Expected stages:** runtime, semantic_validation
- **Tiers:** 2

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.

## Automaton

Constructs a deterministic or declared nondeterministic recognition automaton with stable state identity.

- **Learning track:** Formal grammar analysis
- **Corpus records:** 187
- **Positive / negative / certification:** 147 / 40 / 0
- **Expected stages:** runtime, semantic_validation
- **Tiers:** 5

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.

## Certification Bundle

Collects mutually consistent certificates, artifacts, manifests, and replay evidence for release.

- **Learning track:** Evidence & certification
- **Corpus records:** 500
- **Positive / negative / certification:** 450 / 50 / 0
- **Expected stages:** runtime, semantic_validation
- **Tiers:** 4

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.

## Certification Profile

Defines the gates, tolerances, validators, signatures, and replay obligations for certification.

- **Learning track:** Evidence & certification
- **Corpus records:** 357
- **Positive / negative / certification:** 304 / 53 / 0
- **Expected stages:** runtime, semantic_validation
- **Tiers:** 3

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.

## Character Class

Defines a finite or ranged set of admissible characters and makes encoding assumptions explicit.

- **Learning track:** Lexical foundations
- **Corpus records:** 100
- **Positive / negative / certification:** 90 / 10 / 0
- **Expected stages:** runtime, semantic_validation
- **Tiers:** 1

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.

## Compatibility Profile

Defines which versions, hashes, grammar changes, and evidence transitions remain compatible.

- **Learning track:** Compatibility & integration
- **Corpus records:** 500
- **Positive / negative / certification:** 450 / 50 / 0
- **Expected stages:** runtime, semantic_validation
- **Tiers:** 4

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.

## Compiler Validator

Defines a compiler-phase validator with declared inputs, outputs, dependencies, and failure stage.

- **Learning track:** Semantic validation
- **Corpus records:** 358
- **Positive / negative / certification:** 305 / 53 / 0
- **Expected stages:** runtime, semantic_validation
- **Tiers:** 3

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.

## Cross Language Import

Imports grammar or certificate facts across language boundaries under explicit adapters and profiles.

- **Learning track:** Compatibility & integration
- **Corpus records:** 357
- **Positive / negative / certification:** 303 / 54 / 0
- **Expected stages:** runtime, semantic_validation
- **Tiers:** 3

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.

## Diagnostic

Defines stable, phase-specific diagnostics with severity, source span, evidence, and remediation guidance.

- **Learning track:** Grammar structure
- **Corpus records:** 167
- **Positive / negative / certification:** 155 / 12 / 0
- **Expected stages:** runtime, semantic_validation
- **Tiers:** 2

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.

## Empty Cycle

Detects cycles that can repeat without consuming input, preventing nontermination and false acceptance.

- **Learning track:** Formal grammar analysis
- **Corpus records:** 125
- **Positive / negative / certification:** 0 / 125 / 0
- **Expected stages:** semantic_validation
- **Tiers:** 6

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.

## Evidence Record

Captures source, grammar, analysis, validation, hash, R12, and MCRT facts in a stable record.

- **Learning track:** Evidence & certification
- **Corpus records:** 357
- **Positive / negative / certification:** 303 / 54 / 0
- **Expected stages:** runtime, semantic_validation
- **Tiers:** 3

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.

## First Follow

Computes FIRST and FOLLOW sets as explicit evidence for predictive parsing and conflict diagnosis.

- **Learning track:** Formal grammar analysis
- **Corpus records:** 188
- **Positive / negative / certification:** 152 / 36 / 0
- **Expected stages:** runtime, semantic_validation
- **Tiers:** 5

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.

## Grammar Module

Packages lexical, syntactic, semantic, policy, and certification declarations into a governed unit.

- **Learning track:** EBNF composition
- **Corpus records:** 100
- **Positive / negative / certification:** 100 / 0 / 0
- **Expected stages:** runtime
- **Tiers:** 1

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.

## Grammar Normalization

Transforms grammar form only when language equivalence and diagnostic traceability are proven.

- **Learning track:** Formal grammar analysis
- **Corpus records:** 188
- **Positive / negative / certification:** 152 / 36 / 0
- **Expected stages:** runtime, semantic_validation
- **Tiers:** 5

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.

## Grouping

Controls composition boundaries without inventing a semantic node unless the profile requests one.

- **Learning track:** EBNF composition
- **Corpus records:** 100
- **Positive / negative / certification:** 100 / 0 / 0
- **Expected stages:** runtime
- **Tiers:** 1

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.

## Import

Brings another grammar namespace into scope while preserving version, hash, and compatibility evidence.

- **Learning track:** Grammar structure
- **Corpus records:** 166
- **Positive / negative / certification:** 146 / 20 / 0
- **Expected stages:** runtime, semantic_validation
- **Tiers:** 2

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.

## Invalid Evidence

Rejects malformed, contradictory, incomplete, or provenance-free certification evidence.

- **Learning track:** Evidence & certification
- **Corpus records:** 125
- **Positive / negative / certification:** 0 / 125 / 0
- **Expected stages:** safety_gate
- **Tiers:** 6

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.

## Language Certificate

Packages a grammar identity, analysis result, policy decision, and signed evidence statement.

- **Learning track:** Evidence & certification
- **Corpus records:** 500
- **Positive / negative / certification:** 450 / 50 / 0
- **Expected stages:** runtime, semantic_validation
- **Tiers:** 4

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.

## Left Recursion

Finds direct or indirect left recursion and classifies whether the selected parser strategy can admit it.

- **Learning track:** Formal grammar analysis
- **Corpus records:** 187
- **Positive / negative / certification:** 152 / 35 / 0
- **Expected stages:** runtime, semantic_validation
- **Tiers:** 5

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.

## Lexical Mode

Partitions lexical behavior into named states so context-sensitive scanning remains auditable.

- **Learning track:** Lexical foundations
- **Corpus records:** 166
- **Positive / negative / certification:** 146 / 20 / 0
- **Expected stages:** runtime, semantic_validation
- **Tiers:** 2

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.

## Literal

Represents exact terminal text whose spelling, escaping, and source span must remain reproducible.

- **Learning track:** Lexical foundations
- **Corpus records:** 100
- **Positive / negative / certification:** 100 / 0 / 0
- **Expected stages:** runtime
- **Tiers:** 1

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.

## Migration Profile

Specifies a governed path from one grammar or certificate version to another with rollback evidence.

- **Learning track:** Compatibility & integration
- **Corpus records:** 500
- **Positive / negative / certification:** 450 / 50 / 0
- **Expected stages:** runtime, semantic_validation
- **Tiers:** 4

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.

## Multistage Suite

Coordinates lexical, parser, semantic, policy, lowering, runtime, and certification stages as one suite.

- **Learning track:** Compatibility & integration
- **Corpus records:** 500
- **Positive / negative / certification:** 450 / 50 / 0
- **Expected stages:** runtime, semantic_validation
- **Tiers:** 4

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.

## Optional

Expresses zero-or-one occurrence and therefore contributes directly to nullability analysis.

- **Learning track:** EBNF composition
- **Corpus records:** 100
- **Positive / negative / certification:** 90 / 10 / 0
- **Expected stages:** runtime, semantic_validation
- **Tiers:** 1

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.

## Parser Rule

Maps declarative productions to parser actions, lookahead obligations, and explicit failure behavior.

- **Learning track:** Grammar structure
- **Corpus records:** 167
- **Positive / negative / certification:** 149 / 18 / 0
- **Expected stages:** runtime, semantic_validation
- **Tiers:** 2

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.

## Parser Table Compression

Reduces parser-table size without changing conflict behavior, actions, or recovery semantics.

- **Learning track:** Formal grammar analysis
- **Corpus records:** 187
- **Positive / negative / certification:** 148 / 39 / 0
- **Expected stages:** runtime, semantic_validation
- **Tiers:** 5

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.

## Policy Validator

Enforces no-network, no-unknown-code, provenance, signature, and capability rules as semantics.

- **Learning track:** Semantic validation
- **Corpus records:** 357
- **Positive / negative / certification:** 304 / 53 / 0
- **Expected stages:** runtime, semantic_validation
- **Tiers:** 3

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.

## Precedence

Orders operators or productions to resolve a declared class of conflicts without hiding other ambiguity.

- **Learning track:** Precedence & name analysis
- **Corpus records:** 166
- **Positive / negative / certification:** 146 / 20 / 0
- **Expected stages:** runtime, semantic_validation
- **Tiers:** 2

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.

## Precedence Conflict

Represents incompatible precedence claims that must fail deterministically with a stable diagnostic.

- **Learning track:** Precedence & name analysis
- **Corpus records:** 125
- **Positive / negative / certification:** 0 / 125 / 0
- **Expected stages:** semantic_validation
- **Tiers:** 6

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.

## Production

Defines a named nonterminal relation with stable identity, source provenance, and start-symbol reachability.

- **Learning track:** EBNF composition
- **Corpus records:** 100
- **Positive / negative / certification:** 90 / 10 / 0
- **Expected stages:** runtime, semantic_validation
- **Tiers:** 1

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.

## R12 Mcrt Lowering

Lowers certified semantic relations into stable R12 identities and replayable MCRT evidence.

- **Learning track:** Lowering & conformance
- **Corpus records:** 188
- **Positive / negative / certification:** 148 / 40 / 0
- **Expected stages:** runtime, semantic_validation
- **Tiers:** 5

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.

## Recovery Rule

Defines bounded error recovery that cannot accept invalid input merely to continue parsing.

- **Learning track:** Grammar structure
- **Corpus records:** 167
- **Positive / negative / certification:** 151 / 16 / 0
- **Expected stages:** runtime, semantic_validation
- **Tiers:** 2

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.

## Repetition

Expresses repeated occurrence and must be checked for empty-progress loops and deterministic recovery.

- **Learning track:** EBNF composition
- **Corpus records:** 100
- **Positive / negative / certification:** 100 / 0 / 0
- **Expected stages:** runtime
- **Tiers:** 1

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.

## Semantic Predicate

Adds a typed semantic guard whose dependencies, purity, and evaluation phase are explicit.

- **Learning track:** Semantic validation
- **Corpus records:** 357
- **Positive / negative / certification:** 303 / 54 / 0
- **Expected stages:** runtime, semantic_validation
- **Tiers:** 3

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.

## Sequence

Composes grammar elements in an ordered product and preserves the causal order of recognition.

- **Learning track:** EBNF composition
- **Corpus records:** 100
- **Positive / negative / certification:** 90 / 10 / 0
- **Expected stages:** runtime, semantic_validation
- **Tiers:** 1

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.

## Stale Hash

Detects evidence whose source or semantic identity no longer matches the object being certified.

- **Learning track:** Evidence & certification
- **Corpus records:** 125
- **Positive / negative / certification:** 0 / 125 / 0
- **Expected stages:** runtime_validation
- **Tiers:** 6

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.

## Token

Declares a stable lexical token and its recognizer without conflating token identity with parser meaning.

- **Learning track:** Lexical foundations
- **Corpus records:** 100
- **Positive / negative / certification:** 100 / 0 / 0
- **Expected stages:** runtime
- **Tiers:** 1

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.

## Type Judgment

States and verifies typing relations for grammar nodes, AST bindings, validators, and certificates.

- **Learning track:** Semantic validation
- **Corpus records:** 357
- **Positive / negative / certification:** 303 / 54 / 0
- **Expected stages:** runtime, semantic_validation
- **Tiers:** 3

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.

## Undefined Symbol

Detects references to missing terminals, nonterminals, profiles, validators, or evidence objects.

- **Learning track:** Precedence & name analysis
- **Corpus records:** 125
- **Positive / negative / certification:** 0 / 95 / 30
- **Expected stages:** certification, name_resolution
- **Tiers:** 6

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.

## Unreachable Production

Identifies grammar declarations that cannot be reached from any declared start symbol.

- **Learning track:** Precedence & name analysis
- **Corpus records:** 125
- **Positive / negative / certification:** 0 / 125 / 0
- **Expected stages:** name_resolution
- **Tiers:** 6

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.

## Unsigned Certificate

Prevents an untrusted or unapproved certificate from being treated as authoritative evidence.

- **Learning track:** Evidence & certification
- **Corpus records:** 125
- **Positive / negative / certification:** 0 / 95 / 30
- **Expected stages:** certification, safety_gate
- **Tiers:** 6

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.

## Validator Scheduling

Orders validators by dependency and effect while preventing cycles and evidence races.

- **Learning track:** Semantic validation
- **Corpus records:** 188
- **Positive / negative / certification:** 153 / 35 / 0
- **Expected stages:** runtime, semantic_validation
- **Tiers:** 5

**Engineering lens:** preserve language acceptance, diagnostics, source spans, hashes, policy decisions, and certification evidence through every analysis and lowering pass.
