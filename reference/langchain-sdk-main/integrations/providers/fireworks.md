---
title: "Fireworks integrations"
description: "Integrate with Fireworks AI using LangChain Python."
source: "https://docs.langchain.com/oss/python/integrations/providers/fireworks"
category: "docs"
tags: [docs, integrations, providers, fireworks]
---

# Fireworks integrations

> Integrate with Fireworks AI using LangChain Python.

[Fireworks AI](https://fireworks.ai/) hosts open and proprietary language models with fast inference. The `langchain-fireworks` package implements LangChain chat and embedding interfaces for the Fireworks API.

## Installation and setup

**pip**

```bash
pip install langchain-fireworks
```

**uv**

```bash
uv add langchain-fireworks
```

Get an API key from [fireworks.ai](https://app.fireworks.ai/login) and set the `FIREWORKS_API_KEY` environment variable.

## Model interfaces

#### [ChatFireworks](../chat/fireworks.md)
Interface to chat models hosted on Fireworks AI.

#### [FireworksEmbeddings](../embeddings/fireworks.md)
Embedding models served by Fireworks AI.

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/fireworks.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
