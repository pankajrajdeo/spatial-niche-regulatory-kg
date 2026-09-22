---
title: "Introducing LangSmith Engine"
description: "LangSmith Engine watches your production traces, clusters failures into named issues, and proposes targeted fixes and eval coverage. Stop manually triaging agent failures."
source: "https://www.langchain.com/blog/introducing-langsmith-engine"
category: "blog"
published: "2026-05-13T17:40:00.000Z"
author: "LangChain Accounts"
tags: [blog, introducing-langsmith-engine]
---

# Introducing LangSmith Engine

- **The agent development lifecycle now moves faster.** LangSmith Engine replaces the manual cycle of reading traces, spotting patterns, and writing fixes by doing it continuously — clustering production failures into named issues, diagnosing root causes against your code, and drafting PRs and evaluators for your review.
- **Every resolved issue makes your eval suite stronger.** When Engine surfaces a fix, it also proposes a custom online evaluator and pulls failing traces into your offline eval dataset — so the same failure can't silently recur after you ship.
- **It's built on top of your existing LangSmith setup.** Engine plugs into your current tracing projects, evaluator results, and repositories — no new infrastructure required. Connect a project, optionally connect your repo, and it starts surfacing issues from production automatically.
