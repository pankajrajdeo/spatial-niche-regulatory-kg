---
title: "Anthropic integrations"
description: "Integrate with Anthropic using LangChain JavaScript."
source: "https://docs.langchain.com/oss/javascript/integrations/providers/anthropic"
category: "docs"
tags: [docs, javascript, integrations, providers, anthropic]
---

# Anthropic integrations

> Integrate with Anthropic using LangChain JavaScript.

All functionality related to Anthropic models.

[Anthropic](https://www.anthropic.com/) is an AI safety and research company, and is the creator of Claude.
This page covers all integrations between Anthropic models and LangChain.

## Prompting best practices

Anthropic models have several prompting best practices compared to OpenAI models.

**System Messages may only be the first message**

Anthropic models require any system messages to be the first one in your prompts.

## `ChatAnthropic`

`ChatAnthropic` is a subclass of LangChain's `ChatModel`, meaning it works best with `ChatPromptTemplate`.
You can import this wrapper with the following code:

> [!TIP]
> See [this section for general instructions on installing LangChain packages](../../langchain/install.md).

**npm**

```bash
npm install @langchain/anthropic @langchain/core
```

```typescript
import { ChatAnthropic } from "@langchain/anthropic";
const model = new ChatAnthropic({});
```

When working with ChatModels, it is preferred that you design your prompts as `ChatPromptTemplate`s.
Here is an example below of doing that:

```typescript
import { ChatPromptTemplate } from "@langchain/classic/prompts";

const prompt = ChatPromptTemplate.fromMessages([
  ["system", "You are a helpful chatbot"],
  ["human", "Tell me a joke about {topic}"],
]);
```

You can then use this in a chain as follows:

```typescript
const chain = prompt.pipe(model);
await chain.invoke({ topic: "bears" });
```

See the [chat model integration page](../chat/anthropic.md) for more examples, including multimodal inputs.

***

> [!NOTE]
> [Connect these docs](../../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/providers/anthropic.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
