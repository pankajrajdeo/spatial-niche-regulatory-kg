# Lung gene-to-disease papers with transcription-factor target content, 2015 to 2026

## Overview

I searched PubMed for papers that link genes to lung disease and that carry
transcription-factor (TF) to target-gene content. I list 46 papers. All 46 papers
appeared between 2015 and 2026.

Output file:
`/Users/saljh8/Dropbox/LungMAP/TF_target_disease_literature/lung_TF_target_disease_papers.csv`

## Scope and limits

- I cover human lung disease first. I include 2 mouse papers because they define lung
  cell states that the human papers reuse.
- No single paper gives a comprehensive lung gene-to-disease map built on TF-target
  interactions. The field splits in two. Tier A and Tier B papers cover lung disease but
  hold few TF-target edges. Tier C papers hold millions of TF-target edges but carry no
  lung-disease labels.
- I screened 1,962 unique PMIDs by title. I read 47 abstracts. I selected 46 papers.
  The ratio is 46 of 1,962 (2.3%).
- PubMed sorts a large result set by date. My 12 broad queries returned at most 200 records
  each, so those queries favor recent papers. My 13 relevance-sorted probes and my 41
  title-level lookups correct part of that bias, but not all of it.
- I did not read the full text of any paper. Every number in the CSV comes from the title,
  the abstract, or the PubMed record.
- I did not search Google Scholar, bioRxiv outside PubMed, or Web of Science.

## Method

1. `code/pubmed_scan.py` ran 12 broad boolean queries with a 2015-01-01 to 2026-12-31 date
   filter. The queries returned 1,962 unique PMIDs.
2. `code/verify_titles.py` looked up 41 named resources by title. The lookup returned the
   PMID, year, journal, first author and DOI for each match.
3. `code/verify2.py` and `code/verify3.py` ran 25 relevance-sorted probes. The probes found
   resources that the title lookup missed, for example DBTFLC and TF-Marker.
4. `code/fetch_abstracts.py` pulled 47 abstracts through EFetch.
5. `code/build_table.py` re-queried ESummary for the 46 selected PMIDs and wrote the CSV.
   The script asserts that no PMID repeats and stops if PubMed returns no record.

## Tiers

- **Tier A (15 papers)** - lung atlases and lung-disease gene resources. They give the
  gene-to-disease half. They report marker TFs per cell type, not TF-target edges.
- **Tier B (11 papers)** - lung-disease papers that build an explicit TF-to-target model.
  They give both halves, but each one covers one disease.
- **Tier C (16 papers)** - genome-wide TF-target compendia. They give the TF-target half
  at scale. Only hTFtarget, TF-Marker, GRAND, Cistrome DB and the GTEx network papers
  carry a lung or tissue label.
- **Tier D (4 papers)** - gene-to-disease platforms and one lung-function GWAS. They give
  disease associations and variant-to-gene links, not TF-target links.

## Files

- `lung_TF_target_disease_papers.csv` - 46 rows, 11 columns: tier, pmid, year, journal,
  first_author, title, doi, lung_disease_scope, tf_target_evidence, why_listed, pubmed_url.
- `code/` - the 6 scripts I ran.
- `logs/pubmed_candidates.tsv` - the 1,962 screened PMIDs with title, year and journal.
- `logs/verified_titles.txt`, `logs/verified2.txt`, `logs/verified3.txt` - the raw search output.
- `logs/abstracts.txt` - the 47 abstracts I read.
- `parameters.txt` - the query strings, the date filter and the run date.

## How to reproduce

Run each script with `/opt/homebrew/opt/python@3.11/bin/python3.11`. The scripts call the
NCBI E-utilities at `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/`. PubMed adds records
every day, so a later run can return more PMIDs than 1,962.
