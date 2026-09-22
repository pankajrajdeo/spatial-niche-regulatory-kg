---
title: "Agents"
description: "An agent is a model calling tools in a loop until a given task is complete."
source: "https://docs.langchain.com/oss/javascript/langchain/agents"
category: "docs"
tags: [docs, javascript, langchain, agents]
---

# Agents

An agent is a model calling tools in a loop until a given task is complete.

<img src="https://mintcdn.com/langchain-5e9cc07a/jtty0O--UJOKG0nK/oss/images/core_agent_loop.svg?fit=max&auto=format&n=jtty0O--UJOKG0nK&q=85&s=4b4cbb497b6273758a565de1bc90ece0" alt="Core agent loop diagram" width="1060" height="760" data-path="oss/images/core_agent_loop.svg" />

A harness is everything around that loop: the prompt, the tools, and any middleware that shapes the model's behavior.

> [!NOTE]
> **Agent = Model + Harness**
>
> The job of a harness: get the model the right context at the right time for the given task.

[`create_agent`](https://reference.langchain.com/javascript/langchain/index/createAgent) is a highly configurable harness. At its simplest, you can create one with:

**Google**

```ts
import { createAgent } from "langchain";

var agent = createAgent({ model: "google-genai:gemini-3.6-flash", tools });
```

**OpenAI**

```ts
import { createAgent } from "langchain";

var agent = createAgent({ model: "openai:gpt-5.5", tools });
```

**Anthropic**

```ts
import { createAgent } from "langchain";

var agent = createAgent({ model: "anthropic:claude-sonnet-5", tools });
```

**OpenRouter**

```ts
import { createAgent } from "langchain";

var agent = createAgent({ model: "openrouter:z-ai/glm-5.2", tools });
```

**Fireworks**

```ts
import { createAgent } from "langchain";

var agent = createAgent({ model: "fireworks:accounts/fireworks/models/glm-5p2", tools });
```

**Baseten**

```ts
import { createAgent } from "langchain";

var agent = createAgent({ model: "baseten:zai-org/GLM-5.2", tools });
```

**Ollama**

```ts
import { createAgent } from "langchain";

var agent = createAgent({ model: "ollama:north-mini-code-1.0", tools });
```

Building on that, you can configure the basics directly with the `model=`, `tools=`, and `system_prompt=` parameters. For more advanced capabilities, extend the harness with [middleware](#configure-the-harness).

> [!TIP]
> [Deep Agents](../deepagents/overview.md) builds on `create_agent` and comes with commonly useful capabilities already assembled, such as planning, file system tools, subagents, and memory. Use `create_agent` when you need to configure the harness yourself.

## Core components

<img src="https://mintcdn.com/langchain-5e9cc07a/jtty0O--UJOKG0nK/oss/images/agent_model_harness.svg?fit=max&auto=format&n=jtty0O--UJOKG0nK&q=85&s=5ac6a7e0343af7cb5ba3ca632e2224af" alt="Agent model and harness components diagram" width="1200" height="760" data-path="oss/images/agent_model_harness.svg" />

### Model

Pass a model identifier string (`"provider:model"`) or an initialized model instance to select the model for your agent. See [Models](models.md) for parameters, provider setup, and dynamic model selection.

**Google**

```ts
import { createAgent } from "langchain";

var agent = createAgent({ model: "google-genai:gemini-3.6-flash", tools });
```

**OpenAI**

```ts
import { createAgent } from "langchain";

var agent = createAgent({ model: "openai:gpt-5.5", tools });
```

**Anthropic**

```ts
import { createAgent } from "langchain";

var agent = createAgent({ model: "anthropic:claude-sonnet-5", tools });
```

**OpenRouter**

```ts
import { createAgent } from "langchain";

var agent = createAgent({ model: "openrouter:z-ai/glm-5.2", tools });
```

**Fireworks**

```ts
import { createAgent } from "langchain";

var agent = createAgent({ model: "fireworks:accounts/fireworks/models/glm-5p2", tools });
```

**Baseten**

```ts
import { createAgent } from "langchain";

var agent = createAgent({ model: "baseten:zai-org/GLM-5.2", tools });
```

**Ollama**

```ts
import { createAgent } from "langchain";

var agent = createAgent({ model: "ollama:north-mini-code-1.0", tools });
```

### Tools

To provide the agent with tools, pass any Python callable, LangChain tool, or tool dict. See [Tools](tools.md) for tool definition, context access, and dynamic tool selection.

**Google**

```ts
import { tool } from "langchain";
import * as z from "zod";

var search = tool(({ query }) => `Results for: ${query}`, {
  name: "search",
  description: "Search for information",
  schema: z.object({ query: z.string() }),
});

var agent = createAgent({ model: "google-genai:gemini-3.6-flash", tools: [search] });
```

**OpenAI**

```ts
import { tool } from "langchain";
import * as z from "zod";

var search = tool(({ query }) => `Results for: ${query}`, {
  name: "search",
  description: "Search for information",
  schema: z.object({ query: z.string() }),
});

var agent = createAgent({ model: "openai:gpt-5.5", tools: [search] });
```

**Anthropic**

```ts
import { tool } from "langchain";
import * as z from "zod";

var search = tool(({ query }) => `Results for: ${query}`, {
  name: "search",
  description: "Search for information",
  schema: z.object({ query: z.string() }),
});

var agent = createAgent({ model: "anthropic:claude-sonnet-5", tools: [search] });
```

**OpenRouter**

```ts
import { tool } from "langchain";
import * as z from "zod";

var search = tool(({ query }) => `Results for: ${query}`, {
  name: "search",
  description: "Search for information",
  schema: z.object({ query: z.string() }),
});

var agent = createAgent({ model: "openrouter:z-ai/glm-5.2", tools: [search] });
```

**Fireworks**

```ts
import { tool } from "langchain";
import * as z from "zod";

var search = tool(({ query }) => `Results for: ${query}`, {
  name: "search",
  description: "Search for information",
  schema: z.object({ query: z.string() }),
});

var agent = createAgent({ model: "fireworks:accounts/fireworks/models/glm-5p2", tools: [search] });
```

**Baseten**

```ts
import { tool } from "langchain";
import * as z from "zod";

var search = tool(({ query }) => `Results for: ${query}`, {
  name: "search",
  description: "Search for information",
  schema: z.object({ query: z.string() }),
});

var agent = createAgent({ model: "baseten:zai-org/GLM-5.2", tools: [search] });
```

**Ollama**

```ts
import { tool } from "langchain";
import * as z from "zod";

var search = tool(({ query }) => `Results for: ${query}`, {
  name: "search",
  description: "Search for information",
  schema: z.object({ query: z.string() }),
});

var agent = createAgent({ model: "ollama:north-mini-code-1.0", tools: [search] });
```

### System prompt

Shape how the agent approaches tasks. The system prompt parameter accepts a string or `SystemMessage`. For dynamic prompts at runtime, use [middleware](middleware.md).

**Google**

```ts
var agent = createAgent({
  model: "google-genai:gemini-3.6-flash",
  tools,
  systemPrompt: "You are a helpful assistant. Be concise and accurate.",
});
```

**OpenAI**

```ts
var agent = createAgent({
  model: "openai:gpt-5.5",
  tools,
  systemPrompt: "You are a helpful assistant. Be concise and accurate.",
});
```

**Anthropic**

```ts
var agent = createAgent({
  model: "anthropic:claude-sonnet-5",
  tools,
  systemPrompt: "You are a helpful assistant. Be concise and accurate.",
});
```

**OpenRouter**

```ts
var agent = createAgent({
  model: "openrouter:z-ai/glm-5.2",
  tools,
  systemPrompt: "You are a helpful assistant. Be concise and accurate.",
});
```

**Fireworks**

```ts
var agent = createAgent({
  model: "fireworks:accounts/fireworks/models/glm-5p2",
  tools,
  systemPrompt: "You are a helpful assistant. Be concise and accurate.",
});
```

**Baseten**

```ts
var agent = createAgent({
  model: "baseten:zai-org/GLM-5.2",
  tools,
  systemPrompt: "You are a helpful assistant. Be concise and accurate.",
});
```

**Ollama**

```ts
var agent = createAgent({
  model: "ollama:north-mini-code-1.0",
  tools,
  systemPrompt: "You are a helpful assistant. Be concise and accurate.",
});
```

### Structured output

Return a validated schema from the agent using `response_format=`. See [Structured output](structured-output.md) for strategies and examples.

**Google**

```ts
const Answer = z.object({ summary: z.string(), confidence: z.number() });

var agent = createAgent({
  model: "google-genai:gemini-3.6-flash",
  tools,
  responseFormat: Answer,
});
const result = await agent.invoke({
  messages: [{ role: "user", content: "Summarize AI trends" }],
});
result.structuredResponse; // { summary: ..., confidence: ... }
```

**OpenAI**

```ts
const Answer = z.object({ summary: z.string(), confidence: z.number() });

var agent = createAgent({
  model: "openai:gpt-5.5",
  tools,
  responseFormat: Answer,
});
const result = await agent.invoke({
  messages: [{ role: "user", content: "Summarize AI trends" }],
});
result.structuredResponse; // { summary: ..., confidence: ... }
```

**Anthropic**

```ts
const Answer = z.object({ summary: z.string(), confidence: z.number() });

var agent = createAgent({
  model: "anthropic:claude-sonnet-5",
  tools,
  responseFormat: Answer,
});
const result = await agent.invoke({
  messages: [{ role: "user", content: "Summarize AI trends" }],
});
result.structuredResponse; // { summary: ..., confidence: ... }
```

**OpenRouter**

```ts
const Answer = z.object({ summary: z.string(), confidence: z.number() });

var agent = createAgent({
  model: "openrouter:z-ai/glm-5.2",
  tools,
  responseFormat: Answer,
});
const result = await agent.invoke({
  messages: [{ role: "user", content: "Summarize AI trends" }],
});
result.structuredResponse; // { summary: ..., confidence: ... }
```

**Fireworks**

```ts
const Answer = z.object({ summary: z.string(), confidence: z.number() });

var agent = createAgent({
  model: "fireworks:accounts/fireworks/models/glm-5p2",
  tools,
  responseFormat: Answer,
});
const result = await agent.invoke({
  messages: [{ role: "user", content: "Summarize AI trends" }],
});
result.structuredResponse; // { summary: ..., confidence: ... }
```

**Baseten**

```ts
const Answer = z.object({ summary: z.string(), confidence: z.number() });

var agent = createAgent({
  model: "baseten:zai-org/GLM-5.2",
  tools,
  responseFormat: Answer,
});
const result = await agent.invoke({
  messages: [{ role: "user", content: "Summarize AI trends" }],
});
result.structuredResponse; // { summary: ..., confidence: ... }
```

**Ollama**

```ts
const Answer = z.object({ summary: z.string(), confidence: z.number() });

var agent = createAgent({
  model: "ollama:north-mini-code-1.0",
  tools,
  responseFormat: Answer,
});
const result = await agent.invoke({
  messages: [{ role: "user", content: "Summarize AI trends" }],
});
result.structuredResponse; // { summary: ..., confidence: ... }
```

### Agent state

Every agent manages its execution context through an `AgentState` object that holds the current conversation history and any custom fields your tools and middleware need.

The built-in field is:

| Field      | Type            | Description                                                                                                |
| ---------- | --------------- | ---------------------------------------------------------------------------------------------------------- |
| `messages` | `BaseMessage[]` | The full conversation history for the current thread. Append-only: new messages are added, never replaced. |

`AgentState` is also the type passed to every node-style middleware hook (`beforeModel`, `afterModel`, and similar). Hooks receive the current state and can return an object of updates to merge back into it.

To add custom fields, define a state schema on your middleware using `stateSchema` with a `StateSchema` or Zod object:

**Google**

```ts
import { createAgent, createMiddleware } from "langchain";
import { StateSchema } from "@langchain/langgraph";
import * as z from "zod";

const MyState = new StateSchema({
  userId: z.string(),
  callCount: z.number().default(0),
});

const stateMiddleware = createMiddleware({
  name: "StateExtension",
  stateSchema: MyState, // [!code highlight]
});

const agent = createAgent({
  model: "google-genai:gemini-3.6-flash",
  tools: [],
  middleware: [stateMiddleware],
});
```

**OpenAI**

```ts
import { createAgent, createMiddleware } from "langchain";
import { StateSchema } from "@langchain/langgraph";
import * as z from "zod";

const MyState = new StateSchema({
  userId: z.string(),
  callCount: z.number().default(0),
});

const stateMiddleware = createMiddleware({
  name: "StateExtension",
  stateSchema: MyState, // [!code highlight]
});

const agent = createAgent({
  model: "openai:gpt-5.5",
  tools: [],
  middleware: [stateMiddleware],
});
```

**Anthropic**

```ts
import { createAgent, createMiddleware } from "langchain";
import { StateSchema } from "@langchain/langgraph";
import * as z from "zod";

const MyState = new StateSchema({
  userId: z.string(),
  callCount: z.number().default(0),
});

const stateMiddleware = createMiddleware({
  name: "StateExtension",
  stateSchema: MyState, // [!code highlight]
});

const agent = createAgent({
  model: "anthropic:claude-sonnet-5",
  tools: [],
  middleware: [stateMiddleware],
});
```

**OpenRouter**

```ts
import { createAgent, createMiddleware } from "langchain";
import { StateSchema } from "@langchain/langgraph";
import * as z from "zod";

const MyState = new StateSchema({
  userId: z.string(),
  callCount: z.number().default(0),
});

const stateMiddleware = createMiddleware({
  name: "StateExtension",
  stateSchema: MyState, // [!code highlight]
});

const agent = createAgent({
  model: "openrouter:z-ai/glm-5.2",
  tools: [],
  middleware: [stateMiddleware],
});
```

**Fireworks**

```ts
import { createAgent, createMiddleware } from "langchain";
import { StateSchema } from "@langchain/langgraph";
import * as z from "zod";

const MyState = new StateSchema({
  userId: z.string(),
  callCount: z.number().default(0),
});

const stateMiddleware = createMiddleware({
  name: "StateExtension",
  stateSchema: MyState, // [!code highlight]
});

const agent = createAgent({
  model: "fireworks:accounts/fireworks/models/glm-5p2",
  tools: [],
  middleware: [stateMiddleware],
});
```

**Baseten**

```ts
import { createAgent, createMiddleware } from "langchain";
import { StateSchema } from "@langchain/langgraph";
import * as z from "zod";

const MyState = new StateSchema({
  userId: z.string(),
  callCount: z.number().default(0),
});

const stateMiddleware = createMiddleware({
  name: "StateExtension",
  stateSchema: MyState, // [!code highlight]
});

const agent = createAgent({
  model: "baseten:zai-org/GLM-5.2",
  tools: [],
  middleware: [stateMiddleware],
});
```

**Ollama**

```ts
import { createAgent, createMiddleware } from "langchain";
import { StateSchema } from "@langchain/langgraph";
import * as z from "zod";

const MyState = new StateSchema({
  userId: z.string(),
  callCount: z.number().default(0),
});

const stateMiddleware = createMiddleware({
  name: "StateExtension",
  stateSchema: MyState, // [!code highlight]
});

const agent = createAgent({
  model: "ollama:north-mini-code-1.0",
  tools: [],
  middleware: [stateMiddleware],
});
```

For full details, examples, and middleware-level state schemas, see [Short-term memory](short-term-memory.md#customizing-agent-memory) and [Custom middleware](middleware/custom.md#state-updates).

## Invocation

> [!TIP]
> Trace each step of this loop, debug tool calls, and evaluate agent outputs with [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-langchain-agents). Follow the [tracing quickstart](../../langsmith/trace-with-langchain.md) to get set up. We recommend you also set up [LangSmith Engine](../../langsmith/engine.md) which monitors your traces, detects issues, and proposes fixes.

You can invoke an agent with a message. Behind the scenes that passes an update to the agent's [`State`](../langgraph/graph-api.md#state). All agents include a [sequence of messages](../langgraph/use-graph-api.md#messagesvalue) in their state; to invoke the agent, pass a new message along with a `thread_id` so the agent can persist and resume conversation history:

**Google**

```ts
import { AIMessage } from "@langchain/core/messages";
import { createAgent } from "langchain";
import { MemorySaver } from "@langchain/langgraph";

const agent = createAgent({
  model: "google-genai:gemini-3.6-flash",
  tools: [],
  checkpointer: new MemorySaver(),
});

const config = { configurable: { thread_id: crypto.randomUUID() } };

let result = await agent.invoke(
  {
    messages: [
      { role: "user", content: "What's the weather in San Francisco?" },
    ],
  },
  config,
);

// A follow-up turn on the same conversation: reuse the same thread_id to keep history
result = await agent.invoke(
  { messages: [{ role: "user", content: "What about tomorrow?" }] },
  config,
);
```

**OpenAI**

```ts
import { AIMessage } from "@langchain/core/messages";
import { createAgent } from "langchain";
import { MemorySaver } from "@langchain/langgraph";

const agent = createAgent({
  model: "openai:gpt-5.5",
  tools: [],
  checkpointer: new MemorySaver(),
});

const config = { configurable: { thread_id: crypto.randomUUID() } };

let result = await agent.invoke(
  {
    messages: [
      { role: "user", content: "What's the weather in San Francisco?" },
    ],
  },
  config,
);

// A follow-up turn on the same conversation: reuse the same thread_id to keep history
result = await agent.invoke(
  { messages: [{ role: "user", content: "What about tomorrow?" }] },
  config,
);
```

**Anthropic**

```ts
import { AIMessage } from "@langchain/core/messages";
import { createAgent } from "langchain";
import { MemorySaver } from "@langchain/langgraph";

const agent = createAgent({
  model: "anthropic:claude-sonnet-5",
  tools: [],
  checkpointer: new MemorySaver(),
});

const config = { configurable: { thread_id: crypto.randomUUID() } };

let result = await agent.invoke(
  {
    messages: [
      { role: "user", content: "What's the weather in San Francisco?" },
    ],
  },
  config,
);

// A follow-up turn on the same conversation: reuse the same thread_id to keep history
result = await agent.invoke(
  { messages: [{ role: "user", content: "What about tomorrow?" }] },
  config,
);
```

**OpenRouter**

```ts
import { AIMessage } from "@langchain/core/messages";
import { createAgent } from "langchain";
import { MemorySaver } from "@langchain/langgraph";

const agent = createAgent({
  model: "openrouter:z-ai/glm-5.2",
  tools: [],
  checkpointer: new MemorySaver(),
});

const config = { configurable: { thread_id: crypto.randomUUID() } };

let result = await agent.invoke(
  {
    messages: [
      { role: "user", content: "What's the weather in San Francisco?" },
    ],
  },
  config,
);

// A follow-up turn on the same conversation: reuse the same thread_id to keep history
result = await agent.invoke(
  { messages: [{ role: "user", content: "What about tomorrow?" }] },
  config,
);
```

**Fireworks**

```ts
import { AIMessage } from "@langchain/core/messages";
import { createAgent } from "langchain";
import { MemorySaver } from "@langchain/langgraph";

const agent = createAgent({
  model: "fireworks:accounts/fireworks/models/glm-5p2",
  tools: [],
  checkpointer: new MemorySaver(),
});

const config = { configurable: { thread_id: crypto.randomUUID() } };

let result = await agent.invoke(
  {
    messages: [
      { role: "user", content: "What's the weather in San Francisco?" },
    ],
  },
  config,
);

// A follow-up turn on the same conversation: reuse the same thread_id to keep history
result = await agent.invoke(
  { messages: [{ role: "user", content: "What about tomorrow?" }] },
  config,
);
```

**Baseten**

```ts
import { AIMessage } from "@langchain/core/messages";
import { createAgent } from "langchain";
import { MemorySaver } from "@langchain/langgraph";

const agent = createAgent({
  model: "baseten:zai-org/GLM-5.2",
  tools: [],
  checkpointer: new MemorySaver(),
});

const config = { configurable: { thread_id: crypto.randomUUID() } };

let result = await agent.invoke(
  {
    messages: [
      { role: "user", content: "What's the weather in San Francisco?" },
    ],
  },
  config,
);

// A follow-up turn on the same conversation: reuse the same thread_id to keep history
result = await agent.invoke(
  { messages: [{ role: "user", content: "What about tomorrow?" }] },
  config,
);
```

**Ollama**

```ts
import { AIMessage } from "@langchain/core/messages";
import { createAgent } from "langchain";
import { MemorySaver } from "@langchain/langgraph";

const agent = createAgent({
  model: "ollama:north-mini-code-1.0",
  tools: [],
  checkpointer: new MemorySaver(),
});

const config = { configurable: { thread_id: crypto.randomUUID() } };

let result = await agent.invoke(
  {
    messages: [
      { role: "user", content: "What's the weather in San Francisco?" },
    ],
  },
  config,
);

// A follow-up turn on the same conversation: reuse the same thread_id to keep history
result = await agent.invoke(
  { messages: [{ role: "user", content: "What about tomorrow?" }] },
  config,
);
```

#### [View example trace](https://smith.langchain.com/public/5e5926b4-3156-477c-83e5-969404aeb92e/r)
Open a public LangSmith run for this example.

> [!NOTE]
> Persisting conversation history with `thread_id` requires the agent to be configured with a [checkpointer](long-term-memory.md). When deployed on [LangSmith](../../langsmith/deployment.md), a checkpointer is provisioned automatically. Locally, pass one explicitly, for example `create_agent(..., checkpointer=InMemorySaver())`.

If you also need to pass per-run configuration (such as a user ID, API keys, or feature flags) to tools and middleware, pass it as `context` alongside the config. Define the shape of that data with `contextSchema` and access it through `runtime.context`:

**Google**

```ts
import * as z from "zod";
import { AIMessage } from "@langchain/core/messages";
import { createAgent } from "langchain";
import { MemorySaver } from "@langchain/langgraph";

const contextSchema = z.object({
  user_id: z.string(),
});

const agent = createAgent({
  model: "google-genai:gemini-3.6-flash",
  tools: [],
  contextSchema,
  checkpointer: new MemorySaver(),
});

const result = await agent.invoke(
  {
    messages: [
      { role: "user", content: "What's the weather in San Francisco?" },
    ],
  },
  {
    configurable: { thread_id: crypto.randomUUID() },
    context: { user_id: "user-123" },
  },
);
```

**OpenAI**

```ts
import * as z from "zod";
import { AIMessage } from "@langchain/core/messages";
import { createAgent } from "langchain";
import { MemorySaver } from "@langchain/langgraph";

const contextSchema = z.object({
  user_id: z.string(),
});

const agent = createAgent({
  model: "openai:gpt-5.5",
  tools: [],
  contextSchema,
  checkpointer: new MemorySaver(),
});

const result = await agent.invoke(
  {
    messages: [
      { role: "user", content: "What's the weather in San Francisco?" },
    ],
  },
  {
    configurable: { thread_id: crypto.randomUUID() },
    context: { user_id: "user-123" },
  },
);
```

**Anthropic**

```ts
import * as z from "zod";
import { AIMessage } from "@langchain/core/messages";
import { createAgent } from "langchain";
import { MemorySaver } from "@langchain/langgraph";

const contextSchema = z.object({
  user_id: z.string(),
});

const agent = createAgent({
  model: "anthropic:claude-sonnet-5",
  tools: [],
  contextSchema,
  checkpointer: new MemorySaver(),
});

const result = await agent.invoke(
  {
    messages: [
      { role: "user", content: "What's the weather in San Francisco?" },
    ],
  },
  {
    configurable: { thread_id: crypto.randomUUID() },
    context: { user_id: "user-123" },
  },
);
```

**OpenRouter**

```ts
import * as z from "zod";
import { AIMessage } from "@langchain/core/messages";
import { createAgent } from "langchain";
import { MemorySaver } from "@langchain/langgraph";

const contextSchema = z.object({
  user_id: z.string(),
});

const agent = createAgent({
  model: "openrouter:z-ai/glm-5.2",
  tools: [],
  contextSchema,
  checkpointer: new MemorySaver(),
});

const result = await agent.invoke(
  {
    messages: [
      { role: "user", content: "What's the weather in San Francisco?" },
    ],
  },
  {
    configurable: { thread_id: crypto.randomUUID() },
    context: { user_id: "user-123" },
  },
);
```

**Fireworks**

```ts
import * as z from "zod";
import { AIMessage } from "@langchain/core/messages";
import { createAgent } from "langchain";
import { MemorySaver } from "@langchain/langgraph";

const contextSchema = z.object({
  user_id: z.string(),
});

const agent = createAgent({
  model: "fireworks:accounts/fireworks/models/glm-5p2",
  tools: [],
  contextSchema,
  checkpointer: new MemorySaver(),
});

const result = await agent.invoke(
  {
    messages: [
      { role: "user", content: "What's the weather in San Francisco?" },
    ],
  },
  {
    configurable: { thread_id: crypto.randomUUID() },
    context: { user_id: "user-123" },
  },
);
```

**Baseten**

```ts
import * as z from "zod";
import { AIMessage } from "@langchain/core/messages";
import { createAgent } from "langchain";
import { MemorySaver } from "@langchain/langgraph";

const contextSchema = z.object({
  user_id: z.string(),
});

const agent = createAgent({
  model: "baseten:zai-org/GLM-5.2",
  tools: [],
  contextSchema,
  checkpointer: new MemorySaver(),
});

const result = await agent.invoke(
  {
    messages: [
      { role: "user", content: "What's the weather in San Francisco?" },
    ],
  },
  {
    configurable: { thread_id: crypto.randomUUID() },
    context: { user_id: "user-123" },
  },
);
```

**Ollama**

```ts
import * as z from "zod";
import { AIMessage } from "@langchain/core/messages";
import { createAgent } from "langchain";
import { MemorySaver } from "@langchain/langgraph";

const contextSchema = z.object({
  user_id: z.string(),
});

const agent = createAgent({
  model: "ollama:north-mini-code-1.0",
  tools: [],
  contextSchema,
  checkpointer: new MemorySaver(),
});

const result = await agent.invoke(
  {
    messages: [
      { role: "user", content: "What's the weather in San Francisco?" },
    ],
  },
  {
    configurable: { thread_id: crypto.randomUUID() },
    context: { user_id: "user-123" },
  },
);
```

#### [View example trace](https://smith.langchain.com/public/8b453131-3d7f-4218-a407-f724b96fb4e7/r)
Open a public LangSmith run for this example.

`thread_id` scopes the *conversation* (message history, checkpoints), while `context` carries *per-run* data your tools and middleware read at invocation time. Both are commonly passed together. See [tool context](tools.md#context) and [Runtime](runtime.md) for more.

## Streaming

`invoke` returns the final response at the end of a run. If an agent executes multiple tool calls, users often need progress updates before completion. Use streaming to surface intermediate messages and tool activity as they happen.

```ts
const stream = await agent.streamEvents(
  {
    messages: [
      {
        role: "user",
        content: "Search for AI news and summarize the findings",
      },
    ],
  },
  { version: "v3" },
);

for await (const snapshot of stream.values) {
  // Each snapshot contains the full state at that point
  const latestMessage = snapshot.messages.at(-1);
  if (latestMessage?.content) {
    if (latestMessage.type === "human") {
      console.log(`User: ${latestMessage.content}`);
    } else if (latestMessage.type === "ai") {
      console.log(`Agent: ${latestMessage.content}`);
    }
  } else if (latestMessage?.tool_calls?.length) {
    const toolCallNames = latestMessage.tool_calls.map((tc) => tc.name);
    console.log(`Calling tools: ${toolCallNames.join(", ")}`);
  }
}
```

#### [View example trace](https://smith.langchain.com/public/311f121f-4400-4709-a202-2f11e972669d/r)
Open a public LangSmith run for this example.

> [!TIP]
> For streaming modes, event types, and UI patterns, see [Streaming](streaming.md).

## Configure the harness

`create_agent` is highly extensible. Middleware is the primitive for customization: each piece handles one concern, hooks into the agent loop at the right moment, and composes freely with any other. Take exactly what your use case needs and skip the rest.

Common patterns are prebuilt as first-class middleware. You can build anything else as [custom middleware](middleware/custom.md).

<img src="https://mintcdn.com/langchain-5e9cc07a/jtty0O--UJOKG0nK/oss/images/agent_harness_capabilities.svg?fit=max&auto=format&n=jtty0O--UJOKG0nK&q=85&s=0ff671d72badd0844826660dfcb04391" alt="Agent harness capabilities by category" width="1500" height="360" data-path="oss/images/agent_harness_capabilities.svg" />

As agents take on complex work, they need support across a few key areas. The middleware ecosystem provides:

#### [Execution environment](#execution-environment)
Tools, filesystem, sandboxes, and code execution

#### [Context management](#context-management)
Summarization, memory, skills, and prompt caching

#### [Planning and delegation](#planning-and-delegation)
Todo lists and subagents for parallel, isolated work

#### [Fault tolerance](#fault-tolerance)
Retries, fallbacks, and call limits

#### [Guardrails](#guardrails)
PII detection and content controls

#### [Steering](#steering)
Human-in-the-loop approval before high-impact actions

> [!TIP]
> `create_deep_agent` pre-assembles this stack for long-running coding and research tasks (filesystem, summarization, subagents, and prompt caching included by default). See [Deep Agents](../deepagents/harness.md) for the full prebuilt harness.

### Execution environment

Agents are especially useful when they can take action rather than just generate text. The execution environment gives the agent a workspace: tools it can call, a filesystem for reading and writing files across turns, and code execution for running scripts or shell commands.

**Google**

```ts
import { createAgent } from "langchain";
import { createFilesystemMiddleware, StateBackend } from "deepagents";

var agent = createAgent({
  model: "google-genai:gemini-3.6-flash",
  tools: [search],
  middleware: [createFilesystemMiddleware({ backend: new StateBackend() })],
});
```

**OpenAI**

```ts
import { createAgent } from "langchain";
import { createFilesystemMiddleware, StateBackend } from "deepagents";

var agent = createAgent({
  model: "openai:gpt-5.5",
  tools: [search],
  middleware: [createFilesystemMiddleware({ backend: new StateBackend() })],
});
```

**Anthropic**

```ts
import { createAgent } from "langchain";
import { createFilesystemMiddleware, StateBackend } from "deepagents";

var agent = createAgent({
  model: "anthropic:claude-sonnet-5",
  tools: [search],
  middleware: [createFilesystemMiddleware({ backend: new StateBackend() })],
});
```

**OpenRouter**

```ts
import { createAgent } from "langchain";
import { createFilesystemMiddleware, StateBackend } from "deepagents";

var agent = createAgent({
  model: "openrouter:z-ai/glm-5.2",
  tools: [search],
  middleware: [createFilesystemMiddleware({ backend: new StateBackend() })],
});
```

**Fireworks**

```ts
import { createAgent } from "langchain";
import { createFilesystemMiddleware, StateBackend } from "deepagents";

var agent = createAgent({
  model: "fireworks:accounts/fireworks/models/glm-5p2",
  tools: [search],
  middleware: [createFilesystemMiddleware({ backend: new StateBackend() })],
});
```

**Baseten**

```ts
import { createAgent } from "langchain";
import { createFilesystemMiddleware, StateBackend } from "deepagents";

var agent = createAgent({
  model: "baseten:zai-org/GLM-5.2",
  tools: [search],
  middleware: [createFilesystemMiddleware({ backend: new StateBackend() })],
});
```

**Ollama**

```ts
import { createAgent } from "langchain";
import { createFilesystemMiddleware, StateBackend } from "deepagents";

var agent = createAgent({
  model: "ollama:north-mini-code-1.0",
  tools: [search],
  middleware: [createFilesystemMiddleware({ backend: new StateBackend() })],
});
```

See [`FilesystemMiddleware`](https://reference.langchain.com/javascript/deepagents/middleware/createFilesystemMiddleware), [Sandboxes](../deepagents/sandboxes.md), [Interpreters](../deepagents/interpreters.md).

> [!NOTE]
> This example imports from the `deepagents` package. Install it with:
>
> **npm**
>
> ```bash
> npm install deepagents
> ```
>
> **yarn**
>
> ```bash
> yarn add deepagents
> ```
>
> **pnpm**
>
> ```bash
> pnpm add deepagents
> ```

### Context management

Every model call has a fixed context window. As an agent runs, that window fills with accumulating history, tool results, and intermediate steps. Summarization compresses history before overflow hits; memory loads persistent instructions at startup so knowledge carries across sessions; skills surface domain knowledge on demand rather than loading everything upfront.

**Google**

```ts
import { createAgent } from "langchain";
import {
  StateBackend,
  createFilesystemMiddleware,
  createSkillsMiddleware,
  createSummarizationMiddleware,
} from "deepagents";

var backend = new StateBackend();
const model = "google-genai:gemini-3.6-flash";

var agent = createAgent({
  model,
  tools: [search],
  middleware: [
    createFilesystemMiddleware({ backend }),
    createSummarizationMiddleware({ model, backend }),
    createSkillsMiddleware({ backend, sources: ["./skills/"] }),
  ],
});
```

**OpenAI**

```ts
import { createAgent } from "langchain";
import {
  StateBackend,
  createFilesystemMiddleware,
  createSkillsMiddleware,
  createSummarizationMiddleware,
} from "deepagents";

var backend = new StateBackend();
const model = "openai:gpt-5.5";

var agent = createAgent({
  model,
  tools: [search],
  middleware: [
    createFilesystemMiddleware({ backend }),
    createSummarizationMiddleware({ model, backend }),
    createSkillsMiddleware({ backend, sources: ["./skills/"] }),
  ],
});
```

**Anthropic**

```ts
import { createAgent } from "langchain";
import {
  StateBackend,
  createFilesystemMiddleware,
  createSkillsMiddleware,
  createSummarizationMiddleware,
} from "deepagents";

var backend = new StateBackend();
const model = "anthropic:claude-sonnet-5";

var agent = createAgent({
  model,
  tools: [search],
  middleware: [
    createFilesystemMiddleware({ backend }),
    createSummarizationMiddleware({ model, backend }),
    createSkillsMiddleware({ backend, sources: ["./skills/"] }),
  ],
});
```

**OpenRouter**

```ts
import { createAgent } from "langchain";
import {
  StateBackend,
  createFilesystemMiddleware,
  createSkillsMiddleware,
  createSummarizationMiddleware,
} from "deepagents";

var backend = new StateBackend();
const model = "openrouter:z-ai/glm-5.2";

var agent = createAgent({
  model,
  tools: [search],
  middleware: [
    createFilesystemMiddleware({ backend }),
    createSummarizationMiddleware({ model, backend }),
    createSkillsMiddleware({ backend, sources: ["./skills/"] }),
  ],
});
```

**Fireworks**

```ts
import { createAgent } from "langchain";
import {
  StateBackend,
  createFilesystemMiddleware,
  createSkillsMiddleware,
  createSummarizationMiddleware,
} from "deepagents";

var backend = new StateBackend();
const model = "fireworks:accounts/fireworks/models/glm-5p2";

var agent = createAgent({
  model,
  tools: [search],
  middleware: [
    createFilesystemMiddleware({ backend }),
    createSummarizationMiddleware({ model, backend }),
    createSkillsMiddleware({ backend, sources: ["./skills/"] }),
  ],
});
```

**Baseten**

```ts
import { createAgent } from "langchain";
import {
  StateBackend,
  createFilesystemMiddleware,
  createSkillsMiddleware,
  createSummarizationMiddleware,
} from "deepagents";

var backend = new StateBackend();
const model = "baseten:zai-org/GLM-5.2";

var agent = createAgent({
  model,
  tools: [search],
  middleware: [
    createFilesystemMiddleware({ backend }),
    createSummarizationMiddleware({ model, backend }),
    createSkillsMiddleware({ backend, sources: ["./skills/"] }),
  ],
});
```

**Ollama**

```ts
import { createAgent } from "langchain";
import {
  StateBackend,
  createFilesystemMiddleware,
  createSkillsMiddleware,
  createSummarizationMiddleware,
} from "deepagents";

var backend = new StateBackend();
const model = "ollama:north-mini-code-1.0";

var agent = createAgent({
  model,
  tools: [search],
  middleware: [
    createFilesystemMiddleware({ backend }),
    createSummarizationMiddleware({ model, backend }),
    createSkillsMiddleware({ backend, sources: ["./skills/"] }),
  ],
});
```

See [`SummarizationMiddleware`](https://reference.langchain.com/javascript/langchain/index/summarizationMiddleware), [`MemoryMiddleware`](https://reference.langchain.com/javascript/deepagents/middleware/createMemoryMiddleware), [Skills](multi-agent/skills.md), [Context engineering](../deepagents/context-engineering.md).

> [!NOTE]
> This example imports from the `deepagents` package. Install it with:
>
> **npm**
>
> ```bash
> npm install deepagents
> ```
>
> **yarn**
>
> ```bash
> yarn add deepagents
> ```
>
> **pnpm**
>
> ```bash
> pnpm add deepagents
> ```

### Planning and delegation

Complex tasks often exceed what one context window can handle. Delegation lets the main agent break work into pieces, hand them to subagents that each run in their own isolated context, and stay focused on coordination rather than execution. Work can run in parallel; the main agent's context stays clean.

**Google**

```ts
import { createAgent, todoListMiddleware, tool } from "langchain";
import {
  createFilesystemMiddleware,
  createSubAgentMiddleware,
  StateBackend,
} from "deepagents";
import * as z from "zod";

var search = tool(({ query }) => `Search results for: ${query}`, {
  name: "search",
  description: "Search for a query and return a short summary.",
  schema: z.object({ query: z.string() }),
});

var backend = new StateBackend();

var agent = createAgent({
  model: "google-genai:gemini-3.6-flash",
  tools: [search],
  middleware: [
    createFilesystemMiddleware({ backend }),
    todoListMiddleware(),
    createSubAgentMiddleware({
      defaultModel: "anthropic:claude-sonnet-4-6",
      defaultTools: [],
      subagents: [
        {
          name: "researcher",
          description: "Searches and returns a structured summary.",
          systemPrompt:
            "Use the search tool to research the question and summarize key points.",
          tools: [search],
          model: "google-genai:gemini-3.6-flash",
          middleware: [],
        },
      ],
    }),
  ],
});
```

**OpenAI**

```ts
import { createAgent, todoListMiddleware, tool } from "langchain";
import {
  createFilesystemMiddleware,
  createSubAgentMiddleware,
  StateBackend,
} from "deepagents";
import * as z from "zod";

var search = tool(({ query }) => `Search results for: ${query}`, {
  name: "search",
  description: "Search for a query and return a short summary.",
  schema: z.object({ query: z.string() }),
});

var backend = new StateBackend();

var agent = createAgent({
  model: "openai:gpt-5.5",
  tools: [search],
  middleware: [
    createFilesystemMiddleware({ backend }),
    todoListMiddleware(),
    createSubAgentMiddleware({
      defaultModel: "anthropic:claude-sonnet-4-6",
      defaultTools: [],
      subagents: [
        {
          name: "researcher",
          description: "Searches and returns a structured summary.",
          systemPrompt:
            "Use the search tool to research the question and summarize key points.",
          tools: [search],
          model: "openai:gpt-5.5",
          middleware: [],
        },
      ],
    }),
  ],
});
```

**Anthropic**

```ts
import { createAgent, todoListMiddleware, tool } from "langchain";
import {
  createFilesystemMiddleware,
  createSubAgentMiddleware,
  StateBackend,
} from "deepagents";
import * as z from "zod";

var search = tool(({ query }) => `Search results for: ${query}`, {
  name: "search",
  description: "Search for a query and return a short summary.",
  schema: z.object({ query: z.string() }),
});

var backend = new StateBackend();

var agent = createAgent({
  model: "anthropic:claude-sonnet-5",
  tools: [search],
  middleware: [
    createFilesystemMiddleware({ backend }),
    todoListMiddleware(),
    createSubAgentMiddleware({
      defaultModel: "anthropic:claude-sonnet-4-6",
      defaultTools: [],
      subagents: [
        {
          name: "researcher",
          description: "Searches and returns a structured summary.",
          systemPrompt:
            "Use the search tool to research the question and summarize key points.",
          tools: [search],
          model: "anthropic:claude-sonnet-5",
          middleware: [],
        },
      ],
    }),
  ],
});
```

**OpenRouter**

```ts
import { createAgent, todoListMiddleware, tool } from "langchain";
import {
  createFilesystemMiddleware,
  createSubAgentMiddleware,
  StateBackend,
} from "deepagents";
import * as z from "zod";

var search = tool(({ query }) => `Search results for: ${query}`, {
  name: "search",
  description: "Search for a query and return a short summary.",
  schema: z.object({ query: z.string() }),
});

var backend = new StateBackend();

var agent = createAgent({
  model: "openrouter:z-ai/glm-5.2",
  tools: [search],
  middleware: [
    createFilesystemMiddleware({ backend }),
    todoListMiddleware(),
    createSubAgentMiddleware({
      defaultModel: "anthropic:claude-sonnet-4-6",
      defaultTools: [],
      subagents: [
        {
          name: "researcher",
          description: "Searches and returns a structured summary.",
          systemPrompt:
            "Use the search tool to research the question and summarize key points.",
          tools: [search],
          model: "openrouter:z-ai/glm-5.2",
          middleware: [],
        },
      ],
    }),
  ],
});
```

**Fireworks**

```ts
import { createAgent, todoListMiddleware, tool } from "langchain";
import {
  createFilesystemMiddleware,
  createSubAgentMiddleware,
  StateBackend,
} from "deepagents";
import * as z from "zod";

var search = tool(({ query }) => `Search results for: ${query}`, {
  name: "search",
  description: "Search for a query and return a short summary.",
  schema: z.object({ query: z.string() }),
});

var backend = new StateBackend();

var agent = createAgent({
  model: "fireworks:accounts/fireworks/models/glm-5p2",
  tools: [search],
  middleware: [
    createFilesystemMiddleware({ backend }),
    todoListMiddleware(),
    createSubAgentMiddleware({
      defaultModel: "anthropic:claude-sonnet-4-6",
      defaultTools: [],
      subagents: [
        {
          name: "researcher",
          description: "Searches and returns a structured summary.",
          systemPrompt:
            "Use the search tool to research the question and summarize key points.",
          tools: [search],
          model: "fireworks:accounts/fireworks/models/glm-5p2",
          middleware: [],
        },
      ],
    }),
  ],
});
```

**Baseten**

```ts
import { createAgent, todoListMiddleware, tool } from "langchain";
import {
  createFilesystemMiddleware,
  createSubAgentMiddleware,
  StateBackend,
} from "deepagents";
import * as z from "zod";

var search = tool(({ query }) => `Search results for: ${query}`, {
  name: "search",
  description: "Search for a query and return a short summary.",
  schema: z.object({ query: z.string() }),
});

var backend = new StateBackend();

var agent = createAgent({
  model: "baseten:zai-org/GLM-5.2",
  tools: [search],
  middleware: [
    createFilesystemMiddleware({ backend }),
    todoListMiddleware(),
    createSubAgentMiddleware({
      defaultModel: "anthropic:claude-sonnet-4-6",
      defaultTools: [],
      subagents: [
        {
          name: "researcher",
          description: "Searches and returns a structured summary.",
          systemPrompt:
            "Use the search tool to research the question and summarize key points.",
          tools: [search],
          model: "baseten:zai-org/GLM-5.2",
          middleware: [],
        },
      ],
    }),
  ],
});
```

**Ollama**

```ts
import { createAgent, todoListMiddleware, tool } from "langchain";
import {
  createFilesystemMiddleware,
  createSubAgentMiddleware,
  StateBackend,
} from "deepagents";
import * as z from "zod";

var search = tool(({ query }) => `Search results for: ${query}`, {
  name: "search",
  description: "Search for a query and return a short summary.",
  schema: z.object({ query: z.string() }),
});

var backend = new StateBackend();

var agent = createAgent({
  model: "ollama:north-mini-code-1.0",
  tools: [search],
  middleware: [
    createFilesystemMiddleware({ backend }),
    todoListMiddleware(),
    createSubAgentMiddleware({
      defaultModel: "anthropic:claude-sonnet-4-6",
      defaultTools: [],
      subagents: [
        {
          name: "researcher",
          description: "Searches and returns a structured summary.",
          systemPrompt:
            "Use the search tool to research the question and summarize key points.",
          tools: [search],
          model: "ollama:north-mini-code-1.0",
          middleware: [],
        },
      ],
    }),
  ],
});
```

See [Subagents](multi-agent/subagents.md).

> [!NOTE]
> This example imports from the `deepagents` package. Install it with:
>
> **npm**
>
> ```bash
> npm install deepagents
> ```
>
> **yarn**
>
> ```bash
> yarn add deepagents
> ```
>
> **pnpm**
>
> ```bash
> pnpm add deepagents
> ```

### Name your agent

Optionally use an identifier for the agent. This is especially useful when embedding the agent as a subgraph in [multi-agent](multi-agent.md) systems.

**Google**

```ts
var agent = createAgent({
  model: "google-genai:gemini-3.6-flash",
  tools,
  name: "research_assistant",
});
```

**OpenAI**

```ts
var agent = createAgent({
  model: "openai:gpt-5.5",
  tools,
  name: "research_assistant",
});
```

**Anthropic**

```ts
var agent = createAgent({
  model: "anthropic:claude-sonnet-5",
  tools,
  name: "research_assistant",
});
```

**OpenRouter**

```ts
var agent = createAgent({
  model: "openrouter:z-ai/glm-5.2",
  tools,
  name: "research_assistant",
});
```

**Fireworks**

```ts
var agent = createAgent({
  model: "fireworks:accounts/fireworks/models/glm-5p2",
  tools,
  name: "research_assistant",
});
```

**Baseten**

```ts
var agent = createAgent({
  model: "baseten:zai-org/GLM-5.2",
  tools,
  name: "research_assistant",
});
```

**Ollama**

```ts
var agent = createAgent({
  model: "ollama:north-mini-code-1.0",
  tools,
  name: "research_assistant",
});
```

### Fault tolerance

Agents in production encounter failures that rarely appear in development: rate limits, model timeouts, transient API errors. Fault tolerance middleware handles these at the infrastructure level so your tools and business logic don't need try/catch around every call.

**Google**

```ts
import {
  createAgent,
  modelRetryMiddleware,
  tool,
  toolRetryMiddleware,
} from "langchain";
import * as z from "zod";

var search = tool(({ query }) => `Search results for: ${query}`, {
  name: "search",
  description: "Search for a query and return a short summary.",
  schema: z.object({ query: z.string() }),
});

var agent = createAgent({
  model: "google-genai:gemini-3.6-flash",
  tools: [search],
  middleware: [
    modelRetryMiddleware({ maxRetries: 3 }),
    toolRetryMiddleware({ maxRetries: 2 }),
  ],
});
```

**OpenAI**

```ts
import {
  createAgent,
  modelRetryMiddleware,
  tool,
  toolRetryMiddleware,
} from "langchain";
import * as z from "zod";

var search = tool(({ query }) => `Search results for: ${query}`, {
  name: "search",
  description: "Search for a query and return a short summary.",
  schema: z.object({ query: z.string() }),
});

var agent = createAgent({
  model: "openai:gpt-5.5",
  tools: [search],
  middleware: [
    modelRetryMiddleware({ maxRetries: 3 }),
    toolRetryMiddleware({ maxRetries: 2 }),
  ],
});
```

**Anthropic**

```ts
import {
  createAgent,
  modelRetryMiddleware,
  tool,
  toolRetryMiddleware,
} from "langchain";
import * as z from "zod";

var search = tool(({ query }) => `Search results for: ${query}`, {
  name: "search",
  description: "Search for a query and return a short summary.",
  schema: z.object({ query: z.string() }),
});

var agent = createAgent({
  model: "anthropic:claude-sonnet-5",
  tools: [search],
  middleware: [
    modelRetryMiddleware({ maxRetries: 3 }),
    toolRetryMiddleware({ maxRetries: 2 }),
  ],
});
```

**OpenRouter**

```ts
import {
  createAgent,
  modelRetryMiddleware,
  tool,
  toolRetryMiddleware,
} from "langchain";
import * as z from "zod";

var search = tool(({ query }) => `Search results for: ${query}`, {
  name: "search",
  description: "Search for a query and return a short summary.",
  schema: z.object({ query: z.string() }),
});

var agent = createAgent({
  model: "openrouter:z-ai/glm-5.2",
  tools: [search],
  middleware: [
    modelRetryMiddleware({ maxRetries: 3 }),
    toolRetryMiddleware({ maxRetries: 2 }),
  ],
});
```

**Fireworks**

```ts
import {
  createAgent,
  modelRetryMiddleware,
  tool,
  toolRetryMiddleware,
} from "langchain";
import * as z from "zod";

var search = tool(({ query }) => `Search results for: ${query}`, {
  name: "search",
  description: "Search for a query and return a short summary.",
  schema: z.object({ query: z.string() }),
});

var agent = createAgent({
  model: "fireworks:accounts/fireworks/models/glm-5p2",
  tools: [search],
  middleware: [
    modelRetryMiddleware({ maxRetries: 3 }),
    toolRetryMiddleware({ maxRetries: 2 }),
  ],
});
```

**Baseten**

```ts
import {
  createAgent,
  modelRetryMiddleware,
  tool,
  toolRetryMiddleware,
} from "langchain";
import * as z from "zod";

var search = tool(({ query }) => `Search results for: ${query}`, {
  name: "search",
  description: "Search for a query and return a short summary.",
  schema: z.object({ query: z.string() }),
});

var agent = createAgent({
  model: "baseten:zai-org/GLM-5.2",
  tools: [search],
  middleware: [
    modelRetryMiddleware({ maxRetries: 3 }),
    toolRetryMiddleware({ maxRetries: 2 }),
  ],
});
```

**Ollama**

```ts
import {
  createAgent,
  modelRetryMiddleware,
  tool,
  toolRetryMiddleware,
} from "langchain";
import * as z from "zod";

var search = tool(({ query }) => `Search results for: ${query}`, {
  name: "search",
  description: "Search for a query and return a short summary.",
  schema: z.object({ query: z.string() }),
});

var agent = createAgent({
  model: "ollama:north-mini-code-1.0",
  tools: [search],
  middleware: [
    modelRetryMiddleware({ maxRetries: 3 }),
    toolRetryMiddleware({ maxRetries: 2 }),
  ],
});
```

See [`modelRetryMiddleware`](https://reference.langchain.com/javascript/langchain/index/modelRetryMiddleware), [`toolRetryMiddleware`](https://reference.langchain.com/javascript/langchain/index/toolRetryMiddleware), [Prebuilt middleware](middleware/built-in.md).

### Guardrails

Some policies can't live in a prompt—they need to be enforced deterministically regardless of what the model does. Guardrails intercept data as it flows through the agent loop, applying compliance rules or content policies before tool results reach the model's context.

**Google**

```ts
import { createAgent, piiMiddleware, tool } from "langchain";
import * as z from "zod";

var search = tool(({ query }) => `Search results for: ${query}`, {
  name: "search",
  description: "Search for a query and return a short summary.",
  schema: z.object({ query: z.string() }),
});

var agent = createAgent({
  model: "google-genai:gemini-3.6-flash",
  tools: [search],
  middleware: [piiMiddleware("email")],
});
```

**OpenAI**

```ts
import { createAgent, piiMiddleware, tool } from "langchain";
import * as z from "zod";

var search = tool(({ query }) => `Search results for: ${query}`, {
  name: "search",
  description: "Search for a query and return a short summary.",
  schema: z.object({ query: z.string() }),
});

var agent = createAgent({
  model: "openai:gpt-5.5",
  tools: [search],
  middleware: [piiMiddleware("email")],
});
```

**Anthropic**

```ts
import { createAgent, piiMiddleware, tool } from "langchain";
import * as z from "zod";

var search = tool(({ query }) => `Search results for: ${query}`, {
  name: "search",
  description: "Search for a query and return a short summary.",
  schema: z.object({ query: z.string() }),
});

var agent = createAgent({
  model: "anthropic:claude-sonnet-5",
  tools: [search],
  middleware: [piiMiddleware("email")],
});
```

**OpenRouter**

```ts
import { createAgent, piiMiddleware, tool } from "langchain";
import * as z from "zod";

var search = tool(({ query }) => `Search results for: ${query}`, {
  name: "search",
  description: "Search for a query and return a short summary.",
  schema: z.object({ query: z.string() }),
});

var agent = createAgent({
  model: "openrouter:z-ai/glm-5.2",
  tools: [search],
  middleware: [piiMiddleware("email")],
});
```

**Fireworks**

```ts
import { createAgent, piiMiddleware, tool } from "langchain";
import * as z from "zod";

var search = tool(({ query }) => `Search results for: ${query}`, {
  name: "search",
  description: "Search for a query and return a short summary.",
  schema: z.object({ query: z.string() }),
});

var agent = createAgent({
  model: "fireworks:accounts/fireworks/models/glm-5p2",
  tools: [search],
  middleware: [piiMiddleware("email")],
});
```

**Baseten**

```ts
import { createAgent, piiMiddleware, tool } from "langchain";
import * as z from "zod";

var search = tool(({ query }) => `Search results for: ${query}`, {
  name: "search",
  description: "Search for a query and return a short summary.",
  schema: z.object({ query: z.string() }),
});

var agent = createAgent({
  model: "baseten:zai-org/GLM-5.2",
  tools: [search],
  middleware: [piiMiddleware("email")],
});
```

**Ollama**

```ts
import { createAgent, piiMiddleware, tool } from "langchain";
import * as z from "zod";

var search = tool(({ query }) => `Search results for: ${query}`, {
  name: "search",
  description: "Search for a query and return a short summary.",
  schema: z.object({ query: z.string() }),
});

var agent = createAgent({
  model: "ollama:north-mini-code-1.0",
  tools: [search],
  middleware: [piiMiddleware("email")],
});
```

See [`piiMiddleware`](https://reference.langchain.com/javascript/langchain/index/piiMiddleware), [Prebuilt middleware](middleware/built-in.md).

### Steering

Full autonomy isn't always appropriate. Steering lets you place humans at specific decision points—before destructive writes, expensive API calls, or anything requiring judgment—without restructuring your agent. The agent pauses and waits; a human approves, edits, or rejects; execution continues.

**Google**

```ts
import { createAgent, humanInTheLoopMiddleware, tool } from "langchain";
import * as z from "zod";

var search = tool(({ query }) => `Search results for: ${query}`, {
  name: "search",
  description: "Search for a query and return a short summary.",
  schema: z.object({ query: z.string() }),
});

var agent = createAgent({
  model: "google-genai:gemini-3.6-flash",
  tools: [search],
  middleware: [humanInTheLoopMiddleware({ interruptOn: { writeFile: true } })],
});
```

**OpenAI**

```ts
import { createAgent, humanInTheLoopMiddleware, tool } from "langchain";
import * as z from "zod";

var search = tool(({ query }) => `Search results for: ${query}`, {
  name: "search",
  description: "Search for a query and return a short summary.",
  schema: z.object({ query: z.string() }),
});

var agent = createAgent({
  model: "openai:gpt-5.5",
  tools: [search],
  middleware: [humanInTheLoopMiddleware({ interruptOn: { writeFile: true } })],
});
```

**Anthropic**

```ts
import { createAgent, humanInTheLoopMiddleware, tool } from "langchain";
import * as z from "zod";

var search = tool(({ query }) => `Search results for: ${query}`, {
  name: "search",
  description: "Search for a query and return a short summary.",
  schema: z.object({ query: z.string() }),
});

var agent = createAgent({
  model: "anthropic:claude-sonnet-5",
  tools: [search],
  middleware: [humanInTheLoopMiddleware({ interruptOn: { writeFile: true } })],
});
```

**OpenRouter**

```ts
import { createAgent, humanInTheLoopMiddleware, tool } from "langchain";
import * as z from "zod";

var search = tool(({ query }) => `Search results for: ${query}`, {
  name: "search",
  description: "Search for a query and return a short summary.",
  schema: z.object({ query: z.string() }),
});

var agent = createAgent({
  model: "openrouter:z-ai/glm-5.2",
  tools: [search],
  middleware: [humanInTheLoopMiddleware({ interruptOn: { writeFile: true } })],
});
```

**Fireworks**

```ts
import { createAgent, humanInTheLoopMiddleware, tool } from "langchain";
import * as z from "zod";

var search = tool(({ query }) => `Search results for: ${query}`, {
  name: "search",
  description: "Search for a query and return a short summary.",
  schema: z.object({ query: z.string() }),
});

var agent = createAgent({
  model: "fireworks:accounts/fireworks/models/glm-5p2",
  tools: [search],
  middleware: [humanInTheLoopMiddleware({ interruptOn: { writeFile: true } })],
});
```

**Baseten**

```ts
import { createAgent, humanInTheLoopMiddleware, tool } from "langchain";
import * as z from "zod";

var search = tool(({ query }) => `Search results for: ${query}`, {
  name: "search",
  description: "Search for a query and return a short summary.",
  schema: z.object({ query: z.string() }),
});

var agent = createAgent({
  model: "baseten:zai-org/GLM-5.2",
  tools: [search],
  middleware: [humanInTheLoopMiddleware({ interruptOn: { writeFile: true } })],
});
```

**Ollama**

```ts
import { createAgent, humanInTheLoopMiddleware, tool } from "langchain";
import * as z from "zod";

var search = tool(({ query }) => `Search results for: ${query}`, {
  name: "search",
  description: "Search for a query and return a short summary.",
  schema: z.object({ query: z.string() }),
});

var agent = createAgent({
  model: "ollama:north-mini-code-1.0",
  tools: [search],
  middleware: [humanInTheLoopMiddleware({ interruptOn: { writeFile: true } })],
});
```

See [`humanInTheLoopMiddleware`](https://reference.langchain.com/javascript/langchain/middleware/humanInTheLoopMiddleware), [Human-in-the-loop](human-in-the-loop.md).

### Middleware resources

#### [Middleware overview](middleware/overview.md)
How the middleware stack works and when hooks fire

#### [Prebuilt middleware](middleware/built-in.md)
Full reference with configuration examples

#### [Custom middleware](middleware/custom.md)
Write your own hooks for business logic, PII scrubbing, and more

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/agents.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
