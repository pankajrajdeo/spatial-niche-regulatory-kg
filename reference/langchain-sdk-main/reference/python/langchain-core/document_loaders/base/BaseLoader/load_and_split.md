---
title: "load_and_split"
description: "Load Document and split into chunks. Chunks are returned as Document."
source: "https://reference.langchain.com/python/langchain-core/document_loaders/base/BaseLoader/load_and_split"
category: "reference"
tags: [reference, langchain-core, document_loaders, base, baseloader, load_and_split]
---

# load_and_split

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/document_loaders/base/BaseLoader/load_and_split)

Load `Document` and split into chunks. Chunks are returned as `Document`.

!!! danger

    Do not override this method. It should be considered to be deprecated!

## Signature

```python
load_and_split(
    self,
    text_splitter: TextSplitter | None = None,
) -> list[Document]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text_splitter` | `TextSplitter \| None` | No | `TextSplitter` instance to use for splitting documents.  Defaults to `RecursiveCharacterTextSplitter`. (default: `None`) |

## Returns

`list[Document]`

List of `Document` objects.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/document_loaders/base.py#L53)
