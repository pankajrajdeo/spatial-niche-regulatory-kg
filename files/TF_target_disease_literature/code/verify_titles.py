import json, sys, time, urllib.parse, urllib.request

BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

CANDIDATES = [
 "LungMAP The Molecular Atlas of Lung Development Program",
 "Lung Gene Expression Analysis web portal",
 "LungMAP Portal Ecosystem",
 "A census of the lung CellCards from LungMAP",
 "A molecular cell atlas of the human lung from single-cell RNA sequencing",
 "An integrated cell atlas of the human lung in health and disease",
 "Single-cell RNA-seq reveals ectopic and aberrant lung-resident cell populations in idiopathic pulmonary fibrosis",
 "Single-cell RNA sequencing reveals profibrotic roles of distinct epithelial and mesenchymal lineages in pulmonary fibrosis",
 "A cellular census of human lungs identifies novel cell states in health and in asthma",
 "Characterization of the COPD alveolar niche using single-cell RNA sequencing",
 "TRRUST v2 an expanded reference database of human and mouse transcriptional regulatory interactions",
 "hTFtarget a comprehensive database for regulations of human transcription factors and their targets",
 "ChEA3 transcription factor enrichment analysis by orthogonal omics integration",
 "Benchmark and integration of resources for the estimation of human transcription factor activities",
 "Expanding the coverage of regulons from high-confidence prior knowledge for accurate estimation of transcription factor activities",
 "RegNetwork an integrated database of transcriptional and post-transcriptional regulatory networks in human and mouse",
 "GTRD a database on gene transcription regulation",
 "TFLink an integrated gateway to access transcription factor-target gene interactions for multiple species",
 "KnockTF a comprehensive human gene expression profile database with knockdown or knockout of transcription factors",
 "ChIP-Atlas an integrative web resource for exploring public ChIP-seq data",
 "Cistrome Data Browser expanded datasets and new tools for gene regulatory analysis",
 "The Human Transcription Factors",
 "Understanding Tissue-Specific Gene Regulation",
 "GRAND a database of gene regulatory network models across human conditions",
 "Expanded encyclopaedias of DNA elements in the human and mouse genomes",
 "The DisGeNET knowledge platform for disease genomics",
 "Open Targets Platform facilitating therapeutic hypotheses building in drug discovery",
 "Comparative Toxicogenomics Database update",
 "Understanding multicellular function and disease with human tissue-specific networks",
 "PulmonDB a curated lung disease gene expression database",
 "Multi-ancestry genome-wide association analyses improve resolution of genes and pathways influencing lung function and chronic obstructive pulmonary disease",
 "Genome-Wide Association Study of Susceptibility to Idiopathic Pulmonary Fibrosis",
 "Transcription factor activities enhance markers of drug sensitivity in cancer",
 "A modular master regulator landscape controls cancer transcriptional identity",
 "Single-cell multiomic profiling of human lungs reveals cell-type-specific and age-dynamic control of SARS-CoV2 host genes",
 "Regulatory analysis of the human lung",
 "Integrated single-cell atlas of human lung fibrosis",
 "A single-cell atlas of the human healthy airways",
 "Construction of a human cell landscape",
 "Comprehensive epigenomic profiling of human alveolar epithelial differentiation identifies key epigenetic states and transcription factor co-regulatory networks",
]

def esearch_title(term, retmax=8):
    q = " AND ".join(['"%s"[Title]' % term]) if False else '%s[Title]' % term
    url = BASE + "esearch.fcgi?db=pubmed&retmode=json&retmax=%d&term=%s" % (retmax, urllib.parse.quote(q))
    with urllib.request.urlopen(url) as f:
        return json.load(f)["esearchresult"]["idlist"]

def esummary(pmids):
    if not pmids: return {}
    url = BASE + "esummary.fcgi?db=pubmed&retmode=json&id=" + ",".join(pmids)
    with urllib.request.urlopen(url) as f:
        return json.load(f).get("result", {})

for c in CANDIDATES:
    ids = esearch_title(c)
    time.sleep(0.35)
    res = esummary(ids)
    time.sleep(0.35)
    print("### QUERY: %s" % c)
    if not ids:
        print("    NO MATCH")
    for p in ids:
        r = res.get(p)
        if not r: continue
        au = r.get("sortfirstauthor", "")
        doi = ""
        for aid in r.get("articleids", []):
            if aid.get("idtype") == "doi": doi = aid.get("value", "")
        print("    PMID %s | %s | %s | %s | %s | DOI %s" % (
            p, (r.get("pubdate") or "")[:4], r.get("source",""), au, r.get("title","")[:150], doi))
    print()
