---
title: "Reusable Evaluators and Evaluator Templates in LangSmith"
description: "LangSmith Evaluation now includes 30+ evaluator templates and a central hub to reuse evaluators across projects — so you can ship better evals faster without starting from scratch each time."
source: "https://www.langchain.com/blog/reusable-langsmith-evaluator-templates"
category: "blog"
published: "2026-04-16T17:00:00.000Z"
author: "LangChain Accounts"
tags: [blog, reusable-langsmith-evaluator-templates]
---

# Reusable Evaluators and Evaluator Templates in LangSmith

- **Evaluator templates give you a running start.** LangSmith now includes 30+ templates covering safety, response quality, trajectory, user behavior, and multimodal evaluation. Use them as-is or customize them — they work for both online monitoring and offline experiment runs.
- **Build an evaluator once, apply it everywhere.** A new Evaluators tab centralizes every evaluator in your workspace. You can attach an existing evaluator to a new tracing project in seconds, so your safety checks and quality metrics stay consistent across the org without maintaining duplicate copies.
- **Good evals require coverage at multiple levels.** A single evaluator checking the final answer won't catch whether your retrieval agent pulled the right documents or your planning agent delegated correctly. Effective agent evaluation means testing individual steps, full trajectories, multi-turn conversations, and specific tool calls within a trace.
