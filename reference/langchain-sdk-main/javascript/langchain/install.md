---
title: "Install LangChain"
description: "To install the LangChain package:"
source: "https://docs.langchain.com/oss/javascript/langchain/install"
category: "docs"
tags: [docs, javascript, langchain, install]
---

# Install LangChain

To install the LangChain package:

**npm**

```bash
npm install langchain @langchain/core
# Requires Node.js 22+
```

**pnpm**

```bash
pnpm add langchain @langchain/core
# Requires Node.js 22+
```

**yarn**

```bash
yarn add langchain @langchain/core
# Requires Node.js 22+
```

**bun**

```bash
bun add langchain @langchain/core
# Requires Bun v1.0.0+
```

LangChain provides integrations to hundreds of LLMs and thousands of other integrations. These live in independent provider packages.

**npm**

```bash
# Installing the OpenAI integration
npm install @langchain/openai
# Installing the Anthropic integration
npm install @langchain/anthropic
```

**pnpm**

```bash
# Installing the OpenAI integration
pnpm install @langchain/openai
# Installing the Anthropic integration
pnpm install @langchain/anthropic
```

**yarn**

```bash
# Installing the OpenAI integration
yarn add @langchain/openai
# Installing the Anthropic integration
yarn add @langchain/anthropic
```

**bun**

```bash
# Installing the OpenAI integration
bun add @langchain/openai
# Installing the Anthropic integration
bun add @langchain/anthropic
```

> [!TIP]
> See the [Integrations tab](../integrations/providers/overview.md) for a full list of available integrations.

Now that you have LangChain installed, you can get started by following the [Quickstart guide](quickstart.md).

> [!TIP]
> Set up [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-langchain-install) tracing to debug your first LangChain app. Follow the [tracing quickstart](../../langsmith/trace-with-langchain.md) to get started. We recommend you also set up [LangSmith Engine](../../langsmith/engine.md) which monitors your traces, detects issues, and proposes fixes.

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/install.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
