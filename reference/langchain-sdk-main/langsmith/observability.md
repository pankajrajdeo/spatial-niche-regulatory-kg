---
title: "LangSmith Observability"
description: "Instrument your LLM application, investigate traces, and monitor performance in production with LangSmith."
source: "https://docs.langchain.com/langsmith/observability"
category: "docs"
tags: [docs, langsmith, observability]
---

# LangSmith Observability

> Instrument your LLM application, investigate traces, and monitor performance in production with LangSmith.

LangSmith Observability provides full visibility into your LLM application: from individual traces to production-wide performance metrics. Traces are the record of what your agents did in production. Use them to debug failures, monitor quality, and build the datasets you evaluate against.

> [!NOTE]
> LangSmith works with many frameworks and providers. Browse [available integrations](integrations.md) to connect your stack including OpenAI, Anthropic, CrewAI, Vercel AI SDK, Pydantic AI, and more.

## Get started

### Create an account
Sign up at [smith.langchain.com](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=snippets-langsmith-account-api-key-quickstart) (no credit card required).
You can log in with **Google**, **GitHub**, or **email**.

### Create an API key
Go to your [Settings page](https://smith.langchain.com/settings) > **API Keys** > **Create API Key**.
Copy the key and save it securely.

Once your account and API key are ready, set up tracing:

#### [Set up tracing](observability-quickstart.md)
Add tracing to your app in minutes with environment variables, framework integrations, or the SDK.

#### [Trace a RAG application](observability-llm-tutorial.md)
Follow a step-by-step tutorial to instrument a retrieval-augmented generation app from start to finish.

## Investigate and monitor

#### [View traces](view-traces.md)
Inspect threads and runs in the Messages, Turns, and Details views.

#### [Monitor performance](dashboards.md)
Build dashboards and set alerts to track quality and catch issues early.

#### [Configure automations](rules.md)
Automate workflows with rules, webhooks, and online evaluations.

#### [Collect feedback](attach-user-feedback.md)
Annotate outputs and gather user feedback using queues or inline annotation.

#### [Find and fix failures with Engine](engine-overview.md)
Automatically detect recurring issues in your traces, diagnose their root cause, and resolve them with LangSmith Engine.

For terminology and core concepts, refer to [Observability concepts](observability-concepts.md). For trace pricing, retention, and limits, see [Usage and billing](usage-and-billing.md).

> [!NOTE]
> To set up a LangSmith instance, visit the [Platform setup section](platform-setup.md) to choose between cloud, hybrid, or self-hosted. All options include observability, evaluation, prompt engineering, and deployment.

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/observability.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
