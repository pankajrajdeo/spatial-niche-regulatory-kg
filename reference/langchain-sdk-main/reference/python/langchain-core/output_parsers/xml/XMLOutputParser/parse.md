---
title: "parse"
description: "Parse the output of an LLM call."
source: "https://reference.langchain.com/python/langchain-core/output_parsers/xml/XMLOutputParser/parse"
category: "reference"
tags: [reference, langchain-core, output_parsers, xml, xmloutputparser, parse]
---

# parse

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/output_parsers/xml/XMLOutputParser/parse)

Parse the output of an LLM call.

## Signature

```python
parse(
    self,
    text: str,
) -> dict[str, str | list[Any]]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text` | `str` | Yes | The output of an LLM call. |

## Returns

`dict[str, str | list[Any]]`

A `dict` representing the parsed XML.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/output_parsers/xml.py#L207)
