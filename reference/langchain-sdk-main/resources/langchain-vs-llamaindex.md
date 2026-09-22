---
title: "LangChain vs LlamaIndex: from retrieval to reliable AI agents"
description: "Compare LangChain and LlamaIndex for building production-grade AI agents."
source: "https://www.langchain.com/resources/langchain-vs-llamaindex"
category: "resources"
published: "2026-06-23"
author: "LangChain"
tags: [resources, langchain-vs-llamaindex]
---

# LangChain vs LlamaIndex: from retrieval to reliable AI agents

**Takeaways**

- Pick LangChain or LangGraph for orchestration-heavy AI agents: multi-step execution, branching, loops, durable state, retries, approvals, and complex tool use.
- Pick LlamaIndex for data-heavy LLM applications: 130+ file formats via LlamaParse, 300+ integration packages including 158 reader packages, hybrid search and recursive retrieval out of the box.
- LangSmith is our framework agnostic agent engineering platform, offering observability, evaluation, and deployment that works with LangChain, LangGraph, Deep Agents, LlamaIndex, the OpenAI SDK, the Anthropic SDK, the Vercel AI SDK, and your own custom code.

Most teams asking whether to choose LangChain or LlamaIndex do not have to pick just one. In practice, many production stacks use LlamaIndex for retrieval, LangChain or LangGraph for orchestration, and LangSmith for the agent improvement loop on top of either.

## LangChain and LlamaIndex have different focuses

LangChain (and LangGraph) and LlamaIndex are purpose built for different parts of the AI agent stack, and the right choice depends on where most of your application's complexity sits.

We built [LangGraph](https://www.langchain.com/langgraph) as the orchestration framework and runtime for long-running, stateful AI agents; LlamaIndex built Workflows and AgentWorkflow for event-driven multi-step applications. Both frameworks have expanded past their original scope, but the central focuses haven’t changed.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a24f9bc93d4f2c8ef84aad6_Frame%202147255DWQ849.png)LangGraph allows for low-level control and customizable agents

Harrison Chase's [working definition of an AI agent](https://www.langchain.com/blog/what-is-an-agent) is:

> An AI agent is a system that uses an LLM to decide the control flow of an application.

That framing leads to a practical question around where the LLM’s decision-making sits in your system. If it is choosing routes, tools, retry behavior, and managing multi-turn state, you are solving an orchestration problem. If it is deciding which documents are relevant, how to parse a PDF, and how to blend results across multiple index types, you are solving a data-layer problem. The frameworks differ in how they build the supporting infrastructure, but the core loop is the same: an LLM running in a loop and calling tools.

That framing leads to a practical question around where the LLM’s decision-making sits in your system. If it is choosing routes, tools, retry behavior, and managing multi-turn state, you are solving an orchestration problem. If it is deciding which documents are relevant, how to parse a PDF, and how to blend results across multiple index types, you are solving a data-layer problem. The frameworks differ in how they build the supporting infrastructure, but the core loop is the same: an LLM running in a loop and calling tools.

A [recent comparison](https://dev.to/lycore/langchain-vs-llamaindex-in-2026-what-we-actually-use-and-why-52eb) of LangChain and LlamaIndex by the Lycore team highlights the trap many teams fall into when adopting either framework:

> Both are tools, not commitments. The mistake most teams make is picking one and trying to use it for everything.

## LlamaIndex strengths: ingestion, indexing, retrieval

If your app lives or dies by retrieval quality, LlamaIndex could be a good fit. It is built around the data layer: ingest messy inputs, structure them, index them, and retrieve context with a lot of control when the “standard RAG setup” stops being enough.

| Capability | LangChain | LlamaIndex |
| --- | --- | --- |
| File format coverage | Document loaders + first-class LlamaIndex retriever integration | 130+ formats via LlamaParse, 100+ languages, layout-aware parsing with LLM/VLM modes |
| Total integrations | 1,000+ integrations across the stack (models, vector stores, tools, embeddings, document loaders) | 300+ integration packages across the stack (158 reader packages plus the LlamaHub registry, verified May 2026) |
| Retrieval primitives | EnsembleRetriever, ContextualCompressionRetriever, ParentDocumentRetriever, MultiVectorRetriever | Hybrid search, recursive retrieval, query decomposition, sub-question generation, hierarchical node parsing, auto-merging |
| Index and retrieval types | VectorStore, GraphRAG (knowledge graph), self-query, multi-query, time-weighted vector, parent-document, multi-vector, contextual-compression | VectorStoreIndex, SummaryIndex, TreeIndex, KeywordTableIndex, PropertyGraphIndex |
| Managed deployment | LangSmith Deployment | LlamaCloud (paid, separate product) |

[LlamaParse](https://www.llamaindex.ai/pricing) is the differentiator. It automates document processing that used to take hours of manual cleanup, with multimodal parsing that handles charts, tables, and images alongside text. The combination of [130+ file formats](https://www.llamaindex.ai/pricing), 100+ languages, and layout-aware parsing (with precise bounding-box layout detection plus dedicated chart, graph, and table extraction) lets teams extract structured information from messy real-world documents, not just clean PDFs. The [158 reader integration packages](https://github.com/run-llama/llama_index) (verified May 2026) extend ingestion to sources like Google Drive, Notion, SQL, audio, and more.

The [dev.to](http://dev.to) comparison notes LlamaIndex’s advanced retrieval capabilities:

LlamaIndex has better out-of-the-box support for more sophisticated retrieval patterns: hybrid search, recursive retrieval, query decomposition, and sub-question generation. If retrieval quality is your main concern, LlamaIndex gives you more levers to pull.

On heterogeneous inputs (PDFs, Notion pages, database rows, and the long tail), the same write-up argues that LlamaIndex’s loading and chunking abstractions are more coherent, and that mixed-source ingestion is a more natural fit in its model.

LangChain's document loaders and retrievers are strong for the standard cases, and LangChain even promotes first-class LlamaIndex retriever integrations because that depth can be valuable.

## Where LangGraph's persistence pays off

Most agents need persistence. They need it the moment a workflow has to wait on a human, hold context across hours, or recover from a crashed run.

LangGraph's approach starts with persistence:

We did this by making [persistence a first class citizen](https://www.langchain.com/blog/making-it-easier-to-build-human-in-the-loop-agents-with-interrupt) in LangGraph. Every step of the graph, it reads from and then writes to a checkpoint of that graph state.

That checkpoint makes interrupt-and-resume work: pause an AI agent for a human approval, then resume from exactly where it stopped. You can think of this persistence layer as a scratchpad for human/agent collaboration. LangGraph [resumes from prior checkpoints](../langgraph/use-time-travel.md) so nodes before the checkpoint are not re-executed (results are already saved). Nodes after the checkpoint re-execute, including any LLM calls, API requests, and interrupts.

Persistence is what makes multi-agent delegation safe to run in production. [Four multi-agent patterns](https://www.langchain.com/blog/choosing-the-right-multi-agent-architecture) build on it:

- **Subagents:** Spawn focused specialists to handle a subtask (e.g., “research topic X,” “draft the comparison table,” “generate test prompts”), then merge results back into the main agent’s state.
- **Skills:** Reusable, well-tested capabilities you call repeatedly (e.g., “extract requirements,” “summarize docs,” “generate evaluation set”), treated like modular tools rather than one-off prompts.
- **Handoffs:** Transfer control to a different agent when the task changes shape (e.g., from “research” to “writing” to “editorial QA”) while preserving full context and traceability.
- **Routers:** Decide which agent or skill to invoke based on the current state (inputs, confidence, failure signals, cost limits), instead of hard-coding a single workflow.

In a multi-agent setup, you want two guarantees: (1) each specialist can work independently, and (2) the overall system can pause, recover, and continue without losing the thread of what happened. Persistence gives you that second guarantee. Every subagent run, tool call, and intermediate decision becomes state you can resume, inspect, and evaluate.

Multi-agent systems justify their overhead when the work can be decomposed into parts that are (a) independent, (b) benefit from specialization, and (c) would otherwise force one agent into long, fragile reasoning chains. If the task is straightforward, a single agent with good tools is usually simpler and more reliable.

[Anthropic's 2025 research on multi-agent systems](https://www.anthropic.com/engineering/multi-agent-research-system) found that a multi-agent system using Claude Opus 4 as the lead and Claude Sonnet 4 as subagents outperformed a single-agent Claude Opus 4 setup by 90% on Anthropic's internal research eval.

However, as [Sydney Runkle wrote on our blog](https://www.langchain.com/blog/choosing-the-right-multi-agent-architecture), many agentic tasks are best handled by a single agent with well-designed tools. Start there: single agents are simpler to build, reason about, and debug.

LlamaIndex’s orchestration model is intentionally different. Workflows are “an event-driven, step-based way to control the execution flow of an application.”

[AgentWorkflow](https://www.llamaindex.ai/blog/introducing-agentworkflow-a-powerful-system-for-building-ai-agent-systems) from LlamaIndex builds on the Workflow abstraction to coordinate multiple agents, maintain state, and handle tool-calling. The AgentWorkflow announcement walks through a research, writing, and review pipeline using specialized agents with handoffs and shared state across agents.

LlamaIndex Workflows ship checkpointing too. You can opt in via `WorkflowCheckpointer` and serialize state with `Context.to_dict()` and `Context.from_dict()`. In LangGraph, checkpointing is the default execution model when a checkpointer is configured, which is what makes interrupt-and-resume work without extra wiring. The Lycore post summarized this tradeoff well:

> If you need an agent that takes sequential actions across multiple external tools — not just retrieval — LangChain or building directly on the OpenAI/Anthropic function calling API is usually cleaner.

## How to choose between LangChain and LlamaIndex

Here’s a practical three-step framework we use with teams scoping an agent engineering stack:

**Step 1: Name the workload.** If it’s orchestration (tool selection, retry logic, human approval gates), LangGraph is a good fit. Data retrieval (which documents are relevant, how to parse a PDF, how to combine results across index types) could mean that Llamaindex is a good fit. .

**Step 2: Consider starting without a framework.** A common recommendation we agree with: if it's your team's first AI feature, call the model API directly until the complexity requires a framework like LangGraph or LangChain.

**Step 3: Use both when needed. **The hybrid approach can work well. A common hybrid pattern wraps LlamaIndex query engines as tools that LangGraph nodes call during execution. LlamaIndex handles document retrieval. LangGraph runs the agent loop, manages durable state, and supports human-in-the-loop gates. [LangSmith](https://www.langchain.com/langsmith-platform) traces the full flow end to end.

## How LangSmith makes either framework reliable

LangSmith is our framework agnostic agent engineering platform that offers observability, evaluation, and deployment. It works across LangChain, LangGraph, Deep Agents, LlamaIndex, the OpenAI SDK, the Anthropic SDK, the Vercel AI SDK, and your own custom code. The production problem LangSmith exists to solve goes beyond logging. It is a [reasoning problem](https://www.langchain.com/blog/agent-observability-powers-agent-evaluation):

> When an agent takes 200 steps over two minutes to complete a task and makes a mistake somewhere along the way, that's a different type of error. There's no stack trace, because there's no code that failed. What failed was the agent's reasoning.

Infrastructure-level APM tracing can tell you a request failed; LangSmith traces the reasoning chain to show why. The same agent input can lead to different tool calls, retrieve different context, and produce different answers from one run to the next. Without observability, you cannot see what changed, so you end up guessing why the agent failed based only on the final output.

LangSmith [Insights](../langsmith/insights.md) analyzes traces to surface common usage patterns, agent behaviors, and failure modes, and the analysis can be generated on demand or run on a schedule.

[Chat](../langsmith/chat.md), LangSmith's embedded AI debugging assistant, reads across traces to answer questions in natural language. A developer asks LangSmith Chat a question in natural language ("Why did the agent enter this loop?" or "Did the model hallucinate in step 3?"), and Chat replaces hours of manual trace inspection with a targeted root-cause analysis.

LangSmith’s evaluation layer closes the loop on improving agents. For [LLM evals](https://www.langchain.com/articles/llm-evals), the scoring approach is usually not the limiting factor. The bigger constraint is the workflow that turns production failures into reproducible test cases. [LangSmith Evaluation](https://www.langchain.com/langsmith/evaluation) supports offline evals on curated datasets and online evals on production traffic, scored by [LLM-as-judge](https://www.langchain.com/articles/llm-as-a-judge), code-based, or pairwise evaluators. Align Evals then calibrates judges against human corrections so the evaluators better match your team’s judgment over time.

[Annotation Queues](../langsmith/annotation-queues.md) are where that judgment enters the agent engineering loop. They give labelers, SMEs, product managers, and domain experts a structured place to review traces, correct outputs, and turn those corrections into datasets that catch regressions. AI agents work best when they reflect the knowledge and judgment your team has built over time. A production trace that surfaced a failure becomes a reproducible test case in one step, then joins the dataset that catches regressions in the next deployment.

[LangSmith Engine](https://www.langchain.com/langsmith/engine) brings this all together. Engine is an agent for agent engineering. It analyzes production traces, groups related failures, and recommends fixes so your team can improve agent quality faster.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a38af27efe357a4496438a0_LangSmith%20Engine.png)

> Once you've picked your framework, the next step is wiring in observability before you ship. Chat with an expert about how to use[LangSmith with your stack](https://www.langchain.com/contact-sales) so you can see the trace-to-evaluation loop running across LangChain, LangGraph, LlamaIndex, or whatever you build with.

## Frequently asked questions

### Can I use LlamaIndex with LangChain?

Yes. The canonical form wraps a LlamaIndex query engine as a tool that a LangGraph node invokes during execution: LlamaIndex handles document parsing, indexing, and retrieval; LangChain or LangGraph handles the agent loop, state, and tool calling. The community packages [LlamaIndexRetriever](https://reference.langchain.com/python/langchain-community/retrievers/llama_index/LlamaIndexRetriever) and [LlamaIndexGraphRetriever](https://reference.langchain.com/python/langchain-community/retrievers/llama_index/LlamaIndexGraphRetriever) ship in `langchain-community` for the basic case. For production hybrid stacks, wrap the query engine in a custom tool rather than using the community retrievers directly, so you control invocation, retries, and error handling inside the agent loop.

### Does LangSmith work if I'm not using LangChain?

Yes. LangSmith is framework agnostic and works across any LLM framework. Wrap any function or LLM call with the `@traceable` decorator and traces flow into LangSmith regardless of whether the underlying code calls LangChain, LangGraph, Deep Agents, LlamaIndex, the OpenAI SDK, the Anthropic SDK, the Vercel AI SDK, or your own custom orchestration. You can use your favorite framework and you'll always get full trace visibility, plus access to LangSmith Evaluations, Annotation Queues, Insights, and Chat on top.

### What's the difference between LangChain and LangGraph?

LangChain is the higher-level framework for shipping AI agents fast: standardized model abstractions, prebuilt agent patterns, and 1,000+ integrations. LangGraph is the lower-level orchestration framework and runtime underneath it: durable execution, checkpoints, human-in-the-loop interrupts, and the fine-grained state control that production agents need. LangChain lets you build and ship agents fast with high-level abstractions for common patterns, while LangGraph gives you fine-grained control for complex workflows.

### Do I need LlamaCloud to use LlamaIndex?

No. The LlamaIndex framework itself is open source and runs on its own. LlamaCloud is the separate managed service for parsing (LlamaParse), indexing, and retrieval. You can use it as a SaaS or, on enterprise plans, [self-host the LlamaCloud platform](https://developers.llamaindex.ai/python/cloud/self_hosting/architecture/) on your own infrastructure. The free tier comes with 10,000 credits per month; paid tiers start at $50/month per the [LlamaIndex pricing page](https://www.llamaindex.ai/pricing). If your parsing and retrieval can be served by the open-source LlamaIndex framework, LlamaCloud is optional. If your team needs managed parsing for unstructured data at production scale, you can get that with LlamaCloud.

‍
