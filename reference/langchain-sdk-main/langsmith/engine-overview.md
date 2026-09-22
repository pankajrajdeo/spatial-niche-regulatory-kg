---
title: "LangSmith Engine"
description: "LangSmith Engine is the agent for agent engineering, turning production traces into tracked issues, fixes, and datasets across the development lifecycle."
source: "https://docs.langchain.com/langsmith/engine-overview"
category: "docs"
tags: [docs, langsmith, engine-overview]
---

# LangSmith Engine

> LangSmith Engine is the agent for agent engineering, turning production traces into tracked issues, fixes, and datasets across the development lifecycle.

LangSmith Engine is the LangSmith Agent for agent engineering. It works from your production traces to surface recurring issues, diagnose their root cause, and drive the fix across every stage of the development lifecycle.

Each issue moves through a closed loop: a recurring issue is detected in your traces, the root cause is diagnosed, a fix is proposed, the issue is tracked as new traces matching the same pattern arrive, and if the issue resurfaces after being closed, Engine reopens it automatically.

## Engine across the lifecycle

For each issue, Engine surfaces the contributing traces, proposes a fix, keeps the issue current by attaching new traces that match the same failure pattern, and creates ground truth dataset examples from the production trace inputs.

#### [Build: Open a pull request](engine.md#open-or-view-a-pull-request)
Apply the proposed fix by opening a pull request in your connected repository. Engine can propose code changes to agents built with Deep Agents, LangChain, and LangGraph.

#### [Test: Generate datasets](engine.md#add-offline-examples)
Create ground truth dataset examples from production traces for offline evaluation, so you can verify a fix before it ships.

#### [Monitor: Track recurring issues](engine.md#browse-and-filter-issues)
Scan your tracing projects on a schedule to surface, prioritize, and diagnose recurring issues, and add new matching traces to each issue as they appear.

## How Engine runs

Engine scans each connected tracing project on a dynamic schedule tuned to balance cost and performance, clustering and prioritizing issues by severity. It uses LangChain-managed inference and charges in LangChain Compute Units (LCUs). Each detected issue is tagged with an [issue category](engine-issue-categories.md) such as **Silent tool error** or **Hallucination**. For setup, costs, and the full issue workflow, see [Find and fix your agent's issues](engine.md). For how Engine handles your data, its GitHub and model subprocessor controls, and its compliance posture, see [Engine security](engine-security.md). For how Engine runs in a self-hosted deployment, see [Engine on self-hosted](engine-self-hosted.md).

## Get started

#### [Set up Engine](engine.md#set-up-engine)
Enable Engine for your organization and configure it for a tracing project.

#### [Engine issue categories](engine-issue-categories.md)
Reference for the failure categories Engine assigns to detected issues, with descriptions and detection methods.

#### [Engine webhook events](engine-webhooks.md)
Forward detected issues into your incident-management, paging, or chat tools.

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/engine-overview.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
