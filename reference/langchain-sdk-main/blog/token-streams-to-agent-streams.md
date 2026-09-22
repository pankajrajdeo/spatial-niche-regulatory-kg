---
title: "From Token Streams to Agent Streams"
description: "Move beyond token streaming. Learn how the latest streaming primitives in Deep Agents, LangChain, and LangGraph enable typed events, scoped subscriptions, subagent visibility, multimodal outputs, and..."
source: "https://www.langchain.com/blog/token-streams-to-agent-streams"
category: "blog"
published: "2026-05-21T17:00:00.000Z"
author: "LangChain Accounts"
tags: [blog, token-streams-to-agent-streams]
---

# From Token Streams to Agent Streams

- **Streaming needs to evolve beyond tokens**
Modern agents generate messages, tool calls, subagent activity, state changes, approvals, and media, requiring structured event streams instead of flat text output.
- **Typed events and projections simplify frontend development**
Applications subscribe directly to messages, tool calls, state, subagents, or custom channels while the runtime handles assembly, ordering, and reconnection.
- **Scoped subscriptions make complex agent UIs scalable**
Frontends only stream the parts of the agent tree they render, enabling efficient subagent inspectors, dashboards, and long-running production workloads.
- **One streaming model works across runtimes and modalities**
The same architecture powers local and remote runs, React/Vue/Svelte/Angular SDKs, and supports text, tools, images, audio, video, and custom application events.
