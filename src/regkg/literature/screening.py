"""Provisional, rule-based paper roles and per-lineage screening signals (no model calls).

Roles prioritise work; they do not decide evidence eligibility, which belongs to individual
findings. Each role records the rule, the matched phrases, and the text it was read from, and
stays pending lead review. Advisor tiers and annotations are kept as annotations, never as roles.
Several roles may apply to one paper; a paper with no confident signal is UNCERTAIN.
"""

from __future__ import annotations

import re

from regkg.literature.publications import term_pattern

PRIMARY = "PRIMARY_REGULATORY_EVIDENCE"
CONTEXT = "BIOLOGICAL_CONTEXT"
RESOURCE = "RESOURCE_OR_METHOD"
OTHER = "OTHER_CONTEXT"
UNCERTAIN = "UNCERTAIN"
ROLE_RULE = "p3-roles-1"
REVIEW_STATUS = "provisional_rule_based_pending_lead_review"

ASSAY = re.compile(
    r"\b(ChIP(?:-seq|-exo|-qPCR)?|chromatin immunoprecipitation|CUT&RUN|CUT&Tag|EMSA|electrophoretic mobility|"
    r"luciferase|reporter assays?|knock-?down|knock-?out|siRNA|shRNA|CRISPR(?:i|a)?|over-?expression|"
    r"conditional (?:deletion|knockout|inactivation)|loss-of-function|gain-of-function|DamID|Perturb-seq)\b",
    re.IGNORECASE,
)
REGULATION = re.compile(
    r"\b(transcription factors?|transcriptional(?:ly)?|regulat\w*|target genes?|promoters?|enhancers?|"
    r"binds?|binding|occupancy|represses?|activates?|cis-regulatory)\b",
    re.IGNORECASE,
)
RESOURCE_TITLE = re.compile(
    r"\b(database|portal|atlas|resource|catalog(?:ue)?|compendium|knowledgebase|web ?server|browser|toolkit|"
    r"software|pipeline|benchmark\w*|reference (?:human )?epigenomes?|encyclopedia|collection|repository)\b",
    re.IGNORECASE,
)
LUNG = re.compile(r"\b(lungs?|pulmonary|alveol\w*|airways?|bronch\w*|pneumocytes?|IPF)\b", re.IGNORECASE)
CONTEXT_TOPIC = re.compile(
    r"\b(single[- ]cell|transcriptom\w*|expression|cell types?|cell states?|lineages?|niches?|fibros\w*|atlas|"
    r"development\w*|injury|regenerat\w*|differentiation|heterogeneity|spatial)\b",
    re.IGNORECASE,
)
PPI = re.compile(
    r"\b(protein[- ]protein interactions?|interactome|two-hybrid|affinity purification|BioID|"
    r"co-?immunoprecipitation)\b",
    re.IGNORECASE,
)
REVIEW_TYPES = {"review", "systematic review", "meta-analysis"}
RESOURCE_TYPES = {"dataset", "software"}


def _hits(pattern: re.Pattern, text: str, limit: int = 5) -> list[str]:
    return sorted({m.group(0).lower() for m in pattern.finditer(text)})[:limit]


def provisional_roles(
    title: str | None, abstract: str | None, publication_types: list[str], full_text: str | None = None
) -> list[dict]:
    """Rule-based roles from the paper's own text; the most specific text available is used."""
    basis = "full_text" if full_text else "title_abstract" if (abstract or title) else "none"
    head = f"{title or ''} {abstract or ''}"
    types = {t.lower() for t in publication_types}
    review = bool(types & REVIEW_TYPES)
    roles: list[dict] = []

    def add(role: str, rule: str, evidence: list[str]) -> None:
        roles.append(
            {
                "role": role,
                "rule": f"{ROLE_RULE}:{rule}",
                "evidence": evidence,
                "text_basis": basis,
                "review_status": REVIEW_STATUS,
            }
        )

    if basis == "none":
        add(UNCERTAIN, "no_text", [])
        return roles
    assays, regulation = _hits(ASSAY, head), _hits(REGULATION, head)
    if assays and regulation and not review:
        add(PRIMARY, "assay_and_regulation_terms_in_title_abstract", assays + regulation)
    elif full_text and _hits(ASSAY, full_text) and _hits(REGULATION, full_text) and not review:
        add(PRIMARY, "assay_and_regulation_terms_in_full_text", _hits(ASSAY, full_text) + _hits(REGULATION, full_text))
    resource = _hits(RESOURCE_TITLE, title or "")
    if resource or types & RESOURCE_TYPES:
        add(RESOURCE, "resource_or_method_title_or_type", resource + sorted(types & RESOURCE_TYPES))
    # Strict lung anatomy: "alveolar bone" is not lung (shared with the context rule below).
    lung, topics = _found(LUNG_TISSUE, head), _hits(CONTEXT_TOPIC, head)
    if lung and (topics or review):
        add(CONTEXT, "lung_biology_context" + ("_review" if review else ""), lung + topics)
    ppi = _hits(PPI, head)
    if not lung:
        add(OTHER, "no_lung_terms_in_title_abstract", [])
    elif ppi and not assays:
        add(OTHER, "protein_interaction_focus", ppi)
    if not roles or (all(r["role"] == OTHER for r in roles) and not (assays or resource or topics)):
        add(UNCERTAIN, "no_confident_role_signal", [])
    return roles


def lineage_signals(text: str, lineages: list[dict]) -> dict[str, dict]:
    """Per manuscript lineage: exact named-regulator and candidate-TF mentions, and context phrases.

    Mentions are retrieval signals; they do not establish that the paper studies that lineage.
    `lineages` items carry cell_type, named_tfs {hgnc: names}, candidate_tfs {hgnc: names}, context_terms.
    """
    lowered = text.lower()
    signals = {}
    for lineage in lineages:
        named = sorted(
            h for h, names in lineage["named_tfs"].items() if any(term_pattern(n).search(text) for n in names)
        )
        candidates = sorted(
            h for h, names in lineage["candidate_tfs"].items() if any(term_pattern(n).search(text) for n in names)
        )
        context = sorted({t for t in lineage["context_terms"] if term_pattern(t.lower()).search(lowered)})
        signals[lineage["cell_type"]] = {"named_tfs": named, "candidate_tfs": candidates, "context_terms": context}
    return signals


# ---------------------------------------------------------------------------
# Source-reported biological context versus manuscript association (rule p3-context-1)
#
# A manuscript query association says which lineage's search found a passage. The source context
# says what the paper reports (species, tissue, cell type, disease). Broad words such as "alveolar",
# "lung", or "fibroblast" do not establish a manuscript cell type: "alveolar bone" is not lung and
# ligament fibroblasts are not activated fibrotic lung fibroblasts. Unknown context stays unknown.

CONTEXT_RULE = "p3-context-4"  # 4: longest CL mention wins; direct needs a same-sentence lung statement
DIRECT = "direct_context_candidate"
TRANSFERABLE = "potentially_transferable_mechanism"
BACKGROUND = "biological_background_resource"
IRRELEVANT = "irrelevant_to_assigned_question"
UNRESOLVED = "unresolved"

SPECIES = {
    "human": r"\b(humans?|patients?|Homo sapiens|donors?)\b",
    "mouse": r"\b(mouse|mice|murine|Mus musculus)\b",
    "rat": r"\b(rats?|Rattus)\b",
    "rabbit": r"\b(rabbits?|lapine)\b",
    "other_animal": (
        r"\b(zebrafish|porcine|pigs?|bovine|canine|dogs?|macaques?|chickens?|Drosophila|Xenopus|ovine|sheep)\b"
    ),
}
# Lung only when "alveolar" is qualified by lung anatomy; "alveolar bone" is dental tissue.
LUNG_TISSUE = (
    r"\b(lungs?|pulmonary|airways?|bronch\w*|pleura\w*|pneumocytes?|"
    r"alveol\w* (?:epitheli\w*|type|macrophages?|spaces?|sacs?|ducts?|septa\w*|capillar\w*|regenerat\w*|niches?))\b"
)
OTHER_TISSUE = (
    r"\b(alveolar bone|bones?|osteo\w*|dental|periodont\w*|teeth|tooth|ligaments?|tendons?|cartilage|chondro\w*|"
    r"kidneys?|renal|liver|hepat\w*|heart|cardi\w*|intestin\w*|colon\w*|gastric|breast|mammary|skin|dermal|"
    r"brain|neur\w*|retina\w*|pancrea\w*|prostat\w*|ovar\w*|uter\w*|spleen|skeletal muscle|adipose|thyroid|"
    r"bladder|esophag\w*|oral|calvari\w*)\b"
)
DISEASE = {
    "pulmonary_fibrosis": r"\b(idiopathic pulmonary fibrosis|IPF|pulmonary fibrosis|lung fibrosis)\b",
    "fibrosis_other": r"\bfibros\w*\b",
    "cancer": r"\b(cancers?|carcinomas?|tumou?rs?|adenocarcinomas?|NSCLC|SCLC|leuka?emias?|lymphomas?|melanomas?|"
    r"sarcomas?|gliomas?|metasta\w*|oncogen\w*)\b",
    "infection_or_injury": r"\b(infection|influenza|COVID-19|SARS-CoV-2|pneumonia|bleomycin|injur\w*|sepsis)\b",
}
# Manuscript cell types: strict phrases establish the cell type; broad phrases leave it unresolved.
CELL_TYPES = {
    "AT1": (
        r"\b(alveolar type (?:1|I)|type (?:1|I) alveolar|AT1 cells?|ATI cells?|AEC1s?|type I pneumocytes?|"
        r"alveolar epithelial type (?:1|I)|AT1-like)\b",
        r"\b(alveolar epithel\w*|pneumocytes?|distal lung epithel\w*)\b",
    ),
    "Alveolar_Macrophages": (
        r"\b(alveolar macrophages?|airspace macrophages?|tissue-resident alveolar)\b",
        r"\b(macrophages?|monocyte-derived macrophages?)\b",
    ),
    "KRT5neg_KRT17pos": (
        r"(KRT5[-−]\s*/\s*KRT17\+|KRT17\+\s*/?\s*KRT5[-−]|aberrant basaloid)",
        # "basaloid" alone also names basaloid carcinoma cells: grouping-level only.
        r"\b(basaloid cells?|KRT17|basal cells?|airway epithel\w*|transitional epithel\w*)\b",
    ),
    # "lung fibroblast" is grouping-level: lung context, not the activated fibrotic state.
    "Activated_Fibrotic_FBs": (
        r"\b(fibrotic fibroblasts?|activated (?:lung )?fibroblasts?|CTHRC1\+? fibroblasts?)\b",
        r"\b((?:lung|pulmonary|IPF) (?:myo)?fibroblasts?|(?:myo)?fibroblasts?|mesenchym\w*|stromal cells?)\b",
    ),
}


def _found(pattern: str, text: str) -> list[str]:
    return sorted({m.group(0).lower() for m in re.finditer(pattern, text, re.IGNORECASE)})[:6]


def _ontology_hits(pattern, table: dict[str, str], text: str) -> dict[str, str]:
    from regkg.literature.ontology import lookup

    hits = {}
    for m in pattern.finditer(text) if pattern else ():
        found = lookup(table, m.group(0))
        if found:
            hits[found[0]] = found[1]
    return hits


SENTENCE = re.compile(r"(?<=[.!?;])\s+")


def _spans(pattern, text: str) -> list[tuple[int, int, str]]:
    return [(m.start(), m.end(), m.group(0).lower()) for m in pattern.finditer(text)] if pattern else []


def lookup_ids(table: dict, matched: str) -> list[str] | None:
    from regkg.literature.ontology import lookup

    found = lookup(table, matched)
    return found[1] if found else None


def _strict_mentions(text: str, cell_type: str, ontology, patterns) -> tuple[list[tuple[int, int, str]], list[str]]:
    """Manuscript cell-type mentions, minus those inside a longer CL name of another class."""
    spans = _spans(re.compile(CELL_TYPES[cell_type][0], re.IGNORECASE), text)
    if ontology is not None:
        spans += _spans(patterns["strict"].get(cell_type), text)
    overridden = []
    if ontology is not None and spans:
        own = {i for ids in ontology.strict.get(cell_type, {}).values() for i in ids}
        for start, end, phrase in _spans(patterns["cl_all"], text):
            found = lookup_ids(ontology.cl_all, phrase)
            if not found or set(found) & own:
                continue
            for span in [s for s in spans if s[0] >= start and s[1] <= end and (s[1] - s[0]) < (end - start)]:
                spans.remove(span)
                overridden.append(f"{span[2]} (inside '{phrase}' {found[0]})")
    return spans, overridden


def source_context(text: str, ontology=None) -> dict:
    """What the text itself reports: species, tissue, disease, and manuscript cell-type phrases.

    With `ontology` (literature.ontology.OntologyContext), labels and EXACT synonyms of the mapped CL,
    UBERON, and MONDO terms are matched too and their IDs recorded. A strict cell-type phrase is
    "direct" only when one sentence states it with lung anatomy and without another tissue or cancer.
    """
    patterns = _patterns(ontology) if ontology is not None else None
    profile = {
        "species": {k: _found(p, text) for k, p in SPECIES.items() if _found(p, text)},
        "lung_tissue": _found(LUNG_TISSUE, text),
        "other_tissue": _found(OTHER_TISSUE, text),
        "disease": {k: _found(p, text) for k, p in DISEASE.items() if _found(p, text)},
        "cell_types": {},
        "ontology_ids": {},
        "rule": CONTEXT_RULE,
    }
    ids: dict[str, list[str]] = {}
    if ontology is not None:
        lung = _ontology_hits(patterns["lung"], ontology.lung, text)
        profile["lung_tissue"] = sorted(set(profile["lung_tissue"]) | set(lung))[:8]
        ids.update(lung)
        for group, table in ontology.diseases.items():
            hits = _ontology_hits(patterns["disease"][group], table, text)
            if hits:
                profile["disease"][group] = sorted(set(profile["disease"].get(group, [])) | set(hits))[:8]
                ids.update(hits)

    def lung_in(sentence: str) -> bool:
        if _found(LUNG_TISSUE, sentence):
            return True
        return ontology is not None and bool(_ontology_hits(patterns["lung"], ontology.lung, sentence))

    sentences = SENTENCE.split(text)
    for cell_type, (_, broad_regex) in CELL_TYPES.items():
        spans, overridden = _strict_mentions(text, cell_type, ontology, patterns)
        broad = _found(broad_regex, text)
        if ontology is not None:
            hits = _ontology_hits(patterns["broad"].get(cell_type), ontology.broad.get(cell_type, {}), text)
            broad = sorted(set(broad) | set(hits))[:8]
            ids.update(hits)
            for span in spans:
                found = lookup_ids(ontology.strict.get(cell_type, {}), span[2])
                ids[span[2]] = found or ["regex"]
        phrases_found = {s[2] for s in spans}
        direct_sentence = any(
            any(p in sentence.lower() for p in phrases_found)
            and lung_in(sentence)
            and not _found(OTHER_TISSUE, sentence)
            and not _found(DISEASE["cancer"], sentence)
            for sentence in sentences
        )
        profile["cell_types"][cell_type] = {
            "strict": sorted(phrases_found)[:8],
            "broad": broad,
            "direct_sentence": direct_sentence,
            "overridden_by_longer_cl_name": overridden[:4],
        }
    profile["ontology_ids"] = dict(sorted(ids.items())[:30])
    return profile


_PATTERN_CACHE: dict[int, dict] = {}


def _patterns(ontology) -> dict:
    from regkg.literature.ontology import phrase_pattern

    key = id(ontology)
    if key not in _PATTERN_CACHE:
        _PATTERN_CACHE[key] = {
            "lung": phrase_pattern(ontology.lung),
            "disease": {g: phrase_pattern(t) for g, t in ontology.diseases.items()},
            "strict": {c: phrase_pattern(t) for c, t in ontology.strict.items()},
            "broad": {c: phrase_pattern(t) for c, t in ontology.broad.items()},
            "cl_all": phrase_pattern(ontology.cl_all),
        }
    return _PATTERN_CACHE[key]


def context_relevance(profile: dict, cell_type: str, regulatory: bool, roles: list[str]) -> tuple[str, str]:
    """Provisional relevance of a paper to one manuscript lineage (a screening label, not a finding).

    `regulatory` means a regulatory assay or regulation term in the paper's own title/abstract.
    """
    cells = profile["cell_types"].get(cell_type, {"strict": [], "broad": [], "direct_sentence": False})
    lung, other = bool(profile["lung_tissue"]), bool(profile["other_tissue"])
    if cells["strict"] and cells.get("direct_sentence", lung):
        return DIRECT, f"manuscript cell-type phrase {cells['strict'][:2]} stated with lung anatomy"
    if cells["strict"] and lung:
        return UNRESOLVED, f"cell-type phrase {cells['strict'][:2]} not stated with lung-only, non-cancer context"
    if lung and cells["broad"]:
        return (
            UNRESOLVED,
            f"lung context with broad cell phrase {cells['broad'][:2]}; manuscript cell type not established",
        )
    if other and not lung:
        if regulatory:
            return (
                TRANSFERABLE,
                f"regulation in non-lung context {profile['other_tissue'][:2]}; not manuscript-cell evidence",
            )
        return IRRELEVANT, f"explicit non-lung context {profile['other_tissue'][:2]} without regulatory content"
    if "cancer" in profile["disease"]:
        if regulatory:
            return TRANSFERABLE, f"regulation in cancer context {profile['disease']['cancer'][:2]}; context differs"
        return BACKGROUND, "cancer context without regulatory content"
    if regulatory and lung:
        return UNRESOLVED, "lung regulatory study; manuscript cell type not stated"
    if set(roles) & {RESOURCE, CONTEXT}:
        return BACKGROUND, "background or resource role without regulatory content"
    return UNRESOLVED, "insufficient context to label"


REGULATORY_TERMS = re.compile(
    r"\b(silenc\w*|represses?|repression|activates?|transcriptional(?:ly)? (?:regulat\w*|activat\w*|repress\w*)|"
    r"binds?|binding|occupancy|target genes?|promoter|enhancer)\b",
    re.IGNORECASE,
)


def regulatory_content(text: str) -> bool:
    """A regulatory assay or regulation statement in the text (title/abstract basis for relevance)."""
    return bool(ASSAY.search(text) or REGULATORY_TERMS.search(text))


# Experimental attribution of a passage, from its section and citation markers (rule p3-attribution-1).
ATTRIBUTION_RULE = "p3-attribution-1"
CITATION = re.compile(r"\[\d+(?:[,–-]\s*\d+)*\]|\(\s*[A-Z][A-Za-z-]+ et al\.?,? \d{4}|\bet al\.|\(\d+(?:[,–-]\d+)*\)")


def attribution(kind: str, section_type: str, text: str) -> str:
    """source_result_candidate | abstract_summary | methods_context | attribution_unresolved.

    Results, figure captions, and tables are the paper's own reports unless they cite other work;
    introduction/discussion statements and cited sentences may describe others' experiments, so they
    stay unresolved rather than being attributed to the citing paper.
    """
    cited = bool(CITATION.search(text))
    if kind in {"figure_caption", "table_row", "table_caption", "table_footnote"} and not cited:
        return "source_result_candidate"
    if kind == "abstract":
        return "abstract_summary"
    if section_type == "methods":
        return "methods_context"
    if section_type == "results" and not cited:
        return "source_result_candidate"
    return "attribution_unresolved"
