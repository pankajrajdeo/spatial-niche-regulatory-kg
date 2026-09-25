# Source-grounded extraction and future encoder labels

Current automation: [P4_CRITIQUE_AUTOMATION.md](P4_CRITIQUE_AUTOMATION.md). The ordinary engine now audits every proposed mention and independently read fact, including empty outputs, then performs at most one source-grounded semantic repair and fresh verification. The GLM/Kimi live diagnostic is implementation evidence; its remaining rejected predictions are not training labels.

The user authorized this addition on 2026-09-23: encode the extraction expertise in the models' instructions and retain PubTator/GLM/Kimi annotations for later encoder fine-tuning. This expands the earlier KG-only scope to **preparing reusable source-grounded annotations**. Actual encoder training, model downloads and full-corpus extraction have not started.

## Shared annotation manual

`configs/extraction_schema.yaml` defines the scientific annotation manual; `configs/kg_schema.yaml` defines the final KG vocabulary and evidence dimensions. Version `grounded-observations-6` contains entity and predicate definitions, endpoint constraints, exclusions, synthetic teaching examples and procedures for each stage. It clarifies local protein/gene typing and evidence labels, binds quantity cell references to supplied sources, and identifies critic targets by their original mention IDs during repair. `grounded.system_prompt` embeds this manual in the system message for both model aliases, omitting duplicate stage/evidence-field definitions from the repair prompt where the response contract already supplies them. Original literature and PubTator hints are user-message data, with no authority to change the task. Pydantic generates the model-facing contracts from the same specification.

The manual covers exact and nested mention boundaries; genes versus groups/families/complexes; chemicals versus genes; cell identity versus measurement; species and experiment-specific coreference; expression versus activity/accessibility/binding; perturbation signs; survival versus hazard; primary/cited/speculative attribution; explicit nulls versus missing evidence; and table contrast semantics. It requires a recall pass and explicit incomplete status. Teaching examples are synthetic and are not scientific findings or training labels. Trial answers are not put into prompts.

This implements a published design principle, not a performance guarantee: [GoLLIE](https://arxiv.org/abs/2310.03668) found detailed annotation guidelines useful in a model specifically trained to follow them. Its scores cannot be transferred to these two models merely by improving their prompts.

## Executed workflow and a concrete repair

The deterministic workflow calls LangChain structured models for mention recognition, atomic observation/relation extraction, a fresh source-only read, and field verification. An optional single missing-mention expansion is bounded. PubTator's cached, source-aligned annotations supply candidates for six entity categories; project-specific populations and processes need the LLM pass. This does **not** claim to run a local BioREx relation model. [PubTator architecture](https://academic.oup.com/nar/article/52/W1/W540/7640526).

The first trial revealed that GLM sometimes returned one observation review with repeated check names while omitting the remaining observations. Such reviews were already withheld from acceptance. The revised contract now requires `observation_0`, `observation_1`, etc., each with named, required check objects (ten in the completed version-2 trials, eleven in the new KG-aligned contract). Python assigns indices. Missing observations or checks fail validation; list length cannot masquerade as coverage.

A further host repair preserves a valid source mention when an optional species assertion lacks supporting evidence: species becomes null, its proposed value and issue remain recorded, and normalization/scoring stays unresolved. Unknown species is distinct from a known species conflict. This prevents a metadata error from erasing an otherwise useful NER label.

Exact span and schema validation are necessary but do not prove semantics. A fresh source read is independent of the proposed answer, but it is still model-generated. Disagreement is evidence for review; agreement is not ground truth. Overflow currently blocks acceptance and remains a production limitation until source-preserving continuation is implemented and validated.

## Encoder-oriented annotation records

The file-only exporter is:

```sh
.venv/bin/python -m regkg.workflows.annotation_candidates --trial data/work/p4-accuracy/TRIAL_ID
```

It reads frozen source/result checksums and makes no network or LLM calls. It maintains one `annotation_candidates.jsonl` and one receipt in that trial directory, replacing the partial export atomically instead of accumulating numbered copies. Each record contains source text once per bundle, publication/document/asset identity, character offsets, source-aligned PubTator candidates, both models' mentions and relation observations, evidence, dispositions, field checks and call provenance. Nested/overlapping entities remain spans; they are not forced into a lossy flat BIO sequence. Exact span/type agreement is reported only as agreement.

All current outputs have `label_status=UNREVIEWED_CANDIDATES`, `training_eligible=false`, and `missing_labels=UNLABELED_NOT_NEGATIVE`. Rejected and incomplete predictions remain review material. KG acceptance and encoder-label quality are separate: an entity span may be correct while species normalization is unresolved, and a supported relation may lack context needed for graph scoring.

## From candidates to defensible training data

1. Freeze the extraction schema/prompt/configuration after bounded source review. Retain raw predictions and amendments, with reviewer identity and evidence; do not rewrite predictions as though they were correct originally.
2. Adjudicate all entities and eligible relations in selected complete source windows, including omissions and `NO_RELATION` outputs. A second model or this assistant can propose annotations; those remain provisional without independent review. Measure typed-span NER and ordered, qualified relation precision/recall separately on an independently reviewed sample.
3. Keep training, development and test partitions separate by publication **and study/version group**, including overlapping windows, repeated captions and preprint/published versions. Current diagnostic cases are reserved, not exported as training examples. Source reuse conditions travel with the corpus provenance; unknown status is not invented permission.
4. Prepare encoder inputs only after the target task is fixed: typed spans for NER; ordered entity pairs plus predicate, evidence and relevant context/direction targets for RE. Represent uncertain fields with masks. Explicit experimental `NO_EFFECT` is a positive labeled observation of a null result; it is not the classifier's no-relation class. Generate negative pairs only from fully adjudicated regions.
5. Train and evaluate the encoder later under its own bounded assignment. Report held-out performance and coverage before using it to label more literature. Preserve an escalation path for unsupported types or ambiguous contexts rather than silently copying teacher errors at scale.

No claim of high-accuracy training gold, measured end-to-end F1, or completed encoder fine-tuning follows from the current engineering tests or paired-model trial.
