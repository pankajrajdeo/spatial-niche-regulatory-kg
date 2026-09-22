---
title: "create_citation"
description: "Create a Citation."
source: "https://reference.langchain.com/python/langchain-core/messages/content/create_citation"
category: "reference"
tags: [reference, langchain-core, messages, content, create_citation]
---

# create_citation

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/content/create_citation)

Create a `Citation`.

## Signature

```python
create_citation(
    *,
    url: str | None = None,
    title: str | None = None,
    start_index: int | None = None,
    end_index: int | None = None,
    cited_text: str | None = None,
    id: str | None = None,
    **kwargs: Any = {},
) -> Citation
```

## Description

!!! note

The `id` is generated automatically if not provided, using a UUID4 format
prefixed with `'lc_'` to indicate it is a LangChain-generated ID.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `url` | `str \| None` | No | URL of the document source. (default: `None`) |
| `title` | `str \| None` | No | Source document title. (default: `None`) |
| `start_index` | `int \| None` | No | Start index in the response text where citation applies. (default: `None`) |
| `end_index` | `int \| None` | No | End index in the response text where citation applies. (default: `None`) |
| `cited_text` | `str \| None` | No | Excerpt of source text being cited. (default: `None`) |
| `id` | `str \| None` | No | Content block identifier.  Generated automatically if not provided. (default: `None`) |

## Returns

`Citation`

A properly formatted `Citation`.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/content.py#L1404)
