---
title: "Prompt & Context Hub"
description: "Store, version, and update the prompts and contexts your agents use in production."
source: "https://docs.langchain.com/langsmith/context-hub"
category: "docs"
tags: [docs, langsmith, context-hub]
---

# Prompt & Context Hub

> Store, version, and update the prompts and contexts your agents use in production.

Prompts, retrieval context, skills, and task instructions change more often than the application code around them, and often need to be edited by people who are not engineers. Use the Prompt & Context Hub to store, version, review, and update the non-code parts of your agent so you can change behavior without a full deploy and let domain experts own the context they know best.

[Prompts](#prompts) are individual message templates you send to a model. [Contexts](#context-hub) are versioned bundles of instructions and tools that define a skill or a full agent, promoted through environments so your agents pull the right version.

## Prompts

#### [Create and update prompts](create-a-prompt.md)
Build prompts via the UI or SDK, configure settings, use tools, add multimodal inputs, and connect model providers.

#### [Manage prompts](manage-prompts.md)
Organize with tags, commit changes, trigger webhooks, and share through the public prompt hub.

#### [Explore the prompt hub](manage-prompts.md#public-prompt-hub)
Browse and manage prompt tags and discover community prompts from the LangChain Hub.

#### [Open the Playground](prompt-engineering-concepts.md#playground)
Test and experiment with prompts using custom endpoints and model configurations.

#### [Follow tutorials](optimize-classifier.md)
Learn step-by-step techniques, like optimizing classifiers and advanced prompt engineering.

> [!NOTE]
> Use the **[Chat](chat.md)** in the Playground to optimize prompts, generate tools, and create output schemas with AI-powered assistance.

## Context Hub

#### [Concepts](context-engineering-concepts.md)
Learn the core concepts of context engineering: skills, agents, versioning, and sharing.

#### [Use the Context Hub](use-the-context-hub.md)
Create a context, view its files and history, and promote it to an environment.

#### [Manage contexts with the SDK](manage-contexts-sdk.md)
Push, pull, list, and delete agent and skill repos in the Context Hub programmatically.

#### [Configure commit webhooks](context-hub-webhooks.md)
Send every agent and skill commit in your workspace to an external HTTPS endpoint.

> [!NOTE]
> To set up a LangSmith instance, visit the [Platform setup section](platform-setup.md) to choose between cloud, hybrid, or self-hosted. All options include observability, evaluation, prompt engineering, and deployment.

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/prompt-context-hub.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
