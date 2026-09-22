---
title: "any-llm integrations"
description: "Integrate with any-llm using LangChain Python."
source: "https://docs.langchain.com/oss/python/integrations/providers/anyllm"
category: "docs"
tags: [docs, integrations, providers, anyllm]
---

# any-llm integrations

> Integrate with any-llm using LangChain Python.

> [any-llm](https://github.com/mozilla-ai/any-llm) is a unified interface for calling OpenAI, Anthropic, Google, local models (via Ollama/LocalAI), and [more](https://mozilla-ai.github.io/any-llm/providers/). Switch between providers just by changing a string.

## Installation and setup

**pip**

```bash
pip install langchain-anyllm
```

**uv**

```bash
uv add langchain-anyllm
```

You need the appropriate API key for your chosen provider. API keys can be passed via the `api_key` parameter or set as environment variables (e.g., `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`). See the [any-llm documentation](https://mozilla-ai.github.io/any-llm/providers/) for provider-specific requirements.

## Chat models

```python
from langchain_anyllm import ChatAnyLLM
```

***

## API reference

For detailed documentation of all `ChatAnyLLM` features and configurations, head to the API reference: [https://github.com/mozilla-ai/langchain-any-llm](https://github.com/mozilla-ai/langchain-any-llm)

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/anyllm.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
