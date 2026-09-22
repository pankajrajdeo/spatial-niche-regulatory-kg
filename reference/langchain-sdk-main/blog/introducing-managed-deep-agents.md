---
title: "Introducing Managed Deep Agents"
description: "Run deep agents in production with durable execution, sandboxes, tool access, and LangSmith observability, without building the runtime yourself. Now in private beta"
source: "https://www.langchain.com/blog/introducing-managed-deep-agents"
category: "blog"
published: "2026-05-13T17:35:00.000Z"
author: "LangChain Accounts"
tags: [blog, introducing-managed-deep-agents]
---

# Introducing Managed Deep Agents

- **Building agents is getting easier. Operating them is still the hard part.** Long-running agents need durable execution, tool access, sandboxes, memory, and tracing, and assembling that yourself takes time away from building the actual agent.
- **Managed Deep Agents gives the open-source harness a durable home in LangSmith.** You keep the agent definition in your repo. We handle the runtime: threads, checkpointing, streaming, context, and observability.
- **Agents that run over time need context that persists over time.** Context Hub gives your agent a managed place to store and update what it knows so it can improve from real usage, not just from what you put in the prompt at deploy time.
