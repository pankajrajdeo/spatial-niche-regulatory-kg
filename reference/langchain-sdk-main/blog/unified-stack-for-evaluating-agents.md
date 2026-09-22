---
title: "Harbor x LangChain: A Unified Stack for Evaluating Agents"
description: "Evaluating long-running, stateful agents needs a new kind of runner. Here&#39;s how Deep Agents, LangSmith sandboxes, and observability plug into Harbor."
source: "https://www.langchain.com/blog/unified-stack-for-evaluating-agents"
category: "blog"
published: "2026-06-30T15:00:00.000Z"
author: "LangChain Accounts"
tags: [blog, unified-stack-for-evaluating-agents]
---

# Harbor x LangChain: A Unified Stack for Evaluating Agents

- One small entry point connects your agent to Harbor. A `langgraph.json` registry plus a `make_graph` factory is the only glue you write, and that factory can stay model-agnostic by reading the model Harbor passes from the command line
- Cloud sandboxes let you scale evals horizontally and run agents in isolation. Each trial gets a fresh LangSmith sandbox, so trials never share state, and you can run hundreds in parallel instead of churning through them serially on one machine
- Traces turn scores into explanations. With the `langsmith` plugin, every job lands as a dataset and experiment with the verifier's reward as feedback, and agent traces attach directly so you can see why a trial passed or failed, not just whether it did
