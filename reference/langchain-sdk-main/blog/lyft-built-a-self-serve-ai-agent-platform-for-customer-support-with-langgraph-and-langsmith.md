---
title: "How Lyft Built a Self-Serve AI Agent Platform for Customer Support with LangGraph and LangSmith"
description: "Lyft used LangGraph and LangSmith to build a self-serve AI agent platform for customer support, cutting agent development from months to weeks."
source: "https://www.langchain.com/blog/lyft-built-a-self-serve-ai-agent-platform-for-customer-support-with-langgraph-and-langsmith"
category: "blog"
published: "2026-05-27T15:25:00.000Z"
author: "LangChain Accounts"
tags: [blog, lyft-built-a-self-serve-ai-agent-platform-for-customer-support-with-langgraph-and-langsmith]
---

# How Lyft Built a Self-Serve AI Agent Platform for Customer Support with LangGraph and LangSmith

- **Lyft moved agent development closer to the people who understand customer issues best.** By letting ops teams, VoC leads, and product managers define agents through prompts and configuration, Lyft reduced the need for MLEs to manage every iteration.
- **A router-based multi-agent architecture helped support complex customer workflows.** Lyft uses LangGraph to route rider and driver requests across specialized subagents, with safety checks, state management, and handoffs built into the flow.
- **Production quality depends on evaluation, monitoring, and prompt discipline.** Lyft uses LangSmith for tracing, dashboards, and LLM-as-a-judge evaluation, but the team found that structured prompt writing became one of the biggest factors in agent reliability.
