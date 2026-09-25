"""Bounded assembly proposals and typed local-tool arguments."""

from typing import Literal

from pydantic import Field, model_validator

from regkg.extraction.schemas import StrictRecord


class Selection(StrictRecord):
    part_id: str
    role: Literal["anchor", "legend", "methods", "header", "qualifier", "counter_evidence"]


class ContextBinding(StrictRecord):
    field: Literal[
        "species",
        "cell_type",
        "tissue",
        "condition",
        "intervention",
        "assay",
        "comparison",
        "units",
        "scale",
        "normalization",
        "experiment_link",
        "statistic_definition",
        "reported_sample_structure",
    ]
    value: str | None = Field(max_length=500)
    state: Literal["SOURCE_STATED", "AMBIGUOUS", "UNKNOWN", "CONFLICTING"]
    source_part_ids: list[str] = Field(max_length=8)

    @model_validator(mode="after")
    def supported(self):
        if self.state == "SOURCE_STATED" and (not self.value or not self.source_part_ids):
            raise ValueError("Source-stated binding requires value and citations")
        if self.state == "UNKNOWN" and self.value is not None:
            raise ValueError("Unknown binding must have null value")
        return self


class OpenIssue(StrictRecord):
    code: Literal[
        "MISSING_ASSET",
        "PARSE_REPAIR",
        "IDENTITY_REVIEW",
        "MISSING_CONTEXT",
        "AMBIGUOUS_MEANING",
        "ANALYSIS_REQUIRED",
        "CONTEXT_TOO_LARGE",
        "SOURCE_CONFLICT",
    ]
    question: str = Field(max_length=600)
    source_part_ids: list[str] = Field(max_length=8)


class AssemblyProposal(StrictRecord):
    schema_version: Literal["evidence-assembly-1"]
    disposition: Literal[
        "CONTEXT_PROPOSED",
        "NEEDS_ASSET",
        "NEEDS_PARSE_REPAIR",
        "NEEDS_HUMAN_REVIEW",
        "ANALYSIS_REQUIRED",
        "NO_ADDITIONAL_CONTEXT_FOUND",
    ]
    selection: list[Selection] = Field(max_length=8)
    bindings: list[ContextBinding] = Field(max_length=12)
    issues: list[OpenIssue] = Field(max_length=8)
    decision_note: str = Field(max_length=500)


class PageArgs(StrictRecord):
    cursor: str | None = None
    limit: int = Field(default=10, ge=1, le=20)


class SearchArgs(StrictRecord):
    query: str = Field(min_length=1, max_length=300)
    asset_ids: list[str] | None = None
    kinds: (
        list[
            Literal[
                "paragraph",
                "abstract",
                "title",
                "figure_caption",
                "table_caption",
                "table_row",
                "table_header",
                "table_footnote",
                "footnote",
                "supplementary",
            ]
        ]
        | None
    ) = None
    cursor: str | None = None
    limit: int = Field(default=5, ge=1, le=10)


class ReadArgs(StrictRecord):
    part_ids: list[str] = Field(min_length=1, max_length=3)


class InspectArgs(StrictRecord):
    asset_id: str
    table_id: str | None = None
    cursor: str | None = None
    limit: int = Field(default=5, ge=1, le=10)


class Filter(StrictRecord):
    column_id: str
    op: Literal["eq", "in", "contains_literal", "lt", "le", "gt", "ge"]
    values: list[str] = Field(min_length=1, max_length=20)

    @model_validator(mode="after")
    def one(self):
        if self.op != "in" and len(self.values) != 1:
            raise ValueError("Only in accepts multiple values")
        return self


class TableArgs(StrictRecord):
    table_id: str
    column_ids: list[str] = Field(min_length=1, max_length=12)
    row_ids: list[str] | None = Field(default=None, max_length=20)
    filters: list[Filter] = Field(default_factory=list, max_length=3)
    cursor: str | None = None
    limit: int = Field(default=5, ge=1, le=20)

    @model_validator(mode="after")
    def selector(self):
        if self.row_ids is not None and self.filters:
            raise ValueError("Use row_ids or filters, not both")
        return self


class ReferenceArgs(StrictRecord):
    from_part_id: str
    reference_label: str = Field(min_length=1, max_length=120)
    limit: int = Field(default=5, ge=1, le=10)
