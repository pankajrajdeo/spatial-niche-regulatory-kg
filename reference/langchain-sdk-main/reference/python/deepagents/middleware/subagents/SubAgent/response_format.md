---
title: "response_format"
description: "Structured output response format for the subagent."
source: "https://reference.langchain.com/python/deepagents/middleware/subagents/SubAgent/response_format"
category: "reference"
tags: [reference, deepagents, middleware, subagents, subagent, response_format]
---

# response_format

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/subagents/SubAgent/response_format)

Structured output response format for the subagent.

When specified, the subagent will produce a `structured_response` conforming
to the given schema. The structured response is JSON-serialized and returned
as the `ToolMessage` content to the parent agent, replacing the default
last-message extraction.

Accepted formats (from `langchain.agents.structured_output`):

- `ToolStrategy(schema)`: Use tool calling to extract structured output from the model.
- `ProviderStrategy(schema)`: Use the model provider's native structured output mode.
- `AutoStrategy(schema)`: Automatically select the best strategy.
- A bare Python `type`: A Pydantic `BaseModel` subclass, `dataclass`,
    or `TypedDict` class.

    Equivalent to `AutoStrategy(schema)`.
- `dict[str, Any]`: A JSON schema dictionary
    (e.g., `{"type": "object", "properties": {...}, "required": [...]}`).

## Signature

```python
response_format: NotRequired[ResponseFormat[Any] | type | dict[str, Any]]
```

## Description

**Example:**

```python
from pydantic import BaseModel

class Findings(BaseModel):
    findings: str
    confidence: float

analyzer: SubAgent = {
    "name": "analyzer",
    "description": "Analyzes data and returns structured findings",
    "system_prompt": "Analyze the data and return your findings.",
    "model": "openai:gpt-5.5",
    "tools": [],
    "response_format": Findings,
}
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/subagents.py#L163)
