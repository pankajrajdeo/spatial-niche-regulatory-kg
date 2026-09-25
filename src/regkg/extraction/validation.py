"""Conservative finding disposition, species-aware entity identity and exact source checks."""

import re

from regkg.provenance import canonical_json, stable_id


def species_name(value):
    aliases = {
        "human": "Homo sapiens",
        "humans": "Homo sapiens",
        "homo sapiens": "Homo sapiens",
        "mouse": "Mus musculus",
        "mice": "Mus musculus",
        "murine": "Mus musculus",
        "mus musculus": "Mus musculus",
    }
    return aliases.get((value or "").casefold(), value)


class EntityResolver:
    def __init__(self, mappings, version: str, external_catalog=None):
        self.version = version
        self.external_catalog = external_catalog or {}
        self.index = {}
        for row in mappings:
            for name in {row.get("source_symbol"), row.get("approved_symbol")} - {None, ""}:
                self.index.setdefault(name, []).append(row)

    def resolve(self, entity, identity_hints=None):
        raw = {**entity.model_dump(), "species_reported": entity.species, "species": species_name(entity.species)}
        if entity.kind != "gene":
            return {
                **raw,
                "entity_id": stable_id("entity", raw),
                "mapping_status": "source_named_non_gene",
                "mapping_source": "source text",
                "mapping_version": None,
            }
        rows = [
            r
            for r in self.index.get(entity.name, [])
            if r["species"] == species_name(entity.species)
            and str(r["mapping_status"]).startswith("resolved")
            and r.get("hgnc_id")
        ]
        ids = {r["hgnc_id"] for r in rows}
        if len(ids) != 1:
            external_ids = {
                str(h.get("external_identifier"))
                for h in identity_hints or []
                if str(h.get("external_identifier", "")).isdigit()
            }
            catalog = self.external_catalog.get("response", {}).get("result", {})
            candidates = [
                catalog[i]
                for i in external_ids
                if i in catalog and catalog[i].get("organism", {}).get("scientificname") == raw["species"]
            ]
            # A source-aligned annotation, official identifier and explicit matching
            # source species are all required. External IDs never establish organism.
            if not ids and len(external_ids) == len(candidates) == 1:
                candidate = candidates[0]
                aliases = {candidate["name"].casefold()} | {
                    a.strip().casefold() for a in candidate.get("otheraliases", "").split(",")
                }
                if entity.name.casefold() not in aliases:
                    return {
                        **raw,
                        "entity_id": None,
                        "mapping_status": "annotation_name_conflict",
                        "mapping_source": "NCBI Gene ESummary",
                        "mapping_version": self.external_catalog["retrieved_utc"],
                    }
                canonical_rows = [
                    r
                    for r in self.index.get(candidate["name"], [])
                    if r["species"] == raw["species"]
                    and r.get("hgnc_id")
                    and str(r["mapping_status"]).startswith("resolved")
                ]
                canonical_ids = {r["hgnc_id"] for r in canonical_rows}
                if len(canonical_ids) == 1:
                    hgnc_id = next(iter(canonical_ids))
                    return {
                        **raw,
                        "entity_id": stable_id("gene", {"species": raw["species"], "hgnc_id": hgnc_id}),
                        "hgnc_id": hgnc_id,
                        "ncbi_gene_id": str(candidate["uid"]),
                        "mapping_status": "resolved_source_annotation_hgnc",
                        "mapping_source": "NCBI Gene ESummary + HGNC project snapshot",
                        "mapping_version": self.external_catalog["retrieved_utc"],
                    }
                return {
                    **raw,
                    "entity_id": stable_id("gene", {"species": raw["species"], "ncbi_gene_id": str(candidate["uid"])}),
                    "ncbi_gene_id": str(candidate["uid"]),
                    "approved_symbol": candidate["name"],
                    "mapping_status": "resolved_source_annotation_ncbi",
                    "mapping_source": self.external_catalog["source"],
                    "mapping_version": self.external_catalog["retrieved_utc"],
                }
            return {
                **raw,
                "entity_id": None,
                "mapping_status": "ambiguous" if ids else "unresolved",
                "mapping_source": "HGNC project snapshot",
                "mapping_version": self.version,
            }
        row = rows[0]
        return {
            **raw,
            "entity_id": stable_id("gene", {"species": species_name(entity.species), "hgnc_id": row["hgnc_id"]}),
            "hgnc_id": row["hgnc_id"],
            "project_gene_id": row["gene_id"],
            "mapping_status": "resolved",
            "mapping_source": row["mapping_source"],
            "mapping_version": row["mapping_version"],
        }


def assess(finding, review, parts: list[dict], bundle: dict, resolver: EntityResolver, identity_hints=None) -> dict:
    by_id = {p["part_id"]: p for p in parts}
    failures, uncertain, spans = [], [], []
    if finding.assertion.strip().casefold() in {
        "reported",
        "measured",
        "inferred",
        "unclear",
        "unknown",
        "not established",
    }:
        failures.append("assertion_is_status_label_not_proposition")
    for citation in finding.citations:
        part = by_id.get(citation.part_id)
        if part is None or citation.quote not in part["text"]:
            failures.append("quote_not_in_supplied_source")
            continue
        # Preserve every matching occurrence instead of inventing a unique ambiguous offset.
        offset = 0
        while (offset := part["text"].find(citation.quote, offset)) >= 0:
            spans.append(
                {
                    "part_id": part["part_id"],
                    "document_id": part["document_id"],
                    "document_sha256": part["document_sha256"],
                    "asset_sha256": part["asset_sha256"],
                    "start": part["start"] + offset,
                    "end": part["start"] + offset + len(citation.quote),
                    "quote": citation.quote,
                    "locator": part["locator"],
                    "page": part.get("page"),
                }
            )
            offset += len(citation.quote)
    for q in finding.quantities:
        part = by_id.get(q.part_id)
        reported = bool(part and q.raw_value in part["text"])
        if reported and any(char.isdigit() for char in q.raw_value):
            # A numeric substring is not a source value: preserve minus signs,
            # inequalities, exponents and full digits rather than accepting 1 in 10.
            reported = re.search(r"(?<![\w.<>≤≥+−-])" + re.escape(q.raw_value) + r"(?![\w.])", part["text"]) is not None
        if not reported:
            failures.append("quantity_not_source_reported")
        if part and (part.get("cells") or part.get("kind") in {"table_row", "supplement_table_row"}) and not q.cell_ref:
            failures.append("table_quantity_missing_cell_reference")
        if q.units and part:
            unit_surface = canonical_json({k: part.get(k) for k in ("text", "table_header", "cells")}).casefold()
            if q.units.casefold() not in unit_surface:
                uncertain.append("quantity_units_not_source_located")
        if q.cell_ref:
            cells = (part or {}).get("cells") or []
            if not any(
                f"{part['part_id']}:c{c['col_start']}" == q.cell_ref
                and str(c.get("raw_value", c.get("text"))) == q.raw_value
                for c in cells
            ):
                failures.append("table_cell_mismatch")
        if not q.units or not q.comparison:
            uncertain.append("quantity_meaning_incomplete")
    if review is None or review.status == "INSUFFICIENT_CONTEXT":
        uncertain.append("verifier_context_or_execution_incomplete")
    elif review.status == "UNSUPPORTED" or review.field_issues:
        failures.append("verifier_unsupported_fields")
    # Reject an opposing sign only when all literal directional cues in the cited
    # text agree and the named target occurs there. Mixed/negated text is not inferred.
    quoted = " ".join(c.quote for c in finding.citations).casefold()
    if finding.object.name.casefold() in quoted and not re.search(r"\b(no|not|without|neither|unchanged)\b", quoted):
        up = bool(re.search(r"\b(increas\w*|up[- ]?regulat\w*)\b", quoted))
        down = bool(re.search(r"\b(decreas\w*|down[- ]?regulat\w*)\b", quoted))
        if (up and not down and finding.direction == "DECREASE") or (
            down and not up and finding.direction == "INCREASE"
        ):
            failures.append("target_change_opposes_unambiguous_cited_direction")
    if review is not None and review.source_target_change != finding.direction:
        failures.append("source_target_change_disagrees_with_extraction")
    if (
        finding.relation in {"BINDS", "MOTIF_ASSOCIATION", "EXPRESSION_ASSOCIATION", "PREDICTS"}
        and finding.directness == "direct"
    ):
        failures.append("direct_regulation_not_established_by_evidence_type")
    if finding.relation in {"REGULATES", "BINDS"} and finding.subject.kind not in {
        "gene",
        "protein",
        "complex",
        "family",
        "gene_group",
    }:
        failures.append("regulatory_relation_requires_regulator_entity")
    if finding.direction == "NO_EFFECT" and finding.outcome != "negative_or_null":
        failures.append("null_direction_outcome_mismatch")
    if finding.statement_status != "primary_result":
        uncertain.append("discovery_only_secondary_or_speculative")
    if any(getattr(finding.context, k) is None for k in ("species", "tissue", "cell_type")):
        uncertain.append("essential_context_unknown")
    if finding.assay is None:
        uncertain.append("assay_unknown")
    hints = identity_hints or {}
    subject = resolver.resolve(finding.subject, hints.get("subject"))
    obj = resolver.resolve(finding.object, hints.get("object"))
    if any(e["entity_id"] is None for e in (subject, obj)):
        uncertain.append("unresolved_scoring_entity")
    for entity in (finding.subject, finding.object):
        if entity.kind == "gene":
            if entity.species is None:
                uncertain.append("entity_species_unknown")
            elif finding.context.species and species_name(entity.species) != species_name(finding.context.species):
                uncertain.append("entity_experiment_species_conflict")
    status = "REJECTED" if failures else "UNCERTAIN" if uncertain else "AUTO_ACCEPTED"
    # An intervention effect is part of the proposition; opposite manipulations cannot collapse.
    proposition = {
        "subject": {k: subject[k] for k in ("entity_id", "kind", "species")},
        "object": {k: obj[k] for k in ("entity_id", "kind", "species")},
        "relation": finding.relation,
        "direction": finding.direction,
        "intervention": finding.intervention,
        "context": {**finding.context.model_dump(), "species": species_name(finding.context.species)},
    }
    claim = stable_id("claim", proposition)
    finding_id = stable_id(
        "finding",
        {
            "publication": bundle["publication_id"],
            "proposition": proposition,
            "assay": finding.assay,
            "experiment": finding.experiment_label,
            "quantities": [q.model_dump() for q in finding.quantities],
            "outcome": finding.outcome,
            "directness": finding.directness,
            "statement_status": finding.statement_status,
            "spans": sorted(spans, key=canonical_json),
        },
    )
    return {
        "finding_id": finding_id,
        "claim_id": claim,
        "publication_id": bundle["publication_id"],
        "pmid": bundle["pmid"],
        "bundle_id": bundle["payload_id"],
        "status": status,
        "finding": finding.model_dump(),
        "subject": subject,
        "object": obj,
        "proposition": proposition,
        "spans": spans,
        "failures": sorted(set(failures)),
        "uncertainties": sorted(set(uncertain)),
        "verification": review.model_dump() if review else None,
        "independent_study_id": None,
        "experiment_identity_status": "not_independently_resolved",
    }
