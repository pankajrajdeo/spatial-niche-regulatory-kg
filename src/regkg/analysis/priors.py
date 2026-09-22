"""CollecTRI signed TF→target prior, acquired from its documented Zenodo export.

decoupler 2.2.0's `op.collectri()` reads the same file but then drops rows with missing fields
and keeps only the first row per (source, target), which would discard contradictory-sign
records. The raw export is therefore cached and parsed here with every row preserved.
"""

from __future__ import annotations

from pathlib import Path

from regkg.resources import (
    Fetcher,
    ResourceError,
    Snapshot,
    cached_snapshot,
    dump_json,
    selected_headers,
    store_snapshot,
)

ZENODO_API = "https://zenodo.org/api/records/{record}"
ZENODO_FILE = "https://zenodo.org/records/{record}/files/{filename}?download=1"


def acquire_collectri(external_root: Path, record: str, filename: str, fetcher: Fetcher) -> Snapshot:
    directory = external_root / "collectri" / f"zenodo-{record}"
    cached = cached_snapshot(directory, filename)
    if cached is not None:
        return cached
    record_metadata = fetcher.get_json(ZENODO_API.format(record=record))
    files = {entry["key"]: entry for entry in record_metadata.get("files", [])}
    if filename not in files:
        raise ResourceError(f"Zenodo record {record} has no file {filename}")
    algorithm, _, checksum = files[filename]["checksum"].partition(":")
    if algorithm != "md5":
        raise ResourceError(f"unexpected Zenodo checksum algorithm {algorithm!r}")
    url = ZENODO_FILE.format(record=record, filename=filename)
    response = fetcher.get(url)
    dump_json(directory / "zenodo_record.json", record_metadata)
    metadata = record_metadata.get("metadata", {})
    return store_snapshot(
        directory,
        filename,
        response.content,
        url,
        fetcher,
        expected_md5_hex=checksum,
        metadata={
            "resource": "CollecTRI regulons",
            "publisher": "Zenodo record deposited by the CollecTRI authors (saezlab)",
            "zenodo_record": record,
            "doi": record_metadata.get("doi"),
            "version": metadata.get("version"),
            "publication_date": metadata.get("publication_date"),
            "license": (metadata.get("license") or {}).get("id"),
            "title": metadata.get("title"),
            "integration_reference": "decoupler 2.2.0 decoupler.op.collectri() documents this export URL",
        },
        response_headers=selected_headers(response),
    )


# ---------------------------------------------------------------------------
# Parsing: one prior record per supplied row.

# CollecTRI's sign_decision field (Müller-Dott et al., NAR 2023): "PMID" = sign from curated
# literature evidence; "regulon" = sign inferred from the TF's regulon majority; "default
# activation" = no sign evidence, +1 assumed by the resource. The last is stored as unknown.
SIGN_BASIS = {"PMID": "pmid_evidence", "regulon": "tf_regulon_majority", "default activation": "default_activation"}
REQUIRED_COLUMNS = ["source", "target", "weight", "resources", "references", "sign_decision"]


def _sign(weight: float, basis: str) -> str:
    if basis == "default_activation":
        return "unknown"
    return {1.0: "activation", -1.0: "repression"}.get(weight, "unknown")


def parse_collectri(snapshot: Snapshot, hgnc, complex_regulators: list[str]):
    import pandas as pd

    from regkg.analysis.gene_mapping import resolve_symbol, symbol_index
    from regkg.project_data.io import READ_OPTIONS
    from regkg.provenance import stable_id

    raw = pd.read_csv(snapshot.path, dtype=str, **READ_OPTIONS)
    if list(raw.columns) != REQUIRED_COLUMNS:
        raise ResourceError(f"CollecTRI export columns {list(raw.columns)} differ from {REQUIRED_COLUMNS}")
    unknown_basis = sorted(set(raw["sign_decision"]) - set(SIGN_BASIS))
    if unknown_basis:
        raise ResourceError(f"unrecognized CollecTRI sign_decision values {unknown_basis}")
    weights = pd.to_numeric(raw["weight"], errors="raise")
    approved, previous, alias = symbol_index(hgnc)
    symbol_of = dict(zip(hgnc["hgnc_id"], hgnc["symbol"], strict=True))

    def resolve(symbol: str) -> tuple[str | None, str, str | None, list[str]]:
        status, hgnc_id, route, candidates = resolve_symbol(symbol, approved, previous, alias)
        return hgnc_id, status, route, candidates

    provenance = snapshot.provenance
    records = []
    for index, row in raw.iterrows():
        regulator_complex = row["source"] in complex_regulators
        regulator_hgnc, regulator_status, regulator_route, regulator_candidates = (
            (None, "complex_not_split", None, []) if regulator_complex else resolve(row["source"])
        )
        target_hgnc, target_status, target_route, target_candidates = resolve(row["target"])
        basis = SIGN_BASIS[row["sign_decision"]]
        references = [ref.removeprefix("CollecTRI:") for ref in row["references"].split(";") if ref]
        records.append(
            {
                "prior_interaction_id": stable_id(
                    "prior",
                    {
                        "snapshot_sha256": provenance["sha256"],
                        "source_row_index": int(index),
                        "regulator": row["source"],
                        "target": row["target"],
                    },
                ),
                "resource": "CollecTRI",
                "resource_version": provenance.get("version"),
                "resource_doi": provenance.get("doi"),
                "snapshot_sha256": provenance["sha256"],
                "license": provenance.get("license"),
                "retrieved_at": provenance["retrieved_at"],
                "source_row_index": int(index),
                "regulator_symbol_raw": row["source"],
                "regulator_type": "complex" if regulator_complex else "gene",
                "regulator_mapping_status": regulator_status,
                "regulator_match_route": regulator_route,
                "regulator_candidate_hgnc_ids": regulator_candidates,
                "regulator_hgnc_id": regulator_hgnc,
                "regulator_approved_symbol": symbol_of.get(regulator_hgnc),
                "target_symbol_raw": row["target"],
                "target_mapping_status": target_status,
                "target_match_route": target_route,
                "target_candidate_hgnc_ids": target_candidates,
                "target_hgnc_id": target_hgnc,
                "target_approved_symbol": symbol_of.get(target_hgnc),
                "source_weight": float(weights[index]),
                "sign": _sign(float(weights[index]), basis),
                "sign_basis": basis,
                "pmids": [ref for ref in references if ref.isdigit()],
                "other_references": [ref for ref in references if not ref.isdigit()],
                "component_resources": sorted(
                    {r.removesuffix("_CollecTRI") for r in row["resources"].split(";") if r and r != "CollecTRI"}
                ),
            }
        )
    frame = pd.DataFrame(records)
    # Several records per regulator/target pair are kept; disagreement is flagged, never deduplicated.
    pair = frame.groupby(["regulator_symbol_raw", "target_symbol_raw"])
    frame["pair_record_count"] = pair["prior_interaction_id"].transform("size")
    frame["pair_signs_disagree"] = pair["source_weight"].transform("nunique") > 1
    return frame


def ulm_network(priors, allowed_sign_bases: list[str]):
    """Signed network for ULM plus an explicit exclusion reason for every record not used."""
    import pandas as pd

    frame = priors.copy()
    frame["regulator_key"] = frame["regulator_approved_symbol"].where(
        frame["regulator_type"] == "gene", frame["regulator_symbol_raw"]
    )
    reason = pd.Series("", index=frame.index, dtype=object)
    reason[frame["regulator_key"].isna()] = "regulator_not_uniquely_resolved"
    reason[(reason == "") & frame["target_hgnc_id"].isna()] = "target_not_uniquely_resolved"
    reason[(reason == "") & ~frame["sign_basis"].isin(allowed_sign_bases)] = "sign_basis_not_allowed"
    reason[(reason == "") & frame["pair_signs_disagree"]] = "contradictory_signs"
    candidate = reason == ""
    # Different raw symbols collapsing onto one mapped pair would otherwise be double counted.
    usable = frame[candidate]
    duplicated = usable.index[usable.duplicated(["regulator_key", "target_approved_symbol"], keep=False)]
    reason[duplicated] = "duplicate_mapped_pair"
    frame["ulm_exclusion_reason"] = reason.replace("", None)
    net = frame.loc[frame["ulm_exclusion_reason"].isna(), ["regulator_key", "target_approved_symbol", "source_weight"]]
    net = net.rename(columns={"regulator_key": "source", "target_approved_symbol": "target", "source_weight": "weight"})
    return frame, net.reset_index(drop=True)
