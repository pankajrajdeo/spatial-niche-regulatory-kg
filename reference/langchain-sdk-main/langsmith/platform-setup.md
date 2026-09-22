---
title: "Set up LangSmith"
description: "Host and manage LangSmith infrastructure for observability, evaluation, and prompt engineering."
source: "https://docs.langchain.com/langsmith/platform-setup"
category: "docs"
tags: [docs, langsmith, platform-setup]
---

# Set up LangSmith

> Host and manage LangSmith infrastructure for observability, evaluation, and prompt engineering.

# Overview

Set up **LangSmith** for [observability](observability.md), [evaluation](evaluation.md), and [prompt engineering](prompt-context-hub.md#prompts). LangSmith offers Cloud, Bring Your Own Cloud (BYOC), and Self-hosted options. Choose the option that matches where your data has to live and who runs the infrastructure.

> [!NOTE]
> If you also want to deploy agents in production, you can use [**LangSmith Deployment**](deployment.md) with Cloud, BYOC, or Self-hosted.

#### [Cloud](cloud.md)
Fully managed observability, evaluation, and prompt engineering.

#### [BYOC](byoc.md)
Full control over your data, while LangChain manages the infrastructure.

#### [Self-hosted](self-hosted.md)
Full control with observability, evaluation, and prompt engineering in your infrastructure.

> [!NOTE]
> Self-hosted and BYOC are available on the [Enterprise plan](pricing-plans.md). [Get a demo](https://www.langchain.com/contact-sales) to learn more.

## Compare Cloud, BYOC, and Self-hosted

| Feature                         | **Cloud**         | **BYOC**                                                   | **Self-hosted** |
| ------------------------------- | ----------------- | ---------------------------------------------------------- | --------------- |
| **Who runs the infrastructure** | LangChain         | LangChain runs the control plane, you run your data planes | You             |
| **Where sensitive data lives**  | LangChain's cloud | Your VPC                                                   | Your VPC        |
| **Upgrades and patches**        | Automatic         | Automatic                                                  | Manual          |
| **Scaling**                     | Automatic         | Automatic, managed by LangChain                            | Manual          |

Cloud, BYOC, and Self-hosted support [LangSmith Deployment](deployment.md) for agent workloads. Refer to the [LangSmith Deployment overview](deployment.md) to pick a topology (Cloud managed, BYOC, Hybrid, self-hosted with control plane, or standalone).

## Common setups

* **Fastest to start, managed everything.** [LangSmith Cloud](cloud.md) paired with [LangSmith Deployment](deployment.md) on Cloud. LangChain hosts the platform, and, when you use LangSmith Deployment, also hosts your [Agent Servers](agent-server.md).
* **Bring Your Own Cloud.** Data stays in your VPC, and LangChain manages the infrastructure. Refer to the [BYOC overview](byoc.md).
* **Observability data must stay in your infrastructure.** Self-hosted LangSmith, paired with any LangSmith Deployment topology, including [self-hosted LangSmith Deployment](deploy-with-control-plane.md) for agent workloads.
* **Managed observability, agents in your VPC.** LangSmith Cloud paired with [Hybrid](hybrid.md) LangSmith Deployment. Traces and evaluations stay on SaaS while agent workloads stay in your infrastructure.
* **Observability only, no agent hosting.** LangSmith Cloud or self-hosted, without LangSmith Deployment. Run your agents wherever you already run apps and send traces to LangSmith.

## Related

#### [Account setup](admin.md)
Create an account, manage API keys, and choose a pricing tier.

#### [Plans and pricing](https://www.langchain.com/pricing)
Compare LangSmith plans and tiers.

#### [Observability](observability.md)
Trace and monitor your LLM applications.

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/platform-setup.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
