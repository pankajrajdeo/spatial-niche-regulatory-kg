---
title: "Runtimes, frameworks, and harnesses"
description: "Understand the differences between LangChain, LangGraph, and Deep Agents and when to use each one"
source: "https://docs.langchain.com/oss/python/concepts/products"
category: "docs"
tags: [docs, concepts, products]
---

# Runtimes, frameworks, and harnesses

> Understand the differences between LangChain, LangGraph, and Deep Agents and when to use each one

LangChain maintains several open source packages to help you build agents. Each serves a different purpose in the agent development stack. Understanding the distinctions between [agent frameworks](#agent-frameworks-like-langchain), [agent runtimes](#agent-runtimes-like-langgraph), and [agent harnesses](#agent-harnesses-like-the-deep-agents-sdk) helps you choose the right tool for your needs.

<table>
  <thead>
    <tr>
      <th />

      <th>Runtime</th>
      <th>Framework</th>
      <th>Harness</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Value add</td>
      <td class="tdlist"><ul><li>Durable execution</li><li>Streaming</li><li>HITL</li><li>Persistence</li></ul></td>
      <td class="tdlist"><ul><li>Abstractions</li><li>Integrations</li></ul></td>
      <td class="tdlist"><ul><li>Predefined tools</li><li>Prompts</li><li>Subagents</li></ul></td>
    </tr>

    <tr>
      <td>When to use</td>
      <td class="tdlist"><ul><li>Low-level control</li><li>Long running, stateful workflows and agents</li></ul></td>
      <td class="tdlist"><ul><li>Getting started quickly</li><li>Standardizing how a team builds</li></ul></td>
      <td class="tdlist"><ul><li>More autonomous agents</li><li>Agents faced with complex, non-deterministic tasks</li></ul></td>
    </tr>

    <tr>
      <td>Options</td>
      <td class="tdlist"><ul><li>LangGraph</li><li>Temporal</li><li>Inngest</li></ul></td>
      <td class="tdlist"><ul><li>LangChain</li><li>Vercel's AI SDK</li><li>CrewAI</li><li>OpenAI Agents SDK</li><li>Google ADK</li><li>LlamaIndex</li></ul></td>
      <td class="tdlist"><ul><li>Deep Agents SDK</li><li>Claude Agent SDK</li><li>Manus</li></ul></td>
    </tr>
  </tbody>
</table>

## Agent frameworks (like LangChain)

Agent frameworks provide abstractions that make it easier to get started when building with LLMs.

[LangChain](../langchain/overview.md) is an agent framework that provides abstractions like structured content blocks, the agent loop, and middleware.

LangChain's abstractions are designed to be easy to get started with while still providing the flexibility needed for advanced use cases.

While LangChain is built on top of [LangGraph](../langgraph/overview.md), you don't need to know LangGraph to use LangChain.

Other examples of agent frameworks include [Vercel's AI SDK](https://ai-sdk.dev/docs/introduction), [CrewAI](https://www.crewai.com/), [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/), [Google ADK](https://google.github.io/adk-docs/), [LlamaIndex](https://www.llamaindex.ai/), and many more.

### When to use LangChain

Use LangChain when:

* You want to quickly build agents and autonomous applications.
* You need standard abstractions for models, tools, and agent loops.
* You want an easy-to-use framework that still provides flexibility.
* You're building straightforward agent applications without complex orchestration needs.

## Agent runtimes (like LangGraph)

Agent runtimes provide the tooling for running agents in production.
Supported tools may include:

* **Durable execution**: Agents persist through failures and can run for extended periods, resuming from where they left off.
* **Streaming**: Support for streaming workflows and responses.
* **Human-in-the-loop**: Incorporate human oversight by inspecting and modifying agent state.
* **Persistence**: Thread-level and cross-thread persistence for state management.
* **Low-level control**: Direct control over agent orchestration without high-level abstractions.

[LangGraph](../langgraph/overview.md) is a low-level orchestration framework and runtime for building, managing, and deploying long-running, stateful agents.

Agent frameworks are generally higher level and run on agent runtimes.
For example, LangChain 1.0 is built on top of LangGraph.

Other examples of agent runtimes include [Temporal](https://temporal.io/), [Inngest](https://www.inngest.com/), and other durable execution engines.

### When to use LangGraph

Use LangGraph when:

* You need fine-grained, low-level control over agent orchestration.
* You need durable execution for long-running, stateful agents.
* You're building complex workflows that combine deterministic and agentic steps.
* You need production-ready infrastructure for agent deployment.

## Agent harnesses (like the Deep Agents SDK)

Agent harnesses are opinionated, batteries-included frameworks with built-in tools and capabilities for building sophisticated, long-running agents.
Supported tools may include:

* **Planning capabilities**: Track multiple tasks with a to-do list.
* **Task delegation**: Delegate work and keep context clean with subagents.
* **File system**: Read and write access to files on different pluggable storage backends.
* **Token management**: Conversation history summarization and large tool result eviction.

The [Deep Agents SDK](../deepagents/overview.md) builds on top of LangGraph and adds planning capabilities, file systems for context management, the ability to spawn subagents, and more.
Deep Agents is designed for complex, multi-step tasks that require planning and decomposition.

Example tasks include working with search results, scripts, and other artifacts in state.

Other examples of agent harnesses include [Claude Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview), [Manus](https://manus.im/), and other coding CLIs.

### When to use the Deep Agents SDK

Use the [Deep Agents SDK](../deepagents/overview.md) when:

* You are building agents that run over long time periods.
* You are building agents that need to handle complex, multi-step tasks.
* You want to use predefined tools, such as filesystem operations, bash execution, and automated context engineering.
* You want to use predefined prompts and subagents.

## Feature comparison

While you can accomplish similar tasks with LangChain, LangGraph, and Deep Agents, the level at which you integrate them differ:

| Feature           | LangGraph                                                                   | LangChain                                                               | Deep Agents                                                                  |
| ----------------- | --------------------------------------------------------------------------- | ----------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| Short-term memory | [Short-term memory](../langgraph/add-memory.md#add-short-term-memory) | [Short-term memory](../langchain/short-term-memory.md)            | [`StateBackend`](../deepagents/backends.md#statebackend)               |
| Long-term memory  | [Long-term memory](../langgraph/add-memory.md#add-long-term-memory)   | [Long-term memory](../langchain/long-term-memory.md)              | [Long-term memory](../deepagents/memory.md)                            |
| Skills            | -                                                                           | [Multi-agent skills](../langchain/multi-agent/skills.md)          | [Skills](../deepagents/skills.md)                                      |
| Subagents         | [Subgraphs](../langgraph/use-subgraphs.md)                            | [Multi-agent subagents](../langchain/multi-agent/subagents.md)    | [Subagents](../deepagents/subagents.md)                                |
| Human-in-the-loop | [Interrupts](../langgraph/interrupts.md)                              | [Human-in-the-loop middleware](../langchain/human-in-the-loop.md) | [`interrupt_on` parameter](../deepagents/harness.md#human-in-the-loop) |
| Streaming         | [Streaming](../langgraph/streaming.md)                                | [Agent Streaming](../langchain/event-streaming.md)                | [Streaming](../deepagents/event-streaming.md)                          |

## Learn more

* [LangChain overview](../langchain/overview.md)
* [LangGraph overview](../langgraph/overview.md)
* [Deep Agents overview](../deepagents/overview.md)

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/concepts/products.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
