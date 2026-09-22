---
title: "ChatXAI integration"
description: "Integrate with the ChatXAI chat model using LangChain JavaScript."
source: "https://docs.langchain.com/oss/javascript/integrations/chat/xai"
category: "docs"
tags: [docs, javascript, integrations, chat, xai]
---

# ChatXAI integration

> Integrate with the ChatXAI chat model using LangChain JavaScript.

> [!WARNING]
> This page documents Grok models from [xAI](https://docs.x.ai/docs/overview). Do not confuse xAI with [Groq](https://console.groq.com/docs/overview), a separate inference provider. See the [Groq integration](groq.md).

[xAI](https://x.ai/) develops Grok chat models. See the [xAI model documentation](https://docs.x.ai/docs/models) for available model IDs.

This guide will help you getting started with `ChatXAI` [chat models](../../langchain/models.md). For detailed documentation of all `ChatXAI` features and configurations head to the [API reference](https://reference.langchain.com/javascript/langchain-xai/ChatXAI).

## Overview

### Integration details

| Class                                                                         | Package                                                          | Serializable | [PY support](https://python.langchain.com/docs/integrations/chat/xai/) |                                            Downloads                                           |                                           Version                                           |
| :---------------------------------------------------------------------------- | :--------------------------------------------------------------- | :----------: | :--------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------: |
| [`ChatXAI`](https://reference.langchain.com/javascript/langchain-xai/ChatXAI) | [`@langchain/xai`](https://www.npmjs.com/package/@langchain/xai) |       ✅      |                                    ✅                                   | ![NPM - Downloads](https://img.shields.io/npm/dm/@langchain/xai?style=flat-square\&label=%20&) | ![NPM - Version](https://img.shields.io/npm/v/@langchain/xai?style=flat-square\&label=%20&) |

### Model features

See the links in the table headers below for guides on how to use specific features.

| [Tool calling](../../langchain/tools.md) | [Structured output](../../langchain/structured-output.md) | [Image input](../../langchain/messages.md#multimodal) | Audio input | Video input | [Token-level streaming](../../langchain/streaming.md) | [Token usage](../../langchain/models.md#token-usage) | [Logprobs](../../langchain/models.md#log-probabilities) |
| :---------------------------------------------: | :--------------------------------------------------------------: | :----------------------------------------------------------: | :---------: | :---------: | :-----------------------------------------------------------: | :---------------------------------------------------------: | :------------------------------------------------------------: |
|                        ✅                        |                                 ✅                                |                               ❌                              |      ❌      |      ❌      |                               ✅                               |                              ✅                              |                                ✅                               |

## Setup

To access `ChatXAI` models, create an xAI account, [get an API key](https://console.x.ai/), and install the `@langchain/xai` integration package.

### Credentials

Head to [the xAI website](https://x.ai) to sign up and generate an API key. Set the `XAI_API_KEY` environment variable:

```bash
export XAI_API_KEY="your-api-key"
```

If you want to get automated tracing of your model calls you can also set your [LangSmith](../../../langsmith/observability.md) API key by uncommenting below:

```bash
# export LANGSMITH_TRACING="true"
# export LANGSMITH_API_KEY="your-api-key"
```

### Installation

The LangChain `ChatXAI` integration lives in the `@langchain/xai` package:

**npm**

```bash
npm install @langchain/xai @langchain/core
```

**yarn**

```bash
yarn add @langchain/xai @langchain/core
```

**pnpm**

```bash
pnpm add @langchain/xai @langchain/core
```

## Instantiation

Now we can instantiate our model object and generate chat completions:

```typescript
import { ChatXAI } from "@langchain/xai";

const llm = new ChatXAI({
    model: "grok-3-fast",
    temperature: 0,
    maxTokens: undefined,
    maxRetries: 2,
    // other params...
})
```

## Invocation

```typescript
const aiMsg = await llm.invoke([
    [
      "system",
      "You are a helpful assistant that translates English to French. Translate the user sentence.",
    ],
    ["human", "I love programming."],
])
console.log(aiMsg)
```

```text
AIMessage {
  "id": "71d7e3d8-30dd-472c-8038-b6b283dcee63",
  "content": "J'adore programmer.",
  "additional_kwargs": {},
  "response_metadata": {
    "tokenUsage": {
      "promptTokens": 30,
      "completionTokens": 6,
      "totalTokens": 36
    },
    "finish_reason": "stop",
    "usage": {
      "prompt_tokens": 30,
      "completion_tokens": 6,
      "total_tokens": 36
    },
    "system_fingerprint": "fp_3e3898d4ce"
  },
  "tool_calls": [],
  "invalid_tool_calls": [],
  "usage_metadata": {
    "output_tokens": 6,
    "input_tokens": 30,
    "total_tokens": 36,
    "input_token_details": {},
    "output_token_details": {}
  }
}
```

```typescript
console.log(aiMsg.content)
```

```text
J'adore programmer.
```

***

## API reference

For detailed documentation of all `ChatXAI` features and configurations head to the [API reference](https://reference.langchain.com/javascript/langchain-xai/ChatXAI).

***

> [!NOTE]
> [Connect these docs](../../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/chat/xai.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
