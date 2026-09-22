---
title: "9 LLM Observability Tools for Production AI Agents"
description: "Compare the best LLM observability tools for production AI agents, with practical tradeoffs for traces, evals, debugging, cost, and review workflows."
source: "https://www.langchain.com/resources/llm-observability-tools"
category: "resources"
published: "2026-08-16"
author: "LangChain"
tags: [resources, llm-observability-tools]
---

# 9 LLM Observability Tools for Production AI Agents

Error logs tell you when something goes wrong. AI agents are trickier because a run can finish successfully while returning bad results. The model may generate incorrect information, call the wrong tool, drift from policy, or produce an answer that a domain expert would reject.

Once traces are in place, the decision shifts to what happens after a bad run. Most teams can answer "what went wrong" and stall on who reviews it, how it becomes test coverage, and how it turns into a production change.

We built [LangSmith](https://www.langchain.com/langsmith-platform) for teams that need observability to connect directly to the [Agent Development Lifecycle (ADLC)](https://www.langchain.com/blog/the-agent-development-lifecycle) so they can build, test, deploy, monitor, and improve their agentic applications. The right choice depends on the team's operating model. A platform team already living in Datadog, an infrastructure team standardizing on gateways, and an AI product team running weekly eval experiments need different solutions.

## Summary

- Choose LangSmith if you need framework-agnostic agent observability plus evals, monitoring, and annotation queues, with workflows to [automatically categorize behavior patterns](https://www.langchain.com/blog/insights-agent-multiturn-evals-langsmith) and [cluster recurring failures](https://www.langchain.com/blog/introducing-langsmith-engine) so you can find root causes and ship fixes that prevent regressions. LangSmith is **not** limited to those in the LangChain/LangGraph ecosystem.
- Choose Braintrust if your team organizes AI product quality around datasets, experiments, scores, and eval runs
- Choose Datadog Agent Observability if you already run production operations in Datadog and want AI telemetry correlated with APM, logs, infrastructure, security, and cost
- Choose Langfuse if you want a self-hostable LLM engineering platform with traces, prompts, datasets, and evals

**Main takeaway:** the best LLM observability tool matches the workflow your team will actually run after production behavior starts surprising you.

## The best LLM observability tools at a glance

| Tool | Type | Pricing | Best for |
| --- | --- | --- | --- |
| LangSmith | Framework-agnostic agent engineering platform | Developer $0/seat/mo; Plus $39/seat/mo; Enterprise custom | Production AI agent debugging, evals, review, monitoring, and automatic fixes |
| Braintrust | AI evals platform | Starter $0; Pro listed at $249/month; Enterprise custom | Eval-first teams |
| Datadog Agent Observability | APM-native AI observability | Free tier; Pro starts at $160/month annually for the first 100,000 LLM spans | AI telemetry inside an existing Datadog stack, if you do not want a purpose-built agent observability tool |
| Langfuse | Open source evals and observability | Hobby $0; Core $29/month; Pro $199/month; Enterprise $2,499/month | Self-hostable traces, prompts, datasets, and evals |
| Helicone | LLM observability and gateway | Free; Pro $79/month; Team $799/month | API-level visibility, cost tracking, caching, and routing |
| Portkey | AI gateway with observability | Developer (free); Production $49/month; Enterprise custom | Provider routing, fallbacks, guardrails, and request logs |
| Arize Phoenix and AX | AI observability and evaluation platform | AX Free; AX Pro $50/month; AX Enterprise custom | Local AI observability with a production platform path |
| TruLens | Evaluation and instrumentation library | Community library; commercial options through Snowflake | Python-first RAG evals and local experimentation |
| Lunary | LLM monitoring and prompt platform | Free; Team $20/user/month; Enterprise custom | Lightweight traces, feedback, dashboards, and evals |

## How to evaluate if you need an LLM observability tool

If you're still testing one prompt against a handful of examples, start smaller. A notebook, playground, simple dataset, and disciplined error analysis can teach you more than a large platform rollout in some cases.

The need changes when the application becomes multi-step because you’re no longer evaluating one request at a time. Once your system has retrieval, tool calls, model routing, retries, memory, human feedback, or multiple teams changing prompts and code, LLM observability starts paying for itself.

Trace visibility is only helpful if the team also has a process for deciding which failures are worth debugging, who reviews them, and how regressions stay fixed. LLM observability is worth the additional overhead when that process has to hold across many steps, many releases, and many people changing the system at once, because it gives everyone the same view of what the agent did and turns real production failures into eval coverage the team can rerun before the next deploy.

## What to look for in an LLM observability tool

### Trace capture vs. trace actionability

Most tools can show the basic run record. You can usually see the prompt and response, latency, token counts, and nested calls. The more useful question when evaluating a platform for LLM observability is whether the tool helps you act on that data.

For AI agents, actionability starts with the full execution path. The tool should also group similar failures and show where behavior changed. From there, the team needs a way to turn the trace into engineering work. A trace that answers “what happened?” without showing the team how to fix it leaves the hardest work unresolved.

### Production traces to eval datasets

Production traces are one of the best sources of eval examples because they contain the failures your users actually hit. Whatever tool you pick should make it easy to turn traces into datasets and compare results across model or prompt changes. It should also support offline evals before deployment and online evals on live traffic.

Logging starts to break down when production issues have no path into test coverage. A production issue should become an eval case that the team can run again before the next release.

### Human review mechanics

Many AI agent failures are judgment failures. A clinician, lawyer, analyst, product manager, or support lead may be better positioned than an engineer to decide whether the answer was useful, risky, or incomplete.

Good LLM observability tools give those reviewers a structured way to inspect examples, leave feedback, and route that judgment back into [evals](https://www.langchain.com/resources/llm-evals). If the feedback loop lives outside the tool, it usually ends up in a spreadsheet and never makes it back into the evals that it was meant to improve.

### Cost attribution grain

Request-level cost is a good starting metric, but it stops at the individual call. An engineering team eventually needs to know whether a customer workflow, product feature, agent path, or user segment is worth the tokens it burns.

[LLM gateways](https://www.langchain.com/blog/introducing-llm-gateway) can give you feature-level cost attribution, but only if you tag requests with feature, user/account, and workflow metadata. Without that, cost dashboards show spend totals, not which features are worth what they cost.

### Operating model

The tool's architecture matters as much as its features and capabilities.

- SDK/platform tools can see deeper application context, but require instrumentation discipline
- Gateways and proxies are fast to adopt, but only see what passes through the request path
- APM-native tools fit existing operations, but may not be built around evals and review
- Notebook-friendly local tools are useful for experimentation, but may lack a production path
- Self-hosted tools improve control, but shift maintenance to your team

## How we evaluated these tools

We reviewed official product pages, docs, pricing pages, GitHub repositories (where relevant), and public engineering discussions (where available). For each tool, we looked at who reviews a bad run, how that run becomes an eval, where fix ownership sits, and what work the team still has to do outside the tool.

## LangSmith

### What is LangSmith?

**Quick facts**

- Type: Agent engineering platform
- Company: LangChain
- Pricing: Developer $0/seat/mo; Plus $39/seat/mo; Enterprise custom; Engine priced as an add-on by usage
- Website: [smith.langchain.com](https://smith.langchain.com)

[LangSmith](https://www.langchain.com/langsmith-platform) is our framework-agnostic observability and evaluation platform for LLM applications and AI agents. It works with [Deep Agents](https://www.langchain.com/deep-agents),[LangGraph](https://www.langchain.com/langgraph), and the LangChain framework, as well as other frameworks or custom code. LangSmith is **not** limited to those in the LangChain/LangGraph ecosystem.

LangSmith is the best choice when observability needs to connect directly to the [agent improvement loop](https://www.langchain.com/conceptual-guides/traces-start-agent-improvement-loop). Traces can become datasets, offline evals, online evals, annotation queues, monitoring views, and production debugging work.

[Engine](https://www.langchain.com/langsmith/engine) is the clearest reason to choose LangSmith when your team needs observability to turn into action. It analyzes production traces, clusters failure patterns, prioritizes issues, suggests or opens targeted fixes, and drafts evals so the same regression does not recur. [SmithDB](https://www.langchain.com/blog/introducing-smithdb) is the purpose-built database underneath LangSmith Observability. It is built for long, nested agent traces and is 12-15x faster on core LangSmith workloads depending on the operation, with P50 trace tree loads around 92ms and P50 single run loads around 71ms.

[LangSmith Evaluations](../langsmith/evaluation.md) are a core part of that loop. Teams can run evals over known datasets before shipping and score production traffic online. They can use [LLM-as-a-judge evals](https://www.langchain.com/resources/llm-as-a-judge) where judgment is needed, then use Code/functional evaluators where exact checks are possible.

### Who should use LangSmith?

- Engineering teams building production AI agents that need traces, evals, monitoring, review, and fixes in one workflow
- Teams where clinicians, lawyers, analysts, product managers, or QA reviewers need to inspect outputs through annotation queues
- Organizations that want observability tied to the full [ADLC](https://www.langchain.com/blog/the-agent-development-lifecycle) instead of disparate dashboards

### Standout features

- Engine for failure clustering, issue prioritization, fix suggestions, and eval generation
- LangSmith Evaluations for datasets, offline evals, online evals, LLM-as-a-judge evals, and Code/functional evaluators
- Annotation queues for routing examples to human reviewers
- [Insights](../langsmith/insights.md) for finding usage and behavior patterns
- LangSmith Chat for inspecting, testing, and debugging agent behavior
- SmithDB for AI-specific trace workloads
- [LLM Gateway](../langsmith/llm-gateway.md) for provider-layer spend controls, PII protection, and trace continuity

### Pros and cons

| Pros | Cons |
| --- | --- |
| Connects traces, evals, review, monitoring, and fixes inside one agent engineering workflow. Easy to use and strong UX | Enterprise controls, longer retention, and Engine usage need budget planning |
| Integrates with LangGraph, Deep Agents, the LangChain framework, any other framework, and custom code. LangSmith is not limited to those in the LangChain/LangGraph ecosystem. | If you only need request logs, cost tracking, or provider routing, you may be able to use more basic solutions |
| Purpose-built for AI-specific telemetry, including long traces, nested tool calls, and conversation state | Won't replace Datadog or another APM for day-to-day incident infrastructure triage |

### FAQ

#### Does LangSmith only work with LangChain applications?

No. It's framework agnostic. While [LangSmith](https://www.langchain.com/langsmith-platform) works with the LangChain framework, LangGraph, and Deep Agents, it also works with any other framework, or custom code. LangSmith is **not** limited to those in the LangChain/LangGraph ecosystem.

#### How does LangSmith support evals?

[LangSmith Evaluations](https://www.langchain.com/langsmith/evaluation) supports dataset-based offline evals, online evals on production traffic, LLM-as-a-judge evals, Code/functional evaluators, and human review through annotation queues. Evals sit next to traces, so production failures can become regression coverage.

#### How do Engine and SmithDB work with LangSmith?

Engine helps teams move from trace inspection to action by identifying recurring production issues, prioritizing them, suggesting fixes, and creating evals. SmithDB is the trace data layer built for [AI observability](https://www.langchain.com/resources/ai-observability) workloads.

#### Who shouldn't start with LangSmith?

If you only need a provider proxy, simple request logs, or cost dashboards for a prototype, a gateway-first tool may be a better pick. [LangSmith](https://www.langchain.com/langsmith-platform) becomes more valuable when traces need to feed evals, review, monitoring, engineering fixes, and provider-layer governance.

## Braintrust

### What is Braintrust?

**Quick facts**

- Type: AI evals platform
- Company: Braintrust
- Pricing: Starter $0; Pro listed at $249/month; Enterprise custom
- Website: [braintrust.dev](https://www.braintrust.dev)

Braintrust is an AI-native platform primarily for evals, experiments, and online scoring. It belongs in this guide because many teams now start their AI engineering work with evals rather than logs.

Braintrust starts from the eval loop. Datasets, experiments, model and prompt comparisons, output scoring, and regression review all live in one workspace. While a team can build a simple eval runner in-house, maintaining that history once multiple people are changing the product can become a burden with homegrown tooling.

Braintrust is less APM-native than Datadog and less ADLC-oriented than [LangSmith](https://www.langchain.com/langsmith-platform). It offers a narrower platform than LangSmith as it does not have deployment, an LLM gateway, or advanced observability. Its best fit is a team that already thinks in datasets, scores, and product-quality experiments.

### Who should use Braintrust?

- AI product teams that run frequent eval experiments across prompts, models, and datasets
- Teams that want one workspace for traces, experiments, scoring, prompt work, and human review
- Organizations that would otherwise build internal eval infrastructure around datasets and pass/fail scoring

### Standout features

- Dataset and experiment workflows for comparing AI application changes
- Tracing connected to eval runs and product-quality scoring
- Online scoring for production behavior
- Prompt management and human review
- Collaboration features for engineering and product teams

### Pros and cons

| Pros | Cons |
| --- | --- |
| Good fit for eval-first teams | Less natural for teams who want to prioritize advanced agent observability |
| Helps avoid building internal dataset, score, and experiment plumbing | Weaker if you need the full loop from production failures to prioritized fixes and regression coverage |
| Good bridge between engineering, product, and review workflows | Full governance, retention, and scale requirements can push teams toward Enterprise |

### FAQ

#### Is Braintrust an observability tool or an evals tool?

It's both, but evals are the main workflow. If your team starts agent quality discussions with datasets, experiments, and scores, Braintrust is a natural fit.

#### Is Braintrust worth buying if evals are buildable in-house?

That depends on whether eval infrastructure is strategic for your team. Many teams can build a simple dataset runner. Fewer want to maintain experiment history, review workflows, scoring, prompt comparisons, and production feedback loops as the product grows.

#### When should we choose Braintrust over LangSmith?

Choose Braintrust when your team wants an eval-first workspace. Choose [LangSmith](https://www.langchain.com/langsmith-platform) when you want evals tightly connected to agent observability, agent traces, monitoring, annotation queues, Engine-driven issue prioritization, and the ADLC.

## Datadog Agent Observability

### What is Datadog Agent Observability?

**Quick facts**

- Type: APM-native AI observability
- Company: Datadog
- Pricing: Free tier with 40,000 LLM spans/month; Pro starts at $160/month annually, $200/month month-to-month, or $240/month on-demand for the first 100,000 LLM spans
- Website: [datadoghq.com/products/ai/agent-observability](https://www.datadoghq.com/products/ai/agent-observability)

Datadog Agent Observability extends Datadog's existing production monitoring platform into AI agent telemetry. Its advantage is correlation. AI spans sit alongside APM traces, infrastructure metrics, and real user monitoring in the Datadog platform.

Datadog Agent Observability is a fit when the platform or SRE team already owns production operations in Datadog’s APM platform. In that world, the AI agent is another production service. Model latency, errors, and cost sit next to the rest of the application's telemetry.

The tradeoff is that Datadog focuses on production operations rather than AI product-quality workflows. If your team needs eval dataset curation, annotation queues, and trace-to-fix mechanics, Datadog may serve as the production operations home base for APM, logs, alerting, and incident response, while a dedicated LLM observability tool handles evals, human review, and regression coverage.

### Who should use Datadog Agent Observability?

- Teams already standardized on Datadog for production operations
- Platform and SRE teams that need AI telemetry next to APM, logs, infrastructure, and incidents
- Organizations that want span-based billing and Datadog-native dashboards for AI services

### Standout features

- AI spans correlated with existing Datadog telemetry
- Connection to APM, logs, infrastructure, error tracking, real user monitoring, security, and cost signals
- Production dashboards and alerting inside Datadog
- Public span-based pricing for the Pro plan

### Pros and cons

| Pros | Cons |
| --- | --- |
| Familiar interface for Datadog-standardized teams | Less natural if evals, annotation queues, and AI product review are a core workflow. It is not purpose built for agent observability and evals |
| Strong correlation between AI spans and broader production telemetry | Dedicated AI engineering teams may still need deeper trace-to-eval mechanics |
| Clear public span-based pricing | Teams that do not already use Datadog rarely adopt it solely for LLM observability |

### FAQ

#### How does Datadog compare to dedicated LLM observability tools?

Datadog makes the most sense when AI telemetry needs to live inside broader production observability. Dedicated AI engineering tools are usually a better fit when the core workflow is evals, review, and product-quality improvement.

#### Who is the buyer for Datadog Agent Observability?

Usually the buyer is the platform, SRE, or infrastructure leader who already trusts Datadog for production operations. They're trying to bring AI spans into the monitoring system the team already uses.

#### Do you need a separate eval platform if you go with Datadog Agent Observability?

Possibly. Datadog can help teams understand operational behavior. Teams that need dataset-driven evals, human review queues, and AI quality workflows may still use a dedicated AI observability or eval platform.

## Langfuse

### What is Langfuse?

**Quick facts**

- Type: Open source agent evals and observability
- Company: Langfuse, acquired by ClickHouse (future is uncertain)
- Pricing: Hobby $0; Core $29/month; Pro $199/month; Enterprise $2,499/month
- Website: [langfuse.com](https://langfuse.com)

Langfuse is an open source agent evals & observability platform for tracing, prompt management, datasets, experiments, and evals. It's one of the most viable options for teams that want a self-hostable observability and eval workspace.

Langfuse is most appealing when control matters more than operational simplicity. Teams can run it themselves and keep data closer to their infrastructure while still getting traces, prompts, datasets, experiments, and evals. The diligence question is whether your team wants to own the operational layer underneath that surface area.

Self-hosting an AI observability platform means owning storage, ingestion, ClickHouse behavior, upgrades, OpenTelemetry (aka OTel) ingestion behavior, and edge cases around large traces or media. That may be a good tradeoff for data-control requirements, but it's a compromise.

### Who should use Langfuse?

- Teams that want a self-hostable agent evals & observability platform
- Organizations that need traces, prompts, datasets, experiments, and evals in one workspace
- Engineering teams comfortable owning the infrastructure behind their observability stack

### Standout features

- Tracing for LLM applications and AI agents
- Prompt management, datasets, experiments, and evals
- Self-hosting for teams with data-control requirements
- OpenTelemetry-compatible ingestion paths

### Pros and cons

| Pros | Cons |
| --- | --- |
| Strong self-hostable option with broad LLM engineering coverage | Self-hosting shifts storage, ingestion, upgrades, and reliability work to your team |
| Good fit for teams that want control over observability data | Recent acquisition by ClickHouse creates a roadmap question buyers should consider |
| Combines traces, prompts, datasets, experiments, and evals | Teams still need to define how traces become root-cause analysis, issue ownership, and fixes |

### FAQ

#### When is self-hosting Langfuse worth it?

Self-hosting is worth considering when data residency, internal controls, or infrastructure ownership matter more than operational simplicity. If your team doesn't want to manage storage, upgrades, and ingestion, the maintenance burden may outweigh the control.

#### Does Langfuse solve root-cause analysis automatically?

Langfuse gives teams trace data, evals, prompts, datasets, and experiments. Teams still need a process for clustering failures, assigning ownership, and turning recurring issues into tests or fixes.

#### How should buyers think about the ClickHouse acquisition?

ClickHouse may strengthen Langfuse's data infrastructure over time. Buyers should still ask about product investment, support, hosting options, and roadmap clarity because ownership changes can affect long-term planning.

## Helicone

### What is Helicone?

**Quick facts**

- Type: LLM observability and gateway
- Company: Helicone, now part of Mintlify (future is uncertain)
- Pricing: Free; Pro $79/month; Team $799/month
- Website: [helicone.ai](https://www.helicone.ai)

Helicone is a gateway-style LLM observability tool. It sits in the request path, so teams can add request logging, latency tracking, cost tracking, caching, rate limits, routing, and feedback with a relatively fast setup.

If the main thing you need to observe is provider traffic, a gateway can be easier than adding tracing and metadata throughout your app. Helicone is especially useful when teams care about API-level visibility, spend, cache behavior, and provider reliability.

Gateway-level observability sees what passes through the gateway, but it won't automatically understand your full agent state, product feature, customer workflow, or review loop unless you pass that metadata deliberately.

### Who should use Helicone?

- Teams that want fast API-level visibility into LLM calls
- Organizations focused on cost tracking, caching, routing, and provider behavior
- Developers who prefer proxy or gateway instrumentation over deeper SDK instrumentation

### Standout features

- Request logging for LLM provider calls
- Cost, latency, and usage analytics
- Caching, rate limits, routing, and feedback
- Gateway-based setup path
- Useful dashboards for provider-level behavior

### Pros and cons

| Pros | Cons |
| --- | --- |
| Fast path to request-level observability | Less visibility into full agent state unless metadata is passed through carefully |
| Strong fit for cost, latency, caching, and provider analytics | Feature-level ROI requires disciplined tagging |
| Good gateway option for teams that want minimal application changes | Mintlify acquisition and [maintenance-mode](https://helicone.ai/blog/joining-mintlify#:~:text=foreseeable%20future%20in-,maintenance%20mode,-.%20This%20means%20security) language deserve roadmap diligence |

### FAQ

#### Can Helicone show feature-level cost?

It can help if your team tags requests with feature, user, customer, and workflow metadata. Without those tags, gateway analytics usually show request-level spend rather than whether a product feature is economically viable.

#### When is a gateway enough for observability?

A gateway can be enough when the main questions are provider cost, latency, caching, routing, and usage. If the question is why an agent chose a tool, ignored context, or failed a policy-specific judgment, you usually need deeper tracing and eval workflows.

#### How should buyers evaluate Helicone after the Mintlify acquisition?

Ask about roadmap, support, managed hosting, self-hosting, security updates, and new feature investment. The product can still be useful, but acquisition context matters for long-term infrastructure choices.

## Portkey

### What is Portkey?

**Quick facts**

- Type: AI gateway with observability
- Company: Portkey
- Pricing: Developer (free) with 10,000 recorded logs; Production $49/month; Enterprise custom
- Website: [portkey.ai](https://portkey.ai)

Portkey is primarily an AI gateway. It handles provider routing, fallbacks, retries, load balancing, caching, guardrails, governance, prompt management, and request logs.

Portkey is a better fit when your hardest problem is managing request routing, provider selection, and delivery reliability. Teams usually adopt it to stop maintaining their own provider-routing code.

Observability is still important, but it's attached to the gateway model. Portkey can show what crossed the gateway and how routing behaved. It won't replace a full eval workflow unless the team layers datasets, scoring, and review on top.

### Who should use Portkey?

- Teams that need routing, fallbacks, retries, guardrails, and budget controls
- Organizations managing multiple providers or model endpoints
- Platform teams that want request logs and governance inside the AI gateway layer

### Standout features

- Provider routing, fallbacks, retries, and load balancing
- Request logs and analytics
- Guardrails, governance, budget controls, and RBAC
- Caching and prompt management
- Gateway patterns for centralizing AI traffic

### Pros and cons

| Pros | Cons |
| --- | --- |
| Strong fit for provider routing and traffic governance | Gateway observability provides less application context than full agent trace analysis |
| Helps reduce custom fallback, retry, and routing code | Eval datasets, human review, and regression loops need additional process |
| Useful when teams manage multiple providers | Weak fit if your main pain is product quality rather than provider reliability and routing |

### FAQ

#### Is Portkey an observability platform or a gateway?

Portkey is a gateway first. Observability is part of the gateway workflow, but the main value is routing, fallbacks, guardrails, governance, caching, and request control.

#### When should we choose Portkey over Helicone?

Choose Portkey when provider routing, governance, fallbacks, and policy controls are the main problem. Choose Helicone when fast request-level analytics and cost visibility are the main problem.

#### Can Portkey replace an eval platform?

Usually no. Portkey can help control and observe traffic, but eval datasets, human review, and regression checks still need a dedicated workflow.

## Arize Phoenix and AX

### What is Arize Phoenix?

**Quick facts**

- Type: AI observability and evaluation platform
- Company: Arize AI, acquired by Dynatrace (future is uncertain)
- Pricing: AX Free; AX Pro $50/month; AX Enterprise custom
- Website: [arize.com/phoenix](https://arize.com/phoenix)

Arize Phoenix is an AI observability and evaluation tool with a strong local and notebook-friendly workflow. AX is Arize's managed platform for teams that need a hosted production system.

Phoenix works well for ML engineers who want to inspect traces and run evals close to notebooks or local development. Its OpenTelemetry foundation also works well for teams that want standards-based instrumentation and export paths.

The practical question is where local experimentation ends and production operations begin, because Phoenix and AX are priced, retained, and governed differently past that point.

### Who should use Arize Phoenix?

- ML engineers who want local or notebook-friendly AI observability
- Teams that care about OpenTelemetry-based tracing and instrumentation
- Organizations that want a path from local evals into a managed observability platform

### Standout features

- Local and notebook-friendly tracing workflows
- OpenTelemetry-based instrumentation
- Evals, datasets, and prompt experimentation
- Phoenix local workflow with AX managed platform path
- Useful RAG and agent observability patterns

### Pros and cons

| Pros | Cons |
| --- | --- |
| Strong local and notebook-friendly workflow | Local workflows still need a production operating model |
| OpenTelemetry foundation fits standards-oriented teams | Buyers need to understand the Phoenix vs. AX split. Future of company is also uncertain with Dynatrace acquisition |
| Good fit for ML experimentation and evals | Self-serve span limits and retention may be low for production teams |

### FAQ

#### What is the difference between Phoenix and AX?

Phoenix is the local observability and eval tool. AX is Arize's managed platform. Buyers should evaluate Phoenix for local workflows and AX for hosted production needs.

#### How does OpenTelemetry affect the Phoenix to AX decision?

Arize built Phoenix on OpenTelemetry and maintains OpenInference, the span convention for LLM and agent traces. The instrumentation you write for local Phoenix work is the same instrumentation AX ingests, so moving to the hosted platform is a configuration change rather than a re-instrumentation project. The same spans can also go to another OTel backend if you switch tools later.

#### What is Phoenix less suited for?

Phoenix is less suited as a standalone answer for teams that need a managed production workflow, long retention, broad governance, and structured cross-functional review from day one.

## TruLens

### What is TruLens?

**Quick facts**

- Type: Evaluation and instrumentation library
- Company: TruEra, acquired by Snowflake
- Pricing: Community library; commercial options through Snowflake
- Website: [trulens.org](https://www.trulens.org)

TruLens is best understood as an evaluation and instrumentation library, especially for RAG systems. It's known for the RAG Triad, which checks context relevance, answer relevance, and groundedness.

TruLens is useful when a team wants to score and inspect AI application behavior in a local Python environment before adopting a managed observability platform. It fits notebooks, experiments, and teams that want to think critically about retrieval quality.

TruLens provides evaluation and instrumentation rather than a complete production observability workflow. Teams still need to assemble collaboration, governance, monitoring, human review, and incident processes around it.

### Who should use TruLens?

- Python-first teams evaluating RAG quality
- ML engineers working in notebooks or experiment pipelines
- Teams that want an evaluation library before adopting a managed platform

### Standout features

- RAG Triad for context relevance, answer relevance, and groundedness
- Python-first instrumentation and evaluation workflows
- Useful fit for local experiments and notebooks
- Library-first path
- Snowflake integration

### Pros and cons

| Pros | Cons |
| --- | --- |
| Strong vocabulary for RAG evaluation | Not a complete LLM observability platform by itself |
| Good fit for Python and notebook experimentation | Teams must build more of the review, governance, and monitoring workflow |
| Useful before a team needs a managed platform | Less visible community chatter than some newer AI observability platforms |

### FAQ

#### What is the RAG Triad?

The RAG Triad checks context relevance and answer relevance. It also tests whether the answer is grounded in the provided context.

#### When is a library enough?

A library can be enough when the team is still experimenting, building RAG evals, or working inside notebooks. A managed platform becomes more useful when many people need to review, monitor, compare, and act on production behavior.

#### How does Snowflake ownership affect the decision?

Snowflake gives TruLens a broader enterprise path. Buyers should still evaluate whether they want a library-style workflow or a standalone LLM observability platform.

## Lunary

### What is Lunary?

**Quick facts**

- Type: LLM monitoring and prompt platform
- Company: Lunary
- Pricing: Free tier with 10,000 events; Team $20/user/month with 50,000 events; Enterprise custom
- Website: [lunary.ai](https://lunary.ai)

Lunary is a lightweight platform for LLM monitoring, prompt management, traces, dashboards, user feedback, datasets, evals, and human review. It's the kind of tool a small team might try when they want some structure without a large platform.

The product covers the expected LLM observability basics, and the pricing can make sense for teams that are still early in production.

Before making Lunary a core workflow, buyers should validate production references, retention, event volume, support, and how the team handles larger traces or review-heavy use cases.

### Who should use Lunary?

- Small teams that want lightweight LLM monitoring and prompt workflows
- Teams that need traces, feedback, dashboards, datasets, and evals without a heavier rollout
- Startups that want a low-friction starting point before committing to a larger observability stack

### Standout features

- Traces, monitoring, dashboards, and feedback
- Prompt management and dataset workflows
- Evals and human review
- Free and Team tiers for smaller teams
- Self-hosting option

### Pros and cons

| Pros | Cons |
| --- | --- |
| Lightweight entry point for LLM observability | Less visible community chatter than other tools on this list |
| Combines monitoring, prompts, feedback, datasets, and evals | Event volume, retention, and support should be checked before production rollout |
| Accessible pricing for smaller teams | May be outgrown by teams needing deeper ADLC, APM, or gateway workflows |

### FAQ

#### When is Lunary enough?

Lunary can be enough when a small team needs traces, prompts, feedback, dashboards, and basic eval workflows without a larger platform.

#### When does a team need more than Lunary?

Evaluate additional options when you need deeper trace analysis, longer retention, advanced governance, annotation at scale, or a tighter loop between production failures and the engineers who fix them.

#### How should buyers evaluate Lunary?

Check event volume, retention, self-hosting requirements, support, team permissions, security controls, and references from teams running production traffic similar to yours.

## Frequently asked questions about LLM observability tools

### What is the difference between LLM monitoring, observability, and evals?

Monitoring tells you whether expected metrics changed across latency, errors, cost, token volume, and user feedback. Observability helps explain why behavior changed by exposing traces, inputs, outputs, tool calls, retrieval context, and metadata. Evals test whether the system behaves well against known examples or live traffic.

For production AI agents, the three should connect. A monitor flags an issue, observability explains the run, and evals keep the issue from recurring.

### When is a gateway enough for LLM observability?

A gateway can be enough when your main questions are request volume, provider latency, cost, routing, retries, caching, rate limits, and fallback behavior.

Understanding agent state, tool trajectories, retrieval quality, human review, or regression coverage requires deeper application context and eval workflows than a gateway provides.

### What metadata should we tag before comparing tools?

At minimum, tag environment, user or account, feature, agent version, prompt version, model, route, workflow, and experiment. If cost tracking is important, tag the business unit or product surface that owns the spend.

Without that metadata, most observability tools can show traces, but they can't answer which product workflow is failing or whether a feature is worth its token cost.

### How do production traces become eval coverage?

The best pattern is to review real failures and select representative examples. Once the team labels expected behavior and adds those examples to a dataset, the same cases can run before future releases. Some failures also need online evals over live traffic because they depend on changing context.

Ownership is what ties this together: every trace should have a clear path into a dataset, an eval, a fix, and a regression check.

### Should we choose one tool or combine multiple?

Many teams combine tools because the operating models differ. Datadog may remain the production operations layer, while LangSmith or Braintrust handles evals and AI product quality. A gateway like Portkey or Helicone may handle routing and spend while a deeper observability platform handles traces and review.

If multiple tools are involved, decide where production failures are triaged and where eval datasets live. One team also needs to own the final source of truth for quality.

## Build better AI agents with LangSmith

Most tools in this guide can show a trace. The harder question is whether that trace changes what ships next.

We built [LangSmith](https://www.langchain.com/langsmith-platform) for teams that need that loop to stay inside the way they build AI agents. Traces can become datasets, offline evals, online evals, annotation queues, Insights Agent, LangSmith Chat, and the SmithDB-backed trace layer that supports the ADLC.

[LangSmith](https://www.langchain.com/langsmith-platform) works with the LangChain framework, LangGraph, Deep Agents, any other framework, or custom code. LangSmith is **not** limited to those in the LangChain/LangGraph ecosystem.

If your current observability stops at "here is the trace," LangSmith gives the team a path from production behavior to prioritized issues, targeted fixes, datasets, evals, human feedback, and regression coverage.

> [Get a demo of LangSmith](https://www.langchain.com/contact-sales)

‍
