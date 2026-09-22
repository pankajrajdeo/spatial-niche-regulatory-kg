---
title: "Trace Claude Managed Agents"
description: "Automatically trace Claude Managed Agent sessions and events with LangSmith."
source: "https://docs.langchain.com/langsmith/trace-with-claude-managed-agents"
category: "docs"
tags: [docs, langsmith, trace-with-claude-managed-agents]
---

# Trace Claude Managed Agents

> Automatically trace Claude Managed Agent sessions and events with LangSmith.

[Claude Managed Agents](https://docs.anthropic.com/en/docs/claude-code/managed-agents) are Anthropic's hosted, cloud-based agents that run in managed environments. LangSmith supports tracing Claude Managed Agent sessions via the `wrapAnthropic` wrapper, giving you visibility into agent creation, session events, and message flows.

> [!NOTE]
> Claude Managed Agents tracing is currently supported in **TypeScript only**.

## Installation

**npm**

```bash
npm install langsmith @anthropic-ai/sdk
```

**yarn**

```bash
yarn add langsmith @anthropic-ai/sdk
```

## Environment setup

**Shell**

```bash
export LANGSMITH_TRACING=true
export LANGSMITH_API_KEY=<your-langsmith-api-key>
export ANTHROPIC_API_KEY=<your-anthropic-api-key>
```

## Trace Claude Managed Agents

Wrap the Anthropic client with `wrapAnthropic`. The wrapper will automatically trace agent creation, session creation, and all events that flow through the session.

**TypeScript**

```typescript
import Anthropic from "@anthropic-ai/sdk";
import { wrapAnthropic } from "langsmith/wrappers/anthropic";

const anthropic = wrapAnthropic(new Anthropic());

// Create a managed agent
const agent = await anthropic.beta.agents.create({
  name: "my-agent",
  model: "claude-opus-4-8",
  system: "You are a helpful assistant.",
  tools: [
    // ... your tools here
  ],
});

// Create a cloud environment for the agent to run in
const environment = await anthropic.beta.environments.create({
  name: "my-environment",
  config: {
    type: "cloud",
    networking: { type: "unrestricted" },
  },
});

// Create a session connecting the agent and environment
const session = await anthropic.beta.sessions.create({
  agent: agent.id,
  environment_id: environment.id,
  title: "My session",
});

// Stream session events
const stream = await anthropic.beta.sessions.events.stream(session.id);

// Send a message to the agent
await anthropic.beta.sessions.events.send(session.id, {
  events: [
    {
      type: "user.message",
      content: [
        {
          type: "text",
          text: "Hello! Can you help me with something?",
        },
      ],
    },
  ],
});

// Consume the event stream until the session is idle
for await (const event of stream) {
  if (event.type === "session.status_idle") {
    break;
  }
}
```

> [!NOTE]
> Full tracing of subagents in Anthropic's multi-agent architecture requires
> tapping into a separate event stream and is not yet supported. Only top-level
> session events are traced.

## Next steps

* [Trace Anthropic models](trace-anthropic.md) — trace standard Anthropic API calls and tool use
* [Trace Claude Agent SDK applications](trace-claude-agent-sdk.md) — trace the Claude Agent SDK for local agentic apps
* [Monitor your agent](dashboards.md) — set up dashboards and alerts for production agents

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-claude-managed-agents.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
