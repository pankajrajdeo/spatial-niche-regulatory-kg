import json, time, urllib.parse, urllib.request, csv, os

BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
OUT = "/Users/saljh8/Dropbox/LungMAP/TF_target_disease_literature"

# (pmid, tier, lung_disease_scope, tf_target_evidence, why_listed)
ROWS = [
 # TIER A - lung disease gene resources that carry TF / regulatory content
 ("36413377","A","lung development + lung disease, human/rhesus/mouse","cell-type TF markers, no explicit TF-target edge set","LungMAP gateway portal; harmonized bulk and single-cell multiomics across age, disease and drug treatment"),
 ("33385216","A","lung development and disease","TF expression by cell type","LGEA web portal v3 Lung-at-a-Glance"),
 ("28798251","A","lung development","TF expression by cell type","LungMAP consortium description and data model"),
 ("34936882","A","normal lung cell types with disease links per cell card","TF markers per cell type","CellCards give an explicit disease-link field per lung cell type"),
 ("37516747","A","48 human and 40 mouse lung cell types","cell-type marker TFs","LungMAP CellRef built from 104 human and 17 mouse lungs"),
 ("37291214","A","health plus IPF, COPD, lung cancer and more","cell-type marker genes incl. TFs","HLCA integrates 49 datasets, 2.4 million cells, 486 individuals"),
 ("33208946","A","normal human lung","TFs reported per cell type","58 cell populations from ~75,000 cells"),
 ("32996785","A","IPF, COPD, control","expression only","IPF Cell Atlas web resource"),
 ("32832599","A","IPF, COPD, control","expression only","312,928 cells from 32 IPF, 28 control, 18 COPD lungs"),
 ("32832598","A","pulmonary fibrosis","expression only","114,396 cells, 10 control and 20 PF lungs, 31 cell states"),
 ("35078977","A","COPD","transcriptomic network analysis","COPD alveolar niche, human and mouse smoke-exposure validation"),
 ("31209336","A","asthma","expression only","asthmatic and healthy airway census"),
 ("32726565","A","healthy airways, 35 locations","expression only","77,969 cells, nose to 12th airway division"),
 ("34030460","A","pulmonary hypertension vs control","expression plus signaling networks","integrated human lung endothelial atlas from 6 datasets"),
 ("31949184","A","COPD and IPF","none directly","PulmonDB curated and harmonized lung-disease transcriptome database"),
 # TIER B - lung disease papers that build explicit TF-to-target regulatory models
 ("31600171","B","IPF, staged by microCT alveolar surface density","TF and miRNA regulators per expression track","IPFReg systems model; predicted POU2AF1 and validated it in knockout mice"),
 ("34922464","B","links AEC differentiation to COPD, IPF, LUAD","TF binding in enhancers, TF co-regulatory networks","methylome plus chromatin domains plus RNA in human AEC2-to-AEC1 differentiation"),
 ("33164753","B","respiratory traits, COVID-19 risk locus 3p21.31","cCRE-to-target-gene links in lung cell types","90,980 snATAC and 46,500 snRNA nuclei across 3 ages"),
 ("33707239","B","alveolar formation, BPD relevance","single-cell chromatin accessibility plus pathway expression","AT1 signaling hub controlling myofibroblast and alveolus formation"),
 ("34927678","B","mouse lung development, 9 timepoints","cell-state regulators","102,571 cells, E12 to P14, searchable atlas"),
 ("39461973","B","COPD exacerbation, obstruction severity, infection","validated TF regulons and miRNA regulons as network layers","multi-network gene community detection in AERIS blood samples"),
 ("36661515","B","lung cancer subtypes plus PAH overlap","TF-target regulatory network, ChEA3 validated","26 recurrently dysregulated TFs across lung cancer datasets"),
 ("29236308","B","lung cancer","TF-TF and TF-target gene interactions, manually curated","DBTFLC holds 349 lung-cancer TFs with their target interactions"),
 ("39167456","B","pulmonary arterial hypertension","Bayesian regulatory networks","96 PAH and 52 control lungs, largest PAH lung biobank to date"),
 ("42261399","B","COPD","TF regulatory networks per fibroblast subpopulation","6 control and 10 COPD lungs, fibroblast inflammatory reprogramming"),
 ("38249888","B","lung adenocarcinoma","TF-target gene regulatory network","TF-target network analysis in human LUAD"),
 # TIER C - genome-wide TF-to-target compendia used to build lung TF-target maps
 ("29087512","C","not lung-specific","8,444 human TF-target interactions for 800 TFs; 6,552 mouse for 828 TFs","TRRUST v2, sentence-based text mining plus manual curation"),
 ("32858223","C","tissue-labelled, includes lung samples","7,190 ChIP-seq samples of 659 TFs; binding sites for 699 TFs","hTFtarget, TF-target regulation by dataset and tissue"),
 ("31114921","C","not lung-specific","integrated ChIP-seq, co-expression and co-occurrence TF-target libraries","ChEA3 ranks upstream TFs for a submitted gene set"),
 ("31340985","C","not lung-specific","benchmark of curated, ChIP-seq, motif and reverse-engineered regulons","DoRothEA regulon confidence levels A to E"),
 ("37843125","C","not lung-specific","signed TF-gene interactions for 1,186 TFs","CollecTRI meta-resource, outperformed other collections on perturbation data"),
 ("26424082","C","not lung-specific","TF, miRNA and target interactions from 25 databases plus TFBS motifs","RegNetwork human and mouse"),
 ("33231677","C","not lung-specific","ChIP-seq TFBS across 9 species, uniform processing, HOCOMOCO motifs","GTRD 2021 integrated view of transcription regulation"),
 ("36124642","C","not lung-specific","~12 million TF-target interactions and ~9 million binding sites, 7 species","TFLink, integrates 10 resources"),
 ("37956336","C","tissue and cell-type annotated","1,468 datasets, 612 TFs and 172 co-factors, knockdown/knockout","KnockTF 2.0 gives perturbation-based, not binding-based, TF targets"),
 ("38749504","C","not lung-specific","376,000+ ChIP-seq, ATAC-seq, DNase-seq and bisulfite-seq experiments","ChIP-Atlas 3.0 adds GWAS SNP and ClinVar annotation tracks"),
 ("30462313","C","tissue-labelled samples","~47,000 human and mouse ChIP-seq, DNase-seq and ATAC-seq samples","Cistrome DB Toolkit queries which factors regulate a given gene"),
 ("34986601","C","cell- and tissue-type specific, includes lung","5,905 curated entries, 1,316 TFs, 1,092 TF-regulated markers","TF-Marker links TFs to markers by cell and tissue type"),
 ("34508353","C","36 tissues and 28 cancers, includes lung","12,468 genome-scale TF-gene networks; 173,013 TF and gene targeting scores","GRAND compares regulatory networks between states and drugs"),
 ("29069589","C","38 GTEx tissues, includes lung","TF-to-target edges are more tissue-specific than nodes","tissue-specific regulatory networks from GTEx"),
 ("25915600","C","144 tissues and cell types, includes lung","functional interaction edges, not TF-target edges","GIANT plus NetWAS reweights GWAS genes by tissue network"),
 ("32728249","C","human and mouse tissues, includes lung","926,535 human and 339,815 mouse candidate cis-regulatory elements","ENCODE phase III registry of cCREs and TF occupancy"),
 # TIER D - gene-to-disease association platforms
 ("31680165","D","all human diseases incl. lung","no TF-target edges","DisGeNET covers 24,000+ diseases, 17,000 genes, 117,000 variants"),
 ("39657122","D","all human diseases incl. lung","no TF-target edges","Open Targets Platform target-disease associations with direction of effect"),
 ("39385618","D","chemical-gene-disease incl. lung disease","curated chemical-gene interactions, some TF-mediated","CTD update 2025"),
 ("36914875","D","lung function and COPD","variant-to-gene mapping, not TF-target","580,869 participants, 1,020 signals, 559 genes by >=2 criteria"),
]

def esummary(pmids):
    out = {}
    for i in range(0, len(pmids), 100):
        u = BASE + "esummary.fcgi?db=pubmed&retmode=json&id=" + ",".join(pmids[i:i+100])
        out.update(json.load(urllib.request.urlopen(u)).get("result", {}))
        time.sleep(0.4)
    return out

pmids = [r[0] for r in ROWS]
assert len(set(pmids)) == len(pmids), "duplicate PMID in list"
S = esummary(pmids)

os.makedirs(OUT, exist_ok=True)
missing = [p for p in pmids if p not in S]
if missing:
    raise SystemExit("PubMed returned no record for: %s" % missing)

path = os.path.join(OUT, "lung_TF_target_disease_papers.csv")
with open(path, "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["tier","pmid","year","journal","first_author","title","doi",
                "lung_disease_scope","tf_target_evidence","why_listed","pubmed_url"])
    for pm, tier, scope, ev, why in ROWS:
        r = S[pm]
        doi = ""
        for aid in r.get("articleids", []):
            if aid.get("idtype") == "doi":
                doi = aid.get("value", "")
        w.writerow([tier, pm, (r.get("pubdate") or "")[:4], r.get("source",""),
                    r.get("sortfirstauthor",""), r.get("title","").rstrip("."), doi,
                    scope, ev, why, "https://pubmed.ncbi.nlm.nih.gov/%s/" % pm])

print("wrote %s with %d rows" % (path, len(ROWS)))
years = sorted((S[p].get("pubdate") or "")[:4] for p in pmids)
print("year range: %s to %s" % (years[0], years[-1]))
pre2015 = [p for p in pmids if int((S[p].get("pubdate") or "0")[:4]) < 2015]
print("published before 2015: %s" % (pre2015 or "none"))
