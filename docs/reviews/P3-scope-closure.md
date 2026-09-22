# Lead review: P3 scope closure

Latest continuation: [source-gap completion review](P3-source-gap-completion.md). Follow its bounded repairs and source fetches; earlier assignments below are historical.

Date: 2026-09-22. Inputs: worker attachment `36753bf4-ad16-472b-99e2-493d96e3d7e0`, current handoff, scope-closure code/config and generated records over `litcorpus-f8a11dd187098a3d`.

**Decision: bounded audit and validation design accepted, subject to the execution boundaries below. Corpus closure/freeze not accepted yet. No live inference authorized.**

## Independent verification

- [x] 197 tests passed, two existing Docling deprecation warnings; Ruff passed.
- [x] All 91 immutable corpus output checksums match.
- [x] All configured audit spans pass the local bundle-text check. This checks presence, not scientific entailment.
- [x] Selection contains 18 unique bundles from 10 papers. Two are blocked (`NEEDS_CONTEXT`, `NEEDS_ASSET`) and explicitly marked abstention tests.
- [x] All 8,436 original frontier records have distinct kind/ID pairs and a disposition.
- [ ] Newly identified tasks incorporated and disposition closure justified.
- [ ] Required source gaps resolved or explicitly dispositioned, and corpus frozen.

## Decisions, not further permission questions

Relevant nonhuman and unresolved-name evidence may be extracted while preserving source identity, experimental species and uncertainty. This was already allowed by the preceding assignment. It cannot be promoted to verified human regulation. SPIB/PU.1 conflict and mouse experiments with human annotations are appropriate validation cases. Annotation consistency is not experimental-species validation.

Accept the 18 items as a validation design, not an approved live batch or evidence count. Nine anchors are abstracts, six captions and three paragraphs; this is not a validation of all supplementary-table processing. Preserve primary versus secondary attribution and abstract-level limitations. The two blocked examples must exercise the deterministic preflight refusal path, not enter the live extractor. Source-ready examples may test model abstention. Keep expected answers, `may_extract` and `must_reject` annotations in evaluation records and OUT of extractor/verifier model inputs. P4 still requires implementation and tests before any live run. After source repairs, refresh affected selections against the new source hashes; do not claim a formerly blocked item remains blocked if it is repaired.

Habermann table semantics cannot be decided by reviewer preference. Recover them from the paper, supplement documentation or versioned analysis code. Preserve original `avg_logFC` and `p_val_adj`; do not infer log base, numerator/denominator or sample-aware statistics from a filename. Published expression/DE results remain distinct from regulatory findings and from the project's descriptive Yale signatures. If semantics remain undocumented, retain unknown fields and restrict interpretation. No invented direction/significance claims.

## Scope-record corrections

1. **Provisional is not closed.** The code closes 124 bundles because all context labels are provisional background/irrelevant and 110 article requests because they are lower-priority background. An unrequested download may be closed as an acquisition action without claiming its paper is scientifically irrelevant. Keep scientific relevance provisional unless supported by a reviewed rationale; record disposition approval separately from the proposed rule.
2. **New tasks are not reconciled.** All three `additional_acquisition_needs` IDs are absent from `frontier_dispositions`. Add them or explicitly link them to existing equivalent tasks without double-counting. Distinguish table interpretation from acquisition/parse repair. Identification does not automatically establish that a download is necessary.
3. **Counts are heterogeneous.** 647 blocked bundles and their 745 investigations describe linked work, not 1,392 independent scientific cases. Likewise table, reference and download rows overlap. Report these units separately; 8,202 open rows is not an estimate of manual workload. The 32 MB ZIP is a supplement download, not a 177th article. Report required user downloads separately from possible/background article records and automated acquisition.
4. **Coverage claims must be qualified.** Exact phrase/co-mention searches in available parsed text diagnose retrieval/parse gaps. They do not establish that a population has no regulatory literature. The selected KRT abstract itself mentions aberrant basal-like cells in a different claim, so blanket wording that no bundle names that population is too strong. Distinguish mention, experiment-linked TF finding and direct regulation.

## Next bounded assignment

Follow [P3 source-gap completion](../assignments/P3-source-gap-completion.md). The 32 MB OA supplement and local Adams table repair are authorized routine work; no additional user permission is needed. Do not repeat broad pipeline design. Required work remains open until completed or explicitly dispositioned. P4 live calls, commits and pushes remain unapproved. This review changed only documentation, not artifacts or code.
