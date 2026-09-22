---
title: "Prediction guard integrations"
description: "Integrate with Prediction guard using LangChain Python."
source: "https://docs.langchain.com/oss/python/integrations/providers/predictionguard"
category: "docs"
tags: [docs, integrations, providers, predictionguard]
---

# Prediction guard integrations

> Integrate with Prediction guard using LangChain Python.

This page covers how to use the Prediction Guard ecosystem within LangChain.
It is broken into two parts: installation and setup, and then references to specific Prediction Guard wrappers.

This integration is maintained in the [langchain-predictionguard](https://github.com/predictionguard/langchain-predictionguard)
package.

## Installation and setup

* Install the PredictionGuard LangChain partner package:

**pip**

```bash
pip install langchain-predictionguard
```

**uv**

```bash
uv add langchain-predictionguard
```

* Get a Prediction Guard API key (as described in the [Prediction Guard documentation](https://docs.predictionguard.com/)) and set it as an environment variable (`PREDICTIONGUARD_API_KEY`)

## Prediction guard LangChain integrations

| API            | Description             | Endpoint Docs                                                                           | Import                                                            | Example Usage                                                                                         |
| -------------- | ----------------------- | --------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Chat           | Build Chat Bots         | [Chat](https://docs.predictionguard.com/api-reference/api-reference/chat-completions)   | `from langchain_predictionguard import ChatPredictionGuard`       | [`langchain-predictionguard`](https://github.com/predictionguard/langchain-predictionguard)           |
| Completions    | Generate Text           | [Completions](https://docs.predictionguard.com/api-reference/api-reference/completions) | `from langchain_predictionguard import PredictionGuard`           | [PredictionGuard.ipynb](../llms/predictionguard.md)                                |
| Text Embedding | Embed String to Vectors | [Embeddings](https://docs.predictionguard.com/api-reference/api-reference/embeddings)   | `from langchain_predictionguard import PredictionGuardEmbeddings` | [PredictionGuard embeddings](https://docs.predictionguard.com/api-reference/api-reference/embeddings) |

## Getting started

## Chat models

### Prediction guard chat

See a [usage example](https://github.com/predictionguard/langchain-predictionguard)

```python
from langchain_predictionguard import ChatPredictionGuard
```

#### Usage

```python
# If predictionguard_api_key is not passed, default behavior is to use the `PREDICTIONGUARD_API_KEY` environment variable.
chat = ChatPredictionGuard(model="Hermes-3-Llama-3.1-8B")

chat.invoke("Tell me a joke")
```

## Embedding models

### Prediction guard embeddings

See a [usage example](https://docs.predictionguard.com/api-reference/api-reference/embeddings)

```python
from langchain_predictionguard import PredictionGuardEmbeddings
```

#### Usage

```python
# If predictionguard_api_key is not passed, default behavior is to use the `PREDICTIONGUARD_API_KEY` environment variable.
embeddings = PredictionGuardEmbeddings(model="bridgetower-large-itm-mlm-itc")

text = "This is an embedding example."
output = embeddings.embed_query(text)
```

## LLMs

### Prediction guard LLM

See a [usage example](../llms/predictionguard.md)

```python
from langchain_predictionguard import PredictionGuard
```

#### Usage

```python
# If predictionguard_api_key is not passed, default behavior is to use the `PREDICTIONGUARD_API_KEY` environment variable.
llm = PredictionGuard(model="Hermes-2-Pro-Llama-3-8B")

llm.invoke("Tell me a joke about bears")
```

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/predictionguard.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
