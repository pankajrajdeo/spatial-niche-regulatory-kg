---
title: "extract_sub_links"
description: "Extract all links from a raw HTML string and convert into absolute paths."
source: "https://reference.langchain.com/python/langchain-core/utils/html/extract_sub_links"
category: "reference"
tags: [reference, langchain-core, utils, html, extract_sub_links]
---

# extract_sub_links

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/html/extract_sub_links)

Extract all links from a raw HTML string and convert into absolute paths.

## Signature

```python
extract_sub_links(
    raw_html: str,
    url: str,
    *,
    base_url: str | None = None,
    pattern: str | re.Pattern[str] | None = None,
    prevent_outside: bool = True,
    exclude_prefixes: Sequence[str] = (),
    continue_on_failure: bool = False,
) -> list[str]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `raw_html` | `str` | Yes | Original HTML. |
| `url` | `str` | Yes | The url of the HTML. |
| `base_url` | `str \| None` | No | the base URL to check for outside links against. (default: `None`) |
| `pattern` | `str \| re.Pattern[str] \| None` | No | Regex to use for extracting links from raw HTML. (default: `None`) |
| `prevent_outside` | `bool` | No | If `True`, ignore external links which are not children of the base URL. (default: `True`) |
| `exclude_prefixes` | `Sequence[str]` | No | Exclude any URLs that start with one of these prefixes. (default: `()`) |
| `continue_on_failure` | `bool` | No | If `True`, continue if parsing a specific link raises an exception. Otherwise, raise the exception. (default: `False`) |

## Returns

`list[str]`

A list of absolute paths to sub links.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/utils/html.py#L62)
