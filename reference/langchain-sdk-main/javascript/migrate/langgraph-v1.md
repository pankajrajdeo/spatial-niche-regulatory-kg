---
title: "LangGraph v1 migration guide"
description: "Prompt: Migrate a codebase to LangGraph v1. Migrate this codebase to LangGraph v1 (requires @langchain/langgraph and @langchain/core at v1, plus langchain at v1 when migrating from createReactAgent..."
source: "https://docs.langchain.com/oss/javascript/migrate/langgraph-v1"
category: "docs"
tags: [docs, javascript, migrate, langgraph-v1]
---

# LangGraph v1 migration guide

> **Prompt:** Migrate a codebase to LangGraph v1.
Migrate this codebase to LangGraph v1 (requires `@langchain/langgraph` and `@langchain/core` at v1, plus `langchain` at v1 when migrating from `createReactAgent`, and Node.js 22+).

Key changes:

1. **Upgrade packages**: install `@langchain/langgraph@latest` and `@langchain/core@latest`. If you use `createReactAgent`, also install `langchain@latest`.
2. **`createReactAgent` → `createAgent`**: replace `import { createReactAgent } from "@langchain/langgraph/prebuilts"` with `import { createAgent } from "langchain"`. Rename `prompt` to `systemPrompt`.
3. **Typed interrupts**: define interrupt types at graph construction via an `interrupts` config on `StateGraph`.
4. **`toLangGraphEventStream` removed**: use `graph.stream` with an `encoding` option (for example `"text/event-stream"`) instead of `toLangGraphEventStream` / `toLangGraphEventStreamResponse`.
5. **`useStream`**: supports custom transports.
6. **Build outputs**: do not import from package `dist/` paths; use the public module exports.

Search the codebase for `createReactAgent`, `toLangGraphEventStream`, `toLangGraphEventStreamResponse`, and `@langchain/langgraph/prebuilts`, and apply the necessary changes. Flag anything that cannot be migrated automatically.

This guide outlines changes in LangGraph v1 and how to migrate from previous versions. For a high-level overview of what's new, see the [release notes](../releases/langgraph-v1.md).

To upgrade,

**npm**

```bash
npm install @langchain/langgraph@latest @langchain/core@latest
```

**pnpm**

```bash
pnpm add @langchain/langgraph@latest @langchain/core@latest
```

**yarn**

```bash
yarn add @langchain/langgraph@latest @langchain/core@latest
```

**bun**

```bash
bun add @langchain/langgraph@latest @langchain/core@latest
```

## Summary of changes

| Area                             | What changed                                               |
| -------------------------------- | ---------------------------------------------------------- |
| React prebuilt                   | `createReactAgent` deprecated; use LangChain `createAgent` |
| Interrupts                       | Typed interrupts supported via `interrupts` config         |
| `toLangGraphEventStream` removed | Use `graph.stream` with the desired `encoding` format      |
| `useStream`                      | Supports custom transports                                 |

***

## Deprecation: `createReactAgent` → `createAgent`

LangGraph v1 deprecates the `createReactAgent` prebuilt. Use LangChain's `createAgent`, which runs on LangGraph and adds a flexible middleware system.

See the LangChain v1 docs for details:

* [Release notes](../releases/langchain-v1.md#createagent)
* [Migration guide](langchain-v1.md#createagent)

**v1 (new)**

```typescript
import { createAgent } from "langchain";

const agent = createAgent({
  model,
  tools,
  systemPrompt: "You are a helpful assistant.", // [!code highlight]
});
```

**v0 (old)**

```typescript
import { createReactAgent } from "@langchain/langgraph/prebuilts";

const agent = createReactAgent({
  model,
  tools,
  prompt: "You are a helpful assistant.", // [!code highlight]
});
```

***

## Typed interrupts

You can now define interrupt types at graph construction to strictly type the values passed to and received from interrupts.

**v1 (new)**

```typescript
import { StateGraph, interrupt } from "@langchain/langgraph";
import * as z from "zod";

const State = z.object({ foo: z.string() });

const graphConfig = {
  interrupts: {
    approve: interrupt<{ reason: string }, { messages: string[] }>(),
  },
}

const graph = new StateGraph(State, graphConfig)
  .addNode("node", async (state, runtime) => {
    const value = runtime.interrupt.approve({ reason: "review" }); // [!code highlight]
    return { foo: value };
  })
  .compile();
```

**v0 (old)**

```typescript
import { StateGraph } from "@langchain/langgraph";

const graph = new StateGraph(State)
  .addNode("node", async (state, runtime) => {
    const value = runtime.interrupt.approve({ reason: "review" }); // [!code highlight]
    return state;
  })
  .compile();
```

See [Interrupts](../langgraph/interrupts.md) to learn more.

***

## Event stream encoding

The low-level `toLangGraphEventStream` helper is removed. Streaming responses are handled by the SDK; when using low-level clients, select the wire format via an `encoding` option passed to `graph.stream`.

**v1 (new)**

```typescript
const stream = await graph.stream(input, {
  encoding: "text/event-stream",
  streamMode: ["values", "messages"],
});

return new Response(stream, {
  headers: { "Content-Type": "text/event-stream" }, // [!code highlight]
});
```

**v0 (old)**

```typescript
return toLangGraphEventStreamResponse({
  stream: graph.streamEvents(input, {
    version: "v2",
    streamMode: ["values", "messages"],
  }),
});
```

***

## Breaking changes

### Dropped Node 18 support

All LangGraph packages now require **Node.js 22 or higher**. Node.js 18 reached [end of life](https://nodejs.org/en/about/releases/) in March 2025.

### New build outputs

Builds for all langgraph packages now use a bundler based approach instead of using raw typescript outputs. If you were importing files from the `dist/` directory (which is not recommended), you will need to update your imports to use the new module system.

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/migrate/langgraph-v1.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
