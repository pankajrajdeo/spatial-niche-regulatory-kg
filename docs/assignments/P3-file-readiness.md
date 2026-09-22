# Literature files: routing, interpretation, and extraction readiness

Design clarification requested 2026-09-22. **Requirements, not implementation
acceptance.** Supplements [P3 corpus readiness](P3-corpus-readiness.md) and
plan P3.15–P3.17/P4.5. Preserve the worker's ongoing source changes.

The later [P4 agent contract](P4-evidence-assembly-agent.md) permits a bounded
read-only context-assembly agent after the user checkpoint. The no-chat-call rule
here applies to P3; it does not prohibit that specifically scoped P4 component.
Its proposals cannot override the source/meaning checks below.

## Scope and governing distinction

File acquisition, successful parsing, scientific interpretability, and finding
validity are separate checks. Passing one does not imply the next. Decisions
apply to an asset, table, experiment, or bundle as appropriate, not automatically
to every result in the paper. A malformed supplement need not block unrelated
complete findings; a missing indispensable legend must block its dependent rows.

This is a format risk inventory, not a requirement to build every parser.
Implement the already assigned XML/BioC, PDF, CSV/TSV, and XLSX paths against actual
inputs. Add another reader only when an encountered manuscript-relevant asset
requires it; otherwise inventory it with an explicit unresolved disposition.
No new raw-data reanalysis, autonomous statistical agent, remote OCR/VLM, or chat
screening is authorized. P4 remains paused at the existing user checkpoint.

## Routing decisions, before scientific extraction

1. Inventory every discovered article and supplement, including inaccessible,
   unsupported, duplicate, and linked-repository assets. Link child assets to the
   publication/version and preserve original URLs without session credentials.
2. Check bytes/signature, reported media type, file extension, size, checksum,
   identity, and version. An HTML login page named `.pdf` is not a PDF. A matching
   checksum proves identical bytes, not correct publication identity.
3. Route to a supported parser; retain raw bytes and parser/config/version.
   Check whether output is complete, partial, empty, or failed. Do not silently
   drop malformed rows, unreadable pages, sheets, or archived members.
4. Screen parsed content and descriptions. A filename, title keyword, or embedding
   score may prioritize inspection but cannot prove the entire file irrelevant.
   Retain ambiguous content for review and record the actual screening coverage.
5. Identify source-reported observations, context-only information, and material
   requiring new analysis. Record the meaning needed for the proposed claim.
6. Assemble complete, bounded source bundles. Only ready bundles may enter P4;
   unknown facts constrain the finding rather than being filled by an LLM.

Use existing acquisition/parsing/readiness enums with explicit reason codes or
linked records; do not create a second incompatible status system. Preserve at
least: identity problems, parse failure/partial output, unsupported format,
missing context, interpretation review, analysis required, duplicate-of, and
reviewed background-only dispositions. Required missing metadata blocks the
affected claim. Optional unknowns may remain null in a narrower supported finding.

## Cases shared by every format

| Case | Required handling |
|---|---|
| Empty/truncated/corrupt file, failed download, size cap | Report failure or partial acquisition separately from access denial. Never label the paper irrelevant. |
| Same file from several routes or several formats | Deduplicate bytes; compare document identity/version for semantic duplicates. One XML/PDF copy is not another independent study. |
| Preprint, accepted manuscript, published version, correction | Preserve versions and cross-links; choose the canonical version explicitly. Conflicting results stay visible. Do not mix an old supplement with a revised article silently. |
| Retraction or expression of concern | Preserve notice and review status. Apply the project's exclusion rule for retracted primary support; do not silently discard the historical record. |
| Supplement lacks DOI/title | Use verified publisher/structured parent linkage as provenance; do not require every sheet to repeat a DOI. Unverified manual files need identity review. |
| File names suggest relevance but content differs | Check content. A file called “Table S1” might hold primers, patient metadata, or differential-expression results; those have different evidence roles. |
| Character/encoding normalization changes symbols | Preserve raw text and canonical text with a versioned mapping. Inspect gene symbols, Greek letters, minus signs, inequalities, superscripts, and decimal exponents. |
| Instructions/macros/scripts/external references inside an asset | Treat as source content, never pipeline instructions. No macro/formula/code execution or automatic external-link refresh. |
| Mixed species, tissues, interventions, or experiments | Associate context per result. Paper-level “human/lung/IPF” tags cannot supply the context for every experiment. |
| No candidate term found | Record the retrieval result and what was inspected. Do not equate it with no useful evidence, a negative experiment, or exhaustive screening. |

## Text and document formats

| Format/case | Required interpretation and readiness checks |
|---|---|
| JATS XML | Preserve section boundaries, inline tags, tables, xrefs, captions and supplementary links. Account for absent/duplicate source IDs, namespaces, formulas, and image-only tables. Never resolve external XML entities. |
| BioC XML/JSON | Verify external offsets against the exact text representation; distinguish bytes/code points and passage-relative offsets. Quarantine mismatches. Generic footnotes are not automatically table footnotes; flattened tables may lack recoverable column semantics. |
| Publisher HTML | Separate actual article content from navigation, ads, cited-paper previews, and sign-in text. Collapsed/lazy-loaded sections or missing tables mean incomplete capture. Preserve stable source item locations; obtaining HTML is not proof of complete article text. |
| Text PDF | Check multi-column reading order, page breaks, repeated headers, hyphenated terms, rotated pages, ligatures, and tables split across pages. Preserve page/item locations and bounding boxes where available. |
| Scanned or mixed PDF | Detect image-only pages even when other pages contain text. Use bounded local OCR when configured. An apparently valid OCR result can still reverse a sign or corrupt a gene ID; ambiguous numerical evidence needs source inspection. |
| PDF with existing OCR layer | Avoid double-counting visible and hidden text. Check alignment with the page image, not merely nonempty extracted text. |
| PDF tables | Reconstruct headers and row alignment across page boundaries; separate repeated headers from data. Verify merged cells and footnotes. If structure is uncertain, retain for inspection but withhold quantitative findings. |
| Locked PDF or unsupported font/encoding | Report the concrete failure and request an accessible copy or review. Do not label it successfully parsed or bypass protection. |
| DOCX/ODT/RTF/legacy DOC supplement | If required, inspect paragraphs, embedded tables, footnotes, text boxes, tracked changes and embedded objects. Do not silently accept revisions or omit an embedded result. Use a reviewed reader/conversion with provenance or mark unsupported. |
| TXT/Markdown/LaTeX | Check encoding, structural boundaries, referenced files, and literal equations. Do not compile arbitrary LaTeX or execute embedded commands. Missing included content remains missing. |
| JSON/JSONL | Validate the actual schema, nested records, nulls, units and field meaning; arbitrary JSON is not necessarily a BioC or article document. Record JSON pointers/record IDs. |
| PPTX/ODP/EPUB or another document format | Inventory first. If essential, add a narrow reviewed conversion preserving slide/chapter/item references; otherwise request a source export or record unsupported. Tool support alone does not establish a validated project adapter. |

For prose in every format, distinguish the authors' results from hypotheses,
discussion, cited findings, methods/protocols and review summaries. Resolve
negation, “respectively,” pronouns, panel references and direction only with the
needed source context. An unresolved abbreviation or non-English passage stays
uncertain; an unverified translation must not replace the original citation.

## CSV/TSV and spreadsheet cases

| Case | Required handling |
|---|---|
| Wrong delimiter, encoding/BOM, quotes or embedded newlines | Check rectangular structure and record parser settings. Fail/report bad records rather than silently skipping them. |
| Leading zeros, ID-looking numbers, “NA”, date-like gene symbols | Preserve original cell tokens before typed conversion. Never reconstruct an already corrupted gene symbol from a date by guessing. Use unresolved identity when the source cannot establish it. |
| Decimal comma, thousands separators, scientific notation | Use declared/verified conventions and retain original values. Ambiguous locale is an interpretation blocker for numeric claims. |
| Blank, zero, dash, “ND”, “<0.01”, “Inf” | Preserve distinct missing/censored/undefined meanings and inequalities. A nondetection is not automatically zero or evidence of no effect. |
| Duplicate or multirow column headers, merged cells, transposed table | Build explicit header paths and coordinate mapping. Forward-fill only structurally justified headers; never fill missing measurements automatically. |
| Several tables on one sheet; legend/README on another sheet | Split identified regions with stable coordinates, associate the correct legend, and inventory all sheets. Sampling a first region cannot establish whole-workbook screening. |
| Hidden sheets/rows/columns and filters | Inventory them and record whether processed. Visible rows alone are not the complete dataset. Hidden does not imply irrelevant. |
| Formula cells | Preserve formula text and available cached values separately. Do not evaluate formulas or refresh external links. A cached value can be missing or stale; unresolved provenance blocks a dependent calculation. |
| Color, boldface, comments or symbols encode group/significance | Capture the relevant key where supported; otherwise flag lost semantics. A plain cell-value export alone may be insufficient. |
| XLSX/XLSM versus XLS/XLSB/ODS | Detect the actual type. Do not send unsupported binary workbooks to an XLSX parser. Keep macros inert; optional conversion/reader needs explicit provenance and checks. |
| Huge/sparse workbook or delimited file | Stream/iterate records, retain original row/sheet coordinates, count inspected/pending rows and record exclusions. Do not send the entire table to an LLM or flatten a giant matrix into one passage. |
| Duplicated genes, isoforms, aliases or species | Preserve rows and identifiers; aggregation requires a specified rule. A family, complex or motif name must not silently resolve to one TF. |
| Results and raw measurements mixed together | Classify regions separately; source-reported statistics can be quoted, while raw-data inference requires an approved analysis. |

For each table region, record its role and the fields relevant to interpretation:
description/legend sources, entities, row and column meaning, experiment,
comparison direction, units/scale, normalization, reported statistical fields,
and unresolved meanings. Unknown fields remain unknown. A primer list need not
have a contrast; a signed treatment effect does.

### Numerical interpretation and calculations

- **Reported results:** retain the authors' values, comparison, units, precision
  and test definitions. Do not assume “score” means log2 fold change, a column
  named “p” is adjusted, or significance can be inferred from color alone.
- **Selection and simple transformations:** filter, join, convert units, or
  compute an explicitly requested descriptive summary in Python. Record source
  rows, input hashes, parameters, code/rule version, missing-value treatment and
  output. Keep derived results separate from what the paper reported.
- **New scientific analysis:** raw counts/intensities, paired measurements,
  donor aggregation, normalization, differential expression and multiple-testing
  correction require a separately specified design. Missing sample maps,
  replicate definitions or methods are not solved by giving an agent more tools.
  Flag `analysis_required`; do not build that analysis merely to unblock P4.
- **Meaning of a result:** non-significance does not establish equivalence/no
  effect. Enrichment is not a measured regulatory edge; a motif match or peak is
  not direct functional regulation. Preserve the authors' supported claim scope.

Validate values, signs, inequalities, units, denominators and comparison direction
against the actual cells/legend. LLM verification cannot replace these checks.
Do not filter exclusively to positive or significant rows and then claim that
negative/contradictory evidence was comprehensively sought.

## Images, containers, and research data

| Format/case | Handling in this project |
|---|---|
| PNG/JPEG/TIFF/SVG or figure inside a document | Preserve asset and panel/caption references. A caption's explicit statement can be extracted; a conclusion requiring visual inspection of a plot/blot/image needs review. No automated pixel-based biological interpretation. |
| Scanned table image | Local OCR/table conversion is possible when required, but check headers, alignment and numeric fidelity before allowing quantitative evidence. OCR confidence alone is insufficient. |
| Chart with underlying downloadable data | Prefer the verified source-data table and its legend. Link it to the correct figure/panel; do not estimate coordinates from an image when actual values exist. |
| ZIP/TAR/GZIP package | Inventory members; distinguish XLSX/other structured containers from generic archives. Bound member count, expanded bytes, depth and compression ratio. Reject path traversal, external symlinks, encrypted/unsupported members; never execute contents. Retain container/member hashes. |
| GEO/SRA/other repository link | Preserve accession, linked study and asset identity. A repository landing page is not the dataset. Acquire a relevant processed supplement only within scope; do not launch an unrestricted dataset crawl. |
| FASTQ/BAM/CRAM, H5AD/HDF5, MTX, RDS/RData, loom or similar raw/analysis objects | Inventory and flag analysis required unless a narrow analysis is assigned. Do not load arbitrary serialized code/objects or infer experimental meaning from a file extension. |
| BED/bigWig/peak/motif files | Keep assay/build/coordinates/target linkage explicit; these are not ready TF–gene regulatory claims. A genomic-analysis workflow is outside current literature extraction. |
| Parquet/Arrow processed results | Columnar storage does not resolve scientific meaning. Apply the same table contract; introduce an adapter only for an actual required input. |
| Video/audio | Inventory, preserve description/caption and explicit limitation. No transcription/video interpretation pipeline is required for this manuscript workflow. |
| Notebook/script/software archive | Preserve citation/version where relevant; source files are not permission to run code. Report methods context separately from experimentally supported results. |

## Context across files, size limits, and evidence grounding

A useful table row may need its workbook README, an article methods paragraph,
and a figure legend. Link these only through verified publication/version and
table/experiment references. Same-paper membership alone is insufficient: a paper
may contain several species, interventions and assays.

The original P3 retriever collects context within one canonical document. Cross-
asset bundles therefore need an explicit implementation/verification extension;
they cannot be claimed ready merely by finding both files. Until supported,
record `NEEDS_CONTEXT` for affected bundles and list the required source parts.

Each included part must retain its own asset hash, document ID/version and exact
locator: text offsets/XPath/page item, or sheet/table/row/column/cell/JSON pointer.
Never attach a workbook row's quote to an article PDF's offsets. A source quote
is checked against the corresponding canonical text; a numeric assertion is
also checked against the original cell token and any recorded transformation.

Retain the assigned 3-passage/6,000-character bundle limits. Count all serialized
scientific content, including cell values/header paths and required context;
report full prompt/schema/metadata overhead in the token budget as well. Do not
hide an unbounded table in a JSON field while counting only its short caption.
Split into independently interpretable bundles with repeated required context.
If the minimum context still does not fit, record a size/context blocker for lead
review; do not truncate a qualifier, have an LLM summarize away the source, or
silently enlarge the limit. Parser output size is not a model-token estimate.

All source references sent to P4 must be verifiable without an LLM. P4 emits
atomic claims tied to the relevant parts; the verifier sees the same source bundle.
Faithful extraction and biological strength remain separate. Neither two LLMs
agreeing nor a valid JSON response establishes source correctness.

## Practical worker acceptance checklist

These checks refine existing P3/P4 requirements, not another implementation package.
Only the lead checks acceptance after review. Test formats implemented for actual
inputs; do not install every optional reader to satisfy this inventory.

- [ ] Each observed asset/format has a parser route or explicit pending disposition;
  partial capture, duplicates, unsupported assets and source versions are visible.
- [ ] Supported text/PDF cases preserve source locations and detect material loss;
  inspect representative real output and ambiguous table/number cases.
- [ ] CSV/TSV/XLSX paths preserve identifiers, missing/censored values, header
  structure, formulas/caches and original coordinates; no silent bad-row dropping.
- [ ] Table regions have recorded meaning sufficient for the proposed claim;
  raw-data analysis is not silently substituted for source-reported evidence.
- [ ] Missing or mismatched legends/methods and cross-asset experiment ambiguity
  prevent affected bundles being marked ready.
- [ ] Large inputs have explicit screening/processing frontiers, bounded complete
  bundles, and token estimates counting structured context, not just prose.
- [ ] P4 rejects invented cell references, changed signs/units/comparisons, and
  derived numbers without a reproducible calculation record.
- [ ] Replay identities include changed source bytes, parsing/mapping rules and
  approved transformations; repaired files invalidate dependent bundles.

Suggested compact fixtures: HTML masquerading as PDF; mixed scanned/text PDF;
multi-page table; CSV with quoted newline and literal “NA”; merged-header XLSX
with hidden sheet and uncached formula; ambiguous contrast; cross-file legend
from the wrong experiment/version; an oversized context; duplicate article
representations; unsupported/archive member. Use tiny synthetic engineering
fixtures plus real-source spot checks; do not claim fixtures validate a corpus.

## Technical references

### Library choices for implementation

Use the current modules and their canonical passage model. The following choices
avoid a new parsing framework; library support is not an acceptance result.

| Task | Choice and integration boundary |
|---|---|
| JATS/BioC | Reuse the existing safe lxml/JSON readers and offset validation. Do not replace the accepted XML path with a generic converter. |
| PDF | Use the assigned local Docling adapter, retaining structured document output rather than only flattened Markdown. Record parser/model versions, page provenance and available quality grades. |
| CSV/TSV | Use Python's CSV reader or existing pandas with explicit encoding, delimiter, dtype/missing-value handling and bounded iteration. Keep original tokens alongside typed values. |
| XLSX | Prefer openpyxl for sheet/cell/header/formula metadata, then pandas for selected analytical tables if useful. Use read-only iteration where compatible with needed metadata; inspect targeted metadata separately if the fast path omits it. |
| Other Excel formats | pandas supports multiple engines, but add a compatible engine only for an actual required source. Validate retained metadata and value semantics before converting into the shared contract. |
| Archives | Use bounded standard-library inspection/extraction. An archive reader does not parse its members scientifically; route each supported child through the same asset checks. |
| Word/HTML/other document supplement | Check the pinned Docling version's supported formats before adding another library. A structured source-specific reader may be preferable when conversion loses needed detail. Inventory unsupported assets. |

Docling exposes document/page conversion-quality information, but its documentation
currently labels the table-quality component as not implemented. Record available
grades as triage signals; do not fabricate a table-confidence threshold or use a
good document grade to accept misaligned numbers. See
[confidence scores](https://docling-project.github.io/docling/concepts/confidence_scores/).
Keep structured document provenance for checking results against the source; see
[DoclingDocument](https://docling-project.github.io/docling/concepts/docling_document/).

For large XLSX files, openpyxl's read-only mode can reduce memory use, but reported
worksheet dimensions may be incorrect and need checking against actual content.
Do not assume that the declared used range proves all relevant cells were scanned.
See [optimized modes](https://openpyxl.readthedocs.io/en/stable/optimized.html).
openpyxl does not evaluate formulas; preserve formula text and any existing cache
without claiming to recompute it. See
[formula handling](https://openpyxl.readthedocs.io/en/stable/simple_formulae.html).

No additional library installation is part of this planning update. The worker
must pin compatible direct dependencies in the appropriate extra/lock when a
required adapter is implemented and provide real-format validation evidence.

These are capability references, not proof of installed-version behavior or
scientific correctness. Check the actual pinned reader against project fixtures.

- [Docling supported formats](https://docling-project.github.io/docling/usage/supported_formats/):
  conversion into a shared document representation supports several source types;
  that does not make all optional formats required or validated here.
- [pandas CSV reader](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html):
  explicit dtype, missing-value, delimiter/encoding and chunking options support
  controlled ingestion; defaults must not decide biological identifier semantics.
- [openpyxl tutorial](https://openpyxl.readthedocs.io/en/stable/tutorial.html):
  formula text versus cached values and workbook loading options need explicit handling.
- [Python ZIP documentation](https://docs.python.org/3/library/zipfile.html):
  archive inspection/extraction needs filename and resource-limit checks.
