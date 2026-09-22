---
title: "from_examples"
description: "Create k-shot example selector using example list and embeddings."
source: "https://reference.langchain.com/python/langchain-core/example_selectors/semantic_similarity/MaxMarginalRelevanceExampleSelector/from_examples"
category: "reference"
tags: [reference, langchain-core, example_selectors, semantic_similarity, maxmarginalrelevanceexampleselector, from_examples]
---

# from_examples

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/example_selectors/semantic_similarity/MaxMarginalRelevanceExampleSelector/from_examples)

Create k-shot example selector using example list and embeddings.

Reshuffles examples dynamically based on Max Marginal Relevance.

## Signature

```python
from_examples(
    cls,
    examples: list[dict[str, str]],
    embeddings: Embeddings,
    vectorstore_cls: type[VectorStore],
    k: int = 4,
    input_keys: list[str] | None = None,
    fetch_k: int = 20,
    example_keys: list[str] | None = None,
    vectorstore_kwargs: dict[str, Any] | None = None,
    **vectorstore_cls_kwargs: Any = {},
) -> MaxMarginalRelevanceExampleSelector
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `examples` | `list[dict[str, str]]` | Yes | List of examples to use in the prompt. |
| `embeddings` | `Embeddings` | Yes | An initialized embedding API interface, e.g. OpenAIEmbeddings(). |
| `vectorstore_cls` | `type[VectorStore]` | Yes | A vector store DB interface class, e.g. FAISS. |
| `k` | `int` | No | Number of examples to select. (default: `4`) |
| `fetch_k` | `int` | No | Number of `Document` objects to fetch to pass to MMR algorithm. (default: `20`) |
| `input_keys` | `list[str] \| None` | No | If provided, the search is based on the input variables instead of all variables. (default: `None`) |
| `example_keys` | `list[str] \| None` | No | If provided, keys to filter examples to. (default: `None`) |
| `vectorstore_kwargs` | `dict[str, Any] \| None` | No | Extra arguments passed to similarity_search function of the `VectorStore`. (default: `None`) |
| `vectorstore_cls_kwargs` | `Any` | No | optional kwargs containing url for vector store (default: `{}`) |

## Returns

`MaxMarginalRelevanceExampleSelector`

The ExampleSelector instantiated, backed by a vector store.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/example_selectors/semantic_similarity.py#L275)
