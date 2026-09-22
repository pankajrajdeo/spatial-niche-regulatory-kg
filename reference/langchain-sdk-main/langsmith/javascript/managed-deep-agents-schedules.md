---
title: "Add schedules to Managed Deep Agents"
description: "Declare managed cron schedules for Managed Deep Agents deployments."
source: "https://docs.langchain.com/langsmith/javascript/managed-deep-agents-schedules"
category: "docs"
tags: [docs, langsmith, javascript, managed-deep-agents-schedules]
---

# Add schedules to Managed Deep Agents

> Declare managed cron schedules for Managed Deep Agents deployments.

Managed Deep Agents can run agents on a cron schedule. When you deploy the project, `mda deploy` provisions each schedule as a LangSmith cron after the deployment is live.

> [!NOTE]
> Managed Deep Agents is in **public [beta](../release-stages.md)** and available on [LangSmith Cloud](../cloud.md) in the US region only.

## Project structure

Schedule declarations live in the project-level `schedules/` directory, with one schedule per file:

```text
my-agent/
  agent.ts
  schedules/
    daily-digest.ts
```

## Add a schedule

The file name becomes the managed schedule name.

The schedule module must export a named `schedule` declaration.

**schedules/daily-digest.ts**

```ts
import { defineSchedule } from "managed-deepagents";

export const schedule = defineSchedule({
  cron: "0 8 * * 1-5",
  timezone: "America/Los_Angeles",
  prompt: "Write the daily digest.",
});
```

## Configure schedule input

Each schedule must define exactly one of:

* `prompt`: A natural-language prompt. Managed Deep Agents converts it to a user message when the cron fires.
* `input`: A structured LangGraph input object. Use this when you need to pass custom graph input instead of a single prompt.

**schedules/nightly-sweep.ts**

```ts
import { defineSchedule } from "managed-deepagents";

export const schedule = defineSchedule({
  cron: "30 2 * * *",
  input: {
    messages: [
      { role: "user", content: "Sweep stale tickets and summarize changes." },
    ],
  },
});
```

`cron` must be a standard five-field cron expression: minute, hour, day of month, month, and day of week. If `timezone` is omitted, LangSmith crons use UTC.

## Choose thread behavior

Schedules use ephemeral threads by default. Managed Deep Agents creates a fresh thread for each run and asks LangSmith to delete that temporary thread after the run completes.

Use a persistent thread only when scheduled runs should accumulate durable thread state across invocations.

> [!NOTE]
> The following example requires [durable memory](managed-deep-agents-memory.md).

**schedules/nightly-memory.ts**

```ts
import { defineSchedule } from "managed-deepagents";

export const schedule = defineSchedule({
  cron: "0 3 * * *",
  prompt: "Review the current project memory and list follow-up tasks.",
  thread: { mode: "persistent", id: "nightly-memory" },
});
```

## Deliver results to Slack

Set `deliverTo` to post the final response through a configured [Slack channel](managed-deep-agents-channels-slack.md).

Use a Slack channel ID because scheduled runs have no originating thread.

> [!NOTE]
> Schedule delivery requires `managed-deepagents` version 0.4.0 or later.

**schedules/monday-greeting.ts**

```ts
import { defineSchedule } from "managed-deepagents";

export const schedule = defineSchedule({
  cron: "0 9 * * 1",
  prompt: "Write a short Monday greeting.",
  deliverTo: {
    channel: "slack",
    to: {
      type: "provider_conversation",
      conversationId: "C0123456789",
    },
  },
});
```

The Slack bot must have access to the destination.

## Use static declarations

Schedule declarations are extracted at compile time. Keep schedule configuration statically serializable:

* Use literals, arrays, objects, and references to top-level literal constants.

* Do not read environment variables, call functions, spread objects, or compute schedule values dynamically.

* Put dynamic behavior in the agent, tools, middleware, or runtime context instead.

## Deploy schedules

Test the project locally with [`mda dev`](managed-deep-agents-cli.md#develop-locally), then deploy it with [`mda deploy`](managed-deep-agents-deploy.md). Open deployment traces in LangSmith to inspect model calls, tool calls, errors, and latency.

When the deployment reaches `DEPLOYED`, `mda deploy` searches for existing Managed Deep Agents-owned cron jobs on the deployed Agent Server, deletes them, and creates cron jobs for the current `schedules/` declarations. Removing a local schedule file and redeploying removes the corresponding managed cron.

> [!WARNING]
> If you deploy with `--no-wait`, the CLI triggers the remote build and exits before the deployment reaches `DEPLOYED`, so it does not reconcile schedules during that invocation. Run `mda deploy` without `--no-wait` when adding, changing, or removing schedules.

## Troubleshoot schedules

* `must export a named schedule declaration`: Export a top-level `schedule` from each file in `schedules/`.

* `must define exactly one of prompt or input`: Add either `prompt` or `input`, but not both.

* `cron must be a standard 5-field expression`: Use five cron fields, not seconds-based cron syntax.

* `schedule is not static`: Replace computed values with literals or top-level literal constants.

* `failed to create cron for schedule`: Open the deployment URL in LangSmith and confirm the deployed Agent Server is healthy.

## Next steps

#### [Deploy an agent](managed-deep-agents-deploy.md)
Deploy and reconcile schedule changes.

#### [CLI reference](managed-deep-agents-cli.md)
Look up `mda deploy` flags and troubleshooting.

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/managed-deep-agents-schedules.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
