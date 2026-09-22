import json, time, urllib.parse, urllib.request

BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
PROBES = [
 ("ToppCell", 'ToppCell[tiab] OR ToppGene[tiab] OR ToppCluster[tiab]', 10),
 ("LungMAP CellRef", '(CellRef[tiab]) AND (lung[tiab])', 10),
 ("Zepp alveolus", 'Zepp JA[Author] AND (alveolus[Title] OR alveolar[Title] OR lung[Title])', 15),
 ("mouse lung development atlas", '("single-cell"[Title] OR "single cell"[Title]) AND lung[Title] AND development[Title] AND (atlas[Title] OR trajectory[Title] OR landscape[Title])', 20),
 ("TF-Marker db", '"TF-Marker"[tiab] OR ("transcription factors"[Title] AND "markers"[Title] AND database[Title])', 10),
 ("Neumark IPF atlas", 'Neumark N[Author]', 15),
 ("PAH multiomics lung", '("pulmonary arterial hypertension"[Title] OR "pulmonary hypertension"[Title]) AND (multiomic*[Title] OR multi-omic*[Title] OR transcriptional[Title] OR regulatory[Title] OR network*[Title])', 25),
 ("GTEx tissue eQTL", '(GTEx[Title] OR "human tissues"[Title]) AND (eQTL[Title] OR "gene expression"[Title] OR "genetic effects"[Title])', 15),
 ("asthma GWAS gene", 'asthma[Title] AND ("genome-wide association"[Title] OR GWAS[Title]) AND (gene*[Title] OR loci[Title] OR functional[Title])', 20),
 ("IPF GRN systems", '("idiopathic pulmonary fibrosis"[Title] OR "pulmonary fibrosis"[Title]) AND ("gene regulatory network"[Title] OR "regulatory network"[Title] OR "transcriptional network"[Title] OR "master regulator*"[Title] OR regulon*[Title])', 25),
 ("lung enhancer atlas disease", '(lung[tiab] OR airway[tiab] OR alveolar[tiab]) AND (enhancer[Title] OR "cis-regulatory"[Title] OR "regulatory elements"[Title]) AND (atlas[Title] OR map[Title] OR landscape[Title] OR catalog*[Title])', 25),
 ("scREAD-like disease TF portal", '("single-cell"[Title]) AND (portal[Title] OR database[Title] OR resource[Title]) AND (lung[Title] OR pulmonary[Title] OR respiratory[Title])', 25),
]

def esearch(term, retmax):
    url = BASE + "esearch.fcgi?db=pubmed&retmode=json&sort=relevance&retmax=%d&term=%s&datetype=pdat&mindate=2015/01/01&maxdate=2026/12/31" % (retmax, urllib.parse.quote(term))
    with urllib.request.urlopen(url) as f:
        d = json.load(f)["esearchresult"]
    return d.get("count"), d.get("idlist", [])

def esummary(pmids):
    if not pmids: return {}
    url = BASE + "esummary.fcgi?db=pubmed&retmode=json&id=" + ",".join(pmids)
    with urllib.request.urlopen(url) as f:
        return json.load(f).get("result", {})

for label, term, rm in PROBES:
    c, ids = esearch(term, rm)
    time.sleep(0.35)
    res = esummary(ids)
    time.sleep(0.35)
    print("### %s (hits=%s)" % (label, c))
    for p in ids:
        r = res.get(p)
        if not r: continue
        print("    PMID %s | %s | %-34s | %-16s | %s" % (p, (r.get("pubdate") or "")[:4],
              r.get("source","")[:34], r.get("sortfirstauthor","")[:16], r.get("title","")[:130]))
    print()
