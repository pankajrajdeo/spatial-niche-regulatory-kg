---
title: "init_embeddings"
description: "Initialize an embedding model from a model name and optional provider."
source: "https://reference.langchain.com/python/langchain/embeddings/base/init_embeddings"
category: "reference"
tags: [reference, langchain, embeddings, base, init_embeddings]
---

# init_embeddings

> **Function** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/embeddings/base/init_embeddings)

Initialize an embedding model from a model name and optional provider.

!!! note

    Requires the integration package for the chosen model provider to be installed.

    See the `model_provider` parameter below for specific package names
    (e.g., `pip install langchain-openai`).

    Refer to the [provider integration's API reference](../../../../../integrations/providers.md)
    for supported model parameters to use as `**kwargs`.

## Signature

```python
init_embeddings(
    model: str,
    *,
    provider: str | None = None,
    **kwargs: Any = {},
) -> Embeddings
```

## Description

???+ example

```python
    # pip install langchain langchain-openai

    # Using a model string
    model = init_embeddings("openai:text-embedding-3-small")
    model.embed_query("Hello, world!")

    # Using explicit provider
    model = init_embeddings(model="text-embedding-3-small", provider="openai")
    model.embed_documents(["Hello, world!", "Goodbye, world!"])

    # With additional parameters
    model = init_embeddings("openai:text-embedding-3-small", api_key="sk-...")
```

!!! version-added "Added in `langchain` 0.3.9"

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `model` | `str` | Yes | The name of the model, e.g. `'openai:text-embedding-3-small'`.  You can also specify model and model provider in a single argument using `'{model_provider}:{model}'` format, e.g. `'openai:text-embedding-3-small'`. |
| `provider` | `str \| None` | No | The model provider if not specified as part of the model arg (see above).  Supported `provider` values and the corresponding integration package are:  - `openai`                  -> [`langchain-openai`](../../../../../integrations/providers/openai.md) - `azure_ai`                -> [`langchain-azure-ai`](../../../../../integrations/providers/microsoft.md) - `azure_openai`            -> [`langchain-openai`](../../../../../integrations/providers/openai.md) - `bedrock`                 -> [`langchain-aws`](../../../../../integrations/providers/aws.md) - `cohere`                  -> [`langchain-cohere`](../../../../../integrations/providers/cohere.md) - `google_vertexai`         -> [`langchain-google-vertexai`](../../../../../integrations/providers/google.md) - `huggingface`             -> [`langchain-huggingface`](../../../../../integrations/providers/huggingface.md) - `mistralai`               -> [`langchain-mistralai`](../../../../../integrations/providers/mistralai.md) - `ollama`                  -> [`langchain-ollama`](../../../../../integrations/providers/ollama.md) (default: `None`) |
| `**kwargs` | `Any` | No | Additional model-specific parameters passed to the embedding model.  These vary by provider. Refer to the specific model provider's [integration reference](https://reference.langchain.com/python/integrations/) for all available parameters. (default: `{}`) |

## Returns

`Embeddings`

An `Embeddings` instance that can generate embeddings for text.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/embeddings/base.py#L191)
