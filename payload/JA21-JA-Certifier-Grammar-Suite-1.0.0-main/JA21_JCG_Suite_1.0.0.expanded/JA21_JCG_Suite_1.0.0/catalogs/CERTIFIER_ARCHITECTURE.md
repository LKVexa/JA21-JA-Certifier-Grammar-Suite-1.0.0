# JA Certifier Grammar Architecture

```text
Source + module + policies
           │
           ▼
Lexing ─ tokens ─ modes ─ character classes
           │
           ▼
Parsing ─ productions ─ precedence ─ recovery
           │
           ▼
AST binding ─ names ─ types ─ semantic predicates
           │
           ▼
Grammar analysis ─ nullable ─ FIRST/FOLLOW ─ automata
           │
           ▼
Ambiguity ─ left recursion ─ conflicts ─ reachability
           │
           ▼
Policy validators ─ evidence freshness ─ signatures
           │
           ▼
Normalization/optimization ─ equivalence proof
           │
           ▼
R12 lowering ─ MCRT replay ─ language certificate
           │
           ▼
Certification bundle + release manifest
```

The architecture treats a certificate as the conclusion of an evidence pipeline, not as a decorative file emitted after parsing. Every stage must preserve causal identity and expose the reason for acceptance, rejection, or unresolved status.
