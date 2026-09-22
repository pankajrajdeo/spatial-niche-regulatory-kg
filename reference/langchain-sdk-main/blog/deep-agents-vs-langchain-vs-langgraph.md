---
title: "Deep Agents vs LangChain vs LangGraph"
description: "Deep Agents, LangChain, and LangGraph each offer distinct approaches to building agents. In this post, we cover the key distinctions between our open source frameworks and when you should reach for..."
source: "https://www.langchain.com/blog/deep-agents-vs-langchain-vs-langgraph"
category: "blog"
published: "2026-08-06T17:45:00.000Z"
author: "LangChain Accounts"
tags: [blog, deep-agents-vs-langchain-vs-langgraph]
---

# Deep Agents vs LangChain vs LangGraph

[Deep Agents](../deepagents/overview.md), [LangChain](../langchain/overview.md), and [LangGraph](../langgraph/overview.md) each offer distinct approaches to building agents. In this post, we cover the key distinctions between our open source frameworks and when you should reach for each one.

Deep Agents, LangChain, and LangGraph are the three layers of our open source agent stack, built on the same philosophy: builders should be able to own every part of their agent: the model they choose, the context it sees, and the harness that runs it.

Each layer plays a different role and offers a different amount of control. LangGraph is an agent runtime, LangChain is an agent framework, and Deep Agents is an agent harness. The runtime offers the most control and the least abstraction; the harness offers the inverse. All three are fully composable, so you can move between layers instead of picking one.

## What each layer offers

**Deep Agents** is an off-the-shelf agent harness: The job of an agent harness is to get the right context to the model at the right time via context engineering. Deep Agents comes with a bunch of best practices for this out of the box. These include:

- A [filesystem](../deepagents/backends.md), used to read and write context from (when you don’t want it directly in the context window of an LLM)
- [Subagents](../deepagents/subagents.md), useful for doing specialized work without bloating the main context window
- [Skills](../deepagents/skills.md), so you can provide instructions and scripts that an agent can load on demand
- [Memory](../deepagents/memory.md), so the agent can learn and improve across runs

There are many other pieces it ships with by default. These are opinionated context management best practices that our team constantly reviews and updates. One of the benefits of using Deep Agents is that you can trust us to *constantly* be surveying the landscape and bringing best practices here.

Getting started is simple with [`create_deep_agent:`](../deepagents/quickstart.md)

```
from deepagents import create_deep_agent

agent = create_deep_agent(
    model="anthropic:claude-sonnet-5",
    tools=[web_search],
    system_prompt="you are a research agent...",
    # skills path with citation-format, source-eval
    skills=["./skills/"],
)
```

`‍`**LangChain** is the agent framework: the abstraction and integrations layer. It ships with a super minimal agent harness. Whereas Deep Agents ships with best practices around context management, the LangChain agent abstraction is incredibly minimal and un-opinionated.

The core agent abstraction is pretty simple: an LLM, running in a loop, calling tools.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a74c8bfe906a5e35d75043a_core_loop%20(2).png)

This loop is incredibly simple, yet super powerful. There may, however, be times where you want to modify that loop. Usually this modifications are done to add more deterministic steps - like summarizing when context is close to full, or running a verifier at the end. One of the most powerful parts of LangChain’s agents is how we let you add these modifications. LangChain [middleware](https://www.langchain.com/blog/how-middleware-lets-you-customize-your-agent-harness) provides a set of hooks that can modify this loop in variety of ways.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a74c8b56383b9c1a6301dbd_middleware_hooks.png)

> Fun fact: Deep Agents is actually just the core LangChain agent plus a [bunch of middleware](../deepagents/overview.md#core-capabilities)!

You can use LangChain agents with the simple [`create_agent`](../langchain/quickstart.md) abstraction:

```
from langchain.agents import create_agent

agent = create_agent(
    model="anthropic:claude-sonnet-5",
    tools=[send_email],
    prompt="you are my email assistant...",
    middleware=[...]
)
```

**LangGraph** is the agent runtime: a graph-based framework for custom agent workflows, backed by a durable engine with [human-in-the-loop](../langgraph/interrupts.md), [fault tolerance](../langgraph/fault-tolerance.md), and observability at every step. One of the benefits of thinking of agents as graphs is that you can encode more determinism into them, and more closely control the steps that occur.

LangGraph powers the agent abstractions (seen above, displayed as graphs) in both LangChain and Deep Agents.

## When to reach for each

> **Rule of thumb
**Start with Deep Agents. It’s a very powerful agent harness with all of the bells and whistles included. When you need to model a complex workflow or want complete control of every step, reach for LangChain and LangGraph.

### Deep Agents

Reach for Deep Agents when you want a capable agent out of the box. This is where most builders should start, dropping down only if you need more control over the harness itself.

Say you're building a GTM agent. It needs memory per rep (with things like email style preferences and relationship understanding), skills for recurring workflows like QBR prep, and subagents to do deep research an account across call transcripts, news, and CRM history.

This isn’t just a toy example: we [built our GTM agent](https://www.langchain.com/blog/how-we-built-langchains-gtm-agent) on `deepagents`! It currently sees heavy traffic, almost 10k requests per week, and over 150 active users. 26% of the traffic is user initiated, and the remaining 74% is driven by ambient agent work. We deploy it with [LangSmith deployments](../langsmith/deployment.md), which supports both the bursty traffic and the scheduled/event-triggered ambient runs.

### LangChain

Reach for LangChain when you want the core building blocks and/or plan to assemble your own bespoke harness on top. LangChain's integrations and abstractions can be useful at any level: in custom graphs, with `create_agent`, and with `create_deep_agent`. It's a good fit too when you want fine-grained control over which tools and context reach the model at each step, ultra latency-sensitive apps often want this.

Say you're building a RAG docs Q&A bot: given a question, the agent searches your vector store for relevant pages. The agent loop governs whether or not a satisfactory answer has been reached, and drives the bot until the query is complete. This type of agent doesn’t need delegation via subagents or context management via a filesystem. LangChain's integrations let you plug in any vector store as a tool and pick whichever model you want, and `create_agent` gives you the loop that ties them together.

### LangGraph

Reach for LangGraph when your agent doesn't fit a standard loop, or you need to mix deterministic and agentic steps in the same workflow.

Say you're building a rental application processing pipeline. It has a few steps:

1. Extract income, credit, and rental history from each application
2. Score it against the landlord's criteria
3. Auto-approve clear qualifiers, reject clear non-qualifiers, or escalate borderline cases to a human.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a74c8cc24390199cb778830_rental_application_pipeline.png)

Only step 1 touches an LLM, the rest is fixed code. This workflow uses the power of LLMs to extract information from documents, but it doesn't give the model any tools with which it can take action. It's a relatively deterministic pipeline.

Already on LangGraph? Stay if the value is in the graph's shape and its deterministic steps. If your LangGraph flow is highly agentic, you could benefit from a migration to Deep Agents.

### All Three

All three are composable: drop `create_agent` or `create_deep_agent` into a larger LangGraph workflow, or drop a custom LangGraph workflow in as a subagent inside `create_agent` or `create_deep_agent`.

No matter which package you build with, you can deploy with [LangSmith deployments](../langsmith/deployment.md) and observe with [LangSmith observability](../langsmith/observability.md).

## Balancing determinism and agency

More autonomy gives an agent more potential value, at the cost of reliability. Determinism is the better call for sensitive or preset workflows, and for repeatable tasks that don't need to be agentic at all. The more dynamic an agent is, the more capable and creative it can be. For more examples of these tradeoffs in production, listen to [Max Agency](https://www.youtube.com/playlist?list=PLfaIDFEXuae3UwB1QGEjsRAr8BzCQss7s), our podcast on how teams design, deploy, and iterate on real agent systems.

The three layers sit at different points on that spectrum. LangGraph offers maximal determinism: it lets you encode domain knowledge directly into the graph's topology instead of leaving that judgment to a model. LangChain sits in the middle: the core agent loop is inherently non-deterministic, the model decides what happens next at every step. Deep Agents offers maximal agency: an agent loop that can run for longer and fan out at scale because of builtin features like summarization and subagents.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a74c8d63b2cf7af74e26d53_determinism_agency_spectrum.png)

> For deeper conversations with teams building the best agents, listen to our podcast, [**Max Agency**](https://podcasts.apple.com/us/podcast/max-agency/id1891551672)**.**‍

Many agents run on the core agent loop but still need a few deterministic steps built in: an approval step, a compliance check, a business rule that shouldn't be left to the model. Middleware solves this for Deep Agents and LangChain, letting you inject these steps and human-in-the-loop moments around the core loop.

If you need more flexibility or control than middleware offers through these builtin hooks, LangGraph is the escape hatch that lets you build a completely custom graph, [encoding your workflow's specific logic directly into its shape](https://www.langchain.com/blog/3-years-of-graph-engineering-with-langgraph), like the fan-out-and-synthesize example above.

## Why three layers

LangChain launched in October 2022 as the fastest way to get an LLM app running. As agents got more complex, people needed more control than a chain could give them, so we introduced LangGraph in January 2024: a graph-based runtime with durable execution, streaming, and human-in-the-loop built in as first class primitives.

As models got better, the core agent loop, a model that plans, calls tools, and reacts to results, became powerful enough to standardize. `create_agent` became LangChain's minimal harness, which we built on top of LangGraph because production agents need its primitives (human-in-the-loop, observability, fault tolerance, etc).

Then in July 2025 we went a layer further with Deep Agents, built on the same core loop, but with the aforementioned components (context management, subagents, etc.) bundled by default. Inspired by Claude Code and Manus, we bet builders wanted equally powerful agents for their own use cases, so we built `deepagents` as a general-purpose harness.

## TL;DR

Start with Deep Agents' [`create_deep_agent`](../deepagents/quickstart.md) if you're building or reworking an agent, it's what we use for all of our internal agents: GTM, coding, docs writing, and more.

Pick up LangChain's [`create_agent`](../langchain/quickstart.md) instead when you want less built-in context management and more fine-grained control over your agent loop.

Reach for LangGraph when you need even more control or determinism in a custom workflow.

**Acknowledgements**

Thanks to [Harrison Chase](https://x.com/hwchase17), [Hunter Lovell](https://x.com/huntlovell), [Morgan Curtis](https://www.linkedin.com/in/morganc41/), and [Sean Roche](https://linkedin.com/in/sean-roche01) for their thoughtful reviews!

‍
