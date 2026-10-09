# Semantic Operator Registry

Operators are grouped into five families:

1. **Declaration operators** — declare tokens, productions, modules, imports, annotations, precedence, and recovery rules.
2. **Analysis operators** — compute nullability, FIRST/FOLLOW, reachability, recursion, automata, conflicts, and ambiguity witnesses.
3. **Validation operators** — apply semantic predicates, type judgments, compiler validators, policy validators, and evidence checks.
4. **Transformation operators** — normalize grammars, compress parser tables, and migrate versions under equivalence proof.
5. **Certification operators** — create profiles, evidence records, language certificates, certification bundles, R12 relations, and MCRT replay records.

Every operator record shall include stable identity, declared inputs and outputs, preconditions, postconditions, effects, policy requirements, source and semantic hashes, failure stages, and provenance.
