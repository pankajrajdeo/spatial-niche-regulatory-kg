---
title: "How we built LangChain&#39;s Paid Media Agent"
description: "How LangChain built a paid media agent to analyze campaign performance, optimize ads, propose changes, and turn marketing data into action."
source: "https://www.langchain.com/blog/paid-media-agent"
category: "blog"
published: "2026-09-14T01:07:00.000Z"
author: "LangChain Accounts"
tags: [blog, paid-media-agent]
---

# How we built LangChain&#39;s Paid Media Agent

- **Treat agents like knowledge workers.** The strongest results came from giving the agent a well-designed workspace with a sandbox, software, business context, and clear operating instructions. The system prompt became a map that helped the agent find what it needed without carrying everything in context.
- **Use models for judgment and code for consistency.** Calculations, source-of-truth rules, and safeguards were better handled in code. That made the agent faster, cheaper, and more reliable, while the model focused on interpreting results and recommending what to do next.
- **Design agents around the full workflow. **The agent needed to find the right tools, work within clear permissions, and move from analysis to action. That meant proposing campaign changes, routing them through human approval, and verifying that the changes were applied correctly.
- **Use abstractions to focus on the agent’s job. **[Managed Deep Agents](../langsmith/python/managed-deep-agents-overview.md) manages hosting, sandboxes, Slack integration, and schedules, so you can focus on the tools, context, and decision rules that make the agent useful.
