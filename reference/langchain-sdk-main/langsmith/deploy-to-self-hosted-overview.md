---
title: "Deploy to self-hosted"
description: "Run the LangSmith Deployment platform on your own infrastructure with full control over data, networking, and resources."
source: "https://docs.langchain.com/langsmith/deploy-to-self-hosted-overview"
category: "docs"
tags: [docs, langsmith, deploy-to-self-hosted-overview]
---

# Deploy to self-hosted

> Run the LangSmith Deployment platform on your own infrastructure with full control over data, networking, and resources.

Self-hosted LangSmith Deployment runs the [Agent Server](agent-server.md), control plane, data plane, and supporting databases inside infrastructure that you operate.

LangChain ships the container images, Helm charts, and license; you provide the Kubernetes cluster (or Docker host), PostgreSQL, Redis, and the networking and observability tooling that fit your environment. Self-hosted is the best deployment option when you have data residency, regulatory constraints, custom networking, or air-gapped requirements.

> [!NOTE]
> Self-hosted deployments require an [Enterprise plan](https://www.langchain.com/pricing) and the LangSmith license key delivered with that plan. For a setup guide, see [Self-hosted LangSmith](self-hosted.md).

## Topologies

LangSmith supports three self-hosted topologies that trade off setup complexity against control-plane features. Reference pages for [platform features](self-hosted-platform-features.md), [Agent Server metrics](self-hosted-agent-server-metrics.md), and [diagnostics](diagnostics-self-hosted.md) apply to all three.

#### [Full self-hosted platform](deploy-with-control-plane.md)
The complete LangSmith platform—[control plane](control-plane.md) UI and APIs, [data plane](data-plane.md) listener, observability, evaluation, and agent deployment management. Best for teams that want the LangSmith product experience inside their own network.

#### [Hybrid](hybrid.md)
LangChain-hosted control plane with the data plane (Agent Servers and databases) in your infrastructure. Best when you want managed deployment workflows but need agent workloads and customer data to stay inside your VPC.

#### [Standalone server](deploy-standalone-server.md)
The lightest option—Agent Server containers (API + queue workers) with your own PostgreSQL and Redis. No control plane, no managed UI. Best for embedding the runtime into existing infrastructure or running air-gapped.

#### [Platform features](self-hosted-platform-features.md)
Reference for self-hosted-only platform behavior: custom Postgres and Redis, listeners, and resource customization.

#### [Agent Server metrics](self-hosted-agent-server-metrics.md)
Prometheus and Datadog export for Agent Server, including Deployment UI metrics and internal metrics.

#### [Diagnostics](diagnostics-self-hosted.md)
Collect logs, inspect state, and troubleshoot a self-hosted installation.

## Who manages what

Self-hosted shifts ownership of infrastructure operations from LangChain to your team, which provides flexibility and control over how you configure and operate is layer:

|                                           | **Who manages it** | **Where it runs**   |
| ----------------------------------------- | ------------------ | ------------------- |
| LangSmith platform (UI, APIs, datastores) | You                | Your infrastructure |
| Agent Server runtime                      | You                | Your infrastructure |
| PostgreSQL and Redis                      | You                | Your infrastructure |
| CI/CD for your apps                       | You                | Your CI environment |
| Upgrades, scaling, and backups            | You                | Your infrastructure |

In return, you can integrate with your own [Postgres](self-hosted-platform-features.md#custom-postgresql) and [Redis](self-hosted-platform-features.md#custom-redis), size [CPU and memory](self-hosted-platform-features.md#resource-customization) for your workload, and operate inside your existing network and observability stack. For the corresponding Cloud-managed model, see [Deploy to Cloud](deploy-to-cloud-overview.md).

## Next steps

#### [Pick a topology](deploy-standalone-server.md)
Compare standalone server, full platform, and hybrid to find the right fit.

#### [Install the full platform](deploy-self-hosted-full-platform.md)
Deploy LangSmith on Kubernetes with the control plane and data plane.

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/deploy-to-self-hosted-overview.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
