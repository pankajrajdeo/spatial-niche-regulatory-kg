import json, sys, time, urllib.parse, urllib.request, os

BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
DATE = "&datetype=pdat&mindate=2015/01/01&maxdate=2026/12/31"
OUT = "/private/tmp/claude-503/-Users-saljh8/86ec3749-a2e6-4d98-b638-3d92bedbda91/scratchpad"

LUNG = '(lung[tiab] OR pulmonary[tiab] OR airway[tiab] OR alveolar[tiab] OR bronchial[tiab] OR tracheal[tiab] OR respiratory epithelium[tiab] OR AT2[tiab] OR "type II cell"[tiab] OR NSCLC[tiab] OR "lung adenocarcinoma"[tiab] OR "small cell lung"[tiab])'
CHIP = '("ChIP-seq"[tiab] OR "ChIP-Seq"[tiab] OR "chromatin immunoprecipitation"[tiab] OR "CUT&RUN"[tiab] OR "CUT and RUN"[tiab] OR "CUT&Tag"[tiab] OR "CUT and Tag"[tiab] OR ChIP-exo[tiab] OR DAP-seq[tiab])'

Q = {
 # --- protein-DNA in lung
 "P1_lung_chip_tf": '%s AND %s AND ("transcription factor"[tiab] OR "transcription factors"[tiab] OR binding[tiab] OR cistrome[tiab] OR "target genes"[tiab])' % (LUNG, CHIP),
 "P2_lung_chip_disease": '%s AND %s AND (fibrosis[tiab] OR IPF[tiab] OR COPD[tiab] OR emphysema[tiab] OR asthma[tiab] OR "cystic fibrosis"[tiab] OR "pulmonary hypertension"[tiab] OR dysplasia[tiab] OR injury[tiab])' % (LUNG, CHIP),
 "P3_lung_tf_names": '%s AND (NKX2-1[tiab] OR "TTF-1"[tiab] OR FOXA2[tiab] OR FOXA1[tiab] OR SOX2[tiab] OR SOX9[tiab] OR TP63[tiab] OR GRHL2[tiab] OR CEBPA[tiab] OR GATA6[tiab] OR ELF5[tiab] OR SPDEF[tiab] OR FOXJ1[tiab] OR ASCL1[tiab] OR NEUROD1[tiab] OR POU2F3[tiab] OR NFIB[tiab] OR KLF5[tiab] OR TEAD1[tiab] OR "glucocorticoid receptor"[tiab] OR NFE2L2[tiab] OR NRF2[tiab] OR STAT6[tiab] OR SMAD3[tiab] OR MYB[tiab])' % CHIP,
 "P4_encode_cellline": '%s AND (A549[tiab] OR IMR-90[tiab] OR IMR90[tiab] OR BEAS-2B[tiab] OR NCI-H[tiab] OR "16HBE"[tiab] OR HBEC[tiab] OR "air-liquid interface"[tiab] OR organoid[tiab])' % CHIP,
 "P5_lung_atac_footprint": '%s AND (ATAC-seq[tiab] OR "chromatin accessibility"[tiab]) AND (footprint*[tiab] OR "transcription factor"[tiab] OR motif[tiab]) AND (fibrosis[tiab] OR COPD[tiab] OR asthma[tiab] OR cancer[tiab] OR development[tiab] OR disease[tiab])' % LUNG,
 # --- enhancer-to-gene contacts
 "P6_lung_3d": '%s AND (HiChIP[tiab] OR "Capture Hi-C"[tiab] OR "promoter capture"[tiab] OR PLAC-seq[tiab] OR "Hi-C"[tiab] OR "chromatin interaction"[tiab] OR "activity-by-contact"[tiab] OR "enhancer-promoter"[tiab])' % LUNG,
 # --- perturbation with molecular readout
 "P7_perturbseq": '(Perturb-seq[tiab] OR "Perturb seq"[tiab] OR CROP-seq[tiab] OR CRISPRi[tiab] OR "Perturb-map"[tiab] OR "single-cell CRISPR"[tiab] OR "CRISPR screen"[tiab]) AND %s' % LUNG,
 "P8_tf_perturb_rna": '%s AND (knockdown[tiab] OR knockout[tiab] OR overexpression[tiab] OR degron[tiab] OR "dTAG"[tiab]) AND ("transcription factor"[tiab] OR "transcription factors"[tiab]) AND (RNA-seq[tiab] OR transcriptom*[tiab]) AND ("target genes"[tiab] OR "direct targets"[tiab] OR cistrome[tiab] OR "regulatory network"[tiab])' % LUNG,
 # --- protein-protein
 "P9_lung_ppi": '%s AND ("affinity purification"[tiab] OR AP-MS[tiab] OR "immunoprecipitation mass spectrometry"[tiab] OR BioID[tiab] OR "proximity labeling"[tiab] OR APEX2[tiab] OR TurboID[tiab] OR interactome[tiab] OR "protein-protein interaction"[tiab] OR "protein complex"[tiab]) AND (proteom*[tiab] OR "mass spectrometry"[tiab])' % LUNG,
 "P10_global_ppi": '("protein-protein interaction"[tiab] OR interactome[tiab]) AND (reference[tiab] OR "human interactome"[tiab] OR proteome-scale[tiab] OR "genome-scale"[tiab] OR atlas[tiab] OR map[Title]) AND ("mass spectrometry"[tiab] OR "yeast two-hybrid"[tiab] OR Y2H[tiab] OR AP-MS[tiab] OR BioID[tiab])',
 # --- integrated cell-type-labelled TF-DNA catalogs
 "P11_catalogs": '(UniBind[tiab] OR ReMap[tiab] OR "ChIP-Atlas"[tiab] OR Cistrome[tiab] OR GTRD[tiab] OR "ENCODE"[Title] OR "TF binding"[Title]) AND (catalog*[tiab] OR atlas[tiab] OR database[tiab] OR resource[tiab] OR compendium[tiab] OR "high-confidence"[tiab])',
 # --- lung development in vivo TF binding (mouse)
 "P12_mouse_lung_chip": '(mouse[tiab] OR murine[tiab] OR mice[tiab]) AND %s AND %s AND (development[tiab] OR epithelium[tiab] OR alveolar[tiab] OR regeneration[tiab] OR progenitor[tiab])' % (LUNG, CHIP),
 # --- immune / structural lung cell types
 "P13_lung_immune_chip": '%s AND (macrophage[tiab] OR "alveolar macrophage"[tiab] OR "T cell"[tiab] OR fibroblast[tiab] OR myofibroblast[tiab] OR endothel*[tiab] OR "smooth muscle"[tiab]) AND (lung[tiab] OR pulmonary[tiab] OR airway[tiab])' % CHIP,
 # --- GWAS variant to TF binding, lung
 "P14_variant_tf_binding": '%s AND (MPRA[tiab] OR "massively parallel reporter"[tiab] OR "allele-specific binding"[tiab] OR "SNP-SELEX"[tiab] OR "reporter assay"[tiab]) AND (variant*[tiab] OR SNP*[tiab] OR regulatory[tiab])' % LUNG,
 # --- degron / rapid depletion direct targets
 "P15_direct_targets": '("direct target"[tiab] OR "direct targets"[tiab] OR "primary targets"[tiab]) AND %s AND ("transcription factor"[tiab] OR ChIP[tiab])' % LUNG,
}

def esearch(term, retmax=200, sort=None):
    u = BASE + "esearch.fcgi?db=pubmed&retmode=json&retmax=%d&term=%s%s" % (retmax, urllib.parse.quote(term), DATE)
    if sort: u += "&sort=" + sort
    d = json.load(urllib.request.urlopen(u))["esearchresult"]
    return d.get("count"), d.get("idlist", [])

def esummary(pmids):
    out = {}
    for i in range(0, len(pmids), 120):
        u = BASE + "esummary.fcgi?db=pubmed&retmode=json&id=" + ",".join(pmids[i:i+120])
        out.update(json.load(urllib.request.urlopen(u)).get("result", {}))
        time.sleep(0.4)
    return out

allids = {}
for k, q in Q.items():
    for srt in ("relevance", None):          # both orders: relevance + most-recent
        c, ids = esearch(q, 200, srt)
        for p in ids:
            allids.setdefault(p, set()).add(k)
        time.sleep(0.4)
    print("%-24s total_hits=%-7s" % (k, c), file=sys.stderr)

print("unique PMIDs: %d" % len(allids), file=sys.stderr)
S = esummary(list(allids))

rows = []
for p, qs in allids.items():
    r = S.get(p)
    if not r: continue
    rows.append((p, (r.get("pubdate") or "")[:4], r.get("source",""), r.get("sortfirstauthor",""),
                 r.get("title","").replace("\t"," "), ";".join(sorted(qs)), ";".join(r.get("pubtype",[]))))
rows.sort(key=lambda x: (-len(x[5].split(";")), x[1]))
with open(os.path.join(OUT, "edge_candidates.tsv"), "w") as f:
    f.write("pmid\tyear\tjournal\tauthor\ttitle\tqueries\tpubtype\n")
    for r in rows:
        f.write("\t".join(r) + "\n")
print("wrote %d rows" % len(rows), file=sys.stderr)
