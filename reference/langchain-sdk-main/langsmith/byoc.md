---
title: "Bring Your Own Cloud (BYOC)"
description: "Deploy LangSmith services and store data in your own cloud environment while LangChain operates, scales, and upgrades the infrastructure."
source: "https://docs.langchain.com/langsmith/byoc"
category: "docs"
tags: [docs, langsmith, byoc]
---

# Bring Your Own Cloud (BYOC)

> Deploy LangSmith services and store data in your own cloud environment while LangChain operates, scales, and upgrades the infrastructure.

> [!NOTE]
> BYOC is only available for customers on the [Enterprise plan](https://www.langchain.com/pricing).

Bring Your Own Cloud (BYOC) lets you deploy LangSmith services and store data in your own cloud environment, while LangChain operates, scales, and upgrades the infrastructure. BYOC suits organizations that require complete sovereignty over their data, but do not want the overhead of provisioning and managing infrastructure.

BYOC uses a split responsibility model: the control plane runs in LangChain's cloud, and the data plane runs entirely in your cloud environment. For details on what LangChain manages versus what you manage, see the [BYOC shared responsibility model](byoc-shared-responsibility.md).

## Get started

To deploy LangSmith BYOC, [contact our sales team](https://www.langchain.com/contact-sales). After the LangChain team enables BYOC for your organization, follow the [onboarding guide](byoc-onboarding.md) to create your first data plane.

## Regions and cloud providers

BYOC is generally available (GA) on AWS. Support for additional cloud providers is planned for the second half of 2026.

You can deploy LangSmith BYOC in any of the following AWS regions:

| Area       | AWS regions                                                                                            |
| ---------- | ------------------------------------------------------------------------------------------------------ |
| **US**     | `us-east-1`, `us-east-2`, `us-west-1`, `us-west-2`                                                     |
| **Canada** | `ca-central-1`                                                                                         |
| **EU**     | `eu-central-1`, `eu-west-1`, `eu-west-2`, `eu-west-3`, `eu-north-1`                                    |
| **APAC**   | `ap-south-1`, `ap-northeast-1`, `ap-northeast-2`, `ap-northeast-3`, `ap-southeast-1`, `ap-southeast-2` |

The control plane runs in `us-east-2` regardless of where you place your data planes. If you provision a data plane outside the US, your sensitive application data stays in that region while control plane metadata remains in the US:

| Control plane (US)                                                             | Data plane (your region)                                                                                                     |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| Users, roles, billing, organization configuration, SSO configuration, API keys | Traces, experiments, datasets, insights runs, annotation queues, workspace secrets, and all other sensitive application data |

## Available features

The following features are supported:

* **[Observability](observability.md)**: Tracing, projects, dashboards, and alerts.
* **[Evaluation](evaluation.md)**: Datasets, experiments, evaluators, and annotation queues.
* **[Insights](insights.md)**: Automatic analysis of traces to surface usage patterns, common agent behaviors, and failure modes.
* **[LangSmith Chat](chat.md)**: Analyze traces, threads, prompts, and evaluations from inside your workspace.
* **[Prompt engineering](prompt-context-hub.md#prompts)**: Prompts and prompt commits.
* **[LangSmith Deployment](deployment.md)**: The LangSmith Deployment control plane runs inside your data plane's cluster, so both the agent management layer and your agents run in your VPC.
* **[Sandboxes](sandboxes.md)**: Usage through the CLI and SDK is identical to Cloud, except that you point at your data plane's endpoint.
* **[LLM Gateway](llm-gateway.md)**: Call models across providers with one LangSmith API key, with spend, rate limit, and data-protection policies enforced centrally.
* **[LangSmith MCP](langsmith-remote-mcp.md)**: Connect MCP-compatible clients to LangSmith to query data.
* **[Fleet](fleet/index.md)**: Build and run no-code agents from templates, connectors, and channels.
* **[SmithDB](smithdb-sdk-migration.md)**: The purpose-built observability backend for trace data, persisting to S3 in your account.
* **[Engine](engine-overview.md)**: Automatic detection, diagnosis, and resolution of recurring issues found in production traces. Engine uses the LangSmith Intelligence service for model work. See the [self-hosted Engine architecture](engine-self-hosted.md#how-it-works) for details.

The following features are planned but not yet supported:

* **[Managed Deep Agents](python/managed-deep-agents-overview.md)**: LangChain-hosted deep agents with connectors, channels, and schedules.
* **[LLM auth proxy](llm-auth-proxy-self-hosted.md)**: Enforce your own authentication flows for model invocations so provider credentials are never exposed to end users.

## Prerequisites

Before LangChain can provision a data plane, you need the following:

* **A LangSmith organization on AWS**: Create one at [aws.smith.langchain.com](https://aws.smith.langchain.com), then send your organization ID to the LangChain team to enable BYOC.
* **An AWS account**: LangChain recommends a fresh account dedicated to LangSmith BYOC, but it is not required.
* **A supported region**: Pick one of the AWS regions listed above.
* **An IAM role and external ID**: LangChain provides the external ID. Copy it using the button next to the **Data Planes** header in **Settings > Data Planes**, then apply the [`langsmith-byoc-role` Terraform module](https://github.com/langchain-ai/terraform/tree/main/modules/byoc/aws/langsmith-byoc-role) with this value to create the role LangChain assumes to provision and manage your data plane. You must use this module.

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/byoc.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
