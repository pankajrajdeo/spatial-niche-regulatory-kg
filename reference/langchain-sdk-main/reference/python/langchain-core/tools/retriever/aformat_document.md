---
title: "aformat_document"
description: "Async format a document into a string based on a prompt template."
source: "https://reference.langchain.com/python/langchain-core/tools/retriever/aformat_document"
category: "reference"
tags: [reference, langchain-core, tools, retriever, aformat_document]
---

# aformat_document

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/base/aformat_document)

Async format a document into a string based on a prompt template.

First, this pulls information from the document from two sources:

1. `page_content`: This takes the information from the `document.page_content` and
    assigns it to a variable named `page_content`.
2. `metadata`: This takes information from `document.metadata` and assigns it to
    variables of the same name.

Those variables are then passed into the `prompt` to produce a formatted string.

## Signature

```python
aformat_document(
    doc: Document,
    prompt: BasePromptTemplate[str],
) -> str
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `doc` | `Document` | Yes | `Document`, the `page_content` and `metadata` will be used to create the final string. |
| `prompt` | `BasePromptTemplate[str]` | Yes | `BasePromptTemplate`, will be used to format the `page_content` and `metadata` into the final string. |

## Returns

`str`

String of the document formatted.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/prompts/base.py#L487)
