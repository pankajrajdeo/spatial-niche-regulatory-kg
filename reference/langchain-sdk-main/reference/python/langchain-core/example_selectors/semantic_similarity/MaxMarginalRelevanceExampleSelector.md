---
title: "MaxMarginalRelevanceExampleSelector"
description: "Select examples based on Max Marginal Relevance."
source: "https://reference.langchain.com/python/langchain-core/example_selectors/semantic_similarity/MaxMarginalRelevanceExampleSelector"
category: "reference"
tags: [reference, langchain-core, example_selectors, semantic_similarity, maxmarginalrelevanceexampleselector]
---

# MaxMarginalRelevanceExampleSelector

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/example_selectors/semantic_similarity/MaxMarginalRelevanceExampleSelector)

Select examples based on Max Marginal Relevance.

This was shown to improve performance in this paper:
https://arxiv.org/pdf/2211.13892.pdf

## Signature

```python
MaxMarginalRelevanceExampleSelector()
```

## Extends

- `_VectorStoreExampleSelector`

## Properties

- `fetch_k`

## Methods

- [`select_examples()`](https://reference.langchain.com/python/langchain-core/example_selectors/semantic_similarity/MaxMarginalRelevanceExampleSelector/select_examples)
- [`aselect_examples()`](https://reference.langchain.com/python/langchain-core/example_selectors/semantic_similarity/MaxMarginalRelevanceExampleSelector/aselect_examples)
- [`from_examples()`](https://reference.langchain.com/python/langchain-core/example_selectors/semantic_similarity/MaxMarginalRelevanceExampleSelector/from_examples)
- [`afrom_examples()`](https://reference.langchain.com/python/langchain-core/example_selectors/semantic_similarity/MaxMarginalRelevanceExampleSelector/afrom_examples)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/example_selectors/semantic_similarity.py#L231)
