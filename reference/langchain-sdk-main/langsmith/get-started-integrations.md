---
title: "Integrations"
description: "LangSmith provides integrations for a growing set of popular LLM providers and agent frameworks as well as Deep Agents, LangChain, and LangGraph. For setup and usage, refer to the guides listed on..."
source: "https://docs.langchain.com/langsmith/get-started-integrations"
category: "docs"
tags: [docs, langsmith, get-started-integrations]
---

# Integrations

[LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-integrations) provides integrations for a growing set of popular [LLM providers](#llm-providers) and [agent frameworks](#agent-frameworks) as well as [Deep Agents](../deepagents/overview.md), [LangChain](../langchain/overview.md), and [LangGraph](../langgraph/overview.md). For setup and usage, refer to the guides listed on this page.

## LLM providers

- [Amazon Bedrock](trace-bedrock.md)

- [Anthropic](trace-anthropic.md)

- [DeepSeek](trace-deepseek.md)

- [Google Gemini](trace-with-google-gemini.md)

- [LiteLLM](trace-litellm.md)

- [Mistral](trace-with-mistral.md)

- [OpenAI](trace-openai.md)

- [OpenAI-compatible APIs](trace-with-openai-compatible.md)

> [!NOTE]
> **Using LangChain?** LangChain provides a unified interface to 100+ LLM providers, which allows you to switch between models by setting environment variables. [Initialize a model](../langchain/models.md#initialize-a-model) and LangSmith will automatically trace your application.

## Agent frameworks

- [AutoGen](trace-with-autogen.md)

- [Claude Agent SDK](trace-claude-agent-sdk.md)

- [Claude Managed Agents](trace-with-claude-managed-agents.md)

- [CrewAI](trace-with-crewai.md)

- [Deep Agents](trace-deep-agents.md)

- [Google ADK](trace-with-google-adk.md)

- [LangChain](trace-with-langchain.md)

- [LangGraph](trace-with-langgraph.md)

- [Mastra](trace-with-mastra.md)

- [Microsoft Agent Framework](trace-with-microsoft-agent-framework.md)

- [OpenAI Agents](trace-with-openai-agents-sdk.md)

- [OpenTelemetry](trace-with-opentelemetry.md)

- [PydanticAI](trace-with-pydantic-ai.md)

- [Semantic Kernel](trace-with-semantic-kernel.md)

- [Strands Agents](trace-with-strands-agents.md)

- [Vercel AI SDK](trace-with-vercel-ai-sdk.md)

## Voice AI frameworks

- [OpenAI Realtime](trace-openai-realtime.md)

- [Gemini Live](trace-gemini-live.md)

- [Livekit](trace-with-livekit.md)

- [Pipecat](trace-with-pipecat.md)

## Developer tools

- [Claude Code](trace-claude-code.md)

- [OpenAI Codex](trace-with-codex.md)

- [OpenCode](trace-with-opencode.md)

- [Cursor](trace-with-cursor.md)

- [Instructor](trace-with-instructor.md)

- [n8n](trace-with-n8n.md)

- [Pi](trace-with-pi.md)

- [Temporal](trace-with-temporal.md)

- [VS Code Copilot](trace-with-vscode-copilot.md)

These coding agent integrations follow a shared [metadata contract](coding-agent-metadata-contract.md) that standardizes the trace fields they emit.

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/integrations.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
