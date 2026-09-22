Yes. With the way you are now framing it, I would stop thinking of DPI-KG as an independent project.
Think of the overall project as:
Spatial NicheLinker is the biological/methodological project. DPI-KG is the regulatory knowledge-graph infrastructure inside Spatial NicheLinker that helps explain why neighborhood-defined cell states have different transcription-factor regulatory programs.
That framing makes the whole thing much easier to understand, and it also makes your contribution much more coherent.

1. First, forget the KG for a minute. What biological question are they actually asking?
Start at the simplest possible level.
Imagine two cells that are both officially classified as AT1 cells.
Cell A is surrounded by:
AT2 cells
capillary cells
alveolar fibroblasts
macrophages
Cell B is surrounded by:
basal cells
RASC cells
multiciliated cells
injury-associated epithelial cells
They are both AT1 cells.
But their environments are completely different.
The central biological question is:
Does living in a different cellular neighborhood correspond to the same type of cell entering a different molecular and regulatory state?
That is the entire project.
And there are progressively deeper versions of that question:
LEVEL 1
Are the neighborhoods different?

        ↓

LEVEL 2
Are the AT1 cells themselves expressing
different genes?

        ↓

LEVEL 3
Are different transcription factors
and regulatory DNA programs controlling
those genes?

        ↓

LEVEL 4
What biological mechanisms explain
those differences?

        ↓

LEVEL 5
Which of those proposed TF → gene
mechanisms are already supported by
previous experiments and literature?
Spatial NicheLinker handles primarily Levels 1–3.
Your KG becomes extremely valuable at Levels 3–5.

2. Why should the neighborhood affect the cell at all?
A cell is not an isolated object.
Cells constantly receive signals from surrounding cells.
A neighboring macrophage might release a cytokine.
A fibroblast might alter extracellular matrix composition.
An epithelial cell might produce a growth factor.
The AT1 cell receives these signals through receptors.
Then signaling pathways inside the cell become activated.
Eventually those pathways influence transcription factors.
And transcription factors change which genes are expressed.
Conceptually:
NEIGHBORING CELL
       │
       │ signal
       ▼
Receptor on AT1 cell
       │
       ▼
Intracellular signaling
       │
       ▼
Transcription factor activity
       │
       ▼
DNA regulatory elements
       │
       ▼
Target genes
       │
       ▼
Cellular state / behavior
That is why the neighborhood can matter.
The project is basically trying to connect:
OUTSIDE THE CELL
Who surrounds the cell?

        ↓

INSIDE THE CELL
What genes are expressed?

        ↓

REGULATORY MECHANISM
What TFs and regulatory DNA produced
that expression state?

3. What exactly is a transcription factor?
This is the part you need to understand very clearly for the KG.
DNA contains genes.
A gene can be transcribed into RNA:
DNA
 ↓ transcription
RNA
 ↓ translation
Protein
But cells don't express every gene equally.
Something has to control which genes are active.
One important class of controllers is transcription factors, or TFs.
A transcription factor is a protein that can recognize regulatory DNA and participate in controlling transcription.
Simplified:
                    TF
                    ↓
DNA ───── enhancer ───── promoter ───── GENE
                                  ↓
                                 RNA
Some TFs tend to activate transcription.
Some repress transcription.
Many behave differently depending on partner proteins, regulatory elements and cellular context.
So an important biological relationship looks like:
TF X
  │
  │ regulates
  ▼
Gene Y
A collection of these relationships is a:
Gene Regulatory Network
or GRN.
Your final DPI architecture already treats this correctly: a GRN is not simply "genes that correlate." A regulatory proposition needs to distinguish physical occupancy, enhancer/gene assignment, regulatory effect and biological context. dpi_knowledge_graph_architectur…

4. Why isn't TF → Gene a simple edge?
This is probably the single most important thing for you to understand.
Suppose someone tells you:
XBP1 regulates Gene Y.
Your computer-science instinct might be:
(XBP1)-[:REGULATES]->(GeneY)
Done.
Biologically, that is dangerous.
There are actually three different questions.
Your DPI design calls them B, L and R. dpi_first_principles(1)
B = BINDING
Did TF X actually bind regulatory DNA?

L = LOCUS → GENE
Does that piece of DNA actually regulate Gene Y?

R = REGULATORY EFFECT
If X changes, does Y actually change?
Consider the following.
You find an XBP1 motif in an enhancer.
That tells you:
XBP1 or a related TF might be capable of binding there.
It does not prove XBP1 is actually there.
Then suppose ChIP-seq shows XBP1 physically occupying that region.
Better.
But you still don't know whether that enhancer controls Gene Y.
Maybe it controls Gene Z 200 kb away.
So you need evidence linking the enhancer to Y.
Then even after showing:
XBP1 binds enhancer
enhancer connects to Y
you still haven't proven XBP1 changes Y.
A perturbation experiment might finally show:
Knock down XBP1
        ↓
Gene Y decreases
Now the mechanism is much stronger.
Hence:
TF
 │
 │ BINDING
 ▼
Regulatory DNA locus
 │
 │ LOCUS→GENE
 ▼
Target gene
 │
 │ REGULATORY EFFECT
 ▼
Expression changes
This is why your existing DPI-KG architecture is actually very appropriate for this project.

5. Now put Spatial NicheLinker back into the picture
Spatial NicheLinker starts somewhere completely different.
It starts with geometry.
Imagine Xenium gives you something like:
Cell ID     Cell type      X      Y
------------------------------------
C001        AT1           14.2   19.6
C002        AT2           14.8   20.1
C003        Capillary     13.9   18.9
C004        Fibroblast    15.1   19.7
...
For every AT1 cell, Spatial NicheLinker asks:
Who lives around you?
So AT1 cell A becomes:
AT2             4
Capillary       6
Fibroblast      2
Macrophage      1
Basal           0
RASC            0
and AT1 cell B:
AT2             0
Capillary       1
Fibroblast      1
Macrophage      2
Basal           4
RASC            3
Multiciliated   3
Repeat that for thousands of AT1 cells.
Now cluster using the neighborhood composition, not the AT1 cell's gene expression.
That produces something like:
                    All AT1 cells
                         │
                    neighborhood
                     clustering
                    /           \
                   /             \
             Niche 1           Niche 2

          alveolar-like       remodeling/
          neighborhood        airway-like
This independence is important.
You did not say:
These AT1 cells express differently, therefore let's call them Niche 2.
You first said:
These AT1 cells physically live in different environments.
Then afterward you asked whether their expression differs.
That makes the result considerably more convincing.

6. And in your actual data, it does differ
Your draft already gives a strong AT1 example.
Niche 1 is predominantly associated with an alveolar environment:
AT2
capillary
alveolar fibroblast
Niche 2 is more associated with:
RASC
basal
multiciliated
transitional epithelial
secretory populations
Then you independently examine focal AT1 expression.
Niche 1 has more alveolar-associated features.
Niche 2 has features including things such as:
SCGB3A2
MMP7
CD44
KRT15
XBP1
HSPA5
with injury/remodeling, stress and airway-associated biology.
So now you have:
Different neighborhood
        +
Different transcriptional state
But that still doesn't tell you why.
That is where regulation enters.

7. The problem created by dissociation
This is the clever part of Spatial NicheLinker.
Xenium gives you:
gene expression
+
physical location
But a single-cell multiome experiment typically gives you:
RNA expression
+
chromatin accessibility
while losing:
physical location
because the tissue has been dissociated.
So with the multiome cell, you don't know:
Was this particular AT1 cell surrounded by capillaries?
or:
Was it sitting beside basal/RASC cells?
That information disappeared.
Spatial NicheLinker uses a bridge.
It learns:
Spatial Niche 1 AT1
        ↓
expression signature A

Spatial Niche 2 AT1
        ↓
expression signature B
and then searches the multiome dataset:
Which AT1 cells look like signature A?

Which AT1 cells look like signature B?
Thus:
XENIUM

physical neighborhood
        ↓
Niche 1 / Niche 2
        ↓
gene signatures
        │
        │ transfer
        ▼
MULTIOME

Niche-1-like AT1
Niche-2-like AT1
You are not reconstructing their literal neighborhood.
You're saying:
This dissociated cell has a molecular state corresponding to the state that was originally discovered in spatial Niche 2.
That distinction should remain extremely explicit in the paper.

8. Why multiome is so valuable
A normal scRNA-seq cell tells you:
Which genes are expressed?
Multiome gives you RNA plus ATAC.
ATAC asks:
Which regions of DNA are accessible?
DNA is wrapped around chromatin.
Some areas are tightly closed.
Some are accessible.
TFs generally need accessible regulatory DNA to act.
So now you can compare:
Niche-1-like AT1

RNA:
Gene A ↑
Gene B ↑
Gene C ↓

ATAC:
Region 1 open
Region 2 closed
Region 3 open
versus:
Niche-2-like AT1

RNA:
Gene A ↓
Gene B ↓
Gene C ↑

ATAC:
Region 1 closed
Region 2 open
Region 3 open
Then sequence motifs inside the newly accessible DNA can nominate TF families.
You can move from:
Niche 2 has different genes
to:
Niche 2 has different genes

AND

different regulatory DNA accessibility

AND

different candidate TF activities

AND potentially

different TF → enhancer → gene regulatory networks.
That is what the manuscript means by:
Neighborhood-defined populations exhibit different regulatory states.

9. This is precisely where your KG belongs
Here is the complete project as I now think it should be conceptualized:
                        SPATIAL NICHELINKER
════════════════════════════════════════════════════════════

Xenium spatial cells
        │
        ▼
Cellular neighborhoods
        │
        ▼
Neighborhood clustering within each cell type
        │
        ▼
AT1 Niche 1        AT1 Niche 2
        │                │
        └──────┬─────────┘
               ▼
Niche-associated expression signatures
               │
               ▼
Independent scRNA validation
               │
               ▼
Map signatures → multiome
               │
               ▼
Niche-1-like / Niche-2-like multiome populations
               │
               ▼
RNA + ATAC regulatory analysis
               │
               ▼
Candidate TF → locus → gene regulatory networks
               │
               │
               ▼
             DPI-KG
════════════════════════════════════════════════════════════

      Experimental evidence + literature evidence

TF ──binding──▶ Regulatory locus
                      │
                      │ enhancer/gene link
                      ▼
                   Target gene
                      ▲
                      │
                perturbation
                      │

       + cell type
       + lung/IPF context
       + provenance
       + literature
       + ChIP
       + motifs
       + prior experiments
       + contradictory evidence

               │
               ▼

"Which regulatory mechanisms distinguish
 Niche 1 from Niche 2, and how well are they supported?"
That is the project.

10. So what is DPI-KG now?
I would redefine it internally as:
The context-specific regulatory evidence graph used by Spatial NicheLinker to organize, validate and interpret TF–regulatory-locus–target-gene relationships associated with neighborhood-defined cellular states.
Not another project.
Not another biological hypothesis.
Not another agent product.
It is infrastructure supporting the regulatory part of this manuscript.
The final architecture you already have fits this very well: it is explicitly a gene-level TF→target graph backed by context-specific binding, locus activity, locus→gene and regulatory-effect observations, with experiment/study/publication provenance. dpi_knowledge_graph_architectur…

11. But I would make one important modification to the existing DPI-KG schema
The original DPI-KG schema did not know about Spatial NicheLinker-defined niche states.
Now it needs to.
And I would not put "Niche 2" directly into BiologicalContext.
Why?
Because:
AT1
human
lung
IPF
are biological identities/context.
But:
AT1 Niche 2
is something your algorithm discovered.
It depends upon:
dataset
neighborhood definition
distance/kNN rule
clustering method
parameters
version
Therefore I would introduce a project-specific entity such as:
SpatialNicheState
For example:
SpatialNicheState
────────────────────────
id: AT1_N2_XENIUM_V1
parent_cell_type: AT1
label: Niche 2
dataset: Xenium_IPF_001
method: SpatialNicheLinker
definition_run: RUN_0045
description:
  airway/remodeling-associated neighborhood
And then:
AT1 ──HAS_NICHE_STATE──▶ AT1_Niche2

AT1_Niche2 ──DEFINED_BY──▶ neighborhood composition

AT1_Niche2 ──HAS_SIGNATURE──▶ Niche2_signature

MultiomePopulation ──CORRESPONDS_TO──▶ AT1_Niche2
This is a very important design improvement if DPI-KG is now part of this project.

12. Your KG therefore has two connected worlds
One world records what your experiment discovers.
The other records what the scientific literature already knows.
For example:
PROJECT DISCOVERY

AT1_Niche2
    │
    ├── associated with → KRT17 ↑
    ├── associated with → CD44 ↑
    ├── associated with → AREG ↑
    └── associated with → XBP1 ↑

Multiome ATAC
    │
    └── suggests → TF-X regulatory activity
Then the literature graph asks:
Has TF-X been shown to bind regulatory regions
of these genes?

In epithelial cells?

In lung?

In fibrosis?

Was binding measured?

Was TF-X perturbed?

Were the effects direct?

What experiment established this?

Did multiple databases merely reuse the same experiment?
And you connect the two.

13. A concrete example
Suppose your multiome results eventually suggest that XBP1 is more active in AT1 Niche-2-like cells.
I am using this as an example, not saying your current data has already established XBP1 as the causal regulator.
Your project observation might be:
AT1 Niche 2
      │
      └── higher candidate XBP1 regulatory activity
The KG then asks something much more precise.
Does XBP1 actually bind regulatory loci near Niche-2 genes?
XBP1
 ↓
BindingObservation
 ↓
RegulatoryLocus
Is that locus connected to a gene such as Gene Y?
RegulatoryLocus
 ↓
LocusGeneLink
 ↓
Gene Y
Is XBP1 regulation of Y experimentally observed?
Perturb XBP1
 ↓
Gene Y changes
And was that evidence obtained in something biologically relevant?
human?
mouse?

lung?
liver?

epithelial?
immune?

IPF?
cancer?

primary cell?
cell line?
That context issue is critical. Your final schema deliberately makes TF→gene support context-specific rather than treating it as a universal fact. dpi_knowledge_graph_architectur…

14. This is why your graph is not STRING
STRING might tell you:
XBP1 —— HSPA5
score = 0.92
But what exactly does that mean?
Maybe co-expression.
Maybe a pathway.
Maybe literature.
Maybe physical interaction.
For your biological question that is insufficient.
Your graph should be able to say something resembling:
Regulatory proposition:

XBP1 → Gene Y

Context:
human
lung
epithelial
IPF-compatible context

B = 2
measured TF occupancy

L = 2
credible enhancer→gene evidence

R = 2
TF perturbation changes Gene Y

Direction:
likely activating

Independent experiments:
3

Supporting publications:
4

Conflicting publication:
1

Niche relevance:
Gene Y elevated in AT1 Niche-2-like state

Project evidence:
Niche-2-like AT1 multiome population shows
accessible regulatory locus
That is scientifically much more useful.

15. What your role actually is
This is where your background fits very naturally.
You are not required to become the person who generates all of the biological conclusions manually.
Your expertise is in taking heterogeneous information and turning it into an auditable computational representation.
Biologists see:
paper
ATAC peak
TF
enhancer
gene
cell type
perturbation
disease
experimental assay
You should see:
entities
relations
context
provenance
confidence
evidence type
contradiction
normalization
query
That translation is exactly the KG problem.

16. What does "build the KG from literature" really mean?
This phrase can be misleading.
It should not mean:
Feed 10,000 PDFs to an LLM and create TF→gene edges whenever two gene names appear in a sentence.
That graph would be terrible.
Instead:
PAPER
  ↓
claim
  ↓
What biological statement is actually being made?
  ↓
What experiment supports the statement?
  ↓
What cell/tissue/species/disease?
  ↓
What type of evidence?
  ↓
Normalize entities
  ↓
Store claim + evidence + provenance
Your final DPI design already recommends focused, gene-seeded literature retrieval rather than indiscriminately processing all PubMed. It proposes seed papers from TF/target candidates, citation expansion and database-linked publications. dpi_knowledge_graph_architectur…

17. Here's what I would actually build
I would not start by crawling all IPF literature.
You already have a biological narrowing mechanism:
Spatial NicheLinker
       ↓
interesting cell types
       ↓
niche-specific genes
       ↓
multiome analysis
       ↓
candidate TFs / regulatory loci / targets
That becomes your literature search space.
Suppose the analysis ultimately gives you:
20 important TFs
500 candidate target genes
10 cell populations
Now retrieve literature around relevant combinations.
Conceptually:
"XBP1" AND "HSPA5" AND regulation

"XBP1" AND lung AND epithelial

"XBP1" AND fibrosis

"XBP1" AND ChIP

"XBP1" AND knockdown

"XBP1" AND enhancer AND HSPA5
Then expand around highly relevant papers.
The uploaded design suggested roughly 500–2,000 initial targeted papers followed by citation expansion, rather than whole-PubMed processing. dpi_knowledge_graph_architectur…
That is vastly more realistic.

18. How would the LLM actually be used?
This is where your LLM experience becomes useful.
The LLM is not the scientist deciding truth.
It is primarily a structured information extractor.
Give it a section from a paper.
Suppose a result says, conceptually:
Knockdown of TF-X reduced Y expression in human alveolar epithelial cells.
Your extractor produces:
TF: X

target_gene: Y

relation:
regulatory_effect

direction:
activating

evidence:
TF knockdown

species:
human

cell_type:
alveolar epithelial cell

tissue:
lung

disease:
null / unspecified

directness:
regulatory_effect

publication:
PMID...

section:
Results
Another paper might say:
ChIP-seq demonstrated occupancy of X at an enhancer 20 kb upstream of Y.
That becomes a different observation:
X
 ↓
BindingObservation
 ↓
RegulatoryLocus chr...
 ↓
LocusGeneLink?
 ↓
Y
Notice something important:
You do not collapse those two papers into one vague X REGULATES Y fact.
You preserve what each actually demonstrated.

19. The LLM extraction record should look roughly like this
Your final teaching/design file already recommends retaining TF, target gene, direction, directness, cell type, tissue, species, disease, assay, PMID, source sentence, section, extraction confidence and whether the claim was measured or inferred. dpi_first_principles(1)
That is exactly the right philosophy.
And source section matters.
For example:
Results
→ strongest source for experimental finding

Methods
→ tells you context and assay

Figure caption
→ often valuable experimental information

Abstract
→ summarized claim

Discussion
→ interpretation; weaker

Introduction
→ usually second-hand background

Review
→ useful for finding original papers,
   not ideal as primary evidence
The architecture explicitly recommends this hierarchy. dpi_knowledge_graph_architectur…

20. Where encoders/embeddings help
This is another area where your background is directly useful.
LLMs aren't needed for everything.
Embeddings can help retrieve relevant passages from papers.
You can represent paragraphs as vectors and ask:
Find passages semantically related to:

"TF directly binds enhancer"
"TF knockdown changes target"
"transcriptional regulation"
"chromatin accessibility"
"alveolar epithelial cells"
Then only send high-probability passages to an LLM.
So your pipeline might be:
PubMed / PMC
      ↓
paper retrieval
      ↓
section segmentation
      ↓
biomedical NER
      ↓
embedding retrieval
      ↓
candidate regulatory passages
      ↓
LLM structured extraction
      ↓
entity normalization
      ↓
rule validation
      ↓
human QC sample
      ↓
KG
No agent architecture is required.
A normal deterministic pipeline is perfectly reasonable.

21. You do not need agentic AI for this
I want to emphasize that because you specifically mentioned it.
You could build this entire project with:
Python
+
PubMed/PMC APIs
+
PubTator
+
an LLM
+
embedding model
+
Neo4j
+
Pydantic/LinkML schemas
and have zero autonomous agents.
That would still be a perfectly legitimate AI/KG contribution.
In fact, your own finalized DPI paper strategy explicitly says that an agent is last; an agent over an unvalidated regulatory prior is not the scientific contribution. dpi_paper_strategy(1)
For this project I agree even more strongly.

22. Where PubTator helps
You do not need your LLM to rediscover every biomedical entity.
PubTator Central already performs biomedical entity annotations over PubMed/PMC.
Your DPI plan sensibly recommends using such existing NER infrastructure rather than rebuilding entity detection from scratch. dpi_knowledge_graph_architectur…
Then your LLM can focus on the much harder question:
What relationship is being asserted between these normalized entities?
That is a better use of an LLM.

23. The graph you need is not enormous
This is another important point.
Do not put:
3 million individual AT1 cells
+
every ATAC peak
+
every count matrix value
into Neo4j.
That's not what a KG is for.
The final schema already draws the proper graph/warehouse boundary: normalized entities, summarized observations, evidence assertions, provenance and scores belong in the graph; raw peaks, matrices, per-base attributions, full summary statistics and model artifacts belong in a warehouse/object store. dpi_final_schema(1)
So:
Neo4j / KG
──────────────────────
TF
Gene
RegulatoryLocus
SpatialNicheState
BiologicalContext
EvidenceAssertion
Publication
Experiment
BindingObservation
LocusGeneLink
DEAnalysis
etc.


Parquet / Zarr / S3 / filesystem
────────────────────────────────
raw RNA matrix
raw ATAC matrix
millions of peaks
per-cell data
model outputs
large gene signatures
raw PDFs
The KG points to those artifacts.
It doesn't replace them.

24. Provenance is one of your biggest contributions
Imagine you find XBP1→Y in:
ChIP-Atlas
UniBind
CistromeDB
Paper A
Paper B
Naively:
5 sources support XBP1 → Y!
But maybe:
ChIP-Atlas ─┐
UniBind ────┼── same GEO experiment
CistromeDB ─┘

Paper A reports that experiment

Paper B reviews Paper A
You actually have:
1 independent experiment
not five.
This matters enormously in biomedical KG construction.
Your final architecture deliberately makes Experiment → Study → Publication part of the graph so evidence is deduplicated by underlying experiment/study rather than database count. dpi_knowledge_graph_architectur…
That is a substantive strength of your design.

25. And now here is the most important scientific limitation
Your literature KG cannot, by itself, prove:
AT1 Niche 1 and AT1 Niche 2 have different regulatory states.
Why?
Because the scientific literature does not know what your particular Spatial NicheLinker Niche 1/Niche 2 assignments are.
Your multiome analysis has to establish that.
The KG can then tell you:
The TF and target relationships underlying the observed difference have prior experimental support.
Think of it this way:
MULTIOME DATA

Discovers:
"TF-X regulatory program differs between
 Niche-1-like and Niche-2-like AT1"

        ↓

DPI-KG

Explains:
"Here is what we know about TF-X,
 its binding sites, targets, direction,
 experiments and lung relevance."

        ↓

COMBINED RESULT

"This is an observed niche-associated
 regulatory difference with an evidence-backed
 mechanistic interpretation."
That is much stronger scientifically than having the KG generate the regulatory conclusion.

26. What does the KG ultimately let your collaborators ask?
Instead of searching 50 papers manually, they should eventually be able to ask something like:
What are the highest-supported transcription factors distinguishing Niche-2-like AT1 cells from Niche-1-like AT1 cells?
And receive:
TF-X
  evidence from project multiome
  + lung expression support
  + measured binding
  + 3 independent studies
  + 12 target genes enriched in Niche 2
  + enhancer evidence
  + perturbation evidence

TF-Y
  motif evidence only
  + no direct binding evidence
  + 7 Niche-2 targets
  + literature evidence in cancer cell lines
  - poor primary-lung context

TF-Z
  strong binding
  + strong target effect
  - evidence is mouse only
That is the real value.
Not merely:
TF-X score = .92

27. Your project-specific KG architecture should therefore look roughly like this
                    SPATIAL NICHE LAYER
══════════════════════════════════════════════════

CellType
  │
  └──HAS_STATE──▶ SpatialNicheState
                        │
                        ├──DEFINED_BY──▶ NeighborhoodProfile
                        │
                        ├──HAS_SIGNATURE──▶ GeneSignature
                        │
                        └──DERIVED_BY──▶ AnalysisRun

SpatialNicheState
       ▲
       │ CORRESPONDS_TO
       │
MappedMultiomePopulation


                   REGULATORY LAYER
══════════════════════════════════════════════════

Gene(:TF)
    │
    └──REGULATES_VIA──▶ RegulatoryInteraction
                              │
                              └──TARGETS──▶ Gene
                              │
                              └──HAS_STATEMENT
                                      ↓
                              ContextualStatement
                                      │
                                      ▼
                              BiologicalContext


                 MECHANISTIC EVIDENCE
══════════════════════════════════════════════════

TF / MotifFamily
       │
       ▼
BindingObservation
       │
       ▼
RegulatoryLocus
       │
       ▼
LocusGeneLink
       │
       ▼
Target Gene

TF
 │
 ▼
PerturbationEffectObservation
 │
 ▼
Target Gene


                    PROVENANCE
══════════════════════════════════════════════════

EvidenceAssertion
       │
       ▼
AnalysisRun
       │
       ▼
Experiment
       │
       ▼
Study
       │
       ▼
Publication
This is, to me, the cleanest merger of Spatial NicheLinker + DPI-KG.

28. And the manuscript becomes much easier to understand
Your Results story is basically:
RESULT 1
Cells of the same type occupy
different cellular neighborhoods.

        ↓

RESULT 2
Those neighborhood-defined cells
have different transcriptional states.

        ↓

RESULT 3
The phenomenon occurs across multiple
epithelial, immune and mesenchymal cell types.

        ↓

RESULT 4
Niche-associated transcriptional states
can be found again in independent
scRNA-seq and multiome datasets.

        ↓

RESULT 5
The corresponding multiome populations
also differ in chromatin/regulatory state.

        ↓

RESULT 6 — where your KG becomes powerful

Evidence-backed TF→locus→target networks
explain which regulatory mechanisms
differentiate the niche-associated states.
That is a very coherent paper.

29. What should the final regulatory result actually show?
Ideally, not just:
Niche 1 has TF A and Niche 2 has TF B.
That is weak.
You want something more mechanistically layered.
For representative cell types—probably AT1 and activated fibrotic fibroblasts first—you want to move toward:
Niche 1-like
────────────────────
TF program A
↓
accessible loci A
↓
target genes A
↓
alveolar/homeostatic functions


Niche 2-like
────────────────────
TF program B
↓
accessible loci B
↓
target genes B
↓
injury/remodeling functions
Then DPI-KG provides evidence strength for the TF→target arrows.
This is the critical connection between your contribution and the biological paper.

30. Do not conflate motif evidence with a TF
This will matter a lot in your multiome work.
Imagine an ATAC region contains a forkhead motif.
That may tell you:
Forkhead-family TF could bind here
It does not automatically tell you:
FOXA2 definitely binds here
FOXA1, FOXA2 and other family members can have similar binding preferences.
Your finalized architecture explicitly corrected this by representing Motif/MotifFamily separately from TF-specific occupancy. dpi_knowledge_graph_architectur…
That distinction will save you from a lot of biological overclaiming.

31. One more important issue: the landscape is now competitive
There are already methods addressing pieces of this problem.
For example, COVET/ENVI represents spatial cellular environments and can project spatial information onto scRNA-seq data. DOI
NicheCompass identifies and characterizes spatial niches and supports spatial reference mapping and spatial multi-omics integration. Nature
And this is particularly important: ISON, published in June 2026, explicitly integrates spatial transcriptomics with single-cell multiome data, predicts spatial chromatin accessibility and reconstructs spatially resolved regulatory networks. DOI
Therefore, I would not make the paper's novelty claim simply:
We transfer spatial states into multiome and infer regulatory networks.
That space is becoming crowded.

32. What I think the strongest novelty actually is
The combination is more distinctive:
Same annotated cell type
       ↓
stratified purely by surrounding cell-type composition
       ↓
expression tested only after niche definition
       ↓
states reproduced across independent datasets
       ↓
spatially defined states transferred into multiome
       ↓
regulatory state differences measured
       ↓
TF→locus→gene mechanisms interpreted through
a context-aware, provenance-preserving evidence KG
Particularly strong is the separation:
neighborhood is used to define the population; gene expression is used afterward to test whether the population differs.
That avoids a circular "expression discovered the groups and then expression proved the groups differ" argument.
Then the KG provides an additional mechanistic/evidence dimension.
That, as a complete story, is stronger than treating DPI-KG as another standalone resource.

33. What I would personally change about the old DPI-KG plan
Your uploaded DPI-KG plan originally envisioned the graph as a broader standalone regulatory-resource paper with separate benchmarking, variants, GWAS, perturbation prediction and potentially its own publication. Its final paper strategy says the graph should prove better regulatory ranking/prediction rather than merely "we built a KG." dpi_paper_strategy(1)
Given your new project decision, I would reduce that scope substantially for this paper.
Keep the core:
TFs
genes
regulatory loci
contexts
binding observations
locus→gene evidence
regulatory-effect evidence
literature
experiments
publications
provenance
B/L/R evidence decomposition
Keep niche-state integration.
Keep literature extraction.
Keep multiome regulatory evidence.
But I would move things such as:
full drug discovery layer
large GWAS platform
universal cross-species graph
agentic interface
huge learned TF-ranking model
general biomedical KG
out of the critical path unless the biological team explicitly needs them.
Your own final build order already puts drugs and agents at the end for essentially this reason. dpi_first_principles(1)

34. If they literally assigned you "build this from literature," this is what I would deliver
I would call version 1 something like:
Literature-grounded regulatory evidence graph for Spatial NicheLinker.
It accepts:
candidate TFs
candidate target genes
cell types
niche-associated programs
from the biological analysis.
It returns:
TF-target evidence
binding evidence
direction
directness
lung/IPF relevance
cell-type relevance
experimental system
PMID
independent-study count
conflicting evidence
supporting regulatory loci when available
Then multiome observations can be overlaid later.
That is already a substantial project.

35. How I would build it technically
I would follow the same principle your final architecture arrived at:
Schema
  ↓
Identifiers
  ↓
Provenance
  ↓
Literature retrieval
  ↓
Extraction
  ↓
Normalization
  ↓
Validation
  ↓
Graph materialization
  ↓
Project multiome integration
  ↓
Queries / visualization
The existing DPI design's broader build order is provenance-first precisely because experiment identity, context identity and locus identity become painful to retrofit after ingestion. dpi_knowledge_graph_architectur…
For your narrower project, I would preserve that philosophy while moving the targeted literature pipeline earlier because literature construction is specifically your assigned deliverable.

36. What would make your contribution scientifically meaningful?
The KG becomes valuable if the paper can show something like:
Spatial NicheLinker nominated TF-X as a regulator of an injury-associated AT1 Niche-2 state. Multiome data showed corresponding accessibility and regulon changes. DPI-KG independently identified context-compatible binding and perturbational evidence supporting X→target relationships while distinguishing strong direct evidence from motif-only or non-lung evidence.
Even more interesting:
The multiome analysis nominated TF-Y, but DPI-KG found that the evidence was largely motif-family-level or derived from unrelated cancer lines, so the paper labels TF-Y as a candidate rather than established regulator.
That second example is actually excellent science.
A KG that sometimes says:
"evidence insufficient"
is more useful than one that always produces a beautiful mechanistic network.

37. Your role, in one sentence
If someone in the lab asks what you are contributing, I would describe it this way:
I am building the evidence and knowledge-graph layer that connects the transcription factors and regulatory loci discovered in Spatial NicheLinker's multiome analysis to experimentally supported TF–target mechanisms from the literature, while preserving cell context, evidence type and provenance.
That is both technically accurate and biologically understandable.

38. And your end-to-end mental model should now be this
Memorize this:
NEIGHBORS
   ↓
NICHE
   ↓
CELL STATE
   ↓
GENE SIGNATURE
   ↓
MAP TO MULTIOME
   ↓
CHROMATIN STATE
   ↓
TRANSCRIPTION FACTOR
   ↓
REGULATORY LOCUS
   ↓
TARGET GENE
   ↓
REGULATORY PROGRAM
   ↓
DPI-KG EVIDENCE
   ↓
BIOLOGICAL MECHANISM
Or even shorter:
Who surrounds the cell → what state the cell enters → what regulates that state → what evidence supports that regulation.
That is the whole project.

39. Citation potential
Now to your citation question.
There are two very different possibilities.
If this remains primarily:
"Spatial NicheLinker applied to IPF with a nice AT1/fibroblast/macrophage story"
it is useful, but fairly disease/application-specific.
If it becomes:
"Spatial NicheLinker is a reusable method/package for discovering neighborhood-defined cell states, transferring them into dissociated multiome data, and performing evidence-backed regulatory interpretation"
then the citation ceiling becomes much higher.
For perspective, broad reusable regulatory/spatial methods can accumulate citations rapidly. SCENIC+, published in Nature Methods in 2023, is showing 835 citations on the Nature page as of the current search; COVET/ENVI, published in Nature Biotechnology, shows 94 citations. Nature Those are upper-end comparison points, not realistic direct predictions for this project.
My current expectation would be:
Final form
My expected 3-year citations
Rough 5-year potential
Primarily IPF biological application
25–60
50–120
Strong Spatial NicheLinker methods paper + software + several cell types/datasets
60–120
120–250
Generalizable method + excellent benchmarks + reusable package + strong journal + KG/regulatory layer
100–200+
200–400+
Becomes a field-standard spatial→multiome regulatory method
potentially 300+
potentially much higher
My actual expectation based on what you have shown me today is roughly 60–120 citations in the first three years after publication, with ~80–100 as a reasonable center estimate.
I would move that estimate upward substantially if the authors demonstrate generalization beyond IPF, release a clean package, make the niche-transfer workflow easy to use on other datasets, and make the regulatory/KG component reusable rather than hard-coded to this manuscript.
And I would move it downward if the KG becomes a very large side project that distracts from a clear Spatial NicheLinker story.
The most citable version is not “Spatial NicheLinker + an enormous KG + agents + GWAS + drugs.”
It is:
A clean, reusable Spatial NicheLinker method for identifying neighborhood-conditioned cell states, transferring those states to richer non-spatial modalities, and identifying evidence-backed regulatory programs that distinguish them.
In that formulation, DPI-KG is exactly where it belongs: underneath the biological result, making the regulatory claims stronger rather than competing with the main project for attention.



Yes. For this project, I would modify the existing DPI-KG schema so the KG is explicitly built around Spatial NicheLinker + regulatory interpretation, rather than keeping DPI-KG as a separate generic project.
The key design rule is:
Spatial NicheLinker discovers the niche state. Multiome discovers candidate regulatory differences. The KG stores and evaluates the evidence connecting TF → regulatory locus → target gene in those niche-associated states.
The existing DPI design already gives us the right regulatory backbone: a canonical TF→gene proposition, context-specific statements, binding observations, locus→gene observations, perturbation effects, and experiment/study/publication provenance. dpi_knowledge_graph_architectur…
Proposed Spatial NicheLinker KG schema
════════════════════════════════════════════════════════════════════
1. BIOLOGICAL ENTITIES
════════════════════════════════════════════════════════════════════

Gene
 ├── may also have label :TF
 └── canonical ID = Ensembl / HGNC

Motif
      │
      └── MOTIF_OF ───────────────▶ MotifFamily / TFClass
                                          │
                                          └── CANDIDATE_BINDER ──▶ Gene:TF

RegulatoryLocus
 [chr, start, end, assembly, locus_type]

CellType
 [AT1, AT2, alveolar macrophage, fibroblast...]

BiologicalContext
 [species, tissue, disease, cell_type, system_type, resolution]


════════════════════════════════════════════════════════════════════
2. SPATIAL NICHE LAYER
════════════════════════════════════════════════════════════════════

CellType
   │
   └── HAS_NICHE_STATE ─────────▶ SpatialNicheState
                                   [AT1_Niche1]
                                   [AT1_Niche2]
                                          │
                                          ├── DEFINED_BY ──▶ NeighborhoodProfile
                                          │
                                          ├── HAS_SIGNATURE ──▶ GeneSignature
                                          │
                                          └── DERIVED_BY ──▶ AnalysisRun


SpatialNicheState
       ▲
       │ CORRESPONDS_TO
       │
DatasetPopulation
 [Xenium / scRNA / Multiome population]


Example:

AT1
 │
 ├──HAS_NICHE_STATE──▶ AT1_Niche1
 │
 └──HAS_NICHE_STATE──▶ AT1_Niche2


════════════════════════════════════════════════════════════════════
3. CROSS-DATASET MAPPING LAYER
════════════════════════════════════════════════════════════════════

SpatialNicheState
      │
      ▼
GeneSignature
      │
      │ USED_BY
      ▼
StateMappingObservation
      │
      ├── MAPS_POPULATION ──▶ DatasetPopulation
      │
      ├── TO_NICHE ─────────▶ SpatialNicheState
      │
      └── GENERATED_BY ─────▶ AnalysisRun


Example:

AT1_Niche2
      │
      ▼
Xenium-derived Niche2 signature
      │
      ▼
StateMappingObservation
      │
      ▼
Multiome AT1 Niche2-like population


════════════════════════════════════════════════════════════════════
4. REGULATORY PROPOSITION LAYER
════════════════════════════════════════════════════════════════════

Gene:TF
   │
   └── REGULATES_VIA ──▶ RegulatoryInteraction
                                   │
                                   ├── TARGETS ───────▶ Gene
                                   │
                                   └── HAS_STATEMENT
                                             │
                                             ▼
                                    ContextualStatement
                                             │
                                             └── IN_CONTEXT
                                                      │
                                                      ▼
                                             BiologicalContext


ContextualStatement stores:

B = binding evidence tier
L = locus→gene evidence tier
R = regulatory-effect evidence tier

direction
uncertainty
disagreement
status
context coherence


════════════════════════════════════════════════════════════════════
5. REGULATORY MECHANISM / OBSERVATION LAYER
════════════════════════════════════════════════════════════════════

Gene:TF OR MotifFamily
          │
          └── BINDER_IN ──▶ BindingObservation
                                      │
                                      ├── AT_LOCUS ──▶ RegulatoryLocus
                                      │
                                      └── IN_CONTEXT ─▶ BiologicalContext


RegulatoryLocus
      ▲
      │ FROM_LOCUS
      │
LocusGeneLink
      │
      ├── TO_GENE ─────────▶ Gene
      └── IN_CONTEXT ──────▶ BiologicalContext


RegulatoryLocus
      ▲
      │ OF_LOCUS
      │
LocusActivityObservation
      │
      └── IN_CONTEXT ──────▶ BiologicalContext


Gene:TF
      ▲
      │ PERTURBED_TF
      │
PerturbationEffectObservation
      │
      ├── AFFECTS_GENE ────▶ Gene
      └── IN_CONTEXT ──────▶ BiologicalContext


════════════════════════════════════════════════════════════════════
6. NICHE ↔ REGULATION CONNECTION
════════════════════════════════════════════════════════════════════

SpatialNicheState
       │
       └── HAS_REGULATORY_PROGRAM ──▶ RegulatoryProgram


RegulatoryProgram
       │
       ├── INVOLVES_TF ───────────▶ Gene:TF
       ├── INVOLVES_LOCUS ────────▶ RegulatoryLocus
       ├── INVOLVES_TARGET ───────▶ Gene
       └── DERIVED_BY ────────────▶ AnalysisRun


OR, preferably for individual findings:


RegulatoryStateObservation
       │
       ├── FOR_NICHE ─────────────▶ SpatialNicheState
       ├── INVOLVES_TF ───────────▶ Gene:TF / MotifFamily
       ├── INVOLVES_LOCUS ────────▶ RegulatoryLocus
       ├── INVOLVES_TARGET ───────▶ Gene
       ├── IN_CONTEXT ────────────▶ BiologicalContext
       └── GENERATED_BY ──────────▶ AnalysisRun


════════════════════════════════════════════════════════════════════
7. TRANSCRIPTION / EXPRESSION LAYER
════════════════════════════════════════════════════════════════════

ExpressionObservation
      │
      ├── OF_GENE ───────────────▶ Gene
      ├── FOR_NICHE ─────────────▶ SpatialNicheState
      └── GENERATED_BY ──────────▶ AnalysisRun


DifferentialExpressionAnalysis
      │
      ├── CASE_STATE ────────────▶ SpatialNicheState
      ├── CONTROL_STATE ─────────▶ SpatialNicheState
      └── GENERATED_BY ──────────▶ AnalysisRun

Gene
 │
 └── DE_IN {logFC, q-value} ─────▶ DifferentialExpressionAnalysis


════════════════════════════════════════════════════════════════════
8. EVIDENCE + PROVENANCE LAYER
════════════════════════════════════════════════════════════════════

EvidenceAssertion
      │
      ├── ASSERTS {supports/refutes/inconclusive}
      │               │
      │               ▼
      │       Observation / ContextualStatement
      │
      └── FROM_RUN
               │
               ▼
           AnalysisRun
               │
               ├── USES_EXPERIMENT ──▶ Experiment
               │                          │
               │                          ▼
               │                        Study
               │                          │
               │                          ▼
               │                     Publication
               │
               └── USES_DATASET ─────▶ Dataset


Literature-derived assertion:

EvidenceAssertion
      │
      └── REPORTED_IN ─────────────▶ Publication
The B/L/R part remains particularly valuable. The existing design defines direct-regulation evidence as three separate questions: does the TF occupy the locus, is the locus actually connected to the gene, and does altering the TF affect the target? dpi_first_principles(1)

The most important new nodes
For this project I would add five things to the old DPI-KG:
New entity
Why you need it
SpatialNicheState
Represents AT1 Niche 1, AT1 Niche 2, fibroblast Niche 1, etc.
NeighborhoodProfile
Records what spatial composition caused that niche to exist
GeneSignature
Spatial expression signature used for cross-dataset transfer
DatasetPopulation
Represents the corresponding Xenium/scRNA/multiome population without storing every cell
RegulatoryStateObservation
Connects niche state to TF/motif/locus/target observations discovered from multiome
Of these, SpatialNicheState and RegulatoryStateObservation are the most important additions.

Why SpatialNicheState should NOT simply be BiologicalContext
This distinction matters.
Your existing BiologicalContext should contain stable biological information like:
species = human
tissue = lung
disease = IPF
cell_type = AT1
resolution = single-cell
But:
Niche 2
is different.
Niche 2 was computed by Spatial NicheLinker.
It depends on:
Xenium dataset
+
neighborhood radius/kNN definition
+
cell-type labels
+
clustering algorithm
+
parameters
+
software version
So this:
BiologicalContext:
human / lung / IPF / AT1
should remain reusable.
And this:
SpatialNicheState:
AT1_Niche2
should be an algorithm-derived object.
Then:
AT1_Niche2
      │
      └── IN_CONTEXT ──▶ human / lung / IPF / AT1
That is much cleaner.

Concrete AT1 example
Imagine the regulatory analysis eventually finds an XBP1-associated program.
The graph could contain:
                           SpatialNicheState
                           AT1_Niche2
                               │
                 HAS_REGULATORY_STATE
                               │
                               ▼
                  RegulatoryStateObservation
                          │          │
                          │          │
                    TF/Motif       target
                          │          │
                          ▼          ▼
                        XBP1       HSPA5
                          │
                    binding evidence
                          ▼
                   RegulatoryLocus
                          │
                    locus→gene
                          ▼
                        HSPA5
And underneath that project observation:
XBP1
 │
 └──REGULATES_VIA──▶ RegulatoryInteraction ──TARGETS──▶ HSPA5
                           │
                           ▼
                    ContextualStatement
                           │
                  human / lung /
                 epithelial / IPF
                           │
               ┌───────────┼────────────┐
               ▼           ▼            ▼
             BINDING     LOCUS→GENE   PERTURBATION
             evidence     evidence      evidence
               │           │             │
               └───────────┴─────────────┘
                           │
                           ▼
                      provenance
                           │
                 Experiment → Study
                           ↓
                      Publication
Now your paper can say much more precisely:
XBP1-associated regulatory activity was increased in AT1 Niche-2-like cells, and DPI-KG identified prior context-compatible experimental support for a subset of the inferred XBP1 target relationships.
Rather than:
XBP1 drives Niche 2.
Those are scientifically very different claims.

What I would NOT put into Neo4j
Do not turn the KG into your omics database.
The existing design explicitly separates stable graph entities/observations from raw matrices, raw peaks and large artifacts. dpi_final_schema(1)
So the architecture should be:
                 ┌─────────────────────┐
                 │       Neo4j KG      │
                 │                     │
                 │ TF                  │
                 │ Gene                │
                 │ NicheState          │
                 │ RegulatoryLocus     │
                 │ Evidence            │
                 │ Publication         │
                 │ Observation         │
                 │ Provenance          │
                 └─────────┬───────────┘
                           │ references
                           ▼
                 ┌─────────────────────┐
                 │   Data Warehouse    │
                 │                     │
                 │ RNA matrices        │
                 │ ATAC matrices       │
                 │ peaks               │
                 │ per-cell scores     │
                 │ full signatures     │
                 │ PDFs                │
                 │ model artifacts     │
                 └─────────────────────┘
That is the schema I would now lock for the project.
The central path to remember is:
SpatialNicheState
        ↓
RegulatoryStateObservation
        ↓
TF
        ↓
BindingObservation
        ↓
RegulatoryLocus
        ↓
LocusGeneLink
        ↓
Target Gene
        ↓
PerturbationEffect
        ↓
EvidenceAssertion
        ↓
Experiment / Study / Publication
That turns the KG into the mechanistic evidence backbone of Spatial NicheLinker, rather than a separate DPI-KG project.



Yes. The additional Results section and transcript make the project much clearer, and I would simplify what I told you before.
The immediate project is not “build DPI-KG in full.” It is:
Build a literature-grounded regulatory evidence KG that takes the TF candidates and gene programs coming from Spatial NicheLinker/ChromLinker and nominates a small, defensible set of transcription factors for follow-up, with cell-type, disease, niche, direction, target-gene, pathway, experimental-evidence, and publication context.
And because Anshunya wants this soon, my strongest recommendation is:
Do not spend your time fine-tuning BioBERT, PubMedBERT, GLiNER, GLiNER2.5, or GLiFormer right now.
Use PubTator + a strong LLM with strict structured extraction for the first working KG.If you need cheaper large-scale extraction, add GLiNER2.5 as a first-pass filter/extractor.Fine-tuning becomes Phase 2 only after this pipeline has generated a manually reviewed dataset.
That is the highest-value path for where your project is today.

1. The project has become more specific
The manuscript already produces candidate regulators.
For AT1, for example:
Niche 1:
TEAD1
KLF5
GATA6

Condition dependent:
FOXA2

Niche 2 / IPF:
ETV1
For macrophages:
SPI1
EGR2
BHLHE41
TFEC
IRF8
CEBPB
For KRT5−/KRT17+:
TEAD1
KLF5
RFX2
For activated fibrotic fibroblasts:
FOSB
TEAD1
...
The manuscript is already appropriately cautious:
ChromLinker identifies inferred TF-gene connections. It does not establish direct binding or causal regulation.
That statement tells us exactly what the KG has to provide.
ChromLinker asks:
What regulatory relationships does the multiome data predict?
The KG asks:
Which of those predictions are supported by prior biological evidence?

In what cells?

In what tissue?

In IPF/fibrosis?

Was it actual binding?
Was it perturbation?
Was it only correlation?

Which TFs repeatedly regulate genes in the niche program?

Are there upstream TFs that ChromLinker did not nominate?

Is there contradictory evidence?
So the KG becomes the external evidence and prioritization layer.

2. This is the final conceptual architecture
Your manuscript gives you this:
                       SPATIAL NICHELINKER
                              │
                              ▼
                     Spatial neighborhood
                              │
                              ▼
                      Spatial Niche State
                              │
                              ▼
                    Niche Gene Signature
                              │
                              ▼
            scRNA / Multiome State Mapping
                              │
                 ┌────────────┴────────────┐
                 ▼                         ▼
               RNA                       ATAC
                 │                         │
                 └────────────┬────────────┘
                              ▼
                         ChromLinker
                              │
                              ▼
                  Candidate TF → Gene edges
                              │
                              │
                 YOUR COMPONENT STARTS HERE
                              │
                              ▼
                 ┌────────────────────────┐
                 │ REGULATORY EVIDENCE KG │
                 └────────────┬───────────┘
                              │
           ┌──────────────────┼────────────────────┐
           ▼                  ▼                    ▼
       Literature         TF expression        Pathways
       evidence            / DE evidence         / processes
           │                  │                    │
           └──────────────────┼────────────────────┘
                              ▼
                       TF NOMINATION
                              │
                    evidence vector per TF
                              │
               ┌──────────────┼─────────────┐
               ▼              ▼             ▼
          Supported        Qualified    Literature-only
          candidate        candidate       candidate
               │
               ▼
          top TFs for
       experimental follow-up
And later:
Geneformer perturbation
         │
         ▼
predicted cell-state shift
         │
         └──────────────▶ TF nomination evidence
Eventually:
Perturb-seq
   │
   ▼
experimental validation
That is the full scientific loop.

3. The most important change from our earlier KG design
I would not build the entire regulatory-locus DPI-KG right now.
The original architecture was scientifically rigorous and deliberately separated TF occupancy, locus→gene evidence, regulatory effects, contexts and provenance. dpi_knowledge_graph_architectur…
That remains the correct long-term conceptual model.
But your current manuscript needs:
TF nomination
+
TF → target evidence
+
cell/tissue/disease context
+
direction
+
experimental directness
+
pathway/program relationship
+
provenance
You do not presently need to ingest every enhancer coordinate, GWAS variant, drug, QTL, ABC link, Cistrome peak, etc.
Keep RegulatoryLocus available in the schema as optional.
Don't make it mandatory for the MVP.
That saves enormous work.

4. Final KG schema I would implement
Layer A — biological entities
Node
Purpose
Gene
All genes, including TFs
CellType
AT1, alveolar macrophage, activated fibrotic fibroblast, etc.
SpatialNicheState
AT1 Niche1, AT1 Niche2, etc.
GeneProgram
Niche-associated expression program
Pathway
Reactome/pathway entities
BiologicalProcess
GO biological processes
BiologicalContext
Human/lung/IPF/AT1 etc.
AnatomicalCompartment
alveolar/distal, airway/proximal when useful
RegulatoryLocus
optional for direct ChIP/enhancer evidence
Gene gets:
Gene:
  id: HGNC:...
  symbol: ETV1
  species: human
  is_tf: true
  tf_family: ETS
Do not make TF a completely separate biological entity.
An ETV1 gene is still a gene.
Use:
Gene {is_tf:true}

5. Spatial NicheLinker layer
CellType
   │
   └──HAS_NICHE_STATE──▶ SpatialNicheState
                              │
                              ├──IN_CONTEXT──▶ BiologicalContext
                              │
                              └──HAS_PROGRAM──▶ GeneProgram
                                                    │
                                                    ├──CONTAINS_UP_GENE──▶ Gene
                                                    │
                                                    ├──CONTAINS_DOWN_GENE▶ Gene
                                                    │
                                                    └──ENRICHED_FOR──────▶ Pathway
Example:
AT1
 │
 └─HAS_NICHE_STATE─▶ AT1_Niche2
                          │
                          ├─IN_CONTEXT─▶ Human_Lung_IPF
                          │
                          └─HAS_PROGRAM─▶ AT1_Niche2_Program
                                            │
                                            ├─ GDF15
                                            ├─ KRT17
                                            ├─ ATF3
                                            ├─ GFPT1
                                            ├─ TM4SF1
                                            ├─ CD44
                                            └─ AREG
This is essential because the KG needs to nominate:
TF
  FOR
specific gene program
  IN
specific spatial niche / cell type / disease
not simply:
ETV1 is important.

6. Represent ChromLinker as an observation
Do not convert ChromLinker output directly into:
ETV1 ──REGULATES──▶ Gene-X
That would overstate the evidence.
Create:
ChromLinkerObservation
Example:
ChromLinkerObservation:
  id: CLO:1234

  tf: ETV1
  target_gene: GeneX

  parent_cell_type: AT1

  niche_state:
    AT1_Niche2

  disease:
    IPF

  comparator:
    IPF_Niche1

  connection_score: ...

  difference_score: ...

  run:
    ChromLinker_run_2026_09
Graph:
ChromLinkerObservation
       │
       ├──PREDICTS_TF──────▶ ETV1
       │
       ├──PREDICTS_TARGET──▶ GeneX
       │
       ├──FOR_STATE────────▶ AT1_Niche2
       │
       └──GENERATED_BY─────▶ AnalysisRun
This preserves the manuscript's language:
inferred TF-gene connection.

7. Now the key literature object: RegulatoryClaim
This should be the center of your literature KG.
Do not directly store:
FOXA2 ──REGULATES──▶ GeneX
Instead:
FOXA2
  │
  ▼
RegulatoryClaim
  │
  ▼
GeneX
because the claim needs its context and provenance.
RegulatoryClaim:

  id: RC_000001

  regulator:
    FOXA2

  target:
    SFTPC

  relation:
    activates

  directness:
    direct

  evidence_type:
    ChIP_plus_perturbation

  biological_context:
    species: human
    tissue: lung
    cell_type: alveolar_epithelial
    disease: null
    model_system: primary_cells

  evidence_status:
    measured

  polarity:
    supports
Graph:
Gene:TF
   │
   └──REGULATOR_OF_CLAIM──▶ RegulatoryClaim
                                  │
                                  ├──TARGET_GENE──▶ Gene
                                  │
                                  ├──IN_CONTEXT──▶ BiologicalContext
                                  │
                                  └──HAS_EVIDENCE──▶ EvidenceAssertion
This retains the core principle of your previous DPI design: canonical TF→gene propositions should not be confused with the context-specific evidence supporting them. dpi_knowledge_graph_architectur…

8. Evidence needs categories
This part will make your KG scientifically useful.
EvidenceAssertion
should distinguish:
DIRECT_BINDING
TF_PERTURBATION
REPORTER_ASSAY
CRE_PERTURBATION
EXPRESSION_ASSOCIATION
COMPUTATIONAL_PREDICTION
CURATED_DATABASE
REVIEW_STATEMENT
PATHWAY_ASSOCIATION
The old DPI architecture already establishes the correct principle: evidence should attach to what it actually measures, rather than collapsing ChIP, enhancer assignment, perturbation and literature into one generic support score. dpi_knowledge_graph_architectur…
For this project, simplify that idea to:
EvidenceAssertion:

  polarity:
    supports | contradicts | inconclusive

  evidence_type:
    direct_binding |
    perturbation |
    reporter |
    expression |
    computational |
    review

  directness:
    direct |
    functional |
    associative |
    unclear

  assay:
    ChIP-seq |
    CUT&RUN |
    knockdown |
    knockout |
    overexpression |
    luciferase |
    RNA-seq |
    etc

  context_match:
    exact |
    close |
    partial |
    mismatched

  source:
    Publication

  source_passage:
    Passage

9. Literature provenance schema
RegulatoryClaim
       │
       ▼
EvidenceAssertion
       │
       ▼
Passage
       │
       ▼
Publication
With:
Passage:
  pmid: ...
  pmcid: ...
  section: Results
  sentence: ...
  start_offset: ...
  end_offset: ...
And:
Publication:
  pmid: ...
  doi: ...
  title: ...
  year: ...
The full earlier KG architecture also uses an experiment/study/publication provenance spine precisely to avoid double-counting evidence from multiple derived resources. dpi_knowledge_graph_architectur…
For now:
Publication
is mandatory.
Experiment and Study can be added wherever you can confidently identify them.

10. Add pathways because the meeting explicitly needs them
This is one of the most useful things in the transcript.
They don't want only:
Gene A
Gene B
Gene C
Gene D
They want:
What biology do these candidates represent?
So:
Gene ──MEMBER_OF_PATHWAY──▶ Pathway

Gene ──PARTICIPATES_IN──▶ BiologicalProcess
Examples:
TGF-beta signaling
Unfolded protein response
Hippo/YAP signaling
Epithelial morphogenesis
Cell-cell junction organization
ECM remodeling
Macrophage phagocytosis
Wnt signaling
These should preferably come from structured resources such as:
Reactome
GO
MSigDB where appropriate
not extracted only from papers.
Then:
GeneProgram
     │
     └──ENRICHED_FOR──▶ Pathway

11. The KG can solve the “hierarchy” question from the meeting
This is another reason a graph is useful.
Suppose literature has:
TF-A → TF-B
TF-B → Gene1
TF-B → Gene2
TF-B → Gene3
Since TF-B is itself a Gene {is_tf:true}, nothing special is required.
You simply get:
TF-A
 │
 ▼
RegulatoryClaim
 │
 ▼
TF-B
 │
 ▼
RegulatoryClaim
 │
 ├──Gene1
 ├──Gene2
 └──Gene3
Now queries can identify possible upstream regulators.
But the graph should call this:
literature-supported regulatory path
not:
proven causal hierarchy in AT1 Niche2
unless the evidence actually supports that.

12. Very important: create a TFNomination node
This is the piece that directly solves Anshunya's requirement.
TFNomination
represents:
Why is this TF being nominated for this niche-associated program?
Example:
TFNomination:

  tf:
    ETV1

  cell_type:
    AT1

  niche_state:
    Niche2

  disease:
    IPF

  program:
    AT1_IPF_Niche2_program

  chromlinker_rank:
    2

  chromlinker_support:
    strong

  tf_expression_support:
    yes

  target_program_overlap:
    0.31

  literature_direct_evidence:
    2

  literature_functional_evidence:
    5

  context_matched_publications:
    3

  independent_studies:
    3

  contradictory_studies:
    0

  pathway_support:
    Hippo/YAP
    epithelial_morphogenesis

  geneformer_support:
    null

  nomination_status:
    prioritized

  ranking_version:
    v1
Graph:
TFNomination
      │
      ├──NOMINATES──▶ Gene:TF
      │
      ├──FOR_STATE──▶ SpatialNicheState
      │
      ├──FOR_PROGRAM▶ GeneProgram
      │
      ├──SUPPORTED_BY▶ ChromLinkerObservation
      │
      ├──SUPPORTED_BY▶ ExpressionObservation
      │
      ├──SUPPORTED_BY▶ RegulatoryClaim
      │
      ├──SUPPORTED_BY▶ PerturbationObservation
      │
      └──GENERATED_BY▶ AnalysisRun
This should be the final output object of your KG.

13. This lets literature nominate TFs that ChromLinker did NOT find
This is particularly valuable.
Suppose the Niche2 program contains:
GDF15
KRT17
ATF3
GFPT1
CD44
AREG
...
Your KG asks:
Which TFs have literature-supported regulatory relationships
with an unexpectedly large number of these genes?
Imagine:
TF-X → GDF15
TF-X → KRT17
TF-X → CD44
TF-X → AREG
Then TF-X becomes a literature-derived candidate, even if it wasn't in ChromLinker's top 15.
You can formally calculate:
TF target genes
      ∩
Niche2 signature
and test enrichment with:
Fisher's exact test
against the background of expressed genes.
This is much more defensible than simply asking an LLM:
Which transcription factors are important in IPF?

14. Direction matters
You also know whether Niche genes are up or down.
Suppose:
TF-X ACTIVATES Gene-A
Gene-A ↑ in Niche2
Direction is concordant.
Whereas:
TF-X REPRESSES Gene-A
Gene-A ↑ in Niche2
may be directionally discordant depending on TF activity.
So your literature graph enables:
target overlap
+
direction consistency
rather than simple overlap.
This should be part of TF nomination.

15. Do not require TF differential expression
Nathan's network discussion mentions constraining TF expression.
That's useful, but it should be a filter/evidence feature rather than a universal gate.
TF activity can change because of:
phosphorylation
nuclear localization
cofactor availability
chromatin accessibility
ligand signaling
without large RNA changes.
So:
TF RNA expression
should be:
supporting evidence
not:
must be DE or discard.
That distinction is biologically important.

16. Now: GLiNER vs GLiNER2 vs GLiNER2.5 vs GLiFormer vs LLM?
This is where I would be very decisive.
Use LLM structured extraction as the primary extractor right now
The difficult part of your task is not NER.
Finding:
ETV1
TEAD1
FOXA2
SFTPC
KRT17
is easy.
The difficult question is:
Does this sentence say FOXA2 binds the enhancer of Gene-X, activates Gene-X, changes Gene-X after knockdown, merely correlates with Gene-X, or just discusses Gene-X in the same paragraph?
That requires:
relation
+
direction
+
directness
+
assay
+
cell context
+
species
+
disease
+
negation
+
evidence interpretation
NER alone does not solve your problem.

17. My exact model recommendation
Option
Use now?
Role
Classic GLiNER
No
Superseded for this use case
GLiNER2
No
Better structured IE, but use 2.5 if using the family
GLiNER2.5
Optional
Fast candidate/passages extraction
GLiFormer
No
Too new; relation extraction not strong enough for this project
PubMedBERT/BiomedBERT fine-tune
Later
Good if you obtain real labeled data
Strong LLM structured output
Yes
Primary relation/context/evidence extraction
PubTator 3.0
Yes
Biomedical entity normalization + retrieval assistance
GLiNER2.5 is genuinely interesting: the August 24, 2026 release added long-document processing, native chunking, joint entity/relation extraction and schema-constrained output, and supports inputs up to roughly 4,096 words before library-level chunking. Fastino
If you choose a GLiNER-family model, use GLiNER2.5, not classic GLiNER or GLiNER2.
But there is a major caveat: the published GLiNER2.5 benchmarks presented by its developers are primarily general NER/classification tasks rather than a rigorous benchmark for TF→target biomedical regulatory evidence extraction. Fastino
Therefore I would not make it the sole curator of your regulatory KG.

18. Why I would not use GLiFormer here
GLiFormer is interesting and very new, including NER, structured extraction and joint relation extraction.
But its own model card currently reports relatively weak zero-shot joint relation-extraction numbers on the evaluated general benchmarks—for example micro-F1 around 10 on DocRED/CrossRE and roughly 31.5 on the reported CoNLL04 zero-shot evaluation. Hugging Face
It was also only released very recently.
For your deadline:
Do not turn Spatial NicheLinker into a GLiFormer evaluation project.

19. PubTator should absolutely be part of the pipeline
NCBI PubTator already provides biomedical entity annotations and normalization over PubMed/PMC, and PubTator 3.0 exposes entity and relation search through its API. PMC
Use it for:
gene detection
gene normalization
disease identification
species
chemicals
cell lines
literature retrieval support
But:
PubTator annotation is not itself biological evidence.
Your existing architecture already says exactly that: PubTator is an entity-recognition/normalization utility, while PubMed/PMC passages are the actual literature evidence. dpi_knowledge_graph_architectur…

20. The actual extraction pipeline I would build
Papers supplied by collaborators
          +
targeted PubMed / PMC search
                 │
                 ▼
        PDF / XML / abstract
                 │
                 ▼
            section parser
                 │
        ┌────────┴─────────┐
        ▼                  ▼
    PubTator          optional GLiNER2.5
 entity normalization     prefilter
        │                  │
        └─────────┬────────┘
                  ▼
         candidate passages
                  │
                  ▼
        strong LLM extractor
                  │
          strict JSON schema
                  │
                  ▼
      deterministic validation
                  │
       ┌──────────┴──────────┐
       ▼                     ▼
   accepted               uncertain
    claims                 sidecar
       │
       ▼
       KG
No agent swarm.
No autonomous research loop.
No fine-tuning yet.
Just a deterministic ETL pipeline.

21. The LLM should produce this exact kind of record
{
  "tf": {
    "mention": "FOXA2",
    "normalized_symbol": "FOXA2"
  },

  "target_gene": {
    "mention": "SFTPC",
    "normalized_symbol": "SFTPC"
  },

  "relation": "activates",

  "direction": "positive",

  "directness": "direct",

  "evidence_type": "tf_binding_plus_regulatory_effect",

  "assay": [
    "ChIP-seq",
    "knockdown"
  ],

  "context": {
    "species": "human",
    "tissue": "lung",
    "cell_type": "alveolar epithelial cell",
    "disease": null,
    "condition": null,
    "model_system": "primary cell"
  },

  "claim_strength": "experimental",

  "negated": false,

  "source": {
    "pmid": "12345678",
    "section": "Results",
    "supporting_passage": "...",
    "start_offset": 2144,
    "end_offset": 2327
  }
}
Require the extractor to return:
NO_RELATION
when the relationship is not explicit enough.
That abstention is essential.

22. Section weighting matters
For your task:
Results
    >
figure captions
    >
Abstract
    >
Discussion
    >
Introduction
Methods should mainly provide context/assay information.
Reviews are useful to find primary papers, but I would not count a review statement as independent experimental support.
Your earlier KG plan already reached the same design: Results as the strongest location for primary TF→gene claims, methods for context, figure captions as valuable evidence, abstracts as moderate, and reviews largely for discovery rather than primary edge evidence. dpi_knowledge_graph_architectur…

23. Do you need embeddings?
Yes, but only for retrieval.
You do not need a fancy vector database.
For each paper, chunk into:
paragraph
or
2–4 sentences
and embed passages.
Queries can include:
ETV1 transcriptional regulation lung epithelial fibrosis
ETV1 ChIP target
ETV1 knockdown epithelial
ETV1 IPF
ETV1 Hippo YAP
Then send only high-relevance chunks to the LLM.
For a few hundred papers, FAISS or even a local embedding index is enough.
Do not make vector-search infrastructure the project.

24. Should you generate synthetic training data and fine-tune?
Not now.
You currently lack the thing that matters most:
high-quality task-specific gold labels
If you ask an LLM to generate 20,000 examples and then train another model, you have largely taught the student to reproduce the teacher's errors.
There is evidence that LLM-to-small-model distillation can work well in biomedical information extraction; Microsoft researchers demonstrated gains by distilling LLM supervision into PubMedBERT on biomedical extraction tasks. Microsoft
But that is a second-stage engineering/research project, not something you need before Anshunya sees a functioning KG.
PubMedBERT/BiomedBERT remains attractive later because biomedical-domain pretraining substantially improves representations of biomedical terminology relative to generic BERT. Microsoft

25. What I would do later if extraction volume becomes huge
Once your working system has accumulated, say, a substantial set of human-reviewed extraction records, then create:
train
validation
held-out test
split by:
PMID
not by sentence.
Otherwise passages from the same paper leak across train and test.
Even better, hold out some TFs.
Then compare:
LLM
GLiNER2.5 fine-tuned
PubMedBERT relation classifier
for:
relation existence
direction
directness
context
assay
measured-vs-inferred
If the small model works well, replace most expensive LLM calls with it.
That becomes a nice secondary technical contribution.
Not the first deliverable.

26. How the TF nomination should actually work
Do not ask one model:
Give me the best TF.
Create an evidence vector.
For every:
TF × cell type × niche × condition
calculate:
PROJECT EVIDENCE
────────────────────────────
ChromLinker rank
ChromLinker Δ connectivity
TF RNA expression
TF differential expression
target differential expression
target-program overlap
direction consistency


LITERATURE EVIDENCE
────────────────────────────
# direct binding studies
# TF perturbation studies
# reporter studies
# context-matched studies
# lung studies
# cell-type-matched studies
# IPF/fibrosis studies
# independent publications
contradictory studies


PROGRAM EVIDENCE
────────────────────────────
target-set enrichment
pathway coverage
biological-process coverage


OPTIONAL PERTURBATION EVIDENCE
────────────────────────────
Geneformer predicted shift
future Perturb-seq result
Store the vector.
Do not reduce biological truth to:
confidence = 0.91
The previous architecture explicitly warns against ambiguous probability-like truth scores and recommends keeping evidence dimensions distinguishable. dpi_knowledge_graph_architectur…

27. For operational ranking, use rank aggregation rather than inventing “P(TF is causal)”
Suppose ETV1 has:
ChromLinker rank       1
literature rank        4
target enrichment      2
context match          3
expression rank        6
And FOXA2:
ChromLinker rank       3
literature rank        1
target enrichment      4
context match          1
expression rank        2
You can combine those using a reproducible method such as reciprocal-rank fusion.
Something like:
RRF(TF) =
1/(k + rank_ChromLinker)
+
1/(k + rank_literature)
+
1/(k + rank_target_overlap)
+
1/(k + rank_context)
+
1/(k + rank_expression)
with the exact formula/version recorded in TFNomination.
This is a prioritization score, not biological truth.
That's defendable.

28. Another powerful result: evidence categories
Your interface could give researchers something like:
TF
ChromLinker
TF RNA
Literature
Context
Program overlap
Contradictions
ETV1
strong
present
moderate
lung epithelial / partial IPF
strong
0
FOXA2
condition-dependent
strong
strong
lung epithelial
strong
1
TEAD1
Niche1
present
strong
alveolar/lung
strong
0
KLF5
Niche1
present
moderate
epithelial
moderate
0
Then clicking FOXA2 gives:
FOXA2
 │
 ├── ChromLinker evidence
 ├── expression evidence
 ├── 23 literature claims
 │     ├── direct binding
 │     ├── knockdown
 │     ├── association
 │     └── contradictory
 │
 ├── predicted targets overlapping AT1 Niche2
 ├── pathways
 └── PMID evidence
That is far more useful to the scientists than a mysterious AI score.

29. Add Geneformer later as another observation type
The meeting makes it obvious that Geneformer and ChromLinker are complementary.
ChromLinker:
RNA
+
ATAC
+
motif/chromatin information
Geneformer perturbation:
RNA foundation model
+
in-silico perturbation
So represent:
PerturbationPrediction
       │
       ├──PERTURBED_GENE──▶ Gene
       │
       ├──START_STATE─────▶ CellState
       │
       ├──TOWARD_STATE────▶ CellState
       │
       └──GENERATED_BY────▶ AnalysisRun
Then a candidate may show:
ChromLinker          ✓
literature           ✓
Geneformer           ✓
That overlap is exactly the kind of candidate the transcript says they would like to test experimentally.

30. But do not force all methods to agree
This is scientifically important.
You want categories such as:
ChromLinker + literature
ChromLinker only
literature only
Geneformer + literature
ChromLinker + Geneformer
all three
Then future Perturb-seq becomes an external test.
This creates an excellent manuscript analysis:
Which evidence combinations best predict
experimental perturbation outcomes?
That is much stronger than simply showing a network.

31. Your final core relations
This is the relationship vocabulary I would freeze.
BIOLOGY
══════════════════════════════════════════

CellType
   ──HAS_NICHE_STATE────▶ SpatialNicheState

SpatialNicheState
   ──IN_CONTEXT──────────▶ BiologicalContext

SpatialNicheState
   ──HAS_PROGRAM─────────▶ GeneProgram

GeneProgram
   ──CONTAINS_UP_GENE────▶ Gene

GeneProgram
   ──CONTAINS_DOWN_GENE──▶ Gene

GeneProgram
   ──ENRICHED_FOR────────▶ Pathway

Gene
   ──MEMBER_OF_PATHWAY───▶ Pathway

Gene
   ──PARTICIPATES_IN─────▶ BiologicalProcess


REGULATORY LITERATURE
══════════════════════════════════════════

Gene:TF
   ──REGULATOR_OF_CLAIM──▶ RegulatoryClaim

RegulatoryClaim
   ──TARGET_GENE─────────▶ Gene

RegulatoryClaim
   ──IN_CONTEXT──────────▶ BiologicalContext

RegulatoryClaim
   ──HAS_EVIDENCE────────▶ EvidenceAssertion

EvidenceAssertion
   ──SUPPORTED_BY────────▶ Passage

Passage
   ──FROM_PUBLICATION────▶ Publication


PROJECT EVIDENCE
══════════════════════════════════════════

ChromLinkerObservation
   ──PREDICTS_TF─────────▶ Gene:TF

ChromLinkerObservation
   ──PREDICTS_TARGET─────▶ Gene

ChromLinkerObservation
   ──FOR_STATE────────────▶ SpatialNicheState

ChromLinkerObservation
   ──GENERATED_BY─────────▶ AnalysisRun


ExpressionObservation
   ──OF_GENE──────────────▶ Gene

ExpressionObservation
   ──FOR_STATE────────────▶ SpatialNicheState

ExpressionObservation
   ──GENERATED_BY─────────▶ AnalysisRun


PerturbationPrediction
   ──PERTURBED_GENE───────▶ Gene

PerturbationPrediction
   ──START_STATE──────────▶ SpatialNicheState / CellState

PerturbationPrediction
   ──TOWARD_STATE─────────▶ CellState

PerturbationPrediction
   ──GENERATED_BY─────────▶ AnalysisRun


NOMINATION
══════════════════════════════════════════

TFNomination
   ──NOMINATES────────────▶ Gene:TF

TFNomination
   ──FOR_STATE────────────▶ SpatialNicheState

TFNomination
   ──FOR_PROGRAM──────────▶ GeneProgram

TFNomination
   ──SUPPORTED_BY─────────▶ RegulatoryClaim

TFNomination
   ──SUPPORTED_BY─────────▶ ChromLinkerObservation

TFNomination
   ──SUPPORTED_BY─────────▶ ExpressionObservation

TFNomination
   ──SUPPORTED_BY─────────▶ PerturbationPrediction

TFNomination
   ──GENERATED_BY─────────▶ AnalysisRun
That is the schema I would freeze.

32. Optional locus layer
Leave these classes available:
RegulatoryLocus
BindingObservation
LocusGeneLink
because later a claim may say:
FOXA2
   ↓
BindingObservation
   ↓
enhancer chr...
   ↓
LocusGeneLink
   ↓
target gene
The original architecture already provides the exact semantics for these edges—BINDER_IN, AT_LOCUS, FROM_LOCUS, TO_GENE, PERTURBED_TF, and AFFECTS_GENE. dpi_knowledge_graph_architectur…
But do not block the MVP waiting for coordinate-level extraction.

33. What you should actually build first
Because you said you don't have time, I would execute in this order:
	1	Freeze the schema above. Create Neo4j constraints/indexes, HGNC-normalized Gene nodes, CellType, SpatialNicheState, GeneProgram, BiologicalContext, RegulatoryClaim, EvidenceAssertion, Publication, ChromLinkerObservation, and TFNomination.
	2	Load the project's actual biology first. AT1, activated fibrotic fibroblast, alveolar macrophage and KRT5−/KRT17+; their Niche1/Niche2 gene signatures; ChromLinker TF-target scores; TF RNA evidence.
	3	Start only with the top ~15 ChromLinker TFs per relevant lineage, because the meeting explicitly points in that direction. Do not crawl the entire human TFome initially.
	4	Ingest the papers your collaborators already provided. Get PMID/PMCID/DOI, extract Results/abstract/figure-caption passages, run PubTator normalization, and send candidate passages through the structured LLM extractor.
	5	Perform targeted PubMed/PMC expansion for those TFs and their important target/program genes. This fills gaps without becoming a universal literature KG.
	6	Normalize and validate claims deterministically. HGNC symbols, species, context, assay, direction, directness, PMID, source span. Keep uncertain extractions outside the production graph.
	7	Create literature TF target sets and calculate niche-program target enrichment and direction consistency.
	8	Create TFNomination records integrating ChromLinker, program overlap, literature support, context match and RNA evidence.
	9	Return the top candidates plus explanations, not merely a score: TF, evidence streams, pathways, targets, independent studies, contradictions and PMIDs.
	10	Then add Geneformer perturbation output as another evidence stream if the table is available. Fine-tuning extraction models and coordinate-level regulatory-locus evidence come after the functioning KG.

34. What I would not do now
I would not build a universal PubMed KG, ingest the whole genome, build a GNN, train a TF-ranking neural network, build an agentic research system, fine-tune GLiFormer, fine-tune BioBERT before having gold data, ingest GWAS/drugs/QTLs, or model millions of single cells inside Neo4j.
Those things would make you later—and would not answer Anshunya's immediate question any better.

35. The implementation stack
I would use:
Literature retrieval
    PubMed / PMC
    PubTator 3.0

Paper parsing
    PMC XML whenever possible
    Docling/PyMuPDF fallback for PDFs

Entity normalization
    PubTator
    HGNC
    Cell Ontology
    MONDO
    UBERON

Candidate passage retrieval
    BM25 + embeddings

Primary extraction
    strong structured-output LLM
    temperature ~0
    strict schema
    source-span required
    abstention allowed

Optional fast extractor
    GLiNER2.5

Validation
    Python
    Pydantic
    deterministic rules

Storage
    Neo4j = KG
    Parquet/JSONL = extraction warehouse/raw records

Analysis
    Python
    scipy
    pandas
    networkx if needed

API
    FastAPI

Consumers
    Spatial NicheLinker analysis
    LungChat
    LungMAP website
The meeting's “shared backend” concept still works. The website and LungChat should not independently reconstruct the KG; both can consume the same API.

36. What the API should ultimately answer
The killer query is something like:
GET /tf-nominations
    ?cell_type=AT1
    &niche=Niche2
    &disease=IPF
Response:
{
  "candidate": "ETV1",

  "project_evidence": {
    "chromlinker": "strong_niche2_enrichment",
    "tf_expression": "detected",
    "program_overlap": 0.31
  },

  "literature": {
    "supporting_claims": 11,
    "direct_binding": 2,
    "perturbation": 3,
    "lung_context": 6,
    "ipf_context": 1,
    "independent_studies": 7,
    "contradictions": 0
  },

  "programs": [
    "epithelial morphogenesis",
    "Hippo/YAP",
    "cell projection"
  ],

  "status": "PRIORITIZED",

  "citations": [
    "PMID:...",
    "PMID:..."
  ]
}
And then LungChat can answer:
Why was ETV1 nominated for IPF AT1 Niche2?
with actual evidence paths.
That is a meaningful KG product.

37. The manuscript benefit
Your current result ends approximately at:
populations associated with different cellular neighborhoods exhibit distinct inferred TF-gene networks.
The KG lets you add a much stronger next analysis:
ChromLinker candidates
       ↓
independent literature evidence graph
       ↓
context-aware prioritization
       ↓
cross-evidence TF nomination
Potential Results framing later:
Literature-grounded evidence prioritizes candidate regulators of neighborhood-associated states.
Then you can show:
AT1
Niche1 candidate evidence
Niche2 candidate evidence

Macrophage
resident-program evidence
remodeling-program evidence

Fibroblast
Niche1/Niche2 regulatory candidates
And crucially:
ChromLinker-only
Literature-only
Concordant
Context-limited
Contradictory
That's a real scientific analysis, not a decorative KG.

38. My final answer on the model question
If I were sitting in your position and needed this running soon:
Primary: PubTator + strong LLM structured extraction + deterministic validation + Neo4j.
If literature volume starts making LLM extraction expensive:
Add GLiNER2.5 as the local high-recall front end.
If you eventually accumulate high-quality corrected extractions:
Fine-tune GLiNER2.5 and/or PubMedBERT/BiomedBERT and benchmark them against the LLM.
I would not use GLiFormer for this deliverable.
I would not fine-tune anything before building the KG.
And I would not make NER the centerpiece, because the scientific problem is contextual TF→target evidence extraction and nomination, not finding gene strings in text.
The final project in one sentence is:
Spatial NicheLinker identifies neighborhood-associated cell states and candidate regulatory programs; the regulatory evidence KG integrates ChromLinker, transcriptional, pathway, literature, and optionally perturbational evidence to nominate and explain context-specific transcription factors for experimental follow-up.
That is now the design I would build.



Yes. With the deadline and the fact that there will be no human curator reviewing every extracted claim, I would simplify the system further and freeze it now.
The biggest correction from our previous design is this:
Do not build a general paper-understanding system. Build a high-precision TF-nomination pipeline.
Parse only the parts of papers that can materially change a TF nomination.
I inspected the attachment your advisor sent. It is a strong starting resource, but it is a literature-search package, not a finished evidence corpus: metadata, abstracts, search scripts, 46 TF/disease papers, 71 experimental-edge papers, and screening logs. There are 110 unique PMIDs because seven occur in both lists. The package itself says full text was not read and experimental accessions remain to be collected. TF_target_disease_literature
My final decisions
Question
Decision
Parse full papers?
Yes, selectively
Parse every figure visually?
No
Extract figure captions?
Yes
Parse tables?
Yes
Parse supplementary information?
Yes, selectively and especially structured tables
content.md?
Yes, convenience representation
figures/?
No by default
tables/?
Yes
supplementary/?
Yes
LiteParse?
No for the main pipeline
Docling?
Only for PDF fallback
PMC/Europe PMC XML?
First choice
GLiNER/GLiNER2.5?
Not required for MVP
LLM?
Yes, structured claim extraction + verification
Fine-tune model?
No
Agentic workflow?
No
Neo4j?
Yes
FalkorDB?
Not now
SQL-only?
No
Raw data store?
Files/Parquet + Neo4j for graph
Advisor's papers sufficient?
Good seed, not sufficient final corpus
Search more literature?
Yes, dynamically for your actual candidate TFs

1. Do you need figures?
Not by default.
This is where I would save you a huge amount of effort.
A scientific PDF might have:
Results text
Figure caption
Figure image
Supplementary tables
Underlying GEO data
For your KG, the ordering should be:
Structured supplementary table / source data
            ↓
Results text
            ↓
Figure caption
            ↓
Main-text table
            ↓
Abstract
            ↓
Figure image itself
Figure pixels are the last resort.
Why?
Your graph does not need to know whether a bar in Figure 4 is 1.73 versus 1.51. It needs to know something like:
TEAD1
   ACTIVATES
TWIST1

evidence:
ChIP + reporter assay

context:
lung fibroblast

publication:
PMID...
Usually the Results text and figure caption explicitly describe this.
A good example surfaced in the literature: a pulmonary-fibrosis study states in its text/caption that YAP1/TEAD1 was associated with the TWIST1 promoter, and also reports ChIP, qPCR and luciferase experiments. You do not need computer vision to recover the main regulatory assertion. PMC
Similarly, the YAP1/TEAD1→PRDX3 fibrosis study explicitly describes ChIP, perturbation and promoter experiments in the full text. PMC
Therefore:
Don't create:
figures/
    figure1.png
    figure2.png
    figure3.png
    ...
for every paper.
Instead create:
figure_captions.jsonl
containing:
{
  "figure": "Fig. 5",
  "caption": "...",
  "section": "Results",
  "pmid": "...",
  "page": 8
}

2. When should you actually parse a figure image?
Only trigger visual extraction when all three are true:
1. TF/target is high priority

AND

2. text/caption says the result exists

AND

3. the actual evidence needed for the claim is only represented visually
Example:
“Expression changes are shown in Figure 5.”
with no explanation elsewhere.
Then you could crop that specific figure and run a vision model.
Do not systematically VLM every figure.
Especially with no human review, I would rather have:
claim_status = insufficient_text_evidence
than hallucinate a regulatory relationship from a complicated heatmap.

3. Tables are different: yes, parse them
Tables are much more useful.
And sometimes the actual TF-target network exists only in a supplementary table.
There are real examples of exactly this. The RFX2 study provides supplementary/source-data files containing hundreds of direct target genes with binding and expression measurements. eLife
Likewise, some regulatory studies expose large supplementary XLSX tables containing their actual genomic results. PMC
Therefore:
Tables and structured supplementary data are more important for your KG than figure images.

4. Yes, supplementary information matters
But again: do not parse everything indiscriminately.
Prioritize:
.csv
.tsv
.xlsx
.xls
Then:
.docx
.html
.xml
Then, only if necessary:
supplementary PDF
Ignore initially:
supplementary images
videos
PowerPoint
giant unrelated supplements
Europe PMC has a specific API for downloading supplementary files and full-text XML; it also exposes publication metadata and references. Europe PMC
NCBI also now exposes PMC Open Access supplementary material in BioC form. NCBI
Interestingly, Europe PMC expanded text mining of supplementary files in 2025 and reports tens of millions of biological-term/data-accession annotations from supplements. That reinforces that supplemental files contain scientifically useful information that ordinary abstract mining misses. Europe PMC News Blog

5. Do not PDF-parse when XML exists
This is probably the biggest architecture simplification.
Your acquisition hierarchy should be:
PMID
 │
 ▼
Does PMC / Europe PMC have structured full text?
 │
 ├── YES ──▶ XML / BioC
 │
 │
 │          Extract:
 │          - sections
 │          - paragraphs
 │          - captions
 │          - tables
 │          - supplementary links
 │          - references
 │
 └── NO
      │
      ▼
Is an accessible PDF available?
      │
      ├── YES ──▶ Docling
      │
      └── NO ──▶ abstract only
PMC's text-mining datasets provide structured full text, but not every PMC article is legally available for automated reuse; PMC explicitly says to use its authorized APIs/services and honor article licenses. PMC
PubTator itself consumes BioC PubMed abstracts and PMC Open Access full text. PMC
So XML-first is actually closer to the way major biomedical NLP infrastructure already works.

6. LiteParse or Docling?
For your project:
Use Docling only as the PDF fallback.
Don't maintain two PDF parsers right now.
LiteParse is genuinely fast and can output Markdown, layout blocks, images, tables and spatial metadata. But its own documentation describes Markdown reconstruction as heuristic/rule-based and acknowledges that difficult multi-column documents and dense tables can be imperfect. GitHub
Docling's full PDF pipeline has explicit:
	•	layout recognition,
	•	OCR,
	•	table-structure extraction,
	•	figure detection,
	•	image extraction,
	•	structured document representation. Docling
It can also export figure/table images if you eventually need them. Docling
Therefore:
PMC XML              → native XML parser
Europe PMC XML       → native XML parser

PDF fallback         → Docling

LiteParse            → don't add right now
You don't gain enough from a second PDF engine to justify the extra pipeline branch.

7. Your per-paper folder should look like this
Yes, something roughly like content.md / tables / supplements, but slightly better:
papers/
└── PMID_12345678/
    │
    ├── metadata.json
    │
    ├── source/
    │   ├── article.xml
    │   └── article.pdf              # only if needed / permitted
    │
    ├── parsed/
    │   ├── document.json
    │   ├── content.md
    │   ├── sections.jsonl
    │   ├── figure_captions.jsonl
    │   │
    │   └── tables/
    │       ├── table_01.csv
    │       └── table_02.csv
    │
    ├── supplementary/
    │   ├── raw/
    │   │   ├── supp1.xlsx
    │   │   └── supp2.pdf
    │   │
    │   └── parsed/
    │       ├── supp1.csv
    │       └── supp2.md
    │
    ├── extraction/
    │   ├── candidate_passages.jsonl
    │   ├── regulatory_claims.jsonl
    │   └── rejected_claims.jsonl
    │
    └── provenance/
        └── ingestion_run.json
One change:
Do not maintain figures/ yet.
Just keep:
figure_captions.jsonl
If an individual figure needs visual parsing later, add it on demand.

8. document.json should be canonical, not content.md
content.md is convenient for debugging and LLM input.
But Markdown loses information.
The canonical parsed representation should retain:
section
paragraph
page
offset
table ID
figure ID
caption linkage
source file
So:
document.json
is canonical.
And:
content.md
is derived convenience output.
This matters because every KG claim needs a provenance path like:
RegulatoryClaim
     ↓
EvidenceAssertion
     ↓
Passage
     ↓
PMID
section = Results
paragraph = 17
offset = 5138–5492

9. Do you need an agentic process?
No.
Not for this.
Please don't build:
Retriever Agent
     ↓
Paper Agent
     ↓
Figure Agent
     ↓
Skeptic Agent
     ↓
Validation Agent
     ↓
KG Agent
That is unnecessary architecture and another source of nondeterminism.
Use a normal deterministic pipeline:
retrieve
  ↓
parse
  ↓
normalize entities
  ↓
retrieve candidate passages
  ↓
structured LLM extraction
  ↓
automated verification
  ↓
claim validation
  ↓
Neo4j upsert
  ↓
TF nomination
It can be Python functions.
No LangGraph required.
No DeepAgents required.
No autonomous planner required.

10. But because you have no human reviewer, I WOULD use two LLM passes
This is important.
Human review normally catches:
negation
association mistaken for causation
TF family mistaken for individual TF
mouse/human mismatch
cancer-cell-line vs AT1 mismatch
review article interpreted as primary evidence
binding mistaken for functional regulation
You don't have that safety net.
So do:
PASS 1
LLM extractor
      ↓
structured RegulatoryClaim

PASS 2
LLM verifier
      ↓
VALID / INVALID / UNCERTAIN
The second model receives:
original passage
+
proposed extraction
and asks only:
Does this source passage actually support this exact claim?
It does not search.
It does not revise the claim creatively.
It is a classifier/verifier.
That's still not “agentic.”

11. Automatic acceptance policy
Since you have no reviewer, optimize for precision, not recall.
Accept a literature edge automatically only when:
normalized TF exists
normalized target gene exists

AND

source span explicitly mentions or unambiguously supports relationship

AND

extractor and verifier agree

AND

claim isn't negated

AND

species is known or explicitly unknown

AND

source PMID is retained

AND

evidence type is known

AND

context is retained

AND

directness is not inferred beyond the assay

AND

publication is primary research for experimental claims
Otherwise:
status = UNCERTAIN
Keep it in Parquet/JSONL.
Don't put it into the nomination evidence score.
This is how you survive without human curation.

12. PubTator still comes first
Use PubTator for:
Gene
Disease
Species
Cell line
Chemical
Variant
normalization.
PubTator 3.0 now runs entity recognition/normalization and BioREx relation extraction over PubMed abstracts and PMC-OA articles; its API supports entity and relation search. PMC
But BioREx's relation ontology is broad biomedical gene-gene/disease/chemical relations.
It does not solve your exact ontology:
TF DIRECTLY BINDS target promoter
TF ACTIVATES target
TF REPRESSES target
TF perturbation changes target
TF is only correlated with target
So PubTator provides candidate entities and retrieval.
The LLM provides your project-specific relation semantics.

13. GLiNER2.5: postpone it
GLiNER2.5 has become substantially more useful: current documentation supports schema-conditioned entities, relations, records, long-document chunking and joint IE. GitHub
But it still does not eliminate your core problem:
extracting scientifically correct directness + assay + biological context + direction from biomedical prose.
And right now you don't have a domain-specific benchmark for it.
So:
Phase 1:
PubTator + LLM

Phase 2:
benchmark GLiNER2.5 against accepted extraction records

Phase 3:
possibly replace expensive LLM pass
No model fine-tuning now.

14. The advisor attachment is actually extremely useful
What your advisor did is basically give you the starting retrieval backbone.
It has two complementary groups. TF_target_disease_literature
The first corpus is essentially:
lung disease context
+
lung atlases/resources
+
lung regulatory-network papers
+
general TF-target databases
The second is:
actual experimentally measured edges
+
TF-DNA binding
+
perturbation
+
cell-context TF catalogs
+
PPI
That maps extremely well to what we designed.
Conceptually:
Advisor Tier A
    ↓
CELL / DISEASE CONTEXT

Advisor Tier B
    ↓
LUNG REGULATORY MODELS

Advisor Tier C
    ↓
GENERAL TF→TARGET PRIOR

Advisor Tier D
    ↓
DISEASE ASSOCIATIONS


Advisor T1
    ↓
BINDING EVIDENCE

Advisor T2
    ↓
FUNCTIONAL / PERTURBATION EVIDENCE

Advisor T3
    ↓
LARGE TF-DNA CATALOGS

Advisor T4
    ↓
COFACTORS / PPI
That is why the material is useful.

15. But it is not sufficient
There are three major reasons.
First: it is abstract-level
The README explicitly says no full text was read. TF_target_disease_literature
For your graph you need:
TF
target
direction
assay
cell type
species
condition
directness
Abstracts often don't give that.
Second: it has a 2015–2026 cutoff
That is fine for recent resources.
It is not fine for mechanistic biology.
For example, a relevant direct GATA6/alveolar epithelial target paper goes back to 2008 and contains promoter, ChIP and reporter evidence involving GATA6 and AQP5. PMC
Another important GATA6/alveolar differentiation paper predates 2015. PMC
You would lose valid mechanistic evidence by imposing 2015 as the lower bound.
Third: your actual Spatial NicheLinker TFs appeared after this search strategy was written
Your current manuscript now has:
TEAD1
KLF5
GATA6
FOXA2
ETV1

SPI1
EGR2
BHLHE41
TFEC
IRF8
CEBPB

RFX2
FOSB
...
The provided curated metadata covers some of these well—especially NKX2-1-related biology, some FOXA2, and EGR2—but leaves many of your current candidates poorly represented.
And online research immediately finds highly relevant evidence outside the attachment.
For example, KLF5 has a dedicated lung-development/regeneration study demonstrating a role in AT1 lineage commitment. PubMed
TEAD1/YAP has experimental fibrosis literature, including ChIP/promoter evidence. PMC
BHLHE40/BHLHE41 have an alveolar-macrophage study with genetic loss, transcriptional effects and genome-wide BHLHE40 DNA binding. PMC
Recent IPF work also connects YAP/TAZ/TEAD programs with aberrant alveolar epithelial states. PMC
So yes, expand the corpus.

16. But don't do another giant generic PubMed sweep
Make the expansion candidate driven.
This is the pipeline I would now implement, exactly:
	1	Load the advisor's 110 unique seed PMIDs and tag every source by its existing tier.
	2	Load your actual Spatial NicheLinker/ChromLinker outputs: parent cell type, Niche1/Niche2, condition, TF, target gene, connection score and differential connectivity.
	3	Keep the top ~15 TFs per relevant cell-type/niche comparison initially.
	4	Get a second candidate list from CollecTRI enrichment against the niche gene program, so literature can nominate TFs that ChromLinker missed. CollecTRI provides signed TF-target interactions and, where available, supporting PMIDs. decoupler
	5	Add TRRUST as another curated literature prior. TRRUST explicitly curated TF-target relationships from literature and retained activation/repression evidence; its original curation criteria included TF perturbation, promoter binding and binding-site experiments. PMC
	6	Add hTFtarget as a binding-oriented prior. It integrates thousands of human ChIP-seq datasets and condition/tissue-specific TF-target relationships. PMC
	7	Add KnockTF for perturbational support. KnockTF 2.0 contains more than a thousand curated human TF/cofactor perturbation datasets plus hundreds from mouse. PMC
	8	For each candidate TF, run targeted PubMed/Europe PMC searches without a lower-year limit using TF name + lung/alveolar/airway/macrophage/fibroblast/IPF + binding/perturbation terms.
	9	For high-ranking ChromLinker TF-target pairs, issue targeted pair searches such as TEAD1 AND targetGene, rather than searching all PubMed indiscriminately.
	10	Fetch structured PMC/Europe PMC full text where available; otherwise use abstract; only PDF-parse when structured text is unavailable.
	11	Parse structured supplementary files for the most important experimental papers.
	12	Run PubTator normalization → LLM extraction → verifier → deterministic validation.
	13	Upsert validated evidence into Neo4j.
	14	Compute TF nomination features.
	15	Expose nominations through FastAPI to both LungChat and the website.
That's the build.

17. Do not use the advisor's resource databases as independent votes
This matters scientifically.
Suppose:
Cistrome says TEAD1 → GeneX
ChIP-Atlas says TEAD1 → GeneX
hTFtarget says TEAD1 → GeneX
TFTG says TEAD1 → GeneX
Those might all derive from:
the same GEO ChIP-seq experiment
Do not count that as four experiments.
Your old DPI-KG design correctly required evidence deduplication by underlying experiment/study rather than database. dpi_knowledge_graph_architectur…
TFTG itself describes gathering ChIP-seq from multiple source databases and deduplicating by GEO/SRA identifiers, demonstrating why this matters. PMC
So keep:
source_database
source_accession
PMID
GEO/SRA accession
where available.

18. Now the database decision: Neo4j
Use:
Neo4j Community Edition for the graph.
Don't use SQL-only.
Don't switch to FalkorDB right now.
Why not SQL only?
Your central queries are graph-pattern queries:
Niche2
 → GeneProgram
 → target genes
 ← RegulatoryClaim
 ← TF
 → other target genes
 → Pathway
and:
TF
 → RegulatoryClaim
 → Evidence
 → Passage
 → Publication
and:
TF
 → target
 → target TF
 → downstream genes
You can implement that through relational joins.
But you've intentionally built a knowledge graph.
Don't convert it back into:
15 tables + recursive joins
unless you have a strong operational reason.

19. Why Neo4j instead of FalkorDB?
FalkorDB is not bad.
Its current documentation supports:
property graph
OpenCypher
full-text
vector indexes
range indexes
Bolt/RESP
and it uses sparse-matrix storage. FalkorDB Docs
It can be very fast and lightweight.
But that is not your bottleneck.
You're going to have perhaps:
thousands / tens of thousands of genes/claims
maybe hundreds of thousands of evidence relationships
not billions of rapidly changing social-network edges.
Your bottleneck is:
literature quality
normalization
context
evidence typing
TF nomination
not graph traversal latency.
Also note FalkorDB's own comparison benchmarks are vendor-published, so I would not choose the scientific platform based on those alone. FalkorDB Knowledge Graph Database

20. Neo4j gives you what you need now
Neo4j has:
	•	native nodes/relationships,
	•	Cypher,
	•	indexes,
	•	full-text,
	•	vector indexes if you later want them,
	•	Python drivers,
	•	Browser visualization. Neo4j Graph Intelligence Platform
Neo4j Browser already gives you interactive graph visualization, which will be useful when showing the KG to collaborators. Neo4j Graph Intelligence Platform
Community Edition remains GPLv3 and is free for a project that doesn't require enterprise HA/security features. Neo4j Graph Intelligence Platform
So freeze this:
Neo4j Community
+
Python
+
FastAPI
No graph-database comparison project.

21. Do you need another SQL database?
No.
For now:
Raw files
    ↓
filesystem / object storage

Parsed tables and extraction records
    ↓
Parquet / JSONL

Canonical scientific graph
    ↓
Neo4j
That's enough.
You don't need:
Postgres
+
Neo4j
+
vector database
+
FalkorDB
That is architecture for architecture's sake.
Use Parquet for big flat outputs because you already know how to manipulate it efficiently.

22. Final Neo4j schema
I would reduce it to this exact v1:
(:Gene)
(:CellType)
(:SpatialNicheState)
(:GeneProgram)
(:Pathway)
(:BiologicalContext)

(:RegulatoryClaim)
(:EvidenceAssertion)

(:Publication)
(:Passage)
(:Experiment)

(:ChromLinkerObservation)
(:ExpressionObservation)
(:PerturbationPrediction)

(:TFNomination)
(:AnalysisRun)
Optional later:
(:RegulatoryLocus)
(:BindingObservation)
(:LocusGeneLink)

23. Relations
(:CellType)
  -[:HAS_NICHE_STATE]->
(:SpatialNicheState)


(:SpatialNicheState)
  -[:HAS_PROGRAM]->
(:GeneProgram)


(:GeneProgram)
  -[:CONTAINS_GENE {direction, logFC, qvalue}]->
(:Gene)


(:GeneProgram)
  -[:ENRICHED_FOR]->
(:Pathway)


(:Gene {is_tf:true})
  -[:REGULATOR_OF]->
(:RegulatoryClaim)


(:RegulatoryClaim)
  -[:TARGET_GENE]->
(:Gene)


(:RegulatoryClaim)
  -[:IN_CONTEXT]->
(:BiologicalContext)


(:RegulatoryClaim)
  -[:HAS_EVIDENCE]->
(:EvidenceAssertion)


(:EvidenceAssertion)
  -[:SUPPORTED_BY]->
(:Passage)


(:Passage)
  -[:FROM_PUBLICATION]->
(:Publication)


(:EvidenceAssertion)
  -[:DERIVED_FROM]->
(:Experiment)


(:ChromLinkerObservation)
  -[:PREDICTS_TF]->
(:Gene)


(:ChromLinkerObservation)
  -[:PREDICTS_TARGET]->
(:Gene)


(:ChromLinkerObservation)
  -[:FOR_STATE]->
(:SpatialNicheState)


(:ExpressionObservation)
  -[:OF_GENE]->
(:Gene)


(:ExpressionObservation)
  -[:FOR_STATE]->
(:SpatialNicheState)


(:PerturbationPrediction)
  -[:PERTURBED_GENE]->
(:Gene)


(:TFNomination)
  -[:NOMINATES]->
(:Gene {is_tf:true})


(:TFNomination)
  -[:FOR_STATE]->
(:SpatialNicheState)


(:TFNomination)
  -[:FOR_PROGRAM]->
(:GeneProgram)


(:TFNomination)
  -[:SUPPORTED_BY]->
(:RegulatoryClaim | :ChromLinkerObservation |
 :ExpressionObservation | :PerturbationPrediction)
Freeze that.

24. Evidence types
EvidenceAssertion.evidence_type should be one of:
TF_BINDING
TF_PERTURBATION
TF_BINDING_PLUS_PERTURBATION
REPORTER_ASSAY
CRE_PERTURBATION
EXPRESSION_ASSOCIATION
COMPUTATIONAL_NETWORK
CURATED_LITERATURE
PROTEIN_INTERACTION
And:
directness:

DIRECT
FUNCTIONAL
ASSOCIATIVE
PREDICTED
UNCLEAR
Keep those separate.

25. Context
You need:
species
tissue
cell_type
disease
condition
model_system
For example:
human
lung
AT1
IPF
Niche2
primary tissue
But remember:
Niche2 remains SpatialNicheState, not part of reusable biological context.

26. TF nomination should have two entry routes
This is important.
Route A — ChromLinker first
ChromLinker TF
      ↓
literature validation
      ↓
nomination
Route B — literature first
Niche gene program
      ↓
CollecTRI / TRRUST / hTFtarget enrichment
      ↓
candidate TF
      ↓
literature validation
      ↓
nomination
Therefore the KG isn't just confirming ChromLinker.
It can nominate something that ChromLinker missed.
That's likely what your advisor means by wanting the KG to nominate TFs based on literature.

27. Candidate ranking
Don't create:
ETV1 causal probability = 0.91
Instead calculate dimensions:
chromlinker_support
program_target_enrichment
direction_concordance

tf_expression_support

literature_direct_binding
literature_perturbation
literature_reporter

lung_context_support
cell_type_context_support
ipf_context_support

independent_study_count
contradiction_count

collectri_support
trrust_support
htftarget_support

geneformer_support
Then produce a deterministic nomination_rank.
The actual evidence vector remains visible.

28. Your automatic evidence tiers
Since you have no human review, I recommend simple rule-based tiers:
Tier
Requirement
A
Direct binding and functional perturbation, relevant lung/cell context
B
Binding or perturbation in relevant/closely related context
C
Directional curated literature evidence but context-limited
D
Computational/predicted evidence only
U
Uncertain/contradictory extraction
This is a lot safer than asking an LLM for:
confidence = 0.93

29. One important upgrade to your advisor's queries
Their existing scripts are useful.
But I would modify them in two ways.
Remove the 2015 lower date boundary for mechanistic evidence.
Use all years for:
TF-target regulation
ChIP
reporter assay
knockdown
knockout
direct targets
Dynamically inject the current candidates.
For AT1:
TEAD1
KLF5
GATA6
FOXA2
ETV1
For AM:
SPI1
EGR2
BHLHE41
TFEC
IRF8
CEBPB
etc.
That would already find biology the original curated final table missed.

30. The exact software architecture
                       Spatial NicheLinker
                              │
                     ChromLinker outputs
                              │
                              ▼
                    project_loader.py
                              │
                              ▼
                       Neo4j project nodes
                              │
                              │
        ┌─────────────────────┴──────────────────────┐
        │                                            │
        ▼                                            ▼
 Advisor seed corpus                         Dynamic TF searches
        │                                            │
        └─────────────────────┬──────────────────────┘
                              ▼
                       literature_fetch.py
                              │
               ┌──────────────┴───────────────┐
               ▼                              ▼
         PMC/Europe PMC XML                PDF only
               │                              │
               │                              ▼
               │                           Docling
               │                              │
               └──────────────┬───────────────┘
                              ▼
                        normalized document
                              │
                              ▼
                           PubTator
                              │
                              ▼
                   candidate passage retrieval
                              │
                              ▼
                     structured LLM extractor
                              │
                              ▼
                         LLM verifier
                              │
                              ▼
                    deterministic validation
                              │
                 ┌────────────┴─────────────┐
                 ▼                          ▼
             ACCEPTED                    UNCERTAIN
                 │                          │
                 ▼                          ▼
               Neo4j                 JSONL / Parquet
                 │
                 ▼
              nomination.py
                 │
                 ▼
                    TFNomination nodes
                 │
                 ▼
                         FastAPI
                     ┌──────┴──────┐
                     ▼             ▼
                  LungChat      LungMAP UI
That is the project.

31. What you should start coding first
The first code I would write is not Docling, an agent, GLiNER, or a fancy UI.
It is:
schema/
    models.py

ingest/
    load_spatial_niche.py
    load_chromlinker.py
    load_advisor_seed.py

literature/
    search.py
    fetch.py
    parse_xml.py
    parse_pdf.py
    pubtator.py
    extract_claims.py
    verify_claims.py

graph/
    neo4j.py
    upsert.py

analysis/
    tf_enrichment.py
    nomination.py

api/
    app.py
And make models.py contain your Pydantic contracts for:
Paper
Passage
BiologicalContext
RegulatoryClaim
EvidenceAssertion
ChromLinkerObservation
TFNomination
Once those objects are correct, the rest becomes ETL.

32. What I would aim to show Anshunya first
Don't wait for the entire literature universe.
Build AT1 first.
Put in:
TEAD1
KLF5
GATA6
FOXA2
ETV1
and the AT1 Niche1/Niche2 program.
Then produce:
TF    ChromLinker   Literature   Direct evidence   Lung context   Program overlap
-----------------------------------------------------------------------------------
TEAD1 ...
KLF5  ...
GATA6 ...
FOXA2 ...
ETV1  ...
with:
click TF
   ↓
show targets
   ↓
show pathway
   ↓
show exact passage
   ↓
show PMID
Once that works, run exactly the same pipeline for:
alveolar macrophage
fibroblast
KRT5-/KRT17+
That gets you something scientifically useful fast, while keeping the architecture capable of growing into the larger KG later.
And the additional online literature actually makes me more confident this approach is useful: the papers outside your advisor's seed already contain exactly the kinds of evidence you need—KLF5/AT1 lineage biology, TEAD/YAP experimental lung-fibrosis mechanisms, BHLHE40/41 alveolar-macrophage regulation, older GATA6 direct epithelial regulatory evidence, and structured RFX2 target tables. PubMed
So the answer is not “parse more stuff.” It is parse the right evidence, preserve provenance, and make TF nomination the center of the system.




You mainly need two CSVs from Shunya. Don’t ask him for raw matrices yet.
1. chromlinker_edges.csv — most important
Ask for one row per inferred TF→target edge:
Column
Example
cell_type
AT1
condition
IPF
niche
Niche2
tf
ETV1
target_gene
AREG
chromlinker_score
0.82
comparison
Niche2_vs_Niche1
delta_score
0.31
rank
4
motif
ETS
dataset
Yale_multiome
analysis_version
v1
Ask for all edges, not only top 15, if the file size is manageable. We can filter/rank ourselves.
2. niche_signatures.csv
One row per gene per niche:
Column
Example
cell_type
AT1
condition
IPF
niche
Niche2
gene
KRT17
log2FC
1.8
p_value
...
q_value
...
direction
up
dataset
Yale_multiome
comparison
Niche2_vs_Niche1
If available, add:
pct_expression_niche1
pct_expression_niche2
mean_expression_niche1
mean_expression_niche2
These two files are enough to start the KG + dynamic literature retrieval.
Helpful third file, if easy
tf_summary.csv:
cell_type
condition
niche
tf
tf_expression
tf_log2FC
tf_qvalue
chromlinker_aggregate_score
chromlinker_rank
number_of_targets
But we can calculate much of this ourselves from files 1–2.
Also ask him for this metadata once
Just a tiny README/text file:
dataset name/accession
species
tissue
number of donors/samples
Control/IPF definition
Niche1/Niche2 definition
gene identifier type (HGNC symbols?)
exact meaning of ChromLinker score
how delta_score was calculated
software/version/run used
You can send Shunya this:
Can you send me two CSVs for the KG?1. ChromLinker edges: cell_type, condition, niche, TF, target_gene, ChromLinker score, comparison, delta/differential score, rank, motif if available, dataset/run version. Ideally all TF-target edges rather than only top hits.2. Niche gene signatures: cell_type, condition, niche, gene, log2FC, p/q-value, direction and dataset/comparison. Expression percentages/means if readily available.Also please include a short description of what the ChromLinker score/delta mean and the dataset/run version.
With those, I can dynamically search literature for TFs, TF-target pairs, and TFs whose known targets overlap each niche program.



I checked both files. The ChromLinker file is good. The pseudobulk expression file is useful, but it does not replace the niche-signature/DE file.
The Yale_IPF_with_Niches_tf_to_gene_connection_scores_log10.csv already gives us what we need for the regulatory side: each row is TF → Gene, and the columns give connection scores for contexts such as Control.AT1_niche_1, Control.AT1_niche_2, IPF.AT1_niche_1, IPF.AT1_niche_2, macrophage niches, fibroblast niches, etc. So Shunya does not need to make another ChromLinker summary file. We can reshape it ourselves and calculate Niche2–Niche1 differences and ranks.
The spatial_niche_pseudobulk_CPTT.txt has gene-level pseudobulk expression for those same kinds of condition/cell/niche groups—for example Control/IPF AT1 niche 1/2, macrophage niche 1/2, fibroblast niches, etc. spatial_niche_pseudobulk_CPTT This is enough for expression support and we can calculate expression ratios/log-fold-change-like summaries ourselves.
But it is not sufficient for statistical differential-expression evidence, because it does not contain:
p-value
adjusted p / q-value
per-donor replicates
% expressing cells
So I would reply to Shunya:
Thanks! I checked both files.
The ChromLinker TF-gene connection-score matrix is sufficient — I can reshape it and calculate niche/condition-specific differences and TF rankings myself.
The pseudobulk CPTT expression matrix is also useful and sufficient for expression-level support. However, if available, I would still need the differential-expression/signature output used for the manuscript, ideally with:
	•	cell type
	•	condition
	•	niche/comparison
	•	gene
	•	log2FC
	•	p-value
	•	adjusted p/q-value
	•	% expressing in each group, if available
If that DE/signature table already exists, please just send me the path; no need to create anything new beyond that.
So from Shunya, we are essentially one file away:
ChromLinker matrix → received ✅Pseudobulk expression → received ✅Niche1 vs Niche2 DE/statistics table → still needed if it exists.




Yes. We have enough to start now; Shunya's DE file can simply plug in later.
I checked the data already:
	•	ChromLinker: 26,822 TF→gene rows, 280 TFs, 5,541 target genes, with niche-specific scores.
	•	Pseudobulk RNA: 36,601 genes across Control/IPF cell populations, including the relevant niche groups. spatial_niche_pseudobulk_CPTT
	•	We already have 12 niche contexts present in both files, including:
	◦	Control AT1 Niche1/2
	◦	IPF AT1 Niche1/2
	◦	Control alveolar macrophage Niche1/2
	◦	IPF alveolar macrophage Niche1/2
	◦	IPF activated fibrotic fibroblast Niche1/2
	◦	IPF KRT5−/KRT17+ Niche1/2
So we can start these immediately:
	1	Reshape ChromLinker into:TF | target_gene | condition | cell_type | niche | score
	2	Calculate Niche1-vs-Niche2 TF/target differences and TF rankings.
	3	Reshape the pseudobulk matrix and attach TF/target expression support.
	4	Create the Neo4j schema + import tables for Gene, TF, NicheState, ChromLinkerObservation, ExpressionObservation, etc.
	5	Generate the dynamic literature search queue from actual TFs/targets in the dataset.
	6	Start the advisor-paper + PubMed/PMC literature ingestion/extraction pipeline.
	7	When Shunya sends the DE table, add:log2FC, p/q, direction, % expressed into the existing observations—no redesign needed.
So we should not wait for him. The DE file is enrichment, not a blocker.
The first useful milestone now is: turn these two files into our normalized project evidence tables and identify the initial TF candidate/search list.


Yes — **these are very useful**, and they actually complete an important part of the architecture we were missing.

I inspected both files. Here is what they change.

## 1. `Yale_pooled_niche_expression_signatures.tsv`

This is a much better expression-signature file than the pseudobulk matrix for our KG purposes.

It has **257,528 rows = 32,191 genes × 8 cell-type/condition comparisons**, covering:

- AT1 — Control, IPF
- Alveolar Macrophages — Control, IPF
- Activated Fibrotic Fibroblasts — Control, IPF
- KRT5neg/KRT17pos — Control, IPF

Every row contains:

```text
dataset
cell_type
condition
comparison
gene

mean_log_normalized_expression_niche_1
mean_log_normalized_expression_niche_2

niche_2_minus_niche_1_mean_log_normalized_expression

pct_expressing_niche_1
pct_expressing_niche_2

n_cells_niche_1
n_cells_niche_2

effect_definition
```

And importantly, the comparison is consistently:

```text
niche_2_vs_niche_1
```

with the effect explicitly defined as:

> **mean log-normalized expression, Niche 2 minus Niche 1**

So we now have a very clean quantitative niche-expression layer.

### Example: IPF AT1

Some of the genes we have already discussed show the expected kind of niche-specific signal descriptively:

| Gene | Niche2 − Niche1 mean expression | % N1 | % N2 |
|---|---:|---:|---:|
| CD44 | +0.778 | 5.1% | 39.9% |
| AREG | +0.532 | 11.0% | 34.1% |
| ETV1 | +0.428 | 3.9% | 25.9% |
| GDF15 | +0.260 | 1.3% | 15.3% |
| TM4SF1 | +0.143 | 15.2% | 25.7% |
| GFPT1 | +0.133 | 18.4% | 29.8% |
| XBP1 | +0.053 | 0.5% | 3.7% |

This is very useful because, for example, **ETV1 now has both a ChromLinker regulatory signal and a descriptive expression difference in the same IPF AT1 niche comparison**.

But we must remain careful: this file does **not** contain:

```text
p-value
adjusted p/q-value
formal log2FC
```

So I would **not call this a formal DE table**.

I would call it:

> **niche expression signature / descriptive effect-size table**

and store the actual quantity exactly as named:

```text
niche_2_minus_niche_1_mean_log_normalized_expression
```

rather than relabeling it `log2FC`.

---

# 2. This means the old pseudobulk file changes role

Previously we had:

```text
spatial_niche_pseudobulk_CPTT.txt
```

Now I would treat the two differently:

### Pseudobulk CPTT matrix

Useful as:

```text
absolute/descriptive expression reference
broad expression context
all available populations
```

### New pooled niche-signature file

Much better for:

```text
Niche1 vs Niche2 effect
percentage expressing
cell counts
direction
gene-program construction
TF expression support
target-gene expression support
```

So for our **four focal niche-defined cell types**, the new TSV becomes our primary expression-signature input.

We do **not** throw away the CPTT matrix; it becomes supporting data.

---

# 3. One thing is still missing if Shunya has it

The file is almost exactly what we asked for, except for statistical significance.

So the only remaining question for Shunya is:

> Does a donor/sample-aware Niche2-vs-Niche1 DE result exist with p-values/FDR?

I emphasize **donor/sample-aware** because the new file contains cell counts such as:

```text
AT1 Control:
Niche1 = 6,591 cells
Niche2 = 143 cells

AT1 IPF:
Niche1 = 6,903 cells
Niche2 = 789 cells
```

and especially tiny groups such as:

```text
Activated Fibrotic FB Control:
Niche1 = 41 cells
Niche2 = 11 cells
```

If somebody simply treats thousands of cells as independent replicates, the p-values could be misleading because the biological replication should ordinarily be donors/samples rather than individual cells.

So:

> **Do not block the project waiting for p/q values.**

But if a properly calculated DE table already exists, we should ingest it.

---

# 4. `Neighbour_celltypes.zip` is VERY important

This file provides something we previously only had conceptually:

> **the actual neighborhood composition defining Niche 1 versus Niche 2.**

There are four real data files:

```text
AT1_knn_25_res0.08_neighbor_mean_counts_by_niche.tsv

Alveolar_Macrophages_knn_25_res0.08_neighbor_mean_counts_by_niche.tsv

Activated_Fibrotic_FBs_knn_25_res0.1_neighbor_mean_counts_by_niche.tsv

KRT5neg_KRT17pos_knn_25_res0.15_neighbor_mean_counts_by_niche.tsv
```

Each contains:

```text
Niche 1
Niche 2
```

and mean counts for ~46–47 neighboring cell types.

Even better, I checked the rows:

> **Every row sums to exactly 25 neighbors.**

So these are clearly the mean compositions of a **k = 25 neighborhood**.

That means we now have actual data for the node we had previously designed:

```text
NeighborhoodProfile
```

---

# 5. This closes the beginning of the KG

Previously our KG began approximately here:

```text
CellType
   ↓
SpatialNicheState
   ↓
GeneProgram
```

But we lacked the quantitative information explaining:

> Why is this actually Niche1 or Niche2?

Now we have it.

The graph can become:

```text
CellType
   │
   └──HAS_NICHE_STATE──▶ SpatialNicheState
                              │
                              ├──DEFINED_BY──▶ NeighborhoodProfile
                              │
                              ├──HAS_PROGRAM──▶ GeneProgram
                              │
                              └──HAS_REGULATORY_PROGRAM──▶ ...
```

And:

```text
NeighborhoodProfile
      │
      ├──HAS_NEIGHBOR {mean_count, proportion}──▶ AT2
      ├──HAS_NEIGHBOR {mean_count, proportion}──▶ Capillary
      ├──HAS_NEIGHBOR {mean_count, proportion}──▶ Basal
      ├──HAS_NEIGHBOR {mean_count, proportion}──▶ RASC
      └──...
```

Because `k=25`, we can calculate:

```text
proportion = mean_neighbor_count / 25
```

without ambiguity.

---

# 6. AT1 is especially clean

The AT1 neighborhood file strongly matches the biological story we have been discussing.

### AT1 Niche 1

The largest mean neighbor counts include:

```text
Capillary              5.13
AT2                    3.44
Alveolar fibroblasts   3.11
Interstitial macroph.  1.93
SMCs/pericytes         1.34
AT1                    1.27
```

### AT1 Niche 2

Largest components include:

```text
RASC                   3.05
Alveolar fibroblasts   2.27
Basal                  2.24
AT2                    1.88
Interstitial macroph.  1.51
Transitional AT2       1.48
Multiciliated          1.48
Capillary              1.40
```

And looking directly at **Niche2 − Niche1**, the strongest Niche2-associated neighbors include approximately:

```text
RASC             +3.01 neighbors
Basal            +2.20
Multiciliated    +1.46
Transitional AT2 +1.08
Secretory        +0.69
```

while Niche1 has much more:

```text
Capillary       +3.73 relative to Niche2
AT2             +1.57
Alveolar FB     +0.84
```

That is almost exactly the conceptual picture we have been using:

```text
AT1 Niche1
≈ alveolar / vascular environment

AT1 Niche2
≈ airway / remodeling-associated environment
```

Now that description is backed by an actual quantitative file rather than just prose.

---

# 7. The same pattern exists across the other cell types

For example, the **alveolar macrophage** profiles show Niche2 enrichment in:

```text
Multiciliated       +2.40
RASC                +1.62
Basal               +1.56
SPP1+ macrophages   +1.20
Secretory           +0.64
Goblet              +0.60
```

whereas Niche1 has more:

```text
Alveolar macrophages
Capillary
Alveolar fibroblasts
AT2
```

The KRT5−/KRT17+ profile similarly has strong Niche2 increases in:

```text
Basal
RASC
Multiciliated
```

while Niche1 has more:

```text
KRT5−/KRT17+ cells
activated fibrotic fibroblasts
alveolar fibroblasts
alveolar macrophages
AT2
capillary
```

And activated fibrotic fibroblast Niche2 is likewise enriched for:

```text
Basal
Multiciliated
RASC
Goblet
Secretory
```

So there is a coherent neighborhood axis across several focal cell types.

That is scientifically interesting.

---

# 8. One thing NOT to assume about the neighbor files

I do **not** see Control/IPF columns in these four files.

They are simply:

```text
niche_1
niche_2
```

Therefore I would **not attach `condition=IPF` or `condition=Control` to the NeighborhoodProfile** unless Shunya confirms how these were generated.

They may represent the pooled spatial niche definition across conditions.

That would actually make sense conceptually:

```text
Spatial neighborhood definition
       ↓
same niche labels
       ↓
evaluate expression separately in Control and IPF
```

But we should preserve exactly what the file says and not invent the condition.

---

# 9. We can now improve the schema slightly

Earlier I had considered `NeighborhoodProfile` optional.

It is **no longer optional** because Shunya has given us clean quantitative source data for it.

The project layer should now be:

```text
CellType
   │
   └──HAS_NICHE_STATE──▶ SpatialNicheState
                              │
                              ├──DEFINED_BY──▶ NeighborhoodProfile
                              │
                              └──HAS_PROGRAM──▶ GeneProgram
```

with:

```text
NeighborhoodProfile:
    focal_cell_type
    niche
    k = 25
    clustering_resolution
    dataset/run
```

and for AT1:

```text
k = 25
resolution = 0.08
```

For the others:

```text
Alveolar Macrophage    resolution = 0.08
Activated Fibrotic FB  resolution = 0.10
KRT5neg/KRT17pos       resolution = 0.15
```

These parameters should be provenance, not biological properties.

---

# 10. Our project-data inputs are now quite strong

We now have four major project-derived evidence sources:

```text
1. Neighborhood composition
   ↓
   What defines Niche1 vs Niche2?

2. Niche expression signatures
   ↓
   What genes differ descriptively between those populations?

3. Pseudobulk expression
   ↓
   What is expressed across broader Yale populations?

4. ChromLinker TF→gene scores
   ↓
   What regulatory connections are inferred in multiome?
```

Then literature becomes:

```text
5. External experimental evidence
   ↓
   Which inferred TF→gene mechanisms have prior support?
```

That gives us a very coherent architecture:

```text
NEIGHBORHOOD
      ↓
SpatialNicheState
      ↓
EXPRESSION SIGNATURE
      ↓
GeneProgram
      ↓
CHROMLINKER
      ↓
TF → target candidates
      ↓
LITERATURE EVIDENCE
      ↓
TF NOMINATION
```

---

# 11. What I would build NOW from these files

We no longer need to wait for anything to start the core project-data layer.

I would generate four normalized tables:

```text
neighborhood_profiles.parquet

niche_expression_signatures.parquet

chromlinker_observations.parquet

expression_observations.parquet
```

### `neighborhood_profiles.parquet`

```text
focal_cell_type
niche
neighbor_cell_type
mean_neighbor_count
neighbor_fraction
k
resolution
source_file
```

### `niche_expression_signatures.parquet`

Use the new file essentially as-is, normalized:

```text
dataset
cell_type
condition
comparison
gene

mean_expr_niche1
mean_expr_niche2
effect_niche2_minus_niche1

pct_expr_niche1
pct_expr_niche2

n_cells_niche1
n_cells_niche2
```

Then derive:

```text
direction =
    NICHE2_HIGHER
    NICHE1_HIGHER
    EQUAL
```

but retain the continuous effect.

---

# 12. What I would NOT derive yet

Do not manufacture:

```text
p_value
q_value
significant = true/false
formal log2FC
```

from this file.

Also don't invent an arbitrary threshold such as:

```text
abs(effect) > 0.25 = DE
```

for the scientific KG.

For exploratory ranking we may use continuous effect magnitude, but call it exactly what it is.

---

# 13. This also improves TF nomination

Previously TF nomination contained:

```text
ChromLinker
TF expression
gene-program overlap
literature
context
```

Now it can additionally include:

```text
niche_environment_context
```

Not as a TF score, but as the **biological explanation of the state being regulated**.

For ETV1 in IPF AT1, for example, we can eventually show something like:

```text
ETV1
│
├── nominated for:
│      IPF AT1 Niche2
│
├── Niche2 environment:
│      RASC ↑
│      Basal ↑
│      Multiciliated ↑
│      Transitional AT2 ↑
│
├── ETV1 expression:
│      descriptively higher in Niche2
│
├── ChromLinker:
│      stronger Niche2-associated target connectivity
│
├── target program:
│      ...
│
└── literature:
       binding / perturbation / lung context / etc.
```

That is a substantially richer scientific explanation than:

> ETV1 score = X.

---

# 14. One short question for Shunya eventually

I would ask only this now:

Thanks, these are very helpful. I can use the pooled niche expression-signature table and the neighbor-composition files directly.

One quick clarification: do you also have the donor/sample-aware differential-expression output for Niche 2 vs Niche 1 with p-value/FDR, or is this pooled expression-signature table the intended final comparison output?

Also, are the neighbor-composition profiles pooled across Control and IPF? I just want to preserve the niche-definition metadata correctly.

Those are the only two things I would clarify.

**We absolutely do not need to wait for the answer to begin implementation.**

The project now has enough primary project data to build the complete **Neighborhood → Niche → Expression → ChromLinker** half of the KG, while the literature pipeline builds the **TF → Target → Evidence** half in parallel.


Yes, but **shorten it to two very specific clarifications**.

What he just told you completely answers the `k=25` / interpretation question: each value is the **mean number of the 25 nearest neighboring cells belonging to each neighbor cell type**, averaged across focal cells assigned to Niche 1 or Niche 2. So we do **not** need to ask him anything about how those neighborhood tables should be interpreted.

What is still genuinely unclear:

1. Whether those neighborhood profiles were calculated **pooling Control + IPF together**, or separately and then combined.
2. Whether a **donor/sample-aware statistical DE table with p/FDR** exists, or whether the pooled expression-signature TSV is intentionally the final expression comparison.

I would send only this:

Thanks, that makes sense. Just two quick clarifications for the metadata:

1. Were the Niche 1/Niche 2 neighbor-composition profiles calculated pooling Control and IPF cells together?

2. For the Yale pooled niche expression-signature file, is there also a donor/sample-aware Niche 2 vs Niche 1 DE output with p-value/FDR, or is this descriptive pooled expression-signature table the intended final comparison output?

That's it. **Don't ask him for anything else right now.**

And neither answer blocks us: we can already start building the neighborhood, expression, ChromLinker, and literature/KG layers.


Perfect — that resolves the two remaining ambiguities, and it actually makes the project design cleaner.

The key consequence is that **Niche 1 / Niche 2 are condition-independent spatial states by construction**. Control and IPF were pooled when the neighborhood clusters were defined, and condition was only examined afterward. That is scientifically useful because the niche identity is not being created by disease status itself.

So the project should now be represented as:

```text
FOCAL CELL TYPE
      ↓
kNN neighborhood composition
(k = 25)
      ↓
joint clustering across Control + IPF
      ↓
SpatialNicheState
   Niche 1 / Niche 2
      ↓
condition-specific downstream analyses
      ├── Control expression
      ├── IPF expression
      ├── Control ChromLinker
      └── IPF ChromLinker
```

That means our `SpatialNicheState` should **not** carry `condition=Control` or `condition=IPF`.

Instead:

```text
SpatialNicheState
-----------------
cell_type: AT1
niche: 1
definition_scope: condition_pooled
conditions_used_for_definition:
  - Control
  - IPF
k_neighbors: 25
clustering_resolution: 0.08
```

Then condition belongs on the downstream observations:

```text
ExpressionSignatureObservation
    condition = Control / IPF

ChromLinkerObservation
    condition = Control / IPF
```

This is a very important distinction.

It also strengthens the methodological story:

> **The neighborhood state is defined independently of disease condition, and Control/IPF differences are evaluated after that state has been established.**

That is analogous to the other important independence in Spatial NicheLinker: neighborhood composition defines the population first; expression/regulation is examined afterward.

For the Yale expression file, we should now freeze the terminology too. It is **not a formal DE analysis** and should never be represented as one.

Use something like:

```text
NicheExpressionSignature
```

or:

```text
ExpressionContrastObservation
```

with:

```text
cell_type
condition
comparison = Niche2_vs_Niche1

mean_log_expr_niche1
mean_log_expr_niche2

mean_log_expr_difference
= Niche2 - Niche1

pct_expressing_niche1
pct_expressing_niche2

n_cells_niche1
n_cells_niche2
```

Do **not** create:

```text
p_value
q_value
significant
DEG
formal_log2FC
```

because those are unsupported.

I would also change our earlier `GeneProgram` language slightly. Instead of defining the Yale programs as statistically significant DE gene sets, call them something like:

```text
AT1_IPF_Niche2_Higher_Expression_Program

AT1_IPF_Niche1_Higher_Expression_Program
```

derived from the **continuous descriptive expression contrast**.

We can use the effect values for ranking and enrichment, but the manuscript/interface should say:

> “genes with higher pooled mean log-normalized expression in Niche 2”

rather than:

> “significantly upregulated genes in Niche 2.”

That distinction will keep the KG scientifically honest.

### The project-data hierarchy is now fully clear

```text
1. NeighborhoodDefinition
   condition-pooled Control + IPF
   kNN = 25
        ↓
2. SpatialNicheState
   Niche 1 / Niche 2
        ↓
3. Condition-specific expression signature
   Control N1 vs N2
   IPF N1 vs N2
        ↓
4. Condition-specific ChromLinker network
   Control N1 vs N2
   IPF N1 vs N2
        ↓
5. External literature evidence
        ↓
6. TF nomination
```

And for AT1, for example:

```text
AT1 cells
   ↓
condition-pooled neighborhood clustering
   ↓
┌─────────────────────┬─────────────────────┐
│                     │
AT1 Niche 1           AT1 Niche 2
│                     │
alveolar/vascular     airway/remodeling-like
neighborhood          neighborhood
│                     │
├─ Control RNA        ├─ Control RNA
├─ IPF RNA            ├─ IPF RNA
├─ Control GRN        ├─ Control GRN
└─ IPF GRN            └─ IPF GRN
                         ↓
                 candidate TFs/targets
                         ↓
                  literature evidence
                         ↓
                    TF nomination
```

So **no, I would not send Shunya any more questions right now**. We have enough metadata to interpret these files correctly and begin implementation.

The only thing I would do is record his two answers verbatim in a small `dataset_metadata.yaml`/README so we never accidentally forget later that:

- the niche definition is **condition-pooled**;
- the Yale signature table is **descriptive, not sample-aware inferential DE**.

Those two facts should become hard constraints in the code and manuscript terminology.