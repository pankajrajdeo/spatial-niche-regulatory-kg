---
title: "LangChain Skills"
description: "Boost AI coding agent performance with LangChain Skills. These curated instructions for LangChain, LangGraph, and Deep Agents improve task success from 29% to 95%."
source: "https://www.langchain.com/blog/langchain-skills"
category: "blog"
published: "2026-03-04T18:00:19.000Z"
author: "LangChain Accounts"
tags: [blog, langchain-skills]
---

# LangChain Skills

We're releasing our first set of skills to give AI coding agents expertise in the open source LangChain ecosystem. This includes building agents with [LangChain](../langchain/overview.md), [LangGraph](../langgraph/overview.md), and [Deep Agents](../deepagents/overview.md). On our eval set, this bumps Claude Code's performance on these tasks from 29% to 95%.

## What are Skills?

Skills are curated instructions, scripts, and resources that improve coding agent performance in specialized domains. Importantly, skills are dynamically loaded through progressive disclosure — the agent only retrieves a skill when its relevant to the task at hand. This enhances agent capabilities, as historically, giving too many tools to an [agent would cause its performance to degrade](https://blog.langchain.com/react-agent-benchmarking/).

Skills are portable and shareable — they consist of markdown files and scripts that can be retrieved on demand. We're sharing a set of LangChain skills that can be ported to any coding agent that supports skill functionality.

## LangChain Skills

Within the [langchain-skills repo](https://github.com/langchain-ai/langchain-skills?ref=blog.langchain.com), we maintain a set of 11 skills, split broadly across 3 categories:

- **LangChain:** Guidance on how to use LangChain's `create_agent()`, middleware, and tool patterns. Fundamentals for working with the classic tool calling agent loop
- **LangGraph:** Guidance on how to work with LangGraph's primitives, and take advantage of its native support for Human In the Loop, durable execution, and more.
- **Deep Agents:** Guidance on working with our open source [Deep Agents package](https://github.com/langchain-ai/deepagents?ref=blog.langchain.com) and leverage its prebuilt middleware and `FileSystem`

## Skill Impacts

Using skills, we saw significant improvements in Claude Code's performance on basic LangChain, LangGraph, and Deep Agent tasks.

| Test | Model | Pass Rate |
| --- | --- | --- |
| Claude Code without Skills | Sonnet 4.6 | 25% |
| Claude Code with Skills | Sonnet 4.6 | 95% |

*Pass rate was calculated using LangSmith evaluations. We plan to open source the testing benchmark we used*

To see how easy these skills can make building agents, see the below video:

## **Installation**

To install these skills, you can use [`npx skills`](https://github.com/vercel-labs/skills?ref=blog.langchain.com):

**Local** (current project):

`npx skills add langchain-ai/langchain-skills --skill '*' --yes
`

**Global** (all projects):

`npx skills add langchain-ai/langchain-skills --skill '*' --yes --global
`

To link skills to a specific agent (e.g. Claude Code):

`npx skills add langchain-ai/langchain-skills --agent claude-code --skill '*' --yes --global
`

## **Conclusion**

We're excited for the community to use LangChain and [LangSmith](https://smith.langchain.com/?ref=blog.langchain.com) to improve your experience building with our ecosystem. We plan to continue adding skills content as new capabilities are added to our Open Source and LangSmith. In addition to these skills for LangChain open source - we are also releasing a set of [LangSmith skills](https://blog.langchain.com/langsmith-cli-skills/) today as well. If you have ideas for additional skills or improvements, we'd love to hear from you!
