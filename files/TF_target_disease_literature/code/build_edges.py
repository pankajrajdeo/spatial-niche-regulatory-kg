import json, time, urllib.parse, urllib.request, csv, os

BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
OUT = "/Users/saljh8/Dropbox/LungMAP/TF_target_disease_literature"

# (pmid, tier, assay, cell_type_or_biosample, condition, edge_type, scale_or_note)
ROWS = [
# T1 - protein-DNA measured in lung / airway cells or tissue
("33947861","T1_lung_TF_binding","ChIP-seq (in vivo)","mouse AT1 vs AT2 alveolar cells","normal development","TF-DNA","NKX2-1 binds different sites in AT1 vs AT2; YAP/TAZ loss redirects binding - direct cell-type edge context"),
("31548395","T1_lung_TF_binding","ChIP-seq + genetics","mouse AT1 cells","normal development","TF-DNA","NKX2-1 control of AT1 development and maintenance"),
("33980985","T1_lung_TF_binding","CRISPRi of ChIP-seq peaks","human lung cell lines","normal / innate defense","TF-DNA validated","19 NKX2-1-bound regions tested in SFTPB, LAMP3, SFTPA genes"),
("32500120","T1_lung_TF_binding","CRISPRi of non-coding loci","lung cells","lung-disease GWAS loci","enhancer-gene validated","functional test of lung disease-associated non-coding regions"),
("31782890","T1_lung_TF_binding","ChIP-seq + RNA-seq","NCI-H209 (SCLC) vs NCI-H441 (LUAD)","cancer subtypes","TF-DNA","TTF-1/NKX2-1 binding regions differ by 75.0% between the two lines"),
("27452466","T1_lung_TF_binding","ChIP-seq","SCLC lines, mouse PNEC","neuroendocrine tumor","TF-DNA","ASCL1 and NEUROD1 bind distinct loci; ASCL1 targets MYCL1, RET, SOX2, NFIB; NEUROD1 targets MYC"),
("27374332","T1_lung_TF_binding","ATAC/chromatin + ChIP","SCLC mouse and human","metastasis","TF-DNA","NFIB drives widespread chromatin accessibility increase"),
("32473656","T1_lung_TF_binding","ChIP-seq + models","SCLC","subtype evolution","TF-DNA","MYC reprograms neuroendocrine fate across SCLC subtypes"),
("40963028","T1_lung_TF_binding","lineage tracing + single-cell","mouse SCLC, basal origin","neuroendocrine-tuft plasticity","TF-DNA context","ASCL1 vs POU2F3 lineage states from a basal cell of origin"),
("35848993","T1_lung_TF_binding","ChIP-seq","SCLC subtype","cancer","TF-DNA","NKX2-1 and SOX1 transcriptional circuitry defines an SCLC subtype"),
("31551362","T1_lung_TF_binding","epigenomic profiling","lung squamous carcinoma","cancer","TF-DNA","trans-lineage SOX2 partnerships drive tumor heterogeneity"),
("42160949","T1_lung_TF_binding","epigenomic profiling","neuroendocrine lung cancer","cancer","TF-DNA","ASCL1/NKX2-1 classical-NE subtype and a SOX-defined subtype"),
("35105868","T1_lung_TF_binding","ChIP-seq / enhancer maps","NSCLC","cancer","TF-DNA","dNp63 enhancer-associated gene landscape"),
("30475207","T1_lung_TF_binding","ChIP-seq + genetics","NKX2-1-negative lung cancer","cancer","TF-DNA","FoxA1/FoxA2 drive gastric differentiation, suppress squamous identity"),
("33821796","T1_lung_TF_binding","ChIP-seq + genetics","LUAD","cancer, targeted therapy","TF-DNA","NKX2-1/ERK/WNT feedback loop modulates gastric identity"),
("30332632","T1_lung_TF_binding","ChIP-seq + models","lung cancer","cancer, immune microenvironment","TF-DNA","SOX2 and NKX2-1 determine cell fate and shape the immune microenvironment"),
("37067057","T1_lung_TF_binding","ChIP-seq + models","invasive mucinous adenocarcinoma","cancer","TF-DNA","FOXA2 cooperates with mutant KRAS"),
("31884422","T1_lung_TF_binding","ChIP-seq","A549","cancer, oxidative stress","TF-DNA","genome-wide NRF2 binding sites in a lung line"),
("27076634","T1_lung_TF_binding","ChIP-seq","airway epithelial cells","inflammation, glucocorticoid","TF-DNA","glucocorticoid receptor and NF-kB cistromes cooperate"),
("28375666","T1_lung_TF_binding","ChIP-seq","airway smooth muscle","hypertrophy, glucocorticoid","TF-DNA","GR cistrome identifies PLCD1 as a KLF15 target"),
("40164603","T1_lung_TF_binding","eRNA transcription + reporter","airway cells","asthma","variant-TF-DNA","35 asthma-associated SNPs in eRNA regions; rs258760 disrupts an AHR response element"),
("29572268","T1_lung_TF_binding","ChIP + reporter","airway epithelial cells","CFTR regulation","TF-DNA","a TF network represses CFTR"),
("32432922","T1_lung_TF_binding","ChIP-seq","primary human airway epithelial cells","normal","TF-DNA","FOXA1 network coordinates airway epithelial function"),
("33731112","T1_lung_TF_binding","ChIP-seq + proteomics","developing mouse lung mesenchyme","development","TF-DNA and protein-protein","TBX2 DNA occupancy AND its interaction partners in one study"),
("39980707","T1_lung_TF_binding","ChIP-seq + RNA-seq","human pulmonary cells","pulmonary hypertension","TF-DNA","TBX4 target genes, unique and overlapping sets"),
("33320836","T1_lung_TF_binding","enhancer / epigenetic assays","lung epithelium","IPF (MUC5B rs35705950)","variant-enhancer-gene","lineage- and disease-dependent remodeling of the MUC5B enhancer"),
("36777184","T1_lung_TF_binding","H3K27ac ChIP-seq + MPRA + CRISPRi","primary human bronchial epithelial cells","asthma / IL-13","enhancer-gene validated","IL-13-responsive regulatory elements, functionally optimized"),
("42228021","T1_lung_TF_binding","ATAC + ChIP + genetics","alveolar macrophages","normal identity","TF-DNA","RXR and PPARg cooperative network set by DLL4, GM-CSF and TGFb signals"),
("34797692","T1_lung_TF_binding","epigenomic + genetics","alveolar macrophages","health and tissue injury","TF-DNA","EGR2 imprints alveolar macrophage identity"),
("39042472","T1_lung_TF_binding","epigenomic profiling","alveolar macrophages","antifungal immunity","TF-DNA","EGR2 as epigenomic regulator of phagocytosis"),
("35210623","T1_lung_TF_binding","epigenome profiling","alveolar macrophages","ex vivo expansion and transfer","chromatin state","epigenetic identity restored after in vivo transfer"),
("37142338","T1_lung_TF_binding","snATAC-seq + RNA-seq","IPF myofibroblasts","IPF","TF motif activity","3 IPF and 2 donor lungs snATAC, integrated with 10 IPF / 8 control scRNA; TWIST1"),
("33362848","T1_lung_TF_binding","H3K27ac ChIP-seq","airway epithelium","asthma","enhancer state","asthma influence on the airway epithelial epigenome"),
("34922464","T1_lung_TF_binding","methylome + chromatin domains + RNA","human alveolar epithelial cells","AEC2 to AEC1 differentiation","TF co-regulatory network","enhancer TF binding analysis; NKX2-1, FOXA, MEF2, TEAD, AP1"),
("37150829","T1_lung_TF_binding","chromatin + expression","bronchial premalignant lesions","premalignancy","TF-DNA","YAP/TAZ, TEAD and TP63 activity converge with severity"),
("26947080","T1_lung_TF_binding","ChIP-seq","airway multiciliated cells","normal","TF-DNA","p73 regulates the FOXJ1-associated gene network"),
# T2 - perturbation with molecular readout
("35058622","T2_perturbation","Perturb-seq","A549 lung cancer cells","cancer variants","functional gene-phenotype","200 TP53 and KRAS variants across >300,000 single lung cancer cells"),
("35290801","T2_perturbation","Perturb-map (spatial CRISPR)","mouse lung tumors in tissue","lung cancer","functional gene-microenvironment","dozens of genes knocked out in parallel with spatial transcriptomics"),
("35688146","T2_perturbation","genome-scale Perturb-seq","K562 and RPE1 (NOT lung)","normal","functional gene-program","all expressed genes with CRISPRi across >2.5 million cells"),
("27984732","T2_perturbation","Perturb-seq (method)","cell lines","varied","functional gene-program","original Perturb-seq report"),
("36608654","T2_perturbation","TF overexpression atlas","human embryonic stem cells (NOT lung)","directed differentiation","TF-program","atlas of TF-driven cell states"),
("31784727","T2_perturbation","CRISPRi-FlowFISH","cell lines","normal","enhancer-gene validated",">3,500 potential enhancer-gene connections tested for 30 genes; ABC model"),
("33828297","T2_perturbation","ABC maps from chromatin data","131 human cell types and tissues","72 diseases and traits","enhancer-gene","5,036 GWAS signals linked to 2,249 unique genes"),
("37488417","T2_perturbation","CRISPRi enhancer screen","hESC definitive endoderm (NOT lung)","cell-state transition","enhancer-gene validated","CTCF-loop-constrained interaction activity model"),
("37734371","T2_perturbation","iPSC-AT2 functional genomics","human iPSC-derived AT2 cells","COPD","gene-function","ADGRG6, a COPD GWAS gene, instructs AT2 function and injury response"),
# T3 - cell-type-labelled TF-DNA compendia (filter to lung biosamples)
("34174819","T3_TFDNA_catalog","curated ChIP-seq reprocessing","> 1000 cell lines and tissues","varied","TF-DNA","UniBind: ~10,000 ChIP-seq datasets, ~56 million TFBS for 644 TFs"),
("34751401","T3_TFDNA_catalog","uniform ChIP-seq reprocessing","human, mouse, fly, Arabidopsis","varied","TF-DNA","ReMap 2022: human 8,103 datasets, 1,210 regulators, 182 million peaks"),
("38749504","T3_TFDNA_catalog","ChIP/ATAC/DNase/bisulfite integration","six model organisms","varied","TF-DNA","ChIP-Atlas 3.0: over 376,000 experiments, plus GWAS SNP and ClinVar tracks"),
("30462313","T3_TFDNA_catalog","ChIP-seq/DNase/ATAC browser","human and mouse samples","varied","TF-DNA","Cistrome DB: ~47,000 samples; query which factors regulate a gene"),
("33231677","T3_TFDNA_catalog","uniform ChIP-seq processing","nine species","varied","TF-DNA","GTRD 2021 integrated view"),
("32858223","T3_TFDNA_catalog","ChIP-seq integration","tissue-labelled samples incl. lung","varied","TF-DNA","hTFtarget: 7,190 ChIP-seq samples of 659 TFs"),
("31942977","T3_TFDNA_catalog","ChIP-seq summit analysis","human cell types","varied","TF-DNA","ChIPSummitDB: 3,727 datasets, cistromes of 292 TFs, motif-to-summit distances"),
("37956336","T3_TFDNA_catalog","TF knockdown/knockout expression","tissue and cell-type annotated","varied","TF-target functional","KnockTF 2.0: 1,468 datasets, 612 TFs and 172 co-factors"),
("32814038","T3_TFDNA_catalog","DNase footprinting","27 human tissue types","normal","TF-DNA predicted","192 ENCODE DNase experiments, occupancy for 1,515 TFs"),
("32728250","T3_TFDNA_catalog","DNase I footprinting","243 human cell and tissue types","normal","TF-DNA","~4.5 million footprint elements at nucleotide resolution"),
("32728217","T3_TFDNA_catalog","DNase I hypersensitivity","733 biosamples, 438 cell and tissue types","normal","regulatory DNA index","~3.6 million DHSs with a per-DHS tissue barcode"),
("33536621","T3_TFDNA_catalog","integrative epigenomics","800 samples","540 traits","enhancer-gene-trait","EpiMap: 10,000 epigenomic maps; annotates 30,000 disease loci"),
("25693563","T3_TFDNA_catalog","histone marks, DNA accessibility, methylation, RNA","111 reference epigenomes","primary cells and tissues","regulatory modules","Roadmap Epigenomics; trait variants enriched in tissue-specific marks"),
("32728249","T3_TFDNA_catalog","ENCODE phase III integration","human and mouse tissues","normal","cis-regulatory elements","926,535 human and 339,815 mouse candidate cCREs"),
# T4 - protein-protein interaction, experimentally defined
("32296183","T4_PPI","yeast two-hybrid, all-by-all","human ORFeome","context-free binary","protein-protein","HuRI: ~53,000 binary protein-protein interactions"),
("33961781","T4_PPI","affinity purification mass spectrometry","293T and HCT116 (NOT lung)","two cell lines compared","protein-protein","BioPlex 3.0: 118,162 interactions among 14,586 proteins; cell-specific remodeling measured"),
("28514442","T4_PPI","affinity purification mass spectrometry","293T","context-free","protein-protein","BioPlex 2.0 architecture and disease communities"),
("35271311","T4_PPI","endogenous tagging, imaging plus mass spectrometry","HEK293T (NOT lung)","normal","protein-protein and localization","OpenCell interaction and localization cartography"),
("28596423","T4_PPI","integration of >9,000 MS experiments","human cells","context-free","protein complex","hu.MAP: >4,600 complexes, >7,700 proteins, >56,000 interactions"),
("39526397","T4_PPI","manual curation","mammalian cells","context-free","protein complex","CORUM 2024, complexes as drug targets"),
("33070389","T4_PPI","literature curation","many species","context-free","protein, genetic and chemical interactions","BioGRID comprehensive resource"),
("39558183","T4_PPI","integration incl. predictions","many species","context-free","protein association (NOT all measured)","STRING 2025 adds directionality of regulation; mixed evidence, filter to experimental"),
("28794006","T4_PPI","BioID proximity labeling","lung squamous carcinoma cells","cancer","protein-protein","SOX2 interactome; EP300 mediates squamous differentiation"),
("35649251","T4_PPI","interactome profiling","lung tissue and cells","health and disease","protein-protein","versican interactome in lung health and disease"),
("37914802","T4_PPI","complex purification","lung cancer cells","cancer","protein-protein","COMMD4-H2B protein complex as a lung cancer target"),
("36217030","T4_PPI","affinity purification mass spectrometry","human cells, virus-host","COVID-19","protein-protein","comprehensive SARS-CoV-2-human interactome"),
]

def esummary(pmids):
    out = {}
    for i in range(0, len(pmids), 100):
        u = BASE + "esummary.fcgi?db=pubmed&retmode=json&id=" + ",".join(pmids[i:i+100])
        out.update(json.load(urllib.request.urlopen(u)).get("result", {}))
        time.sleep(0.4)
    return out

pmids = [r[0] for r in ROWS]
assert len(set(pmids)) == len(pmids), "duplicate PMID"
S = esummary(pmids)
missing = [p for p in pmids if p not in S]
if missing:
    raise SystemExit("no PubMed record for %s" % missing)

path = os.path.join(OUT, "lung_experimental_edge_papers.csv")
with open(path, "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["tier","pmid","year","journal","first_author","title","doi","assay",
                "cell_type_or_biosample","condition","edge_type","scale_or_note","pubmed_url"])
    for pm, tier, assay, ct, cond, et, note in ROWS:
        r = S[pm]
        doi = ""
        for aid in r.get("articleids", []):
            if aid.get("idtype") == "doi": doi = aid.get("value","")
        w.writerow([tier, pm, (r.get("pubdate") or "")[:4], r.get("source",""),
                    r.get("sortfirstauthor",""), r.get("title","").rstrip("."), doi,
                    assay, ct, cond, et, note, "https://pubmed.ncbi.nlm.nih.gov/%s/" % pm])

from collections import Counter
c = Counter(r[1] for r in ROWS)
print("wrote %s" % path)
print("rows: %d" % len(ROWS))
for k in sorted(c): print("  %-22s %d" % (k, c[k]))
yrs = sorted((S[p].get("pubdate") or "")[:4] for p in pmids)
print("year range: %s to %s" % (yrs[0], yrs[-1]))
pre = [(p,(S[p].get("pubdate") or "")[:4]) for p in pmids if int((S[p].get("pubdate") or "0")[:4]) < 2015]
print("pre-2015: %s" % (pre or "none"))
