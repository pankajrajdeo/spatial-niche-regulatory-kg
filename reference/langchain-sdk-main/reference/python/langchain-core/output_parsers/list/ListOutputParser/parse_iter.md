---
title: "parse_iter"
description: "Parse the output of an LLM call."
source: "https://reference.langchain.com/python/langchain-core/output_parsers/list/ListOutputParser/parse_iter"
category: "reference"
tags: [reference, langchain-core, output_parsers, list, listoutputparser, parse_iter]
---

# parse_iter

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/output_parsers/list/ListOutputParser/parse_iter)

Parse the output of an LLM call.

## Signature

```python
parse_iter(
    self,
    text: str,
) -> Iterator[re.Match[str]]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text` | `str` | Yes | The output of an LLM call. |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/output_parsers/list.py#L61)
