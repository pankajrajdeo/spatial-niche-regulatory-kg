---
title: "find_all_links"
description: "Extract all links from a raw HTML string."
source: "https://reference.langchain.com/python/langchain-core/utils/html/find_all_links"
category: "reference"
tags: [reference, langchain-core, utils, html, find_all_links]
---

# find_all_links

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/html/find_all_links)

Extract all links from a raw HTML string.

## Signature

```python
find_all_links(
    raw_html: str,
    *,
    pattern: str | re.Pattern[str] | None = None,
) -> list[str]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `raw_html` | `str` | Yes | original HTML. |
| `pattern` | `str \| re.Pattern[str] \| None` | No | Regex to use for extracting links from raw HTML. (default: `None`) |

## Returns

`list[str]`

A list of all links found in the HTML.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/utils/html.py#L46)
