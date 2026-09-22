---
title: "Hugging Face integrations"
description: "Integrate with Hugging Face using LangChain Python."
source: "https://docs.langchain.com/oss/python/integrations/providers/huggingface"
category: "docs"
tags: [docs, integrations, providers, huggingface]
---

# Hugging Face integrations

> Integrate with Hugging Face using LangChain Python.

This page covers all LangChain integrations with [Hugging Face Hub](https://huggingface.co/) and libraries like [transformers](https://huggingface.co/docs/transformers/index), [sentence transformers](https://sbert.net/), and [datasets](https://huggingface.co/docs/datasets/index).

## Chat models

### ChatHuggingFace

We can use the `Hugging Face` LLM classes or directly use the `ChatHuggingFace` class.

See a [usage example](../chat/huggingface.md).

```python
from langchain_huggingface import ChatHuggingFace
```

## LLMs

### HuggingFaceEndpoint

We can use the `HuggingFaceEndpoint` class to run open source models via serverless [Inference Providers](https://huggingface.co/docs/inference-providers) or via dedicated [Inference Endpoints](https://huggingface.co/inference-endpoints/dedicated).

See a [usage example](../llms/huggingface_endpoint.md).

```python
from langchain_huggingface import HuggingFaceEndpoint
```

### HuggingFacePipeline

We can use the `HuggingFacePipeline` class to run open source models locally.

See a [usage example](../llms/huggingface_pipelines.md).

```python
from langchain_huggingface import HuggingFacePipeline
```

## Embedding models

### HuggingFaceEmbeddings

We can use the `HuggingFaceEmbeddings` class to run open source embedding models locally.

See a [usage example](../embeddings/huggingfacehub.md).

```python
from langchain_huggingface import HuggingFaceEmbeddings
```

### HuggingFaceEndpointEmbeddings

We can use the `HuggingFaceEndpointEmbeddings` class to run open source embedding models via a dedicated [Inference Endpoint](https://huggingface.co/inference-endpoints/dedicated).

See a [usage example](../embeddings/huggingfacehub.md).

```python
from langchain_huggingface import HuggingFaceEndpointEmbeddings
```

### Text Embeddings Inference (TEI)

For self-hosted production serving of Sentence Transformers models, Hugging Face publishes [Text Embeddings Inference](https://github.com/huggingface/text-embeddings-inference), a dedicated inference server with batching and GPU support. TEI exposes an OpenAI-compatible API, so point LangChain at a TEI deployment via `OpenAIEmbeddings`. See the dedicated [TEI integration guide](../embeddings/text_embeddings_inference.md).

### BGE embedding models

> [BGE models on Hugging Face](https://huggingface.co/BAAI) are a strong open-source embedding family from the [Beijing Academy of Artificial Intelligence (BAAI)](https://en.wikipedia.org/wiki/Beijing_Academy_of_Artificial_Intelligence).

BGE models are Sentence Transformers models, so use `HuggingFaceEmbeddings` with `encode_kwargs={"normalize_embeddings": True}`. See a [usage example](../embeddings/bge_huggingface.md).

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/huggingface.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
