---
title: "Jev-as-a-Judge for Agent Evals"
description: "We tested using Jev-as-a-Judge against LLM judges on accuracy, repeatability, latency, and cost to see whether System One models could offer a new approach to agent evaluation."
source: "https://www.langchain.com/blog/jev-agent-evals-langsmith"
category: "blog"
published: "2026-09-20T17:00:00.000Z"
author: "LangChain Accounts"
tags: [blog, jev-agent-evals-langsmith]
---

# Jev-as-a-Judge for Agent Evals

- **Jev is a fundamentally different kind of evaluator.** It returns typed answers directly instead of generating text like an LLM judge.
- **Jev was dramatically more consistent on continuous scoring.** Its quality-score variance was 92–913x lower than GPT-5.6 Luna, Terra, and Claude Sonnet 4.6.
- **Jev was also the fastest and cheapest.** It averaged 0.44s and $0.00035/call ($0.34 total vs. $28.17 for Claude).
- **The results are promising, but early.** Despite this being a narrow test, Jev's performance points to a compelling new direction for agent evals.
