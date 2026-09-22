---
title: "langchain"
description: "Index of 33 pages and 7 subdirectories under langchain."
category: "index"
tags: [index, langchain]
---

# langchain

33 pages here, 80 pages including subdirectories.

## Directories

- [errors/](errors/_index.md) - 7 pages
- [frontend/](frontend/_index.md) - 20 pages
- [mcp/](mcp/_index.md) - 3 pages
- [middleware/](middleware/_index.md) - 3 pages
- [multi-agent/](multi-agent/_index.md) - 10 pages
- [streaming/](streaming/_index.md) - 1 page
- [test/](test/_index.md) - 3 pages

## Files

- [Agents](agents.md) - An agent is a model calling tools in a loop until a given task is complete.
- [Component architecture](component-architecture.md) - LangChain's power comes from how its components work together to create sophisticated AI applications. This page provides diagrams showcasing the relationships between different components.
- [Context engineering in agents](context-engineering.md) - The hard part of building agents (or any LLM application) is making them reliable enough. While they may work for a prototype, they often fail in real-world use cases.
- [Build a data analysis agent from scratch](deep-agent-from-scratch.md) - Build a data analysis agent step by step using create_agent and Deep Agents middleware.
- [Deployment](deploy.md) - Deploy LangChain agents to production with LangSmith Cloud or JavaScript frameworks and hosting platforms.
- [Event streaming](event-streaming.md) - Stream real-time updates from LangChain agent runs
- [Get help](get-help.md) - Connect with the LangChain community, access learning resources, and get the support you need to build with confidence.
- [Guardrails](guardrails.md) - Implement safety checks and content filtering for your agents
- [Human-in-the-loop](human-in-the-loop.md) - The Human-in-the-Loop (HITL) middleware lets you add human oversight to agent tool calls. When a model proposes an action that might require review—for example, writing to a file or executing SQL—the...
- [Overview](index.md) - Control and customize agent execution at every step
- [Install LangChain](install.md) - To install the LangChain package:
- [Build a semantic search engine with LangChain](knowledge-base.md) - Build a semantic search engine over a PDF with LangChain embeddings and vector stores. Use it to retrieve passages similar to a query, then plug the retriever into retrieval-augmented generation...
- [Long-term memory](long-term-memory.md) - Add long-term memory to LangChain agents to store and recall data across conversations and sessions
- [Model Context Protocol (MCP)](mcp.md) - Connect LangChain agents to MCP servers with the MCPAdapter, built on FastMCP.
- [Messages](messages.md) - Messages are the fundamental unit of context for models in LangChain. They represent the input and output of models, carrying both the content and metadata needed to represent the state of a...
- [Overview](middleware.md) - Control and customize agent execution at every step
- [Models](models.md) - LLMs are powerful AI tools that can interpret and generate text like humans. They're versatile enough to write content, translate languages, summarize, and answer questions without needing...
- [Multi-agent](multi-agent.md) - Multi-agent systems coordinate specialized components to tackle complex workflows. However, not every complex task requires this approach—a single agent with the right (sometimes dynamic) tools and...
- [LangSmith Observability](observability.md) - As you build and run agents with LangChain, you need visibility into how they behave: which tools they call, what prompts they generate, and how they make decisions. LangChain agents built with...
- [LangChain overview](overview.md) - LangChain provides create_agent: a minimal, highly configurable agent harness. Compose exactly the agent your use case needs from model, tools, prompt, and middleware.
- [Philosophy](philosophy.md) - LangChain exists to be the easiest place to start building with LLMs, while also being flexible and production-ready.
- [Quickstart](quickstart.md) - Build your first agent in minutes
- [Retrieval](retrieval.md) - Large Language Models (LLMs) are powerful, but they have two key limitations:
- [Runtime](runtime.md) - LangChain's create_agent runs on LangGraph's runtime under the hood.
- [Short-term memory](short-term-memory.md) - Memory is a system that remembers information about previous interactions. For AI agents, memory is crucial because it lets them remember previous interactions, learn from feedback, and adapt to user...
- [Build a SQL agent](sql-agent.md) - In this tutorial, you will learn how to build an agent that can answer questions about a SQL database using LangChain agents.
- [Streaming](streaming.md) - Stream real-time updates from agent runs
- [Structured output](structured-output.md) - Structured output allows agents to return data in a specific, predictable format. Instead of parsing natural language responses, you get structured data in the form of JSON objects, Pydantic models...
- [LangSmith Studio](studio.md) - When building agents with LangChain locally, it's helpful to visualize what's happening inside your agent, interact with it in real-time, and debug issues as they occur. LangSmith Studio is a free...
- [Test](test.md) - Strategies for testing LangChain agents, including unit tests, integration tests, and trajectory evaluations.
- [Tools](tools.md) - Tools extend what agents can do—letting them fetch real-time data, execute code, query external databases, and take actions in the world.
- [Agent Chat UI](ui.md) - Agent Chat UI is a Next.js application that provides a conversational interface for interacting with any LangChain agent. It supports real-time chat, tool visualization, and advanced features like...
- [Build a voice agent with LangChain](voice-agent.md) - Chat interfaces have dominated how we interact with AI, but recent breakthroughs in multimodal AI are opening up exciting new possibilities. High-quality generative models and expressive...
