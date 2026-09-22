import json, sys, time, urllib.parse, urllib.request

BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

# free-text (relevance-sorted) probes: (label, term, retmax)
PROBES = [
 ("ChIP-Atlas", 'ChIP-Atlas[Title]', 10),
 ("GRAND db", 'GRAND[Title] AND ("gene regulatory"[Title] OR database[Title])', 10),
 ("KnockTF", 'KnockTF[Title]', 10),
 ("IPF Cell Atlas", '"IPF Cell Atlas"[tiab]', 10),
 ("LungMAP CellRef", 'CellRef[Title] OR ("single cell reference"[Title] AND lung[Title])', 10),
 ("human fetal lung atlas TF", '(fetal[Title] OR embryonic[Title]) AND lung[Title] AND (atlas[Title] OR "cell atlas"[Title])', 15),
 ("lung TF target resource", '(lung[Title] OR pulmonary[Title] OR airway[Title] OR respiratory[Title]) AND ("transcription factor"[Title] OR "transcription factors"[Title] OR transcriptional[Title]) AND (database[Title] OR atlas[Title] OR resource[Title] OR network[Title] OR networks[Title] OR regulome[Title] OR landscape[Title])', 60),
 ("lung disease gene database", '(lung[Title] OR pulmonary[Title] OR respiratory[Title] OR asthma[Title] OR COPD[Title]) AND (database[Title] OR knowledgebase[Title] OR "knowledge base"[Title] OR portal[Title] OR catalog[Title] OR catalogue[Title]) AND (gene[Title] OR genes[Title] OR genomic[Title] OR transcriptom*[Title])', 60),
 ("master regulator lung disease", '("master regulator"[tiab] OR "master regulators"[tiab]) AND (lung[tiab] OR pulmonary[tiab] OR airway[tiab]) AND (fibrosis[tiab] OR COPD[tiab] OR asthma[tiab] OR cancer[tiab] OR hypertension[tiab])', 40),
 ("SCENIC regulon lung disease", '(SCENIC[tiab] OR regulon[tiab] OR regulons[tiab]) AND (lung[tiab] OR pulmonary[tiab]) AND (fibrosis[tiab] OR IPF[tiab] OR COPD[tiab] OR asthma[tiab] OR hypertension[tiab])', 40),
 ("network medicine COPD", '(network[Title]) AND (COPD[Title] OR "chronic obstructive"[Title] OR emphysema[Title] OR asthma[Title])', 40),
 ("lung single cell multiome regulatory", '(lung[tiab] OR pulmonary[tiab] OR airway[tiab]) AND (multiome[tiab] OR "single-cell ATAC"[tiab] OR scATAC[tiab] OR "chromatin accessibility"[tiab]) AND (regulatory[tiab] OR "transcription factor"[tiab])', 40),
]

def esearch(term, retmax, sort="relevance"):
    url = BASE + "esearch.fcgi?db=pubmed&retmode=json&sort=%s&retmax=%d&term=%s&datetype=pdat&mindate=2015/01/01&maxdate=2026/12/31" % (
        sort, retmax, urllib.parse.quote(term))
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
    print("### %s  (total hits=%s, showing %d)" % (label, c, len(ids)))
    for p in ids:
        r = res.get(p)
        if not r: continue
        print("    PMID %s | %s | %-38s | %s | %s" % (
            p, (r.get("pubdate") or "")[:4], r.get("source","")[:38],
            r.get("sortfirstauthor","")[:18], r.get("title","")[:135]))
    print()
