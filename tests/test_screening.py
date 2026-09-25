"""LLM screening contract: inputs, windows, citation validation and the merge rule (no chat calls)."""

from __future__ import annotations

from regkg.literature import screening_llm as sl
from regkg.workflows.screening import Allowance, Budget


def passage(pid: str, text: str, section_type: str = "results", kind: str = "paragraph") -> dict:
    return {"passage_id": pid, "text": text, "section_type": section_type, "kind": kind, "locator": f"/x/{pid}"}


def test_sections_keep_main_text_cap_table_rows_and_drop_bibliography():
    passages = [
        passage("p1", "A title", "title", "title"),
        passage("p2", "We screened lungs.", "abstract", "abstract"),
        passage("p3", "EGR2 was deleted in macrophages.", "results"),
        passage("p4", "Fig 1. EGR2 staining.", "results", "figure_caption"),
        *[passage(f"t{i}", f"GENE{i} | 0.1", "results", "table_row") for i in range(12)],
        passage("p9", "1. Smith et al.", "references"),
    ]
    sections, skipped, notes = sl.build_sections(passages, max_table_rows=3)
    by_kind: dict[str, list[str]] = {}
    for section in sections:
        by_kind.setdefault(section.kind, []).extend(pid for pid, _ in section.passages)
    assert sl.has_main_text(sections) and "references" in skipped
    assert len(by_kind["table"]) == 3 and any("table rows capped at 3" in n for n in notes)
    assert by_kind["caption"] == ["p4"]
    assert sorted(by_kind["abstract"]) == ["p1", "p2"]  # title and abstract are both abstract-level
    assert by_kind["body"] == ["p3"]


def test_abstract_only_paper_is_not_reported_as_main_text():
    sections, _, _ = sl.build_sections(
        [passage("p1", "T", "title", "title"), passage("p2", "A", "abstract", "abstract")]
    )
    assert not sl.has_main_text(sections)


def _paper(sections: list[sl.Section]) -> sl.PaperInput:
    return sl.PaperInput("pub:1", "1", "T", "jats", "a" * 64, "doc", sections)


def test_every_section_reaches_a_window_and_windows_overlap():
    sections = [sl.Section(f"s{i}", "body", f"section{i}", [(f"p{i}", "x" * 400)]) for i in range(6)]
    paper = _paper(sections)
    windows = sl.make_windows(paper, max_chars=900, overlap_sections=1, supplement_block="- none recorded")
    covered = {pid for w in windows for pid in w.passage_ids}
    assert covered == {f"p{i}" for i in range(6)}  # nothing is silently dropped
    assert len(windows) > 1 and windows[-1].total == len(windows)
    assert "SUPPLEMENTARY FILE INVENTORY" in windows[-1].text
    assert set(windows[0].passage_ids) & set(windows[1].passage_ids)  # local overlap


def test_citations_must_name_a_window_passage_and_quote_it_verbatim():
    result = sl.WindowScreening(
        assessments=[
            sl.QuestionAssessment(
                question="Alveolar_Macrophages",
                decision="include_for_extraction",
                rationale="r",
                citations=[
                    sl.EvidenceCitation(passage_id="p1", exact_span="EGR2 was deleted", evidence_category="regulation"),
                    sl.EvidenceCitation(passage_id="p9", exact_span="not here at all", evidence_category="regulation"),
                    sl.EvidenceCitation(
                        passage_id="p1", exact_span="invented claim text", evidence_category="regulation"
                    ),
                ],
            )
        ]
    )
    problems = sl.validate_citations(result, {"p1": "EGR2 was deleted in macrophages."})
    kinds = {p["problem"] for p in problems}
    assert kinds == {"passage_not_in_window", "span_not_in_passage"}
    assert not sl.validate_citations(
        sl.WindowScreening(
            assessments=[
                sl.QuestionAssessment(
                    question="AT1",
                    decision="background",
                    rationale="r",
                    citations=[
                        sl.EvidenceCitation(
                            passage_id="p1", exact_span="EGR2  was   deleted", evidence_category="expression"
                        )
                    ],
                )
            ]
        ),
        {"p1": "EGR2 was deleted in macrophages."},
    )  # whitespace differences are tolerated, invented text is not


def test_one_negative_window_never_excludes_a_paper_and_unread_windows_force_uncertainty():
    window = sl.Window("w1", 1, 2, ["s1"], "t", ["p1"])
    other = sl.Window("w2", 2, 2, ["s2"], "t", ["p2"])
    negative = sl.WindowScreening(
        assessments=[sl.QuestionAssessment(question="AT1", decision="exclude_with_reason", rationale="no AT1 here")]
    )
    positive = sl.WindowScreening(
        assessments=[sl.QuestionAssessment(question="AT1", decision="include_for_extraction", rationale="AT1 result")]
    )
    merged = sl.merge_windows([(window, negative), (other, positive)], unread=[])
    assert merged["AT1"]["decision"] == "include_for_extraction"
    assert merged["AT1"]["decisions_by_window"] == ["exclude_with_reason", "include_for_extraction"]
    # an unread window keeps the paper uncertain rather than excluded
    only_negative = sl.merge_windows([(window, negative)], unread=["w2"])
    assert only_negative["AT1"]["decision"] == "needs_full_text_or_context"


def test_concurrent_attempts_and_repairs_cannot_exceed_allowance(tmp_path):
    from concurrent.futures import ThreadPoolExecutor

    budget = Budget(Allowance(2, 250, 30, None), tmp_path / "budget.json")
    with ThreadPoolExecutor(max_workers=8) as pool:
        outcomes = list(pool.map(lambda _: budget.reserve(100, 10), range(20)))
    allowed = [reservation for reservation, stop in outcomes if stop is None]
    assert len(allowed) == 2
    for reservation in allowed:
        budget.settle(reservation, {"input_tokens": 80, "output_tokens": 8, "usd": None})
    assert budget.used == {"calls": 2, "input_tokens": 160, "output_tokens": 16, "usd": None}
    resumed = Budget(Allowance(2, 250, 30, None), tmp_path / "budget.json")
    assert resumed.reserve(1, 1)[1] == "max_calls"
    assert resumed.price_unknown_calls == 2


def test_crashed_or_failed_requests_keep_reservation_and_unknown_usage(tmp_path):
    path = tmp_path / "budget.json"
    budget = Budget(Allowance(10, 110, 20, None), path)
    reservation, _ = budget.reserve(100, 10)
    resumed = Budget(Allowance(10, 110, 20, None), path)
    assert resumed.reserve(20, 1)[1] == "max_input_tokens"
    budget.settle(reservation, {"input_tokens": None, "output_tokens": None, "usd": None})
    assert budget.used["input_tokens"] == 100 and budget.unknown_token_calls == 1
    assert budget.used["usd"] is None
    assert Budget(Allowance(1, None, None, 1)).reserve(1, 1)[1] == "cost_reservation_unavailable"


def test_invalid_json_retry_is_counted_and_cannot_bypass_call_limit(monkeypatch, tmp_path):
    from regkg.workflows import screening as workflow

    calls = []

    def invalid(*args):
        calls.append(1)
        return None, {"input_tokens": 10, "output_tokens": 5, "usd": None}, "not JSON"

    monkeypatch.setattr(workflow, "call_window", invalid)
    paper = _paper([sl.Section("s", "body", "results", [("p1", "A source result.")])])
    window = sl.Window("w1", 1, 1, ["s"], "[p1] A source result.", ["p1"])
    result = workflow._call_with_repair(
        paper,
        window,
        "scope",
        None,
        {"max_output_tokens": 100, "max_attempts_per_call": 2},
        Budget(Allowance(1, None, None, None)),
        "prompt",
    )
    assert len(calls) == 1 and result["calls"] == 1
    assert result["state"] == "allowance_reached:max_calls"
    assert result["usage"]["usd"] is None


def test_oversized_sections_keep_every_passage_and_bound_windows():
    text = "A long source passage. " * 500
    paper = _paper([sl.Section("s", "body", "results", [("p1", text), ("p2", "Other source text.")])])
    windows = sl.make_windows(paper, 1000, 1, "none")
    assert len(windows) > 5 and all(len(w.text) < 1100 for w in windows)
    assert {pid for w in windows for pid in w.passage_ids} == {"p1", "p2"}
    fragments = []
    for w in windows:
        for line in w.text.splitlines():
            if line.startswith("[p1] "):
                fragments.append(line[5:])
    assert "".join(fragments) == text


def test_ungrounded_inclusion_and_unassessed_questions_stay_uncertain():
    result = sl.WindowScreening(
        assessments=[sl.QuestionAssessment(question="AT1", decision="include_for_extraction", rationale="r")]
    )
    assert sl.validate_citations(result, {})[0]["problem"] == "ungrounded_positive_decision"
    merged = sl.merge_windows([], [])
    assert set(merged) == set(sl.QUESTIONS)
    assert all(q["decision"] == "needs_full_text_or_context" for q in merged.values())


def test_source_hash_changes_with_text_and_declared_missingness():
    paper = _paper([sl.Section("s", "body", "results", [("p1", "Original source.")])])
    original = paper.source_hash()
    paper.sections[0].passages[0] = ("p1", "Changed source.")
    assert paper.source_hash() != original
    changed = paper.source_hash()
    paper.missing_sections.append("methods")
    assert paper.source_hash() != changed


def test_supplement_rendering_lists_files_without_dumping_numbers():
    rendered = sl.render_supplements(
        [
            {
                "filename": "table_s5.csv",
                "route": "delimited",
                "state": "PARTIAL",
                "header": "p_val | avg_logFC",
                "preview": "TEAD1 | 0.05 | 0.3",
                "blocker": "row limit",
            }
        ],
        preview_chars=10,
        limit=5,
    )
    assert "table_s5.csv" in rendered and "p_val | avg_logFC" in rendered
    assert "TEAD1 | 0." in rendered and len(rendered.split("preview: ")[1].split(" blocker")[0]) <= 10


def test_discovery_deduplicates_source_linked_doi_against_acquired_and_keeps_no_tf(tmp_path):
    import pandas as pd

    from regkg.literature.publications import publication_id
    from regkg.provenance import write_json
    from regkg.workflows.screening import discovery_inputs, discovery_pool

    pid = publication_id({"pmid": "1"})
    pd.DataFrame(
        [
            {"publication_id": pid, "pmid": "1", "doi": "10.1/a", "pmcid": None},
            {"publication_id": "old-doi-id", "pmid": None, "doi": "10.1/a", "pmcid": None},
            {"publication_id": publication_id({"pmid": "2"}), "pmid": "2", "doi": None, "pmcid": None},
        ]
    ).to_parquet(tmp_path / "discovery_coverage.parquet")
    fresh = discovery_pool(tmp_path, pd.DataFrame([{"publication_id": pid, "pmid": "1"}]))
    assert fresh.pmid.tolist() == ["2"]
    write_json(
        tmp_path / "discovery" / "batch-000.json",
        {
            "results": [
                {
                    "records": [
                        {
                            "source": "pubmed",
                            "rank": 1,
                            "cache_key": "synthetic",
                            "pmid": "2",
                            "title": "Lung neighborhoods",
                            "abstract": "No exact TF seed is needed to retain this abstract.",
                        }
                    ]
                }
            ]
        },
    )
    prepared = discovery_inputs(tmp_path)[fresh.iloc[0].publication_id]
    assert prepared.version_read.startswith("cached_pubmed_metadata")
    assert prepared.sections[1].passages[0][1].startswith("No exact TF")
    assert prepared.missing_sections == ["main_text(introduction/methods/results/discussion)"]


def test_litellm_adapter_never_forwards_openrouter_options(monkeypatch):
    import langchain_openai

    from regkg.config import ModelRole, parse_model_selector
    from regkg.workflows.screening import build_chat

    calls = []
    monkeypatch.setattr(langchain_openai, "ChatOpenAI", lambda **kw: calls.append(kw) or kw)
    build_chat(
        parse_model_selector("litellm:team/model:revision", ModelRole.CHAT),
        {
            "LITELLM_BASE_URL": "https://example.test",
            "LITELLM_API_KEY": "dummy",
            "OPENROUTER_PROVIDER_ORDER": "should,not,leak",
            "OPENROUTER_REASONING": "invalid",
        },
        {"max_output_tokens": 5000},
    )
    assert calls[0]["model"] == "team/model:revision"
    assert calls[0]["base_url"] == "https://example.test"
    assert "extra_body" not in calls[0] and calls[0]["max_retries"] == 0


def test_targeted_repair_preserves_originals_and_replays_without_calls(monkeypatch, tmp_path):
    from regkg.workflows import screening as workflow

    paper = _paper([sl.Section("s", "body", "results", [("p1", "Exact source statement.")])])
    windows = [
        sl.Window("valid", 1, 2, ["s"], "[p1] Exact source statement.", ["p1"]),
        sl.Window("failed", 2, 2, ["s"], "[p1] Exact source statement.", ["p1"]),
    ]
    calls = []

    def fake_call(paper, window, scope, chat, settings, budget, prompt_sha, repair_record=None):
        calls.append((window.window_id, repair_record is not None))
        valid = window.window_id == "valid" or repair_record is not None
        return {
            "window_id": window.window_id,
            "state": "valid" if valid else "invalid_needs_review",
            "result": {"assessments": []} if valid else None,
            "usage": {"input_tokens": 10, "output_tokens": 5, "usd": None},
            "calls": 1,
            "attempts": [],
        }

    monkeypatch.setattr(workflow, "_call_with_repair", fake_call)
    budget = Budget(Allowance(10, None, None, None))
    first = workflow.screen_paper(paper, windows, "scope", None, {}, budget, tmp_path, "prompt")
    assert first["state"] == "partial"
    originals = {p.name: p.read_bytes() for p in tmp_path.glob("*.json")}
    repaired = workflow.screen_paper(paper, windows, "scope", None, {}, budget, tmp_path, "prompt", True)
    assert repaired["state"] == "screened"
    assert calls == [("valid", False), ("failed", False), ("failed", True)]
    assert originals == {p.name: p.read_bytes() for p in tmp_path.glob("*.json")}
    workflow.screen_paper(paper, windows, "scope", None, {}, budget, tmp_path, "prompt", True)
    assert len(calls) == 3


def test_pointer_repair_requires_unique_unchanged_quote_in_shown_source():
    from regkg.workflows.screening import repair_citation_ids

    result = sl.WindowScreening(
        assessments=[
            sl.QuestionAssessment(
                question="AT1",
                decision="background",
                rationale="source context",
                citations=[
                    sl.EvidenceCitation(
                        passage_id="wrong", exact_span="Exact source statement.", evidence_category="background"
                    )
                ],
            )
        ]
    )
    fixed, changes = repair_citation_ids(result, {"p1": "Exact source statement."}, "Exact source statement.")
    assert fixed.assessments[0].citations[0].passage_id == "p1" and len(changes) == 1
    assert result.assessments[0].citations[0].passage_id == "wrong"
    for passages, shown in [
        ({"p1": "Exact source statement.", "p2": "Exact source statement."}, "Exact source statement."),
        ({"p1": "Exact source statement."}, "Different shown text."),
        ({"p1": "A paraphrase of that statement."}, "Exact source statement."),
    ]:
        fixed, changes = repair_citation_ids(result, passages, shown)
        assert not changes and fixed.assessments[0].citations[0].passage_id == "wrong"
