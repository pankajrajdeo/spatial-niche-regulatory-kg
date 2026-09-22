---
title: "Install LangChain"
description: "To install the LangChain package:"
source: "https://docs.langchain.com/oss/python/langchain/install"
category: "docs"
tags: [docs, langchain, install]
---

# Install LangChain

To install the LangChain package:

**pip**

```bash
pip install -U langchain
# Requires Python 3.10+
```

**uv**

```bash
uv add langchain
# Requires Python 3.10+
```

LangChain provides integrations to hundreds of LLMs and thousands of other integrations. These live in independent provider packages.

**pip**

```bash
# Installing the OpenAI integration
pip install -U langchain-openai

# Installing the Anthropic integration
pip install -U langchain-anthropic
```

**uv**

```bash
# Installing the OpenAI integration
uv add langchain-openai

# Installing the Anthropic integration
uv add langchain-anthropic
```

> [!TIP]
> See the [Integrations tab](../integrations/providers/overview.md) for a full list of available integrations.

Now that you have LangChain installed, you can get started by following the [Quickstart guide](quickstart.md).

> [!TIP]
> Set up [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-langchain-install) tracing to debug your first LangChain app. Follow the [tracing quickstart](../langsmith/trace-with-langchain.md) to get started. We recommend you also set up [LangSmith Engine](../langsmith/engine.md) which monitors your traces, detects issues, and proposes fixes.

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/install.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
