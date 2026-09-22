---
title: "Deploy to Cloud"
description: "Deploy LangSmith agents to LangChain-managed Cloud infrastructure on AWS and GCP."
source: "https://docs.langchain.com/langsmith/deploy-to-cloud-overview"
category: "docs"
tags: [docs, langsmith, deploy-to-cloud-overview]
---

# Deploy to Cloud

> Deploy LangSmith agents to LangChain-managed Cloud infrastructure on AWS and GCP.

[LangSmith Cloud](cloud.md) is a **managed platform for deploying your agents**. LangChain hosts and operates the [control plane](control-plane.md), [data plane](data-plane.md), [Agent Server](agent-server.md) runtime, and supporting databases on AWS and GCP. Push code to a connected GitHub repository or invoke the `langgraph deploy` CLI, and the platform handles build, provisioning, scaling, and ongoing operations. Deployments come in two types: Serverless, a lightweight, fully managed option that scales to zero after a period of inactivity, and Dedicated, always-on infrastructure for production workloads. For details, see [Deployment types](cloud-platform-features.md#deployment-types).

> [!NOTE]
> Agent deployments running on Cloud require a [Plus plan or above](https://www.langchain.com/pricing). Before creating your first agent deployment, verify that your application runs locally with `langgraph dev`. Refer to [Local development and testing](local-dev-testing.md).

#### [Deploy on Cloud](deploy-to-cloud.md)
Step-by-step setup guide for creating, configuring, and managing Cloud deployments from the LangSmith UI or the `langgraph deploy` CLI.

#### [Cloud platform features](cloud-platform-features.md)
Reference for Cloud-only platform behavior: data regions, static IPs, payload limits, deployment types, and managed database provisioning.

#### [Quickstart](deployment-quickstart.md)
Deploy your first LangGraph application to Cloud in a few minutes.

To deploy a code-first Deep Agent without standing up your own Agent Server, [Managed Deep Agents](python/managed-deep-agents-overview.md) offers a CLI-first managed runtime in public beta.

## Next steps

#### [Run the quickstart](deployment-quickstart.md)
Deploy a starter LangGraph application end-to-end.

#### [Read the full deploy guide](deploy-to-cloud.md)
Configure environment variables, secrets, revisions, and deployment settings.

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/deploy-to-cloud-overview.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
