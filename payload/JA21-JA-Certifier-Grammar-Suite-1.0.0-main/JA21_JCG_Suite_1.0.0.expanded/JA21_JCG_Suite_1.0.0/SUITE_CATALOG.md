# Suite Catalog

## Primary deliverables

| Deliverable | Location | Contents |
|---|---|---|
| Technical corpus | `corpus/technical/` | 10,000 normalized records, master file, twenty shards, document metadata |
| Corpus index | `corpus/index/technical_corpus_index.csv` | Record-to-topic, stage, diagnostic, source, semantic, R12, and MCRT map |
| Script example pack | `scripts/` | 1,000 source-faithful `.ebnf` programs including all certification holdouts |
| Script catalog | `catalogs/SCRIPT_CATALOG.csv` | Searchable explanation and provenance for every program |
| Textbook | `textbook/JA21_JA_CERTIFIER_GRAMMAR_TEXTBOOK.md` | Twenty-two chapters, worked examples, laboratories, review questions, glossary |
| Education pack | `education/` | Twelve-week curriculum, student workbook, instructor guide |
| Specifications | `specifications/` | Source grammar plus enhanced language, compiler, runtime, R12/MCRT, conformance contracts |
| Publication system | `design/` | Air-gap-safe visual hierarchy, design tokens, and cover |
| Offline tools | `tools/` | Corpus inspection and structural validation |
| Evidence | `manifests/` | Machine-readable inventory and SHA-256 checksums |

## Script pack by publication role

| Class | Corpus | Script pack |
|---|---:|---:|
| Positive | 7,727 | 750 |
| Negative | 2,213 | 190 |
| Certification | 60 | 60 |

## Topic coverage

| Topic | Learning track | Corpus | Script pack |
|---|---|---:|---:|
| Alternative | EBNF composition | 100 | 11 |
| Ambiguity | Formal grammar analysis | 125 | 5 |
| Ambiguity Analysis | Formal grammar analysis | 187 | 9 |
| Annotation | Grammar structure | 167 | 17 |
| Associativity | Precedence & name analysis | 167 | 17 |
| Ast Binding | Grammar structure | 167 | 17 |
| Automaton | Formal grammar analysis | 187 | 21 |
| Certification Bundle | Evidence & certification | 500 | 50 |
| Certification Profile | Evidence & certification | 357 | 37 |
| Character Class | Lexical foundations | 100 | 11 |
| Compatibility Profile | Compatibility & integration | 500 | 50 |
| Compiler Validator | Semantic validation | 358 | 37 |
| Cross Language Import | Compatibility & integration | 357 | 36 |
| Diagnostic | Grammar structure | 167 | 17 |
| Empty Cycle | Formal grammar analysis | 125 | 5 |
| Evidence Record | Evidence & certification | 357 | 35 |
| First Follow | Formal grammar analysis | 188 | 21 |
| Grammar Module | EBNF composition | 100 | 10 |
| Grammar Normalization | Formal grammar analysis | 188 | 20 |
| Grouping | EBNF composition | 100 | 10 |
| Import | Grammar structure | 166 | 17 |
| Invalid Evidence | Evidence & certification | 125 | 5 |
| Language Certificate | Evidence & certification | 500 | 50 |
| Left Recursion | Formal grammar analysis | 187 | 20 |
| Lexical Mode | Lexical foundations | 166 | 17 |
| Literal | Lexical foundations | 100 | 10 |
| Migration Profile | Compatibility & integration | 500 | 50 |
| Multistage Suite | Compatibility & integration | 500 | 50 |
| Optional | EBNF composition | 100 | 10 |
| Parser Rule | Grammar structure | 167 | 16 |
| Parser Table Compression | Formal grammar analysis | 187 | 20 |
| Policy Validator | Semantic validation | 357 | 35 |
| Precedence | Precedence & name analysis | 166 | 16 |
| Precedence Conflict | Precedence & name analysis | 125 | 5 |
| Production | EBNF composition | 100 | 10 |
| R12 Mcrt Lowering | Lowering & conformance | 188 | 20 |
| Recovery Rule | Grammar structure | 167 | 16 |
| Repetition | EBNF composition | 100 | 9 |
| Semantic Predicate | Semantic validation | 357 | 35 |
| Sequence | EBNF composition | 100 | 10 |
| Stale Hash | Evidence & certification | 125 | 5 |
| Token | Lexical foundations | 100 | 9 |
| Type Judgment | Semantic validation | 357 | 35 |
| Undefined Symbol | Precedence & name analysis | 125 | 35 |
| Unreachable Production | Precedence & name analysis | 125 | 5 |
| Unsigned Certificate | Evidence & certification | 125 | 35 |
| Validator Scheduling | Semantic validation | 188 | 19 |

## Navigation guidance

Use the textbook for sequential learning, the topic atlas for concept lookup, the script catalog for concrete programs and failure modes, the technical corpus for compiler/evaluator/retrieval workflows, and the specifications for native implementation and certification work.
