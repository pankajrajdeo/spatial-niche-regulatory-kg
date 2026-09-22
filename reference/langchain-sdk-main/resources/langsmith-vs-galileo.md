---
title: "LangSmith vs. Galileo: which feedback loop fits your stack?"
description: "Key takeaways"
source: "https://www.langchain.com/resources/langsmith-vs-galileo"
category: "resources"
author: "LangChain"
tags: [resources, langsmith-vs-galileo]
---

# LangSmith vs. Galileo: which feedback loop fits your stack?

**Key takeaways**

- LangSmith is a framework agnostic platform that helps teams turn real production failures into tests for the next release. Galileo focuses on checking and controlling agent behavior while the agent is running.
- Both platforms support LangChain, LangGraph, Deep Agents, and non-LangChain stacks through direct integrations and OpenTelemetry. LangSmith emphasizes low-friction tracing with its `traceable` decorator, while Galileo offers broad OTel-based coverage and Agent Graph for visual debugging, though parts of its native tracing path remain in beta.
- Before choosing, run a representative production workflow through both platforms. Compare how easily your team can instrument it, diagnose a failure, and turn the result into either a regression test or a runtime control.

Since [LangSmith](https://www.langchain.com/langsmith-platform) and [Galileo](https://galileo.ai/) both offer tracing, evaluations, and dashboards, their feature lists can look similar. The more useful question is what happens after an agent makes a mistake in production.

Do you want to collect that failure, turn it into a test, and prevent it from recurring in the next release? Or do you need to evaluate and control the agent while it is running? LangSmith is built around the first workflow. Galileo places more emphasis on the second.

When deciding between LangSmith and Galileo, choose based on four factors: how each platform traces multi-step agents, evaluates performance, turns production failures into improvements, and fits your existing stack.

## Architectural differences between LangSmith and Galileo

When an agent gives a bad answer, both platforms capture a trace that lets teams track the steps that led to it. LangSmith is designed to turn that failure into a test before the next release, while Galileo is designed to assess or constrain the agent as it runs.

That shared trace is where the comparison starts. The platforms differ in what they turn it into. LangSmith can send selected production traces to datasets and review queues, where teams use them to build regression tests for the next release. Galileo can score traces with prebuilt or team-configured evaluators, then use [Agent Control](https://galileo.ai/blog/announcing-agent-control) to run checks while an agent is live.

The practical difference is how much of that workflow each platform packages for you. LangSmith includes datasets, evaluators, prompt management, annotation queues, automations, and deployment alongside tracing. Its rules can route selected traces to a dataset, review queue, or webhook without custom scripting. Galileo does not currently offer the same rule-based routing, so teams that want a similar production-to-test feedback loop need to assemble it with custom SDK code.

## Multi-step agent tracing

When an agent takes 200 steps over two minutes and returns a wrong answer, teams need to inspect the full sequence of LLM decisions, tool calls, and handoffs that produced it. Production traces provide that end-to-end record, making agent observability a distinct discipline. Both platforms can capture the multi-step traces teams need to investigate these failures. The comparison turns on how each one captures, presents, and helps teams act on that data.

LangSmith, our framework-agnostic observability platform, addresses that surface through three primitives:

- **Run:** a single LLM call or tool invocation.
- **Trace:** a full agent turn that strings together hundreds of nested Runs.
- **Thread:** a multi-turn conversation that strings Traces together.

Galileo offers a comparable view through Agent Graph, which maps a multi-agent workflow visually. Teams can select each step to inspect the details from that part of the run. Agent Graph is a strength for teams that want to inspect a multi-agent workflow visually. Both platforms can render multi-step traces, but their instrumentation requirements differ.

LangSmith can trace a function with its `traceable` decorator, which works on any function in any application, alongside broad SDK parity across Python and TypeScript. Galileo’s integrations commonly require OpenTelemetry configuration. Galileo’s native tracing path is still maturing, and its automatic instrumentation is more limited for TypeScript teams. Teams using TypeScript should expect to configure more of their tracing setup themselves.

For teams considering Galileo’s native SDK, three current limitations can affect which frameworks and execution patterns it supports:

- No support yet for ADK, OTel, or LangChain integrations on this path. Galileo's separate OTel-based integration covers LangChain, Google ADK, and Microsoft Agent Framework.
- Galileo’s native SDK does not support fire-and-forget tracing, so applications must wait for a server response when sending trace data, which can add latency to an agent workflow.
- The native SDK does not support nested workflows that run tasks in parallel, which limits its use for agents that fan out work to several tools or subagents at once.

These limitations matter most for teams that rely on TypeScript, framework integrations, or agents that fan out work in parallel.

## Offline datasets and online evaluators

While tracing captures what happened, evaluation determines what to do about it. Curated-dataset regression evals and sampled-traffic online evaluators are complementary methods, and a platform that ships only one half of the pair leaves it up to the user to build the other half.

Galileo’s preconfigured RAG and agentic evaluation catalog gives teams toggle-on workflows for getting initial coverage without writing custom evaluators. Once teams move beyond preconfigured checks, the comparison shifts to pairwise-preference judges, dataset versioning, team-defined structured outputs, and automated production-to-dataset loops, areas where LangSmith offers more depth.

LangSmith supports this more customized evaluation work through two core capabilities:

- **Pairwise experiments and summary evaluators** let teams A/B test two prompt versions on the same dataset, then review the results in a single comparison view.
- **Dataset schemas, tagging, and splits** let teams define typed inputs, label examples by failure mode, and create train and holdout splits in the UI.

### LLM-as-a-judge and the online-to-offline loop

LangSmith treats [LLM-as-a-judge](https://www.langchain.com/resources/llm-as-a-judge) as a first-class evaluator within its evaluation layer. Judges return structured JSON that the evaluator can parse without having to post-process free-form text. Teams can version and manage judge prompts in LangSmith alongside application prompts. [Align Evals](https://www.langchain.com/blog/introducing-align-evals) calibrates each judge against human-graded baselines before it gates a deploy. The methodology stays under the same versioning and review discipline as the dataset it runs against.

Online evaluators in LangSmith continuously score sampled production traffic. [Insights](../langsmith/insights.md) automatically analyzes the trace stream to surface usage patterns and failure modes that the team did not preregister. Together they form a five-part feedback loop:

- Insights surfaces a pattern.
- The team adds the matching trace to a dataset.
- The dataset feeds an offline regression eval.
- The eval gates the next deploy.
- The deploy generates new production traffic the online evaluators score.

Galileo offers related evaluation capabilities, including multi-judge evaluators, session-level annotations, and more extensive synthetic dataset generation. Its workflow still requires teams to write SDK code to route filtered production traces back into a dataset because it lacks a rule-based automation for that step.

That versioning and eval discipline is what Yusuke Kaji, General Manager of AI for Business at Rakuten, means when he says, "LangSmith allows us to get things done scientifically." [Three engineers built Rakuten's employee chatbot platform](https://www.langchain.com/blog/customers-rakuten) on LangChain's OpenGPTs package in one week, ahead of a planned rollout to 32,000 employees across Rakuten's 70+ businesses. Through LangSmith, teams distribute working prompts, collaborate across functions, and develop ideas independently. Pairwise experiments and dataset splits give speed and rigor room to compound at scale.

## Production traces back into datasets

When an agent produces an incorrect or low-quality result in production, teams can add the trace from that run to a dataset with a single click. That dataset becomes the ground truth for regression testing, so once a bug is fixed, it stays fixed.

ServiceNow runs this loop in production across a full [multi-agent customer lifecycle](https://www.langchain.com/blog/customers-servicenow). The system, built on [LangGraph](https://www.langchain.com/langgraph), orchestrates the customer journey from lead qualification through onboarding and implementation to customer satisfaction and advocacy. LangSmith handles granular step-by-step tracing across that lifecycle, with custom evaluation metrics per agent and golden datasets auto-promoted from successful runs that cross score thresholds.

Here is how LangSmith supports each step in the workflow, from capturing a production run to testing and deploying an improved version:

| Loop step | LangSmith primitive | What closes the edge |
| --- | --- | --- |
| Capture | traceable decorator emits a trace | Decorator wraps any function; works regardless of framework |
| Filter | Online evaluators score sampled traffic | Insights surfaces patterns the team did not preregister |
| Route | Automation rule fires on the filter match | Trace lands in a dataset, annotation queue, or webhook |
| Curate | Human review through annotation queues | Reviewer corrections feed the evaluator and the dataset |
| Gate | Offline regression eval on the dataset | Pairwise experiment compares candidate against baseline |
| Deploy | Next version ships behind the gate | New production traffic generates the next batch of traces |

That workflow becomes more concrete in a production agent. Our own [GTM agent](https://www.langchain.com/blog/how-we-built-langchains-gtm-agent) runs on Deep Agents and LangSmith. Each time a sales rep sends, edits, or cancels an action, LangSmith records the event in the run’s trace. Those records help the team refine the evaluators that assess later agent outputs and add useful examples to the dataset for the next regression test.

That example highlights the key difference between capturing production feedback and turning it into a repeatable regression test. Both platforms can capture and evaluate production activity. With Galileo, teams use SDK code to move selected traces into a curated dataset for future testing. LangSmith provides rule-based routing and annotation workflows for that step.

## Framework neutrality without the friction

LangSmith works regardless of whether the team built on the LangChain framework, LangGraph, Deep Agents, any other framework, or custom code. The `traceable` decorator handles trace ingestion across the full list: LangChain, LangGraph, Deep Agents, AutoGen, Claude Agent SDK, CrewAI, Mastra, OpenAI Agents, PydanticAI, Vercel AI SDK, and end-to-end OTel ingestion available in 2026.

Galileo's integrations page lists A2A Protocol, CrewAI, Google ADK, LangChain and LangGraph, OpenAI SDK, OpenAI Agents SDK, Microsoft Agent Framework, Strands Agents, and Vercel AI SDK, plus any framework that supports OpenTelemetry or OpenInference. Most of these integrations use standard OTel components, including `TracerProvider()`, `GalileoSpanProcessor`, and `set_tracer_provider()`.

Integration coverage alone should not decide the choice. Both platforms support LangChain, LangGraph, many other agent frameworks, and OpenTelemetry. The more useful question is how much instrumentation work your team will take on. LangSmith is designed for a quick start from application code, while Galileo offers broad standards-based coverage that can require more OpenTelemetry configuration, especially for TypeScript teams. Run one of your existing agentic workflows through both platforms to see which setup fits your stack and workflow.

### Friction shows up at trace ingestion

Many LangSmith customers, including Clay, Harvey, and Vanta, run LangSmith without our [open source frameworks](https://www.langchain.com/blog/on-agent-frameworks-and-agent-observability), relying on it for [observability](https://www.langchain.com/resources/ai-observability) and [evals](https://www.langchain.com/resources/llm-evals). Both platforms can trace agents built on non-LangChain frameworks. The practical difference is the setup required to start collecting useful traces. On a non-LangChain stack, LangSmith requires one decorator on the agent's entry function and delivers a clean trace. Galileo, on the same stack, requires writing the OTel boilerplate first, then debugging whatever silent-fail behavior the SDK exposes on a stack that does not match the integration's reference implementation, then reading the trace.

## Where Galileo's architecture is strongest

An honest comparison should also highlight Galileo’s clearest strengths.

Three areas stand out:

- **Agent Control's centralized governance architecture:** Agent Control is Galileo's recently announced open-source control plane for centralized governance and runtime policy enforcement, built for teams that value security and governance. Teams can bring their own guardrail tooling from supported third parties or use Galileo's native guardrails, including Luna-2 SLM guards or deterministic guards such as regex or list matching. The client-server model, with @control decorators in application code and policy enforcement on a separate server, lets platform and governance teams change policies without app teams making code changes or redeploying.
- **Luna-2's eval-tuned SLM profile:** Galileo offers Luna-2, a fine-tuned small language model in 3B and 8B Llama-based variants, purpose-built for evaluations. After fine-tuning Luna-2 on a labeled customer dataset, teams may be able to run evaluations at a lower cost. Luna-2 returns scores without the interpretive reasoning that an LLM-as-a-judge can produce, which is the trade-off behind its latency and cost.
- **Agent Graph as a visual debugging surface:** Galileo's Agent Graph renders multi-agent execution as a graph of nodes that can be clicked into for per-node telemetry. Galileo compiles the view from log streams, which makes it valuable to multi-framework teams that want one visual debugging surface across stacks.

What this means for buyers:

- **Fast initial evaluation coverage:** Galileo’s preconfigured RAG and agent evaluations, multi-judge configuration, session-level annotations, and synthetic dataset tools can help teams begin evaluating agents without building every component themselves.
- **Potentially lower evaluation costs at scale:** A fine-tuned Luna-2 model may cost less to run than a large language model judge, but that advantage depends on having a labeled dataset and maintaining the data program behind it.
- **A runtime-control focus:** Galileo is strongest for teams that want to apply governance and guardrails while an agent is running. LangSmith is a better fit for teams focused on turning production failures into regression tests before the next release.

## Capability matrix, organized by loop step

The tables below summarize how LangSmith and Galileo compare across the capabilities covered in this guide, from tracing and evaluation to production feedback and deployment.

**Trace ingestion and visualization**

| Capability | LangSmith | Galileo | Notes |
| --- | --- | --- | --- |
| Multi-turn debugging via threads | Yes | Yes | LangSmith uses Runs, Traces, Threads as primitives. |
| Distributed tracing | Yes | Beta | Galileo's native-SDK distributed tracing is in beta; the OTel-based path is GA. |
| Automated insights from traces | Yes | Yes | Both surface patterns from production traces. |

**Evaluation primitives**

| Capability | LangSmith | Galileo | Notes |
| --- | --- | --- | --- |
| Pairwise-preference LLM judges | Yes | Partial | Galileo supports preference-ranking judge types and side-by-side experiment comparison; LangSmith differentiates on pairwise as a first-class evaluator surface. |
| Dataset schemas, tagging, splits | Yes | Partial | Galileo has dataset versioning; LangSmith adds deeper schemas, tagging, and splits primitives. |
| Team-defined structured judge outputs | Yes | Partial | Galileo supports five typed output formats (Boolean, Categorical, Count, Discrete, Percentage) plus custom-metric code; LangSmith differentiates on arbitrary team-defined JSON schemas. |
| LLM-as-a-judge prompts via prompt hub | Yes | Partial | Galileo supports prompt creation, versioning, and retrieval in the Console; LangSmith differentiates by managing judge prompts in the same Prompt Hub as application prompts. |
| Align Evals (calibrate against human baselines) | Yes | Partial | Galileo's Autotune workflow accepts human-corrected expected values and retunes judge prompts; LangSmith differentiates on packaging within the evaluations layer. |

**Automations and feedback loops**

| Capability | LangSmith | Galileo | Notes |
| --- | --- | --- | --- |
| Production → dataset improvement loops | Yes | Partial | LangSmith Automations route filtered traces via rules; Galileo supports SDK and API curation but no rule-based equivalent. |
| Annotation queues with add-to-dataset | Yes | Beta | Galileo annotation queues are in enterprise beta. |

**Deployment + runtime**

| Capability | LangSmith | Galileo | Notes |
| --- | --- | --- | --- |
| Agent deployments | Yes | No | LangSmith ships a managed deployment runtime. |
| No-code agent builder (Fleet) | Yes | No | Unique to LangSmith. |

**Developer experience**

| Capability | LangSmith | Galileo | Notes |
| --- | --- | --- | --- |
| Framework integrations breadth | Yes | Partial | LangSmith covers AutoGen, Claude Agent SDK, CrewAI, Mastra, OpenAI Agents, PydanticAI, Vercel AI SDK plus OTel. |
| OTel ingestion | Yes | Yes | Galileo integrations rely heavily on OTel TracerProvider() configuration. |
| TS SDK at parity with Python | Yes | Partial | Galileo TypeScript SDK is not at parity with Python. |
| CI/CD support out of the box | Yes | Partial | Galileo documents experiments in CI/CD pipelines via run_experiment(); no first-party GitHub Actions plugin. |
| Granular RBAC | Yes | Partial | LangSmith RBAC supports custom permissions. |

LangSmith provides a more complete built-in workflow for turning production traces into regression tests, including routing traces to datasets, defining structured evaluator outputs, organizing datasets, and gating deployments. Galileo stands out for multi-judge evaluation, session annotations, synthetic data generation, and visual debugging. Teams that need the full production-to-regression-test workflow will find more of it packaged in LangSmith, while teams prioritizing those evaluation and runtime surfaces may favor Galileo.

## Which platform fits your team?

The right choice depends on the job you need the platform to do in production. Galileo is geared toward runtime governance and controls. LangSmith is geared toward tracing production failures and using them to improve future releases.

The situations below show where each option fits best:

- **Regulated enterprise where small language model-backed runtime guardrails are a critical feature.** Galileo's Luna-2 and Agent Control are built for this scenario. Choose Galileo when runtime governance is a priority and your team has the labeled data needed to support it. Luna-2 may lower evaluation costs, but its performance depends on high-quality training data and ongoing maintenance.
- [**Full agent development lifecycle (ADLC)**](https://www.langchain.com/blog/the-agent-development-lifecycle)** engineering **with frequent prompt iterations and a regression-test discipline. LangSmith can automatically turn selected production traces into test cases. Teams use those tests to check a new version before release and catch the same problem again.
- **Multi-framework team on LangGraph plus a non-LangChain stack.** Both platforms support these environments, so framework choice alone should not decide the purchase. Test each platform with one of your production workflows to see which better fits how your team investigates failures and improves the agent.

Both platforms give teams visibility into how their agents behave. The key difference is where they put that insight to work: LangSmith helps teams improve the next version of an agent, while Galileo helps teams evaluate and govern an agent while it is running. Choose the platform that best supports the responsibility your team needs to strengthen first.
