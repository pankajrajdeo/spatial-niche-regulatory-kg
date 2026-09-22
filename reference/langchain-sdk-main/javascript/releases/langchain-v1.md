---
title: "What's new in LangChain v1"
description: "LangChain v1 is a focused, production-ready foundation for building agents. We've streamlined the framework around three core improvements:"
source: "https://docs.langchain.com/oss/javascript/releases/langchain-v1"
category: "docs"
tags: [docs, javascript, releases, langchain-v1]
---

# What's new in LangChain v1

**LangChain v1 is a focused, production-ready foundation for building agents.** We've streamlined the framework around three core improvements:

#### [createAgent](#createagent)
A new standard way to build agents in LangChain, replacing `createReactAgent` from LangGraph with a cleaner, more powerful API.

#### [Standard content blocks](#standard-content-blocks)
A new `contentBlocks` property that provides unified access to modern LLM features across all providers.

#### [Simplified package](#simplified-package)
The `langchain` package has been streamlined to focus on essential building blocks for agents, with legacy functionality moved to `@langchain/classic`.

To upgrade,

**npm**

```bash
npm install langchain @langchain/core
```

**pnpm**

```bash
pnpm install langchain @langchain/core
```

**yarn**

```bash
yarn add langchain @langchain/core
```

**bun**

```bash
bun add langchain @langchain/core
```

For a complete list of changes, see the [migration guide](../migrate/langchain-v1.md).

## `createAgent`

`createAgent` is the standard way to build agents in LangChain 1.0. It provides a simpler interface than the prebuilt `createReactAgent` exported from LangGraph while offering greater customization potential by using middleware.

```ts
import { createAgent } from "langchain";

const agent = createAgent({
  model: "claude-sonnet-4-6",
  tools: [getWeather],
  systemPrompt: "You are a helpful assistant.",
});

const result = await agent.invoke({
  messages: [
    { role: "user", content: "What is the weather in Tokyo?" },
  ],
});

console.log(result.content);
```

Under the hood, `createAgent` is built on the basic agent loop -- calling a model, letting it choose tools to execute, and then finishing when it calls no more tools:

<img src="https://mintcdn.com/langchain-5e9cc07a/Tazq8zGc0yYUYrDl/oss/images/core_agent_loop.png?fit=max&auto=format&n=Tazq8zGc0yYUYrDl&q=85&s=ac72e48317a9ced68fd1be64e89ec063" alt="Core agent loop diagram" width="300" height="268" data-path="oss/images/core_agent_loop.png" />

For more information, see [Agents](../langchain/agents.md).

### Middleware

Middleware is the defining feature of `createAgent`. It makes `createAgent` highly customizable, raising the ceiling for what you can build.

Great agents require [context engineering](../langchain/context-engineering.md): getting the right information to the model at the right time. Middleware helps you control dynamic prompts, conversation summarization, selective tool access, state management, and guardrails through a composable abstraction.

#### Prebuilt middleware

LangChain provides a few [prebuilt middlewares](../langchain/middleware.md#built-in-middleware) for common patterns, including:

* `summarizationMiddleware`: Condense conversation history when it gets too long
* `humanInTheLoopMiddleware`: Require approval for sensitive tool calls
* `piiRedactionMiddleware`: Redact sensitive information before sending to the model

```ts
import {
  createAgent,
  summarizationMiddleware,
  humanInTheLoopMiddleware,
  piiRedactionMiddleware,
} from "langchain";

const agent = createAgent({
  model: "claude-sonnet-4-6",
  tools: [readEmail, sendEmail],
  middleware: [
    piiRedactionMiddleware({ patterns: ["email", "phone", "ssn"] }),
    summarizationMiddleware({
      model: "claude-sonnet-4-6",
      trigger: { tokens: 500 },
    }),
    humanInTheLoopMiddleware({
      interruptOn: {
        sendEmail: {
          allowedDecisions: ["approve", "edit", "reject"],
        },
      },
    }),
  ],
});
```

#### Custom middleware

You can also build custom middleware to fit your specific needs.

Build custom middleware by implementing any of these hooks using the `createMiddleware` function:

| Hook            | When it runs             | Use cases                               |
| --------------- | ------------------------ | --------------------------------------- |
| `beforeAgent`   | Before calling the agent | Load memory, validate input             |
| `beforeModel`   | Before each LLM call     | Update prompts, trim messages           |
| `wrapModelCall` | Around each LLM call     | Intercept and modify requests/responses |
| `wrapToolCall`  | Around each tool call    | Intercept and modify tool execution     |
| `afterModel`    | After each LLM response  | Validate output, apply guardrails       |
| `afterAgent`    | After agent completes    | Save results, cleanup                   |

<img src="https://mintcdn.com/langchain-5e9cc07a/RAP6mjwE5G00xYsA/oss/images/middleware_final.png?fit=max&auto=format&n=RAP6mjwE5G00xYsA&q=85&s=eb4404b137edec6f6f0c8ccb8323eaf1" alt="Middleware flow diagram" width="500" height="560" data-path="oss/images/middleware_final.png" />

Example custom middleware:

```ts
import { createMiddleware } from "langchain";

const contextSchema = z.object({
  userExpertise: z.enum(["beginner", "expert"]).default("beginner"),
})

const expertiseBasedToolMiddleware = createMiddleware({
  wrapModelCall: async (request, handler) => {
    const userLevel = request.runtime.context.userExpertise;
    if (userLevel === "expert") {
      const tools = [advancedSearch, dataAnalysis];
      return handler(
        request.replace("openai:gpt-5.5", tools)
      );
    }
    const tools = [simpleSearch, basicCalculator];
    return handler(
      request.replace("openai:gpt-5-nano", tools)
    );
  },
});

const agent = createAgent({
  model: "claude-sonnet-4-6",
  tools: [simpleSearch, advancedSearch, basicCalculator, dataAnalysis],
  middleware: [expertiseBasedToolMiddleware],
  contextSchema,
});
```

For more information, see [the complete middleware guide](../langchain/middleware.md).

### Built on LangGraph

Because `createAgent` is built on LangGraph, you automatically get built in support for long running and reliable agents via:

#### Persistence
Conversations automatically persist across sessions with built-in checkpointing

#### Streaming
Stream tokens, tool calls, and reasoning traces in real-time

#### Human-in-the-loop
Pause agent execution for human approval before sensitive actions

#### Time travel
Rewind conversations to any point and explore alternate paths and prompts

You don't need to learn LangGraph to use these features—they work out of the box.

### Structured output

`createAgent` has improved structured output generation:

* **Main loop integration**: Structured output is now generated in the main loop instead of requiring an additional LLM call
* **Structured output strategy**: Models can choose between calling tools or using provider-side structured output generation
* **Cost reduction**: Eliminates extra expense from additional LLM calls

```ts
import { createAgent } from "langchain";
import * as z from "zod";

const weatherSchema = z.object({
  temperature: z.number(),
  condition: z.string(),
});

const agent = createAgent({
  model: "gpt-5.4-mini",
  tools: [getWeather],
  responseFormat: weatherSchema,
});

const result = await agent.invoke({
  messages: [
    { role: "user", content: "What is the weather in Tokyo?" },
  ],
});

console.log(result.structuredResponse);
```

**Error handling**: Control error handling via the `handleErrors` parameter to `ToolStrategy`:

* **Parsing errors**: Model generates data that doesn't match desired structure
* **Multiple tool calls**: Model generates 2+ tool calls for structured output schemas

***

## Standard content blocks

> [!NOTE]
> 1.0 releases are available for most packages. Only the following currently support new content blocks:
>
> * `langchain`
> * `@langchain/core`
> * `@langchain/anthropic`
> * `@langchain/openai`
>
> Broader support for content blocks is planned.

### Benefits

* **Provider agnostic**: Access reasoning traces, citations, built-in tools (web search, code interpreters, etc.), and other features using the same API regardless of provider
* **Type safe**: Full type hints for all content block types
* **Backward compatible**: Standard content can be [loaded lazily](../langchain/messages.md#standard-content-blocks), so there are no associated breaking changes

For more information, see our guide on [content blocks](../langchain/messages.md#message-content)

***

## Simplified package

LangChain v1 streamlines the `langchain` package namespace to focus on essential building blocks for agents. The package exposes only the most useful and relevant functionality:

Most of these are re-exported from `@langchain/core` for convenience, which gives you a focused API surface for building agents.

### `@langchain/classic`

Legacy functionality has moved to [`@langchain/classic`](https://www.npmjs.com/package/@langchain/classic) to keep the core package lean and focused.

#### What's in `@langchain/classic`

* Legacy chains and chain implementations
* Retrievers
* The indexing API
* [`@langchain/community`](https://www.npmjs.com/package/@langchain/community) exports
* Other deprecated functionality

If you use any of this functionality, install [`@langchain/classic`](https://www.npmjs.com/package/@langchain/classic):

**npm**

```bash
npm install @langchain/classic
```

**pnpm**

```bash
pnpm install @langchain/classic
```

**yarn**

```bash
yarn add @langchain/classic
```

**bun**

```bash
bun add @langchain/classic
```

Then update your imports:

```typescript
import { ... } from "langchain"; // [!code --]
import { ... } from "@langchain/classic"; // [!code ++]

import { ... } from "langchain/chains"; // [!code --]
import { ... } from "@langchain/classic/chains"; // [!code ++]
```

## Reporting issues

Please report any issues discovered with 1.0 on [GitHub](https://github.com/langchain-ai/langchainjs/issues) using the [`'v1'` label](https://github.com/langchain-ai/langchainjs/issues?q=state%3Aopen%20label%3Av1).

## Additional resources

#### [LangChain 1.0](https://blog.langchain.com/langchain-langchain-1-0-alpha-releases/)
Read the announcement

#### [Middleware guide](https://blog.langchain.com/agent-middleware/)
Deep dive into middleware

#### [Agents Documentation](../langchain/agents.md)
Full agent documentation

#### [Message Content](../langchain/messages.md#message-content)
New content blocks API

#### [Migration guide](../migrate/langchain-v1.md)
How to migrate to LangChain v1

#### [GitHub](https://github.com/langchain-ai/langchainjs)
Report issues or contribute

## See also

* [Versioning](../versioning.md) – Understanding version numbers
* [Release policy](../release-policy.md) – Detailed release policies

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/releases/langchain-v1.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
