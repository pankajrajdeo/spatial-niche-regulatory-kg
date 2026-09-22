"""Literature stages: search -> fetch/parse -> retrieve, each an atomically published artifact.

Stage keys include the outcome of every source request, so a rerun reuses cached successes,
retries only failed requests, and publishes a new artifact only when an outcome changed.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from dataclasses import fields as dataclass_fields
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

import regkg
from regkg.analysis.verify import artifact_integrity as candidate_integrity
from regkg.config import (
    LiteratureConfig,
    LoadedProjectConfig,
    load_environment,
    load_literature_config,
    load_model_settings,
)
from regkg.literature import embeddings as emb
from regkg.literature.fetch import fetch_publication, fetch_pubtator
from regkg.literature.http import NcbiSettings, SourceClient, SourceError
from regkg.literature.parse import (
    Document,
    ParseError,
    Passage,
    parse_bioc,
    parse_jats,
    parse_pubmed_abstract,
    parse_search_record,
)
from regkg.literature.passages import Mention, candidate_name_mentions, pubtator_mentions, reconcile
from regkg.literature.publications import Publication, resolve_publications, select_corpus, selection_features
from regkg.literature.retrieval import BM25Okapi, QueryTerms, assemble_bundles, rank_passages, tokenize
from regkg.literature.search import STATUS_EMPTY, STATUS_FAILED, STATUS_PARTIAL, QuerySpec, SourceRecord, search_papers
from regkg.models import StageStatus
from regkg.provenance import (
    canonical_json,
    code_fingerprint,
    describe_outputs,
    discard_directory,
    git_revision,
    new_execution_id,
    publish_directory,
    read_json,
    sha256_text,
    software_versions,
    staging_directory,
    utc_now,
    write_json,
)

SCHEMA_VERSION = "p3-literature-3"
CODE_PATHS = ["literature", "workflows"]
SOFTWARE = ["httpx", "lxml", "rank-bm25", "numpy", "pandas", "pyarrow", "langchain-ollama", "langchain-core"]

# Coverage vocabulary (plan P3.11). Search-level labels describe the executed retrieval only.
NOT_SEARCHED = "NOT_SEARCHED"
SEARCHED = "SEARCHED_RESULTS_RETAINED"
SEARCHED_NO_SUPPORT_FOUND = "SEARCHED_NO_SUPPORT_FOUND"
SEARCHED_PARTIAL = "SEARCHED_PARTIAL_SOURCE_FAILURE"
SEARCH_FAILED = "SEARCH_FAILED"
FULL_TEXT_PROCESSED = "FULL_TEXT_PROCESSED"
ABSTRACT_ONLY = "ABSTRACT_ONLY"
FETCH_FAILED = "FETCH_FAILED"
PARSE_FAILED = "PARSE_FAILED"
NOT_FOUND = "NOT_FOUND"
NO_CANDIDATE_PASSAGES = "NO_CANDIDATE_PASSAGES"
CANDIDATE_PASSAGES_FOUND = "CANDIDATE_PASSAGES_FOUND"


class LiteratureStageError(RuntimeError):
    """A literature stage failed; this attempt published nothing."""


@dataclass
class StageOutcome:
    stage: str
    status: StageStatus
    key: str
    artifact_dir: Path
    execution_id: str
    network_requests: dict[str, int]
    counts: dict[str, Any] = field(default_factory=dict)


def _relative(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def candidate_integrity_any(candidate_dir: Path):
    """Integrity of an AT1 baseline (`p2-candidates-2`) or manuscript (`p2-manuscript-1`) candidate artifact.

    Both carry a lineage-compatible queue; the manuscript queue adds `cell_type` and fair batches.
    """
    from regkg.analysis import schemas

    manifest = candidate_dir / "manifest.json"
    schema = read_json(manifest).get("schema_version") if manifest.is_file() else None
    allowed = {schemas.CANDIDATE_SCHEMA_VERSION, schemas.MANUSCRIPT_SCHEMA_VERSION}
    return candidate_integrity(candidate_dir, schema if schema in allowed else schemas.CANDIDATE_SCHEMA_VERSION)


def artifact_integrity(directory: Path, stage: str):
    from regkg.project_data.verify import Checks
    from regkg.provenance import sha256_file

    checks = Checks()
    manifest_path = directory / "manifest.json"
    if not manifest_path.is_file():
        checks.add(f"{stage}:manifest", False, f"missing {manifest_path}")
        return checks.results
    manifest = read_json(manifest_path)
    checks.add(
        f"{stage}:manifest",
        manifest.get("status") in {StageStatus.SUCCEEDED.value, StageStatus.PARTIAL.value}
        and manifest.get("schema_version") == SCHEMA_VERSION
        and manifest.get("key") == directory.name,
        f"status {manifest.get('status')}, schema {manifest.get('schema_version')}, key {manifest.get('key')}",
    )
    listed = {o["path"]: o["sha256"] for o in manifest.get("outputs", [])}
    present = {p.relative_to(directory).as_posix() for p in directory.rglob("*") if p.is_file()} - {"manifest.json"}
    changed = sorted(p for p, d in listed.items() if not (directory / p).is_file() or sha256_file(directory / p) != d)
    checks.add(
        f"{stage}:output_checksums",
        not changed and present == set(listed),
        f"{len(listed)} outputs; changed/missing {changed[:5]}; unlisted {sorted(present - set(listed))[:5]}",
    )
    return checks.results


def _run(
    loaded: LoadedProjectConfig,
    stage: str,
    prefix: str,
    identity: dict,
    build,
    network: SourceClient | None,
    extra_record: dict,
    local_requests: dict | None = None,
) -> StageOutcome:
    """Publish `build(staging) -> (counts, status)` under a content key, or reuse an identical artifact."""
    execution_id = new_execution_id(stage)
    runs = loaded.data_root / "runs" / execution_id
    record = {"stage": stage, "execution_id": execution_id, "started_at": utc_now(), **extra_record}
    key = f"{prefix}-{sha256_text(canonical_json(identity))[:16]}"
    record["key"] = key
    final = loaded.data_root / "processed" / key
    try:
        if final.exists():
            failed = [c for c in artifact_integrity(final, stage) if not c.passed]
            if failed:
                raise LiteratureStageError(
                    f"existing artifact {key} failed integrity and will not be replaced: {failed}"
                )
            counts = read_json(final / "manifest.json")["counts"]
            status = StageStatus.REUSED
        else:
            staging = staging_directory(final, execution_id)
            try:
                counts, stage_status = build(staging, key, execution_id, record["started_at"])
                publish_directory(staging, final)
            except BaseException:
                discard_directory(staging)
                raise
            status = stage_status
    except Exception as error:
        record.update(
            status=StageStatus.FAILED.value,
            ended_at=utc_now(),
            error=f"{type(error).__name__}: {error}",
            network_requests=network.network_requests if network else {},
        )
        write_json(runs / "execution.json", record)
        raise
    # This execution's actual requests, distinct from the build counts stored in a reused manifest.
    requests = network.network_requests if network else dict(local_requests or {})
    record.update(
        status=status.value, ended_at=utc_now(), network_requests=requests, artifact=_relative(final, loaded.repo_root)
    )
    write_json(runs / "execution.json", record)
    return StageOutcome(stage, status, key, final, execution_id, requests, counts)


def _manifest(
    out: Path,
    stage: str,
    key: str,
    execution_id: str,
    started: str,
    status: StageStatus,
    inputs: dict,
    config: dict,
    counts: dict,
    repo_root: Path,
    rows: dict[str, int],
    extra: dict | None = None,
) -> None:
    write_json(
        out / "manifest.json",
        {
            "stage": stage,
            "schema_version": SCHEMA_VERSION,
            "key": key,
            "status": status.value,
            "execution_id": execution_id,
            "started_at": started,
            "ended_at": utc_now(),
            "input_mode": "real_sources",
            "inputs": inputs,
            "config": config,
            "counts": counts,
            "code": {
                "fingerprint": code_fingerprint(Path(regkg.__file__).parent, CODE_PATHS),
                "paths": CODE_PATHS,
                "git": git_revision(repo_root),
            },
            "software": software_versions(SOFTWARE),
            "outputs": describe_outputs(out, rows),
            **(extra or {}),
        },
    )


def _write_parquet(frame: pd.DataFrame, path: Path) -> int:
    frame.to_parquet(path, index=False)
    return len(frame)


def _jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(r, sort_keys=True, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")


def _client(loaded: LoadedProjectConfig, config: LiteratureConfig, process_env=None) -> SourceClient:
    env = load_environment(loaded.repo_root / ".env", process_env)
    return SourceClient(
        loaded.data_root / "external" / "literature_cache",
        NcbiSettings.from_env(env, config.search.contact_tool),
        timeout_seconds=config.search.timeout_seconds,
        max_retries=config.search.max_retries,
    )


def _request_outcomes(client: SourceClient) -> list[list[str]]:
    """Identity of what the sources returned: response SHA-256 for successes (equal whether fetched or
    cached), the classified outcome for failures. No timestamps, counts, credentials, or contacts."""
    outcomes = set()
    for r in client.records:
        if r.outcome in {"cached", "fetched"}:
            outcomes.add((r.cache_key, "ok", r.sha256))
        elif r.outcome == "not_found":
            outcomes.add((r.cache_key, "not_found", str(r.http_status)))
        else:
            outcomes.add((r.cache_key, "failed", r.error_kind or "unknown"))
    return sorted(outcomes)


def _names_from_queue(queue: pd.DataFrame) -> tuple[dict[str, list[str]], dict[str, list[str]]]:
    tf_names: dict[str, list[str]] = {}
    target_names: dict[str, list[str]] = {}
    for row in queue.itertuples(index=False):
        terms = json.loads(row.terms_json)
        tf_names.setdefault(row.tf_hgnc_id, list(terms["tf"]))
        if isinstance(row.target_hgnc_id, str) and row.target_hgnc_id:  # TF-only queries have a null target
            target_names.setdefault(row.target_hgnc_id, list(terms["target"]))
    return tf_names, target_names


# ---------------------------------------------------------------------------
# Stage 1: search and corpus selection


def run_search(
    loaded: LoadedProjectConfig,
    candidate_key: str,
    max_papers: int,
    literature: Path,
    client: SourceClient | None = None,
) -> StageOutcome:
    config = load_literature_config(literature)
    if not 0 < max_papers <= config.search.max_papers:
        raise LiteratureStageError(f"--max-papers must be between 1 and {config.search.max_papers}")
    candidate_dir = loaded.data_root / "processed" / candidate_key
    failed = (
        [c for c in candidate_integrity_any(candidate_dir) if not c.passed] if candidate_dir.is_dir() else ["missing"]
    )
    if failed:
        raise LiteratureStageError(f"candidate artifact {candidate_key} is missing or failed integrity: {failed}")
    queue = pd.read_parquet(candidate_dir / "retrieval_queue.parquet").sort_values("priority")
    executed = queue[queue["in_initial_live_slice"]].head(config.search.max_queries)
    seeds = pd.read_parquet(candidate_dir / "seed_publications.parquet")
    candidates = pd.read_parquet(candidate_dir / "candidates.parquet")
    client = client or _client(loaded, config)

    results = []
    for row in executed.itertuples(index=False):
        results.append(
            (
                row,
                search_papers(
                    QuerySpec.from_queue_row(row.query_id, row.terms_json),
                    client,
                    config.search.sources,
                    config.search.max_results_per_query,
                ),
            )
        )
    advisor_records, advisor_status = [], "disabled"
    if config.search.include_advisor_seed_metadata:
        from regkg.literature.search import parse_pubmed_xml

        try:
            response = client.get(
                "pubmed",
                "efetch.fcgi",
                {"db": "pubmed", "id": ",".join(sorted(seeds["pmid"], key=int)), "retmode": "xml"},
                validate=lambda r: parse_pubmed_xml(r.content, ""),
            )
            advisor_records = parse_pubmed_xml(response.body, response.cache_key)
            advisor_status = f"fetched:{len(advisor_records)}"
        except SourceError as error:
            advisor_status = f"failed:{error.kind}"
    identity = {
        "stage": "literature_search",
        "schema": SCHEMA_VERSION,
        "candidate_key": candidate_key,
        "queries": executed["query_id"].tolist(),
        "max_papers": max_papers,
        "search_config": config.search.model_dump(mode="json"),
        "code": code_fingerprint(Path(regkg.__file__).parent, CODE_PATHS),
        "requests": _request_outcomes(client),
    }

    def build(out: Path, key: str, execution_id: str, started: str):
        labelled: list[tuple[str, SourceRecord]] = []
        retained: dict[str, list[str]] = {}
        for row, result in results:
            labelled.extend((row.query_id, record) for record in result.records)
        labelled.extend(("advisor_seed", record) for record in advisor_records)
        publications = resolve_publications(labelled)
        pub_of = {}
        for publication in publications:
            for label, record in publication.records:
                pub_of[(label, record.source, record.rank, id(record))] = publication.publication_id
        hit_rows = []
        for row, result in results:
            best: dict[str, tuple[int, str]] = {}
            for record in result.records:
                pid = pub_of[(row.query_id, record.source, record.rank, id(record))]
                pmid = record.pmid or ""
                if pid not in best or record.rank < best[pid][0]:
                    best[pid] = (record.rank, pmid)
                hit_rows.append(
                    {
                        "query_id": row.query_id,
                        "source": record.source,
                        "rank": record.rank,
                        "publication_id": pid,
                        "pmid": record.pmid,
                        "pmcid": record.pmcid,
                        "doi": record.doi,
                        "epmc_id": record.epmc_id,
                        "response_cache_key": record.cache_key,
                    }
                )
            order = sorted(best, key=lambda p: (best[p][0], int(best[p][1]) if best[p][1] else 10**12, p))
            retained[row.query_id] = order[: config.search.max_results_per_query]
        retained_ids = {p for ids in retained.values() for p in ids}
        pool = [
            p
            for p in publications
            if p.publication_id in retained_ids or any(label == "advisor_seed" for label, _ in p.records)
        ]
        tf_names, target_names = _names_from_queue(queue)
        target_names = {h: n for h, n in target_names.items() if h in set(executed["target_hgnc_id"].dropna())}
        features = [
            selection_features(
                p, tf_names, target_names, config.search.context_terms, config.search.assay_terms, set(seeds["pmid"])
            )
            for p in pool
        ]
        seed_tfs = sorted(set(candidates.loc[candidates["is_seed"], "tf_hgnc_id"]))
        pmids = {p.publication_id: p.identifiers.get("pmid") for p in pool}
        chosen = select_corpus(features, pmids, seed_tfs, max_papers)
        order = {pid: i for i, (pid, _) in enumerate(chosen, start=1)}
        reason = dict(chosen)

        query_rows = []
        executed_ids = {row.query_id: (row, result) for row, result in results}
        for row in queue.itertuples(index=False):
            entry = {
                "query_id": row.query_id,
                "priority": int(row.priority),
                "query_type": row.query_type,
                "tf_hgnc_id": row.tf_hgnc_id,
                "tf_symbol": row.tf_symbol,
                "target_hgnc_id": row.target_hgnc_id,
                "target_symbol": row.target_symbol,
                "is_seed_tf": bool(row.is_seed_tf),
                "terms_json": row.terms_json,
                "candidate_ids": json.dumps(list(row.candidate_ids)),
            }
            if row.query_id in executed_ids:
                result = executed_ids[row.query_id][1]
                status = {
                    STATUS_FAILED: SEARCH_FAILED,
                    STATUS_PARTIAL: SEARCHED_PARTIAL,
                    STATUS_EMPTY: SEARCHED_NO_SUPPORT_FOUND,
                }.get(result.status, SEARCHED)
                entry.update(
                    search_status=status,
                    retained_publications=len(retained[row.query_id]),
                    source_outcomes=json.dumps([asdict(o) for o in result.outcomes]),
                    warnings=json.dumps(result.warnings),
                    translations=json.dumps(result.translations),
                )
            else:
                entry.update(
                    search_status=NOT_SEARCHED,
                    retained_publications=0,
                    source_outcomes="[]",
                    warnings="[]",
                    translations="{}",
                )
            query_rows.append(entry)
        pub_rows = []
        for publication in publications:
            memberships = [
                {"label": label, "source": record.source, "rank": record.rank} for label, record in publication.records
            ]
            pub_rows.append(
                {
                    "publication_id": publication.publication_id,
                    "identifiers": json.dumps(publication.identifiers, sort_keys=True),
                    "pmid": publication.identifiers.get("pmid"),
                    "pmcid": publication.identifiers.get("pmcid"),
                    "doi": publication.identifiers.get("doi"),
                    "title": publication.best("title"),
                    "abstract": publication.best("abstract"),
                    "year": publication.best("year"),
                    "journal": publication.best("journal"),
                    "is_preprint": publication.is_preprint,
                    "retracted": publication.retracted,
                    "corrections": json.dumps([c for _, r in publication.records for c in r.corrections]),
                    "identity_conflict": json.dumps(publication.identity_conflict),
                    "memberships": json.dumps(memberships),
                    "records_json": json.dumps(
                        [{"label": label, **asdict(record)} for label, record in publication.records]
                    ),
                    "in_selection_pool": publication.publication_id in pmids,
                }
            )
        selection_rows = [
            {
                **asdict(f),
                "pmid": pmids[f.publication_id],
                "selected": f.publication_id in order,
                "selection_order": order.get(f.publication_id),
                "selection_reason": reason.get(f.publication_id),
            }
            for f in features
        ]
        requests = pd.DataFrame([asdict(r) for r in client.records]).assign(
            params=lambda f: f["params"].map(json.dumps)
        )
        rows = {
            "queries.parquet": _write_parquet(pd.DataFrame(query_rows), out / "queries.parquet"),
            "search_hits.parquet": _write_parquet(pd.DataFrame(hit_rows), out / "search_hits.parquet"),
            "publications.parquet": _write_parquet(pd.DataFrame(pub_rows), out / "publications.parquet"),
            "selection.parquet": _write_parquet(pd.DataFrame(selection_rows), out / "selection.parquet"),
            "source_requests.parquet": _write_parquet(requests, out / "source_requests.parquet"),
        }
        statuses = pd.DataFrame(query_rows)["search_status"].value_counts().to_dict()
        seed_covered = sorted({t for f in features if f.publication_id in order for t in f.tf_hgnc_ids} & set(seed_tfs))
        counts = {
            "queries_total": len(queue),
            "queries_executed": len(executed),
            "query_status": statuses,
            "source_records": len(labelled),
            "unique_publications": len(publications),
            "selection_pool": len(pool),
            "eligible": sum(f.eligible for f in features),
            "selected": len(order),
            "seed_tfs": seed_tfs,
            "seed_tfs_covered": seed_covered,
            "seed_tfs_uncovered": sorted(set(seed_tfs) - set(seed_covered)),
            "advisor_seed_metadata": advisor_status,
            "network_requests": client.network_requests,
            "request_outcomes": pd.Series([r.outcome for r in client.records]).value_counts().to_dict(),
            "ncbi_settings_present": client.ncbi.presence(),
        }
        write_json(out / "coverage.json", counts)
        partial = any(r.status in {STATUS_FAILED, STATUS_PARTIAL} for _, r in results) or advisor_status.startswith(
            "failed"
        )
        status = StageStatus.PARTIAL if partial else StageStatus.SUCCEEDED
        _manifest(
            out,
            "literature_search",
            key,
            execution_id,
            started,
            status,
            {"candidate_key": candidate_key},
            {"search": config.search.model_dump(mode="json"), "max_papers": max_papers},
            counts,
            loaded.repo_root,
            rows,
            # The exact identity hashed into the key (request outcomes with response hashes).
            {"identity": identity},
        )
        return counts, status

    try:
        return _run(loaded, "literature-search", "litsearch", identity, build, client, {"candidate_key": candidate_key})
    finally:
        client.close()


# ---------------------------------------------------------------------------
# Stage 2: fetch eligible assets and parse canonical documents


def _publications(search_dir: Path) -> list[Publication]:
    frame = pd.read_parquet(search_dir / "publications.parquet")
    selection = pd.read_parquet(search_dir / "selection.parquet")
    order = selection[selection["selected"]].sort_values("selection_order")["publication_id"].tolist()
    by_id = frame.set_index("publication_id")
    result = []
    for pid in order:
        row = by_id.loc[pid]
        records = []
        for item in json.loads(row["records_json"]):
            label = item.pop("label")
            records.append((label, SourceRecord(**item)))
        result.append(Publication(pid, json.loads(row["identifiers"]), records, json.loads(row["identity_conflict"])))
    return result


def _human_gene_map(candidate_dir: Path, repo_root: Path) -> dict[str, str]:
    from regkg.analysis.gene_mapping import read_hgnc

    hgnc_path = repo_root / read_json(candidate_dir / "resources.json")["hgnc"]["path"]
    hgnc = read_hgnc(hgnc_path)
    ids = hgnc[hgnc["entrez_id"] != ""]
    unique = ids[~ids["entrez_id"].duplicated(keep=False)]
    return dict(zip(unique["entrez_id"], unique["hgnc_id"], strict=True))


def run_fetch(
    loaded: LoadedProjectConfig, search_key: str, literature: Path, client: SourceClient | None = None
) -> StageOutcome:
    config = load_literature_config(literature)
    search_dir = loaded.data_root / "processed" / search_key
    failed = (
        [c for c in artifact_integrity(search_dir, "search") if not c.passed] if search_dir.is_dir() else ["missing"]
    )
    if failed:
        raise LiteratureStageError(f"search artifact {search_key} is missing or failed integrity: {failed}")
    if config.fetch.pdf_enabled:
        raise LiteratureStageError("PDF processing is not implemented in this build; set fetch.pdf_enabled: false")
    search_manifest = read_json(search_dir / "manifest.json")
    candidate_dir = loaded.data_root / "processed" / search_manifest["inputs"]["candidate_key"]
    publications = _publications(search_dir)
    client = client or _client(loaded, config)
    pmids = [p.identifiers["pmid"] for p in publications if "pmid" in p.identifiers]
    pubtator_docs, pubtator_key, pubtator_status = None, None, "disabled"
    if config.fetch.pubtator_annotations and pmids:
        try:
            pubtator_docs, pubtator_key = fetch_pubtator(client, pmids)
            pubtator_status = "fetched"
        except SourceError as error:
            pubtator_status = f"failed:{error.kind}"
    papers_root = loaded.data_root / "papers"
    fetched = [
        fetch_publication(
            client,
            p,
            pubtator_docs,
            pubtator_key,
            pubtator_status if pubtator_docs is None else "not_indexed",
            papers_root,
            loaded.repo_root,
        )
        for p in publications
    ]
    identity = {
        "stage": "literature_fetch",
        "schema": SCHEMA_VERSION,
        "search_key": search_key,
        "fetch_config": config.fetch.model_dump(mode="json"),
        "code": code_fingerprint(Path(regkg.__file__).parent, CODE_PATHS),
        "requests": _request_outcomes(client),
        # Stored per-paper assets (including PubTator documents split from the batch response).
        "assets": sorted(a.sha256 for r in fetched for a in r.assets),
    }
    queue = pd.read_parquet(search_dir / "queries.parquet")

    def build(out: Path, key: str, execution_id: str, started: str):
        tf_names, target_names = _names_from_queue(queue)
        names = {**target_names, **tf_names}
        human = _human_gene_map(candidate_dir, loaded.repo_root)
        paper_rows, passage_rows, mention_rows = [], [], []
        for publication, result in zip(publications, fetched, strict=True):
            assets = {a.role: a for a in result.assets}
            document, parse_error, full_text_error = None, None, None
            if "jats_full_text" in assets:
                try:
                    document = parse_jats(
                        publication.publication_id, (loaded.repo_root / assets["jats_full_text"].path).read_bytes()
                    )
                except (ParseError, ValueError) as error:
                    full_text_error = f"{type(error).__name__}: {error}"
            if (
                document is None
                and "pubtator_annotations" in assets
                and result.access_status == "open_access_full_text"
            ):
                try:
                    document = parse_bioc(
                        publication.publication_id,
                        (loaded.repo_root / assets["pubtator_annotations"].path).read_bytes(),
                    )
                except (ParseError, ValueError) as error:
                    full_text_error = (full_text_error or "") + f" bioc: {type(error).__name__}: {error}"
            if document is None and "pubmed_record" in assets:
                try:
                    document = parse_pubmed_abstract(
                        publication.publication_id, (loaded.repo_root / assets["pubmed_record"].path).read_bytes()
                    )
                except (ParseError, ValueError) as error:
                    parse_error = f"{type(error).__name__}: {error}"
            if document is None and "search_record" in assets:
                try:
                    document = parse_search_record(
                        publication.publication_id, (loaded.repo_root / assets["search_record"].path).read_bytes()
                    )
                except (ParseError, ValueError) as error:
                    parse_error = f"{type(error).__name__}: {error}"
            if document is not None:
                status = (
                    FULL_TEXT_PROCESSED
                    if document.text_version in {"europepmc_jats", "pubtator_bioc"}
                    else ABSTRACT_ONLY
                )
            elif not result.assets and result.pubmed_status == "not_found":
                status = NOT_FOUND
            elif not result.assets:
                status = FETCH_FAILED
            else:
                status = PARSE_FAILED
            mentions = []
            if document is not None:
                directory = out / "documents" / publication.publication_id.replace(":", "_")
                directory.mkdir(parents=True)
                payload = document.to_json()
                write_json(directory / "document.json", payload)
                passages = [asdict(p) for p in document.passages]
                _jsonl(
                    directory / "sections.jsonl",
                    [p for p in passages if p["kind"] in {"title", "abstract", "paragraph"}],
                )
                _jsonl(directory / "figure_captions.jsonl", [p for p in passages if p["kind"] == "figure_caption"])
                _jsonl(directory / "tables.jsonl", [p for p in passages if p["kind"].startswith("table_")])
                _jsonl(directory / "supplementary.jsonl", document.supplementary)
                mentions = candidate_name_mentions(document, names)
                if "pubtator_annotations" in assets:
                    mentions += pubtator_mentions(
                        document,
                        json.loads((loaded.repo_root / assets["pubtator_annotations"].path).read_bytes()),
                        human,
                    )
                mentions = reconcile(mentions)
                _jsonl(directory / "mentions.jsonl", [m.to_json() for m in mentions])
                for p in document.passages:
                    passage_rows.append(
                        {
                            "publication_id": publication.publication_id,
                            "canonical_sha256": document.canonical_sha256,
                            "text_version": document.text_version,
                            **asdict(p),
                        }
                    )
                mention_rows.extend(m.to_json() for m in mentions)
            paper_rows.append(
                {
                    "publication_id": publication.publication_id,
                    "selection_order": len(paper_rows) + 1,
                    "identifiers": json.dumps(result.identifiers, sort_keys=True),
                    "processing_status": status,
                    "access_status": result.access_status,
                    "license": result.license,
                    "pubmed_status": result.pubmed_status,
                    "full_text_status": result.full_text_status,
                    "pubtator_status": result.pubtator_status,
                    "text_version": document.text_version if document else None,
                    "canonical_sha256": document.canonical_sha256 if document else None,
                    "passages": len(document.passages) if document else 0,
                    "mentions": len(mentions),
                    "assets": json.dumps([asdict(a) for a in result.assets]),
                    "errors": json.dumps(result.errors),
                    "full_text_parse_error": full_text_error,
                    "parse_error": parse_error,
                    "pdf_branch": "not_needed",
                }
            )
        rows = {
            "papers.parquet": _write_parquet(pd.DataFrame(paper_rows), out / "papers.parquet"),
            "passages.parquet": _write_parquet(pd.DataFrame(passage_rows), out / "passages.parquet"),
            "mentions.parquet": _write_parquet(
                pd.DataFrame(mention_rows, columns=[f.name for f in dataclass_fields(Mention)]),
                out / "mentions.parquet",
            ),
        }
        papers = pd.DataFrame(paper_rows)
        mentions_frame = pd.DataFrame(mention_rows)
        counts = {
            "papers": len(papers),
            "processing_status": papers["processing_status"].value_counts().to_dict(),
            "access_status": papers["access_status"].value_counts().to_dict(),
            "full_text_status": papers["full_text_status"].value_counts().to_dict(),
            "pubtator_status": papers["pubtator_status"].value_counts().to_dict(),
            "passages": len(passage_rows),
            "mentions": len(mention_rows),
            "pubtator_alignment": mentions_frame[mentions_frame["source"] == "pubtator"]["alignment"]
            .value_counts()
            .to_dict()
            if len(mentions_frame)
            else {},
            "mention_resolution": mentions_frame["resolution"].value_counts().to_dict() if len(mentions_frame) else {},
            "pdf_branch": "deferred: no selected paper required a PDF; Docling not installed",
            "network_requests": client.network_requests,
        }
        write_json(out / "coverage.json", counts)
        failures = {FETCH_FAILED, PARSE_FAILED} & set(papers["processing_status"]) or pubtator_status.startswith(
            "failed"
        )
        status = StageStatus.PARTIAL if failures else StageStatus.SUCCEEDED
        _manifest(
            out,
            "literature_fetch",
            key,
            execution_id,
            started,
            status,
            {"search_key": search_key},
            {"fetch": config.fetch.model_dump(mode="json")},
            counts,
            loaded.repo_root,
            rows,
            # The exact identity hashed into the key (request outcomes with response hashes).
            {"identity": identity},
        )
        return counts, status

    try:
        return _run(loaded, "literature-fetch", "litparsed", identity, build, client, {"search_key": search_key})
    finally:
        client.close()


# ---------------------------------------------------------------------------
# Stage 3: passage retrieval and bundles


def load_documents(parsed_dir: Path) -> dict[str, Document]:
    documents = {}
    for path in sorted((parsed_dir / "documents").glob("*/document.json")):
        payload = read_json(path)
        document = Document(
            payload["publication_id"],
            payload["text_version"],
            payload["source_asset_sha256"],
            [Passage(**p) for p in payload["passages"]],
            payload["supplementary"],
        )
        if document.canonical_text != payload["canonical_text"]:
            raise LiteratureStageError(f"{path}: passages do not reproduce the stored canonical text")
        documents[document.publication_id] = document
    return documents


def run_retrieve(loaded: LoadedProjectConfig, parsed_key: str, literature: Path, process_env=None) -> StageOutcome:
    config = load_literature_config(literature)
    parsed_dir = loaded.data_root / "processed" / parsed_key
    failed = (
        [c for c in artifact_integrity(parsed_dir, "fetch") if not c.passed] if parsed_dir.is_dir() else ["missing"]
    )
    if failed:
        raise LiteratureStageError(f"parsed artifact {parsed_key} is missing or failed integrity: {failed}")
    search_key = read_json(parsed_dir / "manifest.json")["inputs"]["search_key"]
    search_dir = loaded.data_root / "processed" / search_key
    queries_frame = pd.read_parquet(search_dir / "queries.parquet")
    settings = load_model_settings(loaded.repo_root, process_env)
    backend, dense_status, dense_error = None, emb.DENSE_NOT_CONFIGURED, None
    execution = {"ollama_metadata_reads": 0, "embedding_requests": 0}
    if settings.embeddings.status.value == "disabled":
        dense_status = emb.DENSE_DISABLED
    else:
        if settings.embeddings.spec and settings.embeddings.spec.provider == "ollama":
            execution["ollama_metadata_reads"] = 3  # /api/tags, /api/show, /api/version (local, before reuse)
        try:
            backend = emb.build_embeddings(settings, config.embeddings)
            dense_status = emb.DENSE_OK if backend else emb.DENSE_NOT_CONFIGURED
        except emb.EmbeddingSetupError as error:
            dense_status, dense_error = emb.DENSE_FAILED, str(error)
    embedding_identity = {k: v for k, v in (backend.identity if backend else {}).items() if k != "metadata"}
    identity = {
        "stage": "literature_retrieve",
        "schema": SCHEMA_VERSION,
        "parsed_key": parsed_key,
        "retrieval": config.retrieval.model_dump(mode="json"),
        "bundles": config.bundles.model_dump(mode="json"),
        "dense_status": dense_status,
        "embedding": embedding_identity,
        "code": code_fingerprint(Path(regkg.__file__).parent, CODE_PATHS),
    }

    def build(out: Path, key: str, execution_id: str, started: str):
        documents = load_documents(parsed_dir)
        passages = [p for d in documents.values() for p in d.passages]
        owners = [d.publication_id for d in documents.values() for _ in d.passages]
        by_id = {p.passage_id: p for p in passages}
        executed = queries_frame[queries_frame["search_status"] != NOT_SEARCHED]
        queries = []
        for row in executed.itertuples(index=False):
            terms = json.loads(row.terms_json)
            queries.append(
                QueryTerms(
                    row.query_id,
                    int(row.priority),
                    row.tf_hgnc_id,
                    list(terms["tf"]),
                    row.target_hgnc_id,
                    list(terms.get("target") or []),
                    list(terms["qualifiers"]),
                    json.loads(row.candidate_ids),
                )
            )
        bm25 = BM25Okapi(
            [tokenize(p.text) for p in passages] or [[""]], k1=config.retrieval.bm25_k1, b=config.retrieval.bm25_b
        )
        embedding_record: dict[str, Any] = {"dense_status": dense_status, "error": dense_error}
        passage_scores: dict[str, np.ndarray] = {}
        if backend is not None and passages:
            store = emb.VectorStore(loaded.data_root / "external" / "embeddings", backend)
            dimension = (backend.identity.get("metadata") or {}).get("embedding_length")  # None unless declared
            chunks = {p.passage_id: emb.chunk_text(p.text, config.embeddings.max_chunk_chars) for p in passages}
            all_chunks = [c for cs in chunks.values() for c in cs]
            vectors = store.encode(all_chunks, config.embeddings.batch_size, dimension)
            import hashlib

            for query in queries:
                q = store.embed_query(query.text, dimension)
                passage_scores[query.query_id] = np.array(
                    [
                        max(
                            float(np.dot(vectors[hashlib.sha256(c.encode()).hexdigest()], q))
                            for c in chunks[p.passage_id]
                        )
                        for p in passages
                    ]
                )
            execution["embedding_requests"] = store.requests
            embedding_record.update(
                {
                    "selector": backend.selector,
                    "provider": backend.provider,
                    "cache_id": backend.cache_id,
                    "identity": backend.identity,
                    "passages": len(passages),
                    "chunks": len(all_chunks),
                    "passages_split": sum(len(cs) > 1 for cs in chunks.values()),
                    "max_chunk_chars": config.embeddings.max_chunk_chars,
                    "longest_chunk_chars": max((len(c) for c in all_chunks), default=0),
                    "chunk_hash_digest": sha256_text(
                        "".join(sorted(hashlib.sha256(c.encode()).hexdigest() for c in all_chunks))
                    ),
                    "encoding_contract": backend.contract.to_record() if backend.contract else None,
                    "truncation": "prevented: every chunk and query was checked against the encoding contract "
                    "before encoding; oversized inputs are rejected",
                    "largest_input_size": max(store.sizes, default=0),
                    "largest_query_size": max(store.query_sizes, default=0),
                    "size_unit": "chars" if backend.contract.method == "wordpiece_char_bound" else "tokens",
                    "vector_dimension": int(next(iter(vectors.values())).shape[0]) if vectors else None,
                    "embedding_requests_this_build": store.requests,
                    "encoded_inputs_checked": len(store.sizes) + len(store.query_sizes),
                    "passage_score": "max cosine over chunks (vectors are unit-normalized)",
                }
            )
        hits = {
            q.query_id: rank_passages(q, passages, owners, bm25, passage_scores.get(q.query_id), config.retrieval)
            for q in queries
        }
        mention_frame = pd.read_parquet(parsed_dir / "mentions.parquet")
        keep = [
            "mention_id",
            "start",
            "end",
            "text",
            "source",
            "candidate_hgnc_id",
            "hgnc_id",
            "resolution",
            "species_taxon",
            "species_evidence",
            "external_identifier",
            "identity_status",
            "alignment",
        ]
        by_passage = {
            pid: [
                {k: (None if pd.isna(v) else v) if not isinstance(v, list) else v for k, v in row.items()}
                for row in group[keep].to_dict("records")
            ]
            for pid, group in mention_frame.dropna(subset=["passage_id"]).groupby("passage_id")
        }
        bundles, rejected = assemble_bundles(queries, hits, documents, by_id, config.bundles, by_passage)
        hit_rows = [{**asdict(h), "reasons": json.dumps(h.reasons)} for q in queries for h in hits[q.query_id]]
        coverage_rows = []
        for row in queries_frame.itertuples(index=False):
            status = row.search_status
            if status not in {NOT_SEARCHED, SEARCH_FAILED}:
                exact = [h for h in hits.get(row.query_id, []) if h.exact_tf]
                status = (
                    CANDIDATE_PASSAGES_FOUND
                    if exact
                    else (NO_CANDIDATE_PASSAGES if documents else SEARCHED_NO_SUPPORT_FOUND)
                )
            coverage_rows.append(
                {
                    "query_id": row.query_id,
                    "priority": int(row.priority),
                    "tf_symbol": row.tf_symbol,
                    "target_symbol": row.target_symbol,
                    "search_status": row.search_status,
                    "retrieval_status": status,
                    "bundles": sum(b.query_id == row.query_id for b in bundles),
                }
            )
        rows = {
            "retrieval_hits.parquet": _write_parquet(pd.DataFrame(hit_rows), out / "retrieval_hits.parquet"),
            "query_coverage.parquet": _write_parquet(pd.DataFrame(coverage_rows), out / "query_coverage.parquet"),
        }
        _jsonl(out / "bundles.jsonl", [b.to_json() for b in bundles])
        write_json(out / "rejected_bundles.json", rejected)
        write_json(out / "embeddings.json", embedding_record)
        coverage = pd.DataFrame(coverage_rows)
        counts = {
            "documents": len(documents),
            "passages": len(passages),
            "queries_ranked": len(queries),
            "hits": len(hit_rows),
            "bundles": len(bundles),
            "rejected_bundle_candidates": len(rejected),
            "retrieval_status": coverage["retrieval_status"].value_counts().to_dict(),
            "bundles_per_tf": pd.Series([b.retrieval_tf_hgnc_id for b in bundles]).value_counts().to_dict()
            if bundles
            else {},
            "dense_status": dense_status,
            "embedding_requests": embedding_record.get("embedding_requests_this_build", 0),
        }
        write_json(out / "coverage.json", counts)
        status = StageStatus.PARTIAL if dense_status == emb.DENSE_FAILED else StageStatus.SUCCEEDED
        _manifest(
            out,
            "literature_retrieve",
            key,
            execution_id,
            started,
            status,
            {"parsed_key": parsed_key, "search_key": search_key},
            {
                "retrieval": config.retrieval.model_dump(mode="json"),
                "bundles": config.bundles.model_dump(mode="json"),
                "embeddings": embedding_identity,
            },
            counts,
            loaded.repo_root,
            rows,
            # The exact identity hashed into the key (request outcomes with response hashes).
            {"identity": identity},
        )
        return counts, status

    return _run(
        loaded, "literature-retrieve", "litretrieval", identity, build, None, {"parsed_key": parsed_key}, execution
    )
