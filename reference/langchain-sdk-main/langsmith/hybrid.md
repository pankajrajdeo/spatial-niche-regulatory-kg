---
title: "Hybrid"
description: "A LangSmith Deployment setup where you self-host Agent Servers in your infrastructure and send traces to LangSmith Cloud or a self-hosted LangSmith instance."
source: "https://docs.langchain.com/langsmith/hybrid"
category: "docs"
tags: [docs, langsmith, hybrid]
---

# Hybrid

> A LangSmith Deployment setup where you self-host Agent Servers in your infrastructure and send traces to LangSmith Cloud or a self-hosted LangSmith instance.

Hybrid is a platform setup for [LangSmith Deployment](deployment.md), which **deploys and runs agents in production**.

In a hybrid platform setup, you self-host [Agent Servers](agent-server.md) in your own infrastructure and send their traces to LangSmith, where LangSmith can be either a [self-hosted](self-hosted.md) instance or [LangSmith Cloud](cloud.md).

This setup gives you control over where your agent workloads run while letting you choose the [LangSmith platform option](platform-setup.md) that best fits your observability and compliance requirements.

## Components

| Component                                                                                                                              | Where it runs                                         | Who manages it                        |
| -------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- | ------------------------------------- |
| Agent Servers <br />for [LangSmith Deployment](deployment.md) | Your infrastructure                                   | You                                   |
| LangSmith <br />(tracing, evaluation, prompts)                                                                                         | Self-hosted in your infrastructure, or LangSmith SaaS | You (self-hosted) or LangSmith (SaaS) |

> [!NOTE]
> Hybrid is a platform setup for LangSmith Deployment (agent serving). To set up LangSmith for observability, evaluation, and prompt engineering only, see [Set up LangSmith](platform-setup.md).

## Workflow

1. Build and test your agent locally.
2. Deploy your agent to an [Agent Server running in your infrastructure](#self-host-your-agent-servers).
3. Send the agent's traces to [LangSmith (self-hosted or SaaS) for observability and evaluation](#choose-where-traces-are-sent).

### Self-host your Agent Servers

Deploy standalone Agent Servers using Docker, Docker Compose, or Kubernetes. See the [standalone server guide](deploy-standalone-server.md) for prerequisites, environment variables, and platform-specific instructions.

### Choose where traces are sent

Agent Servers send traces to LangSmith based on the `LANGSMITH_ENDPOINT` environment variable:

* **LangSmith SaaS**: Omit `LANGSMITH_ENDPOINT` to use the default (GCP US), or set it to the endpoint for your region:

  <table>
    <thead>
      <tr>
        <th>Region</th>

        <th>
          {protocol_0 === false ? "Host" : "URL"}
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td>GCP US</td>

        <td>
          <code>
            {`${protocol_0 === false ? "" : "https://"}${prefix_0 || "api.smith"}.langchain.com${suffix_0 || ""}`}
          </code>
        </td>
      </tr>

      <tr>
        <td>GCP EU</td>

        <td>
          <code>
            {`${protocol_0 === false ? "" : "https://"}eu.${prefix_0 || "api.smith"}.langchain.com${suffix_0 || ""}`}
          </code>
        </td>
      </tr>

      <tr>
        <td>GCP APAC</td>

        <td>
          <code>
            {`${protocol_0 === false ? "" : "https://"}apac.${prefix_0 || "api.smith"}.langchain.com${suffix_0 || ""}`}
          </code>
        </td>
      </tr>

      <tr>
        <td>AWS US</td>

        <td>
          <code>
            {`${protocol_0 === false ? "" : "https://"}aws.${prefix_0 || "api.smith"}.langchain.com${suffix_0 || ""}`}
          </code>
        </td>
      </tr>
    </tbody>
  </table>

* **Self-hosted LangSmith**: Set `LANGSMITH_ENDPOINT` to the hostname of your [self-hosted LangSmith](self-hosted.md) instance.

In both cases, authenticate with a [LangSmith API key](create-account-api-key.md) issued by the LangSmith instance you are tracing to.

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/hybrid.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
