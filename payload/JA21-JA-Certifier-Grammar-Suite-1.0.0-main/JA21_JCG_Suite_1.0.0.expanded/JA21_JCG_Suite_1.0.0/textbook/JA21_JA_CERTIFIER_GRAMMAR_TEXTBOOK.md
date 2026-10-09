# JA21 JA Certifier Grammar
## A Technical Textbook for EBNF, Grammar Analysis, Evidence, and Language Certification

**Suite edition:** 1.0.0  
**Language profile:** `ja.certifier`  
**Primary extension:** `.ebnf`  
**Corpus scale:** 10,000 technical records  
**Example pack:** 1,000 curated programs

> A grammar is not certified because it accepts a demonstration. It is certified only when its language, diagnostics, policies, transformations, evidence, and replay remain inspectable.

## Preface

This textbook turns the JA Certifier Grammar corpus into a standalone language suite for grammar authors, parser and compiler engineers, validation specialists, certification reviewers, instructors, and advanced students. Worked examples are source-faithful to the supplied corpus and are connected to AST, semantic, compiler, runtime, R12, MCRT, diagnostic, and provenance evidence.

The source corpus models expected behavior but does not include a native production certifier. The textbook therefore separates specified outcomes from executed evidence and treats negative cases as essential design material.

## Contents

1. [Certification as a Language Discipline](#chapter-1-certification-as-a-language-discipline)
2. [Compilation Units, Modules, Policies, and Start Symbols](#chapter-2-compilation-units-modules-policies-and-start-symbols)
3. [Tokens, Literals, Character Classes, and Lexical Modes](#chapter-3-tokens-literals-character-classes-and-lexical-modes)
4. [EBNF Composition: Sequence, Choice, Grouping, Optionality, and Repetition](#chapter-4-ebnf-composition-sequence-choice-grouping-optionality-and-repetition)
5. [Productions, Imports, Annotations, and Recovery](#chapter-5-productions-imports-annotations-and-recovery)
6. [Parser Rules and Typed AST Binding](#chapter-6-parser-rules-and-typed-ast-binding)
7. [Precedence, Associativity, and Conflict Discipline](#chapter-7-precedence-associativity-and-conflict-discipline)
8. [Name Resolution and Reachability](#chapter-8-name-resolution-and-reachability)
9. [Nullability, Empty Cycles, and Left Recursion](#chapter-9-nullability-empty-cycles-and-left-recursion)
10. [FIRST/FOLLOW Sets and Recognition Automata](#chapter-10-first-follow-sets-and-recognition-automata)
11. [Grammar Normalization and Parser-Table Compression](#chapter-11-grammar-normalization-and-parser-table-compression)
12. [Ambiguity Detection and Witness Analysis](#chapter-12-ambiguity-detection-and-witness-analysis)
13. [Semantic Predicates and Type Judgments](#chapter-13-semantic-predicates-and-type-judgments)
14. [Compiler Validators and Validator Scheduling](#chapter-14-compiler-validators-and-validator-scheduling)
15. [Policy Validators and Safety Gates](#chapter-15-policy-validators-and-safety-gates)
16. [Evidence Records, Hash Freshness, and Signatures](#chapter-16-evidence-records-hash-freshness-and-signatures)
17. [Compatibility Profiles and Cross-Language Imports](#chapter-17-compatibility-profiles-and-cross-language-imports)
18. [Migration Profiles and Multistage Suites](#chapter-18-migration-profiles-and-multistage-suites)
19. [Certification Profiles, Language Certificates, and Bundles](#chapter-19-certification-profiles-language-certificates-and-bundles)
20. [R12/MCRT Lowering and Deterministic Replay](#chapter-20-r12-mcrt-lowering-and-deterministic-replay)
21. [Diagnostics, Conformance, Certification Holdouts, and Smithson 8S](#chapter-21-diagnostics-conformance-certification-holdouts-and-smithson-8s)
22. [Standalone JA Certifier Toolchain Capstone](#chapter-22-standalone-ja-certifier-toolchain-capstone)

---

# Chapter 1: Certification as a Language Discipline

## Learning objectives

- Explain the role of `grammar_module`, `language_certificate`.
- Trace a grammar construct from source through AST, semantic interpretation, validation, R12, and MCRT evidence.
- Identify the earliest responsible failure stage and the evidence required for a trustworthy diagnostic.
- Design structural and native tests without confusing modeled corpus outcomes with executed proof.

Certification is a language-level judgment, not a decorative seal. A trustworthy certifier states exactly what object was analyzed, which profile governed the judgment, which evidence was present, which policies were active, and which conclusions remain outside scope.

A certifier should make its reasoning inspectable at the same granularity as its conclusion. That means an accepted artifact carries positive evidence, a rejected artifact carries phase-correct negative evidence, and an unresolved artifact carries the precise missing proof, exhausted bound, or conflicting observation. This discipline prevents later stages from laundering uncertainty into a confident-looking certificate.

### Grammar Module

Packages lexical, syntactic, semantic, policy, and certification declarations into a governed unit. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

### Language Certificate

Packages a grammar identity, analysis result, policy decision, and signed evidence statement. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

## Worked corpus example

**Corpus anchor:** `EX-JCG-00008` · Tier 1 · `positive` · `grammar_module`

```ebnf
ja certifier 0.3
module corpus.ja_certifier.example_00008
policy no_execute_unknown_code
policy no_network
grammar Grammar00008 {
  token IDENT = letter, { letter | digit | "_" } ;
  token NUMBER = digit, { digit } ;
  production atom = IDENT | NUMBER | "(", expression, ")" ;
  production expression = atom, { ("+" | "-"), atom } ;
  start expression ;
}
certify grammar Grammar00008 profile basic
```

### Evidence trace

- **Semantic operator:** `declare_grammar_module`
- **Expected stage:** `runtime`
- **Validation result:** `pass`
- **Diagnostic:** `none`
- **R12 operator/state:** `declare_grammar_module` / `validated`
- **MCRT identity:** `JCG-00008`
- **Source hash:** `sha256:e7783d99b3c3e23f9dd270494140c5f31235a5bb96da198fb03269ac332453c3`

## Review lenses

| Lens | Review question |
|---|---|
| SOPHIA | Does the certificate state only what the evidence supports, with uncertainty and claim boundaries intact? |
| CHARLOTTE | Are grammar constructs, profiles, diagnostics, and evidence objects named and indexed coherently? |
| LANDON | Are parser, validator, policy, R12/MCRT, replay, and release contracts enforceable? |
| Professor | Can a learner explain, test, reject, repair, and certify the construct? |
| Podium | Is the evidence hierarchy legible, navigable, and publication-ready? |

## Engineering checklist

- Source, semantic, AST, validator, R12, MCRT, and certificate identities remain linked.
- The diagnostic stage is the earliest stage responsible for the failure.
- No-network, no-unknown-code, provenance, signature, and resource policies are enforced.
- Normalization or compression has an explicit equivalence argument.
- Accepted, rejected, unresolved, and certified outcomes remain distinct.

## Laboratory

Locate three additional scripts concerning `grammar_module`, `language_certificate` in `catalogs/SCRIPT_CATALOG.csv`. Choose one positive case, one negative case, and one certification or advanced-analysis case. Submit an evidence packet containing source, source hash, AST node, semantic operator, validator schedule, diagnostic or proof obligation, R12 state, MCRT identity, compatibility implications, and a proposed native test.

## Review questions

1. Which hidden assumption would most likely make this analysis unsound?
2. Which evidence must survive grammar normalization or parser-table compression?
3. What should fail during name resolution, semantic validation, safety gating, runtime validation, or certification?
4. How would a replay verifier detect a stale hash, changed validator, or altered diagnostic path?

---

# Chapter 2: Compilation Units, Modules, Policies, and Start Symbols

## Learning objectives

- Explain the role of `grammar_module`, `import`, `production`.
- Trace a grammar construct from source through AST, semantic interpretation, validation, R12, and MCRT evidence.
- Identify the earliest responsible failure stage and the evidence required for a trustworthy diagnostic.
- Design structural and native tests without confusing modeled corpus outcomes with executed proof.

The compilation unit establishes stable identity and authority. Modules prevent accidental namespace collapse, policies constrain what validators may do, imports declare dependencies, and start symbols define the language surface being certified.

A certifier should make its reasoning inspectable at the same granularity as its conclusion. That means an accepted artifact carries positive evidence, a rejected artifact carries phase-correct negative evidence, and an unresolved artifact carries the precise missing proof, exhausted bound, or conflicting observation. This discipline prevents later stages from laundering uncertainty into a confident-looking certificate.

### Grammar Module

Packages lexical, syntactic, semantic, policy, and certification declarations into a governed unit. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

### Import

Brings another grammar namespace into scope while preserving version, hash, and compatibility evidence. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

### Production

Defines a named nonterminal relation with stable identity, source provenance, and start-symbol reachability. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

## Worked corpus example

**Corpus anchor:** `EX-JCG-00008` · Tier 1 · `positive` · `grammar_module`

```ebnf
ja certifier 0.3
module corpus.ja_certifier.example_00008
policy no_execute_unknown_code
policy no_network
grammar Grammar00008 {
  token IDENT = letter, { letter | digit | "_" } ;
  token NUMBER = digit, { digit } ;
  production atom = IDENT | NUMBER | "(", expression, ")" ;
  production expression = atom, { ("+" | "-"), atom } ;
  start expression ;
}
certify grammar Grammar00008 profile basic
```

### Evidence trace

- **Semantic operator:** `declare_grammar_module`
- **Expected stage:** `runtime`
- **Validation result:** `pass`
- **Diagnostic:** `none`
- **R12 operator/state:** `declare_grammar_module` / `validated`
- **MCRT identity:** `JCG-00008`
- **Source hash:** `sha256:e7783d99b3c3e23f9dd270494140c5f31235a5bb96da198fb03269ac332453c3`

## Review lenses

| Lens | Review question |
|---|---|
| SOPHIA | Does the certificate state only what the evidence supports, with uncertainty and claim boundaries intact? |
| CHARLOTTE | Are grammar constructs, profiles, diagnostics, and evidence objects named and indexed coherently? |
| LANDON | Are parser, validator, policy, R12/MCRT, replay, and release contracts enforceable? |
| Professor | Can a learner explain, test, reject, repair, and certify the construct? |
| Podium | Is the evidence hierarchy legible, navigable, and publication-ready? |

## Engineering checklist

- Source, semantic, AST, validator, R12, MCRT, and certificate identities remain linked.
- The diagnostic stage is the earliest stage responsible for the failure.
- No-network, no-unknown-code, provenance, signature, and resource policies are enforced.
- Normalization or compression has an explicit equivalence argument.
- Accepted, rejected, unresolved, and certified outcomes remain distinct.

## Laboratory

Locate three additional scripts concerning `grammar_module`, `import`, `production` in `catalogs/SCRIPT_CATALOG.csv`. Choose one positive case, one negative case, and one certification or advanced-analysis case. Submit an evidence packet containing source, source hash, AST node, semantic operator, validator schedule, diagnostic or proof obligation, R12 state, MCRT identity, compatibility implications, and a proposed native test.

## Review questions

1. Which hidden assumption would most likely make this analysis unsound?
2. Which evidence must survive grammar normalization or parser-table compression?
3. What should fail during name resolution, semantic validation, safety gating, runtime validation, or certification?
4. How would a replay verifier detect a stale hash, changed validator, or altered diagnostic path?

---

# Chapter 3: Tokens, Literals, Character Classes, and Lexical Modes

## Learning objectives

- Explain the role of `character_class`, `lexical_mode`, `literal`, `token`.
- Trace a grammar construct from source through AST, semantic interpretation, validation, R12, and MCRT evidence.
- Identify the earliest responsible failure stage and the evidence required for a trustworthy diagnostic.
- Design structural and native tests without confusing modeled corpus outcomes with executed proof.

Lexical rules are the first executable boundary. Encoding, escaping, mode transitions, longest-match behavior, and token precedence must be explicit because downstream parsing cannot repair an unstable token stream.

A certifier should make its reasoning inspectable at the same granularity as its conclusion. That means an accepted artifact carries positive evidence, a rejected artifact carries phase-correct negative evidence, and an unresolved artifact carries the precise missing proof, exhausted bound, or conflicting observation. This discipline prevents later stages from laundering uncertainty into a confident-looking certificate.

### Character Class

Defines a finite or ranged set of admissible characters and makes encoding assumptions explicit. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

### Lexical Mode

Partitions lexical behavior into named states so context-sensitive scanning remains auditable. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

### Literal

Represents exact terminal text whose spelling, escaping, and source span must remain reproducible. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

### Token

Declares a stable lexical token and its recognizer without conflating token identity with parser meaning. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

## Worked corpus example

**Corpus anchor:** `EX-JCG-00001` · Tier 1 · `positive` · `token`

```ebnf
ja certifier 0.3
module corpus.ja_certifier.example_00001
policy no_execute_unknown_code
policy no_network
grammar Grammar00001 {
  token IDENT = letter, { letter | digit | "_" } ;
  token NUMBER = digit, { digit } ;
  production atom = IDENT | NUMBER | "(", expression, ")" ;
  production expression = atom, { ("+" | "-"), atom } ;
  start expression ;
}
certify grammar Grammar00001 profile basic
```

### Evidence trace

- **Semantic operator:** `declare_token`
- **Expected stage:** `runtime`
- **Validation result:** `pass`
- **Diagnostic:** `none`
- **R12 operator/state:** `declare_token` / `validated`
- **MCRT identity:** `JCG-00001`
- **Source hash:** `sha256:9c3c9c4560fc9e07b4203f5358100d50b3443e01f76f07cbccd2c3485f39ab55`

## Review lenses

| Lens | Review question |
|---|---|
| SOPHIA | Does the certificate state only what the evidence supports, with uncertainty and claim boundaries intact? |
| CHARLOTTE | Are grammar constructs, profiles, diagnostics, and evidence objects named and indexed coherently? |
| LANDON | Are parser, validator, policy, R12/MCRT, replay, and release contracts enforceable? |
| Professor | Can a learner explain, test, reject, repair, and certify the construct? |
| Podium | Is the evidence hierarchy legible, navigable, and publication-ready? |

## Engineering checklist

- Source, semantic, AST, validator, R12, MCRT, and certificate identities remain linked.
- The diagnostic stage is the earliest stage responsible for the failure.
- No-network, no-unknown-code, provenance, signature, and resource policies are enforced.
- Normalization or compression has an explicit equivalence argument.
- Accepted, rejected, unresolved, and certified outcomes remain distinct.

## Laboratory

Locate three additional scripts concerning `character_class`, `lexical_mode`, `literal`, `token` in `catalogs/SCRIPT_CATALOG.csv`. Choose one positive case, one negative case, and one certification or advanced-analysis case. Submit an evidence packet containing source, source hash, AST node, semantic operator, validator schedule, diagnostic or proof obligation, R12 state, MCRT identity, compatibility implications, and a proposed native test.

## Review questions

1. Which hidden assumption would most likely make this analysis unsound?
2. Which evidence must survive grammar normalization or parser-table compression?
3. What should fail during name resolution, semantic validation, safety gating, runtime validation, or certification?
4. How would a replay verifier detect a stale hash, changed validator, or altered diagnostic path?

---

# Chapter 4: EBNF Composition: Sequence, Choice, Grouping, Optionality, and Repetition

## Learning objectives

- Explain the role of `alternative`, `grouping`, `optional`, `repetition`, `sequence`.
- Trace a grammar construct from source through AST, semantic interpretation, validation, R12, and MCRT evidence.
- Identify the earliest responsible failure stage and the evidence required for a trustworthy diagnostic.
- Design structural and native tests without confusing modeled corpus outcomes with executed proof.

EBNF operators create algebra over language fragments. Their apparent simplicity hides nullability, ordering, ambiguity, and progress obligations that must be reflected in analysis and diagnostics.

A certifier should make its reasoning inspectable at the same granularity as its conclusion. That means an accepted artifact carries positive evidence, a rejected artifact carries phase-correct negative evidence, and an unresolved artifact carries the precise missing proof, exhausted bound, or conflicting observation. This discipline prevents later stages from laundering uncertainty into a confident-looking certificate.

### Alternative

Declares choice among branches while retaining enough evidence to diagnose overlap or ambiguity. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

### Grouping

Controls composition boundaries without inventing a semantic node unless the profile requests one. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

### Optional

Expresses zero-or-one occurrence and therefore contributes directly to nullability analysis. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

### Repetition

Expresses repeated occurrence and must be checked for empty-progress loops and deterministic recovery. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

### Sequence

Composes grammar elements in an ordered product and preserves the causal order of recognition. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

## Worked corpus example

**Corpus anchor:** `EX-JCG-00002` · Tier 1 · `positive` · `repetition`

```ebnf
ja certifier 0.3
module corpus.ja_certifier.example_00002
policy no_execute_unknown_code
policy no_network
grammar Grammar00002 {
  token IDENT = letter, { letter | digit | "_" } ;
  token NUMBER = digit, { digit } ;
  production atom = IDENT | NUMBER | "(", expression, ")" ;
  production expression = atom, { ("+" | "-"), atom } ;
  start expression ;
}
certify grammar Grammar00002 profile basic
```

### Evidence trace

- **Semantic operator:** `declare_repetition`
- **Expected stage:** `runtime`
- **Validation result:** `pass`
- **Diagnostic:** `none`
- **R12 operator/state:** `declare_repetition` / `validated`
- **MCRT identity:** `JCG-00002`
- **Source hash:** `sha256:9dfc06c48cea1eee62015e0845897c80e8088a72c39b03ca11872c5b582b2aad`

## Review lenses

| Lens | Review question |
|---|---|
| SOPHIA | Does the certificate state only what the evidence supports, with uncertainty and claim boundaries intact? |
| CHARLOTTE | Are grammar constructs, profiles, diagnostics, and evidence objects named and indexed coherently? |
| LANDON | Are parser, validator, policy, R12/MCRT, replay, and release contracts enforceable? |
| Professor | Can a learner explain, test, reject, repair, and certify the construct? |
| Podium | Is the evidence hierarchy legible, navigable, and publication-ready? |

## Engineering checklist

- Source, semantic, AST, validator, R12, MCRT, and certificate identities remain linked.
- The diagnostic stage is the earliest stage responsible for the failure.
- No-network, no-unknown-code, provenance, signature, and resource policies are enforced.
- Normalization or compression has an explicit equivalence argument.
- Accepted, rejected, unresolved, and certified outcomes remain distinct.

## Laboratory

Locate three additional scripts concerning `alternative`, `grouping`, `optional`, `repetition`, `sequence` in `catalogs/SCRIPT_CATALOG.csv`. Choose one positive case, one negative case, and one certification or advanced-analysis case. Submit an evidence packet containing source, source hash, AST node, semantic operator, validator schedule, diagnostic or proof obligation, R12 state, MCRT identity, compatibility implications, and a proposed native test.

## Review questions

1. Which hidden assumption would most likely make this analysis unsound?
2. Which evidence must survive grammar normalization or parser-table compression?
3. What should fail during name resolution, semantic validation, safety gating, runtime validation, or certification?
4. How would a replay verifier detect a stale hash, changed validator, or altered diagnostic path?

---

# Chapter 5: Productions, Imports, Annotations, and Recovery

## Learning objectives

- Explain the role of `annotation`, `import`, `production`, `recovery_rule`.
- Trace a grammar construct from source through AST, semantic interpretation, validation, R12, and MCRT evidence.
- Identify the earliest responsible failure stage and the evidence required for a trustworthy diagnostic.
- Design structural and native tests without confusing modeled corpus outcomes with executed proof.

Productions name reusable grammar relations. Imports and annotations extend context, while recovery rules control how the implementation resumes after failure without converting invalid input into accepted input.

A certifier should make its reasoning inspectable at the same granularity as its conclusion. That means an accepted artifact carries positive evidence, a rejected artifact carries phase-correct negative evidence, and an unresolved artifact carries the precise missing proof, exhausted bound, or conflicting observation. This discipline prevents later stages from laundering uncertainty into a confident-looking certificate.

### Annotation

Attaches typed metadata to grammar nodes without silently changing language acceptance. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

### Import

Brings another grammar namespace into scope while preserving version, hash, and compatibility evidence. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

### Production

Defines a named nonterminal relation with stable identity, source provenance, and start-symbol reachability. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

### Recovery Rule

Defines bounded error recovery that cannot accept invalid input merely to continue parsing. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

## Worked corpus example

**Corpus anchor:** `EX-JCG-00010` · Tier 1 · `positive` · `production`

```ebnf
ja certifier 0.3
module corpus.ja_certifier.example_00010
policy no_execute_unknown_code
policy no_network
grammar Grammar00010 {
  token IDENT = letter, { letter | digit | "_" } ;
  token NUMBER = digit, { digit } ;
  production atom = IDENT | NUMBER | "(", expression, ")" ;
  production expression = atom, { ("+" | "-"), atom } ;
  start expression ;
}
certify grammar Grammar00010 profile basic
```

### Evidence trace

- **Semantic operator:** `declare_production`
- **Expected stage:** `runtime`
- **Validation result:** `pass`
- **Diagnostic:** `none`
- **R12 operator/state:** `declare_production` / `validated`
- **MCRT identity:** `JCG-00010`
- **Source hash:** `sha256:5a422396f4d4c60076ddcaf8455db93262fe204276f70ad2b1c21918d56d208b`

## Review lenses

| Lens | Review question |
|---|---|
| SOPHIA | Does the certificate state only what the evidence supports, with uncertainty and claim boundaries intact? |
| CHARLOTTE | Are grammar constructs, profiles, diagnostics, and evidence objects named and indexed coherently? |
| LANDON | Are parser, validator, policy, R12/MCRT, replay, and release contracts enforceable? |
| Professor | Can a learner explain, test, reject, repair, and certify the construct? |
| Podium | Is the evidence hierarchy legible, navigable, and publication-ready? |

## Engineering checklist

- Source, semantic, AST, validator, R12, MCRT, and certificate identities remain linked.
- The diagnostic stage is the earliest stage responsible for the failure.
- No-network, no-unknown-code, provenance, signature, and resource policies are enforced.
- Normalization or compression has an explicit equivalence argument.
- Accepted, rejected, unresolved, and certified outcomes remain distinct.

## Laboratory

Locate three additional scripts concerning `annotation`, `import`, `production`, `recovery_rule` in `catalogs/SCRIPT_CATALOG.csv`. Choose one positive case, one negative case, and one certification or advanced-analysis case. Submit an evidence packet containing source, source hash, AST node, semantic operator, validator schedule, diagnostic or proof obligation, R12 state, MCRT identity, compatibility implications, and a proposed native test.

## Review questions

1. Which hidden assumption would most likely make this analysis unsound?
2. Which evidence must survive grammar normalization or parser-table compression?
3. What should fail during name resolution, semantic validation, safety gating, runtime validation, or certification?
4. How would a replay verifier detect a stale hash, changed validator, or altered diagnostic path?

---

# Chapter 6: Parser Rules and Typed AST Binding

## Learning objectives

- Explain the role of `ast_binding`, `diagnostic`, `parser_rule`.
- Trace a grammar construct from source through AST, semantic interpretation, validation, R12, and MCRT evidence.
- Identify the earliest responsible failure stage and the evidence required for a trustworthy diagnostic.
- Design structural and native tests without confusing modeled corpus outcomes with executed proof.

Parser rules connect recognition to representation. AST binding is therefore a semantic commitment: node identity, type, child order, source span, and provenance must agree with the parse evidence.

A certifier should make its reasoning inspectable at the same granularity as its conclusion. That means an accepted artifact carries positive evidence, a rejected artifact carries phase-correct negative evidence, and an unresolved artifact carries the precise missing proof, exhausted bound, or conflicting observation. This discipline prevents later stages from laundering uncertainty into a confident-looking certificate.

### Ast Binding

Maps recognized structures to typed AST nodes while preserving source spans and origin hashes. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

### Diagnostic

Defines stable, phase-specific diagnostics with severity, source span, evidence, and remediation guidance. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

### Parser Rule

Maps declarative productions to parser actions, lookahead obligations, and explicit failure behavior. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

## Worked corpus example

**Corpus anchor:** `EX-JCG-01002` · Tier 2 · `positive` · `diagnostic`

```ebnf
ja certifier 0.3
module corpus.ja_certifier.example_01002
policy no_execute_unknown_code
policy no_network
grammar Grammar01002 {
  mode DEFAULT { token IDENT = letter, { letter | digit } ; }
  precedence left "+" "-" level 10 ;
  precedence left "*" "/" level 20 ;
  production expression @ast(BinaryExpr) = expression, operator, expression | IDENT ;
  recovery expression synchronize [";", "}"] ;
  diagnostic JCG-01002 when unexpected_token ;
}
validate parser Grammar01002 with lalr1
```

### Evidence trace

- **Semantic operator:** `compose_diagnostic`
- **Expected stage:** `runtime`
- **Validation result:** `pass`
- **Diagnostic:** `none`
- **R12 operator/state:** `compose_diagnostic` / `validated`
- **MCRT identity:** `JCG-01002`
- **Source hash:** `sha256:38268f4b5263fbecdbf16bd1ca2b5f63c8208dabb2ad2d94c342a26788b605e9`

## Review lenses

| Lens | Review question |
|---|---|
| SOPHIA | Does the certificate state only what the evidence supports, with uncertainty and claim boundaries intact? |
| CHARLOTTE | Are grammar constructs, profiles, diagnostics, and evidence objects named and indexed coherently? |
| LANDON | Are parser, validator, policy, R12/MCRT, replay, and release contracts enforceable? |
| Professor | Can a learner explain, test, reject, repair, and certify the construct? |
| Podium | Is the evidence hierarchy legible, navigable, and publication-ready? |

## Engineering checklist

- Source, semantic, AST, validator, R12, MCRT, and certificate identities remain linked.
- The diagnostic stage is the earliest stage responsible for the failure.
- No-network, no-unknown-code, provenance, signature, and resource policies are enforced.
- Normalization or compression has an explicit equivalence argument.
- Accepted, rejected, unresolved, and certified outcomes remain distinct.

## Laboratory

Locate three additional scripts concerning `ast_binding`, `diagnostic`, `parser_rule` in `catalogs/SCRIPT_CATALOG.csv`. Choose one positive case, one negative case, and one certification or advanced-analysis case. Submit an evidence packet containing source, source hash, AST node, semantic operator, validator schedule, diagnostic or proof obligation, R12 state, MCRT identity, compatibility implications, and a proposed native test.

## Review questions

1. Which hidden assumption would most likely make this analysis unsound?
2. Which evidence must survive grammar normalization or parser-table compression?
3. What should fail during name resolution, semantic validation, safety gating, runtime validation, or certification?
4. How would a replay verifier detect a stale hash, changed validator, or altered diagnostic path?

---

# Chapter 7: Precedence, Associativity, and Conflict Discipline

## Learning objectives

- Explain the role of `associativity`, `precedence`, `precedence_conflict`.
- Trace a grammar construct from source through AST, semantic interpretation, validation, R12, and MCRT evidence.
- Identify the earliest responsible failure stage and the evidence required for a trustworthy diagnostic.
- Design structural and native tests without confusing modeled corpus outcomes with executed proof.

Precedence and associativity resolve only declared conflict classes. They should not be used to conceal unrelated ambiguity, and their effect must be visible in parse tables, AST shape, diagnostics, and compatibility judgments.

A certifier should make its reasoning inspectable at the same granularity as its conclusion. That means an accepted artifact carries positive evidence, a rejected artifact carries phase-correct negative evidence, and an unresolved artifact carries the precise missing proof, exhausted bound, or conflicting observation. This discipline prevents later stages from laundering uncertainty into a confident-looking certificate.

### Associativity

Controls grouping of repeated operators and must agree with AST shape and semantic evaluation. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

### Precedence

Orders operators or productions to resolve a declared class of conflicts without hiding other ambiguity. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

### Precedence Conflict

Represents incompatible precedence claims that must fail deterministically with a stable diagnostic. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

## Worked corpus example

**Corpus anchor:** `EX-JCG-01006` · Tier 2 · `positive` · `associativity`

```ebnf
ja certifier 0.3
module corpus.ja_certifier.example_01006
policy no_execute_unknown_code
policy no_network
grammar Grammar01006 {
  mode DEFAULT { token IDENT = letter, { letter | digit } ; }
  precedence left "+" "-" level 10 ;
  precedence left "*" "/" level 20 ;
  production expression @ast(BinaryExpr) = expression, operator, expression | IDENT ;
  recovery expression synchronize [";", "}"] ;
  diagnostic JCG-01006 when unexpected_token ;
}
validate parser Grammar01006 with lalr1
```

### Evidence trace

- **Semantic operator:** `compose_associativity`
- **Expected stage:** `runtime`
- **Validation result:** `pass`
- **Diagnostic:** `none`
- **R12 operator/state:** `compose_associativity` / `validated`
- **MCRT identity:** `JCG-01006`
- **Source hash:** `sha256:d5fcb35b7c692c7b578183c6ce3b857978bb04242231174086c5b29d5b5265dd`

## Review lenses

| Lens | Review question |
|---|---|
| SOPHIA | Does the certificate state only what the evidence supports, with uncertainty and claim boundaries intact? |
| CHARLOTTE | Are grammar constructs, profiles, diagnostics, and evidence objects named and indexed coherently? |
| LANDON | Are parser, validator, policy, R12/MCRT, replay, and release contracts enforceable? |
| Professor | Can a learner explain, test, reject, repair, and certify the construct? |
| Podium | Is the evidence hierarchy legible, navigable, and publication-ready? |

## Engineering checklist

- Source, semantic, AST, validator, R12, MCRT, and certificate identities remain linked.
- The diagnostic stage is the earliest stage responsible for the failure.
- No-network, no-unknown-code, provenance, signature, and resource policies are enforced.
- Normalization or compression has an explicit equivalence argument.
- Accepted, rejected, unresolved, and certified outcomes remain distinct.

## Laboratory

Locate three additional scripts concerning `associativity`, `precedence`, `precedence_conflict` in `catalogs/SCRIPT_CATALOG.csv`. Choose one positive case, one negative case, and one certification or advanced-analysis case. Submit an evidence packet containing source, source hash, AST node, semantic operator, validator schedule, diagnostic or proof obligation, R12 state, MCRT identity, compatibility implications, and a proposed native test.

## Review questions

1. Which hidden assumption would most likely make this analysis unsound?
2. Which evidence must survive grammar normalization or parser-table compression?
3. What should fail during name resolution, semantic validation, safety gating, runtime validation, or certification?
4. How would a replay verifier detect a stale hash, changed validator, or altered diagnostic path?

---

# Chapter 8: Name Resolution and Reachability

## Learning objectives

- Explain the role of `undefined_symbol`, `unreachable_production`.
- Trace a grammar construct from source through AST, semantic interpretation, validation, R12, and MCRT evidence.
- Identify the earliest responsible failure stage and the evidence required for a trustworthy diagnostic.
- Design structural and native tests without confusing modeled corpus outcomes with executed proof.

Name resolution and reachability establish that every reference has a target and every declared production has a meaningful path from a start symbol. Unreachable grammar may be harmless, obsolete, or evidence of a broken migration; the certifier must classify rather than guess.

A certifier should make its reasoning inspectable at the same granularity as its conclusion. That means an accepted artifact carries positive evidence, a rejected artifact carries phase-correct negative evidence, and an unresolved artifact carries the precise missing proof, exhausted bound, or conflicting observation. This discipline prevents later stages from laundering uncertainty into a confident-looking certificate.

### Undefined Symbol

Detects references to missing terminals, nonterminals, profiles, validators, or evidence objects. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

### Unreachable Production

Identifies grammar declarations that cannot be reached from any declared start symbol. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

## Worked corpus example

**Corpus anchor:** `EX-JCG-09090` · Tier 6 · `certification` · `undefined_symbol`

```ebnf
ja certifier 0.3
module corpus.ja_certifier.example_09090
policy no_execute_unknown_code
policy no_network
grammar Grammar09090 { production start = MissingSymbol ; }
certify grammar Grammar09090 profile strict
```

### Evidence trace

- **Semantic operator:** `certify_grammar`
- **Expected stage:** `certification`
- **Validation result:** `pass`
- **Diagnostic:** `none`
- **R12 operator/state:** `certify_grammar` / `validated`
- **MCRT identity:** `JCG-09090`
- **Source hash:** `sha256:3b1cb717f55ea6270f094ee9f1fcf53647c98b8515c5cc0aed0416b027415227`

## Review lenses

| Lens | Review question |
|---|---|
| SOPHIA | Does the certificate state only what the evidence supports, with uncertainty and claim boundaries intact? |
| CHARLOTTE | Are grammar constructs, profiles, diagnostics, and evidence objects named and indexed coherently? |
| LANDON | Are parser, validator, policy, R12/MCRT, replay, and release contracts enforceable? |
| Professor | Can a learner explain, test, reject, repair, and certify the construct? |
| Podium | Is the evidence hierarchy legible, navigable, and publication-ready? |

## Engineering checklist

- Source, semantic, AST, validator, R12, MCRT, and certificate identities remain linked.
- The diagnostic stage is the earliest stage responsible for the failure.
- No-network, no-unknown-code, provenance, signature, and resource policies are enforced.
- Normalization or compression has an explicit equivalence argument.
- Accepted, rejected, unresolved, and certified outcomes remain distinct.

## Laboratory

Locate three additional scripts concerning `undefined_symbol`, `unreachable_production` in `catalogs/SCRIPT_CATALOG.csv`. Choose one positive case, one negative case, and one certification or advanced-analysis case. Submit an evidence packet containing source, source hash, AST node, semantic operator, validator schedule, diagnostic or proof obligation, R12 state, MCRT identity, compatibility implications, and a proposed native test.

## Review questions

1. Which hidden assumption would most likely make this analysis unsound?
2. Which evidence must survive grammar normalization or parser-table compression?
3. What should fail during name resolution, semantic validation, safety gating, runtime validation, or certification?
4. How would a replay verifier detect a stale hash, changed validator, or altered diagnostic path?

---

# Chapter 9: Nullability, Empty Cycles, and Left Recursion

## Learning objectives

- Explain the role of `empty_cycle`, `left_recursion`, `optional`, `repetition`.
- Trace a grammar construct from source through AST, semantic interpretation, validation, R12, and MCRT evidence.
- Identify the earliest responsible failure stage and the evidence required for a trustworthy diagnostic.
- Design structural and native tests without confusing modeled corpus outcomes with executed proof.

Nullability is a fixed-point property that influences repetition, FIRST/FOLLOW, recursion, and recovery. Empty cycles threaten termination, while left recursion is admissible only under parser strategies that explicitly support it.

A certifier should make its reasoning inspectable at the same granularity as its conclusion. That means an accepted artifact carries positive evidence, a rejected artifact carries phase-correct negative evidence, and an unresolved artifact carries the precise missing proof, exhausted bound, or conflicting observation. This discipline prevents later stages from laundering uncertainty into a confident-looking certificate.

### Empty Cycle

Detects cycles that can repeat without consuming input, preventing nontermination and false acceptance. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

### Left Recursion

Finds direct or indirect left recursion and classifies whether the selected parser strategy can admit it. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

### Optional

Expresses zero-or-one occurrence and therefore contributes directly to nullability analysis. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

### Repetition

Expresses repeated occurrence and must be checked for empty-progress loops and deterministic recovery. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

## Worked corpus example

**Corpus anchor:** `EX-JCG-00002` · Tier 1 · `positive` · `repetition`

```ebnf
ja certifier 0.3
module corpus.ja_certifier.example_00002
policy no_execute_unknown_code
policy no_network
grammar Grammar00002 {
  token IDENT = letter, { letter | digit | "_" } ;
  token NUMBER = digit, { digit } ;
  production atom = IDENT | NUMBER | "(", expression, ")" ;
  production expression = atom, { ("+" | "-"), atom } ;
  start expression ;
}
certify grammar Grammar00002 profile basic
```

### Evidence trace

- **Semantic operator:** `declare_repetition`
- **Expected stage:** `runtime`
- **Validation result:** `pass`
- **Diagnostic:** `none`
- **R12 operator/state:** `declare_repetition` / `validated`
- **MCRT identity:** `JCG-00002`
- **Source hash:** `sha256:9dfc06c48cea1eee62015e0845897c80e8088a72c39b03ca11872c5b582b2aad`

## Review lenses

| Lens | Review question |
|---|---|
| SOPHIA | Does the certificate state only what the evidence supports, with uncertainty and claim boundaries intact? |
| CHARLOTTE | Are grammar constructs, profiles, diagnostics, and evidence objects named and indexed coherently? |
| LANDON | Are parser, validator, policy, R12/MCRT, replay, and release contracts enforceable? |
| Professor | Can a learner explain, test, reject, repair, and certify the construct? |
| Podium | Is the evidence hierarchy legible, navigable, and publication-ready? |

## Engineering checklist

- Source, semantic, AST, validator, R12, MCRT, and certificate identities remain linked.
- The diagnostic stage is the earliest stage responsible for the failure.
- No-network, no-unknown-code, provenance, signature, and resource policies are enforced.
- Normalization or compression has an explicit equivalence argument.
- Accepted, rejected, unresolved, and certified outcomes remain distinct.

## Laboratory

Locate three additional scripts concerning `empty_cycle`, `left_recursion`, `optional`, `repetition` in `catalogs/SCRIPT_CATALOG.csv`. Choose one positive case, one negative case, and one certification or advanced-analysis case. Submit an evidence packet containing source, source hash, AST node, semantic operator, validator schedule, diagnostic or proof obligation, R12 state, MCRT identity, compatibility implications, and a proposed native test.

## Review questions

1. Which hidden assumption would most likely make this analysis unsound?
2. Which evidence must survive grammar normalization or parser-table compression?
3. What should fail during name resolution, semantic validation, safety gating, runtime validation, or certification?
4. How would a replay verifier detect a stale hash, changed validator, or altered diagnostic path?

---

# Chapter 10: FIRST/FOLLOW Sets and Recognition Automata

## Learning objectives

- Explain the role of `automaton`, `first_follow`.
- Trace a grammar construct from source through AST, semantic interpretation, validation, R12, and MCRT evidence.
- Identify the earliest responsible failure stage and the evidence required for a trustworthy diagnostic.
- Design structural and native tests without confusing modeled corpus outcomes with executed proof.

FIRST and FOLLOW sets summarize possible lookahead and continuation. Automata make recognition state explicit. Both become evidence for conflicts, deterministic parsing, compression, and replay.

A certifier should make its reasoning inspectable at the same granularity as its conclusion. That means an accepted artifact carries positive evidence, a rejected artifact carries phase-correct negative evidence, and an unresolved artifact carries the precise missing proof, exhausted bound, or conflicting observation. This discipline prevents later stages from laundering uncertainty into a confident-looking certificate.

### Automaton

Constructs a deterministic or declared nondeterministic recognition automaton with stable state identity. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

### First Follow

Computes FIRST and FOLLOW sets as explicit evidence for predictive parsing and conflict diagnosis. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

## Worked corpus example

**Corpus anchor:** `EX-JCG-07505` · Tier 5 · `positive` · `automaton`

```ebnf
ja certifier 0.3
module corpus.ja_certifier.example_07505
policy no_execute_unknown_code
policy no_network
grammar Grammar07505 {
  production E = E, "+", T | T ;
  production T = T, "*", F | F ;
  production F = IDENT | "(", E, ")" ;
}
normalize grammar Grammar07505 using [eliminate_left_recursion, factor_prefixes, compute_first_follow, build_automaton, compress_tables]
analyze ambiguity Grammar07505
lower certificate Grammar07505 to JA_CERTIFIER_R12
```

### Evidence trace

- **Semantic operator:** `optimize_grammar`
- **Expected stage:** `runtime`
- **Validation result:** `pass`
- **Diagnostic:** `none`
- **R12 operator/state:** `optimize_grammar` / `validated`
- **MCRT identity:** `JCG-07505`
- **Source hash:** `sha256:dc515152984493482ffd67804f7b57797e92175adcf3e4c93ddfae3d0a28b50c`

## Review lenses

| Lens | Review question |
|---|---|
| SOPHIA | Does the certificate state only what the evidence supports, with uncertainty and claim boundaries intact? |
| CHARLOTTE | Are grammar constructs, profiles, diagnostics, and evidence objects named and indexed coherently? |
| LANDON | Are parser, validator, policy, R12/MCRT, replay, and release contracts enforceable? |
| Professor | Can a learner explain, test, reject, repair, and certify the construct? |
| Podium | Is the evidence hierarchy legible, navigable, and publication-ready? |

## Engineering checklist

- Source, semantic, AST, validator, R12, MCRT, and certificate identities remain linked.
- The diagnostic stage is the earliest stage responsible for the failure.
- No-network, no-unknown-code, provenance, signature, and resource policies are enforced.
- Normalization or compression has an explicit equivalence argument.
- Accepted, rejected, unresolved, and certified outcomes remain distinct.

## Laboratory

Locate three additional scripts concerning `automaton`, `first_follow` in `catalogs/SCRIPT_CATALOG.csv`. Choose one positive case, one negative case, and one certification or advanced-analysis case. Submit an evidence packet containing source, source hash, AST node, semantic operator, validator schedule, diagnostic or proof obligation, R12 state, MCRT identity, compatibility implications, and a proposed native test.

## Review questions

1. Which hidden assumption would most likely make this analysis unsound?
2. Which evidence must survive grammar normalization or parser-table compression?
3. What should fail during name resolution, semantic validation, safety gating, runtime validation, or certification?
4. How would a replay verifier detect a stale hash, changed validator, or altered diagnostic path?

---

# Chapter 11: Grammar Normalization and Parser-Table Compression

## Learning objectives

- Explain the role of `grammar_normalization`, `parser_table_compression`.
- Trace a grammar construct from source through AST, semantic interpretation, validation, R12, and MCRT evidence.
- Identify the earliest responsible failure stage and the evidence required for a trustworthy diagnostic.
- Design structural and native tests without confusing modeled corpus outcomes with executed proof.

Normalization and compression are compiler transformations. Their success criterion is not smaller output alone; it is proven preservation of language, conflict behavior, AST commitments, diagnostics, and certification identity.

A certifier should make its reasoning inspectable at the same granularity as its conclusion. That means an accepted artifact carries positive evidence, a rejected artifact carries phase-correct negative evidence, and an unresolved artifact carries the precise missing proof, exhausted bound, or conflicting observation. This discipline prevents later stages from laundering uncertainty into a confident-looking certificate.

### Grammar Normalization

Transforms grammar form only when language equivalence and diagnostic traceability are proven. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

### Parser Table Compression

Reduces parser-table size without changing conflict behavior, actions, or recovery semantics. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

## Worked corpus example

**Corpus anchor:** `EX-JCG-07503` · Tier 5 · `positive` · `grammar_normalization`

```ebnf
ja certifier 0.3
module corpus.ja_certifier.example_07503
policy no_execute_unknown_code
policy no_network
grammar Grammar07503 {
  production E = E, "+", T | T ;
  production T = T, "*", F | F ;
  production F = IDENT | "(", E, ")" ;
}
normalize grammar Grammar07503 using [eliminate_left_recursion, factor_prefixes, compute_first_follow, build_automaton, compress_tables]
analyze ambiguity Grammar07503
lower certificate Grammar07503 to JA_CERTIFIER_R12
```

### Evidence trace

- **Semantic operator:** `optimize_grammar`
- **Expected stage:** `runtime`
- **Validation result:** `pass`
- **Diagnostic:** `none`
- **R12 operator/state:** `optimize_grammar` / `validated`
- **MCRT identity:** `JCG-07503`
- **Source hash:** `sha256:fc29c3274ae852f1d06643cf72cac4524a13b1efaf952e3c81b5ad5311886ea6`

## Review lenses

| Lens | Review question |
|---|---|
| SOPHIA | Does the certificate state only what the evidence supports, with uncertainty and claim boundaries intact? |
| CHARLOTTE | Are grammar constructs, profiles, diagnostics, and evidence objects named and indexed coherently? |
| LANDON | Are parser, validator, policy, R12/MCRT, replay, and release contracts enforceable? |
| Professor | Can a learner explain, test, reject, repair, and certify the construct? |
| Podium | Is the evidence hierarchy legible, navigable, and publication-ready? |

## Engineering checklist

- Source, semantic, AST, validator, R12, MCRT, and certificate identities remain linked.
- The diagnostic stage is the earliest stage responsible for the failure.
- No-network, no-unknown-code, provenance, signature, and resource policies are enforced.
- Normalization or compression has an explicit equivalence argument.
- Accepted, rejected, unresolved, and certified outcomes remain distinct.

## Laboratory

Locate three additional scripts concerning `grammar_normalization`, `parser_table_compression` in `catalogs/SCRIPT_CATALOG.csv`. Choose one positive case, one negative case, and one certification or advanced-analysis case. Submit an evidence packet containing source, source hash, AST node, semantic operator, validator schedule, diagnostic or proof obligation, R12 state, MCRT identity, compatibility implications, and a proposed native test.

## Review questions

1. Which hidden assumption would most likely make this analysis unsound?
2. Which evidence must survive grammar normalization or parser-table compression?
3. What should fail during name resolution, semantic validation, safety gating, runtime validation, or certification?
4. How would a replay verifier detect a stale hash, changed validator, or altered diagnostic path?

---

# Chapter 12: Ambiguity Detection and Witness Analysis

## Learning objectives

- Explain the role of `ambiguity`, `ambiguity_analysis`.
- Trace a grammar construct from source through AST, semantic interpretation, validation, R12, and MCRT evidence.
- Identify the earliest responsible failure stage and the evidence required for a trustworthy diagnostic.
- Design structural and native tests without confusing modeled corpus outcomes with executed proof.

Ambiguity exists when one input has more than one valid derivation. A useful certifier produces witnesses, bounds the search, distinguishes local from global ambiguity, and records unresolved status when proof resources are exhausted.

A certifier should make its reasoning inspectable at the same granularity as its conclusion. That means an accepted artifact carries positive evidence, a rejected artifact carries phase-correct negative evidence, and an unresolved artifact carries the precise missing proof, exhausted bound, or conflicting observation. This discipline prevents later stages from laundering uncertainty into a confident-looking certificate.

### Ambiguity

Represents evidence that one input admits multiple valid derivations under the declared grammar. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

### Ambiguity Analysis

Searches, bounds, explains, and records ambiguity witnesses instead of reporting a vague warning. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

## Worked corpus example

**Corpus anchor:** `EX-JCG-00001` · Tier 1 · `positive` · `token`

```ebnf
ja certifier 0.3
module corpus.ja_certifier.example_00001
policy no_execute_unknown_code
policy no_network
grammar Grammar00001 {
  token IDENT = letter, { letter | digit | "_" } ;
  token NUMBER = digit, { digit } ;
  production atom = IDENT | NUMBER | "(", expression, ")" ;
  production expression = atom, { ("+" | "-"), atom } ;
  start expression ;
}
certify grammar Grammar00001 profile basic
```

### Evidence trace

- **Semantic operator:** `declare_token`
- **Expected stage:** `runtime`
- **Validation result:** `pass`
- **Diagnostic:** `none`
- **R12 operator/state:** `declare_token` / `validated`
- **MCRT identity:** `JCG-00001`
- **Source hash:** `sha256:9c3c9c4560fc9e07b4203f5358100d50b3443e01f76f07cbccd2c3485f39ab55`

## Review lenses

| Lens | Review question |
|---|---|
| SOPHIA | Does the certificate state only what the evidence supports, with uncertainty and claim boundaries intact? |
| CHARLOTTE | Are grammar constructs, profiles, diagnostics, and evidence objects named and indexed coherently? |
| LANDON | Are parser, validator, policy, R12/MCRT, replay, and release contracts enforceable? |
| Professor | Can a learner explain, test, reject, repair, and certify the construct? |
| Podium | Is the evidence hierarchy legible, navigable, and publication-ready? |

## Engineering checklist

- Source, semantic, AST, validator, R12, MCRT, and certificate identities remain linked.
- The diagnostic stage is the earliest stage responsible for the failure.
- No-network, no-unknown-code, provenance, signature, and resource policies are enforced.
- Normalization or compression has an explicit equivalence argument.
- Accepted, rejected, unresolved, and certified outcomes remain distinct.

## Laboratory

Locate three additional scripts concerning `ambiguity`, `ambiguity_analysis` in `catalogs/SCRIPT_CATALOG.csv`. Choose one positive case, one negative case, and one certification or advanced-analysis case. Submit an evidence packet containing source, source hash, AST node, semantic operator, validator schedule, diagnostic or proof obligation, R12 state, MCRT identity, compatibility implications, and a proposed native test.

## Review questions

1. Which hidden assumption would most likely make this analysis unsound?
2. Which evidence must survive grammar normalization or parser-table compression?
3. What should fail during name resolution, semantic validation, safety gating, runtime validation, or certification?
4. How would a replay verifier detect a stale hash, changed validator, or altered diagnostic path?

---

# Chapter 13: Semantic Predicates and Type Judgments

## Learning objectives

- Explain the role of `semantic_predicate`, `type_judgment`.
- Trace a grammar construct from source through AST, semantic interpretation, validation, R12, and MCRT evidence.
- Identify the earliest responsible failure stage and the evidence required for a trustworthy diagnostic.
- Design structural and native tests without confusing modeled corpus outcomes with executed proof.

Semantic predicates and type judgments enrich grammar acceptance with contextual meaning. They must declare dependencies, purity or effects, evaluation phase, and failure semantics so they cannot become hidden arbitrary code.

A certifier should make its reasoning inspectable at the same granularity as its conclusion. That means an accepted artifact carries positive evidence, a rejected artifact carries phase-correct negative evidence, and an unresolved artifact carries the precise missing proof, exhausted bound, or conflicting observation. This discipline prevents later stages from laundering uncertainty into a confident-looking certificate.

### Semantic Predicate

Adds a typed semantic guard whose dependencies, purity, and evaluation phase are explicit. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

### Type Judgment

States and verifies typing relations for grammar nodes, AST bindings, validators, and certificates. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

## Worked corpus example

**Corpus anchor:** `EX-JCG-02505` · Tier 3 · `positive` · `type_judgment`

```ebnf
ja certifier 0.3
module corpus.ja_certifier.example_02505
policy no_execute_unknown_code
policy no_network
grammar Grammar02505 {
  import deepml.core.expression as TensorExpression ;
  production declaration = tensorDecl | functionDecl ;
  predicate no_hidden_network(declaration) ;
  type_judgment declaration : WellTyped ;
  policy_validator SafetyValidator requires [no_network, no_execute_unknown_code] ;
  compiler_validator LoweringValidator verifies [AST, R12, MCRT] ;
  evidence Evidence02505 { source_hash: required compiler_hash: required runtime_hash: required }
  certification profile Strict6 { require all validators }
}
```

### Evidence trace

- **Semantic operator:** `compose_type_judgment`
- **Expected stage:** `runtime`
- **Validation result:** `pass`
- **Diagnostic:** `none`
- **R12 operator/state:** `compose_type_judgment` / `validated`
- **MCRT identity:** `JCG-02505`
- **Source hash:** `sha256:3ad00e48c22186d0a087d80d34c8ef3c37628c23ae915341b4f787bd855c0815`

## Review lenses

| Lens | Review question |
|---|---|
| SOPHIA | Does the certificate state only what the evidence supports, with uncertainty and claim boundaries intact? |
| CHARLOTTE | Are grammar constructs, profiles, diagnostics, and evidence objects named and indexed coherently? |
| LANDON | Are parser, validator, policy, R12/MCRT, replay, and release contracts enforceable? |
| Professor | Can a learner explain, test, reject, repair, and certify the construct? |
| Podium | Is the evidence hierarchy legible, navigable, and publication-ready? |

## Engineering checklist

- Source, semantic, AST, validator, R12, MCRT, and certificate identities remain linked.
- The diagnostic stage is the earliest stage responsible for the failure.
- No-network, no-unknown-code, provenance, signature, and resource policies are enforced.
- Normalization or compression has an explicit equivalence argument.
- Accepted, rejected, unresolved, and certified outcomes remain distinct.

## Laboratory

Locate three additional scripts concerning `semantic_predicate`, `type_judgment` in `catalogs/SCRIPT_CATALOG.csv`. Choose one positive case, one negative case, and one certification or advanced-analysis case. Submit an evidence packet containing source, source hash, AST node, semantic operator, validator schedule, diagnostic or proof obligation, R12 state, MCRT identity, compatibility implications, and a proposed native test.

## Review questions

1. Which hidden assumption would most likely make this analysis unsound?
2. Which evidence must survive grammar normalization or parser-table compression?
3. What should fail during name resolution, semantic validation, safety gating, runtime validation, or certification?
4. How would a replay verifier detect a stale hash, changed validator, or altered diagnostic path?

---

# Chapter 14: Compiler Validators and Validator Scheduling

## Learning objectives

- Explain the role of `compiler_validator`, `validator_scheduling`.
- Trace a grammar construct from source through AST, semantic interpretation, validation, R12, and MCRT evidence.
- Identify the earliest responsible failure stage and the evidence required for a trustworthy diagnostic.
- Design structural and native tests without confusing modeled corpus outcomes with executed proof.

Validators form a dependency graph. Scheduling must preserve prerequisite evidence, avoid cycles and races, and make the earliest responsible failure stage reproducible.

A certifier should make its reasoning inspectable at the same granularity as its conclusion. That means an accepted artifact carries positive evidence, a rejected artifact carries phase-correct negative evidence, and an unresolved artifact carries the precise missing proof, exhausted bound, or conflicting observation. This discipline prevents later stages from laundering uncertainty into a confident-looking certificate.

### Compiler Validator

Defines a compiler-phase validator with declared inputs, outputs, dependencies, and failure stage. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

### Validator Scheduling

Orders validators by dependency and effect while preventing cycles and evidence races. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

## Worked corpus example

**Corpus anchor:** `EX-JCG-02501` · Tier 3 · `positive` · `compiler_validator`

```ebnf
ja certifier 0.3
module corpus.ja_certifier.example_02501
policy no_execute_unknown_code
policy no_network
grammar Grammar02501 {
  import deepml.core.expression as TensorExpression ;
  production declaration = tensorDecl | functionDecl ;
  predicate no_hidden_network(declaration) ;
  type_judgment declaration : WellTyped ;
  policy_validator SafetyValidator requires [no_network, no_execute_unknown_code] ;
  compiler_validator LoweringValidator verifies [AST, R12, MCRT] ;
  evidence Evidence02501 { source_hash: required compiler_hash: required runtime_hash: required }
  certification profile Strict2 { require all validators }
}
```

### Evidence trace

- **Semantic operator:** `compose_compiler_validator`
- **Expected stage:** `runtime`
- **Validation result:** `pass`
- **Diagnostic:** `none`
- **R12 operator/state:** `compose_compiler_validator` / `validated`
- **MCRT identity:** `JCG-02501`
- **Source hash:** `sha256:e3446838d612dbe55af34774122dcfc71c39d717b5fc2b921366388be074ec6f`

## Review lenses

| Lens | Review question |
|---|---|
| SOPHIA | Does the certificate state only what the evidence supports, with uncertainty and claim boundaries intact? |
| CHARLOTTE | Are grammar constructs, profiles, diagnostics, and evidence objects named and indexed coherently? |
| LANDON | Are parser, validator, policy, R12/MCRT, replay, and release contracts enforceable? |
| Professor | Can a learner explain, test, reject, repair, and certify the construct? |
| Podium | Is the evidence hierarchy legible, navigable, and publication-ready? |

## Engineering checklist

- Source, semantic, AST, validator, R12, MCRT, and certificate identities remain linked.
- The diagnostic stage is the earliest stage responsible for the failure.
- No-network, no-unknown-code, provenance, signature, and resource policies are enforced.
- Normalization or compression has an explicit equivalence argument.
- Accepted, rejected, unresolved, and certified outcomes remain distinct.

## Laboratory

Locate three additional scripts concerning `compiler_validator`, `validator_scheduling` in `catalogs/SCRIPT_CATALOG.csv`. Choose one positive case, one negative case, and one certification or advanced-analysis case. Submit an evidence packet containing source, source hash, AST node, semantic operator, validator schedule, diagnostic or proof obligation, R12 state, MCRT identity, compatibility implications, and a proposed native test.

## Review questions

1. Which hidden assumption would most likely make this analysis unsound?
2. Which evidence must survive grammar normalization or parser-table compression?
3. What should fail during name resolution, semantic validation, safety gating, runtime validation, or certification?
4. How would a replay verifier detect a stale hash, changed validator, or altered diagnostic path?

---

# Chapter 15: Policy Validators and Safety Gates

## Learning objectives

- Explain the role of `diagnostic`, `policy_validator`.
- Trace a grammar construct from source through AST, semantic interpretation, validation, R12, and MCRT evidence.
- Identify the earliest responsible failure stage and the evidence required for a trustworthy diagnostic.
- Design structural and native tests without confusing modeled corpus outcomes with executed proof.

Policies govern the certifier itself. No-network, no-unknown-code, provenance, signature, capability, and resource rules must be enforced before an apparently useful validator can influence certification.

A certifier should make its reasoning inspectable at the same granularity as its conclusion. That means an accepted artifact carries positive evidence, a rejected artifact carries phase-correct negative evidence, and an unresolved artifact carries the precise missing proof, exhausted bound, or conflicting observation. This discipline prevents later stages from laundering uncertainty into a confident-looking certificate.

### Diagnostic

Defines stable, phase-specific diagnostics with severity, source span, evidence, and remediation guidance. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

### Policy Validator

Enforces no-network, no-unknown-code, provenance, signature, and capability rules as semantics. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

## Worked corpus example

**Corpus anchor:** `EX-JCG-01002` · Tier 2 · `positive` · `diagnostic`

```ebnf
ja certifier 0.3
module corpus.ja_certifier.example_01002
policy no_execute_unknown_code
policy no_network
grammar Grammar01002 {
  mode DEFAULT { token IDENT = letter, { letter | digit } ; }
  precedence left "+" "-" level 10 ;
  precedence left "*" "/" level 20 ;
  production expression @ast(BinaryExpr) = expression, operator, expression | IDENT ;
  recovery expression synchronize [";", "}"] ;
  diagnostic JCG-01002 when unexpected_token ;
}
validate parser Grammar01002 with lalr1
```

### Evidence trace

- **Semantic operator:** `compose_diagnostic`
- **Expected stage:** `runtime`
- **Validation result:** `pass`
- **Diagnostic:** `none`
- **R12 operator/state:** `compose_diagnostic` / `validated`
- **MCRT identity:** `JCG-01002`
- **Source hash:** `sha256:38268f4b5263fbecdbf16bd1ca2b5f63c8208dabb2ad2d94c342a26788b605e9`

## Review lenses

| Lens | Review question |
|---|---|
| SOPHIA | Does the certificate state only what the evidence supports, with uncertainty and claim boundaries intact? |
| CHARLOTTE | Are grammar constructs, profiles, diagnostics, and evidence objects named and indexed coherently? |
| LANDON | Are parser, validator, policy, R12/MCRT, replay, and release contracts enforceable? |
| Professor | Can a learner explain, test, reject, repair, and certify the construct? |
| Podium | Is the evidence hierarchy legible, navigable, and publication-ready? |

## Engineering checklist

- Source, semantic, AST, validator, R12, MCRT, and certificate identities remain linked.
- The diagnostic stage is the earliest stage responsible for the failure.
- No-network, no-unknown-code, provenance, signature, and resource policies are enforced.
- Normalization or compression has an explicit equivalence argument.
- Accepted, rejected, unresolved, and certified outcomes remain distinct.

## Laboratory

Locate three additional scripts concerning `diagnostic`, `policy_validator` in `catalogs/SCRIPT_CATALOG.csv`. Choose one positive case, one negative case, and one certification or advanced-analysis case. Submit an evidence packet containing source, source hash, AST node, semantic operator, validator schedule, diagnostic or proof obligation, R12 state, MCRT identity, compatibility implications, and a proposed native test.

## Review questions

1. Which hidden assumption would most likely make this analysis unsound?
2. Which evidence must survive grammar normalization or parser-table compression?
3. What should fail during name resolution, semantic validation, safety gating, runtime validation, or certification?
4. How would a replay verifier detect a stale hash, changed validator, or altered diagnostic path?

---

# Chapter 16: Evidence Records, Hash Freshness, and Signatures

## Learning objectives

- Explain the role of `evidence_record`, `invalid_evidence`, `stale_hash`, `unsigned_certificate`.
- Trace a grammar construct from source through AST, semantic interpretation, validation, R12, and MCRT evidence.
- Identify the earliest responsible failure stage and the evidence required for a trustworthy diagnostic.
- Design structural and native tests without confusing modeled corpus outcomes with executed proof.

Evidence records are durable statements about exact artifacts. Stale hashes, invalid structure, missing provenance, and unsigned certificates are not formatting defects; they break the chain of authority.

A certifier should make its reasoning inspectable at the same granularity as its conclusion. That means an accepted artifact carries positive evidence, a rejected artifact carries phase-correct negative evidence, and an unresolved artifact carries the precise missing proof, exhausted bound, or conflicting observation. This discipline prevents later stages from laundering uncertainty into a confident-looking certificate.

### Evidence Record

Captures source, grammar, analysis, validation, hash, R12, and MCRT facts in a stable record. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

### Invalid Evidence

Rejects malformed, contradictory, incomplete, or provenance-free certification evidence. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

### Stale Hash

Detects evidence whose source or semantic identity no longer matches the object being certified. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

### Unsigned Certificate

Prevents an untrusted or unapproved certificate from being treated as authoritative evidence. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

## Worked corpus example

**Corpus anchor:** `EX-JCG-02506` · Tier 3 · `positive` · `evidence_record`

```ebnf
ja certifier 0.3
module corpus.ja_certifier.example_02506
policy no_execute_unknown_code
policy no_network
grammar Grammar02506 {
  import deepml.core.expression as TensorExpression ;
  production declaration = tensorDecl | functionDecl ;
  predicate no_hidden_network(declaration) ;
  type_judgment declaration : WellTyped ;
  policy_validator SafetyValidator requires [no_network, no_execute_unknown_code] ;
  compiler_validator LoweringValidator verifies [AST, R12, MCRT] ;
  evidence Evidence02506 { source_hash: required compiler_hash: required runtime_hash: required }
  certification profile Strict0 { require all validators }
}
```

### Evidence trace

- **Semantic operator:** `compose_evidence_record`
- **Expected stage:** `runtime`
- **Validation result:** `pass`
- **Diagnostic:** `none`
- **R12 operator/state:** `compose_evidence_record` / `validated`
- **MCRT identity:** `JCG-02506`
- **Source hash:** `sha256:2b0d03f3ce260eadc4a6d69eaa2f080e0dd5eb446bccca6eee0008d0e7f10b10`

## Review lenses

| Lens | Review question |
|---|---|
| SOPHIA | Does the certificate state only what the evidence supports, with uncertainty and claim boundaries intact? |
| CHARLOTTE | Are grammar constructs, profiles, diagnostics, and evidence objects named and indexed coherently? |
| LANDON | Are parser, validator, policy, R12/MCRT, replay, and release contracts enforceable? |
| Professor | Can a learner explain, test, reject, repair, and certify the construct? |
| Podium | Is the evidence hierarchy legible, navigable, and publication-ready? |

## Engineering checklist

- Source, semantic, AST, validator, R12, MCRT, and certificate identities remain linked.
- The diagnostic stage is the earliest stage responsible for the failure.
- No-network, no-unknown-code, provenance, signature, and resource policies are enforced.
- Normalization or compression has an explicit equivalence argument.
- Accepted, rejected, unresolved, and certified outcomes remain distinct.

## Laboratory

Locate three additional scripts concerning `evidence_record`, `invalid_evidence`, `stale_hash`, `unsigned_certificate` in `catalogs/SCRIPT_CATALOG.csv`. Choose one positive case, one negative case, and one certification or advanced-analysis case. Submit an evidence packet containing source, source hash, AST node, semantic operator, validator schedule, diagnostic or proof obligation, R12 state, MCRT identity, compatibility implications, and a proposed native test.

## Review questions

1. Which hidden assumption would most likely make this analysis unsound?
2. Which evidence must survive grammar normalization or parser-table compression?
3. What should fail during name resolution, semantic validation, safety gating, runtime validation, or certification?
4. How would a replay verifier detect a stale hash, changed validator, or altered diagnostic path?

---

# Chapter 17: Compatibility Profiles and Cross-Language Imports

## Learning objectives

- Explain the role of `compatibility_profile`, `cross_language_import`.
- Trace a grammar construct from source through AST, semantic interpretation, validation, R12, and MCRT evidence.
- Identify the earliest responsible failure stage and the evidence required for a trustworthy diagnostic.
- Design structural and native tests without confusing modeled corpus outcomes with executed proof.

Compatibility is a declared relation between versions, not an assumption based on similar syntax. Cross-language imports require adapters, profile agreement, namespace control, and evidence that foreign semantics were not silently reinterpreted.

A certifier should make its reasoning inspectable at the same granularity as its conclusion. That means an accepted artifact carries positive evidence, a rejected artifact carries phase-correct negative evidence, and an unresolved artifact carries the precise missing proof, exhausted bound, or conflicting observation. This discipline prevents later stages from laundering uncertainty into a confident-looking certificate.

### Compatibility Profile

Defines which versions, hashes, grammar changes, and evidence transitions remain compatible. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

### Cross Language Import

Imports grammar or certificate facts across language boundaries under explicit adapters and profiles. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

## Worked corpus example

**Corpus anchor:** `EX-JCG-02509` · Tier 3 · `positive` · `cross_language_import`

```ebnf
ja certifier 0.3
module corpus.ja_certifier.example_02509
policy no_execute_unknown_code
policy no_network
grammar Grammar02509 {
  import deepml.core.expression as TensorExpression ;
  production declaration = tensorDecl | functionDecl ;
  predicate no_hidden_network(declaration) ;
  type_judgment declaration : WellTyped ;
  policy_validator SafetyValidator requires [no_network, no_execute_unknown_code] ;
  compiler_validator LoweringValidator verifies [AST, R12, MCRT] ;
  evidence Evidence02509 { source_hash: required compiler_hash: required runtime_hash: required }
  certification profile Strict3 { require all validators }
}
```

### Evidence trace

- **Semantic operator:** `compose_cross_language_import`
- **Expected stage:** `runtime`
- **Validation result:** `pass`
- **Diagnostic:** `none`
- **R12 operator/state:** `compose_cross_language_import` / `validated`
- **MCRT identity:** `JCG-02509`
- **Source hash:** `sha256:cf67097613f95fe1aa987fecbdf9afc1f0dc5024f63672a7759cd616c44a855d`

## Review lenses

| Lens | Review question |
|---|---|
| SOPHIA | Does the certificate state only what the evidence supports, with uncertainty and claim boundaries intact? |
| CHARLOTTE | Are grammar constructs, profiles, diagnostics, and evidence objects named and indexed coherently? |
| LANDON | Are parser, validator, policy, R12/MCRT, replay, and release contracts enforceable? |
| Professor | Can a learner explain, test, reject, repair, and certify the construct? |
| Podium | Is the evidence hierarchy legible, navigable, and publication-ready? |

## Engineering checklist

- Source, semantic, AST, validator, R12, MCRT, and certificate identities remain linked.
- The diagnostic stage is the earliest stage responsible for the failure.
- No-network, no-unknown-code, provenance, signature, and resource policies are enforced.
- Normalization or compression has an explicit equivalence argument.
- Accepted, rejected, unresolved, and certified outcomes remain distinct.

## Laboratory

Locate three additional scripts concerning `compatibility_profile`, `cross_language_import` in `catalogs/SCRIPT_CATALOG.csv`. Choose one positive case, one negative case, and one certification or advanced-analysis case. Submit an evidence packet containing source, source hash, AST node, semantic operator, validator schedule, diagnostic or proof obligation, R12 state, MCRT identity, compatibility implications, and a proposed native test.

## Review questions

1. Which hidden assumption would most likely make this analysis unsound?
2. Which evidence must survive grammar normalization or parser-table compression?
3. What should fail during name resolution, semantic validation, safety gating, runtime validation, or certification?
4. How would a replay verifier detect a stale hash, changed validator, or altered diagnostic path?

---

# Chapter 18: Migration Profiles and Multistage Suites

## Learning objectives

- Explain the role of `migration_profile`, `multistage_suite`.
- Trace a grammar construct from source through AST, semantic interpretation, validation, R12, and MCRT evidence.
- Identify the earliest responsible failure stage and the evidence required for a trustworthy diagnostic.
- Design structural and native tests without confusing modeled corpus outcomes with executed proof.

Migration changes a grammar, certificate, or evidence format under a governed plan. A multistage suite coordinates lexing, parsing, semantic analysis, policy, transformation, lowering, runtime validation, and release certification.

A certifier should make its reasoning inspectable at the same granularity as its conclusion. That means an accepted artifact carries positive evidence, a rejected artifact carries phase-correct negative evidence, and an unresolved artifact carries the precise missing proof, exhausted bound, or conflicting observation. This discipline prevents later stages from laundering uncertainty into a confident-looking certificate.

### Migration Profile

Specifies a governed path from one grammar or certificate version to another with rollback evidence. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

### Multistage Suite

Coordinates lexical, parser, semantic, policy, lowering, runtime, and certification stages as one suite. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

## Worked corpus example

**Corpus anchor:** `EX-JCG-05002` · Tier 4 · `positive` · `multistage_suite`

```ebnf
ja certifier 0.3
module corpus.ja_certifier.example_05002
policy no_execute_unknown_code
policy no_network
grammar Grammar05002 {
  import ja.portal.scene as Scene ;
  import mcrt.portal.timeline as Timeline ;
  lexer suite Lex { modes: [DEFAULT, STRING] unicode: true }
  parser suite Parse { algorithm: lr1 recovery: bounded }
  ast suite AST { provenance: line_column semantic_ids: stable }
  type suite Types { judgments: [WellFormed, WellTyped] }
  safety suite Safety { policies: [no_network, no_execute_unknown_code] }
  lower suite Lower { profiles: [R12, MCRT] }
  compatibility from 0.2 to 0.3 classification additive ;
  certificate Bundle05002 sign_with local_test_key ;
}
package certificate Bundle05002 as "certificate_05002.msslb"
```

### Evidence trace

- **Semantic operator:** `integrate_multistage_suite`
- **Expected stage:** `runtime`
- **Validation result:** `pass`
- **Diagnostic:** `none`
- **R12 operator/state:** `integrate_multistage_suite` / `validated`
- **MCRT identity:** `JCG-05002`
- **Source hash:** `sha256:24e3435769bafb45e8964ce4485f0c3cfeae923b585604b55f55ab5c894fd881`

## Review lenses

| Lens | Review question |
|---|---|
| SOPHIA | Does the certificate state only what the evidence supports, with uncertainty and claim boundaries intact? |
| CHARLOTTE | Are grammar constructs, profiles, diagnostics, and evidence objects named and indexed coherently? |
| LANDON | Are parser, validator, policy, R12/MCRT, replay, and release contracts enforceable? |
| Professor | Can a learner explain, test, reject, repair, and certify the construct? |
| Podium | Is the evidence hierarchy legible, navigable, and publication-ready? |

## Engineering checklist

- Source, semantic, AST, validator, R12, MCRT, and certificate identities remain linked.
- The diagnostic stage is the earliest stage responsible for the failure.
- No-network, no-unknown-code, provenance, signature, and resource policies are enforced.
- Normalization or compression has an explicit equivalence argument.
- Accepted, rejected, unresolved, and certified outcomes remain distinct.

## Laboratory

Locate three additional scripts concerning `migration_profile`, `multistage_suite` in `catalogs/SCRIPT_CATALOG.csv`. Choose one positive case, one negative case, and one certification or advanced-analysis case. Submit an evidence packet containing source, source hash, AST node, semantic operator, validator schedule, diagnostic or proof obligation, R12 state, MCRT identity, compatibility implications, and a proposed native test.

## Review questions

1. Which hidden assumption would most likely make this analysis unsound?
2. Which evidence must survive grammar normalization or parser-table compression?
3. What should fail during name resolution, semantic validation, safety gating, runtime validation, or certification?
4. How would a replay verifier detect a stale hash, changed validator, or altered diagnostic path?

---

# Chapter 19: Certification Profiles, Language Certificates, and Bundles

## Learning objectives

- Explain the role of `certification_bundle`, `certification_profile`, `language_certificate`.
- Trace a grammar construct from source through AST, semantic interpretation, validation, R12, and MCRT evidence.
- Identify the earliest responsible failure stage and the evidence required for a trustworthy diagnostic.
- Design structural and native tests without confusing modeled corpus outcomes with executed proof.

Profiles define the gates; certificates state the judgment; bundles assemble the evidence. These objects must remain separately identifiable so a release can replace one artifact without laundering the others.

A certifier should make its reasoning inspectable at the same granularity as its conclusion. That means an accepted artifact carries positive evidence, a rejected artifact carries phase-correct negative evidence, and an unresolved artifact carries the precise missing proof, exhausted bound, or conflicting observation. This discipline prevents later stages from laundering uncertainty into a confident-looking certificate.

### Certification Bundle

Collects mutually consistent certificates, artifacts, manifests, and replay evidence for release. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

### Certification Profile

Defines the gates, tolerances, validators, signatures, and replay obligations for certification. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

### Language Certificate

Packages a grammar identity, analysis result, policy decision, and signed evidence statement. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

## Worked corpus example

**Corpus anchor:** `EX-JCG-02504` · Tier 3 · `positive` · `certification_profile`

```ebnf
ja certifier 0.3
module corpus.ja_certifier.example_02504
policy no_execute_unknown_code
policy no_network
grammar Grammar02504 {
  import deepml.core.expression as TensorExpression ;
  production declaration = tensorDecl | functionDecl ;
  predicate no_hidden_network(declaration) ;
  type_judgment declaration : WellTyped ;
  policy_validator SafetyValidator requires [no_network, no_execute_unknown_code] ;
  compiler_validator LoweringValidator verifies [AST, R12, MCRT] ;
  evidence Evidence02504 { source_hash: required compiler_hash: required runtime_hash: required }
  certification profile Strict5 { require all validators }
}
```

### Evidence trace

- **Semantic operator:** `compose_certification_profile`
- **Expected stage:** `runtime`
- **Validation result:** `pass`
- **Diagnostic:** `none`
- **R12 operator/state:** `compose_certification_profile` / `validated`
- **MCRT identity:** `JCG-02504`
- **Source hash:** `sha256:6d48ded5c7e129a23e00ac35e2756dc044d819f6d309047ce468d35e7d6de14b`

## Review lenses

| Lens | Review question |
|---|---|
| SOPHIA | Does the certificate state only what the evidence supports, with uncertainty and claim boundaries intact? |
| CHARLOTTE | Are grammar constructs, profiles, diagnostics, and evidence objects named and indexed coherently? |
| LANDON | Are parser, validator, policy, R12/MCRT, replay, and release contracts enforceable? |
| Professor | Can a learner explain, test, reject, repair, and certify the construct? |
| Podium | Is the evidence hierarchy legible, navigable, and publication-ready? |

## Engineering checklist

- Source, semantic, AST, validator, R12, MCRT, and certificate identities remain linked.
- The diagnostic stage is the earliest stage responsible for the failure.
- No-network, no-unknown-code, provenance, signature, and resource policies are enforced.
- Normalization or compression has an explicit equivalence argument.
- Accepted, rejected, unresolved, and certified outcomes remain distinct.

## Laboratory

Locate three additional scripts concerning `certification_bundle`, `certification_profile`, `language_certificate` in `catalogs/SCRIPT_CATALOG.csv`. Choose one positive case, one negative case, and one certification or advanced-analysis case. Submit an evidence packet containing source, source hash, AST node, semantic operator, validator schedule, diagnostic or proof obligation, R12 state, MCRT identity, compatibility implications, and a proposed native test.

## Review questions

1. Which hidden assumption would most likely make this analysis unsound?
2. Which evidence must survive grammar normalization or parser-table compression?
3. What should fail during name resolution, semantic validation, safety gating, runtime validation, or certification?
4. How would a replay verifier detect a stale hash, changed validator, or altered diagnostic path?

---

# Chapter 20: R12/MCRT Lowering and Deterministic Replay

## Learning objectives

- Explain the role of `evidence_record`, `r12_mcrt_lowering`.
- Trace a grammar construct from source through AST, semantic interpretation, validation, R12, and MCRT evidence.
- Identify the earliest responsible failure stage and the evidence required for a trustworthy diagnostic.
- Design structural and native tests without confusing modeled corpus outcomes with executed proof.

R12 preserves stable semantic relations, while MCRT preserves causal runtime and replay evidence. Lowering must retain diagnostics, uncertainty, policy decisions, profile identity, and transformation proofs.

A certifier should make its reasoning inspectable at the same granularity as its conclusion. That means an accepted artifact carries positive evidence, a rejected artifact carries phase-correct negative evidence, and an unresolved artifact carries the precise missing proof, exhausted bound, or conflicting observation. This discipline prevents later stages from laundering uncertainty into a confident-looking certificate.

### Evidence Record

Captures source, grammar, analysis, validation, hash, R12, and MCRT facts in a stable record. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

### R12 Mcrt Lowering

Lowers certified semantic relations into stable R12 identities and replayable MCRT evidence. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

## Worked corpus example

**Corpus anchor:** `EX-JCG-02506` · Tier 3 · `positive` · `evidence_record`

```ebnf
ja certifier 0.3
module corpus.ja_certifier.example_02506
policy no_execute_unknown_code
policy no_network
grammar Grammar02506 {
  import deepml.core.expression as TensorExpression ;
  production declaration = tensorDecl | functionDecl ;
  predicate no_hidden_network(declaration) ;
  type_judgment declaration : WellTyped ;
  policy_validator SafetyValidator requires [no_network, no_execute_unknown_code] ;
  compiler_validator LoweringValidator verifies [AST, R12, MCRT] ;
  evidence Evidence02506 { source_hash: required compiler_hash: required runtime_hash: required }
  certification profile Strict0 { require all validators }
}
```

### Evidence trace

- **Semantic operator:** `compose_evidence_record`
- **Expected stage:** `runtime`
- **Validation result:** `pass`
- **Diagnostic:** `none`
- **R12 operator/state:** `compose_evidence_record` / `validated`
- **MCRT identity:** `JCG-02506`
- **Source hash:** `sha256:2b0d03f3ce260eadc4a6d69eaa2f080e0dd5eb446bccca6eee0008d0e7f10b10`

## Review lenses

| Lens | Review question |
|---|---|
| SOPHIA | Does the certificate state only what the evidence supports, with uncertainty and claim boundaries intact? |
| CHARLOTTE | Are grammar constructs, profiles, diagnostics, and evidence objects named and indexed coherently? |
| LANDON | Are parser, validator, policy, R12/MCRT, replay, and release contracts enforceable? |
| Professor | Can a learner explain, test, reject, repair, and certify the construct? |
| Podium | Is the evidence hierarchy legible, navigable, and publication-ready? |

## Engineering checklist

- Source, semantic, AST, validator, R12, MCRT, and certificate identities remain linked.
- The diagnostic stage is the earliest stage responsible for the failure.
- No-network, no-unknown-code, provenance, signature, and resource policies are enforced.
- Normalization or compression has an explicit equivalence argument.
- Accepted, rejected, unresolved, and certified outcomes remain distinct.

## Laboratory

Locate three additional scripts concerning `evidence_record`, `r12_mcrt_lowering` in `catalogs/SCRIPT_CATALOG.csv`. Choose one positive case, one negative case, and one certification or advanced-analysis case. Submit an evidence packet containing source, source hash, AST node, semantic operator, validator schedule, diagnostic or proof obligation, R12 state, MCRT identity, compatibility implications, and a proposed native test.

## Review questions

1. Which hidden assumption would most likely make this analysis unsound?
2. Which evidence must survive grammar normalization or parser-table compression?
3. What should fail during name resolution, semantic validation, safety gating, runtime validation, or certification?
4. How would a replay verifier detect a stale hash, changed validator, or altered diagnostic path?

---

# Chapter 21: Diagnostics, Conformance, Certification Holdouts, and Smithson 8S

## Learning objectives

- Explain the role of `diagnostic`, `invalid_evidence`, `language_certificate`.
- Trace a grammar construct from source through AST, semantic interpretation, validation, R12, and MCRT evidence.
- Identify the earliest responsible failure stage and the evidence required for a trustworthy diagnostic.
- Design structural and native tests without confusing modeled corpus outcomes with executed proof.

Conformance requires accepted and rejected cases, phase-correct diagnostics, replay, and withheld certification examples. Smithson 8S annotations are preserved as a proposed computational framework with explicit claim boundaries, not as established physical law.

A certifier should make its reasoning inspectable at the same granularity as its conclusion. That means an accepted artifact carries positive evidence, a rejected artifact carries phase-correct negative evidence, and an unresolved artifact carries the precise missing proof, exhausted bound, or conflicting observation. This discipline prevents later stages from laundering uncertainty into a confident-looking certificate.

### Diagnostic

Defines stable, phase-specific diagnostics with severity, source span, evidence, and remediation guidance. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

### Invalid Evidence

Rejects malformed, contradictory, incomplete, or provenance-free certification evidence. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

### Language Certificate

Packages a grammar identity, analysis result, policy decision, and signed evidence statement. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

## Worked corpus example

**Corpus anchor:** `EX-JCG-01002` · Tier 2 · `positive` · `diagnostic`

```ebnf
ja certifier 0.3
module corpus.ja_certifier.example_01002
policy no_execute_unknown_code
policy no_network
grammar Grammar01002 {
  mode DEFAULT { token IDENT = letter, { letter | digit } ; }
  precedence left "+" "-" level 10 ;
  precedence left "*" "/" level 20 ;
  production expression @ast(BinaryExpr) = expression, operator, expression | IDENT ;
  recovery expression synchronize [";", "}"] ;
  diagnostic JCG-01002 when unexpected_token ;
}
validate parser Grammar01002 with lalr1
```

### Evidence trace

- **Semantic operator:** `compose_diagnostic`
- **Expected stage:** `runtime`
- **Validation result:** `pass`
- **Diagnostic:** `none`
- **R12 operator/state:** `compose_diagnostic` / `validated`
- **MCRT identity:** `JCG-01002`
- **Source hash:** `sha256:38268f4b5263fbecdbf16bd1ca2b5f63c8208dabb2ad2d94c342a26788b605e9`

## Review lenses

| Lens | Review question |
|---|---|
| SOPHIA | Does the certificate state only what the evidence supports, with uncertainty and claim boundaries intact? |
| CHARLOTTE | Are grammar constructs, profiles, diagnostics, and evidence objects named and indexed coherently? |
| LANDON | Are parser, validator, policy, R12/MCRT, replay, and release contracts enforceable? |
| Professor | Can a learner explain, test, reject, repair, and certify the construct? |
| Podium | Is the evidence hierarchy legible, navigable, and publication-ready? |

## Engineering checklist

- Source, semantic, AST, validator, R12, MCRT, and certificate identities remain linked.
- The diagnostic stage is the earliest stage responsible for the failure.
- No-network, no-unknown-code, provenance, signature, and resource policies are enforced.
- Normalization or compression has an explicit equivalence argument.
- Accepted, rejected, unresolved, and certified outcomes remain distinct.

## Laboratory

Locate three additional scripts concerning `diagnostic`, `invalid_evidence`, `language_certificate` in `catalogs/SCRIPT_CATALOG.csv`. Choose one positive case, one negative case, and one certification or advanced-analysis case. Submit an evidence packet containing source, source hash, AST node, semantic operator, validator schedule, diagnostic or proof obligation, R12 state, MCRT identity, compatibility implications, and a proposed native test.

## Review questions

1. Which hidden assumption would most likely make this analysis unsound?
2. Which evidence must survive grammar normalization or parser-table compression?
3. What should fail during name resolution, semantic validation, safety gating, runtime validation, or certification?
4. How would a replay verifier detect a stale hash, changed validator, or altered diagnostic path?

---

# Chapter 22: Standalone JA Certifier Toolchain Capstone

## Learning objectives

- Explain the role of `alternative`, `ambiguity`, `ambiguity_analysis`, `annotation`, `associativity`, `ast_binding`, `automaton`, `certification_bundle`.
- Trace a grammar construct from source through AST, semantic interpretation, validation, R12, and MCRT evidence.
- Identify the earliest responsible failure stage and the evidence required for a trustworthy diagnostic.
- Design structural and native tests without confusing modeled corpus outcomes with executed proof.

The capstone integrates source parsing, grammar analysis, semantic validation, policy enforcement, transformation proof, certificate construction, R12/MCRT emission, replay, and release packaging into one bounded toolchain.

A certifier should make its reasoning inspectable at the same granularity as its conclusion. That means an accepted artifact carries positive evidence, a rejected artifact carries phase-correct negative evidence, and an unresolved artifact carries the precise missing proof, exhausted bound, or conflicting observation. This discipline prevents later stages from laundering uncertainty into a confident-looking certificate.

### Alternative

Declares choice among branches while retaining enough evidence to diagnose overlap or ambiguity. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

### Ambiguity

Represents evidence that one input admits multiple valid derivations under the declared grammar. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

### Ambiguity Analysis

Searches, bounds, explains, and records ambiguity witnesses instead of reporting a vague warning. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

### Annotation

Attaches typed metadata to grammar nodes without silently changing language acceptance. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

### Associativity

Controls grouping of repeated operators and must agree with AST shape and semantic evaluation. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

### Ast Binding

Maps recognized structures to typed AST nodes while preserving source spans and origin hashes. In a conforming implementation, the construct must retain stable source and semantic identities, explicit dependencies, deterministic diagnostics, and compatibility implications after transformation and lowering.

## Worked corpus example

**Corpus anchor:** `EX-JCG-00001` · Tier 1 · `positive` · `token`

```ebnf
ja certifier 0.3
module corpus.ja_certifier.example_00001
policy no_execute_unknown_code
policy no_network
grammar Grammar00001 {
  token IDENT = letter, { letter | digit | "_" } ;
  token NUMBER = digit, { digit } ;
  production atom = IDENT | NUMBER | "(", expression, ")" ;
  production expression = atom, { ("+" | "-"), atom } ;
  start expression ;
}
certify grammar Grammar00001 profile basic
```

### Evidence trace

- **Semantic operator:** `declare_token`
- **Expected stage:** `runtime`
- **Validation result:** `pass`
- **Diagnostic:** `none`
- **R12 operator/state:** `declare_token` / `validated`
- **MCRT identity:** `JCG-00001`
- **Source hash:** `sha256:9c3c9c4560fc9e07b4203f5358100d50b3443e01f76f07cbccd2c3485f39ab55`

## Review lenses

| Lens | Review question |
|---|---|
| SOPHIA | Does the certificate state only what the evidence supports, with uncertainty and claim boundaries intact? |
| CHARLOTTE | Are grammar constructs, profiles, diagnostics, and evidence objects named and indexed coherently? |
| LANDON | Are parser, validator, policy, R12/MCRT, replay, and release contracts enforceable? |
| Professor | Can a learner explain, test, reject, repair, and certify the construct? |
| Podium | Is the evidence hierarchy legible, navigable, and publication-ready? |

## Engineering checklist

- Source, semantic, AST, validator, R12, MCRT, and certificate identities remain linked.
- The diagnostic stage is the earliest stage responsible for the failure.
- No-network, no-unknown-code, provenance, signature, and resource policies are enforced.
- Normalization or compression has an explicit equivalence argument.
- Accepted, rejected, unresolved, and certified outcomes remain distinct.

## Laboratory

Locate three additional scripts concerning `alternative`, `ambiguity`, `ambiguity_analysis`, `annotation`, `associativity`, `ast_binding`, `automaton`, `certification_bundle` in `catalogs/SCRIPT_CATALOG.csv`. Choose one positive case, one negative case, and one certification or advanced-analysis case. Submit an evidence packet containing source, source hash, AST node, semantic operator, validator schedule, diagnostic or proof obligation, R12 state, MCRT identity, compatibility implications, and a proposed native test.

## Review questions

1. Which hidden assumption would most likely make this analysis unsound?
2. Which evidence must survive grammar normalization or parser-table compression?
3. What should fail during name resolution, semantic validation, safety gating, runtime validation, or certification?
4. How would a replay verifier detect a stale hash, changed validator, or altered diagnostic path?

---

# Glossary

**Ambiguity witness:** A concrete input and derivation evidence demonstrating multiple valid parses.  
**Certification bundle:** A governed collection of certificates, artifacts, manifests, signatures, and replay evidence.  
**Grammar equivalence:** A declared relation showing that a transformation preserves the required language and observable behavior.  
**Language certificate:** A signed or otherwise authorized statement about an exact grammar under an exact certification profile.  
**MCRT:** The runtime provenance and causal-record representation used for replay.  
**Modeled not executed:** Expected behavior encoded by the corpus but not demonstrated by a native implementation.  
**R12:** The suite’s stable semantic-relation representation.  
**Unresolved:** A result used when proof bounds, evidence, provenance, or tolerance conditions do not permit a truthful pass or fail judgment.
