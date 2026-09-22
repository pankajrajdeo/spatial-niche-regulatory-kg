# Experimentally defined molecular interactions for lung edge building

## Overview

I searched PubMed for papers that report **measured** molecular interactions usable as network
edges: protein-DNA (ChIP-seq, CUT&RUN, CUT&Tag, footprinting) and protein-protein (affinity
purification mass spectrometry, proximity labeling, yeast two-hybrid). I added papers that
**validate** an edge by perturbation (Perturb-seq, CRISPRi of a bound element). I list 71 papers.

Output file:
`/Users/saljh8/Dropbox/LungMAP/TF_target_disease_literature/lung_experimental_edge_papers.csv`

I excluded single-cell RNA co-expression networks. Co-expression gives a correlation, not a
measured interaction. The companion file `lung_TF_target_disease_papers.csv` holds that class.

## Tiers

- **T1, lung TF binding (36 papers).** A transcription factor was pulled down in a lung, airway or
  alveolar cell, or in a lung cell line. Each row names the cell type and the condition.
- **T2, perturbation with molecular readout (9 papers).** A gene or an enhancer was perturbed and
  the transcriptome was read. 3 of the 9 use non-lung cells; the CSV marks them "NOT lung".
- **T3, cell-type-labelled TF-DNA compendia (14 papers).** Reprocessed public ChIP-seq, DNase and
  ATAC data with a biosample label. You filter these to lung biosamples.
- **T4, protein-protein interaction (12 papers).** 8 are proteome-scale reference maps built in
  non-lung cells. 4 report lung-specific complexes.

## What the search found, and what it did not

- **Lung protein-DNA data exist, but concentrate in cancer.** Of the 36 T1 papers, 14 study lung
  cancer cell lines or tumors. Only 4 report a transcription factor pulled down from primary
  human lung or airway tissue.
- **Cell-type-resolved protein-protein data in lung barely exist.** I found 4 lung-specific PPI
  papers against 8 proteome-scale maps built in HEK293T, HCT116 or ORFeome systems. No study maps
  the interactome of a named lung cell type.
- **One paper reports both edge classes in lung:** PMID 33731112 (Lüdtke, Respir Res 2021) gives
  TBX2 DNA occupancy and TBX2 protein partners in the developing lung.
- **The best edge-context example** is PMID 31782890 (Hokari, Mol Oncol 2020). TTF-1/NKX2-1 binding
  regions differ by 75.0% between an SCLC line and a LUAD line. The same TF, two contexts, two
  edge sets.
- **The best in vivo cell-type contrast** is PMID 33947861 (Little, Nat Commun 2021). NKX2-1 binds
  different sites in AT1 and AT2 cells in the mouse lung, and YAP/TAZ loss redirects the binding.

## Scope and limits

- Date filter: 2015-01-01 to 2026-12-31. 1 of the 71 papers is from 2015, so the set spans 11 years,
  not 10.
- I screened 2,429 unique PMIDs from 30 boolean queries, then ran 51 targeted probes for named
  resources. I read 62 abstracts. I selected 71 papers.
- The title screen used a keyword score. The score favors large-scale wording, so it can miss a
  small but rigorous single-TF study. The 51 targeted probes reduce that gap; they do not close it.
- I read no full texts. Every number in the CSV comes from a title, an abstract or a PubMed record.
- I did not collect GEO or ENCODE accessions. Accession collection is the next step.
- I included mouse studies when they map binding in native lung tissue. The CSV names the species
  in the cell_type_or_biosample column.

## Method

1. `code/edge_sweep.py` ran 15 boolean queries in two sort orders, 30 searches in total, and
   returned 2,429 unique PMIDs.
2. `code/screen.py` scored every title. The score adds 2 per edge-assay word, 1 per scale word,
   1 per lung word, and subtracts 4 per low-evidence word.
3. `code/verify_edges.py` and one inline probe script ran 51 targeted lookups for named resources
   and named authors.
4. `code/build_edges.py` re-queried ESummary for the 71 selected PMIDs and wrote the CSV. The
   script stops if a PMID repeats or if PubMed returns no record.

## Files

- `lung_experimental_edge_papers.csv` - 71 rows, 13 columns: tier, pmid, year, journal,
  first_author, title, doi, assay, cell_type_or_biosample, condition, edge_type, scale_or_note,
  pubmed_url.
- `code/edge_sweep.py`, `code/screen.py`, `code/verify_edges.py`, `code/build_edges.py`
- `logs/edge_candidates.tsv` - the 2,429 screened PMIDs.
- `logs/verified_edges.txt`, `logs/verified_edges2.txt` - the targeted probe output.
- `logs/edge_abstracts.txt` - the 62 abstracts I read.

## Suggested next step

Pull GEO and ENCODE accessions for the T1 and T3 papers, then build one edge table with columns:
TF, target gene, cell type, condition, assay, source PMID, source accession, peak or interaction
score. Keep the assay and the cell type on every edge. Do not merge a cancer cell line edge with a
primary cell edge without a flag.
