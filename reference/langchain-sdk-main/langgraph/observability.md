---
title: "LangSmith Observability"
description: "Traces are a series of steps that your application takes to go from input to output. Each of these individual steps is represented by a run. You can use LangSmith to visualize these execution steps..."
source: "https://docs.langchain.com/oss/python/langgraph/observability"
category: "docs"
tags: [docs, langgraph, observability]
---

# LangSmith Observability

Traces are a series of steps that your application takes to go from input to output. Each of these individual steps is represented by a run. You can use [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-langgraph-observability) to visualize these execution steps. To use it, [enable tracing for your application](../langsmith/trace-with-langgraph.md). This enables you to do the following:

* [Debug a locally running application](../langsmith/observability-studio.md#debug-langsmith-traces).
* [Evaluate the application performance](../langchain/test/evals.md).
* [Monitor the application](../langsmith/dashboards.md).

## Prerequisites

Before you begin, ensure you have the following:

* **A LangSmith account**: Sign up (for free) or log in at [smith.langchain.com](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-langgraph-observability).
* **A LangSmith API key**: Follow the [Create an API key](../langsmith/create-account-api-key.md) guide.

## Enable tracing

To enable tracing for your application, set the following environment variables:

```python
export LANGSMITH_TRACING=true
export LANGSMITH_API_KEY=<your-api-key>
```

By default, the trace will be logged to the project with the name `default`. To configure a custom project name, see [Log to a project](#log-to-a-project).

For more information, see [Trace with LangGraph](../langsmith/trace-with-langgraph.md).

## Trace selectively

You may opt to trace specific invocations or parts of your application using LangSmith's `tracing_context` context manager:

```python
import langsmith as ls

# This WILL be traced
with ls.tracing_context(enabled=True):
    agent.invoke({"messages": [{"role": "user", "content": "Send a test email to alice@example.com"}]})

# This will NOT be traced (if LANGSMITH_TRACING is not set)
agent.invoke({"messages": [{"role": "user", "content": "Send another email"}]})
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

```python
import langsmith as ls

with ls.tracing_context(project_name="email-agent-test", enabled=True):
    response = agent.invoke({
        "messages": [{"role": "user", "content": "Send a welcome email"}]
    })
```

</details>

## Add metadata to traces

You can annotate your traces with custom metadata and tags:

```python
response = agent.invoke(
    {"messages": [{"role": "user", "content": "Send a welcome email"}]},
    config={
        "tags": ["production", "email-assistant", "v1.0"],
        "metadata": {
            "user_id": "user_123",
            "session_id": "session_456",
            "environment": "production"
        }
    }
)
```

`tracing_context` also accepts tags and metadata for fine-grained control:

```python
with ls.tracing_context(
    project_name="email-agent-test",
    enabled=True,
    tags=["production", "email-assistant", "v1.0"],
    metadata={"user_id": "user_123", "session_id": "session_456", "environment": "production"}):
    response = agent.invoke(
        {"messages": [{"role": "user", "content": "Send a welcome email"}]}
    )
```

This custom metadata and tags will be attached to the trace in LangSmith.

> [!TIP]
> To learn more about how to use traces to debug, evaluate, and monitor your agents, see the [LangSmith documentation](../langsmith/observability.md).

## Use anonymizers to prevent logging of sensitive data in traces

You may want to mask sensitive data to prevent it from being logged to LangSmith. You can create [anonymizers](../langsmith/mask-inputs-outputs.md#rule-based-masking-of-inputs-and-outputs) and apply them to
your graph using configuration. This example will redact anything matching the Social Security Number format XXX-XX-XXXX from traces sent to LangSmith.

**Python**

```python
from langchain_core.tracers.langchain import LangChainTracer
from langgraph.graph import StateGraph, MessagesState
from langsmith import Client
from langsmith.anonymizer import create_anonymizer

anonymizer = create_anonymizer([
    # Matches SSNs
    { "pattern": r"\b\d{3}-?\d{2}-?\d{4}\b", "replace": "<ssn>" }
])

tracer_client = Client(anonymizer=anonymizer)
tracer = LangChainTracer(client=tracer_client)
# Define the graph
graph = (
    StateGraph(MessagesState)
    ...
    .compile()
    .with_config({'callbacks': [tracer]})
)
```

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/observability.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
