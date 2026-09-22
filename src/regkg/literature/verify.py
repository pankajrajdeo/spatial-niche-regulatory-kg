"""`regkg verify literature`: the search -> fetch -> retrieval chain, bounds, grounding, and secrets."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pandas as pd

from regkg.config import LiteratureConfig, load_environment
from regkg.literature.parse import CAPTION_PRESENT, TABLE_RULE, TEXT_RULE
from regkg.literature.passages import (
    ALIGN_EXTERNAL_MISMATCH,
    ALIGN_UNALIGNED,
    CONFLICTING,
    CONSISTENT,
    HINT_ONLY,
    NOT_ASSESSED,
    NOT_ATTACHED,
    NOT_ATTACHED_STATUS,
    RESOLVED_HUMAN,
)
from regkg.literature.publications import term_pattern
from regkg.literature.retrieval import BUNDLE_STATUS
from regkg.literature.xml import secure_parser
from regkg.models import CheckResult
from regkg.project_data.verify import Checks
from regkg.provenance import canonical_json, read_json, sha256_file, sha256_text, stable_id
from regkg.workflows import literature as flow

SEARCH_STATUSES = {
    flow.NOT_SEARCHED,
    flow.SEARCHED,
    flow.SEARCHED_NO_SUPPORT_FOUND,
    flow.SEARCHED_PARTIAL,
    flow.SEARCH_FAILED,
}
PAPER_STATUSES = {flow.FULL_TEXT_PROCESSED, flow.ABSTRACT_ONLY, flow.FETCH_FAILED, flow.PARSE_FAILED, flow.NOT_FOUND}
RETRIEVAL_STATUSES = SEARCH_STATUSES | {flow.NO_CANDIDATE_PASSAGES, flow.CANDIDATE_PASSAGES_FOUND}
CREDENTIAL_NAMES = ("NCBI_API_KEY", "NCBI_EMAIL", "OPENROUTER_API_KEY")


def verify_literature(retrieval_dir: Path, repo_root: Path, literature: Path) -> list[CheckResult]:
    checks = Checks()
    processed = retrieval_dir.parent
    results = flow.artifact_integrity(retrieval_dir, "retrieval")
    manifest = read_json(retrieval_dir / "manifest.json") if (retrieval_dir / "manifest.json").is_file() else {}
    parsed_dir = processed / manifest.get("inputs", {}).get("parsed_key", "")
    search_dir = processed / manifest.get("inputs", {}).get("search_key", "")
    results += flow.artifact_integrity(parsed_dir, "fetch") + flow.artifact_integrity(search_dir, "search")
    if not all(r.passed for r in results):
        return results
    search_manifest = read_json(search_dir / "manifest.json")
    candidate_dir = processed / search_manifest["inputs"]["candidate_key"]
    results += [
        CheckResult(name=f"upstream:{r.name}", passed=r.passed, detail=r.detail)
        for r in flow.candidate_integrity_any(candidate_dir)
    ]
    config = LiteratureConfig.model_validate(
        {**read_json_yaml(literature), "search": search_manifest["config"]["search"]}
    )
    max_papers = search_manifest["config"]["max_papers"]

    queries = pd.read_parquet(search_dir / "queries.parquet")
    publications = pd.read_parquet(search_dir / "publications.parquet")
    selection = pd.read_parquet(search_dir / "selection.parquet")
    papers = pd.read_parquet(parsed_dir / "papers.parquet")
    passages = pd.read_parquet(parsed_dir / "passages.parquet")
    mentions = pd.read_parquet(parsed_dir / "mentions.parquet")
    hits = pd.read_parquet(retrieval_dir / "retrieval_hits.parquet")
    coverage = pd.read_parquet(retrieval_dir / "query_coverage.parquet")
    bundles = [json.loads(line) for line in (retrieval_dir / "bundles.jsonl").read_text().splitlines() if line]
    queue = pd.read_parquet(candidate_dir / "retrieval_queue.parquet")

    def query_bounds():
        executed = queries[queries["search_status"] != flow.NOT_SEARCHED]
        ok = (
            len(executed) <= config.search.max_queries
            and set(queries["search_status"]) <= SEARCH_STATUSES
            and len(queries) == len(queue)
            and (queries["retained_publications"] <= config.search.max_results_per_query).all()
            and set(executed["query_id"]) <= set(queue.loc[queue["in_initial_live_slice"], "query_id"])
        )
        return ok, (
            f"{len(executed)} executed (<= {config.search.max_queries}) of {len(queue)} queued; "
            f"remaining {int((queries['search_status'] == flow.NOT_SEARCHED).sum())} NOT_SEARCHED; "
            f"<= {config.search.max_results_per_query} retained per query; "
            f"statuses {sorted(set(queries['search_status']))}"
        )

    checks.run("search:query_bounds_and_status", query_bounds)

    def identity():
        unique = publications["publication_id"].is_unique
        collisions = []
        for kind in ("pmid", "pmcid", "doi"):
            values = publications[kind].dropna()
            collisions += values[values.duplicated()].tolist()
        selected = selection[selection["selected"]]
        ok = unique and not collisions and len(selected) <= max_papers and selected["publication_id"].is_unique
        ok &= papers["publication_id"].tolist() == selected.sort_values("selection_order")["publication_id"].tolist()
        return ok, (
            f"{len(publications)} unique publications; identifiers shared by two publications: {collisions[:5]}; "
            f"{len(selected)} selected (<= {max_papers}); each fetched once, in selection order"
        )

    checks.run("search:publication_identity", identity)

    def assets_and_documents():
        problems = []
        if not set(papers["processing_status"]) <= PAPER_STATUSES:
            problems.append("unknown processing status")
        for row in papers.itertuples(index=False):
            for asset in json.loads(row.assets):
                path = repo_root / asset["path"]
                if not path.is_file() or sha256_file(path) != asset["sha256"]:
                    problems.append(f"asset changed: {asset['path']}")
        for path in sorted((parsed_dir / "documents").glob("*/document.json")):
            document = read_json(path)
            text = document["canonical_text"]
            if hashlib.sha256(text.encode()).hexdigest() != document["canonical_sha256"]:
                problems.append(f"canonical hash mismatch {path.parent.name}")
            for p in document["passages"]:
                if text[p["start"] : p["end"]] != p["text"] or not p["locator"]:
                    problems.append(f"passage offset/locator mismatch {p['passage_id']}")
        ok = not problems and passages["passage_id"].is_unique
        return ok, (
            f"{len(papers)} papers {papers['processing_status'].value_counts().to_dict()}; raw asset checksums, "
            f"canonical hashes, and all {len(passages)} passage offsets/locators verified; problems {problems[:3]}"
        )

    checks.run("fetch:assets_documents_offsets", assets_and_documents)

    def mention_alignment():
        documents = {
            p.name: read_json(p / "document.json")["canonical_text"] for p in (parsed_dir / "documents").iterdir()
        }
        bad = mention_alignment_problems(mentions, documents)
        quarantined = int((mentions["alignment"] == ALIGN_EXTERNAL_MISMATCH).sum())
        return not bad, (
            f"{len(mentions)} mentions: aligned spans equal canonical text; unaligned keep external offsets "
            f"only; {quarantined} external-offset mismatches quarantined (raw provenance, no canonical "
            f"grounding or identity); HGNC IDs only on resolved mentions; bad {bad[:3]}"
        )

    checks.run("fetch:mention_alignment", mention_alignment)

    def retrieval_and_bundles():
        known = set(passages["passage_id"])
        text_of = dict(zip(passages["passage_id"], passages["text"], strict=True))
        owner = dict(zip(passages["passage_id"], passages["publication_id"], strict=True))
        problems = [] if set(hits["passage_id"]) <= known else ["hit references unknown passage"]
        if not set(coverage["retrieval_status"]) <= RETRIEVAL_STATUSES:
            problems.append("unknown retrieval status")
        per_paper, per_tf = {}, {}
        terms = {q.query_id: json.loads(q.terms_json) for q in queries.itertuples(index=False)}
        for bundle in bundles:
            ids = [p["passage_id"] for p in bundle["passages"]]
            if (
                len(ids) > config.bundles.max_passages
                or bundle["total_chars"] > config.bundles.max_chars
                or bundle["status"] != BUNDLE_STATUS
            ):
                problems.append(f"bundle bound/status {bundle['bundle_id']}")
            if any(
                owner.get(i) != bundle["publication_id"] or text_of.get(i) != p["text"]
                for i, p in zip(ids, bundle["passages"], strict=True)
            ):
                problems.append(f"bundle passage not from its publication {bundle['bundle_id']}")
            anchor = text_of[bundle["anchor_passage_id"]]
            if not any(term_pattern(t).search(anchor) for t in terms[bundle["query_id"]]["tf"]):
                problems.append(f"anchor lacks exact TF mention {bundle['bundle_id']}")
            per_paper[bundle["publication_id"]] = per_paper.get(bundle["publication_id"], 0) + 1
            per_tf[bundle["retrieval_tf_hgnc_id"]] = per_tf.get(bundle["retrieval_tf_hgnc_id"], 0) + 1
        if (
            len(bundles) > config.bundles.max_bundles
            or max(per_paper.values(), default=0) > config.bundles.max_per_paper
            or max(per_tf.values(), default=0) > config.bundles.max_per_candidate_tf
        ):
            problems.append("run-level bundle limits exceeded")
        return not problems, (
            f"{len(hits)} hits; {len(bundles)} bundles (<= {config.bundles.max_bundles}), each "
            f"<= {config.bundles.max_passages} whole passages and <= {config.bundles.max_chars} chars, "
            f"one publication, exact-TF anchor, status {BUNDLE_STATUS}; problems {problems[:3]}"
        )

    checks.run("retrieval:hits_and_bundles", retrieval_and_bundles)

    def stage_identity():
        problems = []
        for directory, prefix in (
            (search_dir, "litsearch"),
            (parsed_dir, "litparsed"),
            (retrieval_dir, "litretrieval"),
        ):
            stored = read_json(directory / "manifest.json")
            identity = stored.get("identity")
            if identity is None or directory.name != f"{prefix}-{sha256_text(canonical_json(identity))[:16]}":
                problems.append(f"{directory.name}: key does not equal hash of stored identity")
        search_identity = {tuple(x) for x in read_json(search_dir / "manifest.json")["identity"]["requests"]}
        requests = pd.read_parquet(search_dir / "source_requests.parquet")
        for row in requests[requests["outcome"].isin(["fetched", "cached"])].itertuples(index=False):
            if not row.sha256 or (row.cache_key, "ok", row.sha256) not in search_identity:
                problems.append(f"search response {row.cache_key[:12]} hash missing from identity")
        fetch_identity = read_json(parsed_dir / "manifest.json")["identity"]
        assets = sorted(a["sha256"] for r in papers.itertuples(index=False) for a in json.loads(r.assets))
        if fetch_identity.get("assets") != assets:
            problems.append("fetch identity does not list the stored asset hashes")
        # Rules come from each stored document (older artifacts lack parser-specific rules).
        rules = {}
        for path in (parsed_dir / "documents").glob("*/document.json"):
            payload = read_json(path)
            rules[payload["publication_id"]] = (
                payload.get("text_rule", TEXT_RULE),
                payload.get("table_rule", TABLE_RULE),
                payload.get("extra_rules") or {},
            )
        for row in passages.itertuples(index=False):
            text_rule, table_rule, extra = rules[row.publication_id]
            expected = stable_id(
                "passage",
                {
                    "asset_sha256": row.asset_sha256,
                    "locator": row.locator,
                    "kind": row.kind,
                    "text_rule": text_rule,
                    "table_rule": table_rule,
                    "text_sha256": hashlib.sha256(row.text.encode("utf-8")).hexdigest(),
                    **extra,
                },
            )
            if expected != row.passage_id:
                problems.append(f"passage id not content-qualified {row.passage_id}")
                break
        return not problems, (
            f"3 stage keys equal the hash of their stored identities; "
            f"{int(requests['outcome'].isin(['fetched', 'cached']).sum())} successful responses and "
            f"{len(assets)} assets identified by SHA-256; passage IDs include text rule "
            f"{TEXT_RULE}, table rule {TABLE_RULE}, and text hash; problems {problems[:3]}"
        )

    checks.run("provenance:content_identity", stage_identity)

    def mention_identity():
        from regkg.workflows.literature import _human_gene_map

        human = _human_gene_map(candidate_dir, repo_root)
        problems = []
        names = mentions[mentions["source"] == "exact_candidate_name"]
        source = mentions[mentions["source"] == "pubtator"]
        if names["hgnc_id"].notna().any() or names["species_taxon"].notna().any():
            problems.append("candidate-name hit carries a resolved identity or species")
        resolved = source[source["hgnc_id"].notna()]
        for row in resolved.itertuples(index=False):
            if (
                row.resolution != RESOLVED_HUMAN
                or human.get(str(row.external_identifier)) != row.hgnc_id
                or row.species_taxon != "9606"
            ):
                problems.append(f"PubTator identity not from a unique human NCBI Gene ID: {row.mention_id}")
        mismatched = source[source["alignment"] == ALIGN_EXTERNAL_MISMATCH]
        if mismatched["start"].notna().any() or mismatched["hgnc_id"].notna().any():
            problems.append("identifier attached despite external offset/text mismatch")
        attached = source[source["start"].notna()]
        conflicts = consistent = 0
        for row in names.itertuples(index=False):
            same = attached[
                (attached["passage_id"] == row.passage_id)
                & (attached["start"] < row.end)
                & (attached["end"] > row.start)
            ]
            if same.empty:
                expected = HINT_ONLY
            elif ((same["resolution"] == RESOLVED_HUMAN) & (same["hgnc_id"] == row.candidate_hgnc_id)).all():
                expected = CONSISTENT
            else:
                expected = CONFLICTING
            if expected != row.identity_status or sorted(same["mention_id"]) != sorted(row.linked_mention_ids):
                problems.append(f"reconciliation mismatch {row.mention_id}")
            conflicts += expected == CONFLICTING
            consistent += expected == CONSISTENT
        return not problems, (
            f"{len(names)} candidate-name hits carry hints only ({consistent} consistent with a "
            f"human source identifier, {conflicts} conflicting, rest hint-only); {len(resolved)} "
            f"PubTator identities via unique human NCBI Gene IDs; {len(mismatched)} external "
            f"offset mismatches attached nothing; problems {problems[:3]}"
        )

    checks.run("mentions:identity_separation_and_conflicts", mention_identity)

    def table_structure_and_readiness():
        from lxml import etree

        from regkg.literature.parse import caption_status, element_text, row_cells, table_id, table_structure

        problems = []
        tables = passages[passages["kind"].str.startswith("table_")]
        assets_by_pub = {
            r.publication_id: {a["sha256"]: a for a in json.loads(r.assets)} for r in papers.itertuples(index=False)
        }
        checked = 0
        for row in tables[tables["text_version"] == "europepmc_jats"].itertuples(index=False):
            asset = assets_by_pub[row.publication_id][row.asset_sha256]
            root = etree.fromstring((repo_root / asset["path"]).read_bytes(), parser=secure_parser())
            element = root.getroottree().xpath(row.locator)[0]
            wrap = element if element.tag == "table-wrap" else next(element.iterancestors("table-wrap"))
            structure, headers, grid = table_structure(wrap)
            expected_status = caption_status(element_text(wrap.find("label")), element_text(wrap.find("caption")))
            if row.table_id != table_id(row.asset_sha256, root.getroottree().getpath(wrap)) or (
                row.table_caption_status != expected_status
            ):
                problems.append(f"table identity/caption status mismatch {row.passage_id}")
            if row.kind != "table_caption" and structure != row.table_structure:
                problems.append(f"table structure mismatch {row.passage_id}")
            if row.kind == "table_row":
                header_rows = [r for h in wrap.iter("thead") for r in h.iter("tr")]
                body = [r for r in wrap.iter("tr") if r not in header_rows]
                expected = row_cells(body, grid, body.index(element), headers) if grid is not None else None
                stored = None if row.cells is None else [dict(c) for c in row.cells]
                if expected != stored:
                    problems.append(f"table cells/header association mismatch {row.passage_id}")
            checked += 1
        if (
            tables[tables["text_version"] == "pubtator_bioc"]["table_structure"] != "flattened_bioc_no_cell_structure"
        ).any():
            problems.append("flattened BioC table not flagged")
        if tables["table_id"].isna().any():
            problems.append("table passage without internal table identity")
        false_ready = readiness_problems(bundles, passages)
        if false_ready:
            problems.append(f"{false_ready} bundles claim completeness they lack")
        ready = sum(b["extraction_ready"] for b in bundles)
        return not problems, (
            f"{checked} JATS table passages re-derived from raw XML (table identity, caption status, "
            f"structure, cells, headers); {tables['table_id'].nunique()} tables, "
            f"caption status {tables.drop_duplicates('table_id')['table_caption_status'].value_counts().to_dict()}; "
            f"BioC tables flagged flattened; {ready}/{len(bundles)} bundles extraction-ready, "
            f"none falsely complete; problems {problems[:3]}"
        )

    checks.run("tables:structure_and_bundle_readiness", table_structure_and_readiness)

    def embeddings():
        record = read_json(retrieval_dir / "embeddings.json")
        ok, detail = embedding_contract_check(record)
        if ok and record["dense_status"] == "ok":
            store = processed.parent / "external" / "embeddings" / record["cache_id"]
            ok = any(store.glob("vectors-*.parquet"))
            detail += "; cached vectors present" if ok else "; cached vectors missing"
        return ok, detail

    checks.run("retrieval:embeddings", embeddings)

    def no_credentials():
        env = load_environment(repo_root / ".env")
        secrets = [env[name].encode() for name in CREDENTIAL_NAMES if env.get(name) and len(env[name]) >= 6]
        leaked = []
        for directory in (search_dir, parsed_dir, retrieval_dir):
            for path in directory.rglob("*"):
                if path.is_file() and any(secret in path.read_bytes() for secret in secrets):
                    leaked.append(path.relative_to(processed).as_posix())
        requests = pd.read_parquet(search_dir / "source_requests.parquet")
        params_ok = not requests["params"].str.contains('"api_key"|"email"').any()
        return not leaked and params_ok, (
            f"{len(secrets)} configured credential/contact values absent from all stage "
            f"artifacts; recorded request params carry no api_key/email; leaked {leaked[:3]}"
        )

    checks.run("security:no_credentials_in_artifacts", no_credentials)
    return results + checks.results


def read_json_yaml(path: Path) -> dict:
    from regkg.config import read_yaml

    return read_yaml(path)


def readiness_problems(bundles: list[dict], passages: pd.DataFrame) -> int:
    """Bundles claiming extraction readiness that their table structure or included context does not support."""
    by_id = passages.set_index("passage_id")
    false_ready = 0
    for bundle in bundles:
        anchor = by_id.loc[bundle["anchor_passage_id"]]
        included = {p["passage_id"] for p in bundle["passages"]}
        required: set[str] = set()
        if anchor["kind"] in {"table_row", "table_footnote"}:
            # Required context is derived from the parsed table identity, not from what the bundle lists.
            if pd.isna(anchor["table_id"]) or anchor["table_caption_status"] != CAPTION_PRESENT:
                false_ready += bool(bundle["extraction_ready"])
            same = passages[
                (passages["publication_id"] == bundle["publication_id"]) & (passages["table_id"] == anchor["table_id"])
            ]
            required = set(same[same["kind"].isin(["table_caption", "table_footnote"])]["passage_id"]) - {
                bundle["anchor_passage_id"]
            }
            if anchor["table_structure"] != "header_grid_expanded" and bundle["extraction_ready"]:
                false_ready += 1
        if bundle["extraction_ready"] and (bundle["incomplete_reasons"] or not required <= included):
            false_ready += 1
        if bundle["extraction_ready"] != (not bundle["incomplete_reasons"]):
            false_ready += 1
    return false_ready


def mention_alignment_problems(mentions: pd.DataFrame, canonical_text: dict[str, str]) -> list[str]:
    """Mention IDs violating the grounding invariants of their alignment state.

    Attached mentions must equal canonical text. Two unattached states are valid: a text-version
    difference (external offsets kept) and a quarantined external-offset mismatch (raw annotation
    provenance kept; no canonical passage/span, resolved identity, or species).
    """
    bad = []
    for row in mentions.itertuples(index=False):
        key = row.publication_id.replace(":", "_")
        if row.alignment == ALIGN_EXTERNAL_MISMATCH:
            ok = (
                pd.isna(row.start)
                and pd.isna(row.end)
                and pd.isna(row.passage_id)
                and pd.isna(row.hgnc_id)
                and pd.isna(row.species_taxon)
                and row.species_evidence == NOT_ASSESSED
                and row.resolution == NOT_ATTACHED
                and row.identity_status == NOT_ATTACHED_STATUS
                and row.source == "pubtator"
                and pd.notna(row.external_offset)
                and pd.notna(row.external_length)
            )
        elif pd.notna(row.start):
            ok = pd.notna(row.passage_id) and canonical_text[key][int(row.start) : int(row.end)] == row.text
        else:
            ok = row.alignment == ALIGN_UNALIGNED and pd.notna(row.external_offset) and pd.isna(row.passage_id)
        if pd.notna(row.hgnc_id) and not str(row.resolution).startswith("resolved"):
            ok = False
        if not ok:
            bad.append(row.mention_id)
    return bad


def embedding_contract_check(record: dict) -> tuple[bool, str]:
    """Backend-aware: validates the recorded encoding contract of whichever backend ran."""
    if record["dense_status"] != "ok":
        return True, f"dense retrieval {record['dense_status']}; lexical retrieval only ({record.get('error')})"
    contract = record.get("encoding_contract")
    if not contract:
        return False, "no recorded encoding contract"
    if contract["method"] == "wordpiece_char_bound":
        bound_ok = (
            contract["max_input_chars"] <= contract["context_tokens"] - contract["special_tokens"]
            and record["largest_input_size"] <= contract["max_input_chars"]
            and record["largest_query_size"] <= contract["max_input_chars"]
        )
        limit = f"<= {contract['max_input_chars']} chars ({contract['context_tokens']}-token WordPiece context)"
    elif contract["method"] == "tokenizer_token_count":
        bound_ok = (
            record["largest_input_size"] <= contract["max_input_tokens"]
            and record["largest_query_size"] <= contract["max_input_tokens"]
        )
        limit = f"<= {contract['max_input_tokens']} tokens (model tokenizer)"
    else:
        return False, f"unknown contract method {contract['method']}"
    declared = (record.get("identity", {}).get("metadata") or {}).get("embedding_length")
    dimension_ok = bool(record.get("vector_dimension")) and (declared is None or declared == record["vector_dimension"])
    return bound_ok and dimension_ok, (
        f"{record['selector']} ({contract['backend']}, {contract['method']}): largest chunk "
        f"{record['largest_input_size']} and largest query {record['largest_query_size']} {record['size_unit']} "
        f"{limit}; {record.get('vector_dimension')}-d vectors"
    )
