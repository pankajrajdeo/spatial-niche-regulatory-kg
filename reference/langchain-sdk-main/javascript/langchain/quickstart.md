---
title: "Quickstart"
description: "Build your first agent in minutes"
source: "https://docs.langchain.com/oss/javascript/langchain/quickstart"
category: "docs"
tags: [docs, javascript, langchain, quickstart]
---

# Quickstart

> Build your first agent in minutes

This quickstart shows you how to create a fully functional AI agent in just a few minutes.

> **Prompt:** Build the LangChain quickstart agent
Build a basic LangChain agent in this working directory by following the LangChain quickstart.

## Step 1: Read the guide

Detect whether this project uses Python or TypeScript/JavaScript. Fetch and follow the matching page; treat it as the source of truth for package names, model strings, and code:

* Python: [https://docs.langchain.com/oss/python/langchain/quickstart.md](../../langchain/quickstart.md)
* TypeScript: [https://docs.langchain.com/oss/javascript/langchain/quickstart.md](quickstart.md)

## Step 2: Install dependencies

Install the packages from the guide with the package manager already used in this project (`uv`, `pip`, `npm`, `pnpm`, `yarn`, or `bun`). Prefer pinning current stable versions over a floating `latest` tag when the project already pins versions.

## Step 3: Configure model credentials

Check whether a supported provider API key is already set (for example `OPENAI_API_KEY`, `GOOGLE_API_KEY`, or `ANTHROPIC_API_KEY`). If none is set, ask the user which provider to use, then stop and wait while they create a key and set it in the shell or a `.env` file. Do not invent, hardcode, or commit API keys.

## Step 4: Implement the basic agent

Create the "Build a basic agent" example from the guide: `create_agent`, a simple tool such as `get_weather`, a short system prompt, and an `invoke` call. Use a model string for the provider the user chose. Print the final message content (Python: `.content_blocks`) so the user can verify the run.

## Step 5: Optional LangSmith tracing

Ask the user if they want tracing. If yes, ask them to set `LANGSMITH_TRACING=true` and `LANGSMITH_API_KEY` themselves, then re-run. Do not invent a LangSmith key.

## Rules

* Stay scoped to this quickstart. Do not add unrelated frameworks, evals, or production deployment.
* Prefer `create_agent` from `langchain.agents` / `langchain` as shown in the guide.
* Ask rather than guess when a secret, provider choice, or project convention is unclear.

> [!TIP]
> **Using an AI coding assistant?**
>
> * Install the [LangChain Docs MCP servers](../../use-these-docs.md) to give your agent access to up-to-date LangChain documentation and examples.
>
> > **Prompt:** Connect LangChain docs MCP servers
>     Connect both LangChain documentation MCP servers to my coding agent so it can look up current LangChain, LangGraph, and LangSmith docs and API reference.
>
>     Servers to add:
>
>     * `docs-langchain`: [https://docs.langchain.com/mcp](https://docs.langchain.com/mcp)
>     * `reference-langchain`: [https://reference.langchain.com/mcp](https://reference.langchain.com/mcp)
>
>     Detect which agent or editor I am using (Claude Code, Cursor, Codex CLI, Claude Desktop, Deep Agents Code, VS Code, Antigravity, or another MCP-compatible client). Use the matching setup from [https://docs.langchain.com/use-these-docs.md](../../use-these-docs.md):
>
>     * Claude Code: `claude mcp add --transport http` for each server (project scope by default; use `--scope user` only if I ask for global access).
>     * Codex CLI: `codex mcp add` with each server URL.
>     * Cursor, Deep Agents Code, VS Code, or Antigravity: merge both entries into the MCP settings JSON using the field names shown on that page for my client.
>     * Claude Desktop: add both URLs under Settings > Connectors.
>
>     Do not invent alternate MCP URLs. After configuring, confirm both servers are listed and reachable.
> * Install [LangChain Skills](https://github.com/langchain-ai/langchain-skills) to improve your agent's performance on LangChain ecosystem tasks.
>
> > **Prompt:** Install LangChain Skills
>     Install LangChain Skills for my coding agent so it can perform better on LangChain, LangGraph, and Deep Agents tasks.
>
>     Use the Agent Skills installer from [https://github.com/langchain-ai/langchain-skills](https://github.com/langchain-ai/langchain-skills):
>
> ```bash
>     npx skills add langchain-ai/langchain-skills --skill '*' --yes
> ```
>
>     If I ask for a global install instead, use:
>
> ```bash
>     npx skills add langchain-ai/langchain-skills --skill '*' --yes --global
> ```
>
>     Detect which agent or editor I am using. If I use Claude Code and prefer the plugin path, follow the marketplace install from that repository README (`/plugin marketplace add` then `/plugin install`). Do not invent alternate skill package names or install URLs. After installing, confirm the skills are available to the agent.

## Install dependencies

Install the following packages to follow along:

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

## Set up API keys

Get an API key from [any supported model provider](../integrations/providers/overview.md) (for example, Google Gemini or OpenAI).

Set the API keys in your shell or in a `.env` file, for example:

#### OpenAI
**Shell**

```bash
export OPENAI_API_KEY="your-api-key"
```

**.env**

```bash
OPENAI_API_KEY=your-api-key
```

#### Google Gemini
**Shell**

```bash
export GOOGLE_API_KEY="your-api-key"
```

**.env**

```bash
GOOGLE_API_KEY=your-api-key
```

#### Claude (Anthropic)
**Shell**

```bash
export ANTHROPIC_API_KEY="your-api-key"
```

**.env**

```bash
ANTHROPIC_API_KEY=your-api-key
```

#### OpenRouter
**Shell**

```bash
export OPENROUTER_API_KEY="your-api-key"
```

**.env**

```bash
OPENROUTER_API_KEY=your-api-key
```

#### Fireworks
**Shell**

```bash
export FIREWORKS_API_KEY="your-api-key"
```

**.env**

```bash
FIREWORKS_API_KEY=your-api-key
```

#### Baseten
**Shell**

```bash
export BASETEN_API_KEY="your-api-key"
```

**.env**

```bash
BASETEN_API_KEY=your-api-key
```

#### Ollama
**Shell**

```bash
# Local: Ollama must be running (https://ollama.com)
# Cloud: Set your Ollama API key for hosted inference
export OLLAMA_API_KEY="your-api-key"
```

**.env**

```bash
# Local: Ollama must be running (https://ollama.com)
# Cloud: Set your Ollama API key for hosted inference
OLLAMA_API_KEY=your-api-key
```

#### Azure
**Shell**

```bash
export AZURE_OPENAI_API_KEY="your-api-key"
export AZURE_OPENAI_ENDPOINT="https://your-resource.openai.azure.com"
export AZURE_OPENAI_DEPLOYMENT_NAME="your-deployment"
```

**.env**

```bash
AZURE_OPENAI_API_KEY=your-api-key
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_DEPLOYMENT_NAME=your-deployment
```

#### AWS Bedrock
**Shell**

```bash
export AWS_ACCESS_KEY_ID="your-access-key"
export AWS_SECRET_ACCESS_KEY="your-secret-key"
export AWS_REGION="us-east-1"
```

**.env**

```bash
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
AWS_REGION=us-east-1
```

#### HuggingFace
**Shell**

```bash
export HUGGINGFACEHUB_API_TOKEN="hf_..."
```

**.env**

```bash
HUGGINGFACEHUB_API_TOKEN=hf_...
```

#### Other
See the full list of supported [chat model integrations](../integrations/chat.md).

To load a `.env` file, use [`dotenv`](https://www.npmjs.com/package/dotenv) (`import "dotenv/config"`).

> [!TIP]
> **Using LangSmith Gateway**
>
> The [LangSmith Gateway](../../langsmith/llm-gateway.md) routes most major providers through LangSmith. You can [bring your own provider keys](../../langsmith/llm-gateway-quickstart.md#send-a-request), or use [Gateway Credits](../../langsmith/llm-gateway-credits.md) to access models without a provider key.

## Build a basic agent

Start by creating a simple agent that can answer questions and call tools. The agent in this example uses the chosen language model, a basic weather function as a tool, and a simple prompt to guide its behavior:

**OpenAI**

```ts
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

When you run the code and prompt the agent to tell you about the weather in San Francisco, the agent uses that input and its available context.
The agent understands that you are asking about the weather for the city San Francisco and therefore calls the weather tool with the provided city name.

> [!TIP]
> You can use [any supported model](../integrations/providers/overview.md) by changing the model name and setting up the appropriate API key. Trace what is happening inside your agent with [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-langchain-quickstart). Follow the [tracing quickstart](../../langsmith/trace-with-langchain.md) to get set up.
>
> We recommend you also set up [LangSmith Engine](../../langsmith/engine.md) which monitors your traces, detects issues, and proposes fixes.

## Build a real-world agent

In the following example you will build a research agent that can answer questions about text files.
Along the way you will explore the following concepts:

1. **Detailed system prompts** for better agent behavior
2. **Create tools** that integrate with external data
3. **Model configuration** for consistent responses
4. **Conversational memory** for chat-like interactions
5. **Deep Agents** for built-in features
6. **Testing** your agent

### Define the system prompt
The system prompt defines your agent’s role and behavior. Keep it specific and actionable:

```ts
const SYSTEM_PROMPT = `You are a literary data assistant.

## Capabilities

- \`fetch_text_from_url\`: loads document text from a URL into the conversation.
Do not guess line counts or positions—ground them in tool results from the saved file.`;
```

### Create tools
[Tools](tools.md) let a model interact with external systems by calling functions you define.
Tools can depend on [runtime context](runtime.md) and also interact with [agent memory](short-term-memory.md).

This example uses a tool to load a document from a given URL:

```ts
import { tool } from "@langchain/core/tools";
import { createAgent, initChatModel } from "langchain";
import { z } from "zod";

const fetchTextFromUrl = tool(
    async ({ url }: { url: string }): Promise<string> => {
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), 120_000);
        try {
            const resp = await fetch(url, {
                headers: {
                "User-Agent": "Mozilla/5.0 (compatible; quickstart-research/1.0)",
                },
                signal: controller.signal,
            });
            if (!resp.ok) {
                return `Fetch failed: HTTP ${resp.status} ${resp.statusText}`;
            }
            return await resp.text();
        } catch (e) {
            const msg = e instanceof Error ? e.message : String(e);
            return `Fetch failed: ${msg}`;
        } finally {
            clearTimeout(timeoutId);
        }
    },
    {
        name: "fetch_text_from_url",
        description: "Fetch the document from a URL.",
        schema: z.object({ url: z.string().url() }),
    },
);
```

> [!NOTE]
> [Zod](https://zod.dev/) is a library for validating and parsing pre-defined schemas. You can use it to define the input schema for your tools to make sure the agent only calls the tool with the correct arguments.
>
> Alternatively, you can define the `schema` property as a [JSON schema](https://json-schema.org/overview/what-is-jsonschema) object. Keep in mind that JSON schemas **won't** be validated at runtime.
>
> <details>
> <summary>Example: Using JSON schema for tool input</summary>
>
> ```ts
> import { tool } from "@langchain/core/tools";
>
> const fetchTextFromUrl = tool(
> async ({ url }: { url: string }): Promise<string> => {
>     const controller = new AbortController();
>     const timeoutId = setTimeout(() => controller.abort(), 120_000);
>     try {
>     const resp = await fetch(url, {
>         headers: {
>         "User-Agent": "Mozilla/5.0 (compatible; quickstart-research/1.0)",
>         },
>         signal: controller.signal,
>     });
>     if (!resp.ok) {
>         return `Fetch failed: HTTP ${resp.status} ${resp.statusText}`;
>     }
>     return await resp.text();
>     } catch (e) {
>     const msg = e instanceof Error ? e.message : String(e);
>     return `Fetch failed: ${msg}`;
>     } finally {
>     clearTimeout(timeoutId);
>     }
> },
> {
>     name: "fetch_text_from_url",
>     description: "Fetch the document from a URL.",
>     schema: {
>     type: "object",
>     properties: {
>         url: {
>         type: "string",
>         description: "The URL of the document to fetch.",
>         format: "uri",
>         },
>     },
>     required: ["url"],
>     },
> },
> );
> ```
>
> </details>

### Configure your model
Set up your [language model](models.md) with the right parameters for your use case. For example:

**OpenAI**

```ts
import { initChatModel } from "langchain";

const model = await initChatModel("gpt-5.5", {
  temperature: 0.5,
  timeout: 300,
  maxTokens: 25000,
});
```

**Google Gemini**

```ts
import { initChatModel } from "langchain";

const model = await initChatModel("gemini-3.1-pro-preview", {
  modelProvider: "google-genai",
  temperature: 0.5,
  timeout: 600_000,
  maxTokens: 25000,
});
```

**Claude (Anthropic)**

```ts
import { initChatModel } from "langchain";

const model = await initChatModel("claude-sonnet-4-6", {
  temperature: 0.5,
  timeout: 300,
  maxTokens: 25000,
});
```

**OpenRouter**

```ts
import { initChatModel } from "langchain";

const model = await initChatModel("openrouter:anthropic/claude-sonnet-4-6", {
  temperature: 0.5,
  timeout: 300,
  maxTokens: 25000,
});
```

**Fireworks**

```ts
import { initChatModel } from "langchain";

const model = await initChatModel(
  "fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
  { temperature: 0.5, timeout: 300, maxTokens: 25000 }
);
```

**Baseten**

```ts
import { initChatModel } from "langchain";

const model = await initChatModel("baseten:zai-org/GLM-5.2", {
  temperature: 0.5,
  timeout: 300,
  maxTokens: 25000,
});
```

**Ollama**

```ts
import { initChatModel } from "langchain";

const model = await initChatModel("ollama:devstral-2", {
  temperature: 0.5,
  timeout: 300,
  maxTokens: 25000,
});
```

**Azure**

```ts
import { initChatModel } from "langchain";

const model = await initChatModel("azure_openai:gpt-5.5", {
  temperature: 0.5,
  timeout: 300,
  maxTokens: 25000,
});
```

**AWS Bedrock**

```ts
import { initChatModel } from "langchain";

const model = await initChatModel("bedrock:gpt-5.5", {
  temperature: 0.5,
  timeout: 300,
  maxTokens: 25000,
});
```

Depending on the model and provider chosen, initialization parameters may vary; refer to their reference pages for details.

### Add memory
Add [memory](short-term-memory.md) to your agent to maintain state across interactions. This allows
the agent to remember previous conversations and context.

```ts
import { MemorySaver } from "@langchain/langgraph";

const checkpointer = new MemorySaver();
```

> [!NOTE]
> In production, use a persistent checkpointer that saves message history to a database.
> See [Add and manage memory](../langgraph/add-memory.md#manage-short-term-memory) for more details.

### Create and run the agent
Now assemble your agent with all the components and run it.

There are two different frameworks for creating agents: LangChain agents and deep agents.
Both LangChain and deep agents provide you with fine-grained control over tools, memory, and more.
The main difference between both is that deep agents come with a range of commonly useful capabilities already built in, such as planning, file system tools, and subagents.

Use deep agents when you want maximum capability with minimal setup; choose LangChain agents when you need fine-grained control.

To compare both in this step, install the `deepagents` package:

**npm**

```bash
npm install deepagents
```

**pnpm**

```bash
pnpm add deepagents
```

**yarn**

```bash
yarn add deepagents
```

**bun**

```bash
bun add deepagents
```

> [!WARNING]
> This example sends the entire text of The Great Gatsby to the model and may take a minute or two to respond. You can view example output in the next step.

Let's try both:

```ts
async function main() {
    const agent = createAgent({
        model,
        tools: [fetchTextFromUrl],
        systemPrompt: SYSTEM_PROMPT,
        checkpointer,
    });

    const deepAgent = createDeepAgent({
        model,
        tools: [fetchTextFromUrl],
        systemPrompt: SYSTEM_PROMPT,
        checkpointer,
    });

    const content = `Project Gutenberg hosts a full plain-text copy of F. Scott Fitzgerald's The Great Gatsby.
    URL: https://www.gutenberg.org/files/64317/64317-0.txt

    Answer as much as you can:

    1) How many lines in the complete Gutenberg file contain the substring \`Gatsby\` (count lines, not occurrences within a line, each line ends with a line break).
    2) The 1-based line number of the first line in the file that contains \`Daisy\`.
    3) A two-sentence neutral synopsis.

    Do your best on (1) and (2). If at any point you realize you cannot **verify** an exact answer with
    your available tools and reasoning, do not fabricate numbers: use \`null\` for that field and spell out
    the limitation in \`how_you_computed_counts\`. If you encounter any errors please report what the error was and what the error message was.`;

    console.log("Running createAgent...");
    const agentResult = await agent.invoke(
        { messages: [{ role: "user", content }] },
        { configurable: { thread_id: "great-gatsby-lc" } },
    );
    console.log("Running createDeepAgent...");
    const deepAgentResult = await deepAgent.invoke(
        { messages: [{ role: "user", content }] },
        { configurable: { thread_id: "great-gatsby-da" } },
    );

    const agentMessages = agentResult.messages;
    const deepMessages = deepAgentResult.messages;
    console.log("\ncreateAgent:");
    console.log(agentMessages[agentMessages.length - 1]!.contentBlocks);
    console.log("\ncreateDeepAgent:");
    console.log(deepMessages[deepMessages.length - 1]!.contentBlocks);
}

main().catch((err) => {
    console.error(err);
    process.exitCode = 1;
});
```

The following expander has everything together in a runnable script:

**Full example code**
```ts
import { MemorySaver } from "@langchain/langgraph";
import { createDeepAgent } from "deepagents";
import { tool } from "@langchain/core/tools";
import { createAgent, initChatModel } from "langchain";
import { z } from "zod";
const SYSTEM_PROMPT = `You are a literary data assistant.

## Capabilities

- \`fetch_text_from_url\`: loads document text from a URL into the conversation.
Do not guess line counts or positions—ground them in tool results from the saved file.`;

const fetchTextFromUrl = tool(
    async ({ url }: { url: string }): Promise<string> => {
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), 120_000);
        try {
            const resp = await fetch(url, {
                headers: {
                    "User-Agent": "Mozilla/5.0 (compatible; quickstart-research/1.0)",
                },
                signal: controller.signal,
            });
            if (!resp.ok) {
                return `Fetch failed: HTTP ${resp.status} ${resp.statusText}`;
            }
            return await resp.text();
        } catch (e) {
            const msg = e instanceof Error ? e.message : String(e);
            return `Fetch failed: ${msg}`;
        } finally {
           clearTimeout(timeoutId);
        }
    },
    {
        name: "fetch_text_from_url",
        description: "Fetch the document from a URL.",
        schema: z.object({ url: z.string().url() }),
    },
);

const model = await initChatModel("gemini-3.1-pro-preview", {
    modelProvider: "google-genai",
    temperature: 0.5,
    timeout: 600_000,
    maxTokens: 25000,
    streaming: true,
});

const checkpointer = new MemorySaver();

async function main() {
    const agent = createAgent({
        model,
        tools: [fetchTextFromUrl],
        systemPrompt: SYSTEM_PROMPT,
        checkpointer,
    });

    const deepAgent = createDeepAgent({
        model,
        tools: [fetchTextFromUrl],
        systemPrompt: SYSTEM_PROMPT,
        checkpointer,
    });

    const content = `Project Gutenberg hosts a full plain-text copy of F. Scott Fitzgerald's The Great Gatsby.
    URL: https://www.gutenberg.org/files/64317/64317-0.txt

    Answer as much as you can:

    1) How many lines in the complete Gutenberg file contain the substring \`Gatsby\` (count lines, not occurrences within a line, each line ends with a line break).
    2) The 1-based line number of the first line in the file that contains \`Daisy\`.
    3) A two-sentence neutral synopsis.

    Do your best on (1) and (2). If at any point you realize you cannot **verify** an exact answer with
    your available tools and reasoning, do not fabricate numbers: use \`null\` for that field and spell out
    the limitation in \`how_you_computed_counts\`. If you encounter any errors please report what the error was and what the error message was.`;

    console.log("Running createAgent...");
    const agentResult = await agent.invoke(
        { messages: [{ role: "user", content }] },
        { configurable: { thread_id: "great-gatsby-lc" } },
    );
    console.log("Running createDeepAgent...");
    const deepAgentResult = await deepAgent.invoke(
        { messages: [{ role: "user", content }] },
        { configurable: { thread_id: "great-gatsby-da" } },
    );

    const agentMessages = agentResult.messages;
    const deepMessages = deepAgentResult.messages;
    console.log("\ncreateAgent:");
    console.log(agentMessages[agentMessages.length - 1]!.contentBlocks);
    console.log("\ncreateDeepAgent:");
    console.log(deepMessages[deepMessages.length - 1]!.contentBlocks);
}

main().catch((err) => {
    console.error(err);
    process.exitCode = 1;
});
```

### Review the results
The results will differ based on the model and the execution.

#### LangChain agents
```txt
**1) Number of lines containing `Gatsby`:** `null`

**2) First line containing `Daisy`:** `null`

**3) Synopsis:**
The Great Gatsby follows the mysterious millionaire Jay Gatsby and his obsession with reuniting with his former lover, Daisy Buchanan, as narrated by his neighbor Nick Carraway. Set against the backdrop of the Roaring Twenties on Long Island, the novel explores themes of wealth, class, and the elusive nature of the American Dream.

**how_you_computed_counts:**
I successfully fetched the full text of the eBook using the `fetch_text_from_url` tool. However, because I do not have access to a code execution environment (like Python) or text-processing tools (like `grep`), I cannot deterministically split the text by line breaks, iterate through the thousands of lines, and verify the exact line numbers or match counts. LLMs cannot reliably perform exact line-counting or indexing over massive texts within their context window without external computational tools. As instructed, rather than fabricating or guessing a number, I have output `null` for the exact counts and positions.
```

#### Deep agents
```txt
Based on the text fetched directly from the Gutenberg URL and analyzed using filesystem search tools, here are the answers to your questions:

**1) Lines containing the substring `Gatsby`**
**258** lines contain the exact substring `Gatsby`.

**2) First line containing `Daisy`**
Line **181** is the first line in the file that contains the exact substring `Daisy`.
*(For context, the line reads: "Buchanans. Daisy was my second cousin once removed, and I’d known Tom")*

**3) Two-sentence neutral synopsis**
*The Great Gatsby* follows the mysterious millionaire Jay Gatsby and his obsessive pursuit to reunite with his former lover, Daisy Buchanan, in 1920s Long Island. The story is narrated by Nick Carraway, who observes the tragic consequences of Gatsby's relentless ambition and the shallow materialism of the era's wealthy elite.

***

**How counts were computed:**
When fetching the document from the URL, the file was too large for the standard output and was automatically saved to the local filesystem by the system (`/large_tool_results/x246ax2x`). I then used the `grep` tool to search the saved file for the exact literal substrings `Gatsby` and `Daisy`. The `grep` tool returned every matching line along with its 1-based line number. I manually counted the exact number of lines returned for `Gatsby` (which totaled 258) and identified the first line number returned for `Daisy` (which was 181). I also verified there were no uppercase variations (`GATSBY` or `DAISY`) that would have been missed. No errors were encountered during this process.
```

If you look at the output on both tabs, you notice that the LangChain agent provided answers but they are estimates. The agent lacks the tools to answer this question. You may also get errors that the prompt is too long.

The deep agent, on the other hand can:

1. **Plans its approach** using the built-in [`write_todos`](../deepagents/harness.md#task-planning) tool to break down the research task.
2. **Loads the file** by calling the `fetch_text_from_url` tool to gather information.
3. **Manages context** by using file system tools ([`grep`](../deepagents/harness.md#virtual-filesystem-access) and [`read_file`](../deepagents/harness.md#virtual-filesystem-access)).
4. **Spawns subagents** as needed to delegate complex subtasks to specialized subagents.

For LangChain agents, you must implement more capabilities to get a similar level of service and can customize them along the way as needed.

## Trace agent calls

Most interesting applications you build with LangChain make many calls to LLMs. As these applications get more complex, it becomes important to be able to inspect what exactly is going on inside your agent. The best way to do this is with [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-langchain-quickstart).

Sign up for a [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-langchain-quickstart) account and set these to start logging traces:

```shell
export LANGSMITH_TRACING="true"
export LANGSMITH_API_KEY="..."
```

Once set, run your script again and then inspect what happened during your agent calls on [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-langchain-quickstart) .

> [!TIP]
> To learn more about tracing your agent with LangSmith, see the [LangSmith documentation](../../langsmith/trace-with-langchain.md).
>
> We recommend you also set up [LangSmith Engine](../../langsmith/engine.md) which monitors your traces, detects issues, and proposes fixes.

## Next steps

You now have agents that can:

* **Understand context** and remember conversations
* **Use tools** intelligently
* **Provide structured responses** in a consistent format
* **Handle user-specific information** through context
* **Maintain conversation state** across interactions
* **Plan, research, and synthesize** (deep agents only)

Continue with:

* **LangChain agents**: [Add and manage memory](../langgraph/add-memory.md#manage-short-term-memory), [deploy to production](../langgraph/deploy.md)
* **Deep Agents**: [Customization options](../deepagents/customization.md), [persistent memory](../deepagents/memory.md), [deploy to production](../langgraph/deploy.md)

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/quickstart.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
