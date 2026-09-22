---
title: "Add a custom search tool, memory, and a schedule"
description: "Replace provider search with a Tavily tool, then add durable memory and a daily schedule to the research assistant from the quickstart."
source: "https://docs.langchain.com/langsmith/javascript/managed-deep-agents-tutorial"
category: "docs"
tags: [docs, langsmith, javascript, managed-deep-agents-tutorial]
---

# Add a custom search tool, memory, and a schedule

> Replace provider search with a Tavily tool, then add durable memory and a daily schedule to the research assistant from the quickstart.

This tutorial continues from the [quickstart](managed-deep-agents-quickstart.md). Use the `research-assistant` project you created there, with your model, instructions, and a working `mda dev` setup.

`mda init` may also scaffold files such as `identity` and `sandbox/`. Leave those as they are; this tutorial does not change them.

This guide replaces the quickstart's built-in provider search with an authored [Tavily](https://tavily.com) search tool, enables durable memory, adds a daily schedule, then deploys.

> [!NOTE]
> Managed Deep Agents is in **public [beta](../release-stages.md)** and available on [LangSmith Cloud](../cloud.md) in the US region only.

## Extend the agent

### Add a custom search tool
Built-in provider search is convenient for a first run. Authored tools give you more control: choose the search API, tune parameters, and keep the tool code in your project.

> [!NOTE]
> If you followed the steps to use Tavily in the [Quickstart](managed-deep-agents-quickstart.md), skip to the next step.

Add a [Tavily API key](https://app.tavily.com) to `.env`:

**.env**

```text
TAVILY_API_KEY=<TAVILY_API_KEY>
```

Install the Tavily client:

**npm**

```bash
npm install @langchain/tavily
```

**pnpm**

```bash
pnpm add @langchain/tavily
```

**bun**

```bash
bun add @langchain/tavily
```

Create a custom `internet_search` tool:

**tools/search.ts**

```ts
import { TavilySearch } from "@langchain/tavily";
import { tool } from "langchain";
import { z } from "zod";

export const internetSearch = tool(
  async ({ query, maxResults = 5, topic = "general" }) => {
    const tavilySearch = new TavilySearch({
      maxResults,
      tavilyApiKey: process.env.TAVILY_API_KEY,
      topic,
    });
    return tavilySearch._call({ query });
  },
  {
    name: "internet_search",
    description: "Search the internet for relevant sources.",
    schema: z.object({
      query: z.string().describe("The search query."),
      maxResults: z.number().optional().default(5),
      topic: z.enum(["general", "news", "finance"]).optional().default("general"),
    }),
  },
);
```

Replace the provider search tool dict with your authored tool. Keep the `model` value from the quickstart:

**agent.ts**

```ts
import { defineDeepAgent } from "managed-deepagents";

import { internetSearch } from "./tools/search";

export const agent = defineDeepAgent({
  name: "research-assistant",
  model: "openai:gpt-5.5",
  tools: [internetSearch],
});
```

Restart `mda dev` if it is already running. In Studio, ask:

```txt
What were the main announcements from the latest LangChain release?
```

Confirm the agent calls `internet_search` and returns an answer with citations. For more authored tools, see [Custom tools](managed-deep-agents-tools.md).

### Update the instructions for memory
Extend `instructions.md` so the agent knows what shared knowledge to keep. Keep the research behavior and add a memory policy:

**instructions.md**

```markdown
# Research assistant

You are a careful research assistant. Use internet search to find sources,
keep notes, and return concise answers with citations.

## Memory

- Record reusable research procedures and project knowledge that can improve future work.
- For release research, check the project's official changelog before secondary sources.
- Never store personal data or secrets in memory.
```

### Enable and use durable memory
Durable memory is opt-in. Before asking the agent to remember anything, add a memory declaration at the project root:

**memory.ts**

```ts
import { defineMemory } from "managed-deepagents";

export const memory = defineMemory({ scope: "agent" });
```

Memory is shared across the deployment and visible to all callers, so do not store personal data or secrets.

Restart `mda dev` so it discovers the new file. In one thread, ask the agent to research a release and to record a reusable project rule, such as "For release research, check the official changelog before secondary sources." Then create a **new thread** in Studio and ask how it will research the next release. Confirm that it applies the shared rule even though the new thread has no conversation history.

See [Memory](managed-deep-agents-memory.md) for details.

### Schedule a daily digest
Add a `schedules/` module so the agent runs on a cron cadence without a user message. This schedule runs every weekday at 8am Pacific:

**schedules/daily-digest.ts**

```ts
import { defineSchedule } from "managed-deepagents";

export const schedule = defineSchedule({
  cron: "0 8 * * 1-5",
  timezone: "America/Los_Angeles",
  prompt:
    "Review durable memory for reusable research rules. " +
    "Summarize anything useful, then list open questions for today.",
});
```

If memory is empty on the first fire, the agent still returns open questions.

`mda deploy` reconciles this schedule into a LangSmith cron job after the deployment is live. After you deploy in the next step, you should see:

* `mda deploy` finish without schedule errors (do not pass `--no-wait`, or schedules are not reconciled).
* A managed cron for this file on the deployment. The schedule name matches the module stem: `daily_digest` (Python) or `daily-digest` (TypeScript).
* No immediate digest run from this cron. The first fire waits until 8:00 America/Los\_Angeles on a weekday.

For thread behavior and constraints, see [Schedules](managed-deep-agents-schedules.md).

### Deploy and inspect
Deploy the project to LangSmith:

**npm**

```bash
npx mda deploy
```

**pnpm**

```bash
pnpm exec mda deploy
```

**bun**

```bash
bunx mda deploy
```

On success, the CLI prints the deployment dashboard URL. The deploy syncs the instructions to Context Hub, uploads the compiled project, and reconciles the daily schedule.

Open that URL and confirm:

* The deployment is ready.
* The `daily_digest` or `daily-digest` cron exists.
* A test chat run shows model calls, `internet_search` tool calls, and memory reads or writes in the traces.

For deploy flags and troubleshooting, see [Deploy an agent](managed-deep-agents-deploy.md) and the [CLI reference](managed-deep-agents-cli.md#deploy-projects).

## Next steps

#### [Custom middleware](managed-deep-agents-middleware.md)
Add logging, retries, limits, and guardrails around model and tool calls.

#### [Identity](managed-deep-agents-identity.md)
Authenticate callers and use verified identity in tools and middleware.

#### [Evals](managed-deep-agents-evals.md)
Develop Harbor evals with a coding agent and the eval-engineering skill.

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/managed-deep-agents-tutorial.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
