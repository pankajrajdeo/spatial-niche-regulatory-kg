---
title: "create_summarization_middleware"
description: "Create a Deep Agents SummarizationMiddleware with model-aware defaults."
source: "https://reference.langchain.com/python/deepagents/middleware/summarization/create_summarization_middleware"
category: "reference"
tags: [reference, deepagents, middleware, summarization, create_summarization_middleware]
---

# create_summarization_middleware

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/summarization/create_summarization_middleware)

Create a Deep Agents `SummarizationMiddleware` with model-aware defaults.

## Why this exists in `deepagents`

The Deep Agents `SummarizationMiddleware` wraps
`langchain.agents.middleware.SummarizationMiddleware` to add behavior
long-running, file-aware agents need. Prefer LangChain's middleware
directly if none of the below apply:

- **Backend offload of evicted history.** Evicted messages are appended
    to `/conversation_history/{session_id}.md` (default path) on the
    configured backend before the summary replaces them, and the
    summary embeds that path so the agent can re-open it via
    `read_file` when `FilesystemMiddleware` is registered. LangChain
    drops evicted messages with no recovery path.
- **Pre-summarization tool-arg truncation.** Large `write_file` /
    `edit_file` arguments in older messages are clipped at a lower
    threshold than full compaction, often reclaiming enough context
    to skip summarizing. Configured via `truncate_args_settings`.
- **`ContextOverflowError` fallback.** On a provider over-budget
    rejection the middleware summarizes and retries instead of
    bubbling the error up.
- **Non-mutating message state.** Summarization is tracked in a
    private `_summarization_event` field via `wrap_model_call`,
    leaving `state["messages"]` intact. LangChain rewrites it with
    `RemoveMessage(id=REMOVE_ALL_MESSAGES)` from `before_model`.
    Preserving the raw log enables replay, evals, and shared state
    with `SummarizationToolMiddleware`'s `compact_conversation` tool.
- **Auto-selected trigger/keep thresholds.** LangChain accepts
    fraction-based thresholds but defaults to `trigger=None` and
    `keep=("messages", 20)`. This factory picks fraction-based
    defaults from the model's profile when `max_input_tokens` is
    exposed, falling back to fixed counts otherwise — see
    [`compute_summarization_defaults`][deepagents.middleware.summarization.compute_summarization_defaults].

## Signature

```python
create_summarization_middleware(
    model: BaseChatModel,
    backend: BackendProtocol,
    *,
    summary_prompt: str = DEEPAGENTS_DEFAULT_SUMMARY_PROMPT,
    trim_tokens_to_summarize: int | None = None,
    token_counter: TokenCounter = count_tokens_approximately,
) -> _DeepAgentsSummarizationMiddleware
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `model` | `BaseChatModel` | Yes | Resolved `BaseChatModel` instance.  Use `resolve_model()` first if needed for model strings. |
| `backend` | `BackendProtocol` | Yes | Backend instance for persisting conversation history. |
| `summary_prompt` | `str` | No | Prompt template for generating summaries. (default: `DEEPAGENTS_DEFAULT_SUMMARY_PROMPT`) |
| `trim_tokens_to_summarize` | `int \| None` | No | Max tokens to include when generating summary. (default: `None`) |
| `token_counter` | `TokenCounter` | No | Function to count tokens in messages. (default: `count_tokens_approximately`) |

## Returns

`_DeepAgentsSummarizationMiddleware`

Configured `SummarizationMiddleware` instance.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/summarization.py#L1757)
