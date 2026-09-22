"""P3 scope closure: the audited validation selection and a disposition for every frontier item.

The curated audit/selection file (configs/p3_scope_closure.yaml) is lead-reviewable input: each quoted
span must occur verbatim in the named bundle's own parts, so no expectation can be stated about context
the bundle does not contain. Dispositions are derived from the published ledgers by fixed rules; nothing
here re-runs corpus preparation or changes the immutable artifact.
"""

from __future__ import annotations

import html
import json
from pathlib import Path

import pandas as pd
import yaml

from regkg.config import LoadedProjectConfig
from regkg.provenance import canonical_json, sha256_file, sha256_text, utc_now
from regkg.workflows import corpus as c
from regkg.workflows import corpus_ready as r

CLOSURE_RULE = "p3-scope-closure-3"  # 3: obligations generated from the stored records, per source

REQUIRED = "required_acquisition_or_parse_repair_before_extraction"
INVESTIGATION = "permitted_p4_local_context_investigation"
EXTRACTION = "extraction_verification_with_preserved_uncertainty"
BACKGROUND = "background_irrelevant_or_duplicate"
UNRESOLVED = "unresolved_relevance_or_attribution_needs_review"
RESOLVED = "resolved_in_this_artifact_no_further_action"

CLOSED_LABELS = {"biological_background_resource", "irrelevant_to_assigned_question"}
# Rows of different kinds are not comparable work units, and blocked bundles and their investigations
# describe the same work, so totals are reported per unit group and never summed into a workload figure.
UNIT_GROUPS = {
    "bundle": "evidence_bundles",
    "context_investigation": "investigations_linked_to_blocked_bundles",
    "table_region_interpretation": "table_regions_pending_interpretation",
    "deferred_discovery_paper": "papers_pending_relevance_review",
    "download": "acquisition_or_identification_requests",
    "audit": "tasks_established_by_the_scope_closure_audit",
}
DIMENSIONS = ("species", "cell", "attribution", "assay")


class ClosureError(Exception):
    pass


def load_closure(path: Path) -> dict:
    document = yaml.safe_load(path.read_text(encoding="utf-8"))
    for key in ("rule", "corpus_key", "audit", "selection"):
        if key not in document:
            raise ClosureError(f"{path} lacks {key!r}")
    return document


def _part_text(payload: dict) -> str:
    return "\n".join(part["text"] for part in payload["parts"])


def check_spans(document: dict, payloads: dict[str, dict]) -> list[dict]:
    """Every audited dimension span must be an exact substring of that bundle's parts."""
    problems = []
    for record in document["audit"]:
        payload = payloads.get(record["payload_id"])
        if payload is None:
            problems.append({"payload_id": record["payload_id"], "problem": "bundle_not_in_artifact"})
            continue
        text = _part_text(payload)
        for dimension in DIMENSIONS:
            value = record.get(dimension)
            if value == "unknown" or value is None:
                continue
            if not isinstance(value, list) or len(value) != 2:
                problems.append({"payload_id": record["payload_id"], "problem": f"{dimension}_not_[value, span]"})
                continue
            if value[1] not in text:
                problems.append(
                    {
                        "payload_id": record["payload_id"],
                        "problem": f"{dimension}_span_not_in_bundle_parts",
                        "span": value[1][:120],
                    }
                )
    known = {x["payload_id"] for x in document["audit"]}
    for item in document["selection"]:
        if item["payload_id"] not in known:
            problems.append({"payload_id": item["payload_id"], "problem": "selected_bundle_not_audited"})
        payload = payloads.get(item["payload_id"])
        if payload is None:
            continue
        pairs = {(a["cell_type"], a["tf_hgnc_id"]) for a in payload["associations"]}
        for lineage, tf in item["associations"]:
            if (lineage, tf) not in pairs:
                problems.append({"payload_id": item["payload_id"], "problem": f"association_absent:{lineage}/{tf}"})
    return problems


def selection_manifest(document: dict, payloads: dict[str, dict], inputs: dict) -> dict:
    """A batch manifest whose items carry the selected associations, purpose and expected behavior."""
    chosen = [item["payload_id"] for item in document["selection"]]
    manifest = r.batch_manifest({"batch_index": 0, "payload_ids": chosen}, payloads, inputs)
    by_id = {item["payload_id"]: item for item in document["selection"]}
    audit = {record["payload_id"]: record for record in document["audit"]}
    for entry in manifest["items"]:
        item, record = by_id[entry["payload_id"]], audit[entry["payload_id"]]
        payload = payloads[entry["payload_id"]]
        entry["validation"] = {
            "purpose": item["purpose"],
            "control": item.get("control"),
            "coverage": item["coverage"],
            "selected_associations": [
                {
                    "cell_type": lineage,
                    "tf_hgnc_id": tf,
                    # per-TF identity is carried, including co-mentioned TFs that stay unresolved
                    "tf_identity": payload["tf_identity"]["per_tf"][tf],
                }
                for lineage, tf in item["associations"]
            ],
            "co_mentioned_tf_identity": {
                tf: value
                for tf, value in payload["tf_identity"]["per_tf"].items()
                if tf not in {t for _, t in item["associations"]}
            },
            "expected": {
                "may_extract": item.get("may_extract", []),
                "must_remain_unknown": item.get("must_remain_unknown", []),
                "must_reject": item.get("must_reject", []),
            },
            "source_dimensions": {d: record.get(d) for d in DIMENSIONS},
            "readiness_state": payload["readiness_state"],
            "readiness_reasons": payload["readiness_reasons"],
        }
    body = {k: v for k, v in manifest.items() if k != "manifest_sha256"}
    body["status"] = "proposed_validation_selection_pending_lead_review"
    body["rule"] = CLOSURE_RULE
    return {**body, "manifest_sha256": sha256_text(canonical_json(body))}


def _bundle_disposition(row: pd.Series, payload: dict | None, investigating: set[str]) -> tuple[str, str]:
    raw = row["reasons"]
    reasons = json.loads(raw) if isinstance(raw, str) else (list(raw) if isinstance(raw, (list, tuple)) else [])
    state = row["state"]
    if state == "READY_FULL_TEXT":
        labels = set()
        for association in (payload or {}).get("associations", []):
            labels |= {association["relevance"], association["passage_relevance"]}
        attributions = (payload or {}).get("attributions", [])
        kind = "source_result" if "source_result_candidate" in attributions else "abstract_or_supporting_text"
        if labels and labels <= CLOSED_LABELS:
            # A provisional screening label is not a reviewed scientific exclusion, so the item stays open.
            return UNRESOLVED, "provisional_background_or_irrelevant_label_needs_relevance_review"
        return EXTRACTION, f"source_ready:{kind}"
    if state in {"NEEDS_ASSET", "NEEDS_PARSE_REPAIR"}:
        return REQUIRED, reasons[0] if reasons else state.lower()
    if state == "NEEDS_CONTEXT":
        if row["id"] in investigating:
            return INVESTIGATION, "queued_local_context_investigation"
        if any(x.startswith(("required_supplement", "cross_asset")) for x in reasons):
            return REQUIRED, reasons[0]
        return UNRESOLVED, reasons[0] if reasons else "context_incomplete"
    return UNRESOLVED, reasons[0] if reasons else state.lower()


def dispositions(artifact: Path, named: dict[str, set[str]]) -> pd.DataFrame:
    """One disposition per frontier item, with the reason, whether it stays open, and whether it touches a
    named manuscript regulator (which orders the work; it does not close anything)."""
    frontier = pd.read_parquet(artifact / "remaining_work.parquet")
    payloads = {}
    for line in (artifact / "bundles_all.jsonl").read_text(encoding="utf-8").splitlines():
        if line:
            payload = json.loads(line)
            payloads[payload["payload_id"]] = payload
    queue = [json.loads(x) for x in (artifact / "context_investigations.jsonl").read_text().splitlines() if x]
    investigating = {b for item in queue for b in item["bundle_ids"]}
    investigation_of: dict[str, list[str]] = {}
    for item in queue:
        for bundle in item["bundle_ids"]:
            investigation_of.setdefault(bundle, []).append(item["investigation_id"])
    downloads = pd.read_csv(artifact / "manual_downloads.csv")
    navigation = pd.read_csv(artifact / "source_navigation_tasks.csv")
    navigating = set(navigation["payload_id"].dropna()) | set(navigation["task_id"])
    ledger = pd.read_parquet(artifact / "screening_ledger.parquet")
    table_tf = dict(zip(ledger["item_id"], ledger["tf_hgnc_id"], strict=True))
    discovery = pd.read_parquet(artifact / "discovery_coverage.parquet")
    deferred_tfs = {
        row.publication_id: {t for entry in json.loads(row.lineage_associations).values() for t in entry["tfs_named"]}
        for row in discovery.itertuples(index=False)
    }
    download_rows = downloads.set_index("request_id")
    rows = []
    for row in frontier.itertuples(index=False):
        item = row._asdict()
        kind, identifier = item["kind"], item["id"]
        raw = item["lineages"]
        lineages = json.loads(raw) if isinstance(raw, str) else (list(raw) if isinstance(raw, (list, tuple)) else [])
        tfs: set[str] = set()
        linked = ""
        if kind == "bundle":
            linked = json.dumps(investigation_of.get(identifier, []))
            payload = payloads.get(identifier)
            disposition, reason = _bundle_disposition(pd.Series(item), payload, investigating)
            tfs = set((payload or {}).get("tf_hgnc_ids", []))
        elif kind == "context_investigation":
            disposition, reason = INVESTIGATION, "queued_local_context_investigation"
            linked = json.dumps(_queue_bundles(queue, identifier))
            tfs = {
                t
                for b in (payloads.get(b, {}) for b in _queue_bundles(queue, identifier))
                for t in b.get("tf_hgnc_ids", [])
            }
        elif kind == "table_region_interpretation":
            disposition, reason = REQUIRED, "table_meaning_interpretation_required"
            tfs = {table_tf.get(identifier)} - {None}
        elif kind == "deferred_discovery_paper":
            disposition, reason = UNRESOLVED, item["state"] or "deferred_discovery"
            tfs = deferred_tfs.get(identifier, set())
        elif kind.startswith("download:"):
            group = kind.split(":", 1)[1]
            record = download_rows.loc[identifier] if identifier in download_rows.index else None
            affected = (
                json.loads(record["affected_bundles"])
                if record is not None and isinstance(record["affected_bundles"], str)
                else []
            )
            tfs = {t for b in affected for t in payloads.get(b, {}).get("tf_hgnc_ids", [])}
            linked = json.dumps(affected)
            if group == "article_lower_priority_background":
                disposition, reason = (
                    BACKGROUND,
                    "not_requested_as_an_acquisition_action_scientific_relevance_not_assessed",
                )
            elif group == "article_potentially_useful_awaiting_relevance_review":
                disposition, reason = UNRESOLVED, "relevance_review_before_any_request"
            elif group == "unidentified_reference":
                if identifier in navigating or any(b in navigating for b in affected):
                    disposition, reason = INVESTIGATION, "local_candidate_exists_navigate_before_requesting"
                else:
                    disposition, reason = REQUIRED, "reference_must_be_identified_then_acquired"
            else:
                disposition, reason = REQUIRED, group
        else:
            raise ClosureError(f"unhandled frontier kind {kind!r}")
        critical = any(tfs & named.get(lineage, set()) for lineage in lineages) if lineages else False
        rows.append(
            {
                "id": identifier,
                "kind": kind,
                "unit_group": UNIT_GROUPS.get(kind.split(":", 1)[0], "other"),
                "linked_to": linked,
                "pmid": item["pmid"],
                "state": item["state"],
                "lineages": json.dumps(lineages),
                "tf_hgnc_ids": json.dumps(sorted(t for t in tfs if t)),
                "disposition": disposition,
                "reason": reason,
                "blocks_its_own_extraction": disposition in {REQUIRED, INVESTIGATION},
                "open": disposition != BACKGROUND,
                "closes": "acquisition_action_only" if disposition == BACKGROUND else "nothing",
                "scientific_relevance": "reviewed" if disposition == EXTRACTION else "provisional_not_reviewed",
                "disposition_status": "proposed_pending_lead_approval",
                "names_manuscript_regulator": critical,
            }
        )
    return pd.DataFrame(rows)


def _queue_bundles(queue: list[dict], investigation_id: str) -> list[str]:
    for item in queue:
        if item["investigation_id"] == investigation_id:
            return item["bundle_ids"]
    return []


def _paper_questions(artifact: Path) -> dict[str, tuple[list[str], list[str]]]:
    """Per PMID, the lineages and named regulators its title/abstract associated it with. A request for a
    paper with no bundle yet still names the manuscript questions it would answer."""
    questions: dict[str, tuple[list[str], list[str]]] = {}
    for name in ("discovery_coverage.parquet", "advisor_coverage.parquet"):
        path = artifact / name
        if not path.is_file():
            continue
        frame = pd.read_parquet(path)
        if "lineage_associations" not in frame.columns:
            continue
        for row in frame.itertuples(index=False):
            if not isinstance(row.pmid, str):
                continue
            associations = json.loads(row.lineage_associations)
            questions[row.pmid] = (
                sorted(associations),
                sorted({t for entry in associations.values() for t in entry.get("tfs_named", [])}),
            )
    return questions


def audit_tasks(artifact: Path, frontier: pd.DataFrame, semantics: dict | None) -> pd.DataFrame:
    """The three tasks this audit established, reconciled against what the artifact now contains.

    Each is one task row linked to the work units it covers; the linked units keep their own rows, so
    nothing is counted twice.
    """
    registry = json.loads((artifact / "needed_supplement_registry.json").read_text())
    zipped = next(
        (f for f in registry["files"] if f["filename"] == "EMS210609-supplement-Supplemental_information.zip"), None
    )
    parse = pd.read_parquet(artifact / "parse_inventory.parquet")
    adams = parse[(parse["pmid"] == "32832599") & (parse["name"].astype(str).str.startswith("aba1983_Data_"))]
    scanned = [
        json.loads(x)["scan_complete"] if isinstance(x, str) else bool((x or {}).get("scan_complete"))
        for x in adams.get("components", pd.Series(dtype=object)).dropna()
    ]
    regions = frontier[frontier["kind"] == "table_region_interpretation"]
    tables = regions[regions["pmid"] == "32832598"]
    unresolved_semantics = [x["field"] for x in (semantics or {}).get("unresolved", []) if x.get("status") == "unknown"]
    rows = [
        {
            "id": "audit:41075787-supplement-zip",
            "task": "automated supplement acquisition under the named size allowance",
            "disposition": RESOLVED if (zipped and zipped.get("registered")) else REQUIRED,
            "reason": f"supplement state {zipped['state'] if zipped else 'not_in_registry'}",
            "linked_to": json.dumps([zipped["sha256"]] if zipped and zipped.get("sha256") else []),
            "counts_as": "task_not_a_work_unit",
            "user_action_required": False,
        },
        {
            "id": "audit:32832599-table-row-limit",
            "task": "local parse repair: stream the Adams tables through their full row range",
            "disposition": RESOLVED if scanned and all(scanned) else REQUIRED,
            "reason": f"{sum(bool(x) for x in scanned)} of {len(scanned)} Adams table parses scanned completely",
            "linked_to": json.dumps(sorted(adams["document_id"].dropna().astype(str))[:20]),
            "counts_as": "task_not_a_work_unit",
            "user_action_required": False,
        },
        {
            "id": "audit:32832598-table-meaning",
            "task": "table-meaning interpretation for PMID 32832598 only (not a parse repair or acquisition)",
            "disposition": REQUIRED if unresolved_semantics else RESOLVED,
            "reason": (
                f"unresolved fields: {', '.join(unresolved_semantics) or 'none'}; covers "
                f"{len(tables)} of {len(regions)} table regions, the rest belong to other publications"
            ),
            "linked_to": json.dumps(sorted(tables["id"])[:20]),
            "covers_regions": int(len(tables)),
            "counts_as": "task_not_a_work_unit",
            "user_action_required": False,
        },
    ]
    for row in rows:
        row.setdefault("covers_regions", 0)  # only the interpretation task covers regions
        row.update(
            kind="audit_task",
            unit_group=UNIT_GROUPS["audit"],
            pmid=row["id"].split(":")[1].split("-")[0],
            state="",
            lineages="[]",
            tf_hgnc_ids="[]",
            blocks_its_own_extraction=row["disposition"] == REQUIRED,
            open=row["disposition"] != RESOLVED,
            closes="task_completed" if row["disposition"] == RESOLVED else "nothing",
            scientific_relevance="not_applicable",
            disposition_status="proposed_pending_lead_approval",
            names_manuscript_regulator=False,
        )
    return pd.DataFrame(rows)


def carry_forward(document: dict, payloads: dict[str, dict], previous: Path | None) -> tuple[dict, list[dict]]:
    """Re-find audited bundles in a refreshed artifact by source provenance (PMID and anchor locator).

    A repaired source can change a bundle's identifier; the validation case follows the source, and a
    formerly blocked item that is now ready is reported as repaired, not as still blocked.
    """
    if previous is None or not previous.is_file():
        return document, []
    old = {}
    for line in previous.read_text(encoding="utf-8").splitlines():
        if line:
            payload = json.loads(line)
            old[payload["payload_id"]] = payload
    anchors = {}
    for payload in payloads.values():
        anchor = next(p for p in payload["parts"] if p["passage_id"] == payload["anchor_passage_id"])
        anchors[(payload["pmid"], anchor["locator"])] = payload
    moved = []
    for section in ("audit", "selection"):
        for entry in document[section]:
            if entry["payload_id"] in payloads:
                continue
            source = old.get(entry["payload_id"])
            if source is None:
                continue
            anchor = next(p for p in source["parts"] if p["passage_id"] == source["anchor_passage_id"])
            replacement = anchors.get((source["pmid"], anchor["locator"]))
            if replacement is None:
                moved.append(
                    {"section": section, "payload_id": entry["payload_id"], "status": "not_found_in_refreshed_artifact"}
                )
                continue
            moved.append(
                {
                    "section": section,
                    "payload_id": entry["payload_id"],
                    "carried_to": replacement["payload_id"],
                    "pmid": source["pmid"],
                    "locator": anchor["locator"],
                    "readiness_before": source["readiness_state"],
                    "readiness_after": replacement["readiness_state"],
                }
            )
            entry["payload_id"] = replacement["payload_id"]
    return document, moved


def _task_kind(group: str) -> str:
    """Request taxonomy: only a required candidate-evidence article is a user download."""
    if group == "article_required_for_candidate_evidence":
        return "user_article_download_required"
    if group.startswith("article"):
        return "article_not_requested_pending_review"
    if group == "unidentified_reference":
        return "identify_reference"
    return "parse_or_format_repair"


def actionable_downloads(artifact: Path, frontier: pd.DataFrame, extra: list[dict]) -> pd.DataFrame:
    """Article requests, identification tasks and parse repairs, plus needs established by the audit."""
    downloads = pd.read_csv(artifact / "manual_downloads.csv")
    questions = _paper_questions(artifact)
    by_id = frontier.set_index("id")
    rows = []
    for row in downloads.itertuples(index=False):
        record = row._asdict()
        key = f"download:{record['group']}"
        frontier_id = record["request_id"]
        disposition = by_id.loc[frontier_id] if frontier_id in by_id.index else None
        lineages = sorted(set(json.loads(disposition["lineages"]))) if disposition is not None else []
        regulators = sorted(set(json.loads(disposition["tf_hgnc_ids"]))) if disposition is not None else []
        paper_lineages, paper_tfs = questions.get(str(record["pmid"]), ([], []))
        rows.append(
            {
                "request_id": frontier_id,
                "task": _task_kind(record["group"]),
                "user_action_required": record["group"] == "article_required_for_candidate_evidence",
                "group": record["group"],
                "pmid": record["pmid"],
                "title": record["title"],
                "item": record["item"],
                "link": record["verified_link"] or record["doi_url"] or record["pubmed_url"],
                "expected_path": record["inbox_destination"],
                "why": record["why"],
                "affected_manuscript_questions": json.dumps(lineages or paper_lineages),
                "affected_regulators": json.dumps(regulators or paper_tfs),
                "disposition": disposition["disposition"] if disposition is not None else UNRESOLVED,
                "established_by": "corpus_preparation",
                "kind": key,
            }
        )
    rows += extra
    return pd.DataFrame(rows)


def run_scope_closure(
    loaded: LoadedProjectConfig, manuscript_key: str, literature: Path, closure_path: Path | None = None
) -> dict:
    closure_path = closure_path or loaded.repo_root / "configs" / "p3_scope_closure.yaml"
    document = load_closure(closure_path)
    corpus_key = document["corpus_key"]
    artifact = loaded.data_root / "processed" / corpus_key
    ctx = c.corpus_context(loaded, manuscript_key, literature)
    named = {x["cell_type"]: set(x["named_tfs"]) for x in c.lineage_terms(ctx)}
    payloads = {}
    for line in (artifact / "bundles_all.jsonl").read_text(encoding="utf-8").splitlines():
        if line:
            payload = json.loads(line)
            payloads[payload["payload_id"]] = payload
    semantics_path = loaded.repo_root / "configs" / "p3_table_semantics.yaml"
    semantics = yaml.safe_load(semantics_path.read_text(encoding="utf-8")) if semantics_path.is_file() else None
    previous = document.get("carry_forward_from")
    document, moved = carry_forward(
        document, payloads, (loaded.data_root / "processed" / previous / "bundles_all.jsonl") if previous else None
    )
    problems = check_spans(document, payloads)
    if problems:
        raise ClosureError(f"audit spans not found in their bundles: {problems[:5]} ({len(problems)} problems)")
    manifest = selection_manifest(
        document, payloads, {"manuscript_key": manuscript_key, "corpus_key": corpus_key, "rule": CLOSURE_RULE}
    )
    frontier = dispositions(artifact, named)
    tasks = audit_tasks(artifact, frontier, semantics)
    frontier = pd.concat([frontier, tasks], ignore_index=True)
    downloads = actionable_downloads(
        artifact,
        frontier,
        document.get("additional_acquisition_needs", []) + document.get("new_acquisition_needs", []),
    )
    out = loaded.repo_root / "reports" / "literature" / corpus_key
    out.mkdir(parents=True, exist_ok=True)
    counts = {
        "frontier_items": int(len(frontier)),
        "by_disposition": frontier["disposition"].value_counts().to_dict(),
        # unit groups are not comparable and are never summed into a workload figure
        "by_unit_group": frontier.groupby("unit_group").size().to_dict(),
        "open_by_unit_group": frontier[frontier["open"]].groupby("unit_group").size().to_dict(),
        "open_items": int(frontier["open"].sum()),
        "names_manuscript_regulator": int(frontier["names_manuscript_regulator"].sum()),
        "selected_bundles": len(document["selection"]),
        "selected_papers": len({payloads[x["payload_id"]]["pmid"] for x in document["selection"]}),
        "audited_bundles": len(document["audit"]),
        "download_tasks": downloads["task"].value_counts().to_dict(),
        "user_downloads_required": int(downloads["user_action_required"].fillna(False).astype(bool).sum()),
    }
    record = {
        "rule": CLOSURE_RULE,
        "status": "proposed_pending_lead_review",
        "created_at": utc_now(),
        "corpus_key": corpus_key,
        "inputs_sha256": {
            "closure_input": sha256_file(closure_path),
            "manifest.json": sha256_file(artifact / "manifest.json"),
            "source_bundles_ready.jsonl": sha256_file(artifact / "source_bundles_ready.jsonl"),
            "remaining_work.parquet": sha256_file(artifact / "remaining_work.parquet"),
        },
        "ontology": json.loads((artifact / "ontology_scope.json").read_text())["mapping_sha256"],
        "counts": counts,
        "audit": document["audit"],
        "selection": document["selection"],
        "audit_selection_rule": document["audit_selection_rule"],
        "coverage_by_lineage": _coverage(document, payloads, named),
        "selection_carry_forward": moved,
        "table_semantics": semantics,
        "supplement_recovery": document.get("supplement_recovery"),
        "audit_tasks": tasks.to_dict("records"),
        "count_units": (
            "Unit groups are reported separately. Blocked bundles and their investigations describe the same "
            "work; table regions, references and download requests overlap; no total is a workload estimate."
        ),
        "user_download_requests": downloads[downloads["user_action_required"].fillna(False).astype(bool)][
            ["request_id", "pmid", "title", "link", "expected_path", "affected_manuscript_questions"]
        ]
        .astype(object)
        .where(lambda frame: frame.notna(), None)
        .to_dict("records"),
        "global_prerequisites": [
            "lead acceptance of these dispositions and of the validation selection",
            "P3 corpus freeze of the approved sources, ready bundles and investigation queue",
            "user choice of provider, model and spending cap",
            "P4 implementation and its no-inference payload validation",
        ],
    }
    readiness = json.loads((artifact / "extraction_readiness.json").read_text())["summary"]
    record["proposed_freeze_manifest"] = {
        "status": "proposed_not_frozen",
        "corpus_artifact": corpus_key,
        "artifact_manifest_sha256": sha256_file(artifact / "manifest.json"),
        "sources": {
            "acquired_publications": readiness["unique_publications"]["acquired_total"],
            "registered_assets": int(pd.read_parquet(artifact / "coverage_assets.parquet").shape[0]),
            "needed_supplements": readiness["needed_supplement_registry"]["needed_files"],
            "needed_supplements_acquired": readiness["needed_supplement_registry"]["acquired"],
        },
        "evidence": {
            "ready_bundles": readiness["bundles"]["by_state"].get("READY_FULL_TEXT", 0),
            "ready_batches": readiness["ready_batches"],
            "investigation_queue": readiness["context_investigations"]["queued"],
            "validation_selection_manifest_sha256": manifest["manifest_sha256"],
        },
        "outstanding_obligations": [
            {
                "obligation": "user article downloads for candidate evidence",
                "count": counts["user_downloads_required"],
                "ids": [x["request_id"] for x in record["user_download_requests"]],
            },
            {
                "obligation": "table regions pending source-specific meaning interpretation",
                "unit": "table regions",
                "count": int((frontier["reason"] == "table_meaning_interpretation_required").sum()),
                "by_publication": {
                    str(k): int(v)
                    for k, v in frontier[frontier["reason"] == "table_meaning_interpretation_required"]["pmid"]
                    .value_counts()
                    .head(5)
                    .items()
                },
                "named_tasks": [x["id"] for x in record["audit_tasks"] if x["id"].endswith("table-meaning")],
            },
            {
                "obligation": "of those, full-text requests that no authorized route satisfied",
                "unit": "requests",
                "subset_of": "user article downloads for candidate evidence",
                "count": int((downloads["group"] == "gap_established_full_text_missing").sum()),
                "ids": downloads.loc[downloads["group"] == "gap_established_full_text_missing", "request_id"].tolist(),
            },
            {
                "obligation": "reference identification tasks",
                "unit": "references",
                "count": int((frontier["reason"] == "reference_must_be_identified_then_acquired").sum()),
            },
            {
                "obligation": "relevance or attribution review of unresolved items",
                "unit": "mixed rows (bundles, papers, requests)",
                "count": int((frontier["disposition"] == UNRESOLVED).sum()),
            },
            {
                "obligation": "unresolved table semantics keep their interpretation blocker",
                "unit": "fields",
                "ids": [x["field"] for x in (semantics or {}).get("unresolved", []) if x.get("status") == "unknown"],
                "count": len([x for x in (semantics or {}).get("unresolved", []) if x.get("status") == "unknown"]),
            },
            {"obligation": "P4 implementation, no-inference validation, provider/model/budget choice", "count": 1},
        ],
        "blocks_a_specific_bundle": {
            "unit": "evidence bundles",
            "count": int(((frontier["kind"] == "bundle") & frontier["blocks_its_own_extraction"]).sum()),
            "note": "these block only their own bundle; the manuscript-completion obligations are listed above",
        },
        "not_claimed": (
            "Neither the validation selection nor the source-ready bundles are the final scientific evidence "
            "scope; every manuscript case stays in reporting whether or not literature was found."
        ),
    }
    record["record_sha256"] = sha256_text(canonical_json({k: v for k, v in record.items() if k != "created_at"}))
    (out / "scope_closure.json").write_text(json.dumps(record, indent=1, sort_keys=True, default=str), encoding="utf-8")
    (out / "validation_selection_manifest.json").write_text(json.dumps(manifest, indent=1, sort_keys=True), "utf-8")
    frontier.to_parquet(out / "frontier_dispositions.parquet", index=False)
    frontier.to_csv(out / "frontier_dispositions.csv", index=False)
    downloads.to_csv(out / "actionable_downloads.csv", index=False)
    (out / "scope_closure.md").write_text(_markdown(record, frontier, downloads, manifest), encoding="utf-8")
    return {
        "status": "SUCCEEDED",
        "key": record["record_sha256"][:16],
        "artifact": out,
        "corpus_id": ctx.corpus_id,
        "counts": counts,
    }


def _coverage(document: dict, payloads: dict, named: dict) -> dict:
    report = {}
    for lineage in sorted(named):
        selected = [
            (item, tf) for item in document["selection"] for line, tf in item["associations"] if line == lineage
        ]
        report[lineage] = {
            "selected_associations": len(selected),
            "exact_population": sum(1 for i, _ in selected if i["coverage"] == "exact_population"),
            "adjacent_population": sum(1 for i, _ in selected if i["coverage"] == "adjacent_population"),
            "transferable_other_tissue": sum(1 for i, _ in selected if i["coverage"] == "transferable_other_tissue"),
            "controls": sum(1 for i, _ in selected if i["purpose"] != "genuine_evidence"),
            "named_regulators_selected": sorted({tf for _, tf in selected} & named[lineage]),
            "named_regulators_not_selected": sorted(named[lineage] - {tf for _, tf in selected}),
        }
    return report


def _markdown(record: dict, frontier: pd.DataFrame, downloads: pd.DataFrame, manifest: dict) -> str:
    esc = lambda v: html.escape(str(v)).replace("|", "\\|")  # noqa: E731
    counts = record["counts"]
    lines = [
        "# P3 scope closure — PROPOSAL ONLY (pending lead review)",
        "",
        f"Corpus `{esc(record['corpus_key'])}`, rule `{CLOSURE_RULE}`, record `{record['record_sha256'][:16]}`.",
        f"Audited bundles: {counts['audited_bundles']}. Validation selection: {counts['selected_bundles']} bundles "
        f"from {counts['selected_papers']} papers (manifest `{manifest['manifest_sha256'][:16]}`).",
        "",
        "## Frontier dispositions",
        "",
        f"{counts['frontier_items']} items; {counts['open_items']} stay open; "
        f"{counts['names_manuscript_regulator']} name a manuscript regulator of their own lineage.",
        "",
        "| Disposition | Items |",
        "|---|---|",
    ]
    lines += [f"| {esc(k)} | {v} |" for k, v in sorted(counts["by_disposition"].items())]
    lines += ["", "| Disposition | Kind | Items | Open |", "|---|---|---|---|"]
    grouped = frontier.groupby(["disposition", "kind"]).agg(items=("id", "size"), open=("open", "sum")).reset_index()
    lines += [
        f"| {esc(x.disposition)} | {esc(x.kind)} | {x.items} | {x.open} |" for x in grouped.itertuples(index=False)
    ]
    lines += [
        "",
        "## Validation selection",
        "",
        "| Lineage | TF | Purpose | Coverage | PMID | Bundle | State |",
        "|---|---|---|---|---|---|---|",
    ]
    for entry in manifest["items"]:
        validation = entry["validation"]
        for association in validation["selected_associations"]:
            lines.append(
                f"| {esc(association['cell_type'])} | {esc(association['tf_hgnc_id'])} "
                f"({esc(association['tf_identity']['status'])}) | "
                f"{esc(validation['purpose'])}{'/' + esc(validation['control']) if validation.get('control') else ''} "
                f"| {esc(validation['coverage'])} | {esc(entry['pmid'])} | `{esc(entry['payload_id'])}` | "
                f"{esc(validation['readiness_state'])} |"
            )
    lines += ["", "## Coverage by lineage", ""]
    lines += [f"- **{esc(k)}**: {esc(v)}" for k, v in record["coverage_by_lineage"].items()]
    lines += ["", "## Actionable downloads and tasks", "", "| Task | Items |", "|---|---|"]
    lines += [f"| {esc(k)} | {v} |" for k, v in sorted(counts["download_tasks"].items())]
    lines += [
        "",
        f"**User downloads required: {counts['user_downloads_required']}.** Everything else is automated "
        "acquisition, identification or repair work; background and possible articles are listed, not requested.",
        "",
        "| Request | PMID | Title | Link | Expected path | Manuscript question |",
        "|---|---|---|---|---|---|",
    ]
    lines += [
        f"| {esc(x['request_id'])} | {esc(x['pmid'])} | {esc(str(x['title'])[:70])} | {esc(x['link'])} | "
        f"{esc(x['expected_path'])} | {esc(x['affected_manuscript_questions'])} |"
        for x in record["user_download_requests"]
    ]
    freeze = record["proposed_freeze_manifest"]
    lines += [
        "",
        f"## Proposed freeze manifest ({esc(freeze['status'])})",
        "",
        f"Corpus `{esc(freeze['corpus_artifact'])}`, manifest sha256 `{freeze['artifact_manifest_sha256'][:16]}`.",
        f"Sources: {esc(freeze['sources'])}",
        f"Evidence: {esc(freeze['evidence'])}",
        "",
        "| Outstanding obligation | Count |",
        "|---|---|",
    ]
    lines += [
        f"| {esc(x['obligation'])} | {esc(x.get('count', len(x.get('ids', []))))} |"
        for x in freeze["outstanding_obligations"]
    ]
    lines += ["", esc(freeze["not_claimed"]), ""]
    lines += ["", "## Global prerequisites before any extraction", ""]
    lines += [f"- {esc(x)}" for x in record["global_prerequisites"]]
    return "\n".join(lines) + "\n"
