---
title: "SummarizationMiddleware"
description: "Summarizes conversation history when token limits are approached."
source: "https://reference.langchain.com/python/langchain/agents/middleware/summarization/SummarizationMiddleware"
category: "reference"
tags: [reference, langchain, agents, middleware, summarization, summarizationmiddleware]
---

# SummarizationMiddleware

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/summarization/SummarizationMiddleware)

Summarizes conversation history when token limits are approached.

This middleware monitors message token counts and automatically summarizes older
messages when a threshold is reached, preserving recent messages and maintaining
context continuity by ensuring AI/Tool message pairs remain together.

Transient summary-generation errors (rate limits, timeouts) are retried
in-process, up to 3 attempts total, via `Runnable.with_retry`. If a summary call
still fails after those attempts, the underlying error propagates rather than
fabricating a summary.

## Signature

```python
SummarizationMiddleware(
    self,
    model: str | BaseChatModel,
    *,
    trigger: ContextSize | TriggerClause | list[ContextSize | TriggerClause] | None = None,
    keep: ContextSize = ('messages', _DEFAULT_MESSAGES_TO_KEEP),
    token_counter: TokenCounter = count_tokens_approximately,
    summary_prompt: str = DEFAULT_SUMMARY_PROMPT,
    trim_tokens_to_summarize: int | None = _DEFAULT_TRIM_TOKEN_LIMIT,
    **deprecated_kwargs: Any = {},
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `model` | `str \| BaseChatModel` | Yes | The language model to use for generating summaries. |
| `trigger` | `ContextSize \| TriggerClause \| list[ContextSize \| TriggerClause] \| None` | No | One or more thresholds that trigger summarization.  Provide a single [`ContextSize`][langchain.agents.middleware.summarization.ContextSize] tuple, or a single [`TriggerClause`][langchain.agents.middleware.summarization.TriggerClause] dict, or a list mixing either form.  A `ContextSize` tuple expresses one threshold. A `TriggerClause` dict expresses multiple thresholds that must *all* be met (AND). When a list is provided, summarization runs if *any* item is met (OR).  !!! example      ```python     # Trigger summarization when 50 messages is reached     ("messages", 50)      # Trigger summarization when 3000 tokens is reached     ("tokens", 3000)      # Trigger summarization either when 80% of model's max input tokens     # is reached or when 100 messages is reached (whichever comes first)     [("fraction", 0.8), ("messages", 100)]      # Trigger when tokens >= 4000 AND messages >= 10     {"tokens": 4000, "messages": 10}      # Trigger when (tokens >= 5000 AND messages >= 3) OR     # (tokens >= 3000 AND messages >= 6)     [{"tokens": 5000, "messages": 3}, {"tokens": 3000, "messages": 6}]     ```      See [`ContextSize`][langchain.agents.middleware.summarization.ContextSize]     for more details. (default: `None`) |
| `keep` | `ContextSize` | No | Context retention policy applied after summarization.  Provide a [`ContextSize`][langchain.agents.middleware.summarization.ContextSize] tuple to specify how much history to preserve.  Defaults to keeping the most recent `20` messages.  Does not support multiple values like `trigger`.  !!! example      ```python     # Keep the most recent 20 messages     ("messages", 20)      # Keep the most recent 3000 tokens     ("tokens", 3000)      # Keep the most recent 30% of the model's max input tokens     ("fraction", 0.3)     ``` (default: `('messages', _DEFAULT_MESSAGES_TO_KEEP)`) |
| `token_counter` | `TokenCounter` | No | Function to count tokens in messages. (default: `count_tokens_approximately`) |
| `summary_prompt` | `str` | No | Prompt template for generating summaries. (default: `DEFAULT_SUMMARY_PROMPT`) |
| `trim_tokens_to_summarize` | `int \| None` | No | Maximum tokens to keep when preparing messages for the summarization call.  Pass `None` to skip trimming entirely. (default: `_DEFAULT_TRIM_TOKEN_LIMIT`) |

## Extends

- `AgentMiddleware[AgentState[ResponseT], ContextT, ResponseT]`

## Constructors

```python
__init__(
    self,
    model: str | BaseChatModel,
    *,
    trigger: ContextSize | TriggerClause | list[ContextSize | TriggerClause] | None = None,
    keep: ContextSize = ('messages', _DEFAULT_MESSAGES_TO_KEEP),
    token_counter: TokenCounter = count_tokens_approximately,
    summary_prompt: str = DEFAULT_SUMMARY_PROMPT,
    trim_tokens_to_summarize: int | None = _DEFAULT_TRIM_TOKEN_LIMIT,
    **deprecated_kwargs: Any = {},
) -> None
```

| Name | Type |
|------|------|
| `model` | `str \| BaseChatModel` |
| `trigger` | `ContextSize \| TriggerClause \| list[ContextSize \| TriggerClause] \| None` |
| `keep` | `ContextSize` |
| `token_counter` | `TokenCounter` |
| `summary_prompt` | `str` |
| `trim_tokens_to_summarize` | `int \| None` |

## Properties

- `transformers`
- `model`
- `trigger`
- `keep`
- `token_counter`
- `summary_prompt`
- `trim_tokens_to_summarize`

## Methods

- [`before_model()`](https://reference.langchain.com/python/langchain/agents/middleware/summarization/SummarizationMiddleware/before_model)
- [`abefore_model()`](https://reference.langchain.com/python/langchain/agents/middleware/summarization/SummarizationMiddleware/abefore_model)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/summarization.py#L232)
