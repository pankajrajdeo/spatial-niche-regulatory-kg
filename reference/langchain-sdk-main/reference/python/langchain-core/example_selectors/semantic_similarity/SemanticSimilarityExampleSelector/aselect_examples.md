---
title: "aselect_examples"
description: "Asynchronously select examples based on semantic similarity."
source: "https://reference.langchain.com/python/langchain-core/example_selectors/semantic_similarity/SemanticSimilarityExampleSelector/aselect_examples"
category: "reference"
tags: [reference, langchain-core, example_selectors, semantic_similarity, semanticsimilarityexampleselector, aselect_examples]
---

# aselect_examples

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/example_selectors/semantic_similarity/SemanticSimilarityExampleSelector/aselect_examples)

Asynchronously select examples based on semantic similarity.

## Signature

```python
aselect_examples(
    self,
    input_variables: dict[str, str],
) -> list[dict[str, Any]]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `input_variables` | `dict[str, str]` | Yes | The input variables to use for search. |

## Returns

`list[dict[str, Any]]`

The selected examples.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/example_selectors/semantic_similarity.py#L122)
