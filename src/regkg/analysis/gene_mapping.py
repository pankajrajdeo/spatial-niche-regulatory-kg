"""Official HGNC gene-mapping snapshot and exact, unambiguity-checked symbol resolution."""

from __future__ import annotations

from pathlib import Path
from urllib.parse import quote

from regkg.resources import (
    Fetcher,
    ResourceError,
    Snapshot,
    cached_snapshot,
    dump_json,
    md5_from_base64,
    selected_headers,
    store_snapshot,
)

HGNC_BUCKET = "public-download-files"
HGNC_ARCHIVE_PREFIX = "hgnc/archive/archive/monthly/tsv/"


def acquire_hgnc(external_root: Path, archive_date: str, fetcher: Fetcher) -> Snapshot:
    """Dated monthly HGNC complete-set archive, verified against its object-store MD5."""
    filename = f"hgnc_complete_set_{archive_date}.tsv"
    directory = external_root / "hgnc" / filename.removesuffix(".tsv")
    cached = cached_snapshot(directory, filename)
    if cached is not None:
        return cached
    object_name = HGNC_ARCHIVE_PREFIX + filename
    metadata_url = f"https://storage.googleapis.com/storage/v1/b/{HGNC_BUCKET}/o/{quote(object_name, safe='')}"
    object_metadata = fetcher.get_json(metadata_url)
    if "md5Hash" not in object_metadata:
        raise ResourceError(f"HGNC archive metadata for {object_name} lacks an MD5 checksum")
    url = f"https://storage.googleapis.com/{HGNC_BUCKET}/{object_name}"
    response = fetcher.get(url)
    dump_json(directory / "object_metadata.json", object_metadata)
    return store_snapshot(
        directory,
        filename,
        response.content,
        url,
        fetcher,
        expected_md5_hex=md5_from_base64(object_metadata["md5Hash"]),
        metadata={
            "resource": "HGNC complete set",
            "publisher": "HUGO Gene Nomenclature Committee",
            "version": archive_date,
            "object_generation": object_metadata.get("generation"),
            "object_updated": object_metadata.get("updated"),
            "species": "Homo sapiens",
            "license": "HGNC data are freely available (https://www.genenames.org/about/license/)",
        },
        response_headers=selected_headers(response),
    )


# ---------------------------------------------------------------------------
# Resolution. Case-sensitive exact matching only; no fuzzy, case-folded, or suffix-stripped keys.

STATUS_APPROVED = "resolved_approved_symbol"
STATUS_PREVIOUS = "resolved_previous_symbol"
STATUS_ALIAS = "resolved_alias_symbol"
STATUS_AMBIGUOUS = "ambiguous"
STATUS_CONFLICT = "conflict_shared_hgnc_id"
STATUS_UNRESOLVED = "unresolved"
RESOLVED = frozenset({STATUS_APPROVED, STATUS_PREVIOUS, STATUS_ALIAS})
MAPPING_RULE_VERSION = "hgnc-approved-then-indirect-union-2"


def read_hgnc(path: Path):
    import pandas as pd

    frame = pd.read_csv(path, sep="\t", dtype=str, keep_default_na=False, na_filter=False)
    required = {
        "hgnc_id",
        "symbol",
        "status",
        "alias_symbol",
        "prev_symbol",
        "entrez_id",
        "ensembl_gene_id",
        "locus_group",
        "locus_type",
        "name",
    }
    missing = required - set(frame.columns)
    if missing:
        raise ResourceError(f"HGNC snapshot lacks columns {sorted(missing)}")
    if frame["symbol"].duplicated().any() or frame["hgnc_id"].duplicated().any():
        raise ResourceError("HGNC snapshot has duplicated approved symbols or HGNC IDs")
    return frame


def _split(value: str) -> list[str]:
    return [item for item in value.split("|") if item]


def symbol_index(hgnc) -> tuple[dict[str, str], dict[str, set[str]], dict[str, set[str]]]:
    approved = dict(zip(hgnc["symbol"], hgnc["hgnc_id"], strict=True))
    previous: dict[str, set[str]] = {}
    alias: dict[str, set[str]] = {}
    for hgnc_id, prev_value, alias_value in zip(
        hgnc["hgnc_id"], hgnc["prev_symbol"], hgnc["alias_symbol"], strict=True
    ):
        for symbol in _split(prev_value):
            previous.setdefault(symbol, set()).add(hgnc_id)
        for symbol in _split(alias_value):
            alias.setdefault(symbol, set()).add(hgnc_id)
    return approved, previous, alias


def resolve_symbol(
    symbol: str, approved: dict[str, str], previous: dict[str, set[str]], alias: dict[str, set[str]]
) -> tuple[str, str | None, str | None, list[str]]:
    """Shared rule for project and prior symbols: (status, hgnc_id, match_route, candidate IDs).

    An exact approved symbol wins. Otherwise previous-symbol and alias owners are pooled: a single
    HGNC ID across both fields resolves; several IDs are ambiguous and none is selected. A match
    unique within one field can still collide with the other field, so fields are never tried in turn.
    """
    if symbol in approved:
        return STATUS_APPROVED, approved[symbol], "symbol", [approved[symbol]]
    from_previous, from_alias = previous.get(symbol, set()), alias.get(symbol, set())
    candidates = sorted(from_previous | from_alias)
    route = "|".join(name for name, ids in (("prev_symbol", from_previous), ("alias_symbol", from_alias)) if ids)
    if not candidates:
        return STATUS_UNRESOLVED, None, None, []
    if len(candidates) > 1:
        return STATUS_AMBIGUOUS, None, route, candidates
    status = STATUS_PREVIOUS if from_previous else STATUS_ALIAS
    return status, candidates[0], route, candidates


def resolve_symbols(genes, hgnc, version: str):
    """One mapping row per P1 local gene; P1 gene IDs are carried unchanged.

    Resolution follows `resolve_symbol`. A non-approved
    mapping onto an HGNC ID that another source feature already holds is a conflict, because two
    distinct supplied features must not be merged on nomenclature alone.
    """
    import pandas as pd

    approved, previous, alias = symbol_index(hgnc)
    by_id = hgnc.set_index("hgnc_id")
    rows = []
    for gene_id, symbol in zip(genes["gene_id"], genes["source_symbol"], strict=True):
        status, hgnc_id, route, candidates = resolve_symbol(symbol, approved, previous, alias)
        rows.append(
            {
                "gene_id": gene_id,
                "source_symbol": symbol,
                "mapping_status": status,
                "match_route": route,
                "hgnc_id": hgnc_id,
                "candidate_hgnc_ids": candidates,
            }
        )
    frame = pd.DataFrame(rows)

    resolved = frame["mapping_status"].isin(RESOLVED)
    holders = frame[resolved].groupby("hgnc_id")["gene_id"].agg(list)
    shared = holders[holders.map(len) > 1]
    conflict = pd.Series(False, index=frame.index)
    for gene_ids in shared:
        members = frame["gene_id"].isin(gene_ids)
        # An exact approved-symbol holder keeps the ID; indirect claimants are rejected.
        has_exact = (members & (frame["mapping_status"] == STATUS_APPROVED)).any()
        conflict |= members & ((frame["mapping_status"] != STATUS_APPROVED) | ~has_exact)
    frame["conflicting_gene_ids"] = [
        sorted(set(shared.get(h, [])) - {g}) if c else []
        for g, h, c in zip(frame["gene_id"], frame["hgnc_id"], conflict, strict=True)
    ]
    frame.loc[conflict, "mapping_status"] = STATUS_CONFLICT
    frame.loc[conflict, "hgnc_id"] = None

    kept = frame["hgnc_id"].notna()
    frame["approved_symbol"] = frame["hgnc_id"].map(by_id["symbol"]).where(kept)
    frame["ncbi_gene_id"] = frame["hgnc_id"].map(by_id["entrez_id"]).where(kept).replace("", None)
    frame["ensembl_gene_id"] = frame["hgnc_id"].map(by_id["ensembl_gene_id"]).where(kept).replace("", None)
    frame["locus_group"] = frame["hgnc_id"].map(by_id["locus_group"]).where(kept)
    frame["species"] = "Homo sapiens"
    frame["mapping_source"] = "HGNC complete set"
    frame["mapping_version"] = version
    frame["mapping_rule_version"] = MAPPING_RULE_VERSION
    return frame[
        [
            "gene_id",
            "source_symbol",
            "species",
            "mapping_status",
            "match_route",
            "hgnc_id",
            "approved_symbol",
            "ncbi_gene_id",
            "ensembl_gene_id",
            "locus_group",
            "candidate_hgnc_ids",
            "conflicting_gene_ids",
            "mapping_source",
            "mapping_version",
            "mapping_rule_version",
        ]
    ]


def safe_aliases(hgnc_id: str, hgnc, limit: int = 3) -> list[str]:
    """Aliases usable in literature queries: unique across all HGNC symbol fields, >=4 chars, with a digit.

    The digit/length rule avoids short or word-like aliases (e.g. "AA", "CKLF") that retrieve
    unrelated papers; uniqueness avoids aliases shared with, or equal to, another gene's symbol.
    """
    approved, previous, alias = symbol_index(hgnc)
    row = hgnc.loc[hgnc["hgnc_id"] == hgnc_id].iloc[0]
    chosen = []
    for candidate in sorted(set(_split(row["alias_symbol"])) | set(_split(row["prev_symbol"]))):
        owners = set(previous.get(candidate, ())) | set(alias.get(candidate, ()))
        if candidate in approved:
            owners.add(approved[candidate])
        if owners == {hgnc_id} and len(candidate) >= 4 and any(ch.isdigit() for ch in candidate):
            chosen.append(candidate)
    return chosen[:limit]
