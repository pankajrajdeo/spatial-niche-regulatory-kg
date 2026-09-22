---
title: "A Developer’s First 10 Minutes: Secure LangChain Agents with Cisco AI Defense"
description: "Cisco AI Defense integrates with LangChain middleware to enforce runtime security for agents, blocking prompt injection, PII exposure, and risky tool calls from one place."
source: "https://www.langchain.com/blog/secure-agents-cisco-ai-defense"
category: "blog"
published: "2026-04-16T16:00:00.000Z"
author: "LangChain Accounts"
tags: [blog, secure-agents-cisco-ai-defense]
---

# A Developer’s First 10 Minutes: Secure LangChain Agents with Cisco AI Defense

- **Middleware is the right place to enforce agent security.** Adding security checks at the middleware layer keeps your `langchain` code clean and creates one consistent enforcement point across the agent loop, instead of bolting on logic across prompts, tools, and custom orchestration code.
- **Cisco AI Defense gives you two modes: monitor and enforce.** Monitor mode records risk signals and decision traces without interrupting the agent. Enforce mode blocks policy violations with an auditable reason, so you can always point to exactly what was stopped and why.
- **Protection applies across LLM calls, MCP tool calls, and middleware.** Agents don't just generate text, they call tools, retrieve data, and take actions autonomously. Runtime protection needs to cover all three layers, especially in multi-agent systems where an orchestrator is chaining agents together at runtime.
