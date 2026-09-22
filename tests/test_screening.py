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


def test_allowance_stops_the_run_at_the_first_bound():
    budget = Budget(Allowance(max_calls=2, max_input_tokens=None, max_output_tokens=None, max_usd=0.5))
    assert budget.check() is None
    budget.spend({"input_tokens": 100, "output_tokens": 10, "usd": 0.1})
    assert budget.check() is None
    budget.spend({"input_tokens": 100, "output_tokens": 10, "usd": None})
    assert budget.check() == "max_calls" and budget.price_unknown_calls == 1
    spent = Budget(Allowance(max_calls=None, max_input_tokens=None, max_output_tokens=None, max_usd=0.2))
    spent.spend({"input_tokens": 1, "output_tokens": 1, "usd": 0.25})
    assert spent.check() == "max_usd"


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
