---
title: "Add custom tools to Managed Deep Agents"
description: "Define authored tools for managed deep agents projects."
source: "https://docs.langchain.com/langsmith/javascript/managed-deep-agents-tools"
category: "docs"
tags: [docs, langsmith, javascript, managed-deep-agents-tools]
---

# Add custom tools to Managed Deep Agents

> Define authored tools for managed deep agents projects.

Custom tools are application code the agent can call for fetching real-time data, querying databases, executing code, and taking actions. Unlike [instructions](managed-deep-agents-instructions.md) and [skills](managed-deep-agents-skills.md), MDA does not discover them automatically.

To load tools from a remote MCP server, see [Connect to MCP servers](managed-deep-agents-mcp-connectors.md).

> [!NOTE]
> Managed Deep Agents is in **public [beta](../release-stages.md)** and available on [LangSmith Cloud](../cloud.md) in the US region only.

Put authored tools under `tools/`, import them into the agent entry, and pass them to the agent definition:

```text
my-agent/
  agent.ts
  tools/
    customer.ts
```

For the full project layout, see [Project structure](managed-deep-agents-project-structure.md).

To load tools from a remote MCP server without importing them into the agent entry, use an [MCP connector](managed-deep-agents-mcp-connectors.md) instead.

MCP connectors are declared under `tools/` as well, so the `tools/mcp.ts` file name is reserved for that declaration.

## Add a tool

Use authored tools for business logic, private APIs, database access, and other code that belongs in your agent project.

### Define a tool module
**tools/customer.ts**

```ts
import { tool } from "langchain";
import { z } from "zod";

export const lookupCustomer = tool(
  async ({ customerId }) => `Customer ${customerId} is on the enterprise plan.`,
  {
    name: "lookup_customer",
    description: "Look up a customer record by ID.",
    schema: z.object({
      customerId: z.string().describe("Customer ID from the CRM."),
    }),
  },
);
```

Use clear, unique tool names to avoid collisions. For more about LangChain tool definitions, see [Tools](../../javascript/langchain/tools.md).

### Attach the tool to the agent
Import the tool into the project-root agent entry and pass it in the `tools` list:

**agent.ts**

```ts
import { defineDeepAgent } from "managed-deepagents";

import { lookupCustomer } from "./tools/customer";

export const agent = defineDeepAgent({
  name: "support-agent",
  model: "openai:gpt-5.5",
  tools: [lookupCustomer],
});
```

Your imports should work the same way they do in a normal local TypeScript project.

<a id="human-in-the-loop"></a>

### Add human-in-the-loop (Optional)
Pause the agent before sensitive tool calls so a person can approve, edit, or reject them.

Set `interruptOn` in the agent definition, and optionally set `permissions` to gate tool and filesystem access:

**agent.ts**

```ts
import { defineDeepAgent } from "managed-deepagents";

import { lookupCustomer } from "./tools/customer";

export const agent = defineDeepAgent({
  name: "support-agent",
  model: "openai:gpt-5.5",
  tools: [lookupCustomer],
  interruptOn: {
    lookup_customer: true,
  },
});
```

The `interruptOn` field applies the same interrupt behavior as LangChain's [human-in-the-loop middleware](../../javascript/langchain/guardrails.md#human-in-the-loop).

For decision types (approve, edit, reject), conditional interrupts, and permission rules, see the Deep Agents [Human-in-the-loop](../../javascript/deepagents/human-in-the-loop.md) and [Permissions](../../javascript/deepagents/permissions.md) guides.

To resume a paused run, see [Respond to an interrupt](#respond-to-an-interrupt).

## Use secrets and context

Tools can read deployment secrets from environment variables. Put local values in `.env` for `mda dev`; `mda deploy` forwards non-reserved `.env` values as hosted deployment secrets.

For per-run values such as request metadata or feature flags, use the normal LangChain runtime context patterns for tools. See [how to access context from within your tools](../../javascript/langchain/tools.md#access-context).

## Deployment

`mda dev` and `mda deploy` copy project files into the compiled build, including modules under `tools/`. Tools are not synced to Context Hub; they ship with the agent code.

## When to use tools

| Concept                                                                        | Kind                  | How it reaches the agent                                                  |
| ------------------------------------------------------------------------------ | --------------------- | ------------------------------------------------------------------------- |
| **Tools**                                                                      | Application code      | Import and pass in the agent definition                                   |
| **[MCP connectors](managed-deep-agents-mcp-connectors.md)** | Managed configuration | Declared in the MCP module under `tools/`; no import into the agent entry |
| **[Skills](managed-deep-agents-skills.md)**                 | Managed context       | Procedures the agent loads when relevant                                  |
| **[Instructions](managed-deep-agents-instructions.md)**     | Managed context       | Always-on system prompt                                                   |

For more information, see [Project structure](managed-deep-agents-project-structure.md).

## Respond to an interrupt

When a run hits an interrupt, it pauses and waits for a human response before continuing.

* **During local development**, `mda dev` runs the agent in LangSmith Studio, which surfaces the interrupt so you can inspect the pending tool call and resume the run.

* **On a deployed agent**, resume the paused run through the LangGraph server API with a resume payload. See [Human-in-the-loop using server API](../add-human-in-the-loop.md).

> [!NOTE]
> During public beta, Managed Deep Agents is CLI-first and programmatic invocation is not yet documented. To resume runs programmatically from your own application, contact your LangChain team.

Human-in-the-loop needs durable thread state to pause and resume. The managed runtime owns the checkpointer, so no extra setup is required.

## Use tools that require authentication

If a tool requires an API key or OAuth token, use a connection to resolve the credential at runtime. See [Manage connections](managed-deep-agents-connections.md).

## Access runtime context

For per-run values such as request metadata or feature flags, use the normal LangChain runtime context patterns for tools. See [how to access context from within your tools](../../javascript/langchain/tools.md#access-context).

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/managed-deep-agents-tools.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
