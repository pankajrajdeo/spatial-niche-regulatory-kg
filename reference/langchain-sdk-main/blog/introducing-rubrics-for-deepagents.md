---
title: "Introducing Rubrics: Build Agents that Evaluate and Correct Their Work"
description: "Deep Agents&#39; RubricMiddleware adds a self-evaluation loop to your agent runs. Set a rubric, configure a grader, and get reliable outputs on tasks where correctness matters."
source: "https://www.langchain.com/blog/introducing-rubrics-for-deepagents"
category: "blog"
published: "2026-06-02T16:30:00.000Z"
author: "LangChain Accounts"
tags: [blog, introducing-rubrics-for-deepagents]
---

# Introducing Rubrics: Build Agents that Evaluate and Correct Their Work

- Agents often produce outputs that head in the right direction but don't fully land on the first attempt.
- `RubricMiddleware` is how you tell the agent what "done" looks like — and make it keep going until it gets there.
- Most effective for tasks with clear, verifiable success criteria like passing tests, avoiding forbidden patterns, covering required sections.
