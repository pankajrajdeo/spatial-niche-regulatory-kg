Current implementation update (2026-09-23): the user subsequently instructed “i want this automated..do now.” The [bounded critique/repair workflow](P4_CRITIQUE_AUTOMATION.md) is implemented in the ordinary extraction engine and exercised with live GLM extraction/Kimi criticism on three existing cases. It adds empty-output/mention/fact audits, one correction, bounded local context recovery and fresh verification. Remaining defects are rejected or uncertain; accuracy is not established and production remains stopped. Historical “not implemented” statements below describe the research checkpoint. See also [P4_ANNOTATION_DESIGN.md](P4_ANNOTATION_DESIGN.md).

# P4 entity and relation accuracy: research and repair decision

## Agentic critique research update — 2026-09-23

The user asked whether an agent could critique and improve entity/relation extraction. Recommendation: evaluate one bounded, evidence-grounded correction pass within the existing deterministic LangChain workflow. Keep a distinct extractor and critic role; use the already specified local evidence-assembly agent for missing source context. A general autonomous agent or multi-agent debate infrastructure is not necessary for these functions. This is a design recommendation, not a claim that the correction loop is implemented or that production has resumed.

Primary research inspected:

| Study | Relevant evidence and limitation |
|---|---|
| [CrossAgentIE, Findings ACL 2025](https://aclanthology.org/2025.findings-acl.718/) | Evaluates coordinated entity-type and NER/RE feedback on five NER and five RE datasets. Table 5 reports GPT-3.5 average RE micro-F1 of 30.97 versus 21.84 for direct prompting. Its error analysis also shows later feedback can introduce typing errors. These are different datasets/models from our regulatory evidence task; improvement is not a high-precision guarantee. |
| [VerifiNER, 2024](https://arxiv.org/html/2402.18374v1) | Biomedical mention verification uses knowledge-grounded span/type revision and contextual checks on GENIA/BC5CDR. Appendix A augments its knowledge base using annotated dataset entities, giving strong coverage that our unseen cell-state corpus does not have. Adapt source-aware identity checking, not its reported accuracy or gold-augmented evaluation setup. |
| [ANCHOR-RE, August 2026 preprint](https://arxiv.org/html/2608.03154v1) | Ontology constraints, retrieved examples and learned error-pattern verification improve BioRE benchmark performance. SemRepGS micro-F1 rises from .654 to .676; DDI from .769 to .872. The verifier trades recall for precision. Its PubTator-based newer-paper experiment reports 69% precision among 500 positive predictions reviewed by one author; it does not measure complete recall on those new papers. This is promising, task-dependent evidence, not publication-quality accuracy by default. |
| [CRITIC, ICLR 2024](https://arxiv.org/abs/2305.11738) | Tool feedback supports correction in QA, program synthesis and toxicity tasks. This supports the design principle of checks grounded outside the model's own answer; it is not a biomedical NER/RE evaluation. |
| [Large Language Models Cannot Self-Correct Reasoning Yet, ICLR 2024](https://arxiv.org/abs/2310.01798) | Finds that intrinsic correction without external feedback is unreliable and can degrade reasoning. It does not establish that every modern model or every source-grounded critic fails. It argues against assuming repeated self-review or agreement proves correctness. |

For this project, scientific evidence must remain the specific paper/experiment. Ontologies and PubTator can disambiguate identities but cannot substitute a known database association for a result missing from the paper. An external relationship absent from a database is not automatically false either.

### Bounded design to evaluate

1. Preserve the existing PubTator-assisted mention inventory and source-grounded atomic extraction under the shared extraction/KG contracts.
2. Have the critic first read source without seeing the proposed answer, then produce structured field defects and exact supporting citations. Include omitted entities/findings and empty outputs in the coverage check, not just predicted relations. Current code performs a blind read for nonempty extraction and verifies fields; an exhaustive omission/empty-output repair gate remains pending.
3. For an actionable defect, allow one correction pass with a field-level change record. The critic cannot redefine the schema, supply outside biological facts or silently turn missing evidence into a result. If local context is missing, the existing bounded assembly role may select source-linked passages/legends/table rows; source verification and experiment compatibility still gate use.
4. Run the corrected result through fresh field verification and the same deterministic span, identity, species, quantity, schema and eligibility checks. Keep original and amended provenance. Unresolved defects stay UNCERTAIN/REJECTED; disagreement is not settled by majority vote. No open-ended debate or self-modifying rules.
5. Compare current workflow versus the added correction on the same fixed source units and independently reviewed complete labels. Measure NER typed-span precision/recall and qualified end-to-end RE precision/recall, omissions, false positives, abstention, introduced errors and calls/time. Reserve known failures for development and keep held-out papers/study groups out of prompts. Prefer the extra stage only if its measured benefit justifies it; no new model tournament is needed.

GLM extraction with Kimi criticism is a candidate allocation, not an established superiority ordering. Both are capable of errors, and different model names do not ensure independent errors. Our own audit found model-approved invalid quantity references that deterministic Python rejected. This assistant's source judgments are also provisional; being an agent does not make it a gold annotator. The transferable behavior is evidence access, explicit criteria, targeted checking and controlled correction, all compatible with the existing LangChain abstractions.

Research is sufficient to choose this bounded experiment. Full-corpus extraction remains stopped; no new inference was launched by this research or schema-alignment work.

## Historical research checkpoint

Research checked 2026-09-23. Status: extraction stopped at the user's request; research/design only. No accuracy improvement or model comparison has yet been measured. This document supersedes the previous P4 acceptance for scientific extraction quality. It does not authorize restarting the full corpus.

## What was stopped and removed

PID 23074 and its `caffeinate` helper are no longer running. Six corpus batches completed and batch seven was interrupted. All generated `data/{work,processed}/extraction-*` directories and P4 response/assembly caches were removed, including earlier validation artifacts that must not be reused as accepted scientific outputs. The old corpus log was removed. Cleanup removed 450 files, 5,150,244 bytes, across 39 directories and the log. The sources, PubTator assets, P3 screening/parsing/embeddings, frozen manifests, environment and code remain intact. The `.env` checksum was unchanged.

`data/work/p4-corpus/status.json` records cancellation. `reports/continuation/p4/extraction-removal.json` records exact paths and a few defective examples for diagnosis, not usable KG evidence. The cumulative budget ledger remains: historical usage and unknown interrupted usage must not become zero after deletion. Historical reports and tests are engineering history, not present scientific acceptance.

## Local causes established by inspection

| Defect | Evidence in this implementation | Required repair |
|---|---|---|
| Entity types lack necessary distinctions | `Entity.kind` allows gene/complex/family/process/cell_state/other; gene sets, chemicals, phenotypes and measurements were forced into the wrong categories. | Define explicit mention types and separate measured endpoints from biological entities. |
| Model invents both endpoints during relation generation | `Finding.subject` universally describes a regulator/manipulated gene, even for association and phenotype relations. Entities have names but no individual mention-span contract. | Recognize and resolve mentions first; relations select validated mention/entity IDs with relation-specific roles. |
| PubTator integration is partial | `pubtator_context()` passes cached Gene annotations as hints. It does not supply a complete typed entity inventory or execute BioREx relation extraction. | Use aligned available PubTator types; retain annotation provenance and coverage. Add source-grounded cell-state/phenotype recognition for types PubTator does not cover. |
| Normalization is human-only | `EntityResolver` requires HGNC rows; a correctly recognized mouse Nf2 remains unresolved. | Separate recognition correctness from normalization; validate species-qualified external IDs with documented mappings. Never map a mouse symbol to a human ID. |
| Relations lose measurement semantics | POSTN -> survival INCREASE contradicts poorer survival; mixed regeneration/fibrosis endpoints collapse into one direction. | Represent intervention, measured variable, comparison and observed change separately. One experiment/outcome per record. |
| A matching sentence is mistaken for a valid tuple | The verifier supported a cell-atlas resource statement as a phenotype and Stk3/4 as a single gene. | Independently check endpoint types, roles, relation eligibility and evidence for each field. Exact quoting alone is insufficient. |
| No end-to-end accuracy assessment | Passing JSON/source checks and verifier agreement were used as readiness evidence. The first-batch audit was not representative and measured no recall. | Evaluate omissions and false positives against independently adjudicated source annotations, including empty outputs. |

The source registry, canonical offsets, structured calls, source-preserving parser, deterministic execution and accounting are reusable. More prompt prose alone does not repair the contracts above.

## Research findings and limits

1. **Guidelines are part of the extraction specification.** GoLLIE (ICLR 2024) found benefits from detailed annotation guidelines, including unseen task definitions, using a model trained to follow those guidelines. Apply the design lesson as entity/relation definitions, exclusion rules and examples; this does not prove that adding descriptions alone gives GLM the published performance. We are not starting fine-tuning. [Paper](https://arxiv.org/abs/2310.03668)

2. **Examples should match the extraction decision.** GPT-RE (EMNLP 2023) uses entity/relation-aware example retrieval and explanations of gold labels; it also addresses the tendency to force NULL cases into positive classes. Use a small reviewed development example bank for group entities, null findings, binding versus regulation, and intervention direction. Select examples by relation/assay/error category; never include held-out answers or auto-promote generated examples to gold. [Paper](https://aclanthology.org/2023.emnlp-main.214/)

3. **Use a specialist/generalist cascade selectively.** CoRE (ACL 2026) combines a relation detector with an LLM for difficult cases, retrieved demonstrations and bounded reconsideration. Its BioRED/CDR results support testing decomposition and selective escalation, not assuming the same scores on lung full texts or importing an entire trained system. Adapt the principle using existing PubTator/source evidence and structured LLM calls; no new local model download, training infrastructure or autonomous agent swarm. [Paper](https://aclanthology.org/2026.acl-long.1517/)

4. **Ontology constraints help, but do not establish correctness.** RELATE standardizes predicates using retrieval and LLM reranking with negation handling. It reports 52% final exact match and 94% candidate accuracy@10 on ChemProt: the latter is not 94% final extraction accuracy. It explicitly notes upstream entity errors propagate, and its appendix shows reranking can hurt some settings. For our small relation vocabulary, begin with explicit permitted types/roles and supplied definitions; a new predicate embedding model is not justified. [Paper and results](https://arxiv.org/pdf/2509.19057)

5. **Directionality needs its own evaluation.** The BioRED directionality extension adds 10,864 subject/object annotations. Entity-pair or relation-type success alone cannot establish correct roles. Our additional intervention-versus-observed-effect distinction is project-specific and must be assessed separately. [Paper](https://arxiv.org/abs/2501.14079)

6. **LLM judging is fallible.** The ACL 2025 biomedical LLM-judge study reports poor baseline judging and improvements from structured formatting and domain adaptation. A second GLM invocation, Kimi invocation or majority vote is not ground truth. Their disagreements are useful review signals, not calibrated error probabilities. [Paper](https://aclanthology.org/2025.acl-long.1238/)

7. **End-to-end evaluation matters.** A seven-dataset biomedical study (WASP 2025) found zero-shot LLM extraction still struggles with complex inputs containing multiple predicates, and explains how different endpoint matching rules change reported F1. Report strict mention/type, normalized entity and complete relation measures separately, rather than one ambiguous accuracy number. Its tested models were not our GLM/Kimi pair. [Paper](https://aclanthology.org/2025.wasp-main.6/)

8. **Schema validity and semantic fidelity are different.** ExtractBench (February 2026 preprint) separates field-specific scoring, missing records and hallucinations, and observes problems with broad schemas. It concerns enterprise document extraction, so it supports evaluation/decomposition design, not a biomedical performance estimate. [Paper](https://arxiv.org/abs/2602.12247)

9. **PubTator is a component, not a complete ontology implementation.** PubTator 3.0 uses AIONER for six entity categories, specialized normalization including GNorm2, and BioREx for relation predictions. Its categories include genes/proteins, chemicals, diseases, variants, species and cell lines. Cell lines are not general cell types, and AT1/KRT17-positive cell states need separate handling. Annotation IDs do not prove experimental species or causal regulation. Reuse cached annotations; use available relation annotations only as independently labelled candidates. [PubTator paper](https://academic.oup.com/nar/article/52/W1/W540/7640526), [NCBI BioREx](https://github.com/ncbi/BioREx)

## Recommended extraction design

This is a deterministic Python workflow using existing LangChain standalone `with_structured_output` calls. It preserves the separately bounded local evidence-assembly role. No new orchestration framework is needed. The local LangChain mirror's `langchain/models.md` documents Pydantic, JSON Schema, raw output retention and provider-specific structured modes; these provide output contracts, not scientific guarantees.

### 1. One versioned schema specification

Put scientific definitions, allowed relations, role constraints, exclusion rules and examples in `configs/extraction_schema.yaml` when implementing the repair. Load and validate that specification through Pydantic; compile descriptions and constraints into each stage's JSON Schema and prompts. Hash the specification with model/prompt/settings in cache identity. Do not maintain two drifting ontology definitions. The present `configs/extraction.yaml` contains runtime settings, not the requested full scientific ontology.

Separate three record types:

- **Mention:** exact surface text, source-part ID and verified span; kind; raw species evidence; optional normalized candidate IDs with mapping source/version and ambiguity. Preserve single genes, proteins when experimentally distinguished, complexes, families, explicitly stated gene groups/signatures, chemicals, cell types/states, processes and phenotypes. Tissue/disease/species can remain context roles. No forced fine-grained identity when the source is ambiguous.
- **Experiment observation:** manipulation/exposure, comparison, responding entity, measured variable, observed change, assay, experimental context, explicit negation/null/speculation and source spans. Organoid size and AT1 proportion are measurements, not cell states. A gene group has members only when grounded; joint perturbation does not imply independently measured effects for every member.
- **Relation finding:** validated endpoint IDs, permitted predicate, experimental observation ID, evidence provenance and qualified support. Gene expression, protein abundance, phosphorylation and activity must remain distinguishable measurements. Preserve unresolved findings without gene-specific scoring.

### 2. Entity-first extraction with a recall path

Build an inventory from aligned PubTator annotations plus a bounded source-only LLM mention pass for missing and project-specific types. Resolve exact mentions/aliases deterministically where justified, keeping species conflicts and competing IDs. Relations choose from validated inventory IDs rather than invent new endpoint names. If an essential endpoint was missed, return an explicit missing-mention proposal for one validated expansion; restricting relations to an incomplete inventory without this path would reduce recall.

Normalization must cover species actually present in the sources, using versioned official mappings or validated PubTator-linked records. Human normalization must not be applied to mouse findings. Unknown species remains unknown; normalizer success is not evidence of experimental organism. Do not broadly download taxonomic databases when bounded cached lookups suffice.

### 3. Extract events, then classify relations

Use the existing result paragraph plus linked caption/table/header/method context. Split dense bundles by experiment or source-linked table block without discarding required context. Do not silently stop after the current maximum of 12 findings: report overflow and deterministically continue on remaining source units. Deduplicate only with preserved experiment/provenance.

For each grounded event, classify among the applicable relation definitions plus `NO_RELATION` and `INSUFFICIENT_CONTEXT`. Reuse the existing vocabulary where adequate; distinguish an observed perturbation effect from an inferred regulatory mechanism. Additions such as enrichment belong in clearly typed observations, not fabricated regulatory edges. A static gene count is metadata, not a PREDICTS effect. Direct regulation still requires the manuscript's evidentiary conditions, not just a causal verb.

For the observed POSTN error, the measured endpoint is survival with lower outcome; an increased hazard ratio is a different variable. Preserve the source HR separately. For knockout X increasing Y, retain intervention=loss of X and observed change of Y=increase; do not turn this into X activates Y or silently invert it into a proven normal-function mechanism.

### 4. Independent evidence checks and selective repair

Have a source-first pass extract endpoint roles, measured variables, change, negation and attribution before exposing it to the proposed answers. Compare these facts deterministically. A subsequent structured critique identifies unsupported fields and missing evidence, not merely a global supported label. Keep evidence per critical field; no free-form rationale can override a failed source check.

Apply deterministic span/ID, endpoint-type, cardinality, relation-role, species and experiment consistency checks. Ambiguous natural-language entailment still needs evidence review; regular expressions are not a general semantic verifier. A type-correct tuple can be false. Validate any repaired candidate through the same checks, with one bounded retry and an explicit unresolved disposition if disagreement remains. Do not loop until acceptance.

A different model may help on difficult cases, but model diversity and self-consistency must demonstrate value on reviewed examples. No confidence score or agreeing model pair is treated as calibrated truth. Keep null findings distinct from no relation, and missing evidence distinct from a failed extraction.

## GLM 5.3 Flash versus Kimi K3

Both are viable candidates for evaluation; we have not established which is accurate enough for this corpus. The failed run establishes defects in this pipeline/configuration, not GLM's best achievable task performance. The official cards reviewed do not provide a directly comparable biomedical NER/RE evaluation under our schema. Parameter counts, coding scores and general document benchmarks do not answer that question.

The [official GLM card](https://huggingface.co/zai-org/GLM-5.3-Flash/blob/main/README.md) documents `reasoning_effort` values low/high/max. Our configuration used low. Test high effort for relation/context work; increasing reasoning is an experimental setting, not a guaranteed correction. Confirm the LiteLLM proxy's resolved model and parameter handling rather than equating request acceptance with verified backend behavior.

The [official Kimi K3 card](https://huggingface.co/moonshotai/Kimi-K3) documents low/high/max and always-enabled thinking. Thus switching to Kimi is not a way to disable reasoning entirely. Its official API identifier does not establish an alias on this user's LiteLLM proxy. No provider/model has been switched and no new subscription, model download or Kimi inference has been started.

Recommendation: repair the contracts first, then compare GLM-low, GLM-high and Kimi-high on the same bounded, frozen source evaluation if Kimi is available through an authorized endpoint. GLM-low isolates reasoning's effect; Kimi-high tests the model alternative. Use identical source content, definitions, scoring and output limits, and account for truncations/errors. Choose Kimi as main extractor if it materially improves the relevant metrics; choose it only for difficult verification if that is the measured benefit. If neither passes, extraction remains stopped. Do not continue GLM at scale solely because its quota is unlimited.

## Concrete accuracy check before production

This is a bounded P4 quality gate, not a separate NLP benchmark project or model tournament. Proposed design, not a completed evaluation:

1. Select 20 papers balanced across the four manuscript lineages, with human/mouse material, prose, captions and interpretable tables. Split by paper/study group into eight development papers and twelve held-out papers. Keep preprint/published variants together. Select four complete source units per paper: 32 development and 48 test units. Include representative positives, nulls, co-mentions with no relation, secondary/speculative statements, complexes/groups and direction challenges. Record any unavailable stratum instead of inventing examples. Known failed outputs are development cases, not an untouched test set.
2. Annotate all eligible entities and relations in each chosen source unit, including items the model misses. Gold labels must be independently reviewed from source; another LLM's labels alone are a provisional reference. Assistant/model preparation can reduce effort, but report the adjudication method honestly and do not call an unreviewed silver set a gold benchmark. Test labels are never supplied in prompts or example retrieval. This limited review is distinct from manually screening the whole corpus.
3. Measure strict span-plus-type NER precision/recall/F1; normalized-ID accuracy with coverage and species mismatch rate; relation precision/recall/F1 with gold entities; and end-to-end relation precision/recall/F1 with predicted entities. A complete correct relation includes ordered endpoints, predicate, measured variable, intervention/comparison, outcome direction, experimental context/attribution and supporting source. Publish field errors separately to distinguish entity propagation from relation errors.
4. Measure the final accepted subset and the raw candidates separately. Rejected/uncertain/empty outputs still count as missed findings where gold evidence exists. Sample `NO_RELATION` outputs for false negatives. Report false positives on negative source units and coverage/abstention rates. Strong precision achieved by returning nothing does not pass.
5. Proposed engineering targets: typed-mention precision >=95% and recall >=90%; end-to-end relation precision >=95% and recall >=85%; target-direction accuracy >=98% on gold-direction-known relations whose endpoints/predicate match. Also report direction-sensitive end-to-end recall so missed relations cannot inflate direction accuracy. These are proposed project targets, not published guarantees or measured scores. Report denominators, per-lineage/type results and uncertainty intervals grouped by study. Require enough predictions to interpret the precision estimates; a few correct findings cannot certify the corpus.
6. Known gene-group collapse, chemical-as-gene, reversed endpoints, knockout-sign inversion, survival/hazard confusion and negation failures must all be corrected on the development regression set. Those tests do not replace held-out results. Freeze the selected schema/prompt/model/settings and retain a compact evaluation receipt before any decision to resume production. Current user instruction remains stop/research; do not automatically relaunch from this design document.

## Next implementation work, in order

1. Repair `schemas.py`, the scientific YAML specification and normalization boundary; add behavior tests drawn from the observed defect classes.
2. Refactor the existing workflow into mention inventory, atomic observation/relation extraction and field-level verification, with bounded missing-mention/overflow handling and the existing cache/accounting infrastructure.
3. Build the small source-derived development/held-out evaluation and complete transparent adjudication and scoring. Verify PubTator coverage separately.
4. Run only the bounded model/configuration comparison when explicitly authorized to resume validation; report observed metrics and remaining errors. Production and P5 scientific evidence integration remain on hold.

No pipeline refactor, new ontology file, live model comparison or improved-accuracy claim was made as part of this research turn.
