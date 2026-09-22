import json, time, urllib.parse, urllib.request

BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

PROBES = [
 # cell-type-labelled TF-DNA catalogs
 ("UniBind", 'UniBind[Title]'),
 ("ReMap atlas", 'ReMap[Title] AND (atlas[Title] OR regulatory[Title])'),
 ("Vierstra footprints", '"transcription factor footprints"[Title] OR ("global reference"[Title] AND footprint*[Title])'),
 ("Meuleman DHS index", '("DNase I hypersensitive"[Title] AND (index[Title] OR spectrum[Title]))'),
 ("EpiMap Boix", '(Boix CA[Author] OR "regulatory genomic circuitry"[Title])'),
 ("Roadmap epigenomes", '"Integrative analysis of 111 reference human epigenomes"[Title]'),
 ("ENCODE TF binding perspectives", '(ENCODE[Title] AND (perspectives[Title] OR portal[Title] OR "data portal"[Title] OR encyclopedia[Title]))'),
 ("Funk ENCODE DHS TFBS atlas", '("Atlas of Transcription Factor Binding Sites"[Title])'),
 ("ChIPSummitDB", 'ChIPSummitDB[Title]'),
 # lung in-vivo TF ChIP
 ("Little NKX2-1 lung", 'Little DR[Author] AND (NKX2-1[Title] OR alveolar[Title] OR lung[Title])'),
 ("Borromeo ASCL1 NEUROD1", 'Borromeo MD[Author]'),
 ("Denny NFIB SCLC", 'Denny SK[Author]'),
 ("Camolotto FOXA lung", 'Camolotto SA[Author]'),
 ("Gerber GR airway cistrome", '(Sasse SK[Author] OR Gerber AN[Author]) AND (ChIP[Title] OR cistrome[Title] OR glucocorticoid[Title] OR enhancer[Title])'),
 ("Harris CFTR regulation", '(Harris A[Author] OR Paranjapye A[Author] OR Mutolo MJ[Author]) AND (CFTR[Title] OR airway[Title] OR FOXA1[Title])'),
 ("Hokari TTF1 binding", 'Hokari S[Author] AND (TTF-1[Title] OR binding[Title])'),
 ("Lung TF ChIP in vivo", '(lung[Title] OR alveolar[Title] OR airway[Title]) AND ("ChIP-seq"[Title] OR "CUT&RUN"[Title] OR "binding sites"[Title] OR cistrome[Title] OR "binding"[Title]) AND ("in vivo"[tiab] OR primary[tiab] OR tissue[tiab])'),
 # perturbation with molecular readout
 ("Perturb-map lung", '"Perturb-map"[tiab] OR ("spatial CRISPR"[Title])'),
 ("Ursu Perturb-seq variants", 'Ursu O[Author] AND (Perturb-seq[Title] OR variants[Title])'),
 ("Replogle genome-scale Perturb-seq", 'Replogle JM[Author]'),
 ("Joung TF atlas", 'Joung J[Author] AND (transcription factor[Title] OR atlas[Title])'),
 ("Perturb-seq lung any", 'Perturb-seq[Title] OR "Perturb-seq"[tiab]'),
 ("CRISPRi enhancer lung", 'CRISPRi[Title] AND (lung[tiab] OR airway[tiab] OR NKX2-1[tiab] OR enhancer[Title] OR "non-coding"[Title])'),
 # protein-protein reference maps
 ("HuRI", '("human reference interactome"[tiab] OR "reference map of the human binary protein interactome"[Title] OR HuRI[tiab])'),
 ("BioPlex", 'BioPlex[Title] OR ("interaction network"[Title] AND "human cells"[Title])'),
 ("OpenCell", 'OpenCell[Title] OR ("proteome-scale"[Title] AND (localization[Title] OR interaction[Title]))'),
 ("huMAP", '("hu.MAP"[tiab] OR "human protein complex map"[Title])'),
 ("CORUM", 'CORUM[Title]'),
 ("IntAct BioGRID", '(IntAct[Title] OR BioGRID[Title] OR STRING[Title]) AND (database[Title] OR update[Title] OR resource[Title] OR 20[Title])'),
 ("lung AP-MS BioID", '(lung[tiab] OR airway[tiab] OR alveolar[tiab] OR NSCLC[tiab]) AND (BioID[Title] OR "proximity labeling"[Title] OR AP-MS[Title] OR "interactome"[Title] OR "interaction partners"[Title] OR "protein complex"[Title])'),
 ("lung proteome atlas", '(lung[Title] OR pulmonary[Title] OR airway[Title]) AND (proteom*[Title]) AND (atlas[Title] OR map[Title] OR landscape[Title] OR "cell type"[Title] OR compendium[Title])'),
 # enhancer-gene contact in lung
 ("lung HiChIP 3D", '(lung[tiab] OR airway[tiab] OR alveolar[tiab] OR NSCLC[tiab]) AND (HiChIP[Title] OR "promoter capture"[Title] OR "chromatin interaction"[Title] OR "3D genome"[Title] OR "enhancer-promoter"[Title])'),
 ("ABC model", '"activity-by-contact"[tiab] OR ("enhancer-gene"[Title] AND (map[Title] OR predictions[Title]))'),
]

def run(term, retmax=10):
    u = BASE + "esearch.fcgi?db=pubmed&retmode=json&sort=relevance&retmax=%d&term=%s&datetype=pdat&mindate=2015/01/01&maxdate=2026/12/31" % (retmax, urllib.parse.quote(term))
    ids = json.load(urllib.request.urlopen(u))["esearchresult"].get("idlist", [])
    time.sleep(0.35)
    if not ids: return []
    r = json.load(urllib.request.urlopen(BASE + "esummary.fcgi?db=pubmed&retmode=json&id=" + ",".join(ids)))["result"]
    time.sleep(0.35)
    return [(p, r.get(p, {})) for p in ids]

for lab, t in PROBES:
    print("### %s" % lab)
    res = run(t)
    if not res: print("    NO MATCH")
    for p, d in res:
        print("    PMID %s | %s | %-28s | %-15s | %s" % (p, (d.get("pubdate") or "")[:4],
              d.get("source","")[:28], d.get("sortfirstauthor","")[:15], d.get("title","")[:125]))
    print()
