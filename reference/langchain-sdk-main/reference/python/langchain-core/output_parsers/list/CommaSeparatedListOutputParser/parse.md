---
title: "parse"
description: "Parse the output of an LLM call."
source: "https://reference.langchain.com/python/langchain-core/output_parsers/list/CommaSeparatedListOutputParser/parse"
category: "reference"
tags: [reference, langchain-core, output_parsers, list, commaseparatedlistoutputparser, parse]
---

# parse

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/output_parsers/list/CommaSeparatedListOutputParser/parse)

Parse the output of an LLM call.

## Signature

```python
parse(
    self,
    text: str,
) -> list[str]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text` | `str` | Yes | The output of an LLM call. |

## Returns

`list[str]`

A list of strings.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/output_parsers/list.py#L164)
