---
title: "translate_grounding_metadata_to_citations"
description: "Translate Google AI grounding metadata to LangChain Citations."
source: "https://reference.langchain.com/python/langchain-core/messages/block_translators/google_genai/translate_grounding_metadata_to_citations"
category: "reference"
tags: [reference, langchain-core, messages, block_translators, google_genai, translate_grounding_metadata_to_citations]
---

# translate_grounding_metadata_to_citations

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/block_translators/google_genai/translate_grounding_metadata_to_citations)

Translate Google AI grounding metadata to LangChain Citations.

## Signature

```python
translate_grounding_metadata_to_citations(
    grounding_metadata: dict[str, Any],
) -> list[Citation]
```

## Description

**Example:**

>>> metadata = {
...     "web_search_queries": ["UEFA Euro 2024 winner"],
...     "grounding_chunks": [
...         {
...             "web": {
...                 "uri": "https://uefa.com/euro2024",
...                 "title": "UEFA Euro 2024 Results",
...             }
...         }
...     ],
...     "grounding_supports": [
...         {
...             "segment": {
...                 "start_index": 0,
...                 "end_index": 47,
...                 "text": "Spain won the UEFA Euro 2024 championship",
...             },
...             "grounding_chunk_indices": [0],
...         }
...     ],
... }
>>> citations = translate_grounding_metadata_to_citations(metadata)
>>> len(citations)
1
>>> citations[0]["url"]
'https://uefa.com/euro2024'

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `grounding_metadata` | `dict[str, Any]` | Yes | Google AI grounding metadata containing web search queries, grounding chunks, and grounding supports. |

## Returns

`list[Citation]`

List of Citation content blocks derived from the grounding metadata.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/block_translators/google_genai.py#L25)
