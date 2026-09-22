---
title: "LangChain overview"
description: "LangChain provides create_agent: a minimal, highly configurable agent harness. Compose exactly the agent your use case needs from model, tools, prompt, and middleware."
source: "https://docs.langchain.com/oss/javascript/langchain/overview"
category: "docs"
tags: [docs, javascript, langchain]
---

# LangChain overview

> LangChain provides create_agent: a minimal, highly configurable agent harness. Compose exactly the agent your use case needs from model, tools, prompt, and middleware.

**Agent = Model + Harness.** LangChain provides `create_agent`: a minimal, highly configurable harness. The harness is everything around the model loop: the prompt, the tools, and any middleware that shapes behavior. Start with the primitives and compose exactly what your use case needs. Supports [OpenAI, Anthropic, Google, and more](../integrations/providers/overview.md).

> [!TIP]
> **LangChain vs. LangGraph vs. Deep Agents**
>
> Start with [Deep Agents](../deepagents/overview.md) for a "batteries-included" agent with features like automatic context compression, a virtual filesystem, and subagent-spawning. Deep Agents are built on LangChain [agents](agents.md) which you can also use directly.
>
> Use [LangChain](agents.md) (`create_agent`) for a highly customizable harness, easily tailored to your use case and data.
>
> Use [LangGraph](../langgraph/overview.md), our low-level orchestration framework, for advanced needs combining deterministic and agentic workflows.
>
> Use [LangSmith](../../langsmith/observability.md) to trace, debug, and evaluate agents built with any of these frameworks. Follow the [tracing quickstart](../../langsmith/trace-with-langchain.md) to get set up. We recommend you also set up [LangSmith Engine](../../langsmith/engine.md) which monitors your traces, detects issues, and proposes fixes.

##  Create an agent

This example demonstrates how to create a simple LangChain agent with a custom tool:

**OpenAI**

```ts
// First install: npm install langchain zod @langchain/openai
import { createAgent, tool } from "langchain";
import * as z from "zod";

const getWeather = tool(
  (input) => `It's always sunny in ${input.city}!`,
  {
    name: "get_weather",
    description: "Get the weather for a given city",
    schema: z.object({
      city: z.string().describe("The city to get the weather for"),
    }),
  }
);

const agent = createAgent({
  model: "gpt-5.5",
  tools: [getWeather],
});

console.log(
  await agent.invoke({
    messages: [{ role: "user", content: "What's the weather in San Francisco?" }],
  })
);
```

**Google Gemini**

```ts
// First install: npm install langchain zod @langchain/google-genai
import { createAgent, tool } from "langchain";
import * as z from "zod";

const getWeather = tool(
  (input) => `It's always sunny in ${input.city}!`,
  {
    name: "get_weather",
    description: "Get the weather for a given city",
    schema: z.object({
      city: z.string().describe("The city to get the weather for"),
    }),
  }
);

const agent = createAgent({
  model: "google-genai:gemini-2.5-flash-lite",
  tools: [getWeather],
});

console.log(
  await agent.invoke({
    messages: [{ role: "user", content: "What's the weather in San Francisco?" }],
  })
);
```

**Claude (Anthropic)**

```ts
// First install: npm install langchain zod @langchain/anthropic
import { createAgent, tool } from "langchain";
import * as z from "zod";

const getWeather = tool(
  (input) => `It's always sunny in ${input.city}!`,
  {
    name: "get_weather",
    description: "Get the weather for a given city",
    schema: z.object({
      city: z.string().describe("The city to get the weather for"),
    }),
  }
);

const agent = createAgent({
  model: "claude-sonnet-4-6",
  tools: [getWeather],
});

console.log(
  await agent.invoke({
    messages: [{ role: "user", content: "What's the weather in San Francisco?" }],
  })
);
```

**OpenRouter**

```ts
// First install: npm install langchain zod @langchain/openrouter
import { createAgent, tool } from "langchain";
import * as z from "zod";

const getWeather = tool(
  (input) => `It's always sunny in ${input.city}!`,
  {
    name: "get_weather",
    description: "Get the weather for a given city",
    schema: z.object({
      city: z.string().describe("The city to get the weather for"),
    }),
  }
);

const agent = createAgent({
  model: "openrouter:anthropic/claude-sonnet-4-6",
  tools: [getWeather],
});

console.log(
  await agent.invoke({
    messages: [{ role: "user", content: "What's the weather in San Francisco?" }],
  })
);
```

**Fireworks**

```ts
// First install: npm install langchain zod
import { createAgent, tool } from "langchain";
import * as z from "zod";

const getWeather = tool(
  (input) => `It's always sunny in ${input.city}!`,
  {
    name: "get_weather",
    description: "Get the weather for a given city",
    schema: z.object({
      city: z.string().describe("The city to get the weather for"),
    }),
  }
);

const agent = createAgent({
  model: "fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
  tools: [getWeather],
});

console.log(
  await agent.invoke({
    messages: [{ role: "user", content: "What's the weather in San Francisco?" }],
  })
);
```

**Baseten**

```ts
// First install: npm install langchain zod
import { createAgent, tool } from "langchain";
import * as z from "zod";

const getWeather = tool(
  (input) => `It's always sunny in ${input.city}!`,
  {
    name: "get_weather",
    description: "Get the weather for a given city",
    schema: z.object({
      city: z.string().describe("The city to get the weather for"),
    }),
  }
);

const agent = createAgent({
  model: "baseten:zai-org/GLM-5.2",
  tools: [getWeather],
});

console.log(
  await agent.invoke({
    messages: [{ role: "user", content: "What's the weather in San Francisco?" }],
  })
);
```

**Ollama**

```ts
// First install: npm install langchain zod @langchain/ollama
import { createAgent, tool } from "langchain";
import * as z from "zod";

const getWeather = tool(
  (input) => `It's always sunny in ${input.city}!`,
  {
    name: "get_weather",
    description: "Get the weather for a given city",
    schema: z.object({
      city: z.string().describe("The city to get the weather for"),
    }),
  }
);

const agent = createAgent({
  model: "ollama:devstral-2",
  tools: [getWeather],
});

console.log(
  await agent.invoke({
    messages: [{ role: "user", content: "What's the weather in San Francisco?" }],
  })
);
```

**Azure**

```ts
// First install: npm install langchain zod @langchain/openai
import { createAgent, tool } from "langchain";
import * as z from "zod";

const getWeather = tool(
  (input) => `It's always sunny in ${input.city}!`,
  {
    name: "get_weather",
    description: "Get the weather for a given city",
    schema: z.object({
      city: z.string().describe("The city to get the weather for"),
    }),
  }
);

const agent = createAgent({
  model: "azure_openai:gpt-5.5",
  tools: [getWeather],
});

console.log(
  await agent.invoke({
    messages: [{ role: "user", content: "What's the weather in San Francisco?" }],
  })
);
```

**AWS Bedrock**

```ts
// First install: npm install langchain zod @langchain/aws
import { createAgent, tool } from "langchain";
import * as z from "zod";

const getWeather = tool(
  (input) => `It's always sunny in ${input.city}!`,
  {
    name: "get_weather",
    description: "Get the weather for a given city",
    schema: z.object({
      city: z.string().describe("The city to get the weather for"),
    }),
  }
);

const agent = createAgent({
  model: "bedrock:gpt-5.5",
  tools: [getWeather],
});

console.log(
  await agent.invoke({
    messages: [{ role: "user", content: "What's the weather in San Francisco?" }],
  })
);
```

See the [Installation instructions](install.md) and [Quickstart guide](quickstart.md) to get started building your own agents and applications with LangChain.

> [!TIP]
> Use [LangSmith](../../langsmith/observability.md) to trace requests, debug agent behavior, and evaluate outputs. Set `LANGSMITH_TRACING=true` and your API key to get started.

##  Core benefits

#### [Standard model interface](models.md)
Use one interface for chat models, embeddings, and more across providers. Switch models with minimal code changes and keep your application portable as requirements evolve.

#### [Highly configurable harness](agents.md)
Start with `create_agent` as a minimal harness and add capabilities incrementally through middleware. Compose only what your use case needs, from guardrails and retries to routing and custom tool policies.

#### [Built on top of LangGraph](../langgraph/overview.md)
LangChain's agents are built on top of LangGraph. This allows us to take advantage of LangGraph's durable execution, human-in-the-loop support, persistence, and more.

#### [Debug with LangSmith](../../langsmith/observability.md)
Inspect traces, tool calls, state transitions, and latency in one place. Find failure modes, evaluate quality, and improve agent behavior with execution data.

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/overview.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
