# Gene Regulation & DPI Knowledge Graph — From Absolute Zero

> **Purpose:** This document builds everything from first principles with ASCII diagrams and examples, then connects it to the DPI knowledge graph design.

---

## Part 1: The Central Dogma — Why Genes Matter

### 1.1 DNA Is a Recipe Book

Every cell in your body has the same DNA — ~3 billion letters (A, T, G, C) organized into 23 pairs of chromosomes. Think of DNA as a massive recipe book with ~20,000 recipes (genes).

```
YOUR DNA (one chromosome, simplified)
═══════════════════════════════════════════════════════════════
...ATCG[===GENE A===]TTGCA...CCAG[===GENE B===]AATC...GG[===GENE C===]...
═══════════════════════════════════════════════════════════════
        ↑ recipe for               ↑ recipe for         ↑ recipe for
        protein A                  protein B             protein C
```

**Key insight:** A gene is a stretch of DNA that contains instructions for making a protein. Proteins do the actual work in cells — they're the workers, structural materials, signals, and machines.

### 1.2 The Central Dogma: DNA → RNA → Protein

When a cell needs a protein, it doesn't use the DNA directly (too precious — it's the master copy). Instead:

```
Step 1: TRANSCRIPTION              Step 2: TRANSLATION
(copy the recipe)                  (cook from the copy)

    DNA (master copy)                  mRNA (working copy)
    ════════════════                   ════════════════
    ...ATGCCCGAA...    ──copy──▶       ...AUGCCCGAA...    ──build──▶   Protein
    ════════════════                   ════════════════                 🔵🔵🔵🔵
         gene                              mRNA                       (functional
                                                                       molecule)
```

**Transcription** = copying a gene from DNA into a messenger RNA (mRNA)
**Translation** = reading the mRNA to build a protein

**The critical question:** If every cell has the SAME 20,000 genes, why is a liver cell different from a brain cell?

**Answer:** Because different genes are turned ON or OFF in different cell types.

```
LIVER CELL                              BRAIN CELL
Gene A: ON  ████████ (makes albumin)    Gene A: OFF ░░░░░░░░
Gene B: OFF ░░░░░░░░                    Gene B: ON  ████████ (makes dopamine receptor)
Gene C: ON  ████████ (makes bile acid)  Gene C: OFF ░░░░░░░░
Gene D: ON  █████    (low level)        Gene D: ON  █████████ (high level)
```

**This is gene regulation.** The DPI-KG project is about understanding WHO turns genes on and off, and HOW.

---

## Part 2: Transcription Factors — The On/Off Switches

### 2.1 What Is a Transcription Factor?

A **Transcription Factor (TF)** is a protein whose job is to turn other genes on or off. It does this by **physically sitting on the DNA** near a target gene and either helping or blocking the transcription machinery.

```
A TF is itself a protein (made by its own gene):

Gene for MYC ──transcription──▶ mRNA ──translation──▶ MYC protein (a TF)
                                                           │
                                                           │ MYC protein goes and
                                                           │ sits on DNA near OTHER genes
                                                           ▼
                                               ┌─────────────────────┐
                                               │ DNA near BCL2 gene  │
                                               │     ▼               │
                                               │   [MYC]             │
                                               │   ═══╦══════════    │
                                               │      ║ BCL2 gene    │
                                               │   ═══╩══════════    │
                                               │                     │
                                               │ MYC turns BCL2 ON   │
                                               └─────────────────────┘
```

**Concrete example:**
- **MYC** is a transcription factor (one of the most studied in biology)
- MYC protein binds to DNA near the **BCL2** gene
- This binding ACTIVATES BCL2 — turns it on, makes more BCL2 protein
- BCL2 protein prevents cell death (apoptosis)
- So: MYC → turns on BCL2 → cell survives

### 2.2 Activators vs. Repressors

TFs come in two flavors:

```
ACTIVATOR TF                              REPRESSOR TF
════════════                              ════════════

    [TF] 🟢                                  [TF] 🔴
    ═══╦══════════                            ═══╦══════════
       ║ Gene X    ──▶ MORE mRNA ──▶ MORE       ║ Gene Y    ──▶ LESS mRNA ──▶ LESS
    ═══╩══════════     protein X              ═══╩══════════     protein Y

"TF activates Gene X"                    "TF represses Gene Y"
Gene expression goes UP ↑                Gene expression goes DOWN ↓
```

**Real examples:**
- **MYC activates BCL2** → more BCL2 → cell survives
- **TP53 represses MYC** → less MYC → cell stops growing
- **FOXO3 activates CDKN1A (p21)** → more p21 → cell cycle arrest

**This is regulatory "direction":** Is this TF an activator or repressor of this target gene?

### 2.3 How Does a TF "Know" Where to Sit?

TFs don't randomly land on DNA. Each TF has a **DNA-binding domain** — a part of the protein that recognizes a specific short sequence pattern (called a **motif**).

```
MYC recognizes this motif: CACGTG (called an "E-box")

DNA: ...TTGACCACGTGAAATCCC...      ◀── MYC binds HERE because it
           ══════                       "sees" the CACGTG sequence
           CACGTG
           (E-box motif)

    [MYC protein]
       │
       ▼ binds
    ...TTGACCACGTGAAATCCC...
           ══════
```

**JASPAR** is a database of these motifs — it catalogs the DNA sequence patterns that each TF recognizes. When we say "motif evidence," it means: does the TF's known binding motif exist at that genomic position?

---

## Part 3: Where on the DNA Does Regulation Happen?

### 3.1 Regulatory Regions

Genes don't start at the beginning of the gene body. There's a stretch of DNA **upstream** (before) each gene that controls whether it gets transcribed. These are called **regulatory regions** or **cis-regulatory elements (CREs)**.

```
                    REGULATORY REGIONS                          GENE BODY
    ◀───────────────────────────────────────────▶    ◀──────────────────────▶

    Enhancer          Promoter                       Gene X
    (far away)        (right at the start)
    ┌──────┐         ┌──────────┐                   ┌══════════════════════┐
    │ [TF] │─ ─ ─ ─ ─│ [TF][TF] │──────────────────▶│     coding region    │
    │      │  loops   │ RNA Pol  │  starts            │                      │
    └──────┘  over    └──────────┘  transcription    └══════════════════════┘

    ◀─ can be 10,000-1,000,000       ◀─ typically within
       bases away from the gene          500 bases of gene start (TSS)
```

**Three main types of regulatory regions:**

| Region Type | Where | What It Does | Analogy |
|---|---|---|---|
| **Promoter** | Right at the gene start (TSS) | Base station — RNA polymerase lands here to start copying | The runway where the plane takes off |
| **Enhancer** | Far away (10kb to 1Mb) | Boosts transcription by looping DNA to contact the promoter | A turbo button that can be far from the engine |
| **Insulator/CTCF** | Between genes | Blocks enhancers from activating the wrong gene | A wall between apartments |

**Design note:** For the KG, knowing promoter vs. enhancer is nice-to-have but not essential initially.

---

## Part 4: Co-Factors — When Two TFs Work Together

### 4.1 The MYC + MAX Example

Some TFs can't work alone. They need a partner (a **co-factor**) to bind DNA effectively.

```
MYC ALONE: can't bind DNA well          MYC + MAX TOGETHER: strong binding
═══════════════════════                  ═══════════════════════

    [MYC] ← unstable                        [MYC]──[MAX]  ← stable complex
       │    on its own                           │
       ↓    weak binding                         ↓ strong binding
    ───CACGTG───                              ───CACGTG───
    (barely sticks)                           (locks on)
                                                  │
                                                  ▼
                                              Gene X → ON (activated)
```

**This is the co-factor problem:**
- TF1 (MYC) and TF2 (MAX) must both be present for the interaction to work
- In the KG, this is a "conditional edge" — the regulation only happens when BOTH TFs are there
- Sid currently handles this by concatenating: `"MYC_MAX"` — which is fragile
- Better: a `RegulatoryComplex` node that says "MYC AND MAX together regulate Gene X"

### 4.2 Why It Matters

```
MYC + MAX  → activates target genes → cell proliferation
MYC + MIZ1 → represses target genes → blocks differentiation

SAME TF (MYC), different partner → OPPOSITE effect!
```

This is why concatenating TF names is bad engineering — MYC participates in multiple complexes with different biological outcomes.

---

## Part 5: How Do We MEASURE TF Binding? (The Experiments)

### 5.1 ATAC-seq — "Where Is the DNA Open?"

**Problem:** DNA in cells is tightly packed around proteins called histones (like thread wound around spools). When DNA is tightly packed, TFs can't access it. When it's open, TFs CAN bind.

```
CLOSED CHROMATIN (inaccessible)          OPEN CHROMATIN (accessible)
════════════════════════                 ════════════════════════

    DNA wound tightly                       DNA is loose/open
    around histones                         TFs can reach the DNA

    ◯◯◯◯◯◯◯◯◯◯◯◯◯                          ◯    ◯    ◯    ◯
    ═══════════════  ← DNA buried           ═══╤══════╤═══  ← DNA exposed
    can't access                               │      │
                                             [TF1]  [TF2]  ← TFs can bind!
```

**ATAC-seq** (Assay for Transposase-Accessible Chromatin) measures **which parts of the genome are open** in a given cell type. It tells you: "at THIS position in the genome, the DNA is accessible, so TFs COULD bind here."

```
ATAC-seq output for a cell type:

Chromosome position →
     ___        ________            ___
    /   \      /        \          /   \
───/─────\────/──────────\────────/─────\──────  ← Signal height = accessibility
                                                    ("openness")
  Peak 1     Peak 2               Peak 3
  (short)    (strong, tall)       (short)

Peaks = "open" regions where TFs might be binding
```

### 5.2 ChIP-seq — "WHERE Does a Specific TF Actually Bind?"

While ATAC-seq tells you where DNA is open (general), **ChIP-seq** tells you where a **specific** TF is physically sitting on the DNA.

```
ChIP-seq for MYC in K562 cells:

1. Cells are alive, MYC is bound to DNA at various positions
2. Cross-link: freeze everything in place (formaldehyde)
3. Shred DNA into fragments
4. Use an antibody (anti-MYC) to fish out only fragments with MYC attached
5. Sequence those fragments → tells you EXACTLY where MYC was sitting

                anti-MYC
               antibody
                  │
                  ▼
    ═══[MYC]═══  ◀── this fragment gets captured
    ═══════════  ◀── this fragment is NOT captured (no MYC)
    ═══[MYC]═══  ◀── this fragment gets captured
    ═══════════  ◀── this fragment is NOT captured

Result: a genome-wide map of every position where MYC was bound
```

**Key ChIP-seq databases:**
- **ChIP-Atlas**: 224K+ ChIP-seq experiments, uniformly processed. You look up "MYC in K562 cells" and get every position where MYC binds.
- **UniBind**: Same idea but ALSO checks that the TF's motif is present at the peak (higher confidence — "the TF actually directly touched the DNA here, not just nearby")
- **CistromeDB**: Another large collection of uniformly reprocessed ChIP-seq data

### 5.3 ATAC-seq vs. ChIP-seq — The Key Difference

```
ATAC-seq:                               ChIP-seq:
"Where is the DNA open?"                "Where does MYC specifically bind?"

Shows ALL open regions                  Shows binding of ONE specific TF
(many TFs could be there)               (only the TF you have antibody for)

Cheaper, easier to run                  More expensive, need specific antibody
Works for any cell type                 Need to run separately for each TF

Tells you POTENTIAL binding sites       Tells you ACTUAL binding sites
```

---

## Part 6: ChromLinker/ChromBPNet — From ATAC-seq to TF Predictions

### 6.1 The Problem ChromBPNet Solves

ATAC-seq tells you "the DNA is open here," but it doesn't tell you WHICH TF is causing the opening. ChromBPNet is a deep learning model that looks at ATAC-seq data and **predicts which TFs are responsible** for each open region.

```
Input: ATAC-seq signal + DNA sequence at an open region

    ATAC-seq peak:       ___
                        /   \
    ───────────────────/─────\──────────
                      chr7:55,019,000

    DNA sequence:  ...TTGACCACGTGAAATCCC...
                          ══════
                          E-box motif → MYC probably binds here!

ChromBPNet learns: "a peak with this shape at a position with an E-box motif
                    = MYC is likely binding here"
```

### 6.2 How ChromBPNet Builds the Regulatory Edges

Here's the ChromBPNet pipeline:

```
Step 1: Run ATAC-seq on Cell Type X
        → Get open chromatin peaks

Step 2: Feed peaks + DNA sequences into ChromBPNet
        → For each peak, predict WHICH TFs are binding there

Step 3: Link TF binding prediction to nearby genes
        → "TF A binds at position chr7:55,019,000, which is near Gene B"

Step 4: Correlate: does Gene B's expression go UP when TF A's binding signal
        goes UP? (across many cells/samples)
        → Positive correlation = TF A likely ACTIVATES Gene B
        → Negative correlation = TF A likely REPRESSES Gene B

Result: TF A ──(+0.72)──▶ Gene B    (in Cell Type X)
        "TF A likely activates Gene B in this cell type,
         with correlation strength 0.72"
```

**This is the PRIMARY data source for the knowledge graph.** Every edge starts here. The ChromLinker framework combines RNA, surface protein, and chromatin data to produce GRN predictions; ChromBPNet is the underlying base-resolution binding model.

### 6.3 The Correlation Score

The target gene expression correlation with the DNA accessibility gives a correlated value — basically a correlation score that can be positive or negative.

```
POSITIVE correlation (+0.72):              NEGATIVE correlation (-0.65):
TF accessibility ↑ → Gene expression ↑     TF accessibility ↑ → Gene expression ↓

TF access:  ▁▃▆█████▆▃▁                   TF access:  ▁▃▆█████▆▃▁
Gene expr:  ▁▃▅███████▅▃                   Gene expr:  █▇▅▃▁▁▁▃▅█

→ TF is an ACTIVATOR of this gene          → TF is a REPRESSOR of this gene
   (more TF binding = more gene expression)   (more TF binding = less gene expression)
```

**Critical detail:** This score is **cell-type-specific.** The same TF→Gene pair can have a +0.72 correlation in lung cells and a -0.3 correlation in liver cells — meaning MYC activates BCL2 in lung but might repress it in liver. Same edge, different score, different biology.

---

## Part 7: Gene Regulatory Networks (GRNs) — The Big Picture

### 7.1 What Is a GRN?

A **Gene Regulatory Network** is a map of all the TF→Gene regulatory relationships in a cell. It answers: "Who regulates whom?"

```
A small GRN:

    TP53 (master regulator)
     │ \
     │  \── represses ──▶ MYC
     │                    │ \
     │                    │  \── activates ──▶ BCL2
     │                    │                    │
     │                    │                    ▼
     │                    │             Cell Survival ↑
     │                    │
     │                    └── activates ──▶ CDK4
     │                                       │
     │                                       ▼
     │                                Cell Division ↑
     │
     └── activates ──▶ CDKN1A (p21)
                          │
                          ▼
                    Cell Cycle Arrest ↑
```

**Reading this network:**
- TP53 represses MYC → less MYC → less cell growth → anti-cancer
- TP53 activates p21 → more p21 → cell cycle stops → anti-cancer
- MYC activates BCL2 → more BCL2 → cell survives → can be pro-cancer
- If TP53 is mutated (broken): MYC runs wild → uncontrolled growth → cancer

### 7.2 Why Cell-Type Specificity Matters

The SAME TFs exist in every cell, but they regulate DIFFERENT targets in different cell types because different regulatory regions are open:

```
LUNG EPITHELIAL CELL:                    T-CELL (immune):
═════════════════════                    ════════════════

Open regions near lung genes             Open regions near immune genes
MYC can access lung-specific             MYC can access immune-specific
enhancers                                enhancers

MYC ──(+0.8)──▶ SFTPC (surfactant)      MYC ──(+0.7)──▶ IL2 (interleukin)
MYC ──(+0.6)──▶ NKX2-1 (lung TF)        MYC ──(+0.5)──▶ CD69 (activation marker)
MYC ──(-0.3)──▶ KRT5 (basal cell)        MYC ──(-0.4)──▶ FOXP3 (Treg marker)

DIFFERENT targets, DIFFERENT scores       DIFFERENT targets, DIFFERENT scores
```

**This is WHY cell-type-specific scores are essential.** A "generic" GRN without cell type context is meaningless — it mashes together regulatory relationships from incompatible biological contexts.

---

## Part 8: Why STRING Is McDonald's

### 8.1 What STRING Actually Does

STRING (string-db.org) is a database of "protein-protein associations." It throws everything into one pot:

```
STRING edge types (ALL mixed together):

1. "These proteins are co-expressed"          ← NOT an interaction
2. "These proteins are in the same pathway"   ← NOT an interaction
3. "A text mining algorithm found them in     ← MAYBE an interaction
    the same sentence"
4. "These proteins physically bind each other" ← THIS is an interaction
5. "They appear in the same Gene Ontology     ← DEFINITELY NOT an interaction
    annotation"

STRING combines all of these into one "confidence score."
```

**The fundamental problem:** co-expression and pathway co-membership are **concepts**, not **interactions**. Two genes having similar expression patterns is not evidence that one regulates the other — they could both be regulated by a third gene.

### 8.2 What YOUR KG Does Differently

```
YOUR DPI-KG edge requirements:

✅ TF protein physically binds DNA near target gene
   (ChIP-seq evidence or ChromLinker/ChromBPNet prediction)

✅ Binding correlates with target gene expression change
   (ATAC-seq/expression correlation)

✅ Optional: TF's binding motif is present at the binding site
   (JASPAR motif match)

✅ Optional: Literature confirms regulatory direction
   (PubMed Central extraction)

❌ NOT: "these genes are co-expressed" (that's correlation, not causation)
❌ NOT: "they're in the same pathway" (that's annotation, not interaction)
❌ NOT: "they were mentioned in the same paper" (that's text mining, not biology)
```

---

## Part 9: The Evidence Sources — All of Them

Now you understand the biology. Here's every data source and why it matters:

```
╔══════════════════════════════════════════════════════════════════════╗
║                    EVIDENCE SOURCES FOR THE KG                      ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                     ║
║  ┌────────────────────────────────────────────────────────┐         ║
║  │ 1. ChromLinker/ChromBPNet (your lab's primary source)   │         ║
║  │    Input: ATAC-seq data for a specific cell type       │         ║
║  │    Output: TF → Gene edge with correlation score (+/-) │         ║
║  │    Also produces: base-resolution seqlets/peaks that   │         ║
║  │    feed RegulatoryLocus nodes for position-level       │         ║
║  │    evidence (GWAS/variant overlap queries)              │         ║
║  │    Type: CONTINUOUS (e.g., +0.72, -0.45)               │         ║
║  │    This is THE primary source of edges                 │         ║
║  └────────────────────────────────────────────────────────┘         ║
║                           │                                         ║
║                           ▼                                         ║
║  ┌────────────────────────────────────────────────────────┐         ║
║  │ 2. ChIP-seq Databases (confirms TF actually binds)     │         ║
║  │    ChIP-Atlas: 224K experiments, most TFs, most cells  │         ║
║  │    UniBind: highest stringency (motif-validated peaks) │         ║
║  │    CistromeDB: uniformly reprocessed public data      │         ║
║  │    Type: BINARY (yes/no, this TF binds here)           │         ║
║  │         + quality metadata (q-value, peak score)       │         ║
║  └────────────────────────────────────────────────────────┘         ║
║                           │                                         ║
║                           ▼                                         ║
║  ┌────────────────────────────────────────────────────────┐         ║
║  │ 3. Motif Databases (TF's DNA sequence pattern exists)  │         ║
║  │    JASPAR: curated TF motif database (~2000 motifs)    │         ║
║  │    Type: BINARY (motif present at binding site, yes/no)│         ║
║  │         + quality metadata (p-value of match)          │         ║
║  └────────────────────────────────────────────────────────┘         ║
║                           │                                         ║
║                           ▼                                         ║
║  ┌────────────────────────────────────────────────────────┐         ║
║  │ 4. Curated Databases (gold-standard known interactions)│         ║
║  │    TRRUST: ~8,400 human TF→target with direction      │         ║
║  │    CollecTRI: ~47K interactions with direction         │         ║
║  │    DoRothEA: ~1.5M interactions tiered A-E            │         ║
║  │    Type: BINARY (known interaction yes/no)             │         ║
║  │         + direction (activator/repressor)              │         ║
║  │    ROLE: validation FIRST, then evidence               │         ║
║  └────────────────────────────────────────────────────────┘         ║
║                           │                                         ║
║                           ▼                                         ║
║  ┌────────────────────────────────────────────────────────┐         ║
║  │ 5. Literature (PubMed Central)                         │         ║
║  │    Section-aware extraction pipeline (see Part 11)    │         ║
║  │    Extracts: TF, target gene, direction, cell type     │         ║
║  │    Type: SEMI-STRUCTURED                               │         ║
║  │    ROLE: confirms regulatory DIRECTION that data       │         ║
║  │          alone can only suggest via correlation sign    │         ║
║  └────────────────────────────────────────────────────────┘         ║
║                           │                                         ║
║                           ▼                                         ║
║  ┌────────────────────────────────────────────────────────┐         ║
║  │ 6. BioGRID (protein-protein interaction)               │         ║
║  │    Only for CO-FACTOR evidence: do TF1 and TF2         │         ║
║  │    physically interact? (yeast two-hybrid, co-IP)      │         ║
║  │    Type: BINARY                                        │         ║
║  │    NOT for TF→gene edges. Only for TF-TF co-binding.  │         ║
║  └────────────────────────────────────────────────────────┘         ║
║                           │                                         ║
║                           ▼                                         ║
║  ┌────────────────────────────────────────────────────────┐         ║
║  │ 7. Perturb-seq / CRISPRi (gold-standard causal)       │         ║
║  │    Directly knock out a TF, measure what genes change  │         ║
║  │    Type: CONTINUOUS (fold change + p-value)            │         ║
║  │    ROLE: the BEST validation. Causal, not correlative. │         ║
║  │    If you knock out MYC and BCL2 goes down → PROOF     │         ║
║  │    that MYC activates BCL2.                            │         ║
║  └────────────────────────────────────────────────────────┘         ║
║                           │                                         ║
║                           ▼                                         ║
║  ┌────────────────────────────────────────────────────────┐         ║
║  │ 8. GWAS / Variant Databases (disease-variant links)    │         ║
║  │    GWAS Catalog: curated trait-variant associations     │         ║
║  │    Open Targets: credible sets, L2G, colocalisation    │         ║
║  │    ENCODE SCREEN: cCRE annotations (human + mouse)     │         ║
║  │    RegulomeDB: variant regulatory potential scoring     │         ║
║  │    Type: BINARY + statistics (p-value, odds ratio)     │         ║
║  │    ROLE: overlap variants with regulatory loci to find │         ║
║  │          disease-relevant TF binding disruptions        │         ║
║  └────────────────────────────────────────────────────────┘         ║
║                           │                                         ║
║                           ▼                                         ║
║  ┌────────────────────────────────────────────────────────┐         ║
║  │ 9. Drug-Target Databases (druggability)                │         ║
║  │    DGIdb: aggregated drug-gene interactions (40+ src)  │         ║
║  │    Open Targets: drug-target with clinical evidence    │         ║
║  │    ChEMBL: bioactivity data for drug-like molecules    │         ║
║  │    Type: BINARY (drug targets this gene, yes/no)       │         ║
║  │    NOT DrugBank (licensed). Use open sources only.     │         ║
║  └────────────────────────────────────────────────────────┘         ║
╚══════════════════════════════════════════════════════════════════════╝
```

---

## Part 10: The Knowledge Graph — Putting It All Together

### 10.1 A Single Edge, Fully Illustrated

Let's trace one complete example: **MYC activates BCL2 in A549 cells.**

```
Step 1: ChromBPNet predicts MYC binds near BCL2 in A549 cells
        Correlation score: +0.72 (positive = activator)
        Binding position: chr18:63,100,100-63,100,450

Step 2: ChIP-Atlas confirms MYC binding at that position
        Experiment SRX3456789, anti-MYC antibody in A549
        Peak q-value: 1e-12 (very significant)

Step 3: JASPAR motif match: E-box (CACGTG) present at chr18:63,100,250
        p-value: 1e-8

Step 4: TRRUST says: MYC → BCL2, direction: activator
        (curated from literature)

Step 5: Extraction from PMID:35000001:
        "MYC directly activates BCL2 transcription in A549 cells"
        Direction: activator, directness: direct_binding, confidence: 0.9
```

**In the graph (with InteractionContext):**

```
 ┌──────────────┐                      ┌──────────────┐
 │  MYC (:TF)   │──REGULATES_VIA──▶   │  BCL2 (:Gene)│
 │  HGNC:7553   │                      │  HGNC:990    │
 └──────────────┘                      └──────────────┘
                        │
                        ▼
              ┌─────────────────────────┐
              │  RegulatoryInteraction   │
              │  (canonical edge)        │
              │  base_confidence: 0.92   │◀─── "this TF CAN regulate this gene"
              └─────────┬───────────────┘
                        │
                   HAS_CONTEXT
                        │
              ┌─────────┴───────────────┐
              ▼                         ▼
    ┌─────────────────────┐   ┌─────────────────────┐
    │ InteractionContext   │   │ InteractionContext   │
    │ A549, NSCLC, human   │   │ Jurkat, T-ALL, human │
    │ direction: activator │   │ direction: unknown    │
    │ confidence: 0.87     │   │ confidence: 0.45      │
    │ correlation: +0.72   │   │ correlation: -0.15    │
    └─────────┬───────────┘   └─────────┬─────────────┘
              │                         │
         SUPPORTS                  SUPPORTS
              │                         │
    ┌─────────┼──────────┐              ▼
    ▼         ▼          ▼         ┌───────────┐
┌────────┐ ┌────────┐ ┌────────┐   │ ChromBPNet│
│ChromBPN│ │ChIP-Atl│ │TRRUST  │   │ score:-0.1│
│+0.72   │ │q:1e-12 │ │dir:act │   │ cell:Jurkt│
└────────┘ └────────┘ └────────┘   └───────────┘
```

**The confidence scores are NOT hand-assigned.** Two trained models produce them:
- **base_confidence (0.92):** "Is this a real TF→Gene edge at all?" (trained on TRRUST/CollecTRI)
- **context_confidence (0.87):** "Is this edge active as an activator in A549/NSCLC?" (trained on Perturb-seq + matched ChromLinker/ChromBPNet data)

### 10.2 Cell-Type-Specific Scoring — Why InteractionContext Matters

The same MYC → BCL2 pair has different behavior in different cell systems. Each gets its OWN InteractionContext with its OWN evidence:

```
                    RegulatoryInteraction
                    MYC → BCL2 (canonical)
                         │
                    HAS_CONTEXT
                         │
              ┌──────────┼──────────┐
              ▼          ▼          ▼
    ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
    │ A549         │ │ HCC827       │ │ Jurkat       │
    │ NSCLC        │ │ NSCLC        │ │ T-ALL        │
    │ activator    │ │ activator    │ │ unknown      │
    │ +0.72        │ │ +0.45        │ │ -0.15        │
    │ conf: 0.87   │ │ conf: 0.68   │ │ conf: 0.45   │
    └──────────────┘ └──────────────┘ └──────────────┘
         ▲                ▲                ▲
     4 evidence       2 evidence       1 evidence
     nodes            nodes            node

Same TF, same gene, DIFFERENT contexts → DIFFERENT behavior.
This is why a single global 'direction' on the canonical edge would be misleading.
```

### 10.3 Co-Factor Example

MYC + MAX co-bind to activate BCL2:

```
 ┌──────────────┐
 │  MYC (:TF)   │──MEMBER_OF──┐
 │  HGNC:7553   │             │
 └──────────────┘             ▼
                    ┌──────────────────┐         ┌──────────────────────┐
                    │RegulatoryComplex │──REG──▶ │RegulatoryInteraction │──▶ BCL2
                    │ MYC + MAX        │         │ direction: activator  │
 ┌──────────────┐   │ condition: AND   │         │ confidence: 0.91      │
 │  MAX (:TF)   │──▶│ type: cobinding  │         └──────────────────────┘
 │  HGNC:6913   │   └──────────────────┘
 └──────────────┘

Meaning: BOTH MYC and MAX must be present for this regulation to happen.
```

### 10.4 Context Dimensions — Disease, Development, Species

Cell type is not the ONLY context that matters. The same TF→Gene interaction can mean completely different things depending on three additional dimensions. All four context dimensions live on **InteractionContext** nodes:

#### Disease Context

A TF→Gene edge can be specific to a disease. MYC→BCL2 matters differently in cancer vs. normal tissue:

```
RegulatoryInteraction: MYC → BCL2 (canonical)
     │
     ├── HAS_CONTEXT ──▶ InteractionContext
     │                   cell_system: A549
     │                   disease: MONDO:0005233 (NSCLC)
     │                   direction: activator
     │                   "MYC overexpression drives survival"
     │
     └── HAS_CONTEXT ──▶ InteractionContext
                         cell_system: Raji
                         disease: MONDO:0018906 (Lymphoma)
                         direction: activator
                         "MYC-BCL2 double-hit = worst prognosis"
```

**Why it matters:** If you're studying NSCLC, you query for `disease = 'MONDO:0005233'` and get only the evidence relevant to NSCLC.

#### Developmental Stage

Gene regulation changes dramatically during development. A TF that is active in embryonic lungs may be silenced in adult lungs:

```
RegulatoryInteraction: SOX9 → COL2A1 (canonical)
     │
     ├── HAS_CONTEXT ──▶ InteractionContext
     │                   dev_stage: "embryonic"
     │                   direction: activator
     │                   "SOX9 actively drives branching morphogenesis"
     │
     └── HAS_CONTEXT ──▶ InteractionContext
                         dev_stage: "adult"
                         direction: unknown
                         "SOX9 mostly silenced, re-activated in cancer"
```

**Why it matters:** A TF→Gene edge observed in embryonic tissue may not be relevant to adult disease biology, and vice versa.

#### Species

Many experiments are done in mouse. The KG tracks this per context:

```
RegulatoryInteraction: NKX2-1 → SFTPC (canonical)
     │
     ├── HAS_CONTEXT ──▶ InteractionContext
     │                   species: NCBITaxon:10090 (mouse)
     │                   "validated in mouse lung development"
     │
     └── HAS_CONTEXT ──▶ InteractionContext
                         species: NCBITaxon:9606 (human)
                         "confirmed in human alveolar type II cells"
```

**Why it matters:** Mouse and human share most TFs, but regulatory regions differ. An interaction validated in mouse is good evidence but not proof in human.

#### The Complete Context Picture

```
              RegulatoryInteraction (canonical)
              MYC → BCL2
              base_confidence: 0.92
                    │
               HAS_CONTEXT
                    │
         ┌──────────┴──────────┐
         ▼                     ▼
┌──────────────────┐  ┌──────────────────┐
│InteractionContext│  │InteractionContext│
│ A549 / NSCLC     │  │ Jurkat / T-ALL   │
│ human / adult    │  │ human / adult    │
│ activator, 0.87  │  │ unknown, 0.45   │
│ corr: +0.72      │  │ corr: -0.15     │
└────────┬─────────┘  └────────┬─────────┘
         │                     │
     SUPPORTS              SUPPORTS
         │                     │
    ┌────┴────┐           ┌────┴────┐
    ▼    ▼    ▼           ▼         
  Ev1  Ev2  Ev3         Ev4       
  CBP  ChIP LIT         CBP       
```

**Query example:** `MATCH (ri)-[:HAS_CONTEXT]->(ctx) WHERE ctx.disease = 'MONDO:0005233' AND ctx.species = 'NCBITaxon:9606' AND ctx.context_confidence > 0.5`

---

## Part 11: The Complete Pipeline

### The One-Line Summary

```
structured data first → variants + eQTLs → initial weights → choose papers →
read papers → parse tables → revised weights → context assembly → vision last
```

### The Full Pipeline

```
╔══════════════════════════════════════════════════════════════════════════╗
║                        DPI-KG CONSTRUCTION PIPELINE                     ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                         ║
║  Phase 1: BUILD EDGES FROM STRUCTURED DATA                              ║
║  ════════════════════════════════════════                                ║
║                                                                         ║
║  ATAC-seq data ──▶ ChromLinker/ChromBPNet ──▶ TF→Gene edges             ║
║                    + RegulatoryLocus nodes from peaks/seqlets            ║
║                                   (PRIMARY source — creates graph)      ║
║                                          │                              ║
║  CistromeDB ─────────────────────────────┤                              ║
║  ChIP-Atlas ─── attach as ───────────────┤ ◀── Evidence nodes           ║
║  UniBind    ─── evidence ────────────────┤     (SUPPORTS relationship)  ║
║  JASPAR     ─── nodes    ────────────────┤                              ║
║  BioGRID    ─── (co-factor only) ────────┘                              ║
║  TRRUST/CollecTRI ──▶ curated gold standard (validation labels)         ║
║  Perturb-seq ──▶ causal validation evidence                             ║
║                                                                         ║
║  Phase 2: VARIANT OVERLAY + GTEx eQTLs                                  ║
║  ═════════════════════════════════════                                   ║
║                                                                         ║
║  RegulatoryLocus nodes enable:                                          ║
║  Variant ──OVERLAPS──▶ RegulatoryLocus ──LINKED_TO_GENE──▶ Gene         ║
║  Variant ──HAS_GWAS──▶ GWASAssociation                                  ║
║                                                                         ║
║  GTEx eQTLs strengthen the LINKED_TO_GENE edge:                         ║
║    link_method: eQTL   (variant actually changes gene expression)       ║
║    link_method: proximity (nearest gene — weaker)                       ║
║    link_method: HiC    (physical chromatin contact)                      ║
║                                                                         ║
║  Phase 3: INITIAL WEIGHT LEARNING (Stage 1)                             ║
║  ══════════════════════════════════════════                              ║
║                                                                         ║
║  Known interactions (TRRUST + Perturb-seq) = positive training set      ║
║  Random TF-Gene pairs with no evidence = negative training set          ║
║                    │                                                    ║
║                    ▼                                                    ║
║  Train base edge model on structured features only                      ║
║  Output: base_confidence per RegulatoryInteraction                      ║
║                                                                         ║
║  Phase 4: CHOOSE PAPERS (corpus selection)                              ║
║  ═════════════════════════════════════════                               ║
║                                                                         ║
║  GRN gene list ──▶ gene-seeded PubMed/PMC queries                       ║
║  Citation expansion ──▶ forward/backward from seed hits                 ║
║  DB-linked papers ──▶ papers cited by TRRUST/CistromeDB entries         ║
║                    │                                                    ║
║                    ▼                                                    ║
║  Article triage ──▶ Tier 0/1/2/3/Reject                                 ║
║  (see "How We Choose Papers" below)                                     ║
║                                                                         ║
║  Phase 5: READ PAPERS (text + table + supplement extraction)            ║
║  ═══════════════════════════════════════════════════════════             ║
║                                                                         ║
║  PMC JATS/XML ──▶ structured sections                                   ║
║  PDF fallback ──▶ Docling                                               ║
║                    │                                                    ║
║         ┌──────────┼──────────┐                                         ║
║         ▼          ▼          ▼                                         ║
║       TEXT       TABLES    SUPPLEMENTS                                  ║
║    (section-    (ChIP-seq  (CSV/XLSX,                                   ║
║     aware)      target     DEG lists,                                   ║
║                 lists)     peak tables)                                  ║
║         │          │          │                                         ║
║         └──────────┼──────────┘                                         ║
║                    ▼                                                    ║
║  Grounding (BOND) ──▶ HGNC, CL, MONDO, NCBITaxon, hg38                 ║
║                    │                                                    ║
║                    ▼                                                    ║
║  Precision gate: >80% vs TRRUST/CollecTRI?                              ║
║    YES ──▶ attach as Evidence nodes                                     ║
║    NO  ──▶ fix extraction pipeline first                                ║
║                                                                         ║
║  Phase 6: REVISED WEIGHT LEARNING (Stage 2)                             ║
║  ══════════════════════════════════════════                              ║
║                                                                         ║
║  Retrain with literature features added to structured features          ║
║  Output: context_confidence per InteractionContext                      ║
║                                                                         ║
║  Phase 7: CONTEXT ASSEMBLY                                              ║
║  ═════════════════════════                                              ║
║                                                                         ║
║  BOND harmonization ──▶ standardize cell/disease/species labels         ║
║  InteractionContext nodes per cell system                                ║
║  DEGSet overlay ──▶ contextual annotation                               ║
║  Drug overlay (DGIdb/ChEMBL) ──▶ druggable target annotation            ║
║                                                                         ║
║  Phase 8: FIGURE / VISION LAYER (build last)                            ║
║  ═══════════════════════════════════════════                             ║
║                                                                         ║
║  Extract figures + captions from PMC                                    ║
║  Classify: pathway diagram / ChIP track / plot / microscopy             ║
║  Vision LLM ──▶ Evidence {source: "figure_vision"}                      ║
║  Cross-validate against text claims from same paper                     ║
║  (see "Why Vision Is Useful but Dangerous" below)                       ║
║                                                                         ║
║  DOWNSTREAM APPLICATIONS                                                ║
║  ════════════════════════                                                ║
║                                                                         ║
║  • GNN for perturbation prediction                                      ║
║    "If I knock out MYC, what happens to the network in A549?"           ║
║  • Variant-aware network prioritization                                 ║
║    "Which GWAS variants overlap TF binding sites in the IPF AT2 GRN?"   ║
║  • Drug-target overlay                                                  ║
║    "Which DEGs in the GRN are druggable?"                               ║
║  • Hypothesis generation                                                ║
║    "Patient has KEAP1 mutation — what TF network is disrupted?"         ║
║                                                                         ║
╚══════════════════════════════════════════════════════════════════════════╝
```

### How We Choose Papers

Not all papers are worth processing. PubMed has ~37 million abstracts. PMC has ~8 million full-text articles. We need maybe 2,000-5,000.

**PubMed vs PMC — the distinction matters:**

| | PubMed | PubMed Central (PMC) |
|---|---|---|
| **What it has** | Abstracts + metadata for ~37M articles | Full text (XML + PDF + figures + supplements) for ~8M articles |
| **Access** | Free, E-utilities API | Free (Open Access subset), FTP/OAI-PMH |
| **What we can extract** | Gene mentions in abstracts only | Full Results sections, tables, figure captions, supplementary files |
| **Usefulness for DPI-KG** | Tier 3 (abstract-only) | Tier 1-2 (full multimodal processing) |

**The retrieval strategy:**

```
  Step 1: SEED
  ════════════
  Input: your GRN gene list (200 TFs + 2000 targets from ChromLinker)

  For each TF-Gene pair, query PubMed/PMC:
    "{TF}[Title/Abstract] AND {Gene}[Title/Abstract]
     AND (regulates OR activates OR represses OR ChIP OR knockdown)"

  This finds papers that ALREADY mention both the TF and target together.
  Expected: ~500-2000 papers.

  Step 2: EXPAND
  ══════════════
  For high-value papers from Step 1:
    - Get papers that cite them (forward citations)
    - Get papers they cite (backward citations)
    - Filter: same TFs/genes mentioned
  This catches papers using different gene names or aliases.

  Step 3: DB-LINKED
  ═════════════════
  Papers cited by TRRUST/CollecTRI entries for your TF-Gene pairs.
  Papers linked to ChIP-Atlas experiments you're already using.
  These are papers the curated databases already vetted.
```

**Article triage — score before expensive processing:**

Every paper gets scored on five dimensions BEFORE you spend time extracting from it:

| Score | What it measures | Example |
|-------|-----------------|---------|
| `domain_score` | Is this about our disease/cell type? | "IPF", "AT2", "alveolar" → high |
| `regulatory_score` | Does it discuss TF regulation? | "ChIP-seq", "knockdown", "enhancer" → high |
| `evidence_score` | Primary research or review? | Experimental paper → high; editorial → low |
| `asset_score` | Does it have full text + figures + supplements? | PMC OA with supplements → high |
| `trust_score` | Journal quality, retraction status | Not retracted, peer-reviewed → high |

**Tiers:**
- **Tier 0:** Curated gold papers you've hand-selected for validation
- **Tier 1:** Full processing (text + tables + figures) — highest domain + regulatory scores
- **Tier 2:** Text and tables only — good papers without extractable figures
- **Tier 3:** Abstract only — PubMed-only papers, no full text available
- **Reject:** Irrelevant, editorials, vague association studies, retracted

**NLP shortcut you should know about:**

**PubTator Central** is an NCBI service that has ALREADY run gene/disease/species/mutation NER on the entirety of PubMed. You don't need to build your own gene name recognizer from scratch — PubTator gives you pre-annotated mentions. You still need to do *relation extraction* (which TF regulates which gene), but the entity recognition step is free.

**BioRED** is an NCBI dataset with ~600 PubMed articles where biomedical relations have been manually annotated. It's useful as training/validation supervision for your relation extraction pipeline, though it's not specifically a TF-target benchmark.

### How We Read Papers

Different sections of a paper contain different kinds of evidence, at different confidence levels.

**The key insight:** Results sections contain primary findings. Discussion sections contain speculation. Treating them equally would pollute your graph with low-confidence claims.

```
  WHAT WE EXTRACT FROM EACH SECTION
  ══════════════════════════════════

  RESULTS ────────▶ "FOXA2 directly binds the MUC5B promoter"
                    → primary claim, highest confidence
                    → directness: direct_binding

  METHODS ────────▶ "AT2 cells, ChIP-seq, hg38"
                    → context only (cell type, assay, assembly)
                    → no regulatory claims extracted

  FIGURE CAPTIONS ▶ "Fig 3A: FOXA2 ChIP-seq peaks at MUC5B locus"
                    → evidence claim, high confidence
                    → tied to specific figure panel

  ABSTRACT ───────▶ "FOXA2 regulates MUC5B in IPF"
                    → summary claim, medium confidence
                    → often restates Results more broadly

  DISCUSSION ─────▶ "FOXA2 may coordinate MUC5B and SFTPC"
                    → interpretive, low confidence
                    → "may" = speculation, not evidence

  INTRODUCTION ───▶ "MUC5B is known to be upregulated in IPF (Smith 2015)"
                    → second-hand citation, lowest confidence
                    → go read Smith 2015 instead

  REVIEW ARTICLES ▶ cite many papers, but add no primary data
                    → use for FINDING relevant papers
                    → do NOT use as edge evidence
```

**What the extraction output looks like:**

For each claim we extract from a paper, we capture:

```python
class TFTargetClaim:
    tf_symbol: str              # "FOXA2"
    target_gene_symbol: str     # "MUC5B"
    direction: str              # "activator" | "repressor" | "unknown"
    directness: str             # "direct_binding" | "regulatory_effect" | "unclear"
    cell_type: str | None       # "AT2 cells"
    species: str | None         # "human"
    disease: str | None         # "IPF"
    assay: str | None           # "ChIP-seq"
    pmid: str                   # "28272906"
    source_sentence: str        # exact sentence from paper
    section: str                # "Results" — determines confidence weight
    measured_or_inferred: str   # "measured" | "inferred" | "reported"
```

**Tables and supplements are often MORE valuable than text.** A Results section might say "we identified 150 FOXA2 target genes." The supplementary table has all 150 genes with ChIP-seq peak coordinates and q-values. That table is structured data — much easier to parse than prose.

**Watch out for:**
- **Excel gene name corruption:** Excel auto-converts gene names like MARCH1 and SEPT1 to dates. A common problem in published supplementary gene lists (see [PMID 32346221](https://pubmed.ncbi.nlm.nih.gov/32346221/)). Your pipeline must detect and correct these.
- **Non-standard supplement formats:** Supplements come as CSV, XLSX, PDF tables, Word docs, even PowerPoint. Parse what you can, skip gracefully.

**The precision gate:**

Literature-extracted claims do NOT enter the graph automatically. They must first pass a validation check:

```
  Extract claims from papers
       │
       ▼
  Compare TF→Gene pairs against TRRUST + CollecTRI
       │
  ┌────┴────┐
  ▼         ▼
 >80%      <80%
 precision  precision
  │         │
  ▼         ▼
 Attach    STOP.
 as        Fix your
 Evidence  extraction
 nodes     pipeline.
```

Claims that pass become `Evidence` nodes in the graph. Claims below threshold go into a **sidecar store** — they're kept for later review but don't influence edge confidence scores.

### Why Vision Is Useful but Dangerous

Figures in papers contain real evidence that text sometimes omits: pathway diagrams with TF→Gene arrows, ChIP-seq tracks showing binding peaks, volcano plots showing differential expression. A vision-capable LLM can read these.

**But figure extraction is the NOISIEST evidence source.** Build it last.

```
  FIGURE TYPES AND WHAT TO DO WITH THEM
  ══════════════════════════════════════

  GRN / pathway diagrams ──▶ EXTRACT (TF→Gene arrows)     MEDIUM priority
  ChIP-seq / ATAC tracks ──▶ EXTRACT (binding confirmation) MEDIUM priority
  Perturbation bar plots ──▶ EXTRACT (labeled values)       MEDIUM priority
  Motif logos ─────────────▶ EXTRACT (TF identity)          LOW priority
  Heatmaps ────────────────▶ EXTRACT (relative only)        LOW priority
  Microscopy / histology ──▶ SKIP (not relevant to DPI-KG)
```

**The critical distinction: measured vs schematic.**

A ChIP-seq track in a figure is **measured data** — someone ran an experiment and this is the result. A cartoon pathway diagram is **schematic** — someone drew arrows to illustrate a hypothesis. These are fundamentally different confidence levels:

| Figure Type | Status | Confidence |
|------------|--------|------------|
| ChIP-seq track showing FOXA2 binding at MUC5B locus | **Measured** | Can create/support edge |
| Cartoon showing "FOXA2 → MUC5B → mucus production" | **Schematic** | Reported/inferred only, lower weight |

**Guardrails:**

- Do NOT use vision LLM output as unverified truth for exact quantitative values from plots
- Do NOT infer causality from cartoon diagrams
- Do NOT create high-confidence edges from figure-only claims without text/caption support
- Always cross-validate figure-extracted claims against text claims from the same paper
- A figure-only claim gets `Evidence {source: "figure_vision", measured_or_schematic: "schematic"}` — it exists in the graph but carries low weight

**Why include it at all?** Because some regulatory evidence is ONLY in figures. A paper might show a ChIP-seq track demonstrating FOXA2 binding at the MUC5B promoter in a figure, with the text only saying "we confirmed binding by ChIP-seq (Fig 3A)." If you skip the figure, you miss the positional evidence. If you process only text, you get "confirmed binding" but not where.

---

## Part 12: Why Binding Sites Matter Even in a Gene-Level Graph

The main graph is gene-level: `TF → regulates → Gene`. This is clean, queryable, and what most biologists want to see. But some of the best questions in regulatory biology require knowing **where** on the DNA the regulation happens.

### 12.1 The Dual-Resolution Design

```
GENE-LEVEL (what you query):
    FOXA2 (TF) ──regulates──▶ MUC5B (Gene)

POSITION-LEVEL (why you believe it):
    FOXA2 ──binds_at──▶ RegulatoryLocus (chr11:1219800-1220200, hg38, promoter)
                                │
                         linked_to_gene
                                │
                                ▼
                           MUC5B (Gene)
```

The gene-level edge says "FOXA2 regulates MUC5B." The locus layer says **where** on the genome FOXA2 sits to do this. Both layers exist simultaneously.

### 12.2 Why This Matters: The GWAS Connection

Genome-wide association studies (GWAS) find genetic variants (e.g., SNPs) associated with disease risk. Most disease-associated variants are **noncoding** — they don't change a protein, they change **where a TF can bind**.

Here's a concrete example:

```
Step 1: GWAS finds rs35705950 is strongly associated with IPF risk
        (p-value: 5e-60 — one of the strongest GWAS signals in all of lung disease)
        Location: chr11:1219991 (hg38)

Step 2: This variant falls INSIDE a regulatory locus near MUC5B
        RegulatoryLocus: chr11:1219800-1220200 (MUC5B promoter)

Step 3: FOXA2 binds at this locus
        TF: FOXA2 ──binds_at──▶ this locus

Step 4: The variant potentially disrupts FOXA2's binding motif
        motif_disrupted: true
        disruption_score: 0.85

Step 5: MUC5B is differentially expressed in IPF AT2 cells
        MUC5B ──is_deg_in──▶ DEGSet (IPF, AT2)

Conclusion: The GWAS variant → disrupts TF binding → at a regulatory locus
            → affecting a gene that is DE in disease → in the relevant cell type

This is a complete regulatory mechanism hypothesis, built from graph traversal.
```

**Without the locus layer,** you can say "FOXA2 regulates MUC5B" but you CAN'T answer:
- Does the IPF GWAS variant overlap with where FOXA2 binds?
- Does the variant disrupt FOXA2's binding motif?
- Do different diseases have variants affecting the SAME regulatory locus?

**With the locus layer,** all of these become graph queries.

### 12.3 What DEGs Are (and Are NOT)

Differentially expressed genes (DEGs) are genes whose expression levels change significantly between conditions (e.g., IPF vs. healthy in AT2 cells). They tell you **what changes** in disease.

```
DEGs are:                                DEGs are NOT:
════════                                 ════════════
"MUC5B goes UP in IPF AT2 cells"         "FOXA2 causes MUC5B to go up"
"SFTPC goes DOWN in IPF AT2 cells"       "FOXA2 causes SFTPC to go down"

DEGs tell you WHAT changes.              DEGs don't tell you WHO caused it.
```

In the KG, DEGs are a **contextual overlay** — they annotate genes, but they do NOT create or weight TF→Gene edges. A DEG is a prioritization signal: "focus on TF→Gene edges where the target gene is actually changing in disease."

### 12.4 Drugs in the Network

Some genes are druggable — there exist approved or experimental drugs that target them. When a DEG in the GRN is also druggable, that's a high-value finding:

```
  Drug (nintedanib) ──targets──▶ FGFR1 (:Gene)
                                  │
                                  │ IS_DEG_IN
                                  ▼
                              DEGSet (IPF, AT2)

  AND: some TF ──regulates──▶ FGFR1 (in the GRN)

  = "FGFR1 is regulated by a TF in the AT2 GRN,
     is differentially expressed in IPF,
     and is targetable by nintedanib."
```

Drug-target data comes from DGIdb, Open Targets, or ChEMBL (NOT DrugBank, which is licensed).

---

## Part 13: Glossary — Quick Reference

| Term | Plain English | In the KG |
|---|---|---|
| **Transcription Factor (TF)** | A protein that turns other genes on or off by sitting on DNA | A Gene node with `:TF` label |
| **Target Gene** | The gene being regulated by a TF | A Gene node |
| **Activator** | A TF that turns a gene ON (more expression) | `direction: activator` on InteractionContext |
| **Repressor** | A TF that turns a gene OFF (less expression) | `direction: repressor` on InteractionContext |
| **Co-factor** | A second TF that must be present for regulation to occur | `RegulatoryComplex` node (supports 2-4 TFs) |
| **Motif** | The short DNA sequence pattern a TF recognizes (e.g., CACGTG) | Motif evidence node |
| **ATAC-seq** | Experiment that measures where DNA is open/accessible | Input to ChromLinker/ChromBPNet |
| **ChIP-seq** | Experiment that measures where a specific TF binds DNA | ChIP-seq evidence node |
| **ChromLinker / ChromBPNet** | Lab pipeline: ATAC-seq → predicted TF binding with base-resolution intermediates | Primary edge source. ChromLinker is the framework, ChromBPNet is the underlying model. |
| **Correlation score** | How strongly TF binding predicts gene expression (+/-) | `correlation` on InteractionContext |
| **Promoter** | DNA region right at the gene start where transcription begins | `locus_type: promoter` on RegulatoryLocus |
| **Enhancer** | DNA region far from gene that boosts transcription via DNA looping | `locus_type: enhancer` on RegulatoryLocus |
| **GRN** | Gene Regulatory Network — the full map of who-regulates-whom | The entire knowledge graph |
| **Perturb-seq** | Directly knock out a gene, measure what changes — gold standard causal evidence | Validation evidence |
| **TRRUST / CollecTRI** | Curated databases of known TF→Gene interactions (TRRUST is human-only) | Gold standard for validation/training |
| **InteractionContext** | A specific observed instance of a regulatory relationship in a given cell/disease/species | InteractionContext node linked via `:HAS_CONTEXT` |
| **Disease context** | The disease in which the interaction is relevant (e.g., IPF) | `disease` property on InteractionContext (MONDO ID) |
| **Developmental stage** | Whether the interaction is from embryonic, postnatal, or adult biology | `dev_stage` property on InteractionContext |
| **Species** | Whether the interaction was observed in human, mouse, or both | `species` property on InteractionContext (NCBITaxon ID) |
| **RegulatoryLocus** | A specific genomic position where a TF binds (binding site / peak / seqlet) | `RegulatoryLocus` node with `chr`, `start`, `end`, `assembly` |
| **Variant** | A genetic variant (SNP, indel) at a specific genomic position | `Variant` node with rsID or chr:pos:ref:alt, `assembly` |
| **GWAS** | Genome-Wide Association Study — finds variants linked to disease risk | `GWASAssociation` node linked from Variant |
| **DEGSet** | A set of differentially expressed genes in a disease/cell-type context | `DEGSet` node — overlay, NOT edge evidence |
| **Drug** | A compound that targets a specific gene/protein | `Drug` node from DGIdb/ChEMBL/Open Targets |
| **Genome assembly** | The reference genome version coordinates are based on (hg38, mm10, etc.) | `assembly` property on RegulatoryLocus and Variant — **mandatory** |
| **BOND** | Lab-developed automated ontology harmonization system (in review) | Maps cell-type labels to standardized CL/EFO IDs using biological context |
| **Dual-resolution** | Gene-level GRN for querying + position-level loci for variant/GWAS queries | The architecture design principle |
| **PubMed** | NCBI database of ~37M biomedical article abstracts and metadata | Source for Tier 3 (abstract-only) papers |
| **PMC (PubMed Central)** | NCBI repository of ~8M full-text biomedical articles (XML + PDF + figures + supplements) | Source for Tier 1-2 papers; JATS/XML enables structured section extraction |
| **PubTator Central** | NCBI service with pre-annotated gene/disease/species/mutation NER on all of PubMed | Use instead of building gene NER from scratch |
| **BioRED** | NCBI dataset of ~600 articles with manually annotated biomedical relations | Training/validation supervision for relation extraction (not a TF-target benchmark specifically) |
| **Docling** | Document conversion tool supporting PDF layout detection, table extraction, image extraction, and OCR | Used as fallback when PMC JATS/XML is not available |
| **GTEx** | Genotype-Tissue Expression project — measures gene expression across 54 human tissues | Source for eQTL data |
| **eQTL** | Expression Quantitative Trait Locus — a genetic variant that correlates with gene expression in a specific tissue | Strengthens `LINKED_TO_GENE` edges with `link_method: eQTL` |
| **Evidence sidecar** | Storage for claims that fail the precision gate — kept for review but do not influence graph confidence | Prevents low-quality literature from polluting edge scores |
| **Precision gate** | Validation requirement: literature extraction must achieve >80% precision against TRRUST/CollecTRI before claims enter the graph | Quality control for the literature pipeline |
| **Section-aware extraction** | Treating different paper sections at different confidence levels (Results > Abstract > Discussion) | Prevents speculative claims from carrying equal weight to experimental findings |
