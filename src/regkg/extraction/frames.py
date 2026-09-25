"""Source-backed experiment context prepared before atomic finding extraction."""

from pydantic import Field, create_model

from regkg.extraction.critique import ContextRequest
from regkg.extraction.schemas import Citation, StrictRecord
from regkg.provenance import stable_id


class FrameField(StrictRecord):
    value: str = Field(min_length=1, max_length=400)
    evidence: list[Citation] = Field(min_length=1, max_length=3)


FRAME_FIELDS = {
    "intervention": "Source-stated manipulation/exposure, preserving joint groups.",
    "comparison": "Explicit comparison; never invent a control group.",
    "species": "Source-stated experimental organism, not inferred from a gene or project.",
    "tissue": "Source-stated anatomical tissue.",
    "cell_type": "Experimental cell population with marker qualifiers exactly preserved.",
    "condition": "Source-stated condition of this experiment.",
    "disease": "Source-stated disease; null when absent.",
    "model_system": "Source-stated animal/culture/organoid system.",
    "assay": "Assay explicitly linked to THIS result, not merely a nearby caption panel.",
    "experiment_label": "Exact figure/panel/experiment label explicitly linked to this result.",
    "time": "Explicit experimental time, not inferred.",
    "dose": "Explicit dose, not inferred.",
    "measured_variable": "Exactly ONE measured variable for this frame. Split distinct outcomes into separate frames.",
    "subject": "Manipulated entity or measured subject of an observational comparison.",
    "object": "Responding entity or context for this one measured outcome.",
}
FrameFields = create_model(
    "ExperimentFields",
    __base__=StrictRecord,
    **{
        name: (FrameField | None, Field(description=description + " Null if unknown."))
        for name, description in FRAME_FIELDS.items()
    },
)


class EvidenceFrame(StrictRecord):
    result: Citation = Field(description="Exact explicit result, including nulls; not a methods-only statement.")
    fields: FrameFields
    missing_context: list[str] = Field(max_length=8)


class FrameAssembly(StrictRecord):
    frames: list[EvidenceFrame] = Field(max_length=24)
    context_requests: list[ContextRequest] = Field(max_length=3)
    overflow: bool


FRAME_PROMPT = (
    "Assemble experimental evidence frames BEFORE relation extraction. Read original source only.\n"
    "One frame links ONE measured variable and ONE intervention/comparison to its experiment and result; "
    "it is not a regulatory claim.\n"
    "Include observational, computational and explicit null findings; resource descriptions are not results.\n"
    "For each non-null field provide exact quotations establishing it for THIS experiment. Set unknown "
    "fields null.\n"
    "Split distinct outcomes (e.g. cell proportion versus cell size) into separate frames when separately "
    "stated;\n"
    "never concatenate variables or repeat fields to squeeze multiple experiments into one frame.\n"
    "A caption saying a measurement was performed is not a result: do not emit a frame without a reported "
    "outcome.\n"
    "Do not supply customary marker combinations absent from the text, even with an inferred qualifier.\n"
    "Identify the intervention, comparator, local molecular form, measured variable, assay and model/context.\n"
    "Do not fill species, control group, assay, time or dose from general knowledge. A nearby methods "
    "statement,\n"
    "shared gene or same figure number does not establish experiment linkage. Preserve joint perturbations.\n"
    "Split distinct panels/experiments; retain qualifiers, contradictions and primary/secondary attribution.\n"
    "If an identifiable reference needs additional local context, request it with an exact anchor and a "
    "specific\n"
    "question. A missing optional detail does not erase a supported result. Source labels are navigation "
    "hints,\n"
    "not proof that two parts describe the same experiment. Do not invent outcomes from a caption listing "
    "assays.\n"
    "Return no frames when there is no eligible result. Flag overflow rather than truncating silently.\n"
)


def grounded(citation, parts):
    return any(p["part_id"] == citation.part_id and citation.quote in p["text"] for p in parts)


def validate_frames(assembly, parts):
    valid, invalid = [], []
    for index, frame in enumerate(assembly.frames):
        fields = [f for f in frame.fields.__dict__.values() if f is not None]
        failures = []
        if not all(grounded(c, parts) for c in [frame.result, *[c for f in fields for c in f.evidence]]):
            failures.append("frame_quote_not_grounded")
        if failures:
            invalid.append({"index": index, "failures": failures, "frame": frame.model_dump()})
        else:
            value = frame.model_dump()
            value["frame_id"] = stable_id("experiment-frame", value)
            if value not in valid:
                valid.append(value)
    return valid, invalid


def frame_failures(observation, frames):
    frame = frames.get(observation.frame_id)
    if frame is None:
        return ["unknown_evidence_frame"]
    variable = frame["fields"].get("measured_variable")
    if variable is None or observation.measured_variable != variable["value"]:
        return ["frame_measurement_mismatch"]
    return []


def compact_frame_context(frames):
    """Deduplicate repeated frame citations without dropping source text or fields."""
    from copy import deepcopy

    compact = deepcopy(frames)
    citations = {}

    def reference(citation):
        key = stable_id("frame-citation", citation)
        citations[key] = citation
        return key

    for frame in compact:
        frame["result_ref"] = reference(frame.pop("result"))
        for field in frame["fields"].values():
            if field is not None:
                field["evidence_refs"] = [reference(c) for c in field.pop("evidence")]
    return compact, citations
