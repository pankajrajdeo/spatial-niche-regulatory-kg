---
title: "How Toyota North America Put Enterprise AI on the Balance Sheet with Deep Agents and LangSmith"
description: "See how Toyota North America uses Deep Agents and LangSmith to run 50+ production agents, cut delivery from 6 months to 4 days, and track AI ROI."
source: "https://www.langchain.com/blog/how-toyota-north-america-put-enterprise-ai-on-the-balance-sheet-with-deep-agents-and-langsmith"
category: "blog"
published: "2026-08-24T17:30:00.000Z"
author: "LangChain Accounts"
tags: [blog, how-toyota-north-america-put-enterprise-ai-on-the-balance-sheet-with-deep-agents-and-langsmith]
---

# How Toyota North America Put Enterprise AI on the Balance Sheet with Deep Agents and LangSmith

[Toyota Motor North America](https://www.toyota.com/usa) is one of the world's premier automotive manufacturers. Their enterprise AI team, spanning engineers, architects, product managers, and internal evangelists, functions like an internal startup. The roughly 35-person team sets the AI North Star for the entire enterprise, architects the standards every application must follow, and builds the highest-priority AI products with [Deep Agents](https://www.langchain.com/deep-agents), [LangGraph](../langgraph/overview.md), and [LangSmith](https://www.langchain.com/langsmith-platform).

## A small team with an enterprise-wide mandate

Toyota's enterprise AI team serves use cases across every facet of the company: manufacturing, supply chain, financial services, dealerships, on-vehicle development, R&D, and more. The three-dozen-person team cannot afford to build tooling from scratch for each new application.

*"We went through the pain of building everything ourselves. We experienced a lot of that heartache to try to roll our own solutions, and it just costs a lot of labor, a lot of engineering time,"* said Kordel France, Director of AI Engineering at Toyota Motor North America.

With a mandate to clear a 6-to-7-figure annual ROI threshold for each project, the team needed a solution that met the demand for shipping agents that could materially change manufacturing output and efficiency.

## ToyotaGPT: from 6 months and 6 engineers to 4 days and 1 engineer

At the center of Toyota's enterprise AI portfolio is ToyotaGPT, the team's internal flagship platform. It consists of a growing library of custom, domain-specific agents. Employees across departments use ToyotaGPT for answers grounded in Toyota's internal data, from manufacturing documentation to R&D reports to supply chain records. Access is permission-gated to the underlying data; for example, if a team member doesn't have SharePoint access to a dataset, the agent doesn't surface it.

The platform now has more than 50 agents in production. Before the team built their current development infrastructure on Deep Agents and LangGraph, shipping a new agent took 6 months and 6 engineers. Today it takes [4 days and 1 engineer](https://www.youtube.com/watch?v=nUNuNxMhwug).

Ravi Chandu Ummadisetti, Director of Agentic AI and Product Research, described the foundation: *"LangChain’s Deep Agents is a beautiful concept. With a single command, `create deep agent`, you get a powerful harness and an entire ecosystem for each new agent."*

Rather than encoding Toyota domain knowledge inside individual agents, the enterprise AI team built a library of reusable skills covering manufacturing, supply chain, R&D, branding, and more. Those skills are injected into Deep Agents at runtime, feeding institutional knowledge directly to the model in a form that's portable across use cases.

## GearPal: keeping every machine on the production line running

The manufacturing line is Toyota's greatest product. It produces every vehicle Toyota sells, and it's the system that made Toyota one of the greatest manufacturers in the world—a self-evolving operation that continuously adapts to new technologies. Every minute of unplanned downtime costs Toyota hundreds of thousands to millions of dollars depending on where in the line the stoppage occurs.

To minimize downtime, the enterprise AI team built GearPal, an application that gives any machine technician a natural-language interface to diagnose issues with any manufacturing robot or asset on the line. A technician can walk up, ask why a machine is broken and how to fix it, and GearPal surfaces the relevant diagnostics, historical service records, and repair guidance. What previously could take 5 to 6 hours of diagnosis now resolves in 2 to 3 minutes.

GearPal also addresses a generational knowledge-transfer problem; as veteran technicians retire, newer employees need tools that surface institutional expertise. Here skills play a role too, codifying machinery knowledge to help new and seasoned employees fix issues fast. The team also added an LLM gateway to handle LLM fallbacks in the case of a provider outage, to ensure GearPal is reliable enough to deploy on a live production line.

## R&D GPT: compressing years of research into months

On the R&D side, Ravi's team is tackling a different but equally high-stakes problem. Toyota's research materials are vast, highly technical, and distributed across dozens of document repositories. Developing something as seemingly simple as the paint on a Toyota vehicle involves years of formulation work, with testing across extreme heat and cold, analysis of corrosion resistance, and validation of robotic application precision.

R&D GPT is an agent, built on Deep Agents, that allows researchers to query all of Toyota's internal R&D materials and surface nuances that would otherwise require weeks of manual review. Since launching the agent, research timelines have compressed from roughly 3 years to 1 year.

A key technical challenge was retrieval precision across overlapping domains (paint, corrosion, seat materials, leathers, etc.). For example, early on, a query about paint would sometimes incorrectly pull from the corrosion database instead. In response, the team built a LangGraph-powered parallel tool-calling system. When the agent can't find documents in the primary tool, it simultaneously queries secondary tools and merges the results before responding.

## LangSmith: the Andon Board for AI

The Andon board, one of Toyota’s foundational manufacturing principles, gives everyone on the factory floor a real-time view of what's running, what's failing, and where resources need to go. LangSmith is, in Kordel's words, the Andon board for Toyota's AI applications.

*"LangSmith gives us the ability to monitor all of our agents, understand what's working, what's not, what tool calls have failed, what PR just broke the pipeline, and what features our users are adopting,"* explained Kordel. *"This observability is critical not only for us building better products, but also for convincing our stakeholders that every tool we're building is secure."*

With LangSmith, the team can trace individual agent interactions, identify retrieval failures, and quantify behavior patterns across user populations—essential for bridging the gap between engineering confidence and executive sign-off. *“LangSmith observability is probably our largest asset from the entire LangChain ecosystem," *said Kordel.

The team also applies LangSmith Insights Agent to ToyotaGPT at the platform level, using it to understand how different departments are adopting the system and identify what new, purpose-built agents are worth prioritizing next.

## Tracking towards 8-figure savings

Each manufacturing use case is on track to deliver at least 6 figures in annual savings per line, per shop, and per plant. Extrapolated across Toyota's North American manufacturing footprint, Kordel projects multi-million-dollar annual savings per facility as the portfolio matures.

*"Hopefully next year when we talk, I can say we're in the 7-to-8-figure range of savings. We’re predicting that over the next few years,"* said Kordel.

More immediately, the 4-day agent delivery cycle means the team can now keep pace with the demand signal coming from across the enterprise. With 50+ agents in production and a scalable platform, the enterprise AI team's goal is straightforward: *“AI will be on the balance sheet, and it will be because of LangChain. We'll see the effects and we'll see the return on investment.”*

*Learn more about how *[*Deep Agents*](https://www.langchain.com/deep-agents)* and *[*LangSmith*](https://www.langchain.com/langsmith-platform)* can accelerate agent development*.
