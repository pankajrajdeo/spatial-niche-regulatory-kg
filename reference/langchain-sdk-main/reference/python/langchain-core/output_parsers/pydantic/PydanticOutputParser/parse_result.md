---
title: "parse_result"
description: "Parse the result of an LLM call to a Pydantic object."
source: "https://reference.langchain.com/python/langchain-core/output_parsers/pydantic/PydanticOutputParser/parse_result"
category: "reference"
tags: [reference, langchain-core, output_parsers, pydantic, pydanticoutputparser, parse_result]
---

# parse_result

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/output_parsers/pydantic/PydanticOutputParser/parse_result)

Parse the result of an LLM call to a Pydantic object.

## Signature

```python
parse_result(
    self,
    result: list[Generation],
    *,
    partial: bool = False,
) -> TBaseModel | None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `result` | `list[Generation]` | Yes | The result of the LLM call. |
| `partial` | `bool` | No | Whether to parse partial JSON objects.  If `True`, the output will be a JSON object containing all the keys that have been returned so far. (default: `False`) |

## Returns

`TBaseModel | None`

The parsed Pydantic object.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/output_parsers/pydantic.py#L57)
