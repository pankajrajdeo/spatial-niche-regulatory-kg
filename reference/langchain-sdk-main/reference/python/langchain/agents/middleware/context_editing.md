---
title: "context_editing"
description: "Context editing middleware."
source: "https://reference.langchain.com/python/langchain/agents/middleware/context_editing"
category: "reference"
tags: [reference, langchain, agents, middleware, context_editing]
---

# context_editing

> **Module** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/context_editing)

Context editing middleware.

Mirrors Anthropic's context editing capabilities by clearing older tool results once the
conversation grows beyond a configurable token threshold.

The implementation is intentionally model-agnostic so it can be used with any LangChain
chat model.

## Properties

- `ResponseT`
- `DEFAULT_TOOL_PLACEHOLDER`
- `TokenCounter`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/context_editing.py)
