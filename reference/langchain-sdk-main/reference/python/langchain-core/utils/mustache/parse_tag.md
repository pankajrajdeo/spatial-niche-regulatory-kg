---
title: "parse_tag"
description: "Parse a tag from a template."
source: "https://reference.langchain.com/python/langchain-core/utils/mustache/parse_tag"
category: "reference"
tags: [reference, langchain-core, utils, mustache, parse_tag]
---

# parse_tag

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/mustache/parse_tag)

Parse a tag from a template.

## Signature

```python
parse_tag(
    template: str,
    l_del: str,
    r_del: str,
) -> tuple[tuple[str, str], str]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `template` | `str` | Yes | The template. |
| `l_del` | `str` | Yes | The left delimiter. |
| `r_del` | `str` | Yes | The right delimiter. |

## Returns

`tuple[tuple[str, str], str]`

The tag and the template.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/utils/mustache.py#L118)
