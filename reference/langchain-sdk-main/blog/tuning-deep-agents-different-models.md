---
title: "Tuning Deep Agents to Work Well with Different Models"
description: "Deep Agents was previously designed in a generic way to work well across model families. Today we’re adding model-specific profiles to adjust prompts, tools, and middleware. We ship profiles for..."
source: "https://www.langchain.com/blog/tuning-deep-agents-different-models"
category: "blog"
published: "2026-04-29T17:00:00.000Z"
author: "LangChain Accounts"
tags: [blog, tuning-deep-agents-different-models]
---

# Tuning Deep Agents to Work Well with Different Models

‍💡**TL;DR: **[Deep Agents](https://github.com/langchain-ai/deepagents) was previously designed in a generic way to work well across model families. Today we’re adding model-specific profiles to adjust prompts, tools, and middleware. This allows us to better conform to prompting guides specific to model families. We ship profiles for OpenAI, Anthropic, and Google models out of the box, which we see leads to a 10–20 point jump on a subset of tau2-bench over the default harness.
