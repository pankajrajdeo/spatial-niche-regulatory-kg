---
title: "model_fallback"
description: "Model fallback middleware for agents."
source: "https://reference.langchain.com/python/langchain/agents/middleware/model_fallback"
category: "reference"
tags: [reference, langchain, agents, middleware, model_fallback]
---

# model_fallback

> **Module** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/model_fallback)

Model fallback middleware for agents.

When a caching middleware such as `AnthropicPromptCachingMiddleware` wraps this
middleware from the outside, it applies Anthropic `cache_control` markers to the
request *before* the fallback loop runs. Those markers are provider-specific and
cause API errors on non-Anthropic fallback models, so this middleware strips them
from fallback attempts — but only when the fallback model itself cannot accept
Anthropic cache markers. When the fallback is another Anthropic model the markers
are valid and preserve prompt caching, so they are left intact.

The knowledge of the `cache_control` marker is duplicated here (rather than owned
solely by the Anthropic partner package) because an outer caching middleware
never re-runs during fallback and therefore cannot clean up after itself.

## Properties

- `ResponseT`
- `logger`

## Methods

- [`init_chat_model()`](https://reference.langchain.com/python/langchain/agents/middleware/model_fallback/init_chat_model)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/model_fallback.py)
