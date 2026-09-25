# Automated critique and repair

The user's instruction “i want this automated..do now” authorizes implementation and a bounded live check of the proposed P4 correction workflow. This is now the default extraction engine, not a separate manual review script. Full-corpus extraction is still stopped while scientific accuracy remains unresolved.

Prior live check: `trial-2c83876001d2386b`, three existing source bundles, **77 focused tests passed**, identical replay **zero new calls**. Both nonempty cases completed repair and fresh review; all eleven final observations remained rejected. Read the [prior source audit and implementation evidence](../reports/continuation/p4/critique-repair-review.md). The subsequent user instruction to continue authorized targeted corrections below; current execution status is in CONTINUE_HERE and the latest handoff.

## Execution

`grounded-observations-6` uses the existing LangChain structured-call adapter and Pydantic contracts. The configured extractor is LiteLLM `prescient.glm-5.3-flash`; `configs/extraction.yaml` selects `litellm:prescient.kimi-k3` for independent reading, field verification and criticism. Existing environment/provider precedence is preserved. The old paired-model trial remains available; a bounded hybrid run can select the configured roles explicitly.

1. Assemble source-only experimental evidence frames before mentions/observations. Each stated context field has exact source citations; unknown fields are omitted, not inferred. Frame IDs are assigned in Python. Frame slots are fixed named keys, preventing duplicate field entries. Observations must copy the selected frame’s measured-variable label exactly; host code rejects mismatches. Frames remain proposals and the semantic verifier checks experiment/result correspondence. A bounded frame-amendment pass can supply omitted or corrected frames before an observation patch, retaining original frames in the audit.
2. If frames identify a grounded missing reference, invoke the existing bounded local assembly agent, retain all original anchors, and rebuild frames before extraction. Source links must still be validated; shared publication identity does not establish a shared experiment.
3. Recognize source mentions using PubTator candidates and local assay context. Extract atomic observations referring to host-assigned frames and mention IDs. The final 20-node/29-relation KG vocabulary is unchanged.
4. Read source facts independently without proposed frames or answers. Check observations in batches of at most two against original source and their experiment fields, then audit mention/fact coverage. Python handles source spans, schemas, endpoint eligibility, quantities and contradictions it can establish mechanically. Stage prompts no longer repeat every other stage's instructions.
5. Apply one bounded correction pass. The model returns individual observation patches, original-observation hashes, changed-field lists and source evidence. Host code enforces the correction scope and preserves all other fields/observations; missing-finding additions require an explicit omission. Patch application is atomic. Entire affected findings are reverified; shared dependency changes cannot bypass semantic checks. Full bundle review currently also runs after repair for conservative omission auditing.
6. Keep finding disposition separate from bundle coverage. An unrelated unconnected mention or omitted fact does not downgrade an independently verified finding. Unresolved endpoint, matching fact, relevant context or unavailable critique still blocks acceptance of the dependent finding. Bundle coverage stays INCOMPLETE while any audit defect remains.

P4 evidence packages now allow eight original parts and 16,000 serialized characters. Frozen P3 manifests are unchanged. The agent retains four model calls/eight tool calls per investigation and finite tool/input/time bounds; context beyond those bounds remains explicit. Pre-extraction and post-critique investigations retain their own accounting. The conservative upper scheduling bound is 36 model calls per bundle (including two four-call context investigations, frame/source refreshes, one frame-amendment pass, up to eight two-finding review batches per pass and one mention expansion), excluding separate capability checks/transport retries. Cumulative accounting is never reset.

Model-visible parts retain document IDs, original figure/table IDs and labels, page/bounding-box/locator metadata and table structure when available. No label, panel or scientific linkage is fabricated when the existing parse lacks it. Context navigation remains within the host-pinned canonical document; cross-asset joins require separately validated links. Figure pixels are not interpreted by this change.

## Targeted corrections after the first live diagnostic

The canonical vocabulary remains unchanged. `spatial-nichelinker-kg-2` clarifies evidence-category meanings in the model-facing field description: CURATED_LITERATURE requires an attributed pre-existing curated assertion/resource, rather than merely a finding read in a paper. Unclassified primary non-TF effects retain null evidence type, with their intervention, assay, result and functional directness preserved. These are explicit operational annotation definitions for previously underdefined labels, not new biological results.

The mention manual now distinguishes the local protein detected by immunostaining or nuclear localization from a transcript or genotype component. PubTator's Gene candidate cannot override the molecular form stated by the local assay. The critic must supply corrected source-grounded mentions, not only textual complaints.

Repair feedback now attaches original mention IDs/surfaces/types to criticism. Previously, `mention_N` slots referred to an inventory whose positions could change after removing unsupported mentions; that made a valid criticism ambiguous to the repair model. Source offsets and original reviews remain preserved.

The Pydantic quantity contract is constructed from the actual source bundle. A prose/caption-only bundle permits only null cell references; table bundles permit supplied cell IDs or null, with the existing host checks still requiring the correct table cell/value pair. The contract refreshes after context recovery. Qualitative changes need no numeric quantity; reported table values must still be retained without recalculation. This constrains invalid output before inference without silently repairing source values or weakening the validator.

## Provenance and persistence

Bundle outcomes preserve original/final observations, initial/final mention inventories, two review snapshots at most, deterministic defect assessments, repair change counts, unresolved issues, source hashes and call/cache identities. Raw model responses remain in the existing shared cache. Context-recovered sources and PubTator assets are checked and included in annotation export. Nothing is promoted to a new graph schema or a training gold label by model agreement.

Repair feedback omits redundant passed checks while preserving all actionable defects; oversized critic feedback uses the same compaction. Original source text and the complete saved reviews are preserved. The 60,000 conservative input-token bound is unchanged. The local assembly role uses low reasoning and a 2,500-token response allowance after the initial live diagnostic exposed truncation at 1,000 tokens. Its four-call/eight-tool limits remain unchanged; a named context repair retains the original stopped ledger and cumulative usage.

The ordinary extraction writer still preserves accepted broad findings while restricting canonical RegulatoryClaim projection to eligible resolved gene-level evidence. Full-source processing failures remain distinct from `NO_RELATION`, explicit experimental nulls, and incomplete criticism. A completed live diagnostic is not an accuracy estimate or manuscript acceptance.

## Commands

```sh
.venv/bin/python -m pytest tests/test_critique_repair.py tests/test_kg_contract.py tests/test_grounded_extraction.py tests/test_extraction.py tests/test_annotation_candidates.py -q

SSL_CERT_FILE="$PWD/data/external/tls/project-ca-bundle.pem" \
  .venv/bin/python -m regkg.workflows.extraction_trial --live \
  --model prescient.glm-5.3-flash --critic-model prescient.kimi-k3 \
  --context-repair-id critique-budget-fix \
  --case joint_gene_loss --case organoid_endpoints --case atlas_no_relation
```

The selected diagnostic inputs are existing frozen P3 bundles. No acquisition, parsing or embedding is repeated. Log: `data/work/p4-accuracy/critique-repair.log`; the run's manifest/status/results live under its content-addressed trial directory. Read the latest handoff before rerunning a completed diagnostic. Same-input structured calls reuse the existing cache.

Remaining scientific validation: bounded source regression checks and explicit disposition of unresolved context/overflow. Independently established labels are required for measured precision/recall claims, not a new prerequisite to finish the manuscript KG. The automated critic can still miss errors or propose bad corrections; tests verify that known structural/source failures are blocked, not that semantic accuracy is perfect.
