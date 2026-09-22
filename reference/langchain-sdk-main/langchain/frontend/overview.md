---
title: "Overview"
description: "Build generative UIs with real-time streaming from LangChain agents"
source: "https://docs.langchain.com/oss/python/langchain/frontend/overview"
category: "docs"
tags: [docs, langchain, frontend]
---

# Overview

> Build generative UIs with real-time streaming from LangChain agents

Build rich, interactive frontends for agents created with `createAgent`. These
patterns cover everything from basic message rendering to advanced workflows
like human-in-the-loop approval, queued submissions, durable stream rejoin, and
time travel debugging.

LangChain frontend SDKs are built for **agent applications**, not only
token-streaming chatbots. The same hook that renders messages also exposes the
agent's durable thread state, tool-call lifecycle, interrupts, checkpoint
history, and custom state values, so your UI can become a control plane for
long-running agent work.

> [!NOTE]
> These patterns use the v1 frontend SDK packages. If you are using an earlier version, see the migration guides for [React](https://github.com/langchain-ai/langgraphjs/blob/main/libs/sdk-react/docs/v1-migration.md), [Vue](https://github.com/langchain-ai/langgraphjs/blob/main/libs/sdk-vue/docs/v1-migration.md), [Svelte](https://github.com/langchain-ai/langgraphjs/blob/main/libs/sdk-svelte/docs/v1-migration.md), and [Angular](https://github.com/langchain-ai/langgraphjs/blob/main/libs/sdk-angular/docs/v1-migration.md).

## Architecture

Every pattern follows the same architecture: a `createAgent` backend streams state to a frontend via the SDK stream API.

```mermaid
%%{
  init: {
    "fontFamily": "monospace",
    "flowchart": {
      "curve": "curve"
    }
  }
}%%
graph LR
  FRONTEND["useStream()"]
  BACKEND["createAgent()"]

  BACKEND --"stream"--> FRONTEND
  FRONTEND --"submit"--> BACKEND

  classDef blueHighlight fill:#E5F4FF,stroke:#006DDD,color:#030710;
  classDef greenHighlight fill:#F6FFDB,stroke:#6E8900,color:#2E3900;
  class FRONTEND blueHighlight;
  class BACKEND greenHighlight;
```

On the backend, `createAgent` produces a compiled LangGraph graph that exposes a streaming API. On the frontend, the stream handle connects to that API and provides reactive state — messages, tool calls, interrupts, values, and thread metadata — that you render with any framework.

## Why use the LangChain frontend SDKs?

Most AI UI libraries help you append streamed text to a chat transcript.
LangChain's SDKs expose the richer runtime semantics that production agents
need:

| Capability                      | What it enables in your UI                                                                                                       |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **Durable threads**             | Reload a page, switch devices, or rejoin a run without losing the conversation state.                                            |
| **Typed agent state**           | Render any state key, not just messages: todos, pipeline outputs, citations, sandbox files, metrics, or custom business objects. |
| **Tool-call lifecycle**         | Show pending, completed, and failed tool calls as purpose-built UI cards instead of raw JSON.                                    |
| **Interrupts**                  | Pause execution for human approval, edits, or missing information, then resume from the exact point where the agent stopped.     |
| **Checkpoints**                 | Build edit, retry, branch, audit, and time-travel flows from persisted state snapshots.                                          |
| **Nested execution**            | Visualize deep agents, subagents, and graph nodes without flattening everything into one unreadable stream.                      |
| **Framework-native reactivity** | Use the same protocol from React, Vue, Svelte, or Angular while keeping idiomatic hooks, composables, stores, or signals.        |

These primitives let you design UIs where users can inspect, steer, pause,
resume, and fork agent work while it is happening.

**agent.py**

```python
from langchain import create_agent
from langgraph.checkpoint.memory import MemorySaver

agent = create_agent(
    model="openai:gpt-5.5",
    tools=[get_weather, search_web],
    checkpointer=MemorySaver(),
)
```

**types.ts**

```ts
export interface GraphState {
  messages: BaseMessage[];
}
```

**Chat.tsx**

```tsx
import { useStream } from "@langchain/react";
import type { GraphState } from "./types";

function Chat() {
  const stream = useStream<GraphState>({
    apiUrl: "http://localhost:2024",
    assistantId: "agent",
  });

  return (
    <div>
      {stream.messages.map((msg) => (
        <Message key={msg.id} message={msg} />
      ))}
    </div>
  );
}
```

React, Vue, and Svelte use `useStream`. Angular uses `injectStream`:

```ts
import { useStream } from "@langchain/react";      // React
import { useStream } from "@langchain/vue";        // Vue
import { useStream } from "@langchain/svelte";     // Svelte
import { injectStream } from "@langchain/angular"; // Angular
```

## Type inference

Pass a type parameter to [`useStream`](https://reference.langchain.com/javascript/langchain-react/index/useStream) (or [`injectStream`](https://reference.langchain.com/javascript/langchain-angular/injectStream) in Angular) for type-safe access to `stream.messages`, `stream.toolCalls`, `stream.interrupt`, `stream.values`, and other reactive state.

Define a TypeScript interface that matches your agent's state schema and pass it as the type parameter:

```ts
import type { BaseMessage } from "langchain";

interface AgentState {
  messages: BaseMessage[];
}

const stream = useStream<AgentState>({
  apiUrl: "http://localhost:2024",
  assistantId: "agent",
});
```

Use the graph name from `langgraph.json` as `assistantId`. In the pattern examples throughout this guide, replace `typeof myAgent` with your interface name (for example, `AgentState`).

If your agent exposes custom state keys, extend the interface:

```ts
import type { BaseMessage, Todo } from "langchain";

interface AgentState {
  messages: BaseMessage[];
  todos: Todo[];
}
```

## Patterns

### Render messages and output

#### [Markdown messages](markdown-messages.md)
Parse and render streamed markdown with proper formatting and code highlighting.

#### [Structured output](structured-output.md)
Render typed agent responses as custom UI components instead of plain text.

#### [Reasoning tokens](reasoning-tokens.md)
Display model thinking processes in collapsible blocks.

#### [Generative UI](generative-ui-overview.md)
Render agent-generated interfaces across the spectrum from controlled to declarative to open-ended.

### Display agent actions

#### [Tool calling](tool-calling.md)
Show tool calls as rich, type-safe UI cards with loading and error states.

#### [Headless tools](headless-tools.md)
Run browser and device APIs on the client while keeping typed tool schemas on the agent.

#### [Human-in-the-loop](human-in-the-loop.md)
Pause the agent for human review with approve, reject, and edit workflows.

### Manage conversations

#### [Branching chat](branching-chat.md)
Edit messages, regenerate responses, and navigate conversation branches.

#### [Message queues](message-queues.md)
Queue multiple messages while the agent processes them sequentially.

### Advanced streaming

#### [Join & rejoin streams](join-rejoin.md)
Disconnect from and reconnect to running agent streams without losing progress.

#### [Time travel](time-travel.md)
Inspect, navigate, and resume from any checkpoint in the conversation history.

## Choosing a frontend pattern

Start from the UX question your application needs to answer:

| If users need to...                        | Start with                                                                                                                                                                                                                   |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Understand what the agent is doing         | [Tool calling](tool-calling.md) and [reasoning tokens](reasoning-tokens.md)                                                                                          |
| Safely approve sensitive actions           | [Human-in-the-loop](human-in-the-loop.md)                                                                                                                                                        |
| Send work while a run is active            | [Message queues](message-queues.md)                                                                                                                                                              |
| Leave and come back to long-running work   | [Join & rejoin streams](join-rejoin.md)                                                                                                                                                          |
| Edit or retry from an earlier turn         | [Branching chat](branching-chat.md) and [time travel](time-travel.md)                                                                                                |
| Render state as an application, not a chat | [Structured output](structured-output.md), [generative UI](generative-ui-overview.md), and [Deep Agents frontend patterns](../../deepagents/frontend/overview.md) |

## Integrations

The stream API is UI-agnostic. Use it with any component library or generative UI
framework. Component libraries can own the presentation layer while LangChain's
SDK owns the agent runtime state, resumability, interrupts, and checkpoint
semantics underneath.

#### [AI Elements](integrations/ai-elements.md)
Composable shadcn/ui components for AI chat: `Conversation`, `Message`, `Tool`, `Reasoning`.

#### [assistant-ui](integrations/assistant-ui.md)
Headless React framework with built-in thread management, branching, and attachment support.

#### [OpenUI](integrations/openui.md)
Generative UI library for data-rich reports and dashboards using the openui-lang component DSL.

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/frontend/overview.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
