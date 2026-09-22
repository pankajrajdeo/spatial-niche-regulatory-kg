"""Cell Ontology, UBERON, and MONDO snapshots and the term lists derived from them.

Exact pinned releases come from the OBO Foundry release PURLs; their SHA-256s are pinned in
configs/ontology_scope.yaml (the PURLs publish no checksum). Only labels and EXACT synonyms of reviewed seed terms and
their is_a/part_of descendants become matching phrases; RELATED/BROAD/NARROW synonyms are recorded
but never used for matching, because they widen a term beyond the class it names.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

from pydantic import BaseModel, ConfigDict

from regkg.provenance import write_json
from regkg.resources import Fetcher, cached_snapshot, selected_headers, store_snapshot

ONTOLOGIES = {
    "cl": ("Cell Ontology", "http://purl.obolibrary.org/obo/cl/cl-basic.obo", "cl-basic.obo"),
    "uberon": ("UBERON", "http://purl.obolibrary.org/obo/uberon/uberon-basic.obo", "uberon-basic.obo"),
    "mondo": ("MONDO", "http://purl.obolibrary.org/obo/mondo.obo", "mondo.obo"),
}
SYNONYM = re.compile(r'^synonym: "((?:[^"\\]|\\.)*)" (EXACT|RELATED|BROAD|NARROW)')


@dataclass
class Term:
    id: str
    name: str = ""
    synonyms: list[tuple[str, str]] = field(default_factory=list)  # (text, scope)
    is_a: list[str] = field(default_factory=list)
    part_of: list[str] = field(default_factory=list)
    obsolete: bool = False


def parse_obo(path: Path) -> dict[str, Term]:
    terms: dict[str, Term] = {}
    current: Term | None = None
    in_term = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("["):
            in_term = line == "[Term]"
            current = None
            continue
        if not in_term or not line:
            continue
        key, _, value = line.partition(": ")
        if key == "id":
            current = terms.setdefault(value, Term(value))
        elif current is None:
            continue
        elif key == "name":
            current.name = value
        elif key == "synonym":
            m = SYNONYM.match(line)
            if m:
                current.synonyms.append((m.group(1).replace('\\"', '"'), m.group(2)))
        elif key == "is_a":
            current.is_a.append(value.split(" ")[0])
        elif key == "relationship" and value.startswith("part_of "):
            current.part_of.append(value.split(" ")[1])
        elif key == "is_obsolete" and value == "true":
            current.obsolete = True
    return terms


def descendants(terms: dict[str, Term], root: str, relations=("is_a", "part_of"), limit: int = 5000) -> set[str]:
    children: dict[str, set[str]] = {}
    for term in terms.values():
        for relation in relations:
            for parent in getattr(term, relation):
                children.setdefault(parent, set()).add(term.id)
    found, stack = {root}, [root]
    while stack and len(found) < limit:
        for child in children.get(stack.pop(), ()):
            if child not in found and not terms.get(child, Term(child)).obsolete:
                found.add(child)
                stack.append(child)
    return found


# ---------------------------------------------------------------------------
# Reviewed mapping (configs/ontology_scope.yaml) -> matching phrase sets

RELEASE_URL = {
    "cl": "http://purl.obolibrary.org/obo/cl/releases/{release}/{file}",
    "uberon": "http://purl.obolibrary.org/obo/uberon/releases/{release}/{file}",
    "mondo": "http://purl.obolibrary.org/obo/mondo/releases/{release}/{file}",
}


class Release(BaseModel):
    model_config = ConfigDict(extra="forbid")
    version: str  # the file's data-version date (cache directory)
    release: str  # OBO PURL release directory
    file: str
    sha256: str


class LineageOntology(BaseModel):
    model_config = ConfigDict(extra="forbid")
    exact_cl: list[str]
    grouping_parents: list[str]
    manuscript_label_phrases: list[str] = []
    grouping_phrases: list[str] = []


class OntologyScope(BaseModel):
    model_config = ConfigDict(extra="forbid")
    schema_version: int
    mapping_version: str
    status: str
    releases: dict[str, Release]
    cell_types: dict[str, LineageOntology]
    anatomy: dict[str, list[str]]
    diseases: dict[str, list[str]]


def load_scope(scope_path: Path) -> OntologyScope:
    import yaml

    return OntologyScope.model_validate(yaml.safe_load(scope_path.read_text()))


def setup_pinned(scope_path: Path, external_root: Path, fetcher: Fetcher) -> dict:
    """Reproducible acquisition of exactly the pinned releases (`regkg literature ontology-setup`).

    A cached copy is reused only if its bytes match the pinned SHA-256; otherwise the exact release URL
    is fetched and must match. No newer or "latest" release is ever substituted.
    """
    import hashlib

    scope, result = load_scope(scope_path), {}
    for name, pin in scope.releases.items():
        directory = external_root / "ontologies" / name / pin.version
        cached = cached_snapshot(directory, pin.file)  # raises if the cached bytes changed
        if cached is not None and cached.provenance["sha256"] == pin.sha256:
            result[name] = {"status": "cached", "sha256": pin.sha256}
            continue
        url = RELEASE_URL[name].format(release=pin.release, file=pin.file)
        response = fetcher.get(url)
        digest = hashlib.sha256(response.content).hexdigest()
        if digest != pin.sha256:
            raise ValueError(
                f"{name} release {pin.release}: SHA-256 {digest[:12]} differs from the pinned {pin.sha256[:12]}"
            )
        store_snapshot(
            directory,
            pin.file,
            response.content,
            url,
            fetcher,
            expected_md5_hex=None,
            metadata={
                "resource": ONTOLOGIES[name][0],
                "version": pin.version,
                "release": pin.release,
                "license": "CC BY 4.0",
                "doi": None,
            },
            response_headers=selected_headers(response),
        )
        write_json(external_root / "ontologies" / name / "current.json", {"version": pin.version})
        result[name] = {"status": "fetched", "sha256": digest, "url": url}
    return result


@dataclass
class OntologyContext:
    record: dict  # mapping/phrase-table hashes, release pins, problems, counts
    strict: dict[str, dict[str, list[str]]]  # cell type -> phrase -> IDs (manuscript cell-type evidence)
    broad: dict[str, dict[str, list[str]]]  # cell type -> phrase -> grouping IDs (never direct evidence)
    lung: dict[str, list[str]]
    diseases: dict[str, dict[str, list[str]]]
    cl_all: dict[str, list[str]] = field(default_factory=dict)  # every CL label/EXACT synonym -> IDs


def phrase_ids(terms: dict[str, Term], ids: set[str], min_length: int = 4) -> dict[str, list[str]]:
    """Lower-cased label and EXACT synonym -> every term ID carrying it (ambiguity is kept, not resolved)."""
    table: dict[str, set[str]] = {}
    for term_id in ids:
        term = terms.get(term_id)
        if term is None or term.obsolete:
            continue
        for text in [term.name] + [s for s, scope in term.synonyms if scope == "EXACT"]:
            text = " ".join(text.split()).lower()
            if len(text) >= min_length:
                table.setdefault(text, set()).add(term_id)
    return {k: sorted(v) for k, v in sorted(table.items())}


def build_context(scope_path: Path, external_root: Path) -> OntologyContext:
    """Phrase sets from the pinned releases; unpinned or changed bytes are refused."""
    import hashlib

    from regkg.provenance import canonical_json

    scope = load_scope(scope_path)
    loaded, provenance = {}, {}
    for name in ("cl", "uberon", "mondo"):
        pin = scope.releases[name]
        directory = external_root / "ontologies" / name / pin.version
        snapshot = cached_snapshot(directory, pin.file)
        if snapshot is None:
            raise FileNotFoundError(
                f"{name} release {pin.version} is not cached under {directory}; run `regkg literature ontology-setup`"
            )
        if snapshot.provenance["sha256"] != pin.sha256:
            raise ValueError(f"{name} cached SHA-256 differs from the pinned release")
        loaded[name] = parse_obo(snapshot.path)
        provenance[name] = {"version": pin.version, "release": pin.release, "sha256": pin.sha256}
    cl, uberon, mondo = loaded["cl"], loaded["uberon"], loaded["mondo"]
    problems = []
    for source, ids in (
        ("cl", [t for c in scope.cell_types.values() for t in c.exact_cl + c.grouping_parents]),
        ("uberon", [t for v in scope.anatomy.values() for t in v]),
        ("mondo", [t for v in scope.diseases.values() for t in v]),
    ):
        for term_id in ids:
            term = loaded[source].get(term_id)
            if term is None or term.obsolete:
                problems.append(
                    {"ontology": source, "id": term_id, "problem": "missing" if term is None else "obsolete"}
                )
    cl_all = phrase_ids(cl, set(cl))
    strict, broad, ambiguous = {}, {}, []
    for cell_type, mapping in scope.cell_types.items():
        exact = (
            set().union(*[descendants(cl, t, ("is_a",)) for t in mapping.exact_cl if t in cl])
            if mapping.exact_cl
            else set()
        )
        table = phrase_ids(cl, exact)
        for phrase, ids in list(table.items()):
            owners = set(cl_all.get(phrase, ids))
            if owners - exact:  # the phrase also names a CL class outside this lineage's mapping
                ambiguous.append({"cell_type": cell_type, "phrase": phrase, "ids": sorted(owners)})
                del table[phrase]
        strict[cell_type] = {**table, **{p.lower(): ["manuscript_label"] for p in mapping.manuscript_label_phrases}}
        broad[cell_type] = {
            **phrase_ids(cl, set(mapping.grouping_parents)),
            **{p.lower(): ["grouping_phrase"] for p in mapping.grouping_phrases},
            **{a["phrase"]: a["ids"] for a in ambiguous if a["cell_type"] == cell_type},
        }
    lung_ids = set().union(*[descendants(uberon, t) for t in scope.anatomy["lung"] if t in uberon])
    lung = phrase_ids(uberon, lung_ids)
    diseases = {
        group: phrase_ids(mondo, set().union(*[descendants(mondo, t, ("is_a",)) for t in ids if t in mondo]))
        for group, ids in scope.diseases.items()
    }
    tables = {"strict": strict, "broad": broad, "lung": lung, "diseases": diseases}
    record = {
        "mapping_version": scope.mapping_version,
        "status": scope.status,
        "releases": provenance,
        "mapping_sha256": hashlib.sha256(canonical_json(scope.model_dump()).encode()).hexdigest(),
        "phrase_tables_sha256": hashlib.sha256(canonical_json(tables).encode()).hexdigest(),
        "mapping_problems": problems,
        "ambiguous_phrases_demoted_to_broad": ambiguous,
        "phrases": {
            "strict": {c: len(v) for c, v in strict.items()},
            "broad": {c: len(v) for c, v in broad.items()},
            "lung": len(lung),
            "diseases": {g: len(v) for g, v in diseases.items()},
        },
        "matching": "labels and EXACT synonyms only; ambiguous phrases are grouping-level; longest CL mention wins",
    }
    return OntologyContext(record, strict, broad, lung, diseases, cl_all)


def phrase_pattern(table: dict) -> re.Pattern | None:
    if not table:
        return None
    body = "|".join(re.escape(p) for p in sorted(table, key=len, reverse=True))
    # Plural forms ("alveolar macrophages") match their singular label; the match maps back to it.
    return re.compile(rf"(?<![A-Za-z0-9])(?:{body})(?:e?s)?(?![A-Za-z0-9])", re.IGNORECASE)


def lookup(table: dict, matched: str):
    key = matched.lower()
    for candidate in (key, key[:-1] if key.endswith("s") else None, key[:-2] if key.endswith("es") else None):
        if candidate and candidate in table:
            return candidate, table[candidate]
    return None


def _word_form(phrase: str) -> str:
    # PubMed and Europe PMC reduce punctuation to word tokens (P3 punctuation probe), so
    # "KRT5−/KRT17+" and "KRT5-/KRT17+" are one search phrase.
    return " ".join(re.sub(r"[^\w]+", " ", phrase.lower()).split())


def query_synonym_gaps(ontology: OntologyContext, lineages: list[dict], names: dict[str, list[str]]) -> dict:
    """Strict ontology phrases no accepted-queue context term covers lexically, and one query per
    lineage and named regulator: (TF names) AND (uncovered phrases).

    Lexical non-coverage is not a retrieval gap: broader queue queries may already find the same
    papers. Only executed supplemental searches and their overlap with P2 discovery measure yield.
    """
    report = {"rule": "p3-ontology-query-gaps-2", "status": "proposed_not_searched", "lineages": {}, "queries": []}
    for lineage in lineages:
        covered = {_word_form(t) for t in lineage["context_terms"]}
        strict = ontology.strict.get(lineage["cell_type"], {})
        missing, forms = [], set()
        for phrase in sorted(strict):
            form = _word_form(phrase)
            if form in covered or form in forms or any(c in form or form in c for c in covered if len(c) > 5):
                continue
            forms.add(form)
            missing.append(phrase)
        report["lineages"][lineage["cell_type"]] = {
            "existing_context_terms": sorted(lineage["context_terms"]),
            "ontology_strict_phrases": sorted(strict),
            "lexically_uncovered_phrases": missing,
        }
        if not missing:
            continue
        for hgnc in sorted(lineage["named_tfs"]):
            report["queries"].append(
                {
                    "cell_type": lineage["cell_type"],
                    "tf_hgnc_id": hgnc,
                    "tf_terms": list(names[hgnc]),
                    "context_phrases": missing,
                    "phrase_ontology_ids": {p: strict[p] for p in missing},
                    "query_text": "("
                    + " OR ".join(f'"{n}"' for n in names[hgnc])
                    + ") AND ("
                    + " OR ".join(f'"{p}"' for p in missing)
                    + ")",
                    "search_status": "NOT_SEARCHED",
                }
            )
    return report
