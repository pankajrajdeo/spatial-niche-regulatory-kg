---
title: "Why managed agents are the next big thing in agent building"
description: "Managed Deep Agents gives developers a managed way to build, run, and deploy Deep Agents with built-in runtime, streaming, sandboxes, evals, memory, and auth."
source: "https://www.langchain.com/blog/why-managed-agents-are-the-next-big-thing-in-agent-building"
category: "blog"
published: "2026-08-12T18:00:00.000Z"
author: "LangChain Accounts"
tags: [blog, why-managed-agents-are-the-next-big-thing-in-agent-building]
---

# Why managed agents are the next big thing in agent building

Last week we launched Managed Deep Agents - the easiest way to build, run and deploy production agents. We have a [release blog](https://www.langchain.com/blog/managed-deep-agents-is-now-in-public-beta) and [docs](../langsmith/python/managed-deep-agents-overview.md) if you want to read more. In this article I want to talk about the journey to get here and why I’m so excited about what I think is the next step of agent building.

I think there are a few distinct periods of agent building.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a7d08584326c7022acde00a_agent-evolution-timeline-dark-3000x3000%20(2).png)

Briefly covering two of the earlier ones:

Early AI Frameworks/Apps (Late 2022/Early 2023): LangChain was [launched October 2022](https://www.langchain.com/blog/announcing-our-10m-seed-round-led-by-benchmark), ChatGPT in [November 2022](https://openai.com/index/chatgpt/), AutoGPT [early 2023](https://github.com/Significant-Gravitas/AutoGPT). All of these were early AI frameworks or apps that first started to leverage LLMs.

More mature AI frameworks like [LangGraph](https://www.langchain.com/blog/langgraph), Google ADK, Vercel’s AI SDK emerged in 2024 and first half of 2025. These gave developers more control over LLMs. People weren't really building agents we think of them today, but they were able to build more complex AI apps.

Sometime in early to mid 2025 the models started to get good enough to power what we think of agents today: [LLMs running in a loop calling tools](https://www.langchain.com/blog/langgraph). This is the core primitive, the core algorithm, that underpins agents today. Really early agent apps like Manus, Deep Research, and Claude Code followed this same pattern.

When the models became good enough to just run in a loop and call tools, this became a more solid foundation we could build upon. The concept of Agent Harnesses like Claude Code, Pi, and Deep Agents emerged as we figured out the rights tools and environments to add into this loop. We launched [Deep Agents nearly a year ago](https://www.langchain.com/blog/doubling-down-on-deepagents) - one of the first attempts to take some of the patterns we saw in the application layer and bring them to a general use harness.

Over the past year, there have been two set of learnings that have shaped the next direction.

First, we started to learn some of the common primitives for running these agent harnesses at scale. Things like [durable execution](../langsmith/deployment.md) to back the running of the agent loop, and [sandboxes](../langsmith/sandboxes.md) for running untrusted code. “[Separating the brain and hands](https://www.anthropic.com/engineering/managed-agents)” became a common design choice. The infrastructure required for running these agents started to become more known.

Second, standards for how users should drive these agent harnesses emerged. Things like [AGENTS.md](https://agents.md/) for base set of instructions, MCP for plugging into other systems, skills for progressive disclosure of context. These became standards to control and drive parts of harnesses.

Both of these contributed to the rise of “managed agent” experiences. Where the agent harness is run on managed infrastructure, and builders use these standards to drive agent behavior.

I think these managed agent experiences will unlock a new wave of building production agents. When building agents, there are three parts:

1. The business logic (context, tools, and instructions) you provide
2. The harness
3. The infrastructure to run the harness in production

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a7d086a9166aa6bc4dd73e5_agent-stack_dark_nologo%20(2).png)

You always need to bring your own business logic. Off-the-shelf harnesses like [Deep Agents](../deepagents/overview.md) have made it easier to get started. But there’s lot of challenges you face when trying to run an agent in production!

- [Runtime](../langsmith/deployment.md): How do I run it in a reliable way? How do I resume a run if it fails halfway through?
- [UX](../langsmith/event-streaming.md): How do I stream events back to a UI? How do I bring my agent to where users already are?
- [Sandboxes](../langsmith/sandboxes.md): Where does untrusted code execute?
- [Context Management](../langsmith/context-hub.md): Where do instructions, skills, and other context live? Can I have business users (or subject matter experts) edit them directly?
- [Evaluation](../langsmith/harbor-integrations.md): How do I evaluate changes to prompts, tools, or models?
- [Memory](../langsmith/managed-deep-agents-memory.md): What does the agent remember?
- [Auth](../langsmith/auth.md): Who is allowed to call it, and what are they allowed to do? When the agent calls external systems, who does it act as?

These are a lot of different considerations! Managed agent services make a lot of this easier, by bundling the harness with the infrastructure. This makes it much easier for builders - rather than Having to pick a harness and then assemble all these pieces individually, they just pick a bundle of the harness and infrastructure. Much easier!

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a7d0881b4424075e4356fbb_managed-deep-agents-stack_dark%20(3).png)

One early version of this that we worked on was [Fleet](https://www.langchain.com/blog/introducing-langsmith-fleet) - our no-code agent building platform. This pushed the “managed” aspect to the extreme - Fleet is built for non-developers and is purely UI based. We used standards like [AGENTS.md](http://AGENTS.md), skills, and MCP to make it easy to port agents back to code if needed.

One thing we purposefully did here - we represented and defined Fleet agents just as files in a filesystem. All the standards above - those just became files that our harness would load. We even had a toggle to show Fleet agents in a file explorer.

This targeted a bit of a different audience for us - non developers. Because it was so “managed”, and because our target audience is largely developers, we kept on getting more and more technical feature requests: custom middleware, custom tools as code, programmatic creation of agents from the API.

Claude Managed Agents was launched a little after this. It also had a UI based experience, but more so was API first, which targeted developers much more. It made it super easy to create agents via an API, and used a lot of the same standards. It relied less on treating the agent definition as just files in a filesystem. It introduced some cool concepts like “[dreaming](https://claude.com/blog/new-in-claude-managed-agents)”.

Vercel launched Eve a month or so as another entry here. It very much leans into [representing agents as files](https://vercel.com/docs/eve/concepts), uses a lot of the same standards, and bundles up infrastructure to make it easy to deploy.

Today we’re launching our version of managed agents meant for developers: Managed Deep Agents. It builds upon the Deep Agents harness, represents agents as files, but allows for a lot more configurability than Fleet: you can bring [custom middleware](../langsmith/managed-deep-agents-middleware.md) and [custom tools as code](../langsmith/managed-deep-agents-tools.md). It bundles in infrastructure to make it easy to run agents in production:

- Runtime: [LangSmith Deployments](../langsmith/deployment.md)
- UX: [Streaming from LangSmith Agent Server](../langsmith/event-streaming.md), [Channels](../langsmith/managed-deep-agents-channels.md)
- Sandboxes: [LangSmith Sandboxes](../langsmith/sandboxes.md)
- Context Management: [LangSmith Context Hub](../langsmith/context-hub.md)
- Evaluation: [Harbor](../langsmith/harbor-integrations.md)
- Memory: [Opinionated on top of Deep Agents](../langsmith/managed-deep-agents-memory.md)
- Auth: [AuthN built in](../langsmith/python/managed-deep-agents-identity.md)

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a7aa8e9a63c8c26e3329f15_managed-deep-agents-architecture.jpeg)

This is one of the launches I’m most excited about in a while. I think it will make it so much easier for developers to build and deploy agents in production, not just run them locally.

If you want to get started, I filmed a "[Managed Deep Agents explained in 20 minutes](https://youtu.be/yi-XZnAVFJg)" video that I think is the best place to get started.

I also think it is still early when it comes to building agents. More infrastructure requirements will emerge. More standards will be needed. We want to learn those and build those with you, so please reach out with feedback.
