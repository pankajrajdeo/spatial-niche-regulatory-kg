---
title: "Agent Server"
description: "Configure and operate the LangSmith Agent Server runtime, including capabilities, application structure, auth, and customization."
source: "https://docs.langchain.com/langsmith/develop-agents-overview"
category: "docs"
tags: [docs, langsmith, develop-agents-overview]
---

# Agent Server

> Configure and operate the LangSmith Agent Server runtime, including capabilities, application structure, auth, and customization.

Configure and build applications on the [Agent Server](agent-server.md) runtime. Once deployed, agents work with three primitives: [**assistants**](assistants.md) for configuration, [**threads**](use-threads.md) for state, and [**runs**](runs.md) for workloads. The pages in this tab cover the capabilities Agent Server provides, how to [structure your application](application-structure.md), and how to [secure](auth.md) and [customize](custom-routes.md) the server.

## Capabilities

#### [Develop your application](application-structure.md)
Structure your app, configure dependencies for Python, JavaScript, and monorepos, and connect agents with RemoteGraph, semantic search, TTLs, and CI/CD.

#### [Agent Server runtime](agent-server.md)
Work with assistants, threads, runs, and cron jobs. Stream to users, pause for human review, handle concurrent input, and connect via MCP and A2A.

#### [Auth & access control](auth.md)
Authenticate users, enforce resource-level access, and connect external OAuth2 identity providers.

#### [Server customization](caching.md)
Add caching, custom stores and checkpointers, lifespan hooks, middleware, custom routes, encryption, and configurable headers and logs.

#### [REST API](server-api-ref.md)
Full REST API reference for assistants, threads, runs, crons, store, A2A, MCP, and system endpoints.

## Tutorials

* [Collect user feedback for Agent Server runs](agent-server-feedback.md): Attach end-user feedback to runs and traces
* [Deploy other frameworks (e.g., Strands, CrewAI)](deploy-other-frameworks.md): Wrap existing agents with Functional API and deploy
* [Implement generative user interfaces with LangGraph](generative-ui-react.md): Stream UI elements to a React client
* [Implement a CI/CD pipeline](cicd-pipeline-example.md): Automate tests, evaluations, and deployments with GitHub Actions

## Securing and customizing your server

* [Custom auth](auth.md): Authentication and multi-tenant access control
* [Server customization](custom-routes.md): Custom routes, [middleware](custom-middleware.md), [lifespan hooks](custom-lifespan.md), [encryption](encryption.md)

## Operations

* [CI/CD pipelines](cicd-pipeline-example.md)
* [TTL configuration](configure-ttl.md) for state and thread management
* [Semantic search](semantic-search.md)

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/agent-server-overview.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
