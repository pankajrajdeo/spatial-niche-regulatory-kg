---
title: "LangSmith vs Arize: AI agent observability, evals, and deployment compared"
description: "Compare LangSmith and Arize for AI agent engineering. Feature-by-feature breakdown of observability, evaluation, deployment, pricing, and migration."
source: "https://www.langchain.com/resources/langsmith-vs-arize"
category: "resources"
published: "2026-09-10"
author: "LangChain"
tags: [resources, langsmith-vs-arize]
---

# LangSmith vs Arize: AI agent observability, evals, and deployment compared

[LangSmith](https://www.langchain.com/langsmith-platform) is a fully framework-agnostic platform for agent engineering, combining observability, evaluation, and deployment so teams can iterate quickly. It is trusted by Harvey, Clay, Cloudflare, Cisco, and millions of developers worldwide. Both LangSmith and Arize provide tracing and evals for LLM applications and AI agents in production. However, LangSmith supports the full Agent Development lifecycle, from traces to evals to deployment, in one platform, and isn't just for those in the LangChain/LangGraph ecosystem.

- **Full-lifecycle agent engineering in one platform**
- **Production traces that feed directly into evals and improvements**
- **Built-in deployment for stateful agents**

> [Get a demo of LangSmith's agent engineering platform](https://www.langchain.com/contact-sales)

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a24cfe111c01721b6fbb889_5.png)

## What sets LangSmith apart from Arize?

Arize earns G2 praise for intuitive navigation and responsive support. Its OpenTelemetry (aka OTel)-native instrumentation is strong, making it a capable monitoring platform for teams that span generative AI and classical ML.

In August 2026, Dynatrace announced a definitive agreement to acquire Arize. Dynatrace says that after the acquisition closes, the two companies will continue to operate independently. The comparison below reflects Arize as it stands today.

The differences show up when you need more than monitoring.

| Capability | LangSmith | Arize |
| --- | --- | --- |
| End-to-end agent tracing | ✓ | ✓ |
| Trace automations (routing, webhooks, retention) | ✓ (Extensive) | Limited (dataset adds only) |
| Trace comparison (side-by-side) | ✓ | ✗ |
| Thread-level evaluation (full conversations) | ✓ | ✓ (AX only) |
| Online evals on production traffic | ✓ | ✓ (AX only) |
| Offline evals on datasets | ✓ | ✓ |
| Self-improving evaluators | ✓ | ✗ |
| Automated usage pattern insights from traces | ✓ | ✓ |
| Human-in-the-loop annotation queues | ✓ | ✓ |
| Agent deployment infrastructure | ✓ | ✗ |
| No-code agent creation | ✓ | ✗ |
| CI/CD quality gates for evals | ✓ | Manual Integration |
| Traditional ML/CV monitoring | ✗ | ✓ |
| Source-available self-hosting | ✗ | ✓ (Phoenix) |
| SDK language support | Python, TS, Go, Java | Python only |
| SDK operability | Extensive: 100+ methods, single client | Limited: ~20 methods, multiple clients |

## Where teams hit friction with Arize

Arize is a capable platform. These are scope boundaries that matter as your AI agents grow more complex.

- **Self-hosted ingest performance under sustained load:** A high-priority GitHub issue reports that Phoenix's BulkInserter can open up to seven database sessions per loop iteration. That risks connection-pool exhaustion. A separate issue reports 504 errors when exporting large span datasets via `get_spans_dataframe()`. (Sources:[Phoenix #12358](https://github.com/Arize-ai/phoenix/issues/12358);[Phoenix #11873](https://github.com/Arize-ai/phoenix/issues/11873))
- **Data delay for traces:** After traces are ingested, there is a notable delay before data appears in Arize's project dashboard. Data appears incrementally, and complete traces aren't visible until much later. By contrast, LangSmith traces appear in seconds.
- **Token counts not surfaced in REST API:** An open GitHub issue notes that Phoenix tracks token counts but doesn't expose them in project-level REST endpoints, it only exposes them via span attributes and GraphQL. (Source:[Phoenix #12349](https://github.com/Arize-ai/phoenix/issues/12349))
- **Latency and custom instrumentation friction:** A G2 enterprise reviewer from June 2025 cited latency and custom instrumentation as the platform's main downside. (Source:[G2](https://www.g2.com/products/arize-ai/reviews/arize-ai-review-11330759))
- **Agent workflow depth perception:** community commenters noted that Phoenix feels more oriented toward model monitoring than productized agent workflows. (Source:[r/LLMDevs discussion, 2025](https://www.reddit.com/r/LLMDevs/comments/1nofqco/what_are_the_best_platforms_for_ai_evaluations/))
- **Platform direction now runs through an acquirer:** Dynatrace announced plans to acquire Arize in August 2026. Dynatrace says that after the acquisition closes, Arize and Dynatrace will continue to operate independently, with no immediate changes to existing products, relationships, or commitments. But the longer-term picture is still unclear. The announcements do not explain whether or how Arize AX’s packaging and pricing will change after closing, or how Phoenix governance and roadmap decisions will work longer term. For multi-year agent platform decisions, ask Arize directly. (Sources: [Dynatrace press release](https://www.dynatrace.com/news/press-release/dynatrace-to-acquire-arize/) and [blog](https://www.dynatrace.com/news/blog/dynatrace-intends-to-acquire-arize/), August 2026)

## Why choose LangSmith over Arize?

Each limitation above maps to a capability we built into LangSmith. We give you opinionated mechanics for offline and online evals, with LLM-as-a-judge built in.

LangSmith evaluators are versioned prompts with pre-templated structures, making it clear how evaluators are configured and how variables are injected. Arize’s evaluators don’t come with pre-templated prompts, making it harder to get started and understand variable injection.

LangSmith's cloud platform ingests 500K–750K spans per minute in independent load tests, processes over 100M runs per day, and serves 30K+ monthly active tenants. Our server-side logic was rewritten in Go and re-architected for large payload sizes, including audio and video.

[SmithDB](https://www.langchain.com/blog/introducing-smithdb), our purpose-built database for agent observability, delivers industry-leading performance across every key observability workload — with P50 latencies of 92ms for trace tree loads, 400ms for full-text search, and 82ms for run filtering.

The Developer tier on LangSmith is free: one seat, 5,000 base traces/month, with production features and code evaluators included.

We designed LangSmith to cover the full application lifecycle without forcing you to stitch together separate tools: you trace and evaluate agents in one place, then deploy them with built-in persistence.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a24fb06ca105aad8dda3b2e_11.png)

## Turn production traces into improvements automatically

Most observability platforms stop at surfacing data. LangSmith goes a step further by turning that data into a repeatable improvement cycle we call the [Agent Development Lifecycle](https://www.langchain.com/blog/the-agent-development-lifecycle).

Production traces flow into [Insights](../langsmith/insights.md), which identifies usage patterns and failure modes. Those insights become datasets. The datasets power evals. The evals then guide the next round of changes.

LangSmith also removes friction from iteration. You can pull traces straight into the Playground to test and refine prompts. In Arize, you typically need to add a trace to a dataset before you can test with it, which slows the debug and iterate loop.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a24f65ea5fda1afab334705_Group%202147239596.png)

## Evaluate conversations as they happen, not after

Single-turn evals miss context that matters. Did the user express frustration across the conversation? Did the agent loop on the same tool call repeatedly?

LangSmith's thread-level evaluation measures the entire interaction as one unit, because that's how your users actually experience the agent. Phoenix's open-source evaluator library runs against traces you've already collected. However,[Arize AX can support online evals](https://arize.com/docs/ax/get-started/get-started-evaluations) that score LLM outputs in real time as traces are ingested, enabling immediate monitoring, dashboards, and threshold-based alerting in production.

LangSmith evaluators also self-improve through human corrections. When domain experts provide feedback, those corrections become few-shot examples that are first-class inputs to the evaluator, continuously improving scoring accuracy. Arize lacks self-improving evaluators entirely.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a24f68c9577a06c5396409e_Evaluation.png)

## Deploy stateful AI agents without a separate platform

AI agents are long-running and stateful by nature. A deep research agent runs for hours, pauses for human feedback, then resumes with full context. [LangSmith Deployment](https://www.langchain.com/langsmith-platform) has purpose-built infrastructure for these workloads: persistence and durable checkpointing, with LangSmith Studio for visual debugging. Arize does not position itself as a deployment solution, so teams using Arize typically pair it with separate hosting infrastructure.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a24f61770869dce2c9ccf9a_Group%202147239551.png)

## How LangSmith has helped frontier teams

> *"We can pull down LangSmith traces, see how they interact with the code being executed, and make changes informed by what's actually happening. There's a loose self-improving loop: make changes, execute a graph, see the trace, pull the trace back in." (*[*Harmonic Story*](https://www.langchain.com/blog/how-harmonic-rebuilt-scout-on-deep-agents-and-4xd-retention-with-langsmith)*)*

> *"As we embedded AI into individual products, it became clear that siloed, vertical-specific models couldn't scale. Rippling's data model spans thousands of tables across HR, IT, finance, and global ops — with overlapping entities and shared concepts that mean entirely different things depending on context. We needed an AI-native reasoning layer that could disambiguate and operate across that entire ontology, not just optimize for one domain." (*[*Rippling Story*](https://www.langchain.com/blog/how-rippling-went-ai-native-across-every-product-in-6-months-with-deep-agents-and-langsmith)*)*

## Switching from Arize to LangSmith

Moving from Arize doesn't require a rebuild, and if your team can navigate Arize, it can navigate LangSmith. The organizational UX structure (projects, traces, datasets, experiments) is nearly identical between the two platforms, so the learning curve is minimal. LangSmith is framework agnostic and works with [LangGraph](https://www.langchain.com/langgraph), the LangChain framework, Deep Agents and any other stack.

- **Tracing setup:** Add the `@traceable` wrapper to your existing code. Most teams finish instrumentation within a day.
- **Dataset migration:** Export your evaluation datasets and import them into LangSmith for continuity. LangSmith accepts CSV uploads directly through the UI or SDK.
- **Eval mechanics:** Recreate your evaluation logic using LangSmith's built-in offline and online evals, plus LLM-as-a-judge support.
- **Team onboarding:** [Annotation Queues](../langsmith/annotation-queues.md) let domain experts review traces immediately.
- **Timeline:** Most teams complete migration in under two weeks. Our team supports you through the process.

## When to use LangSmith vs. Arize

| LangSmith is a better fit when you: | Arize is a better fit when you: |
| --- | --- |
| Build stateful, multi-step AI agents that need deployment infrastructure | Monitor both generative AI and traditional ML/CV models on one platform |
| Want production traces to feed directly into evals and improvements | Prefer OpenTelemetry-native instrumentation as your observability standard |
| Need thread-level evaluation across full conversations | Need a free, self-hosted option. |
| Require CI/CD quality gates on agent behavior | Want business-facing dashboards accessible to non-technical stakeholders |
| Want a neutral platform for the full agent development lifecycle today | Already use Dynatrace and want AI evaluation alongside its application and infrastructure observability after the acquisition closes |

## Where LangSmith pulls ahead

### Multi-step AI agent debugging at enterprise scale

- **LangSmith renders the full execution tree for each trace.** You get X-ray vision into 50-step agent runs instead of linearized logs.
- **Automated feedback triggers surface issues in real time.** Your team can act on failures as they happen.

### Domain expert review without engineering bottlenecks

- **Annotation Queues** put traces in front of domain experts like clinicians, lawyers, analysts, and product managers for review without requiring code access.
- **Align Evaluators** aligns LLM-as-a-judge scoring with expert feedback through few-shot examples.

## FAQ

### Does LangSmith work if we don't use LangChain or LangGraph?

Yes: LangSmith is framework-agnostic and works with any LLM application or AI agent stack, including the LangChain framework, LangGraph, Deep Agents, or your own custom setup. Add the `@traceable` wrapper to get full tracing regardless of your orchestration framework.

### How long does it take to switch from Arize to LangSmith?

We typically see teams complete the transition to[LangSmith](https://www.langchain.com/langsmith-platform) in under two weeks by following a structured migration path. Day 1 is focused on technical instrumentation; you simply apply the `@traceable` wrapper to your functions across the LangChain framework, LangGraph, Deep Agents, or any other stack.

By the end of the first week, teams usually achieve evals parity by importing existing Arize datasets and mapping their evaluation mechanics to our built-in LLM-as-a-judge scorers. This timeline allows for a full week of parallel testing to validate your AI agent performance against historical benchmarks before the final production cutover.

### Will we lose historical data when switching?

You keep any datasets you export from Arize. LangSmith starts collecting new traces immediately after instrumentation, and historical Arize traces stay in your Arize account.

### What does LangSmith cost?

Plans start at $0/month on the Developer plan: one user seat and 5,000 base traces included.

The Plus plan is $39/seat/month with 10,000 base traces and one dev-sized deployment, which we’ve optimized for testing and low-concurrency workloads. For organizations requiring high-volume throughput and higher resource limits, we offer a tailored Enterprise tier. Enterprise pricing is custom. [See full pricing details.](https://www.langchain.com/pricing)

### Does Arize offer anything LangSmith doesn't?

Yes: Arize supports traditional ML and computer vision monitoring alongside generative AI. If your team monitors classical models and LLM agents on one platform, that's a big benefit of Arize.

Arize also offers Phoenix as a free, self-hosted source-available tool. It’s worth noting that Phoenix and Arize’s enterprise product (AX) have incompatible SDKs, so there is no seamless migration path from the free tool to the paid platform. Phoenix also lacks production-grade capabilities like online evals and monitoring. Teams who start on Phoenix expecting a smooth upgrade to AX will need to re-instrument. And if you already run Dynatrace for application monitoring, the pending acquisition may eventually make Arize a natural fit inside your existing observability stack.

### What does the Dynatrace acquisition mean if we're evaluating Arize?

Dynatrace announced a definitive agreement to acquire Arize on August 13, 2026. At the time of publishing, the deal is pending regulatory approval and has not closed, and both companies have said they will continue to operate independently after the acquisition closes. Dynatrace has stated that nothing changes immediately for existing customers, products, and commitments, and that it intends to support Phoenix and contribute to the continued stewardship of OpenInference.

What hasn't been published is how Arize AX will be packaged and priced within the Dynatrace platform after close, or how Phoenix governance and roadmap decisions will work longer term. If you're committing to a platform for the next several years, it's worth asking Arize for specifics on post-close packaging, pricing, and open-source governance.

LangSmith is a standalone agent engineering platform, built and roadmapped by the same team behind LangGraph, the LangChain framework, and Deep Agents.

### Arize has an AI assistant, Alyx. How does LangSmith compare?

Arize’s Alyx is a strong conversational interface for onboarding and rapid prototyping. It can generate synthetic traces, test prompts, and create evaluators through chat.

LangSmith takes a different approach, with two complementary AI capabilities. [Insights](../langsmith/insights.md) produces structured, repeatable analysis across large volumes of production traces, and you can run it via the UI or SDK for systematic monitoring. [Chat](../langsmith/chat.md) supports in-platform assistance for real-time trace analysis and debugging.

The core difference is intent. Alyx is designed for interactive exploration. LangSmith’s AI tools are designed to support production decisions in a consistent, repeatable way.

### Can we use LangSmith for evaluation only, without switching our tracing?

You can: LangSmith's evaluation mechanics work independently. Teams often start with evals and expand to tracing and deployment over time.

## See what full-lifecycle agent engineering looks like

LangSmith gives you tracing and evals with built-in deployment and it works with the LangChain framework, LangGraph, Deep Agents, as well as any other agent stack.

> [Get started today for free](https://smith.langchain.com/) or[get a demo of LangSmith's agent engineering platform](https://www.langchain.com/contact-sales).
