---
title: "LangSmith Studio"
description: "When building agents with LangChain locally, it's helpful to visualize what's happening inside your agent, interact with it in real-time, and debug issues as they occur. LangSmith Studio is a free..."
source: "https://docs.langchain.com/oss/javascript/langchain/studio"
category: "docs"
tags: [docs, javascript, langchain, studio]
---

# LangSmith Studio

When building agents with LangChain locally, it's helpful to visualize what's happening inside your agent, interact with it in real-time, and debug issues as they occur. **LangSmith Studio** is a free visual interface for developing and testing your LangChain agents from your local machine.

Studio connects to your locally running agent to show you each step your agent takes: the prompts sent to the model, tool calls and their results, and the final output. You can test different inputs, inspect intermediate states, and iterate on your agent's behavior without additional code or deployment.

This pages describes how to set up Studio with your local LangChain agent.

## Prerequisites

Before you begin, ensure you have the following:

* **A LangSmith account**: Sign up (for free) or log in at [smith.langchain.com](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=snippets-oss-studio-js).
* **A LangSmith API key**: Follow the [Create an API key](../../langsmith/create-account-api-key.md) guide.
* If you don't want data [traced](../../langsmith/observability-concepts.md#traces) to LangSmith, set `LANGSMITH_TRACING=false` in your application's `.env` file. With tracing disabled, no data leaves your local server.

## Set up local Agent server

### 1. Install the LangGraph CLI

The [LangGraph CLI](../../langsmith/cli.md) provides a local development server (also called [Agent Server](../../langsmith/agent-server.md)) that connects your agent to Studio.

```shell
npx @langchain/langgraph-cli
```

### 2. Prepare your agent

If you already have a LangChain agent, you can use it directly. This example uses a simple email agent:

```typescript
import { createAgent } from "@langchain/agents";

function sendEmail(to: string, subject: string, body: string): string {
  const email = {
    to,
    subject,
    body,
  };
  // ... email sending logic

  return `Email sent to ${to}`;
}

const agent = createAgent({
  model: "gpt-5.5",
  tools: [sendEmail],
  systemPrompt: "You are an email assistant. Always use the send_email tool.",
});
```

### 3. Environment variables

Studio requires a LangSmith API key to connect your local agent. Create a `.env` file in the root of your project and add your API key from [LangSmith](https://smith.langchain.com/settings).

> [!WARNING]
> Ensure your `.env` file is not committed to version control, such as Git.

**.env**

```bash
LANGSMITH_API_KEY=lsv2...
```

### 4. Create a LangGraph config file

The LangGraph CLI uses a configuration file to locate your agent and manage dependencies. Create a `langgraph.json` file in your app's directory:

```json
{
  "dependencies": ["."],
  "graphs": {
    "agent": "./src/agent.ts:agent"
  },
  "env": ".env"
}
```

The [`createAgent`](https://reference.langchain.com/javascript/langchain/index/createAgent) function automatically returns a compiled LangGraph graph, which is what the `graphs` key expects in the configuration file.

> [!NOTE]
> For detailed explanations of each key in the JSON object of the configuration file, refer to the [LangGraph configuration file reference](../../langsmith/cli.md#configuration-file).

At this point, the project structure will look like this:

```bash
my-app/
├── src
│   └── agent.ts
├── .env
└── langgraph.json
```

### 5. Install dependencies

```shell
yarn install
```

### 6. View your agent in Studio

Start the development server to connect your agent to Studio:

```shell
npx @langchain/langgraph-cli dev
```

> [!WARNING]
> Safari blocks `localhost` connections to Studio. To work around this, run the above command with `--tunnel` to access Studio via a secure tunnel.

Once the server is running, your agent is accessible both via API at `http://127.0.0.1:2024` and through the Studio UI at `https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024`:

<img src="https://mintcdn.com/langchain-5e9cc07a/TCDks4pdsHdxWmuJ/oss/images/studio_create-agent.png?fit=max&auto=format&n=TCDks4pdsHdxWmuJ&q=85&s=ebd259e9fa24af7d011dfcc568f74be2" alt="Agent view in the Studio UI" width="2836" height="1752" data-path="oss/images/studio_create-agent.png" />

With Studio connected to your local agent, you can iterate quickly on your agent's behavior. Run a test input, inspect the full execution trace including prompts, tool arguments, return values, and token/latency metrics. When something goes wrong, Studio captures exceptions with the surrounding state to help you understand what happened.

The development server supports hot-reloading—make changes to prompts or tool signatures in your code, and Studio reflects them immediately. Re-run conversation threads from any step to test your changes without starting over. This workflow scales from simple single-tool agents to complex multi-node graphs.

For more information on how to run Studio, refer to the following guides in the [LangSmith docs](../../langsmith/observability.md):

* [Run application](../../langsmith/use-studio.md#run-application)
* [Manage assistants](../../langsmith/use-studio.md#manage-assistants)
* [Manage threads](../../langsmith/use-studio.md#manage-threads)
* [Iterate on prompts](../../langsmith/observability-studio.md)
* [Debug LangSmith traces](../../langsmith/observability-studio.md#debug-langsmith-traces)
* [Add node to dataset](../../langsmith/observability-studio.md#add-node-to-dataset)

## Video guide

> **Embedded Content:** [Studio](https://www.youtube.com/embed/Mi1gSlHwZLM?si=zA47TNuTC5aH0ahd)

> [!TIP]
> For more information about deployed agents, see [Deployment](deploy.md).

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/studio.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
