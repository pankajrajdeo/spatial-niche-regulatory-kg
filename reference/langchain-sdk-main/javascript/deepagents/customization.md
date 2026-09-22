---
title: "Customize Deep Agents"
description: "Learn how to customize Deep Agents with system prompts, tools, subagents, and more"
source: "https://docs.langchain.com/oss/javascript/deepagents/customization"
category: "docs"
tags: [docs, javascript, deepagents, customization]
---

# Customize Deep Agents

> Learn how to customize Deep Agents with system prompts, tools, subagents, and more

Build the harness around your goal. `create_deep_agent` gives you a production-ready foundation: connect it to your data, shape its behavior, and add the capabilities your use case needs.

`createDeepAgent` ships with a pre-assembled harness: filesystem, summarization, subagents, and prompt caching by default. The parameters below let you define the agent's persona, connect it to your data and tools, and extend the [Deep Agents stack](#deep-agents-stack) with additional middleware.

**Google**

```ts
import { createDeepAgent } from "deepagents";

const agent = await createDeepAgent({
  model: "google-genai:gemini-3.6-flash",
  systemPrompt: "You are a helpful assistant.",
  tools: [search, fetchUrl],
  memory: ["./AGENTS.md"],
  skills: ["./skills/"],
});
```

**OpenAI**

```ts
import { createDeepAgent } from "deepagents";

const agent = await createDeepAgent({
  model: "openai:gpt-5.5",
  systemPrompt: "You are a helpful assistant.",
  tools: [search, fetchUrl],
  memory: ["./AGENTS.md"],
  skills: ["./skills/"],
});
```

**Anthropic**

```ts
import { createDeepAgent } from "deepagents";

const agent = await createDeepAgent({
  model: "anthropic:claude-sonnet-5",
  systemPrompt: "You are a helpful assistant.",
  tools: [search, fetchUrl],
  memory: ["./AGENTS.md"],
  skills: ["./skills/"],
});
```

**OpenRouter**

```ts
import { createDeepAgent } from "deepagents";

const agent = await createDeepAgent({
  model: "openrouter:z-ai/glm-5.2",
  systemPrompt: "You are a helpful assistant.",
  tools: [search, fetchUrl],
  memory: ["./AGENTS.md"],
  skills: ["./skills/"],
});
```

**Fireworks**

```ts
import { createDeepAgent } from "deepagents";

const agent = await createDeepAgent({
  model: "fireworks:accounts/fireworks/models/glm-5p2",
  systemPrompt: "You are a helpful assistant.",
  tools: [search, fetchUrl],
  memory: ["./AGENTS.md"],
  skills: ["./skills/"],
});
```

**Baseten**

```ts
import { createDeepAgent } from "deepagents";

const agent = await createDeepAgent({
  model: "baseten:zai-org/GLM-5.2",
  systemPrompt: "You are a helpful assistant.",
  tools: [search, fetchUrl],
  memory: ["./AGENTS.md"],
  skills: ["./skills/"],
});
```

**Ollama**

```ts
import { createDeepAgent } from "deepagents";

const agent = await createDeepAgent({
  model: "ollama:north-mini-code-1.0",
  systemPrompt: "You are a helpful assistant.",
  tools: [search, fetchUrl],
  memory: ["./AGENTS.md"],
  skills: ["./skills/"],
});
```

| Parameter                                                                         | What it does                                                             |
| --------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| `model`                                                                           | Which model to use                                                       |
| `systemPrompt`                                                                    | Custom instructions for the agent                                        |
| `tools`                                                                           | Domain tools the agent can call                                          |
| `memory`                                                                          | AGENTS.md files loaded at startup                                        |
| `skills`                                                                          | Skills directory for on-demand knowledge                                 |
| `backend`                                                                         | Filesystem backend (StateBackend by default)                             |
| `permissions`                                                                     | Path-level access control for the filesystem                             |
| `subagents`                                                                       | Custom subagents for delegated tasks                                     |
| `middleware`                                                                      | Extra middleware appended to the [Deep Agents stack](#deep-agents-stack) |
| `interruptOn`                                                                     | Pause before tool calls for human approval                               |
| `responseFormat`                                                                  | Structured output schema                                                 |
| [`contextSchema`](context-engineering.md#runtime-context) | Per-run runtime context schema (user IDs, API keys, feature flags)       |

For the full parameter list, see the [`createDeepAgent`](https://reference.langchain.com/javascript/deepagents/types/CreateDeepAgentParams) API reference. To compose a fully custom harness from scratch, see [Configure the harness](../langchain/agents.md#configure-the-harness).

> [!TIP]
> As you add tools, subagents, and backends, use [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-deepagents-customization) to trace how each piece behaves together. Follow the [observability quickstart](../../langsmith/observability-quickstart.md) to get set up, and see [Going to production](going-to-production.md) for deployment on LangSmith.
>
> We recommend you also set up [LangSmith Engine](../../langsmith/engine.md), which monitors your traces, detects issues, and proposes fixes.

## Model

Pass a `model` string in `provider:model` format, or an initialized model instance. See [supported models](models.md#supported-models) for all providers and [suggested models](models.md#suggested-models) for tested recommendations.

> [!TIP]
> Use the `provider:model` format (for example `openai:gpt-5.5`) to quickly switch between models.

#### OpenAI
👉 Read the [OpenAI chat model integration docs](../integrations/chat/openai.md)

**npm**

```bash
npm install @langchain/openai deepagents
```

**pnpm**

```bash
pnpm install @langchain/openai deepagents
```

**yarn**

```bash
yarn add @langchain/openai deepagents
```

**bun**

```bash
bun add @langchain/openai deepagents
```

**default parameters**

```typescript
import { createDeepAgent } from "deepagents";

process.env.OPENAI_API_KEY = "your-api-key";

const agent = createDeepAgent({ model: "gpt-5.5" });
// this calls initChatModel for the specified model with default parameters
// to use specific model parameters, use initChatModel directly
```

**initChatModel**

```typescript
import { initChatModel } from "langchain";
import { createDeepAgent } from "deepagents";

process.env.OPENAI_API_KEY = "your-api-key";

const model = await initChatModel("gpt-5.5");
const agent = createDeepAgent({
  model,
  temperature: 0,
});
```

**Model Class**

```typescript
import { ChatOpenAI } from "@langchain/openai";
import { createDeepAgent } from "deepagents";

const agent = createDeepAgent({
  model: new ChatOpenAI({
    model: "gpt-5.5",
    apiKey: "your-api-key",
    temperature: 0,
  }),
});
```

#### Anthropic
👉 Read the [Anthropic chat model integration docs](../integrations/chat/anthropic.md)

**npm**

```bash
npm install @langchain/anthropic deepagents
```

**pnpm**

```bash
pnpm install @langchain/anthropic deepagents
```

**yarn**

```bash
yarn add @langchain/anthropic deepagents
```

**bun**

```bash
bun add @langchain/anthropic deepagents
```

**default parameters**

```typescript
import { createDeepAgent } from "deepagents";

process.env.ANTHROPIC_API_KEY = "your-api-key";

const agent = createDeepAgent({ model: "anthropic:claude-sonnet-4-6" });
// this calls initChatModel for the specified model with default parameters
// to use specific model parameters, use initChatModel directly
```

**initChatModel**

```typescript
import { initChatModel } from "langchain";
import { createDeepAgent } from "deepagents";

process.env.ANTHROPIC_API_KEY = "your-api-key";

const model = await initChatModel("claude-sonnet-4-6");
const agent = createDeepAgent({
  model,
  temperature: 0,
});
```

**Model Class**

```typescript
import { ChatAnthropic } from "@langchain/anthropic";
import { createDeepAgent } from "deepagents";

const agent = createDeepAgent({
  model: new ChatAnthropic({
    model: "claude-sonnet-4-6",
    apiKey: "your-api-key",
    temperature: 0,
  }),
});
```

#### Azure
👉 Read the [Azure chat model integration docs](../integrations/chat/azure.md)

**npm**

```bash
npm install @langchain/azure deepagents
```

**pnpm**

```bash
pnpm install @langchain/azure deepagents
```

**yarn**

```bash
yarn add @langchain/azure deepagents
```

**bun**

```bash
bun add @langchain/azure deepagents
```

**default parameters**

```typescript
import { createDeepAgent } from "deepagents";

process.env.AZURE_OPENAI_API_KEY = "your-api-key";
process.env.AZURE_OPENAI_ENDPOINT = "your-endpoint";
process.env.OPENAI_API_VERSION = "your-api-version";

const agent = createDeepAgent({ model: "azure_openai:gpt-5.5" });
// this calls initChatModel for the specified model with default parameters
// to use specific model parameters, use initChatModel directly
```

**initChatModel**

```typescript
import { initChatModel } from "langchain";
import { createDeepAgent } from "deepagents";

process.env.AZURE_OPENAI_API_KEY = "your-api-key";
process.env.AZURE_OPENAI_ENDPOINT = "your-endpoint";
process.env.OPENAI_API_VERSION = "your-api-version";

const model = await initChatModel("azure_openai:gpt-5.5");
const agent = createDeepAgent({
  model,
  temperature: 0,
});
```

**Model Class**

```typescript
import { AzureChatOpenAI } from "@langchain/openai";
import { createDeepAgent } from "deepagents";

const agent = createDeepAgent({
  model: new AzureChatOpenAI({
    model: "gpt-5.5",
    azureOpenAIApiKey: "your-api-key",
    azureOpenAIApiEndpoint: "your-endpoint",
    azureOpenAIApiVersion: "your-api-version",
    temperature: 0,
  }),
});
```

#### Google Gemini
👉 Read the [Google GenAI chat model integration docs](../integrations/chat/google_generative_ai.md)

**npm**

```bash
npm install @langchain/google-genai deepagents
```

**pnpm**

```bash
pnpm install @langchain/google-genai deepagents
```

**yarn**

```bash
yarn add @langchain/google-genai deepagents
```

**bun**

```bash
bun add @langchain/google-genai deepagents
```

**default parameters**

```typescript
import { createDeepAgent } from "deepagents";

process.env.GOOGLE_API_KEY = "your-api-key";

const agent = createDeepAgent({ model: "google-genai:gemini-3.1-pro-preview" });
// this calls initChatModel for the specified model with default parameters
// to use specific model parameters, use initChatModel directly
```

**initChatModel**

```typescript
import { initChatModel } from "langchain";
import { createDeepAgent } from "deepagents";

process.env.GOOGLE_API_KEY = "your-api-key";

const model = await initChatModel("google-genai:gemini-3.1-pro-preview");
const agent = createDeepAgent({
  model,
  temperature: 0,
});
```

**Model Class**

```typescript
import { ChatGoogleGenerativeAI } from "@langchain/google-genai";
import { createDeepAgent } from "deepagents";

const agent = createDeepAgent({
  model: new ChatGoogleGenerativeAI({
    model: "gemini-3.1-pro-preview",
    apiKey: "your-api-key",
    temperature: 0,
  }),
});
```

#### Bedrock Converse
👉 Read the [AWS Bedrock chat model integration docs](../integrations/chat/bedrock_converse.md)

**npm**

```bash
npm install @langchain/aws deepagents
```

**pnpm**

```bash
pnpm install @langchain/aws deepagents
```

**yarn**

```bash
yarn add @langchain/aws deepagents
```

**bun**

```bash
bun add @langchain/aws deepagents
```

**default parameters**

```typescript
import { createDeepAgent } from "deepagents";

// Follow the steps here to configure your credentials:
// https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started.html

const agent = createDeepAgent({ model: "bedrock:anthropic.claude-sonnet-4-6" });
// this calls initChatModel for the specified model with default parameters
// to use specific model parameters, use initChatModel directly
```

**initChatModel**

```typescript
import { initChatModel } from "langchain";
import { createDeepAgent } from "deepagents";

// Follow the steps here to configure your credentials:
// https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started.html

const model = await initChatModel("bedrock:anthropic.claude-sonnet-4-6");
const agent = createDeepAgent({
  model,
  temperature: 0,
});
```

**Model Class**

```typescript
import { ChatBedrockConverse } from "@langchain/aws";
import { createDeepAgent } from "deepagents";

// Follow the steps here to configure your credentials:
// https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started.html

const agent = createDeepAgent({
  model: new ChatBedrockConverse({
    model: "anthropic.claude-sonnet-4-6",
    region: "us-east-2",
    temperature: 0,
  }),
});
```

#### Other
Pass any [supported model string](models.md#supported-models), or an initialized model instance:

```typescript
import { initChatModel } from "langchain";
import { createDeepAgent } from "deepagents";

const model = await initChatModel("provider:model-name");
const agent = createDeepAgent({ model });
```

> [!TIP]
> Chat models automatically retry transient API failures (with exponential backoff). For defaults, limits, and code samples for tuning `max_retries` / `timeout` live on the LangChain [Models](../langchain/models.md#connection-resilience) page.

## Tools

In addition to [built-in tools](overview.md#execution-environment) for file management and subagent spawning, you can provide custom tools:

**Google**

```ts
import { tool } from "langchain";
import { TavilySearch } from "@langchain/tavily";
import { createDeepAgent } from "deepagents";
import { z } from "zod";

const internetSearch = tool(
  async ({
    query,
    maxResults = 5,
    topic = "general",
    includeRawContent = false,
  }: {
    query: string;
    maxResults?: number;
    topic?: "general" | "news" | "finance";
    includeRawContent?: boolean;
  }) => {
    const tavilySearch = new TavilySearch({
      maxResults,
      tavilyApiKey: process.env.TAVILY_API_KEY,
      includeRawContent,
      topic,
    });
    return await tavilySearch._call({ query });
  },
  {
    name: "internet_search",
    description: "Run a web search",
    schema: z.object({
      query: z.string().describe("The search query"),
      maxResults: z.number().optional().default(5),
      topic: z
        .enum(["general", "news", "finance"])
        .optional()
        .default("general"),
      includeRawContent: z.boolean().optional().default(false),
    }),
  },
);

const agent = createDeepAgent({
  model: "google-genai:gemini-3.6-flash",
  tools: [internetSearch],
});
```

**OpenAI**

```ts
import { tool } from "langchain";
import { TavilySearch } from "@langchain/tavily";
import { createDeepAgent } from "deepagents";
import { z } from "zod";

const internetSearch = tool(
  async ({
    query,
    maxResults = 5,
    topic = "general",
    includeRawContent = false,
  }: {
    query: string;
    maxResults?: number;
    topic?: "general" | "news" | "finance";
    includeRawContent?: boolean;
  }) => {
    const tavilySearch = new TavilySearch({
      maxResults,
      tavilyApiKey: process.env.TAVILY_API_KEY,
      includeRawContent,
      topic,
    });
    return await tavilySearch._call({ query });
  },
  {
    name: "internet_search",
    description: "Run a web search",
    schema: z.object({
      query: z.string().describe("The search query"),
      maxResults: z.number().optional().default(5),
      topic: z
        .enum(["general", "news", "finance"])
        .optional()
        .default("general"),
      includeRawContent: z.boolean().optional().default(false),
    }),
  },
);

const agent = createDeepAgent({
  model: "openai:gpt-5.5",
  tools: [internetSearch],
});
```

**Anthropic**

```ts
import { tool } from "langchain";
import { TavilySearch } from "@langchain/tavily";
import { createDeepAgent } from "deepagents";
import { z } from "zod";

const internetSearch = tool(
  async ({
    query,
    maxResults = 5,
    topic = "general",
    includeRawContent = false,
  }: {
    query: string;
    maxResults?: number;
    topic?: "general" | "news" | "finance";
    includeRawContent?: boolean;
  }) => {
    const tavilySearch = new TavilySearch({
      maxResults,
      tavilyApiKey: process.env.TAVILY_API_KEY,
      includeRawContent,
      topic,
    });
    return await tavilySearch._call({ query });
  },
  {
    name: "internet_search",
    description: "Run a web search",
    schema: z.object({
      query: z.string().describe("The search query"),
      maxResults: z.number().optional().default(5),
      topic: z
        .enum(["general", "news", "finance"])
        .optional()
        .default("general"),
      includeRawContent: z.boolean().optional().default(false),
    }),
  },
);

const agent = createDeepAgent({
  model: "anthropic:claude-sonnet-5",
  tools: [internetSearch],
});
```

**OpenRouter**

```ts
import { tool } from "langchain";
import { TavilySearch } from "@langchain/tavily";
import { createDeepAgent } from "deepagents";
import { z } from "zod";

const internetSearch = tool(
  async ({
    query,
    maxResults = 5,
    topic = "general",
    includeRawContent = false,
  }: {
    query: string;
    maxResults?: number;
    topic?: "general" | "news" | "finance";
    includeRawContent?: boolean;
  }) => {
    const tavilySearch = new TavilySearch({
      maxResults,
      tavilyApiKey: process.env.TAVILY_API_KEY,
      includeRawContent,
      topic,
    });
    return await tavilySearch._call({ query });
  },
  {
    name: "internet_search",
    description: "Run a web search",
    schema: z.object({
      query: z.string().describe("The search query"),
      maxResults: z.number().optional().default(5),
      topic: z
        .enum(["general", "news", "finance"])
        .optional()
        .default("general"),
      includeRawContent: z.boolean().optional().default(false),
    }),
  },
);

const agent = createDeepAgent({
  model: "openrouter:z-ai/glm-5.2",
  tools: [internetSearch],
});
```

**Fireworks**

```ts
import { tool } from "langchain";
import { TavilySearch } from "@langchain/tavily";
import { createDeepAgent } from "deepagents";
import { z } from "zod";

const internetSearch = tool(
  async ({
    query,
    maxResults = 5,
    topic = "general",
    includeRawContent = false,
  }: {
    query: string;
    maxResults?: number;
    topic?: "general" | "news" | "finance";
    includeRawContent?: boolean;
  }) => {
    const tavilySearch = new TavilySearch({
      maxResults,
      tavilyApiKey: process.env.TAVILY_API_KEY,
      includeRawContent,
      topic,
    });
    return await tavilySearch._call({ query });
  },
  {
    name: "internet_search",
    description: "Run a web search",
    schema: z.object({
      query: z.string().describe("The search query"),
      maxResults: z.number().optional().default(5),
      topic: z
        .enum(["general", "news", "finance"])
        .optional()
        .default("general"),
      includeRawContent: z.boolean().optional().default(false),
    }),
  },
);

const agent = createDeepAgent({
  model: "fireworks:accounts/fireworks/models/glm-5p2",
  tools: [internetSearch],
});
```

**Baseten**

```ts
import { tool } from "langchain";
import { TavilySearch } from "@langchain/tavily";
import { createDeepAgent } from "deepagents";
import { z } from "zod";

const internetSearch = tool(
  async ({
    query,
    maxResults = 5,
    topic = "general",
    includeRawContent = false,
  }: {
    query: string;
    maxResults?: number;
    topic?: "general" | "news" | "finance";
    includeRawContent?: boolean;
  }) => {
    const tavilySearch = new TavilySearch({
      maxResults,
      tavilyApiKey: process.env.TAVILY_API_KEY,
      includeRawContent,
      topic,
    });
    return await tavilySearch._call({ query });
  },
  {
    name: "internet_search",
    description: "Run a web search",
    schema: z.object({
      query: z.string().describe("The search query"),
      maxResults: z.number().optional().default(5),
      topic: z
        .enum(["general", "news", "finance"])
        .optional()
        .default("general"),
      includeRawContent: z.boolean().optional().default(false),
    }),
  },
);

const agent = createDeepAgent({
  model: "baseten:zai-org/GLM-5.2",
  tools: [internetSearch],
});
```

**Ollama**

```ts
import { tool } from "langchain";
import { TavilySearch } from "@langchain/tavily";
import { createDeepAgent } from "deepagents";
import { z } from "zod";

const internetSearch = tool(
  async ({
    query,
    maxResults = 5,
    topic = "general",
    includeRawContent = false,
  }: {
    query: string;
    maxResults?: number;
    topic?: "general" | "news" | "finance";
    includeRawContent?: boolean;
  }) => {
    const tavilySearch = new TavilySearch({
      maxResults,
      tavilyApiKey: process.env.TAVILY_API_KEY,
      includeRawContent,
      topic,
    });
    return await tavilySearch._call({ query });
  },
  {
    name: "internet_search",
    description: "Run a web search",
    schema: z.object({
      query: z.string().describe("The search query"),
      maxResults: z.number().optional().default(5),
      topic: z
        .enum(["general", "news", "finance"])
        .optional()
        .default("general"),
      includeRawContent: z.boolean().optional().default(false),
    }),
  },
);

const agent = createDeepAgent({
  model: "ollama:north-mini-code-1.0",
  tools: [internetSearch],
});
```

### MCP tools

> [!TIP]
> Deep Agents fully support [Model Context Protocol (MCP)](../langchain/mcp.md) tools. You can load tools from any MCP server—databases, APIs, file systems, and more—and pass them directly to `create_deep_agent`.

Install `@langchain/mcp-adapters` to connect to MCP servers:

```bash
npm install @langchain/mcp-adapters
```

**Google**

```ts
import { createDeepAgent } from "deepagents";

const { MultiServerMCPClient } = await import("@langchain/mcp-adapters");

const client = new MultiServerMCPClient({
    my_server: {
        transport: "http",
        url: "http://localhost:8000/mcp",
    },
});

const tools = await client.getTools();

const agent = await createDeepAgent({
    model: "google-genai:gemini-3.6-flash",
    tools,
});

const result = await agent.invoke({
    messages: [{ role: "user", content: "Use the MCP server to help me." }],
});
```

**OpenAI**

```ts
import { createDeepAgent } from "deepagents";

const { MultiServerMCPClient } = await import("@langchain/mcp-adapters");

const client = new MultiServerMCPClient({
    my_server: {
        transport: "http",
        url: "http://localhost:8000/mcp",
    },
});

const tools = await client.getTools();

const agent = await createDeepAgent({
    model: "openai:gpt-5.5",
    tools,
});

const result = await agent.invoke({
    messages: [{ role: "user", content: "Use the MCP server to help me." }],
});
```

**Anthropic**

```ts
import { createDeepAgent } from "deepagents";

const { MultiServerMCPClient } = await import("@langchain/mcp-adapters");

const client = new MultiServerMCPClient({
    my_server: {
        transport: "http",
        url: "http://localhost:8000/mcp",
    },
});

const tools = await client.getTools();

const agent = await createDeepAgent({
    model: "anthropic:claude-sonnet-5",
    tools,
});

const result = await agent.invoke({
    messages: [{ role: "user", content: "Use the MCP server to help me." }],
});
```

**OpenRouter**

```ts
import { createDeepAgent } from "deepagents";

const { MultiServerMCPClient } = await import("@langchain/mcp-adapters");

const client = new MultiServerMCPClient({
    my_server: {
        transport: "http",
        url: "http://localhost:8000/mcp",
    },
});

const tools = await client.getTools();

const agent = await createDeepAgent({
    model: "openrouter:z-ai/glm-5.2",
    tools,
});

const result = await agent.invoke({
    messages: [{ role: "user", content: "Use the MCP server to help me." }],
});
```

**Fireworks**

```ts
import { createDeepAgent } from "deepagents";

const { MultiServerMCPClient } = await import("@langchain/mcp-adapters");

const client = new MultiServerMCPClient({
    my_server: {
        transport: "http",
        url: "http://localhost:8000/mcp",
    },
});

const tools = await client.getTools();

const agent = await createDeepAgent({
    model: "fireworks:accounts/fireworks/models/glm-5p2",
    tools,
});

const result = await agent.invoke({
    messages: [{ role: "user", content: "Use the MCP server to help me." }],
});
```

**Baseten**

```ts
import { createDeepAgent } from "deepagents";

const { MultiServerMCPClient } = await import("@langchain/mcp-adapters");

const client = new MultiServerMCPClient({
    my_server: {
        transport: "http",
        url: "http://localhost:8000/mcp",
    },
});

const tools = await client.getTools();

const agent = await createDeepAgent({
    model: "baseten:zai-org/GLM-5.2",
    tools,
});

const result = await agent.invoke({
    messages: [{ role: "user", content: "Use the MCP server to help me." }],
});
```

**Ollama**

```ts
import { createDeepAgent } from "deepagents";

const { MultiServerMCPClient } = await import("@langchain/mcp-adapters");

const client = new MultiServerMCPClient({
    my_server: {
        transport: "http",
        url: "http://localhost:8000/mcp",
    },
});

const tools = await client.getTools();

const agent = await createDeepAgent({
    model: "ollama:north-mini-code-1.0",
    tools,
});

const result = await agent.invoke({
    messages: [{ role: "user", content: "Use the MCP server to help me." }],
});
```

For detailed configuration options including stdio servers, OAuth authentication, tool filtering, and stateful sessions, see the full [MCP guide](../langchain/mcp.md).

## System prompt

Pass `system_prompt=` to give the agent your own instructions:

**Google**

```ts
import { createDeepAgent } from "deepagents";

const researchInstructions =
  `You are an expert researcher. ` +
  `Your job is to conduct thorough research, and then ` +
  `write a polished report.`;

const agent = createDeepAgent({
  model: "google-genai:gemini-3.6-flash",
  systemPrompt: researchInstructions,
});
```

**OpenAI**

```ts
import { createDeepAgent } from "deepagents";

const researchInstructions =
  `You are an expert researcher. ` +
  `Your job is to conduct thorough research, and then ` +
  `write a polished report.`;

const agent = createDeepAgent({
  model: "openai:gpt-5.5",
  systemPrompt: researchInstructions,
});
```

**Anthropic**

```ts
import { createDeepAgent } from "deepagents";

const researchInstructions =
  `You are an expert researcher. ` +
  `Your job is to conduct thorough research, and then ` +
  `write a polished report.`;

const agent = createDeepAgent({
  model: "anthropic:claude-sonnet-5",
  systemPrompt: researchInstructions,
});
```

**OpenRouter**

```ts
import { createDeepAgent } from "deepagents";

const researchInstructions =
  `You are an expert researcher. ` +
  `Your job is to conduct thorough research, and then ` +
  `write a polished report.`;

const agent = createDeepAgent({
  model: "openrouter:z-ai/glm-5.2",
  systemPrompt: researchInstructions,
});
```

**Fireworks**

```ts
import { createDeepAgent } from "deepagents";

const researchInstructions =
  `You are an expert researcher. ` +
  `Your job is to conduct thorough research, and then ` +
  `write a polished report.`;

const agent = createDeepAgent({
  model: "fireworks:accounts/fireworks/models/glm-5p2",
  systemPrompt: researchInstructions,
});
```

**Baseten**

```ts
import { createDeepAgent } from "deepagents";

const researchInstructions =
  `You are an expert researcher. ` +
  `Your job is to conduct thorough research, and then ` +
  `write a polished report.`;

const agent = createDeepAgent({
  model: "baseten:zai-org/GLM-5.2",
  systemPrompt: researchInstructions,
});
```

**Ollama**

```ts
import { createDeepAgent } from "deepagents";

const researchInstructions =
  `You are an expert researcher. ` +
  `Your job is to conduct thorough research, and then ` +
  `write a polished report.`;

const agent = createDeepAgent({
  model: "ollama:north-mini-code-1.0",
  systemPrompt: researchInstructions,
});
```

> [!NOTE]
> Besides a string, the main agent also accepts a [`SystemMessage`](https://reference.langchain.com/javascript/langchain-core/messages/SystemMessage) with structured [content blocks](../langchain/messages.md#standard-content-blocks); Deep Agents preserve those blocks ([subagent](subagents.md) dictionary specs remain strings).

<details>
<summary>Subagent prompts</summary>

Declarative [subagents](subagents.md) resolve profile overlays against their own model, then apply the resolved profile's `base_system_prompt` / `system_prompt_suffix` to the subagent's authored `system_prompt`. A profile that ships only a `system_prompt_suffix` (the common case for built-in Anthropic / OpenAI profiles) appends to the authored prompt. A profile that sets `base_system_prompt` replaces it outright.

</details>

<details>
<summary>General-purpose subagent prompt</summary>

The auto-added [general-purpose subagent](subagents.md#the-general-purpose-subagent) resolves its base prompt as **`general_purpose_subagent.system_prompt` (if set) -> `HarnessProfile.base_system_prompt` (if set) -> SDK general-purpose default**, with the profile suffix layered on top. When both override fields are set, the general-purpose-specific one wins so a caller tuning both fields never sees their GP override silently dropped:

```python
from deepagents import (
    GeneralPurposeSubagentProfile,
    HarnessProfile,
    register_harness_profile,
)

register_harness_profile(
    "anthropic",
    HarnessProfile(
        base_system_prompt="You are ACME's support orchestrator.",  # main agent
        general_purpose_subagent=GeneralPurposeSubagentProfile(
            system_prompt="You are a research subagent. Cite sources.",  # GP subagent
        ),
        system_prompt_suffix="Always think step by step.",
    ),
)
```

| Stack       | Final system prompt                                     |
| ----------- | ------------------------------------------------------- |
| Main agent  | `"You are ACME's support orchestrator." + SUFFIX`       |
| GP subagent | `"You are a research subagent. Cite sources." + SUFFIX` |

</details>

## Middleware

Deep Agents support any [middleware](../langchain/middleware/overview.md), including the built-in middleware listed below, prebuilt middleware from LangChain, provider-specific middleware, and custom middleware you write yourself.

Pass middleware to the `middleware` argument of `createDeepAgent`. Custom middleware is appended after [`PatchToolCallsMiddleware`](https://reference.langchain.com/javascript/deepagents/middleware/createPatchToolCallsMiddleware) in the [Deep Agents stack](#deep-agents-stack).

### Deep Agents stack

`createDeepAgent` builds middleware in a fixed order. The [bare stack](#bare-stack) is what you get with only a model. The [full stack](#full-stack) is the complete assembly order, including slots that appear only when you pass optional arguments or when the resolved [harness profile](profiles.md) contributes them.

#### Bare stack

With only a `model` (no other optional arguments), the main agent typically includes:

1. [`FilesystemMiddleware`](https://reference.langchain.com/javascript/deepagents/middleware/createFilesystemMiddleware)
2. [`SubAgentMiddleware`](https://reference.langchain.com/javascript/deepagents/middleware/createSubAgentMiddleware) (because the [general-purpose subagent](subagents.md#default-subagent) is auto-added unless a harness profile disables it)
3. [`SummarizationMiddleware`](https://reference.langchain.com/javascript/langchain/index/summarizationMiddleware)
4. [`PatchToolCallsMiddleware`](https://reference.langchain.com/javascript/deepagents/middleware/createPatchToolCallsMiddleware)
5. **Prompt caching** middleware (added for supported providers; no-ops elsewhere)
6. **Harness profile extras** and **excluded-tool filtering**, if the resolved model profile defines them

#### Full stack

From first to last:

1. [`SkillsMiddleware`](https://reference.langchain.com/javascript/deepagents/middleware/createSkillsMiddleware): Only when you pass `skills`. Injected **before** filesystem middleware so skill metadata is available before file tools run.

2. [`FilesystemMiddleware`](https://reference.langchain.com/javascript/deepagents/middleware/createFilesystemMiddleware): Handles file system operations such as reading, writing, and navigating directories. When you pass `permissions`, filesystem permissions enforcement is included here so it can evaluate every tool the agent might call.

3. [`SubAgentMiddleware`](https://reference.langchain.com/javascript/deepagents/middleware/createSubAgentMiddleware): Only when at least one synchronous subagent is available. Spawns and coordinates subagents for delegating tasks. Included in the [bare stack](#bare-stack) because the general-purpose subagent is auto-added by default; omit it by disabling that subagent and passing no synchronous `subagents`. See [Running without subagents](subagents.md#running-without-subagents).

4. [`SummarizationMiddleware`](https://reference.langchain.com/javascript/langchain/index/summarizationMiddleware): Condenses message history to stay within context limits when conversations grow long (via [createSummarizationMiddleware](https://reference.langchain.com/javascript/deepagents/middleware/createSummarizationMiddleware)).

5. [`PatchToolCallsMiddleware`](https://reference.langchain.com/javascript/deepagents/middleware/createPatchToolCallsMiddleware): Repairs dangling tool calls in message history when a run resumes after an interruption or receives malformed tool-call arguments. Runs **before** Anthropic prompt caching and the tail stack below.

6. [`AsyncSubAgentMiddleware`](https://reference.langchain.com/javascript/deepagents/agent/createDeepAgent): Only when you configure async subagents.

7. **Your middleware argument**: Optional middleware you pass as the `middleware` argument is appended here (after Patch, before the tail stack).

8. **Harness profile extras**: Provider-specific middleware from the resolved model profile, if any.

9. **Excluded-tool filtering**: When the harness profile lists excluded tools, middleware removes those tools from the agent.

10. **Prompt caching** ([`AnthropicPromptCachingMiddleware`](https://reference.langchain.com/javascript/langchain/index/anthropicPromptCachingMiddleware) and [`BedrockPromptCachingMiddleware`](https://reference.langchain.com/javascript/langchain/index/bedrockPromptCachingMiddleware)): Added automatically for Anthropic models and Amazon Bedrock Converse models, respectively. Both run **after** Patch and after your middleware so the cached prefix matches what is actually sent to the model.

11. [`MemoryMiddleware`](https://reference.langchain.com/javascript/deepagents/middleware/createMemoryMiddleware): Only when you pass `memory`.

> [!NOTE]
>     `MemoryMiddleware` is placed **after** profile extras and the prompt caching middleware so updates to injected memory are less likely to invalidate the cache prefix. The same ordering concern is called out in the `createDeepAgent` implementation comments.

12. `HumanInTheLoopMiddleware`: Only when you pass `interruptOn`. Pauses for human approval or input at configured tool calls.

### Synchronous subagent stack

The built-in **general-purpose** subagent and each declarative synchronous `SubAgent` graph use a stack that `createDeepAgent` builds in code. It matches the main agent in broad shape (filesystem, summarization, Patch, profile extras, Anthropic and Bedrock caching, optional permissions) but differs in two ways:

* **Skills run after** [`PatchToolCallsMiddleware`](https://reference.langchain.com/javascript/deepagents/middleware/createPatchToolCallsMiddleware) on these inner agents (on the main agent, skills run **before** filesystem middleware when `skills` is set).
* There is **no** [`SubAgentMiddleware`](https://reference.langchain.com/javascript/deepagents/middleware/createSubAgentMiddleware) inside a subagent graph (only the parent agent exposes the `task` tool).

When a declarative subagent sets `interruptOn`, that value is forwarded to `createAgent` for the subagent, which wires up human-in-the-loop handling for the configured tool calls.

### Prebuilt middleware

LangChain exposes additional prebuilt middleware that let you add-on various features, such as retries, fallbacks, or PII detection. See [Prebuilt middleware](../langchain/middleware/built-in.md) for more.

The `deepagents` package also exposes [`createSummarizationMiddleware`](https://reference.langchain.com/javascript/deepagents/middleware/createSummarizationMiddleware) for the same workflow. For more detail, see [Summarization](context-engineering.md#summarization).

### Provider-specific middleware

For provider-specific middleware that is optimized for specific LLM providers, see [Middleware integrations](../integrations/middleware.md).

### Custom middleware

You can provide additional middleware to extend functionality, add tools, or implement custom hooks:

**Google**

```ts
import { tool, createMiddleware } from "langchain";
import { createDeepAgent } from "deepagents";
import * as z from "zod";

const getWeather = tool(
  ({ city }: { city: string }) => {
    return `The weather in ${city} is sunny.`;
  },
  {
    name: "get_weather",
    description: "Get the weather in a city.",
    schema: z.object({
      city: z.string(),
    }),
  },
);

let callCount = 0;

const logToolCallsMiddleware = createMiddleware({
  name: "LogToolCallsMiddleware",
  wrapToolCall: async (request, handler) => {
    // Intercept and log every tool call - demonstrates cross-cutting concern
    callCount += 1;
    const toolName = request.toolCall.name;

    console.log(`[Middleware] Tool call #${callCount}: ${toolName}`);
    console.log(
      `[Middleware] Arguments: ${JSON.stringify(request.toolCall.args)}`,
    );

    // Execute the tool call
    const result = await handler(request);

    // Log the result
    console.log(`[Middleware] Tool call #${callCount} completed`);

    return result;
  },
});

const agent = await createDeepAgent({
  model: "google-genai:gemini-3.6-flash",
  tools: [getWeather] as any,
  middleware: [logToolCallsMiddleware] as any,
});
```

**OpenAI**

```ts
import { tool, createMiddleware } from "langchain";
import { createDeepAgent } from "deepagents";
import * as z from "zod";

const getWeather = tool(
  ({ city }: { city: string }) => {
    return `The weather in ${city} is sunny.`;
  },
  {
    name: "get_weather",
    description: "Get the weather in a city.",
    schema: z.object({
      city: z.string(),
    }),
  },
);

let callCount = 0;

const logToolCallsMiddleware = createMiddleware({
  name: "LogToolCallsMiddleware",
  wrapToolCall: async (request, handler) => {
    // Intercept and log every tool call - demonstrates cross-cutting concern
    callCount += 1;
    const toolName = request.toolCall.name;

    console.log(`[Middleware] Tool call #${callCount}: ${toolName}`);
    console.log(
      `[Middleware] Arguments: ${JSON.stringify(request.toolCall.args)}`,
    );

    // Execute the tool call
    const result = await handler(request);

    // Log the result
    console.log(`[Middleware] Tool call #${callCount} completed`);

    return result;
  },
});

const agent = await createDeepAgent({
  model: "openai:gpt-5.5",
  tools: [getWeather] as any,
  middleware: [logToolCallsMiddleware] as any,
});
```

**Anthropic**

```ts
import { tool, createMiddleware } from "langchain";
import { createDeepAgent } from "deepagents";
import * as z from "zod";

const getWeather = tool(
  ({ city }: { city: string }) => {
    return `The weather in ${city} is sunny.`;
  },
  {
    name: "get_weather",
    description: "Get the weather in a city.",
    schema: z.object({
      city: z.string(),
    }),
  },
);

let callCount = 0;

const logToolCallsMiddleware = createMiddleware({
  name: "LogToolCallsMiddleware",
  wrapToolCall: async (request, handler) => {
    // Intercept and log every tool call - demonstrates cross-cutting concern
    callCount += 1;
    const toolName = request.toolCall.name;

    console.log(`[Middleware] Tool call #${callCount}: ${toolName}`);
    console.log(
      `[Middleware] Arguments: ${JSON.stringify(request.toolCall.args)}`,
    );

    // Execute the tool call
    const result = await handler(request);

    // Log the result
    console.log(`[Middleware] Tool call #${callCount} completed`);

    return result;
  },
});

const agent = await createDeepAgent({
  model: "anthropic:claude-sonnet-5",
  tools: [getWeather] as any,
  middleware: [logToolCallsMiddleware] as any,
});
```

**OpenRouter**

```ts
import { tool, createMiddleware } from "langchain";
import { createDeepAgent } from "deepagents";
import * as z from "zod";

const getWeather = tool(
  ({ city }: { city: string }) => {
    return `The weather in ${city} is sunny.`;
  },
  {
    name: "get_weather",
    description: "Get the weather in a city.",
    schema: z.object({
      city: z.string(),
    }),
  },
);

let callCount = 0;

const logToolCallsMiddleware = createMiddleware({
  name: "LogToolCallsMiddleware",
  wrapToolCall: async (request, handler) => {
    // Intercept and log every tool call - demonstrates cross-cutting concern
    callCount += 1;
    const toolName = request.toolCall.name;

    console.log(`[Middleware] Tool call #${callCount}: ${toolName}`);
    console.log(
      `[Middleware] Arguments: ${JSON.stringify(request.toolCall.args)}`,
    );

    // Execute the tool call
    const result = await handler(request);

    // Log the result
    console.log(`[Middleware] Tool call #${callCount} completed`);

    return result;
  },
});

const agent = await createDeepAgent({
  model: "openrouter:z-ai/glm-5.2",
  tools: [getWeather] as any,
  middleware: [logToolCallsMiddleware] as any,
});
```

**Fireworks**

```ts
import { tool, createMiddleware } from "langchain";
import { createDeepAgent } from "deepagents";
import * as z from "zod";

const getWeather = tool(
  ({ city }: { city: string }) => {
    return `The weather in ${city} is sunny.`;
  },
  {
    name: "get_weather",
    description: "Get the weather in a city.",
    schema: z.object({
      city: z.string(),
    }),
  },
);

let callCount = 0;

const logToolCallsMiddleware = createMiddleware({
  name: "LogToolCallsMiddleware",
  wrapToolCall: async (request, handler) => {
    // Intercept and log every tool call - demonstrates cross-cutting concern
    callCount += 1;
    const toolName = request.toolCall.name;

    console.log(`[Middleware] Tool call #${callCount}: ${toolName}`);
    console.log(
      `[Middleware] Arguments: ${JSON.stringify(request.toolCall.args)}`,
    );

    // Execute the tool call
    const result = await handler(request);

    // Log the result
    console.log(`[Middleware] Tool call #${callCount} completed`);

    return result;
  },
});

const agent = await createDeepAgent({
  model: "fireworks:accounts/fireworks/models/glm-5p2",
  tools: [getWeather] as any,
  middleware: [logToolCallsMiddleware] as any,
});
```

**Baseten**

```ts
import { tool, createMiddleware } from "langchain";
import { createDeepAgent } from "deepagents";
import * as z from "zod";

const getWeather = tool(
  ({ city }: { city: string }) => {
    return `The weather in ${city} is sunny.`;
  },
  {
    name: "get_weather",
    description: "Get the weather in a city.",
    schema: z.object({
      city: z.string(),
    }),
  },
);

let callCount = 0;

const logToolCallsMiddleware = createMiddleware({
  name: "LogToolCallsMiddleware",
  wrapToolCall: async (request, handler) => {
    // Intercept and log every tool call - demonstrates cross-cutting concern
    callCount += 1;
    const toolName = request.toolCall.name;

    console.log(`[Middleware] Tool call #${callCount}: ${toolName}`);
    console.log(
      `[Middleware] Arguments: ${JSON.stringify(request.toolCall.args)}`,
    );

    // Execute the tool call
    const result = await handler(request);

    // Log the result
    console.log(`[Middleware] Tool call #${callCount} completed`);

    return result;
  },
});

const agent = await createDeepAgent({
  model: "baseten:zai-org/GLM-5.2",
  tools: [getWeather] as any,
  middleware: [logToolCallsMiddleware] as any,
});
```

**Ollama**

```ts
import { tool, createMiddleware } from "langchain";
import { createDeepAgent } from "deepagents";
import * as z from "zod";

const getWeather = tool(
  ({ city }: { city: string }) => {
    return `The weather in ${city} is sunny.`;
  },
  {
    name: "get_weather",
    description: "Get the weather in a city.",
    schema: z.object({
      city: z.string(),
    }),
  },
);

let callCount = 0;

const logToolCallsMiddleware = createMiddleware({
  name: "LogToolCallsMiddleware",
  wrapToolCall: async (request, handler) => {
    // Intercept and log every tool call - demonstrates cross-cutting concern
    callCount += 1;
    const toolName = request.toolCall.name;

    console.log(`[Middleware] Tool call #${callCount}: ${toolName}`);
    console.log(
      `[Middleware] Arguments: ${JSON.stringify(request.toolCall.args)}`,
    );

    // Execute the tool call
    const result = await handler(request);

    // Log the result
    console.log(`[Middleware] Tool call #${callCount} completed`);

    return result;
  },
});

const agent = await createDeepAgent({
  model: "ollama:north-mini-code-1.0",
  tools: [getWeather] as any,
  middleware: [logToolCallsMiddleware] as any,
});
```

> [!WARNING]
> **Do not mutate attributes after initialization**
>
> If you need to track values across hook invocations (for example, counters or accumulated data), use graph state.
> Graph state is scoped to a thread by design, so updates are safe under concurrency.
>
> **Do this:**
>
> ```ts
> const customMiddleware = createMiddleware({
>   name: "CustomMiddleware",
>   beforeAgent: async (state) => {
>     return { x: (state.x ?? 0) + 1 }; // Update graph state instead
>   },
> });
> ```
>
> Do **not** do this:
>
> ```ts
> let x = 1;
>
> const customMiddlewareBad = createMiddleware({
>   name: "CustomMiddleware",
>   beforeAgent: async () => {
>     x += 1; // Mutation causes race conditions
>   },
> });
> ```
>
> Mutation in place, such as modifying `state.x` in `beforeAgent`, mutating a shared variable in `beforeAgent`, or changing other shared values in hooks, can lead to subtle bugs and race conditions because many operations run concurrently (subagents, parallel tools, and parallel invocations on different threads).
>
> If you must use mutation in custom middleware, consider what happens when subagents, parallel tools, or concurrent agent invocations run at the same time.

### Override a default middleware instance

### Interpreters

Use [interpreters](interpreters.md) to add an `eval` tool that runs JavaScript in a scoped QuickJS runtime. Interpreters are useful when the agent needs to compose tools programmatically, batch work, handle errors in code, or transform structured data without a full shell environment.

**Google**

```ts
import { createDeepAgent } from "deepagents";
import { createCodeInterpreterMiddleware } from "@langchain/quickjs";

const agent = createDeepAgent({
  model: "google-genai:gemini-3.6-flash",
  middleware: [createCodeInterpreterMiddleware()],
});
```

**OpenAI**

```ts
import { createDeepAgent } from "deepagents";
import { createCodeInterpreterMiddleware } from "@langchain/quickjs";

const agent = createDeepAgent({
  model: "openai:gpt-5.5",
  middleware: [createCodeInterpreterMiddleware()],
});
```

**Anthropic**

```ts
import { createDeepAgent } from "deepagents";
import { createCodeInterpreterMiddleware } from "@langchain/quickjs";

const agent = createDeepAgent({
  model: "anthropic:claude-sonnet-5",
  middleware: [createCodeInterpreterMiddleware()],
});
```

**OpenRouter**

```ts
import { createDeepAgent } from "deepagents";
import { createCodeInterpreterMiddleware } from "@langchain/quickjs";

const agent = createDeepAgent({
  model: "openrouter:z-ai/glm-5.2",
  middleware: [createCodeInterpreterMiddleware()],
});
```

**Fireworks**

```ts
import { createDeepAgent } from "deepagents";
import { createCodeInterpreterMiddleware } from "@langchain/quickjs";

const agent = createDeepAgent({
  model: "fireworks:accounts/fireworks/models/glm-5p2",
  middleware: [createCodeInterpreterMiddleware()],
});
```

**Baseten**

```ts
import { createDeepAgent } from "deepagents";
import { createCodeInterpreterMiddleware } from "@langchain/quickjs";

const agent = createDeepAgent({
  model: "baseten:zai-org/GLM-5.2",
  middleware: [createCodeInterpreterMiddleware()],
});
```

**Ollama**

```ts
import { createDeepAgent } from "deepagents";
import { createCodeInterpreterMiddleware } from "@langchain/quickjs";

const agent = createDeepAgent({
  model: "ollama:north-mini-code-1.0",
  middleware: [createCodeInterpreterMiddleware()],
});
```

For setup, programmatic tool calling, subagent orchestration, and limits, see [Interpreters](interpreters.md).

## Subagents

To isolate detailed work and avoid context bloat, use subagents:

**Google**

```ts
import { tool } from "langchain";
import { TavilySearch } from "@langchain/tavily";
import { createDeepAgent, type SubAgent } from "deepagents";
import { z } from "zod";

const internetSearch = tool(
  async ({
    query,
    maxResults = 5,
    topic = "general",
    includeRawContent = false,
  }: {
    query: string;
    maxResults?: number;
    topic?: "general" | "news" | "finance";
    includeRawContent?: boolean;
  }) => {
    const tavilySearch = new TavilySearch({
      maxResults,
      tavilyApiKey: process.env.TAVILY_API_KEY,
      includeRawContent,
      topic,
    });
    return await tavilySearch._call({ query });
  },
  {
    name: "internet_search",
    description: "Run a web search",
    schema: z.object({
      query: z.string().describe("The search query"),
      maxResults: z.number().optional().default(5),
      topic: z
        .enum(["general", "news", "finance"])
        .optional()
        .default("general"),
      includeRawContent: z.boolean().optional().default(false),
    }),
  },
);

const researchSubagent: SubAgent = {
  name: "research-agent",
  description: "Used to research more in depth questions",
  systemPrompt: "You are a great researcher",
  tools: [internetSearch],
  model: "google-genai:gemini-3.6-flash", // Optional override, defaults to main agent model
};
const subagents = [researchSubagent];

const agent = createDeepAgent({
  model: "google_genai:gemini-3.6-flash",
  subagents,
});
```

**OpenAI**

```ts
import { tool } from "langchain";
import { TavilySearch } from "@langchain/tavily";
import { createDeepAgent, type SubAgent } from "deepagents";
import { z } from "zod";

const internetSearch = tool(
  async ({
    query,
    maxResults = 5,
    topic = "general",
    includeRawContent = false,
  }: {
    query: string;
    maxResults?: number;
    topic?: "general" | "news" | "finance";
    includeRawContent?: boolean;
  }) => {
    const tavilySearch = new TavilySearch({
      maxResults,
      tavilyApiKey: process.env.TAVILY_API_KEY,
      includeRawContent,
      topic,
    });
    return await tavilySearch._call({ query });
  },
  {
    name: "internet_search",
    description: "Run a web search",
    schema: z.object({
      query: z.string().describe("The search query"),
      maxResults: z.number().optional().default(5),
      topic: z
        .enum(["general", "news", "finance"])
        .optional()
        .default("general"),
      includeRawContent: z.boolean().optional().default(false),
    }),
  },
);

const researchSubagent: SubAgent = {
  name: "research-agent",
  description: "Used to research more in depth questions",
  systemPrompt: "You are a great researcher",
  tools: [internetSearch],
  model: "openai:gpt-5.5", // Optional override, defaults to main agent model
};
const subagents = [researchSubagent];

const agent = createDeepAgent({
  model: "google_genai:gemini-3.6-flash",
  subagents,
});
```

**Anthropic**

```ts
import { tool } from "langchain";
import { TavilySearch } from "@langchain/tavily";
import { createDeepAgent, type SubAgent } from "deepagents";
import { z } from "zod";

const internetSearch = tool(
  async ({
    query,
    maxResults = 5,
    topic = "general",
    includeRawContent = false,
  }: {
    query: string;
    maxResults?: number;
    topic?: "general" | "news" | "finance";
    includeRawContent?: boolean;
  }) => {
    const tavilySearch = new TavilySearch({
      maxResults,
      tavilyApiKey: process.env.TAVILY_API_KEY,
      includeRawContent,
      topic,
    });
    return await tavilySearch._call({ query });
  },
  {
    name: "internet_search",
    description: "Run a web search",
    schema: z.object({
      query: z.string().describe("The search query"),
      maxResults: z.number().optional().default(5),
      topic: z
        .enum(["general", "news", "finance"])
        .optional()
        .default("general"),
      includeRawContent: z.boolean().optional().default(false),
    }),
  },
);

const researchSubagent: SubAgent = {
  name: "research-agent",
  description: "Used to research more in depth questions",
  systemPrompt: "You are a great researcher",
  tools: [internetSearch],
  model: "anthropic:claude-sonnet-5", // Optional override, defaults to main agent model
};
const subagents = [researchSubagent];

const agent = createDeepAgent({
  model: "google_genai:gemini-3.6-flash",
  subagents,
});
```

**OpenRouter**

```ts
import { tool } from "langchain";
import { TavilySearch } from "@langchain/tavily";
import { createDeepAgent, type SubAgent } from "deepagents";
import { z } from "zod";

const internetSearch = tool(
  async ({
    query,
    maxResults = 5,
    topic = "general",
    includeRawContent = false,
  }: {
    query: string;
    maxResults?: number;
    topic?: "general" | "news" | "finance";
    includeRawContent?: boolean;
  }) => {
    const tavilySearch = new TavilySearch({
      maxResults,
      tavilyApiKey: process.env.TAVILY_API_KEY,
      includeRawContent,
      topic,
    });
    return await tavilySearch._call({ query });
  },
  {
    name: "internet_search",
    description: "Run a web search",
    schema: z.object({
      query: z.string().describe("The search query"),
      maxResults: z.number().optional().default(5),
      topic: z
        .enum(["general", "news", "finance"])
        .optional()
        .default("general"),
      includeRawContent: z.boolean().optional().default(false),
    }),
  },
);

const researchSubagent: SubAgent = {
  name: "research-agent",
  description: "Used to research more in depth questions",
  systemPrompt: "You are a great researcher",
  tools: [internetSearch],
  model: "openrouter:z-ai/glm-5.2", // Optional override, defaults to main agent model
};
const subagents = [researchSubagent];

const agent = createDeepAgent({
  model: "google_genai:gemini-3.6-flash",
  subagents,
});
```

**Fireworks**

```ts
import { tool } from "langchain";
import { TavilySearch } from "@langchain/tavily";
import { createDeepAgent, type SubAgent } from "deepagents";
import { z } from "zod";

const internetSearch = tool(
  async ({
    query,
    maxResults = 5,
    topic = "general",
    includeRawContent = false,
  }: {
    query: string;
    maxResults?: number;
    topic?: "general" | "news" | "finance";
    includeRawContent?: boolean;
  }) => {
    const tavilySearch = new TavilySearch({
      maxResults,
      tavilyApiKey: process.env.TAVILY_API_KEY,
      includeRawContent,
      topic,
    });
    return await tavilySearch._call({ query });
  },
  {
    name: "internet_search",
    description: "Run a web search",
    schema: z.object({
      query: z.string().describe("The search query"),
      maxResults: z.number().optional().default(5),
      topic: z
        .enum(["general", "news", "finance"])
        .optional()
        .default("general"),
      includeRawContent: z.boolean().optional().default(false),
    }),
  },
);

const researchSubagent: SubAgent = {
  name: "research-agent",
  description: "Used to research more in depth questions",
  systemPrompt: "You are a great researcher",
  tools: [internetSearch],
  model: "fireworks:accounts/fireworks/models/glm-5p2", // Optional override, defaults to main agent model
};
const subagents = [researchSubagent];

const agent = createDeepAgent({
  model: "google_genai:gemini-3.6-flash",
  subagents,
});
```

**Baseten**

```ts
import { tool } from "langchain";
import { TavilySearch } from "@langchain/tavily";
import { createDeepAgent, type SubAgent } from "deepagents";
import { z } from "zod";

const internetSearch = tool(
  async ({
    query,
    maxResults = 5,
    topic = "general",
    includeRawContent = false,
  }: {
    query: string;
    maxResults?: number;
    topic?: "general" | "news" | "finance";
    includeRawContent?: boolean;
  }) => {
    const tavilySearch = new TavilySearch({
      maxResults,
      tavilyApiKey: process.env.TAVILY_API_KEY,
      includeRawContent,
      topic,
    });
    return await tavilySearch._call({ query });
  },
  {
    name: "internet_search",
    description: "Run a web search",
    schema: z.object({
      query: z.string().describe("The search query"),
      maxResults: z.number().optional().default(5),
      topic: z
        .enum(["general", "news", "finance"])
        .optional()
        .default("general"),
      includeRawContent: z.boolean().optional().default(false),
    }),
  },
);

const researchSubagent: SubAgent = {
  name: "research-agent",
  description: "Used to research more in depth questions",
  systemPrompt: "You are a great researcher",
  tools: [internetSearch],
  model: "baseten:zai-org/GLM-5.2", // Optional override, defaults to main agent model
};
const subagents = [researchSubagent];

const agent = createDeepAgent({
  model: "google_genai:gemini-3.6-flash",
  subagents,
});
```

**Ollama**

```ts
import { tool } from "langchain";
import { TavilySearch } from "@langchain/tavily";
import { createDeepAgent, type SubAgent } from "deepagents";
import { z } from "zod";

const internetSearch = tool(
  async ({
    query,
    maxResults = 5,
    topic = "general",
    includeRawContent = false,
  }: {
    query: string;
    maxResults?: number;
    topic?: "general" | "news" | "finance";
    includeRawContent?: boolean;
  }) => {
    const tavilySearch = new TavilySearch({
      maxResults,
      tavilyApiKey: process.env.TAVILY_API_KEY,
      includeRawContent,
      topic,
    });
    return await tavilySearch._call({ query });
  },
  {
    name: "internet_search",
    description: "Run a web search",
    schema: z.object({
      query: z.string().describe("The search query"),
      maxResults: z.number().optional().default(5),
      topic: z
        .enum(["general", "news", "finance"])
        .optional()
        .default("general"),
      includeRawContent: z.boolean().optional().default(false),
    }),
  },
);

const researchSubagent: SubAgent = {
  name: "research-agent",
  description: "Used to research more in depth questions",
  systemPrompt: "You are a great researcher",
  tools: [internetSearch],
  model: "ollama:north-mini-code-1.0", // Optional override, defaults to main agent model
};
const subagents = [researchSubagent];

const agent = createDeepAgent({
  model: "google_genai:gemini-3.6-flash",
  subagents,
});
```

For more information, see [Subagents](subagents.md).

## Backends

Tools for a deep agent can make use of virtual file systems to store, access, and edit files. By default, deep agents use a [`StateBackend`](https://reference.langchain.com/javascript/deepagents/backends/StateBackend).

If you are using [skills](#skills) or [memory](#memory), you must add the expected skill or memory files to the backend before creating the agent.

#### StateBackend
A thread-scoped filesystem backend stored in `langgraph` state.

Files persist across turns within a thread (via your checkpointer) and are not shared across threads.

```ts
import { createDeepAgent, StateBackend } from "deepagents";

// By default we provide a StateBackend
const agent = createDeepAgent();

// Under the hood, it looks like
const agent2 = createDeepAgent({
  backend: new StateBackend(),
});
```

#### FilesystemBackend
The local machine's filesystem.

> [!WARNING]
> This backend grants agents direct filesystem read/write access.
> Use with caution and only in appropriate environments.
> For more information, see [`FilesystemBackend`](backends.md#filesystembackend-local-disk).

**Google**

```ts
import { createDeepAgent, FilesystemBackend } from "deepagents";

const agent = createDeepAgent({
  model: "google-genai:gemini-3.6-flash",
  backend: new FilesystemBackend({ rootDir: ".", virtualMode: true }),
});
```

**OpenAI**

```ts
import { createDeepAgent, FilesystemBackend } from "deepagents";

const agent = createDeepAgent({
  model: "openai:gpt-5.5",
  backend: new FilesystemBackend({ rootDir: ".", virtualMode: true }),
});
```

**Anthropic**

```ts
import { createDeepAgent, FilesystemBackend } from "deepagents";

const agent = createDeepAgent({
  model: "anthropic:claude-sonnet-5",
  backend: new FilesystemBackend({ rootDir: ".", virtualMode: true }),
});
```

**OpenRouter**

```ts
import { createDeepAgent, FilesystemBackend } from "deepagents";

const agent = createDeepAgent({
  model: "openrouter:z-ai/glm-5.2",
  backend: new FilesystemBackend({ rootDir: ".", virtualMode: true }),
});
```

**Fireworks**

```ts
import { createDeepAgent, FilesystemBackend } from "deepagents";

const agent = createDeepAgent({
  model: "fireworks:accounts/fireworks/models/glm-5p2",
  backend: new FilesystemBackend({ rootDir: ".", virtualMode: true }),
});
```

**Baseten**

```ts
import { createDeepAgent, FilesystemBackend } from "deepagents";

const agent = createDeepAgent({
  model: "baseten:zai-org/GLM-5.2",
  backend: new FilesystemBackend({ rootDir: ".", virtualMode: true }),
});
```

**Ollama**

```ts
import { createDeepAgent, FilesystemBackend } from "deepagents";

const agent = createDeepAgent({
  model: "ollama:north-mini-code-1.0",
  backend: new FilesystemBackend({ rootDir: ".", virtualMode: true }),
});
```

> [!TIP]
> Wrap `FilesystemBackend` in a `CompositeBackend` to prevent internal agent data (offloaded tool results, conversation history) from being written to disk alongside your project files. See the [recommended pattern](backends.md#filesystembackend-local-disk).

#### LocalShellBackend
A filesystem with shell execution directly on the host. Provides filesystem tools plus the `execute` tool for running commands.

> [!WARNING]
> This backend grants agents direct filesystem read/write access **and** unrestricted shell execution on your host.
> Use with extreme caution and only in appropriate environments.
> For more information, see [`LocalShellBackend`](backends.md#localshellbackend-local-shell).

**Google**

```ts
import { createDeepAgent, LocalShellBackend } from "deepagents";

const backend = new LocalShellBackend({ workingDirectory: "." });

const agent = createDeepAgent({
  model: "google-genai:gemini-3.6-flash",
  backend,
});
```

**OpenAI**

```ts
import { createDeepAgent, LocalShellBackend } from "deepagents";

const backend = new LocalShellBackend({ workingDirectory: "." });

const agent = createDeepAgent({
  model: "openai:gpt-5.5",
  backend,
});
```

**Anthropic**

```ts
import { createDeepAgent, LocalShellBackend } from "deepagents";

const backend = new LocalShellBackend({ workingDirectory: "." });

const agent = createDeepAgent({
  model: "anthropic:claude-sonnet-5",
  backend,
});
```

**OpenRouter**

```ts
import { createDeepAgent, LocalShellBackend } from "deepagents";

const backend = new LocalShellBackend({ workingDirectory: "." });

const agent = createDeepAgent({
  model: "openrouter:z-ai/glm-5.2",
  backend,
});
```

**Fireworks**

```ts
import { createDeepAgent, LocalShellBackend } from "deepagents";

const backend = new LocalShellBackend({ workingDirectory: "." });

const agent = createDeepAgent({
  model: "fireworks:accounts/fireworks/models/glm-5p2",
  backend,
});
```

**Baseten**

```ts
import { createDeepAgent, LocalShellBackend } from "deepagents";

const backend = new LocalShellBackend({ workingDirectory: "." });

const agent = createDeepAgent({
  model: "baseten:zai-org/GLM-5.2",
  backend,
});
```

**Ollama**

```ts
import { createDeepAgent, LocalShellBackend } from "deepagents";

const backend = new LocalShellBackend({ workingDirectory: "." });

const agent = createDeepAgent({
  model: "ollama:north-mini-code-1.0",
  backend,
});
```

#### StoreBackend
A filesystem that provides long-term storage that is *persisted across threads*.

**Google**

```ts
import { createDeepAgent, StoreBackend } from "deepagents";
import { InMemoryStore } from "@langchain/langgraph";

const store = new InMemoryStore(); // Good for local dev; omit for LangSmith Deployment

const agent = createDeepAgent({
  model: "google-genai:gemini-3.6-flash",
  backend: new StoreBackend({
    namespace: (rt) => [rt.serverInfo.user.identity],
  }),
  store,
});
```

**OpenAI**

```ts
import { createDeepAgent, StoreBackend } from "deepagents";
import { InMemoryStore } from "@langchain/langgraph";

const store = new InMemoryStore(); // Good for local dev; omit for LangSmith Deployment

const agent = createDeepAgent({
  model: "openai:gpt-5.5",
  backend: new StoreBackend({
    namespace: (rt) => [rt.serverInfo.user.identity],
  }),
  store,
});
```

**Anthropic**

```ts
import { createDeepAgent, StoreBackend } from "deepagents";
import { InMemoryStore } from "@langchain/langgraph";

const store = new InMemoryStore(); // Good for local dev; omit for LangSmith Deployment

const agent = createDeepAgent({
  model: "anthropic:claude-sonnet-5",
  backend: new StoreBackend({
    namespace: (rt) => [rt.serverInfo.user.identity],
  }),
  store,
});
```

**OpenRouter**

```ts
import { createDeepAgent, StoreBackend } from "deepagents";
import { InMemoryStore } from "@langchain/langgraph";

const store = new InMemoryStore(); // Good for local dev; omit for LangSmith Deployment

const agent = createDeepAgent({
  model: "openrouter:z-ai/glm-5.2",
  backend: new StoreBackend({
    namespace: (rt) => [rt.serverInfo.user.identity],
  }),
  store,
});
```

**Fireworks**

```ts
import { createDeepAgent, StoreBackend } from "deepagents";
import { InMemoryStore } from "@langchain/langgraph";

const store = new InMemoryStore(); // Good for local dev; omit for LangSmith Deployment

const agent = createDeepAgent({
  model: "fireworks:accounts/fireworks/models/glm-5p2",
  backend: new StoreBackend({
    namespace: (rt) => [rt.serverInfo.user.identity],
  }),
  store,
});
```

**Baseten**

```ts
import { createDeepAgent, StoreBackend } from "deepagents";
import { InMemoryStore } from "@langchain/langgraph";

const store = new InMemoryStore(); // Good for local dev; omit for LangSmith Deployment

const agent = createDeepAgent({
  model: "baseten:zai-org/GLM-5.2",
  backend: new StoreBackend({
    namespace: (rt) => [rt.serverInfo.user.identity],
  }),
  store,
});
```

**Ollama**

```ts
import { createDeepAgent, StoreBackend } from "deepagents";
import { InMemoryStore } from "@langchain/langgraph";

const store = new InMemoryStore(); // Good for local dev; omit for LangSmith Deployment

const agent = createDeepAgent({
  model: "ollama:north-mini-code-1.0",
  backend: new StoreBackend({
    namespace: (rt) => [rt.serverInfo.user.identity],
  }),
  store,
});
```

> [!NOTE]
> When deploying to [LangSmith Deployment](../../langsmith/deployment.md), omit the `store` parameter. The platform automatically provisions a store for your agent.

> [!TIP]
> The `namespace` parameter controls data isolation. For multi-user deployments, always set a [namespace factory](backends.md#namespace-factories) to isolate data per user or tenant.

#### ContextHubBackend
Durable filesystem storage in a LangSmith Hub repo.

For more details, see [`ContextHubBackend`](backends.md#contexthubbackend).

#### CompositeBackend
A flexible backend where you can specify different routes in the filesystem to point towards different backends.

**Google**

```ts
import {
  createDeepAgent,
  CompositeBackend,
  StateBackend,
  StoreBackend,
} from "deepagents";
import { InMemoryStore } from "@langchain/langgraph";

const store = new InMemoryStore();

const agent = createDeepAgent({
  model: "google-genai:gemini-3.6-flash",
  backend: new CompositeBackend(new StateBackend(), {
    "/memories/": new StoreBackend({
      namespace: () => ["memories"],
    }),
  }),
  store,
});
```

**OpenAI**

```ts
import {
  createDeepAgent,
  CompositeBackend,
  StateBackend,
  StoreBackend,
} from "deepagents";
import { InMemoryStore } from "@langchain/langgraph";

const store = new InMemoryStore();

const agent = createDeepAgent({
  model: "openai:gpt-5.5",
  backend: new CompositeBackend(new StateBackend(), {
    "/memories/": new StoreBackend({
      namespace: () => ["memories"],
    }),
  }),
  store,
});
```

**Anthropic**

```ts
import {
  createDeepAgent,
  CompositeBackend,
  StateBackend,
  StoreBackend,
} from "deepagents";
import { InMemoryStore } from "@langchain/langgraph";

const store = new InMemoryStore();

const agent = createDeepAgent({
  model: "anthropic:claude-sonnet-5",
  backend: new CompositeBackend(new StateBackend(), {
    "/memories/": new StoreBackend({
      namespace: () => ["memories"],
    }),
  }),
  store,
});
```

**OpenRouter**

```ts
import {
  createDeepAgent,
  CompositeBackend,
  StateBackend,
  StoreBackend,
} from "deepagents";
import { InMemoryStore } from "@langchain/langgraph";

const store = new InMemoryStore();

const agent = createDeepAgent({
  model: "openrouter:z-ai/glm-5.2",
  backend: new CompositeBackend(new StateBackend(), {
    "/memories/": new StoreBackend({
      namespace: () => ["memories"],
    }),
  }),
  store,
});
```

**Fireworks**

```ts
import {
  createDeepAgent,
  CompositeBackend,
  StateBackend,
  StoreBackend,
} from "deepagents";
import { InMemoryStore } from "@langchain/langgraph";

const store = new InMemoryStore();

const agent = createDeepAgent({
  model: "fireworks:accounts/fireworks/models/glm-5p2",
  backend: new CompositeBackend(new StateBackend(), {
    "/memories/": new StoreBackend({
      namespace: () => ["memories"],
    }),
  }),
  store,
});
```

**Baseten**

```ts
import {
  createDeepAgent,
  CompositeBackend,
  StateBackend,
  StoreBackend,
} from "deepagents";
import { InMemoryStore } from "@langchain/langgraph";

const store = new InMemoryStore();

const agent = createDeepAgent({
  model: "baseten:zai-org/GLM-5.2",
  backend: new CompositeBackend(new StateBackend(), {
    "/memories/": new StoreBackend({
      namespace: () => ["memories"],
    }),
  }),
  store,
});
```

**Ollama**

```ts
import {
  createDeepAgent,
  CompositeBackend,
  StateBackend,
  StoreBackend,
} from "deepagents";
import { InMemoryStore } from "@langchain/langgraph";

const store = new InMemoryStore();

const agent = createDeepAgent({
  model: "ollama:north-mini-code-1.0",
  backend: new CompositeBackend(new StateBackend(), {
    "/memories/": new StoreBackend({
      namespace: () => ["memories"],
    }),
  }),
  store,
});
```

For more information, see [Backends](backends.md).

### Sandboxes

Sandboxes are specialized [backends](backends.md) that run agent code in an isolated environment with their own filesystem and an `execute` tool for shell commands.
Use a sandbox backend when you want your deep agent to write files, install dependencies, and run commands without changing anything on your local machine.

You configure sandboxes by passing a sandbox backend to `backend` when creating your deep agent:

```typescript
import { createDeepAgent, LangSmithSandbox } from "deepagents";
import { ChatAnthropic } from "@langchain/anthropic";
import { SandboxClient } from "langsmith/sandbox";

const client = new SandboxClient();
const lsSandbox = await client.createSandbox();

try {
  const agent = createDeepAgent({
    model: new ChatAnthropic({ model: "claude-opus-4-8" }),
    systemPrompt: "You are a coding assistant with sandbox access.",
    backend: new LangSmithSandbox({ sandbox: lsSandbox }),
  });

  const result = await agent.invoke({
    messages: [
      {
        role: "user",
        content: "Create a hello world Python script and run it",
      },
    ],
  });
} finally {
  await client.deleteSandbox(lsSandbox.name);
}
```

For more information, see [Sandboxes](sandboxes.md).

## Human-in-the-loop

Some tool operations may be sensitive and require human approval before execution.
You can configure the approval for each tool:

```ts
import { tool } from "langchain";
import { createDeepAgent } from "deepagents";
import { MemorySaver } from "@langchain/langgraph";
import { z } from "zod";

const removeFile = tool(
  async ({ path }: { path: string }) => {
    return `Deleted ${path}`;
  },
  {
    name: "remove_file",
    description: "Delete a file from the filesystem.",
    schema: z.object({
      path: z.string(),
    }),
  },
);

const fetchFile = tool(
  async ({ path }: { path: string }) => {
    return `Contents of ${path}`;
  },
  {
    name: "fetch_file",
    description: "Read a file from the filesystem.",
    schema: z.object({
      path: z.string(),
    }),
  },
);

const notifyEmail = tool(
  async ({
    to,
    subject,
    body,
  }: {
    to: string;
    subject: string;
    body: string;
  }) => {
    return `Sent email to ${to}`;
  },
  {
    name: "notify_email",
    description: "Send an email.",
    schema: z.object({
      to: z.string(),
      subject: z.string(),
      body: z.string(),
    }),
  },
);

// Checkpointer is REQUIRED for human-in-the-loop
const checkpointer = new MemorySaver();

const agent = createDeepAgent({
  model: "google_genai:gemini-3.6-flash",
  tools: [removeFile, fetchFile, notifyEmail],
  interruptOn: {
    remove_file: true, // Default: approve, edit, reject, respond
    fetch_file: false, // No interrupts needed
    notify_email: { allowedDecisions: ["approve", "reject"] }, // No editing
  },
  checkpointer, // Required!
});
```

You can configure interrupt for agents and subagents on tool call as well as from within tool calls.
For more information, see [Human-in-the-loop](human-in-the-loop.md).

## Skills

You can use [skills](overview.md) to provide your deep agent with new capabilities and expertise.
While [tools](#tools) tend to cover lower level functionality like native file system actions, skills can contain detailed instructions on how to complete tasks, reference info, and other assets, such as templates.
These files are only loaded by the agent when the agent has determined that the skill is useful for the current prompt.
This progressive disclosure reduces the amount of tokens and context the agent has to consider upon startup.

For example skills, see [Deep Agents example skills](https://github.com/langchain-ai/deepagentsjs/tree/main/examples/skills).

To add skills to your deep agent, pass them as an argument to `create_deep_agent`:

#### StateBackend
```ts
import { createDeepAgent, StateBackend, type FileData } from "deepagents";
import { MemorySaver } from "@langchain/langgraph";

const checkpointer = new MemorySaver();
const backend = new StateBackend();

function createFileData(content: string): FileData {
  const now = new Date().toISOString();
  return {
    content: content.split("\n"),
    created_at: now,
    modified_at: now,
  };
}

const skillsFiles: Record<string, FileData> = {};
const skillUrl =
  "https://raw.githubusercontent.com/langchain-ai/deepagentsjs/refs/heads/main/examples/skills/langgraph-docs/SKILL.md";
const response = await fetch(skillUrl);
const skillContent = await response.text();

skillsFiles["/skills/langgraph-docs/SKILL.md"] = createFileData(skillContent);

const agent = await createDeepAgent({
  model: "anthropic:claude-sonnet-4-6",
  backend,
  checkpointer, // Required !
  // IMPORTANT: deepagents skill source paths are virtual (POSIX) paths relative to the backend root.
  skills: ["/skills/"],
});

const config = { configurable: { thread_id: `thread-${Date.now()}` } };
const result = await agent.invoke(
  {
    messages: [{ role: "user", content: "what is langraph?" }],
    files: skillsFiles,
  },
  config,
);
```

#### StoreBackend
```ts
import { createDeepAgent, StoreBackend } from "deepagents";
import { InMemoryStore, MemorySaver } from "@langchain/langgraph";

const checkpointer = new MemorySaver();
const store = new InMemoryStore();
const backend = new StoreBackend({
  namespace: () => ["filesystem"],
  store,
});

const skillUrl =
  "https://raw.githubusercontent.com/langchain-ai/deepagentsjs/refs/heads/main/examples/skills/langgraph-docs/SKILL.md";

const response = await fetch(skillUrl);
const skillContent = await response.text();

await backend.uploadFiles([
  ["/skills/langgraph-docs/SKILL.md", new TextEncoder().encode(skillContent)],
]);

const agent = await createDeepAgent({
  model: "anthropic:claude-sonnet-4-6",
  backend,
  store,
  checkpointer,
  // IMPORTANT: deepagents skill source paths are virtual (POSIX) paths relative to the backend root.
  skills: ["/skills/"],
});

const config = {
  recursionLimit: 50,
  configurable: { thread_id: `thread-${Date.now()}` },
};
const result = await agent.invoke(
  { messages: [{ role: "user", content: "what is langraph?" }] },
  config,
);
```

#### FilesystemBackend
```ts
import { createDeepAgent, FilesystemBackend } from "deepagents";
import { MemorySaver } from "@langchain/langgraph";

const checkpointer = new MemorySaver();

const skillUrl =
  "https://raw.githubusercontent.com/langchain-ai/deepagentsjs/refs/heads/main/examples/skills/langgraph-docs/SKILL.md";
const response = await fetch(skillUrl);
const skillContent = await response.text();

let backend = new FilesystemBackend({
  rootDir: process.cwd(),
  virtualMode: true,
});
await backend.uploadFiles([
  ["/skills/langgraph-docs/SKILL.md", new TextEncoder().encode(skillContent)],
]);

const agent = await createDeepAgent({
  model: "anthropic:claude-sonnet-4-6",
  backend,
  // IMPORTANT: deepagents skill source paths are virtual (POSIX) paths relative to the backend root.
  skills: ["/skills/"],
  interruptOn: {
    read_file: true,
    write_file: true,
    delete_file: true,
  },
  checkpointer, // Required for filesystem operations!
});

const config = { configurable: { thread_id: `thread-${Date.now()}` } };
const result = await agent.invoke(
  { messages: [{ role: "user", content: "what is langraph?" }] },
  config,
);
```

## Memory

Use [`AGENTS.md` files](https://agents.md/) to provide extra context to your deep agent.

> [!TIP]
> To generate a repository wiki that coding agents discover through `AGENTS.md`, see [OpenWiki](../../openwiki/overview.md).

You can pass one or more file paths to the `memory` parameter when creating your deep agent:

#### StateBackend
**Google**

```ts
import { createDeepAgent, type FileData } from "deepagents";
import { MemorySaver } from "@langchain/langgraph";

const AGENTS_MD_URL =
  "https://raw.githubusercontent.com/langchain-ai/deepagents/refs/heads/main/examples/text-to-sql-agent/AGENTS.md";

async function fetchText(url: string): Promise<string> {
  const res = await fetch(url);
  if (!res.ok) {
    throw new Error(`Failed to fetch ${url}: ${res.status} ${res.statusText}`);
  }
  return await res.text();
}

const agentsMd = await fetchText(AGENTS_MD_URL);
const checkpointer = new MemorySaver();

function createFileData(content: string): FileData {
  const now = new Date().toISOString();
  return {
    content,
    mimeType: "text/plain",
    created_at: now,
    modified_at: now,
  };
}

const agent = await createDeepAgent({
  model: "google-genai:gemini-3.6-flash",
  memory: ["/AGENTS.md"],
  checkpointer: checkpointer,
});

const result = await agent.invoke(
  {
    messages: [
      {
        role: "user",
        content: "Please tell me what's in your memory files.",
      },
    ],
    // Seed the default StateBackend's in-state filesystem (virtual paths must start with "/").
    files: { "/AGENTS.md": createFileData(agentsMd) },
  },
  { configurable: { thread_id: "12345" } },
);
```

**OpenAI**

```ts
import { createDeepAgent, type FileData } from "deepagents";
import { MemorySaver } from "@langchain/langgraph";

const AGENTS_MD_URL =
  "https://raw.githubusercontent.com/langchain-ai/deepagents/refs/heads/main/examples/text-to-sql-agent/AGENTS.md";

async function fetchText(url: string): Promise<string> {
  const res = await fetch(url);
  if (!res.ok) {
    throw new Error(`Failed to fetch ${url}: ${res.status} ${res.statusText}`);
  }
  return await res.text();
}

const agentsMd = await fetchText(AGENTS_MD_URL);
const checkpointer = new MemorySaver();

function createFileData(content: string): FileData {
  const now = new Date().toISOString();
  return {
    content,
    mimeType: "text/plain",
    created_at: now,
    modified_at: now,
  };
}

const agent = await createDeepAgent({
  model: "openai:gpt-5.5",
  memory: ["/AGENTS.md"],
  checkpointer: checkpointer,
});

const result = await agent.invoke(
  {
    messages: [
      {
        role: "user",
        content: "Please tell me what's in your memory files.",
      },
    ],
    // Seed the default StateBackend's in-state filesystem (virtual paths must start with "/").
    files: { "/AGENTS.md": createFileData(agentsMd) },
  },
  { configurable: { thread_id: "12345" } },
);
```

**Anthropic**

```ts
import { createDeepAgent, type FileData } from "deepagents";
import { MemorySaver } from "@langchain/langgraph";

const AGENTS_MD_URL =
  "https://raw.githubusercontent.com/langchain-ai/deepagents/refs/heads/main/examples/text-to-sql-agent/AGENTS.md";

async function fetchText(url: string): Promise<string> {
  const res = await fetch(url);
  if (!res.ok) {
    throw new Error(`Failed to fetch ${url}: ${res.status} ${res.statusText}`);
  }
  return await res.text();
}

const agentsMd = await fetchText(AGENTS_MD_URL);
const checkpointer = new MemorySaver();

function createFileData(content: string): FileData {
  const now = new Date().toISOString();
  return {
    content,
    mimeType: "text/plain",
    created_at: now,
    modified_at: now,
  };
}

const agent = await createDeepAgent({
  model: "anthropic:claude-sonnet-5",
  memory: ["/AGENTS.md"],
  checkpointer: checkpointer,
});

const result = await agent.invoke(
  {
    messages: [
      {
        role: "user",
        content: "Please tell me what's in your memory files.",
      },
    ],
    // Seed the default StateBackend's in-state filesystem (virtual paths must start with "/").
    files: { "/AGENTS.md": createFileData(agentsMd) },
  },
  { configurable: { thread_id: "12345" } },
);
```

**OpenRouter**

```ts
import { createDeepAgent, type FileData } from "deepagents";
import { MemorySaver } from "@langchain/langgraph";

const AGENTS_MD_URL =
  "https://raw.githubusercontent.com/langchain-ai/deepagents/refs/heads/main/examples/text-to-sql-agent/AGENTS.md";

async function fetchText(url: string): Promise<string> {
  const res = await fetch(url);
  if (!res.ok) {
    throw new Error(`Failed to fetch ${url}: ${res.status} ${res.statusText}`);
  }
  return await res.text();
}

const agentsMd = await fetchText(AGENTS_MD_URL);
const checkpointer = new MemorySaver();

function createFileData(content: string): FileData {
  const now = new Date().toISOString();
  return {
    content,
    mimeType: "text/plain",
    created_at: now,
    modified_at: now,
  };
}

const agent = await createDeepAgent({
  model: "openrouter:z-ai/glm-5.2",
  memory: ["/AGENTS.md"],
  checkpointer: checkpointer,
});

const result = await agent.invoke(
  {
    messages: [
      {
        role: "user",
        content: "Please tell me what's in your memory files.",
      },
    ],
    // Seed the default StateBackend's in-state filesystem (virtual paths must start with "/").
    files: { "/AGENTS.md": createFileData(agentsMd) },
  },
  { configurable: { thread_id: "12345" } },
);
```

**Fireworks**

```ts
import { createDeepAgent, type FileData } from "deepagents";
import { MemorySaver } from "@langchain/langgraph";

const AGENTS_MD_URL =
  "https://raw.githubusercontent.com/langchain-ai/deepagents/refs/heads/main/examples/text-to-sql-agent/AGENTS.md";

async function fetchText(url: string): Promise<string> {
  const res = await fetch(url);
  if (!res.ok) {
    throw new Error(`Failed to fetch ${url}: ${res.status} ${res.statusText}`);
  }
  return await res.text();
}

const agentsMd = await fetchText(AGENTS_MD_URL);
const checkpointer = new MemorySaver();

function createFileData(content: string): FileData {
  const now = new Date().toISOString();
  return {
    content,
    mimeType: "text/plain",
    created_at: now,
    modified_at: now,
  };
}

const agent = await createDeepAgent({
  model: "fireworks:accounts/fireworks/models/glm-5p2",
  memory: ["/AGENTS.md"],
  checkpointer: checkpointer,
});

const result = await agent.invoke(
  {
    messages: [
      {
        role: "user",
        content: "Please tell me what's in your memory files.",
      },
    ],
    // Seed the default StateBackend's in-state filesystem (virtual paths must start with "/").
    files: { "/AGENTS.md": createFileData(agentsMd) },
  },
  { configurable: { thread_id: "12345" } },
);
```

**Baseten**

```ts
import { createDeepAgent, type FileData } from "deepagents";
import { MemorySaver } from "@langchain/langgraph";

const AGENTS_MD_URL =
  "https://raw.githubusercontent.com/langchain-ai/deepagents/refs/heads/main/examples/text-to-sql-agent/AGENTS.md";

async function fetchText(url: string): Promise<string> {
  const res = await fetch(url);
  if (!res.ok) {
    throw new Error(`Failed to fetch ${url}: ${res.status} ${res.statusText}`);
  }
  return await res.text();
}

const agentsMd = await fetchText(AGENTS_MD_URL);
const checkpointer = new MemorySaver();

function createFileData(content: string): FileData {
  const now = new Date().toISOString();
  return {
    content,
    mimeType: "text/plain",
    created_at: now,
    modified_at: now,
  };
}

const agent = await createDeepAgent({
  model: "baseten:zai-org/GLM-5.2",
  memory: ["/AGENTS.md"],
  checkpointer: checkpointer,
});

const result = await agent.invoke(
  {
    messages: [
      {
        role: "user",
        content: "Please tell me what's in your memory files.",
      },
    ],
    // Seed the default StateBackend's in-state filesystem (virtual paths must start with "/").
    files: { "/AGENTS.md": createFileData(agentsMd) },
  },
  { configurable: { thread_id: "12345" } },
);
```

**Ollama**

```ts
import { createDeepAgent, type FileData } from "deepagents";
import { MemorySaver } from "@langchain/langgraph";

const AGENTS_MD_URL =
  "https://raw.githubusercontent.com/langchain-ai/deepagents/refs/heads/main/examples/text-to-sql-agent/AGENTS.md";

async function fetchText(url: string): Promise<string> {
  const res = await fetch(url);
  if (!res.ok) {
    throw new Error(`Failed to fetch ${url}: ${res.status} ${res.statusText}`);
  }
  return await res.text();
}

const agentsMd = await fetchText(AGENTS_MD_URL);
const checkpointer = new MemorySaver();

function createFileData(content: string): FileData {
  const now = new Date().toISOString();
  return {
    content,
    mimeType: "text/plain",
    created_at: now,
    modified_at: now,
  };
}

const agent = await createDeepAgent({
  model: "ollama:north-mini-code-1.0",
  memory: ["/AGENTS.md"],
  checkpointer: checkpointer,
});

const result = await agent.invoke(
  {
    messages: [
      {
        role: "user",
        content: "Please tell me what's in your memory files.",
      },
    ],
    // Seed the default StateBackend's in-state filesystem (virtual paths must start with "/").
    files: { "/AGENTS.md": createFileData(agentsMd) },
  },
  { configurable: { thread_id: "12345" } },
);
```

#### [View example trace](https://smith.langchain.com/public/5c07e925-9d8f-4792-b73c-9dbee94890cd/r)
Open a public LangSmith run for this example.

#### StoreBackend
**Google**

```ts
import { createDeepAgent, StoreBackend, type FileData } from "deepagents";
import { InMemoryStore, MemorySaver } from "@langchain/langgraph";

const AGENTS_MD_URL =
  "https://raw.githubusercontent.com/langchain-ai/deepagents/refs/heads/main/examples/text-to-sql-agent/AGENTS.md";

async function fetchText(url: string): Promise<string> {
  const res = await fetch(url);
  if (!res.ok) {
    throw new Error(`Failed to fetch ${url}: ${res.status} ${res.statusText}`);
  }
  return await res.text();
}

const agentsMd = await fetchText(AGENTS_MD_URL);

function createFileData(content: string): FileData {
  const now = new Date().toISOString();
  return {
    content,
    mimeType: "text/plain",
    created_at: now,
    modified_at: now,
  };
}

const store = new InMemoryStore();
const fileData = createFileData(agentsMd);
await store.put(["filesystem"], "/AGENTS.md", fileData);

const checkpointer = new MemorySaver();

const agent = await createDeepAgent({
  model: "google-genai:gemini-3.6-flash",
  backend: new StoreBackend({
    namespace: () => ["filesystem"],
  }),
  store: store,
  checkpointer: checkpointer,
  memory: ["/AGENTS.md"],
});

const result = await agent.invoke(
  {
    messages: [
      {
        role: "user",
        content: "Please tell me what's in your memory files.",
      },
    ],
  },
  { configurable: { thread_id: "12345" } },
);
```

**OpenAI**

```ts
import { createDeepAgent, StoreBackend, type FileData } from "deepagents";
import { InMemoryStore, MemorySaver } from "@langchain/langgraph";

const AGENTS_MD_URL =
  "https://raw.githubusercontent.com/langchain-ai/deepagents/refs/heads/main/examples/text-to-sql-agent/AGENTS.md";

async function fetchText(url: string): Promise<string> {
  const res = await fetch(url);
  if (!res.ok) {
    throw new Error(`Failed to fetch ${url}: ${res.status} ${res.statusText}`);
  }
  return await res.text();
}

const agentsMd = await fetchText(AGENTS_MD_URL);

function createFileData(content: string): FileData {
  const now = new Date().toISOString();
  return {
    content,
    mimeType: "text/plain",
    created_at: now,
    modified_at: now,
  };
}

const store = new InMemoryStore();
const fileData = createFileData(agentsMd);
await store.put(["filesystem"], "/AGENTS.md", fileData);

const checkpointer = new MemorySaver();

const agent = await createDeepAgent({
  model: "openai:gpt-5.5",
  backend: new StoreBackend({
    namespace: () => ["filesystem"],
  }),
  store: store,
  checkpointer: checkpointer,
  memory: ["/AGENTS.md"],
});

const result = await agent.invoke(
  {
    messages: [
      {
        role: "user",
        content: "Please tell me what's in your memory files.",
      },
    ],
  },
  { configurable: { thread_id: "12345" } },
);
```

**Anthropic**

```ts
import { createDeepAgent, StoreBackend, type FileData } from "deepagents";
import { InMemoryStore, MemorySaver } from "@langchain/langgraph";

const AGENTS_MD_URL =
  "https://raw.githubusercontent.com/langchain-ai/deepagents/refs/heads/main/examples/text-to-sql-agent/AGENTS.md";

async function fetchText(url: string): Promise<string> {
  const res = await fetch(url);
  if (!res.ok) {
    throw new Error(`Failed to fetch ${url}: ${res.status} ${res.statusText}`);
  }
  return await res.text();
}

const agentsMd = await fetchText(AGENTS_MD_URL);

function createFileData(content: string): FileData {
  const now = new Date().toISOString();
  return {
    content,
    mimeType: "text/plain",
    created_at: now,
    modified_at: now,
  };
}

const store = new InMemoryStore();
const fileData = createFileData(agentsMd);
await store.put(["filesystem"], "/AGENTS.md", fileData);

const checkpointer = new MemorySaver();

const agent = await createDeepAgent({
  model: "anthropic:claude-sonnet-5",
  backend: new StoreBackend({
    namespace: () => ["filesystem"],
  }),
  store: store,
  checkpointer: checkpointer,
  memory: ["/AGENTS.md"],
});

const result = await agent.invoke(
  {
    messages: [
      {
        role: "user",
        content: "Please tell me what's in your memory files.",
      },
    ],
  },
  { configurable: { thread_id: "12345" } },
);
```

**OpenRouter**

```ts
import { createDeepAgent, StoreBackend, type FileData } from "deepagents";
import { InMemoryStore, MemorySaver } from "@langchain/langgraph";

const AGENTS_MD_URL =
  "https://raw.githubusercontent.com/langchain-ai/deepagents/refs/heads/main/examples/text-to-sql-agent/AGENTS.md";

async function fetchText(url: string): Promise<string> {
  const res = await fetch(url);
  if (!res.ok) {
    throw new Error(`Failed to fetch ${url}: ${res.status} ${res.statusText}`);
  }
  return await res.text();
}

const agentsMd = await fetchText(AGENTS_MD_URL);

function createFileData(content: string): FileData {
  const now = new Date().toISOString();
  return {
    content,
    mimeType: "text/plain",
    created_at: now,
    modified_at: now,
  };
}

const store = new InMemoryStore();
const fileData = createFileData(agentsMd);
await store.put(["filesystem"], "/AGENTS.md", fileData);

const checkpointer = new MemorySaver();

const agent = await createDeepAgent({
  model: "openrouter:z-ai/glm-5.2",
  backend: new StoreBackend({
    namespace: () => ["filesystem"],
  }),
  store: store,
  checkpointer: checkpointer,
  memory: ["/AGENTS.md"],
});

const result = await agent.invoke(
  {
    messages: [
      {
        role: "user",
        content: "Please tell me what's in your memory files.",
      },
    ],
  },
  { configurable: { thread_id: "12345" } },
);
```

**Fireworks**

```ts
import { createDeepAgent, StoreBackend, type FileData } from "deepagents";
import { InMemoryStore, MemorySaver } from "@langchain/langgraph";

const AGENTS_MD_URL =
  "https://raw.githubusercontent.com/langchain-ai/deepagents/refs/heads/main/examples/text-to-sql-agent/AGENTS.md";

async function fetchText(url: string): Promise<string> {
  const res = await fetch(url);
  if (!res.ok) {
    throw new Error(`Failed to fetch ${url}: ${res.status} ${res.statusText}`);
  }
  return await res.text();
}

const agentsMd = await fetchText(AGENTS_MD_URL);

function createFileData(content: string): FileData {
  const now = new Date().toISOString();
  return {
    content,
    mimeType: "text/plain",
    created_at: now,
    modified_at: now,
  };
}

const store = new InMemoryStore();
const fileData = createFileData(agentsMd);
await store.put(["filesystem"], "/AGENTS.md", fileData);

const checkpointer = new MemorySaver();

const agent = await createDeepAgent({
  model: "fireworks:accounts/fireworks/models/glm-5p2",
  backend: new StoreBackend({
    namespace: () => ["filesystem"],
  }),
  store: store,
  checkpointer: checkpointer,
  memory: ["/AGENTS.md"],
});

const result = await agent.invoke(
  {
    messages: [
      {
        role: "user",
        content: "Please tell me what's in your memory files.",
      },
    ],
  },
  { configurable: { thread_id: "12345" } },
);
```

**Baseten**

```ts
import { createDeepAgent, StoreBackend, type FileData } from "deepagents";
import { InMemoryStore, MemorySaver } from "@langchain/langgraph";

const AGENTS_MD_URL =
  "https://raw.githubusercontent.com/langchain-ai/deepagents/refs/heads/main/examples/text-to-sql-agent/AGENTS.md";

async function fetchText(url: string): Promise<string> {
  const res = await fetch(url);
  if (!res.ok) {
    throw new Error(`Failed to fetch ${url}: ${res.status} ${res.statusText}`);
  }
  return await res.text();
}

const agentsMd = await fetchText(AGENTS_MD_URL);

function createFileData(content: string): FileData {
  const now = new Date().toISOString();
  return {
    content,
    mimeType: "text/plain",
    created_at: now,
    modified_at: now,
  };
}

const store = new InMemoryStore();
const fileData = createFileData(agentsMd);
await store.put(["filesystem"], "/AGENTS.md", fileData);

const checkpointer = new MemorySaver();

const agent = await createDeepAgent({
  model: "baseten:zai-org/GLM-5.2",
  backend: new StoreBackend({
    namespace: () => ["filesystem"],
  }),
  store: store,
  checkpointer: checkpointer,
  memory: ["/AGENTS.md"],
});

const result = await agent.invoke(
  {
    messages: [
      {
        role: "user",
        content: "Please tell me what's in your memory files.",
      },
    ],
  },
  { configurable: { thread_id: "12345" } },
);
```

**Ollama**

```ts
import { createDeepAgent, StoreBackend, type FileData } from "deepagents";
import { InMemoryStore, MemorySaver } from "@langchain/langgraph";

const AGENTS_MD_URL =
  "https://raw.githubusercontent.com/langchain-ai/deepagents/refs/heads/main/examples/text-to-sql-agent/AGENTS.md";

async function fetchText(url: string): Promise<string> {
  const res = await fetch(url);
  if (!res.ok) {
    throw new Error(`Failed to fetch ${url}: ${res.status} ${res.statusText}`);
  }
  return await res.text();
}

const agentsMd = await fetchText(AGENTS_MD_URL);

function createFileData(content: string): FileData {
  const now = new Date().toISOString();
  return {
    content,
    mimeType: "text/plain",
    created_at: now,
    modified_at: now,
  };
}

const store = new InMemoryStore();
const fileData = createFileData(agentsMd);
await store.put(["filesystem"], "/AGENTS.md", fileData);

const checkpointer = new MemorySaver();

const agent = await createDeepAgent({
  model: "ollama:north-mini-code-1.0",
  backend: new StoreBackend({
    namespace: () => ["filesystem"],
  }),
  store: store,
  checkpointer: checkpointer,
  memory: ["/AGENTS.md"],
});

const result = await agent.invoke(
  {
    messages: [
      {
        role: "user",
        content: "Please tell me what's in your memory files.",
      },
    ],
  },
  { configurable: { thread_id: "12345" } },
);
```

#### [View example trace](https://smith.langchain.com/public/ff0f387f-c0c3-4456-8081-d6fc23504942/r)
Open a public LangSmith run for this example.

#### Filesystem
**Google**

```ts
import { createDeepAgent, FilesystemBackend } from "deepagents";
import { MemorySaver } from "@langchain/langgraph";

// Checkpointer is REQUIRED for human-in-the-loop
const checkpointer = new MemorySaver();

const agent = await createDeepAgent({
  model: "google-genai:gemini-3.6-flash",
  backend: new FilesystemBackend({ rootDir: "/Users/user/{project}" }),
  memory: ["./AGENTS.md", "./.deepagents/AGENTS.md"],
  interruptOn: {
    read_file: true,
    write_file: true,
    delete_file: true,
  },
  checkpointer, // Required!
});
```

**OpenAI**

```ts
import { createDeepAgent, FilesystemBackend } from "deepagents";
import { MemorySaver } from "@langchain/langgraph";

// Checkpointer is REQUIRED for human-in-the-loop
const checkpointer = new MemorySaver();

const agent = await createDeepAgent({
  model: "openai:gpt-5.5",
  backend: new FilesystemBackend({ rootDir: "/Users/user/{project}" }),
  memory: ["./AGENTS.md", "./.deepagents/AGENTS.md"],
  interruptOn: {
    read_file: true,
    write_file: true,
    delete_file: true,
  },
  checkpointer, // Required!
});
```

**Anthropic**

```ts
import { createDeepAgent, FilesystemBackend } from "deepagents";
import { MemorySaver } from "@langchain/langgraph";

// Checkpointer is REQUIRED for human-in-the-loop
const checkpointer = new MemorySaver();

const agent = await createDeepAgent({
  model: "anthropic:claude-sonnet-5",
  backend: new FilesystemBackend({ rootDir: "/Users/user/{project}" }),
  memory: ["./AGENTS.md", "./.deepagents/AGENTS.md"],
  interruptOn: {
    read_file: true,
    write_file: true,
    delete_file: true,
  },
  checkpointer, // Required!
});
```

**OpenRouter**

```ts
import { createDeepAgent, FilesystemBackend } from "deepagents";
import { MemorySaver } from "@langchain/langgraph";

// Checkpointer is REQUIRED for human-in-the-loop
const checkpointer = new MemorySaver();

const agent = await createDeepAgent({
  model: "openrouter:z-ai/glm-5.2",
  backend: new FilesystemBackend({ rootDir: "/Users/user/{project}" }),
  memory: ["./AGENTS.md", "./.deepagents/AGENTS.md"],
  interruptOn: {
    read_file: true,
    write_file: true,
    delete_file: true,
  },
  checkpointer, // Required!
});
```

**Fireworks**

```ts
import { createDeepAgent, FilesystemBackend } from "deepagents";
import { MemorySaver } from "@langchain/langgraph";

// Checkpointer is REQUIRED for human-in-the-loop
const checkpointer = new MemorySaver();

const agent = await createDeepAgent({
  model: "fireworks:accounts/fireworks/models/glm-5p2",
  backend: new FilesystemBackend({ rootDir: "/Users/user/{project}" }),
  memory: ["./AGENTS.md", "./.deepagents/AGENTS.md"],
  interruptOn: {
    read_file: true,
    write_file: true,
    delete_file: true,
  },
  checkpointer, // Required!
});
```

**Baseten**

```ts
import { createDeepAgent, FilesystemBackend } from "deepagents";
import { MemorySaver } from "@langchain/langgraph";

// Checkpointer is REQUIRED for human-in-the-loop
const checkpointer = new MemorySaver();

const agent = await createDeepAgent({
  model: "baseten:zai-org/GLM-5.2",
  backend: new FilesystemBackend({ rootDir: "/Users/user/{project}" }),
  memory: ["./AGENTS.md", "./.deepagents/AGENTS.md"],
  interruptOn: {
    read_file: true,
    write_file: true,
    delete_file: true,
  },
  checkpointer, // Required!
});
```

**Ollama**

```ts
import { createDeepAgent, FilesystemBackend } from "deepagents";
import { MemorySaver } from "@langchain/langgraph";

// Checkpointer is REQUIRED for human-in-the-loop
const checkpointer = new MemorySaver();

const agent = await createDeepAgent({
  model: "ollama:north-mini-code-1.0",
  backend: new FilesystemBackend({ rootDir: "/Users/user/{project}" }),
  memory: ["./AGENTS.md", "./.deepagents/AGENTS.md"],
  interruptOn: {
    read_file: true,
    write_file: true,
    delete_file: true,
  },
  checkpointer, // Required!
});
```

## Structured output

Deep Agents support [structured output](../langchain/structured-output.md).

You can set a desired structured output schema by passing it as the `responseFormat` argument to the call to `createDeepAgent()`.
When the model generates the structured data, it's captured, validated, and returned in the 'structuredResponse' key of the agent's state.

```ts
import { tool } from "langchain";
import { TavilySearch } from "@langchain/tavily";
import { createDeepAgent } from "deepagents";
import { z } from "zod";

const internetSearch = tool(
  async ({
    query,
    maxResults = 5,
    topic = "general",
    includeRawContent = false,
  }: {
    query: string;
    maxResults?: number;
    topic?: "general" | "news" | "finance";
    includeRawContent?: boolean;
  }) => {
    const tavilySearch = new TavilySearch({
      maxResults,
      tavilyApiKey: process.env.TAVILY_API_KEY,
      includeRawContent,
      topic,
    });
    return await tavilySearch._call({ query });
  },
  {
    name: "internet_search",
    description: "Run a web search",
    schema: z.object({
      query: z.string().describe("The search query"),
      maxResults: z.number().optional().default(5),
      topic: z
        .enum(["general", "news", "finance"])
        .optional()
        .default("general"),
      includeRawContent: z.boolean().optional().default(false),
    }),
  },
);

const weatherReportSchema = z.object({
  location: z.string().describe("The location for this weather report"),
  temperature: z.number().describe("Current temperature in Celsius"),
  condition: z
    .string()
    .describe("Current weather condition (e.g., sunny, cloudy, rainy)"),
  humidity: z.number().describe("Humidity percentage"),
  windSpeed: z.number().describe("Wind speed in km/h"),
  forecast: z.string().describe("Brief forecast for the next 24 hours"),
});

const agent = await createDeepAgent({
  responseFormat: weatherReportSchema,
  tools: [internetSearch],
});

const result = await agent.invoke({
  messages: [
    {
      role: "user",
      content: "What's the weather like in San Francisco?",
    },
  ],
});

console.log(result.structuredResponse);
// {
//   location: 'San Francisco, California',
//   temperature: 18.3,
//   condition: 'Sunny',
//   humidity: 48,
//   windSpeed: 7.6,
//   forecast: 'Clear skies with temperatures remaining mild. High of 18°C (64°F) during the day, dropping to around 11°C (52°F) at night.'
// }
```

#### [View example trace](https://smith.langchain.com/public/e4587886-ebb6-4fbc-8b57-d41b27180770/r)
Open a public LangSmith run for this example.

For more information and examples, see [response format](../langchain/structured-output.md#response-format).

## Advanced

`createDeepAgent` pre-assembles a middleware stack on top of `createAgent`. To build a fully custom agent—choosing exactly which capabilities to include—see [Configure the harness](../langchain/agents.md#configure-the-harness).

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/customization.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
