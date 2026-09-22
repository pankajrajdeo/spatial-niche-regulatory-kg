---
title: "The runtime behind production deep agents"
description: "Deploying long horizon agents in production requires purpose-built infrastructure. This guide covers durable execution, memory, HITL, observability, and how deepagents deploy ships it all to..."
source: "https://www.langchain.com/blog/runtime-behind-production-deep-agents"
category: "blog"
published: "2026-04-20T08:03:00.000Z"
author: "LangChain Accounts"
tags: [blog, runtime-behind-production-deep-agents]
---

# The runtime behind production deep agents

- A good harness gives your agent the right prompts, tools, and skills. But deploying long-running agents in production requires durable execution, memory, multi-tenancy, human-in-the-loop, and observability. This infrastructure lives underneath the harness and keeps the agent running reliably across crashes, deploys, and long-running tasks.
- Durable execution is the foundation everything else depends on. Agents that run for minutes or hours, pause for human approval, or survive mid-run deploys all need checkpointed execution that can stop, resume, and retry across process boundaries. Streaming, human-in-the-loop, cron jobs, and concurrent message handling all build on top of it.
- Production agents need open and model-agnostic infrastructure. Deep Agents is MIT licensed, agents are exposed via open protocols (MCP, A2A), and memory lives in your own PostgreSQL. Teams keep full visibility into how their agent works and the ability to change it without a rewrite.
