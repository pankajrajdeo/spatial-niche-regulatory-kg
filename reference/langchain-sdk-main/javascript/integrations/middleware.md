---
title: "Middleware integrations"
description: "Integrate with middleware using LangChain JavaScript."
source: "https://docs.langchain.com/oss/javascript/integrations/middleware"
category: "docs"
tags: [docs, javascript, integrations, middleware]
---

# Middleware integrations

> Integrate with middleware using LangChain JavaScript.

Browse available middleware for different providers or contribute your own to the ecosystem. Learn more about how middleware works in the [middleware overview](../langchain/middleware/overview.md) and how to use middleware with Deep Agents in the [Deep Agents docs](../deepagents/customization.md#middleware).

## Share your middleware

Middleware enables context engineering, harness customization, and runtime safety controls. It is a useful extension point in LangChain and we love highlighting what the community builds with it:

#### [Add an official integration](../contributing/implement-langchain.md#middleware)
Follow the contributing guide to build and publish a middleware package.

#### [Share a community middleware](https://github.com/langchain-ai/docs)
Open a PR to the docs repo to add your middleware to the table below.

## Official integrations

| Provider                                                         | Middleware available | Source                                                                                                                                      | Downloads                                                                                                                                                                                                                                                              |
| :--------------------------------------------------------------- | :------------------- | :------------------------------------------------------------------------------------------------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`AWS middleware`](middleware/aws.md)  | Prompt caching       | [`langchain-ai/langchain-aws`](https://github.com/langchain-ai/langchain-aws)                                                               | <span data-sort-value="3181274"><a href="https://www.npmjs.com/package/@langchain/aws" target="_blank">  <img src="https://img.shields.io/npm/dm/@langchain/aws?style=flat-square&label=%20&" alt="Downloads per month" class="rounded not-prose" /></a></span> |
| [`Anthropic`](middleware/anthropic.md) | Prompt caching       | [`langchain-ai/langchainjs`](https://github.com/langchain-ai/langchainjs/tree/main/libs/langchain/src/agents/middleware/provider/anthropic) | <span data-sort-value="-1">N/A</span>                                                                                                                                                                                                                                  |

## Community integrations

> [!NOTE]
> The community maintains these middleware integrations. They are contributed on an open-source basis and are not managed or maintained by LangChain.

| Middleware                                                                            | Description                                                                                                                                                                                                        | Source                                                                                                  |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------- |
| [langchain-task-steering](https://github.com/edvinhallvaxhiu/langchain-task-steering) | Implicit state-machine middleware for ordered task pipelines with per-task tool scoping, dynamic prompt injection, and composable completion validation.                                                           | [`edvinhallvaxhiu/langchain-task-steering`](https://github.com/edvinhallvaxhiu/langchain-task-steering) |
| [Nuggets Authority](https://nuggets.life)                                             | Pre-execution authority enforcement for tool calls. Verifies a scoped, signed delegation before each tool runs, fails closed on deny, and emits an independently verifiable cryptographic proof of every decision. | [`NuggetsLtd/langchain-nuggets`](https://github.com/NuggetsLtd/langchain-nuggets)                       |

Have a middleware to share? [Open a PR](https://github.com/langchain-ai/docs) to add it here.

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/middleware/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
