---
title: "parse_result"
description: "Parse a list of candidate model Generation objects into a specific format."
source: "https://reference.langchain.com/python/langchain-core/output_parsers/base/BaseLLMOutputParser/parse_result"
category: "reference"
tags: [reference, langchain-core, output_parsers, base, basellmoutputparser, parse_result]
---

# parse_result

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/output_parsers/base/BaseLLMOutputParser/parse_result)

Parse a list of candidate model `Generation` objects into a specific format.

## Signature

```python
parse_result(
    self,
    result: list[Generation],
    *,
    partial: bool = False,
) -> T
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `result` | `list[Generation]` | Yes | A list of `Generation` to be parsed.  The `Generation` objects are assumed to be different candidate outputs for a single model input. |
| `partial` | `bool` | No | Whether to parse the output as a partial result.  This is useful for parsers that can parse partial results. (default: `False`) |

## Returns

`T`

Structured output.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/output_parsers/base.py#L37)
