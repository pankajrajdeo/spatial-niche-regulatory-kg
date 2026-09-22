# Gene Regulation & DPI Knowledge Graph — From Absolute Zero

> **Final teaching guide.** The biological basics are unchanged, but the KG sections now match the finalized provenance-first schema: motif-family predictions are separated from TF-specific occupancy, context is shared/normalized, binding and locus→gene links are observations, evidence is experiment-traceable, DE uses explicit contrasts, and scores are versioned ranking/predictive outputs rather than unexplained probabilities of truth.

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
- Some TFs form canonical or context-specific complexes, but co-occurrence does not automatically prove that every member is mechanistically required at every target locus.
- Sid's old concatenation approach (`"MYC_MAX"`) is fragile because it destroys the identity and reuse of the individual TFs.
- The final KG keeps a canonical `RegulatoryComplex` entity and, when needed, a locus/context-specific `ComplexObservation` describing where joint occupancy or functional requirement was actually observed.
- Requirement is represented biologically (`obligate`, `facilitating`, `competitive`, `unknown`) rather than as a simplistic global Boolean AND/OR rule.

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

## Part 6: ChromLinker/ChromBPNet — From ATAC-seq to Regulatory Candidates

### 6.1 What ChromBPNet Actually Gives You

ATAC-seq tells you **where chromatin is accessible**. ChromBPNet learns sequence features that predict that accessibility and can highlight sequence patterns/seqlets that matter in a particular trained context.

The important correction is this:

```text
ChromBPNet attribution / seqlet
        ↓
sequence motif or motif family
        ↓
candidate TF family / compatible paralogs
```

It does **not automatically prove that one specific TF paralog is physically occupying that site**.

Example:

```text
DNA sequence contains a forkhead-like motif
        ↓
sequence model says this motif contributes to accessibility
        ↓
Candidate binder family: FOX / forkhead
        ↓
FOXA1? FOXA2? another forkhead TF?
```

To name a specific TF such as FOXA2, add evidence that resolves the paralog — for example TF expression in the context and ideally TF-specific ChIP-seq, CUT&RUN, or CUT&Tag.

That is why the final graph has both `Motif`/`MotifFamily` and TF-specific `BindingObservation` nodes.

### 6.2 The Final Regulatory-Candidate Pipeline

```text
Step 1: ATAC-seq / chromatin data in Cell Context X
        → which regulatory loci are active/open?

Step 2: ChromBPNet / sequence attribution
        → which sequence motifs/families help explain the accessibility?
        → write predicted, family-level binding observations when TF identity is unresolved

Step 3: Resolve candidate TF identity where possible
        → is the TF expressed in this context?
        → is there TF-specific ChIP/CUT&RUN/CUT&Tag evidence?

Step 4: Link the regulatory locus to a target gene
        → promoter identity, ABC/rE2G, chromatin contact, colocalized QTL, or CRE perturbation
        → do NOT assume “nearest gene” is the mechanism

Step 5: Ask whether TF activity/binding and target expression are associated
        → correlation is an R1 regulatory-effect signal, not causal proof

Step 6: Add perturbation evidence
        → if perturbing the TF changes the target, that is stronger R-axis evidence
        → but a downstream change can still be indirect unless binding + locus→gene evidence also support directness
```

The lab's ChromLinker framework can integrate these modalities and propose TF→Gene candidates, but the **KG does not convert every candidate directly into a fact**. It stores the candidate proposition plus the observations and evidence that justify it.

### 6.3 Correlation Is Not Directional Proof

A signed correlation is useful, but it is an observation:

```text
positive correlation:
TF-related accessibility/binding signal ↑
target expression ↑

negative correlation:
TF-related accessibility/binding signal ↑
target expression ↓
```

This can contribute to a direction posterior, but it does not by itself mean:

```text
positive = proven activator
negative = proven repressor
```

The final `ContextualStatement` therefore keeps direction as something like:

```text
p(activating)
p(repressing)
p(no_effect)
epistemic uncertainty / unresolved evidence
```

and preserves which evidence type produced each sign.

### 6.4 Cell Context Still Matters

The same canonical TF→Gene proposition can have very different support in different contexts. What changes is not only one score — the **binding, locus activity, locus→gene assignment, perturbation evidence, and direction can all differ**.

This is why the final graph separates a reusable `BiologicalContext` from the per-interaction `ContextualStatement`.

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

The final DPI-KG does not have one vague “edge requirement.” It asks three separate mechanistic questions:

```text
B — BINDING:
Does this specific TF (or at least its motif family) occupy a regulatory locus?
Measured ChIP/CUT&RUN is stronger than motif/sequence-model support.

L — LOCUS→GENE:
Why is this regulatory locus assigned to this target gene?
Promoter identity, ABC/rE2G, chromatin contact, colocalization, or CRE perturbation
are different strengths of evidence.

R — REGULATORY EFFECT:
Does changing the TF actually change the target gene?
Correlation is weaker than perturbation evidence.
```

Only compatible combinations of B + L + R justify a **direct-regulation** class.

```text
❌ co-expression alone is not direct regulation
❌ pathway co-membership is not regulation
❌ motif presence is not TF occupancy
❌ ChIP binding alone is not regulatory effect
❌ TF perturbation effect alone may be indirect
❌ literature co-mention is not biology
```

---

## Part 9: The Evidence Sources — What Each One Actually Means

The final design groups sources by the biological question they answer. The most important rule is: **a database name is not an independent experiment.** Several public ChIP resources can contain/reprocess the same GEO/SRA/ENCODE experiment, so independence is counted by the underlying experiment/study.

| Source / modality | What it tells you | Final KG role |
|---|---|---|
| **ChromLinker / ChromBPNet** | Context-specific accessibility/sequence attribution and candidate regulatory links | Predicted binding/locus/regulatory observations; motif-family-level where TF identity is unresolved |
| **CistromeDB / ChIP-Atlas** | Measured TF/chromatin peaks from public experiments | `BindingObservation` / locus activity with experiment provenance |
| **UniBind** | Motif-supported high-stringency ChIP-derived binding | Strong processing of a parent ChIP experiment; not automatically an independent experiment |
| **JASPAR** | TF DNA motif definitions | `Motif` / `MotifFamily`; plausibility, not occupancy |
| **TF census / TFClass** | Which genes are TFs and which sequence families they belong to | TF identity/taxonomy and paralog ambiguity |
| **Lung expression / ATAC atlases** | Which TFs/genes are expressed and which loci are active in lung contexts | `ExpressionObservation` + `LocusActivityObservation` |
| **ABC / ENCODE rE2G / chromatin contacts** | Candidate enhancer→gene links | `LocusGeneLink` with method/context/tier |
| **CRISPRi/CRISPRa CRE perturbation** | Does perturbing the regulatory element affect the gene? | Strong L3 locus→gene validation |
| **Perturb-seq / TF perturbation** | Does perturbing the TF change the gene? | `PerturbationEffectObservation`; strong regulatory-effect evidence but not automatically direct |
| **TRRUST / CollecTRI / DoRothEA** | Curated TF-target knowledge | Validation/baseline block; publication-resolved assertions may enter scoring only under leakage-safe evaluation |
| **PubMed / PMC** | Published direction/directness/context claims | Secondary `EvidenceAssertion` after manual QC gate |
| **PubTator Central** | Pre-annotated biomedical entities | Extraction utility, not evidence |
| **GWAS Catalog / Open Targets** | Variant-trait studies, credible sets, coloc resources | GWAS/credible-set provenance and disease genetics |
| **GTEx / eQTL Catalogue** | Variant→expression QTLs | QTL/colocalization evidence; eQTL overlap alone is not proof of target assignment |
| **ENCODE SCREEN / project cCRE registry** | Stable candidate regulatory-element coordinates | `RegulatoryLocus` registry; registry presence is not activity in every context |
| **caQTL / allele-specific ATAC/ChIP** | Whether an allele changes locus activity or occupancy | `AllelicEffectObservation` |
| **BioGRID / CORUM / Complex Portal** | Protein interaction / canonical complexes | Co-factor/complex support; PPI alone does not prove joint regulation at one locus |
| **DGIdb / ChEMBL / Open Targets drugs** | Druggability / pharmacological relations | Optional application layer, not core regulation evidence |

### The provenance rule

Suppose the same MYC ChIP experiment appears in ChIP-Atlas, CistromeDB, and UniBind.

Wrong interpretation:

```text
3 databases support MYC binding → 3 independent pieces of evidence
```

Correct interpretation:

```text
1 biological experiment
  ├─ processed by ChIP-Atlas
  ├─ processed by CistromeDB
  └─ motif-filtered by UniBind

= one experimental provenance unit, several analysis assertions
```

That is why the final KG has:

```text
EvidenceAssertion → AnalysisRun
                    ├─ USES_EXPERIMENT → Experiment → Study → Publication   [experimental]
                    └─ REPORTED_IN → Publication                             [literature/curated]
```

---

## Part 10: The Knowledge Graph — Putting It All Together

### 10.1 The Most Important Mental Model

The final KG separates **things**, **propositions**, **observations**, and **evidence**.

```text
BIOLOGICAL THINGS:
MYC, BCL2, a regulatory locus, a variant, a biological context

PROPOSITION:
“MYC directly regulates BCL2 somewhere”
        = RegulatoryInteraction

CONTEXT-SPECIFIC STATEMENT:
“What is actually supported in A549?”
        = ContextualStatement

OBSERVATIONS:
MYC occupancy at locus
locus active in A549
locus linked to BCL2
MYC perturbation changes BCL2
        = BindingObservation / LocusActivityObservation /
          LocusGeneLink / PerturbationEffectObservation

EVIDENCE:
which database processing, experiment, study, publication, statistic?
        = EvidenceAssertion + provenance spine
```

This avoids prematurely turning predictions into facts.

### 10.2 A Single Interaction, Fully Illustrated

Use MYC → BCL2 as a schematic example. The exact numerical values below are illustrative; the point is the schema.

```text
MYC (:Gene:TF)
      │
REGULATES_VIA
      ▼
RegulatoryInteraction ──TARGETS──▶ BCL2 (:Gene)
      │
HAS_STATEMENT
      ▼
ContextualStatement
  B tier = measured binding support
  L tier = promoter/locus→gene support
  R tier = perturbation/correlation support
  p_activating / p_repressing / p_no_effect
  epistemic_uncertainty
  edge_class = derived from B/L/R
      │
IN_CONTEXT
      ▼
BiologicalContext
  human / A549 / cell_line / lung-derived / NSCLC
```

Then the supporting observations:

```text
MYC ──BINDER_IN──▶ BindingObservation ──AT_LOCUS──▶ RegulatoryLocus
                              │
                          IN_CONTEXT

LocusActivityObservation ──OF_LOCUS──▶ RegulatoryLocus
            │
        IN_CONTEXT

LocusGeneLink ──FROM_LOCUS──▶ RegulatoryLocus
      └───────TO_GENE───────▶ BCL2
      └───────IN_CONTEXT────▶ same/compatible context

PerturbationEffectObservation
      ├──PERTURBED_TF──▶ MYC
      ├──AFFECTS_GENE──▶ BCL2
      └──IN_CONTEXT────▶ context
```

Each observation has evidence assertions that trace back to the exact analysis and experiment.

### 10.3 Why There Is No Bare `base_confidence`

The old design tried to store:

```text
base_confidence = 0.92
context_confidence = 0.87
```

as if those were universal probabilities that the biology is true.

The final design instead gives you two things:

1. **transparent evidence tiers** — B (binding), L (locus→gene), R (regulatory effect), and
2. a **versioned ranking/predictive score** in `ConfidenceScore`, with explicit `score_type`, prediction target/endpoint, calibration status, model version, feature snapshot, uncertainty, and code commit.

That makes “why is this ranked 0.81?” answerable.

### 10.4 Shared BiologicalContext vs. ContextualStatement

A `BiologicalContext` is reused across many interactions. Its identity is based on stable biology (species, system type, cell type/cell line, tissue, disease, developmental stage, resolution); treatment, dose, time, genotype, perturbation, sex, and donor/cohort remain observation/analysis dimensions rather than changing the shared context ID:

```text
BiologicalContext:
  species = human
  system_type = primary_cell
  cell_type = AT2
  tissue = lung
  disease = IPF
```

Many regulatory statements can point to this same node.

A `ContextualStatement` is the interaction-specific claim:

```text
FOXA2 → target X in this context
MYC   → target Y in this context
NKX2-1→ target Z in this context
```

This is cleaner than minting an “InteractionContext” node that duplicates the same context vocabulary for every TF-target pair.

### 10.5 Co-Factors

Keep canonical complexes as entities, but do not reduce biology to `AND/OR`.

```text
MYC ──MEMBER_OF{role}──▶ MYC:MAX complex
MAX ──MEMBER_OF{role}──▶ MYC:MAX complex

ContextualStatement ──MEDIATED_BY──▶ complex
```

When locus/context-specific co-occupancy is represented, use `ComplexObservation`.

### 10.6 The B / L / R Definition of “Direct”

To say a TF **directly regulates** a target, answer three separate questions:

```text
B: does the TF actually occupy a regulatory locus?
L: is that locus credibly linked to the target gene?
R: does perturbing/regulating the TF affect the target?
```

Examples:

- motif only + nearest gene + correlation = **candidate**, not direct regulation.
- measured TF occupancy at a promoter + TF perturbation effect = strong promoter-direct evidence.
- measured TF occupancy at a distal enhancer + ABC/contact/coloc/CRISPRi link + perturbation effect = strong distal-direct evidence.
- TF perturbation effect without binding = `EFFECT_ONLY`, potentially indirect.

This is the core semantic contract of the final KG.

---

## Part 11: The Complete Pipeline

### The One-Line Summary

```text
normalize IDs/context → deduplicate experiments → register loci → measure context activity/expression
→ ingest measured binding → add motif-family predictions → build locus→gene links
→ load designated perturbation-effect evidence while reserving gold sets
→ benchmark/mask before scoring → add disease genetics/DE → test perturbation utility
→ add literature after manual QC → complete the remaining final capabilities
```

### The Full Pipeline

The project has **one final architecture**. The sequence below is only the recommended build order; it does not define separate schema phases or versions.

```text
STEP 1 — FOUNDATION
final schema + Ensembl/ontology IDs + BOND
Experiment/Study/Publication registry
Crosswalk Cistrome/ChIP-Atlas/UniBind/GTRD accessions
RegulatoryLocus registry

STEP 2 — CONTEXT + MEASURED BIOLOGY
Lung expression observations
Locus activity observations
Measured ChIP/CUT&RUN/CUT&Tag binding observations
Motif / TFClass taxonomy

STEP 3 — PREDICTED BINDING + LOCUS→GENE
ChromBPNet/ChromLinker predictions
  → motif-family-level when TF identity unresolved
ABC/rE2G/promoter/contact links
CRISPRi enhancer-gene benchmark
Designated perturbation-effect observations for model features/training
Reserve separate perturbation datasets as untouched gold sets

STEP 4 — EVALUATION BEFORE SCORING
Experiment/publication leakage audit
Popularity-only baseline
Held-out TF / TF-family / target / study / context tests
Orthogonal perturbation and CRE-perturbation gold sets
For every fold: mask held-out gold observations first, then recompute B/L/R and feature snapshots

STEP 5 — RANKING MODEL
B/L/R tiers per ContextualStatement
Experiment-deduplicated ranking/predictive model
Append-only ConfidenceScore with score semantics + uncertainty + model provenance

STEP 6 — DISEASE GENETICS + EXPRESSION
GWASStudy + GWASAssociation + CredibleSet/PIP
Variant ↔ RegulatoryLocus overlap
DEAnalysis with explicit IPF-vs-control contrasts
QTL/colocalization/allelic-effect observations

STEP 7 — DOWNSTREAM UTILITY
Perturbation prediction with/without DPI-KG prior
Cross-context transfer
Variant-aware mechanistic-hypothesis ranking

STEP 8 — LITERATURE
Gene-seeded PubMed/PMC corpus
Section-aware text/table/supplement extraction
Manual field-level QC gate
Accepted claims → typed EvidenceAssertion
Rejected/uncertain claims → sidecar store

STEP 9 — COMPLETE FINAL CAPABILITIES
Complex observations
Cross-species conservation
Prospective validation
Drug overlay
Agent / NL interface
```

### How We Choose Papers

Not all papers are worth processing. Use a focused gene-seeded corpus rather than whole-PubMed ingestion.

**Retrieval strategy:**

1. **SEED:** query TF-target pairs from the candidate network with regulation/ChIP/perturbation terms.
2. **EXPAND:** forward/backward citations from high-value seed papers.
3. **DB-LINKED:** publications referenced by curated resources and the exact experiments already present in the provenance registry.

**Triage dimensions:** domain relevance, regulatory relevance, primary-data strength, asset availability, and publication trust/retraction status.

Recommended tiers:

- **Tier 0:** manually curated gold/QC papers.
- **Tier 1:** full text + tables/supplements; figures only when a measured panel contains otherwise-unavailable positional evidence.
- **Tier 2:** text/tables/captions.
- **Tier 3:** abstract/metadata only.
- **Reject:** irrelevant, retracted, editorial, or vague association-only content.

Use **PubTator Central** for basic entity recognition/normalization rather than rebuilding NER. **BioRED** may help relation-extraction development but is not the final TF-target benchmark.

### How We Read Papers

```text
Results        → primary findings; strongest text evidence
Methods        → assay/context/assembly; usually not regulatory claims
Figure captions→ useful measured evidence descriptors
Abstract       → summary claims; moderate confidence
Discussion     → interpretation/speculation; lower confidence
Introduction   → background/secondary claims
Reviews        → paper discovery; not primary edge evidence
```

For each extracted claim, retain at least:

```python
class TFTargetClaim:
    tf_symbol: str
    target_gene_symbol: str
    direction: str              # activator | repressor | dual | unknown
    directness: str             # direct_binding | regulatory_effect | correlational | unclear
    cell_type: str | None
    tissue: str | None
    species: str | None
    disease: str | None
    assay: str | None
    pmid: str
    source_sentence: str
    section: str
    extraction_confidence: float
    claim_status: str           # measured | inferred | reported | schematic
```

Tables/supplements often contain the most useful coordinates, perturbation results, and full gene lists. Parse structured files directly where possible, detect Excel gene-name corruption, and skip unsupported formats gracefully.

### The Literature QC Gate

Do **not** use one “>80% agreement with TRRUST” number as the gate.

Instead:

1. Create a held-out manually double-annotated sample.
2. Measure relation existence, direction, directness, cell/tissue context, species, and measured-vs-inferred separately.
3. Report precision with confidence intervals and annotator agreement.
4. Choose a high-precision operating threshold for scoring.
5. Keep rejected/uncertain claims in the sidecar store.
6. Require PMID/provenance so evaluation publications can be excluded from training features.

### Figure / Vision Extraction

Default recommendation: **defer it and exclude it from scoring**. Use vision only for a small Tier-0 set when a measured panel contains otherwise-unavailable information. Never let a cartoon pathway diagram become a direct-regulation claim.

---

## Part 12: Why Binding Sites Matter Even in a Gene-Level Graph

The dual-resolution idea remains one of the most important parts of DPI-KG. The update is that **binding, locus activity, and locus→gene assignment are context-specific observations rather than global edges**.

### 12.1 The Dual-Resolution Design

```text
GENE LEVEL — proposition you query:
FOXA2 ──REGULATES_VIA──▶ RegulatoryInteraction ──TARGETS──▶ MUC5B

POSITION / OBSERVATION LEVEL — why you might believe it:
FOXA2 or MotifFamily ──BINDER_IN──▶ BindingObservation ──AT_LOCUS──▶ RegulatoryLocus
LocusActivityObservation ─────────▶ RegulatoryLocus
LocusGeneLink ──FROM_LOCUS────────▶ RegulatoryLocus ──TO_GENE──▶ MUC5B

all observations ──IN_CONTEXT──▶ relevant BiologicalContext
```

The gene-level proposition is clean for network queries. The observation layer explains **where, in which context, and with what evidence** the proposition is supported.

### 12.2 The GWAS Connection — Overlap Is Only Step 1

A disease-associated variant can affect regulatory biology in several ways. Do not assume every noncoding variant simply “breaks the TF motif.”

```text
CredibleSet
    │ PIP
    ▼
Variant
    │
    ├── OVERLAPS ─────────────▶ RegulatoryLocus        # geometric fact
    │                              │
    │                              ├─ active in context?       # locus activity observation
    │                              ├─ allele changes activity?  # caQTL/asATAC/prediction
    │                              ├─ TF occupancy?             # binding observation
    │                              └─ linked to which gene?     # LocusGeneLink
    │
    └── GWASAssociation / study provenance
```

Only after those links are evaluated should the system assemble a **mechanistic hypothesis**.

For a strong hypothesis, prefer:

1. fine-mapped credible-set membership rather than index-SNP-only overlap;
2. locus activity in the disease-relevant cell/tissue context;
3. allelic effect on accessibility/binding/activity when available;
4. specific measured TF occupancy, or explicit motif-family uncertainty;
5. a strong locus→gene link, especially for distal elements;
6. disease expression as an association/prioritization overlay, not causal evidence.

### 12.3 The MUC5B / rs35705950 Example — Use It Honestly

The final graph should **not pre-encode** the simplistic story:

```text
rs35705950 → directly disrupts FOXA2 motif → FOXA2 causes MUC5B in AT2 → IPF
```

Instead it should be able to represent:

```text
rs35705950 is associated with IPF
        ↓
variant/credible-set evidence
        ↓
regulatory region near MUC5B
        ↓
context-specific accessibility / epigenetic effects
        ↓
FOXA2 or forkhead-family occupancy evidence near the locus
        ↓
MUC5B linkage/expression evidence
        ↓
multiple epithelial compartments + competing mechanisms + unresolved causal step
```

That is a **better** flagship example because it demonstrates that the KG can preserve uncertainty and competing mechanisms rather than force a clean story.

### 12.4 Differential Expression — What Changes, Not Who Caused It

The old `DEGSet` is replaced by an explicit `DEAnalysis`:

```text
DEAnalysis
  case_context    = IPF AT2 (or another explicit compartment)
  control_context = control matched compartment
  assay/pipeline
  sample counts/covariates

Gene ──DE_IN{logFC, q, tested}──▶ DEAnalysis
```

A gene can be differentially expressed and still provide **zero evidence** about which TF caused the change. This rule is structural: DE results do not point to `RegulatoryInteraction` as support.

### 12.5 Drugs

Druggability remains useful but is not part of the core regulatory evidence layer. Query Open Targets/ChEMBL/DGIdb externally first. If drug relations are materialized, preserve mechanism/action type rather than a vague `Drug TARGETS Gene` edge.

---

## Part 13: Glossary — Quick Reference

| Term | Plain English | In the final KG |
|---|---|---|
| **Transcription Factor (TF)** | A gene/protein capable of sequence-specific transcriptional regulation | Species-scoped `Gene` node with `:TF` label and TF-census provenance |
| **Motif** | DNA sequence pattern compatible with a TF/family | `Motif` node |
| **MotifFamily / TFClass** | Group of TFs with related DNA-binding specificity | Makes paralog ambiguity explicit; links to candidate TFs |
| **ATAC-seq** | Measures accessible/open chromatin | Produces `LocusActivityObservation`; input to ChromBPNet |
| **ChIP-seq / CUT&RUN / CUT&Tag** | Measures occupancy of a specific TF/protein | `BindingObservation` with experiment provenance |
| **ChromBPNet** | Sequence model for bias-corrected accessibility and sequence attribution | Predicted locus/motif-family evidence; not automatically a specific-TF binding fact |
| **ChromLinker** | Lab integration framework for regulatory candidates | Versioned analysis producing candidate observations/propositions |
| **RegulatoryInteraction** | Canonical proposition that TF X directly regulates Gene Y in some context | Context-free proposition node |
| **BiologicalContext** | Reusable biological situation | Species, system type, cell type, tissue, disease, developmental stage, resolution |
| **ContextualStatement** | What is supported for one interaction in one context | B/L/R tiers, edge class, direction posterior, status, coherence |
| **BindingObservation** | A measured/predicted binder at one locus in one context | TF-specific if measured/resolved; MotifFamily-level if unresolved |
| **LocusActivityObservation** | Whether a regulatory locus is active/open in a context | ATAC/DNase/histone observation |
| **LocusGeneLink** | Evidence-backed assignment from regulatory element to gene | promoter / ABC / rE2G / contact / coloc / CRISPRi tiers |
| **PerturbationEffectObservation** | What happens to a target after perturbing the TF | R-axis evidence; may still be indirect |
| **B/L/R tiers** | Binding / locus-link / regulatory-effect evidence strengths | Transparent directness classification on `ContextualStatement` |
| **Direction posterior** | Probabilities/uncertainty for activating, repressing, no effect, unresolved | Replaces a single overconfident direction field |
| **EvidenceAssertion** | One typed source/run claim supporting/refuting an observation | Links to provenance; carries native statistic and measured/predicted status |
| **AnalysisRun** | One pipeline/database processing of data | Prevents analysis source from being confused with the experiment |
| **Experiment** | Underlying measured dataset | Deduplication unit across ChIP aggregators |
| **Study / Publication** | Experimental/publication provenance | Used for independence and leakage-safe splits |
| **ConfidenceScore** | Versioned learned ranking/prediction | Stores score, uncertainty, model/features/training/calibration/code versions |
| **RegulatoryLocus** | Stable genomic regulatory coordinate | Registry-anchored `chr/start/end/assembly`; raw peaks stay outside graph |
| **Variant** | Normalized genomic variant | Primary key `assembly:chr:pos:ref:alt`; rsID as alias |
| **CredibleSet** | Fine-mapped group of plausible causal variants | Variant membership carries PIP |
| **AllelicEffectObservation** | Evidence that an allele changes locus activity/binding/etc. | variant-mechanism layer |
| **GWASAssociation** | Study-specific variant–trait association | Includes effect allele/statistics and study provenance |
| **DEAnalysis** | Explicit case-vs-control differential-expression analysis | Gene `DE_IN` result; never TF-edge evidence |
| **RegulatoryComplex** | Canonical TF/cofactor complex | Context/locus-specific requirement uses `ComplexObservation` |
| **Genome assembly** | Reference coordinate system | Mandatory on coordinate-bearing objects |
| **BOND** | Lab ontology harmonization system | Normalizes cell/system labels; raw labels + BOND version retained |
| **UBERON / CL / MONDO / NCBITaxon / Cellosaurus** | Anatomy/cell/disease/species/cell-line vocabularies | Shared context normalization |
| **PubTator Central** | Pre-annotated biomedical entity recognition | Extraction utility, not evidence |
| **BioRED** | Biomedical relation dataset | Optional extraction-model supervision, not TF-target gold standard |
| **Evidence sidecar** | Store for sub-threshold/uncertain assertions | Preserves information without letting it drive final scores |
| **Dual-resolution** | Gene-level proposition + locus-level observations | Core architecture principle |

