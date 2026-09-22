---
title: "handle_errors"
description: "Error handling strategy for structured output via ToolStrategy."
source: "https://reference.langchain.com/python/langchain/agents/structured_output/ToolStrategy/handle_errors"
category: "reference"
tags: [reference, langchain, agents, structured_output, toolstrategy, handle_errors]
---

# handle_errors

> **Attribute** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/structured_output/ToolStrategy/handle_errors)

Error handling strategy for structured output via `ToolStrategy`.

- `True`: Catch all errors with default error template
- `str`: Catch all errors with this custom message
- `type[Exception]`: Only catch this exception type with default message
- `tuple[type[Exception], ...]`: Only catch these exception types with default
    message
- `Callable[[Exception], str]`: Custom function that returns error message
- `False`: No retry, let exceptions propagate

!!! warning "Raw JSON schema dicts are not validated"
    When `schema` is a raw JSON schema `dict` (as opposed to a Pydantic model,
    `dataclass`, or `TypedDict`), the model's tool-call arguments are returned
    **as-is without validation** against the schema.

    As a result, `handle_errors` is effectively inert for dict schemas. To get
    validation and automatic retries, express the schema as a Pydantic model,
    `dataclass`, or `TypedDict` instead.

## Signature

```python
handle_errors: bool | str | type[Exception] | tuple[type[Exception], ...] | Callable[[Exception], str] = handle_errors
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/structured_output.py#L251)
