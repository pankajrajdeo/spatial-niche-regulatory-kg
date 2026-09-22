---
title: "Overview"
description: "Control and customize agent execution at every step"
source: "https://docs.langchain.com/oss/javascript/langchain"
category: "docs"
tags: [docs, javascript, langchain]
---

# Overview

> Control and customize agent execution at every step

Middleware provides a way to more tightly control what happens inside the agent. Middleware is useful for the following:

* Tracking agent behavior with logging, analytics, and debugging.
* Transforming prompts, [tool selection](langchain/middleware/built-in.md#llm-tool-selector), and output formatting.
* Adding [retries](langchain/middleware/built-in.md#tool-retry), [fallbacks](langchain/middleware/built-in.md#model-fallback), and early termination logic.
* Applying [rate limits](langchain/middleware/built-in.md#model-call-limit), guardrails, and [PII detection](langchain/middleware/built-in.md#pii-detection).

Add middleware by passing them to `createAgent`:

```typescript
import {
  createAgent,
  summarizationMiddleware,
  humanInTheLoopMiddleware,
} from "langchain";

const agent = createAgent({
  model: "gpt-5.5",
  tools: [...],
  middleware: [summarizationMiddleware, humanInTheLoopMiddleware],
});
```

## The agent loop

The core agent loop involves calling a model, letting it choose tools to execute, and then finishing when it calls no more tools:

<img src="https://mintcdn.com/langchain-5e9cc07a/Tazq8zGc0yYUYrDl/oss/images/core_agent_loop.png?fit=max&auto=format&n=Tazq8zGc0yYUYrDl&q=85&s=ac72e48317a9ced68fd1be64e89ec063" alt="Core agent loop diagram" width="300" height="268" data-path="oss/images/core_agent_loop.png" />

Middleware exposes hooks before and after each of those steps:

<img src="https://mintcdn.com/langchain-5e9cc07a/RAP6mjwE5G00xYsA/oss/images/middleware_final.png?fit=max&auto=format&n=RAP6mjwE5G00xYsA&q=85&s=eb4404b137edec6f6f0c8ccb8323eaf1" alt="Middleware flow diagram" width="500" height="560" data-path="oss/images/middleware_final.png" />

## Use middleware inside a LangGraph workflow

Middleware is not a separate runtime: hooks run inside the compiled [LangGraph](langgraph/overview.md) that [`create_agent`](https://reference.langchain.com/javascript/langchain/index/createAgent) returns. You can drop the whole agent (middleware and all) into a larger [StateGraph](https://reference.langchain.com/javascript/langchain-langgraph/index/StateGraph) as a node or subgraph, and every middleware hook continues to run.

Reach for this pattern when the surrounding topology is more than a standard "loop until done": classifying input before routing to one of several agents, fanning out work in parallel, or stitching agent calls together with deterministic steps.

`HumanInTheLoopMiddleware` matches against each tool's `.name`.

The key matches the `name` you pass to `tool({...}, { name })`.

```typescript
import { AgentState, createAgent, humanInTheLoopMiddleware } from "langchain";
import { StateGraph, START } from "@langchain/langgraph";

// Assumes readEmail, sendEmail, classifyNode, and route are defined elsewhere.
// readEmail / sendEmail are registered with name: "read_email" / "send_email".
const emailAgent = createAgent({
  model: "claude-sonnet-4-6",
  tools: [readEmail, sendEmail],
  middleware: [humanInTheLoopMiddleware({ interruptOn: { send_email: true } })],
});

const graph = new StateGraph(AgentState)
  .addNode("classify", classifyNode)
  .addNode("emailAgent", emailAgent)
  .addEdge(START, "classify")
  .addConditionalEdges("classify", route)
  .compile();
```

The HITL interrupt, summarization, PII redaction, retries, and any custom hooks all travel with the agent node. See [Use subgraphs](langgraph/use-subgraphs.md) for the full set of composition patterns, including subgraph checkpointer scoping (per-invocation versus per-thread).

## Additional resources

#### [Built-in middleware](langchain/middleware/built-in.md)
Explore built-in middleware for common use cases.

#### [Custom middleware](langchain/middleware/custom.md)
Build your own middleware with hooks and decorators.

#### [Middleware API reference](https://reference.langchain.com/python/langchain/middleware/)
Complete API reference for middleware.

#### [Middleware integrations](integrations/middleware.md)
Provider-specific middleware for Anthropic, AWS, OpenAI, and more.

#### [Testing agents](langchain/test.md)
Test your agents with LangSmith.

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/middleware/overview.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
