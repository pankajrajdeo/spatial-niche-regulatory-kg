---
title: "parse_result"
description: "Parse the result of an LLM call to a list of Pydantic objects."
source: "https://reference.langchain.com/python/langchain-core/output_parsers/openai_tools/PydanticToolsParser/parse_result"
category: "reference"
tags: [reference, langchain-core, output_parsers, openai_tools, pydantictoolsparser, parse_result]
---

# parse_result

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/output_parsers/openai_tools/PydanticToolsParser/parse_result)

Parse the result of an LLM call to a list of Pydantic objects.

## Signature

```python
parse_result(
    self,
    result: list[Generation],
    *,
    partial: bool = False,
) -> Any
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `result` | `list[Generation]` | Yes | The result of the LLM call. |
| `partial` | `bool` | No | Whether to parse partial JSON.  If `True`, the output will be a JSON object containing all the keys that have been returned so far.  If `False`, the output will be the full JSON object. (default: `False`) |

## Returns

`Any`

The parsed Pydantic objects.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/output_parsers/openai_tools.py#L313)
