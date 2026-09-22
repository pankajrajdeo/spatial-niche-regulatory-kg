---
title: "Running Subagents in the Background"
description: "Inline subagents block your supervisor and cut off mid-task updates. Deep Agents now supports async subagents — background tasks your supervisor can launch, steer, and cancel in real time."
source: "https://www.langchain.com/blog/running-subagents-in-the-background"
category: "blog"
published: "2026-04-16T18:16:00.000Z"
author: "LangChain Accounts"
tags: [blog, running-subagents-in-the-background]
---

# Running Subagents in the Background

- **Inline subagents block the supervisor agent for the duration of the task.** Because tool calls in an agent loop are synchronous, the supervisor can't respond to users, coordinate other work, or course-correct until the subagent finishes, a real problem when a task takes an hour or more.
- **Async subagents return a task ID immediately, so supervisors stay in control.** The supervisor can launch multiple subagents in parallel, keep talking to the user, send mid-task updates, or cancel work that's no longer needed, more like "fire-and-steer" than "fire-and-forget."
- **Async subagents are built on Agent Protocol, so you're not locked into one deployment.** They run as fully separate agents with their own process and state, and can be hosted on LangSmith deployments or self-hosted on your own infrastructure, the supervisor manages them through the same standard interface either way.
