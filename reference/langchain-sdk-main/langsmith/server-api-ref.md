---
title: "Agent Server API reference for LangSmith Deployment"
description: "The Agent Server API reference is available within each deployment at the /docs endpoint (e.g. http://localhost:8124/docs)."
source: "https://docs.langchain.com/langsmith/server-api-ref"
category: "docs"
tags: [docs, langsmith, server-api-ref]
---

# Agent Server API reference for LangSmith Deployment

The Agent Server API reference is available within each [deployment](deployment.md) at the `/docs` endpoint (e.g. `http://localhost:8124/docs`).

Browse the full API reference in the **Agent Server API** section in the sidebar, or see the endpoint groups below:

* [Assistants](agent-server-api/assistants.md) - Configured instances of a graph
* [Threads](agent-server-api/threads.md) - Accumulated outputs of a group of runs
* [Thread Runs](agent-server-api/thread-runs.md) - Invocations of a graph/assistant on a thread
* [Stateless Runs](agent-server-api/stateless-runs.md) - Invocations with no state persistence
* [Crons](agent-server-api/crons.md) - Periodic runs on a schedule
* [Store](agent-server-api/store.md) - Persistent key-value store for long-term memory
* [A2A](agent-server-api/a2a.md) - Agent-to-Agent Protocol endpoints
* [MCP](agent-server-api/mcp.md) - Model Context Protocol endpoints
* [System](agent-server-api/system.md) - Health checks and server info

<a id="tag/a2a/post/a2a/\{assistant_id}"></a>

## Authentication

For deployments to LangSmith, authentication is required. Pass the `X-Api-Key` header with each request to the Agent Server. The value of the header should be set to a valid LangSmith API key for the organization where the Agent Server is deployed.

Example `curl` command:

```shell
curl --request POST \
  --url http://localhost:8124/assistants/search \
  --header 'Content-Type: application/json' \
  --header 'X-Api-Key: LANGSMITH_API_KEY' \
  --data '{
  "metadata": {},
  "limit": 10,
  "offset": 0
}'
```

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/server-api-ref.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
