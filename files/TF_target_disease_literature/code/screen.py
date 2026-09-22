import re, csv, sys
P = "/private/tmp/claude-503/-Users-saljh8/86ec3749-a2e6-4d98-b638-3d92bedbda91/scratchpad/edge_candidates.tsv"

SCALE = ["genome-wide","genome wide","atlas","catalog","catalogue","compendium","landscape","map of",
         "integrative","integrated","comprehensive","resource","database","large-scale","multi-omic",
         "multiomic","screen","screens","systematic","encyclopedia","encyclopaedia","high-throughput"]
EDGE  = ["chip-seq","chip seq","cut&run","cut and run","cut&tag","cut and tag","chip-exo","cistrome",
         "binding","occupancy","interactome","protein-protein","ap-ms","bioid","proximity labeling",
         "proximity labelling","mass spectrometry","hichip","hi-c","promoter capture","plac-seq",
         "enhancer","cis-regulatory","regulatory element","perturb-seq","perturb-map","crispri",
         "crop-seq","crispr screen","mpra","massively parallel reporter","allele-specific","footprint",
         "direct target","target genes","tf binding","transcription factor binding","super-enhancer",
         "regulatory circuitry","core regulatory"]
LUNG  = ["lung","pulmonary","airway","alveolar","bronchial","tracheal","nsclc","adenocarcinoma",
         "small cell","a549","imr-90","imr90","beas-2b","hbec","respiratory","copd","asthma","fibrosis",
         "emphysema","cystic fibrosis","at2","club cell","basal cell"]
NEG   = ["network pharmacology","molecular docking","bioinformatics analysis","prognostic","signature",
         "mendelian randomization","meta-analysis of","case report","systematic review","nomogram",
         "traditional chinese","decoction","herbal","circrna","cerna","mirna-mrna","lncrna-mirna",
         "immune infiltration","ferroptosis-related","cuproptosis","machine learning"]

rows = list(csv.DictReader(open(P), delimiter="\t"))
scored = []
for r in rows:
    t = (r["title"] or "").lower()
    s = 0
    s += 2 * sum(k in t for k in EDGE)
    s += 1 * sum(k in t for k in SCALE)
    s += 1 * sum(k in t for k in LUNG)
    s -= 4 * sum(k in t for k in NEG)
    s += len(r["queries"].split(";")) - 1
    if "preprint" in (r["pubtype"] or "").lower(): s -= 1
    scored.append((s, r))
scored.sort(key=lambda x: -x[0])
cut = int(sys.argv[1]) if len(sys.argv) > 1 else 5
n = 0
for s, r in scored:
    if s < cut: break
    n += 1
    print("%3d | %s | %s | %-26s | %-14s | %s" % (s, r["pmid"], r["year"], r["journal"][:26],
          r["author"][:14], r["title"][:120]))
print("\n%d of %d rows at score >= %d" % (n, len(rows), cut), file=sys.stderr)
