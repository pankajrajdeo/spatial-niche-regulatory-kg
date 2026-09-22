---
title: "MistralAI integrations"
description: "Integrate with MistralAI using LangChain Python."
source: "https://docs.langchain.com/oss/python/integrations/providers/mistralai"
category: "docs"
tags: [docs, integrations, providers, mistralai]
---

# MistralAI integrations

> Integrate with MistralAI using LangChain Python.

> [Mistral AI](https://docs.mistral.ai/api/) is a platform that offers hosting for their powerful open source models.

## Installation and setup

A valid [API key](https://console.mistral.ai/users/api-keys/) is needed to communicate with the API.

You will also need the `langchain-mistralai` package:

**pip**

```bash
pip install langchain-mistralai
```

**uv**

```bash
uv add langchain-mistralai
```

## Chat models

### ChatMistralAI

See a [usage example](../chat/mistralai.md).

```python
from langchain_mistralai.chat_models import ChatMistralAI
```

## Embedding models

### MistralAIEmbeddings

See a [usage example](../embeddings/mistralai.md).

```python
from langchain_mistralai import MistralAIEmbeddings
```

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/mistralai.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
