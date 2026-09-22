import json, sys, time, urllib.parse, urllib.request, os

BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
DATE = "&datetype=pdat&mindate=2015/01/01&maxdate=2026/12/31"

QUERIES = {
 "Q1_lung_GRN_disease": '("gene regulatory network"[tiab] OR "regulatory network"[tiab] OR "transcriptional network"[tiab]) AND (lung[tiab] OR pulmonary[tiab] OR airway[tiab] OR alveolar[tiab]) AND (fibrosis[tiab] OR IPF[tiab] OR COPD[tiab] OR emphysema[tiab] OR asthma[tiab] OR "lung cancer"[tiab] OR adenocarcinoma[tiab] OR "cystic fibrosis"[tiab] OR "pulmonary hypertension"[tiab] OR BPD[tiab])',
 "Q2_scenic_lung": '(SCENIC[tiab] OR regulon[tiab] OR regulons[tiab]) AND (lung[tiab] OR pulmonary[tiab] OR airway[tiab])',
 "Q3_tf_target_database": '(("transcription factor"[tiab] AND (target[tiab] OR targets[tiab])) AND (database[tiab] OR atlas[tiab] OR resource[tiab] OR compendium[tiab] OR repository[tiab]))',
 "Q4_lung_atlas": '(LungMAP[tiab] OR "Human Lung Cell Atlas"[tiab] OR "IPF Cell Atlas"[tiab] OR "lung cell atlas"[tiab])',
 "Q5_lung_chipseq_tf": '(ChIP-seq[tiab] OR CUT&RUN[tiab] OR ATAC-seq[tiab]) AND (lung[tiab] OR pulmonary[tiab] OR airway[tiab] OR alveolar[tiab]) AND ("transcription factor"[tiab] OR "transcription factors"[tiab])',
 "Q6_gwas_lung_regulatory": '(GWAS[tiab] OR "genome-wide association"[tiab]) AND (lung[tiab] OR pulmonary[tiab] OR asthma[tiab] OR COPD[tiab]) AND (regulatory[tiab] OR enhancer[tiab] OR "transcription factor"[tiab] OR eQTL[tiab])',
 "Q7_disease_gene_resource": '(DisGeNET[tiab] OR "Open Targets"[tiab] OR "Comparative Toxicogenomics Database"[tiab] OR TRRUST[tiab] OR hTFtarget[tiab] OR ChEA3[tiab] OR DoRothEA[tiab] OR RegNetwork[tiab] OR GTRD[tiab] OR TFLink[tiab] OR KnockTF[tiab] OR "Cistrome"[tiab] OR TFregulomeR[tiab] OR "TF2Network"[tiab] OR HumanBase[tiab] OR GRAND[tiab])',
 "Q8_ipf_tf": '(("idiopathic pulmonary fibrosis"[tiab] OR IPF[tiab]) AND ("transcription factor"[tiab] OR "transcription factors"[tiab] OR "transcriptional regulator"[tiab]))',
 "Q9_copd_asthma_tf": '((COPD[tiab] OR asthma[tiab] OR "chronic obstructive"[tiab]) AND ("transcription factor"[tiab] OR "transcription factors"[tiab]) AND (network[tiab] OR targets[tiab] OR regulome[tiab] OR integrative[tiab]))',
 "Q10_lung_cancer_tf_network": '("lung cancer"[tiab] OR "lung adenocarcinoma"[tiab] OR NSCLC[tiab]) AND ("transcription factor"[tiab] OR "master regulator"[tiab]) AND (network[tiab] OR regulon[tiab] OR "target genes"[tiab] OR pan-cancer[tiab])',
 "Q11_lung_dev_tf": '(lung[tiab] AND development[tiab] AND ("transcription factor"[tiab] OR "transcriptional"[tiab]) AND (network[tiab] OR atlas[tiab] OR "single-cell"[tiab]))',
 "Q12_pah_bpd_tf": '(("pulmonary hypertension"[tiab] OR "bronchopulmonary dysplasia"[tiab] OR "cystic fibrosis"[tiab]) AND ("transcription factor"[tiab] OR "gene regulatory"[tiab]))',
}

def esearch(term, retmax=200):
    url = BASE + "esearch.fcgi?db=pubmed&retmode=json&retmax=%d&term=%s%s" % (
        retmax, urllib.parse.quote(term), DATE)
    with urllib.request.urlopen(url) as f:
        d = json.load(f)
    return d["esearchresult"]["count"], d["esearchresult"]["idlist"]

def esummary(pmids):
    out = {}
    for i in range(0, len(pmids), 150):
        chunk = pmids[i:i+150]
        url = BASE + "esummary.fcgi?db=pubmed&retmode=json&id=" + ",".join(chunk)
        with urllib.request.urlopen(url) as f:
            d = json.load(f)
        for p in chunk:
            r = d.get("result", {}).get(p)
            if r:
                out[p] = r
        time.sleep(0.4)
    return out

all_ids = {}
counts = {}
for k, q in QUERIES.items():
    c, ids = esearch(q)
    counts[k] = c
    for p in ids:
        all_ids.setdefault(p, []).append(k)
    print("%-28s hits=%-7s retrieved=%d" % (k, c, len(ids)), file=sys.stderr)
    time.sleep(0.4)

print("TOTAL unique PMIDs: %d" % len(all_ids), file=sys.stderr)
summ = esummary(list(all_ids))

rows = []
for p, qs in all_ids.items():
    r = summ.get(p)
    if not r:
        continue
    rows.append({
        "pmid": p,
        "year": (r.get("pubdate") or "")[:4],
        "journal": r.get("source", ""),
        "title": r.get("title", "").replace("\t", " "),
        "type": ";".join(r.get("pubtype", [])),
        "queries": ";".join(qs),
    })
rows.sort(key=lambda x: (-len(x["queries"].split(";")), x["year"]))

outdir = "/private/tmp/claude-503/-Users-saljh8/86ec3749-a2e6-4d98-b638-3d92bedbda91/scratchpad"
with open(os.path.join(outdir, "pubmed_candidates.tsv"), "w") as f:
    f.write("pmid\tyear\tjournal\ttype\tqueries\ttitle\n")
    for r in rows:
        f.write("%(pmid)s\t%(year)s\t%(journal)s\t%(type)s\t%(queries)s\t%(title)s\n" % r)
print("wrote %d rows" % len(rows), file=sys.stderr)
