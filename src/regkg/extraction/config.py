"""Validated finite bounds for P4; model selectors retain the shared env/YAML contract."""

from typing import Literal

from pydantic import Field

from regkg.config import read_yaml
from regkg.extraction.schemas import StrictRecord


class RuntimeConfig(StrictRecord):
    structured_method: str
    max_output_tokens: int = Field(ge=1, le=16000)
    max_input_tokens: int = Field(ge=1, le=100000)
    reasoning_effort: str | None
    timeout_seconds: int = Field(ge=1, le=180)
    attempts_per_call: int = Field(ge=1, le=2)
    max_calls: int = Field(ge=1, le=1000)
    max_input_tokens_total: int = Field(ge=1)
    max_output_tokens_total: int = Field(ge=1)
    max_usd: float | None = Field(ge=0)
    max_papers: int = Field(ge=1, le=10)
    max_bundles: int = Field(ge=1, le=20)


class AssemblyConfig(StrictRecord):
    reasoning_effort: Literal["low", "medium", "high"] = "low"
    max_model_calls: int = Field(ge=1, le=4)
    max_tool_calls: int = Field(ge=1, le=8)
    max_input_tokens: int = Field(ge=1, le=24000)
    max_output_tokens: int = Field(ge=1, le=6000)
    max_tool_chars: int = Field(ge=100, le=6000)
    model_timeout_seconds: int = Field(ge=1, le=60)
    tool_timeout_seconds: int = Field(ge=1, le=10)
    max_runtime_seconds: int = Field(ge=1, le=300)


def load_config(path):
    value = read_yaml(path)
    unknown = set(value) - {"extractor", "verifier", "runtime", "assembly"}
    if unknown:
        raise ValueError(f"Unknown extraction configuration sections: {sorted(unknown)}")
    runtime = RuntimeConfig.model_validate(value["runtime"])
    if runtime.structured_method not in {"json_schema", "function_calling"}:
        raise ValueError("P4 requires an explicitly selected structured-output mode")
    value["runtime"] = runtime.model_dump()
    value["assembly"] = AssemblyConfig.model_validate(value["assembly"]).model_dump()
    return value
