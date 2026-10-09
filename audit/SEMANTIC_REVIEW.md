# ja.certifier audit findings

The shipped inspector has an unterminated string at line 23. The provisional grammar references 10 external or undefined symbols and omits a start declaration alternative used by starter/hello_certifier.ebnf.

Upgrade status: applied source or tool repair and qualified. JCG inspector syntax repair.

Proposed fabric role: Versioned grammar identities, ambiguity and reachability checks, diagnostics and exact-source certification obligations.

Import rule: Import syntax, contracts and source as reviewed reference; never import modeled outcomes as observed facts.

Source locations: `JA21_JCG_Suite_1.0.0/tools/inspect_corpus.py`, `JA21_JCG_Suite_1.0.0/specifications/JA_CERTIFIER_GRAMMAR_SOURCE.ebnf`
