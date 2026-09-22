---
title: "LangSmith Observability"
description: "Traces are a series of steps that your application takes to go from input to output. Each of these individual steps is represented by a run. You can use LangSmith to visualize these execution steps..."
source: "https://docs.langchain.com/oss/javascript/langgraph/observability"
category: "docs"
tags: [docs, javascript, langgraph, observability]
---

# LangSmith Observability

Traces are a series of steps that your application takes to go from input to output. Each of these individual steps is represented by a run. You can use [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-langgraph-observability) to visualize these execution steps. To use it, [enable tracing for your application](../../langsmith/trace-with-langgraph.md). This enables you to do the following:

* [Debug a locally running application](../../langsmith/observability-studio.md#debug-langsmith-traces).
* [Evaluate the application performance](../langchain/test/evals.md).
* [Monitor the application](../../langsmith/dashboards.md).

## Prerequisites

Before you begin, ensure you have the following:

* **A LangSmith account**: Sign up (for free) or log in at [smith.langchain.com](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-langgraph-observability).
* **A LangSmith API key**: Follow the [Create an API key](../../langsmith/create-account-api-key.md) guide.

## Enable tracing

To enable tracing for your application, set the following environment variables:

```python
export LANGSMITH_TRACING=true
export LANGSMITH_API_KEY=<your-api-key>
```

By default, the trace will be logged to the project with the name `default`. To configure a custom project name, see [Log to a project](#log-to-a-project).

For more information, see [Trace with LangGraph](../../langsmith/trace-with-langgraph.md).

## Trace selectively

You may opt to trace specific invocations or parts of your application using LangSmith's `tracing_context` context manager:

```ts
import { LangChainTracer } from "@langchain/core/tracers/tracer_langchain";

// This WILL be traced
const tracer = new LangChainTracer();
await agent.invoke(
  {
    messages: [{role: "user", content: "Send a test email to alice@example.com"}]
  },
  { callbacks: [tracer] }
);

// This will NOT be traced (if LANGSMITH_TRACING is not set)
await agent.invoke(
  {
    messages: [{role: "user", content: "Send another email"}]
  }
);
```

## Log to a project

<details>
<summary>Statically</summary>

You can set a custom project name for your entire application by setting the `LANGSMITH_PROJECT` environment variable:

```bash
export LANGSMITH_PROJECT=my-agent-project
```

</details>

<details>
<summary>Dynamically</summary>

You can set the project name programmatically for specific operations:

```ts
import { LangChainTracer } from "@langchain/core/tracers/tracer_langchain";

const tracer = new LangChainTracer({ projectName: "email-agent-test" });
await agent.invoke(
  {
    messages: [{role: "user", content: "Send a test email to alice@example.com"}]
  },
  { callbacks: [tracer] }
);
```

</details>

## Add metadata to traces

You can annotate your traces with custom metadata and tags:

```ts
import { LangChainTracer } from "@langchain/core/tracers/tracer_langchain";

const tracer = new LangChainTracer({ projectName: "email-agent-test" });
await agent.invoke(
  {
    messages: [{role: "user", content: "Send a test email to alice@example.com"}]
  },
  config: {
    tags: ["production", "email-assistant", "v1.0"],
    metadata: {
      userId: "user123",
      sessionId: "session456",
      environment: "production"
    }
  },
);

```

This custom metadata and tags will be attached to the trace in LangSmith.

> [!TIP]
> To learn more about how to use traces to debug, evaluate, and monitor your agents, see the [LangSmith documentation](../../langsmith/observability.md).

## Use anonymizers to prevent logging of sensitive data in traces

You may want to mask sensitive data to prevent it from being logged to LangSmith. You can create [anonymizers](../../langsmith/mask-inputs-outputs.md#rule-based-masking-of-inputs-and-outputs) and apply them to
your graph using configuration. This example will redact anything matching the Social Security Number format XXX-XX-XXXX from traces sent to LangSmith.

**TypeScript**

```typescript
import { StateGraph } from "@langchain/langgraph";
import { LangChainTracer } from "@langchain/core/tracers/tracer_langchain";
import { StateAnnotation } from "./state.js";
import { createAnonymizer } from "langsmith/anonymizer"
import { Client } from "langsmith"

const anonymizer = createAnonymizer([
  // Matches SSNs
  { pattern: /\b\d{3}-?\d{2}-?\d{4}\b/, replace: "<ssn>" }
])

const langsmithClient = new Client({ anonymizer })
const tracer = new LangChainTracer({
  client: langsmithClient,
});

export const graph = new StateGraph(StateAnnotation)
  .compile()
  .withConfig({ callbacks: [tracer] });
```

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/observability.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
