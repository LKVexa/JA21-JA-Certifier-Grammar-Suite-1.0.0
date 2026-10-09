# JA21 JA Certifier Grammar Suite 1 0 0 main Updated Corpus Audit

This updated copy supplies grammar version identities, diagnostics and language conformance gates. Its import boundary is: Complete grammar and run actual parser/type/proof checks.

## Source and coverage

Original input: `JA21-JA-Certifier-Grammar-Suite-1.0.0-main.zip`. Source SHA 256: `1e88a0fa8a93db91a5e936913012b3e9a29bcbff45c62e5f35696ed0052054ab`. The source archive is preserved in the parent folder. All 1,173 original leaf files were read and hashed; 31,392 stored JSONL rows were structurally parsed, including historical/reconstructed copies. Nested ZIPs are materialized in `.expanded` directories. Dataset row counts include duplicate representations and metadata headers; they are not unique executable programs.

Original checks and locations are in [the source manifest](audit/source_manifest.json). Current payload bytes are in [the updated manifest](audit/updated_manifest.json), and changes are in [the ledger](audit/change_ledger.json). Embedded source layers have [separate coverage](audit/embedded_layer_coverage.json). Historical hashes and modeled labels retain their historical meaning. The updated manifest and qualification sidecars govern this release.

## Upgrades and open implementation work

### JA-02 Medium priority

The shipped inspector has an unterminated string at line 23. The provisional grammar references 10 external or undefined symbols and omits a start declaration alternative used by starter/hello_certifier.ebnf.

Status: **applied_source_or_tool_repair_and_qualified**. JCG inspector syntax repair

Evidence: `JA21_JCG_Suite_1.0.0/tools/inspect_corpus.py | JA21_JCG_Suite_1.0.0/specifications/JA_CERTIFIER_GRAMMAR_SOURCE.ebnf`.

Remaining gate: A complete versioned profile parser, semantic inference and target/runtime conformance are needed before native admission.

### BASE-09 Medium priority

Nested packaging, raw modeled labels and historical copies need explicit current provenance and reuse boundaries.

Status: **APPLIED**. Expanded materialized payload; source and updated manifests; change ledger; dataset-bound qualification; individual audit and fabric role.

Evidence: `audit/source_manifest.json | audit/updated_manifest.json | audit/dataset_qualification.json`.

Remaining gate: Complete grammar and run actual parser/type/proof checks.

## Contribution to the new fabric language

Profile owner: `ja.certifier`. Grammar version identities, diagnostics and language conformance gates. Complete grammar and run actual parser/type/proof checks.

The [adapter contract](audit/fabric_adapter_contract.json) is a proposed interface with executable_adapter_implemented=false. It preserves source authority rather than using a feature label as inferred semantics. See [the collection architecture](../../fabric_language/ARCHITECTURE.md) and the [8S foundation](../../fabric_language/profiles/coupling8s/PROFILE.md).

## Qualification and verification

Use [dataset qualifications](audit/dataset_qualification.json) before training, importing or treating a record as evidence. A modeled pass or a structural validator pass is not native execution, authenticated federation, race proof, or physical device evidence. Current JA and DeepML technical records carry additional qualifications; deliberate negative examples remain negative examples.

The release provides an offline integrity checker: run `python tools/verify_release.py --deep` from the collection root. Per-profile test reports and validators qualify the exact behavior they checked. Complete grammars, native adapters, authenticated transports and a bootable unikernel remain separately tracked implementation gates.
