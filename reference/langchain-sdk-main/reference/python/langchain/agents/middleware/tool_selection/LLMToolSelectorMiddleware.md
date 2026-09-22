---
title: "LLMToolSelectorMiddleware"
description: "Uses an LLM to select relevant tools before calling the main model."
source: "https://reference.langchain.com/python/langchain/agents/middleware/tool_selection/LLMToolSelectorMiddleware"
category: "reference"
tags: [reference, langchain, agents, middleware, tool_selection, llmtoolselectormiddleware]
---

# LLMToolSelectorMiddleware

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/tool_selection/LLMToolSelectorMiddleware)

Uses an LLM to select relevant tools before calling the main model.

When an agent has many tools available, this middleware filters them down
to only the most relevant ones for the user's query. This reduces token usage
and helps the main model focus on the right tools.

## Signature

```python
LLMToolSelectorMiddleware(
    self,
    *,
    model: str | BaseChatModel | None = None,
    system_prompt: str = DEFAULT_SYSTEM_PROMPT,
    max_tools: int | None = None,
    always_include: list[str] | None = None,
    max_retries: int = 1,
    on_parsing_failure: OnParsingFailure = 'error',
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `model` | `str \| BaseChatModel \| None` | No | Model to use for selection.  If not provided, uses the agent's main model.  Can be a model identifier string or `BaseChatModel` instance. (default: `None`) |
| `system_prompt` | `str` | No | Instructions for the selection model. (default: `DEFAULT_SYSTEM_PROMPT`) |
| `max_tools` | `int \| None` | No | Maximum number of tools to select.  If the model selects more, only the first `max_tools` will be used.  If not specified, there is no limit. (default: `None`) |
| `always_include` | `list[str] \| None` | No | Tool names to always include regardless of selection.  These do not count against the `max_tools` limit. (default: `None`) |
| `max_retries` | `int` | No | Maximum number of retry attempts after the initial call if the selection model returns a malformed response (not a dict with a `tools` list).  Must be `>= 0`. (default: `1`) |
| `on_parsing_failure` | `OnParsingFailure` | No | Behavior once `max_retries` is exhausted and the response is still malformed.  Options:  - `'error'` (default): Raise a `ValueError`. - `'none'`: Select no tools. - `'all'`: Select every available tool. - A `list[str]` of tool names to fall back to. - A callable that takes the last (malformed) response and returns     the tool names to use.  Unlike a normal model selection, the fallback tools are not capped by `max_tools` -- it's an already-deliberate choice, not raw model output that needs bounding. (default: `'error'`) |

## Extends

- `AgentMiddleware[AgentState[ResponseT], ContextT, ResponseT]`

## Constructors

```python
__init__(
    self,
    *,
    model: str | BaseChatModel | None = None,
    system_prompt: str = DEFAULT_SYSTEM_PROMPT,
    max_tools: int | None = None,
    always_include: list[str] | None = None,
    max_retries: int = 1,
    on_parsing_failure: OnParsingFailure = 'error',
) -> None
```

| Name | Type |
|------|------|
| `model` | `str \| BaseChatModel \| None` |
| `system_prompt` | `str` |
| `max_tools` | `int \| None` |
| `always_include` | `list[str] \| None` |
| `max_retries` | `int` |
| `on_parsing_failure` | `OnParsingFailure` |

## Properties

- `transformers`
- `system_prompt`
- `max_tools`
- `always_include`
- `max_retries`
- `on_parsing_failure`
- `model`

## Methods

- [`wrap_model_call()`](https://reference.langchain.com/python/langchain/agents/middleware/tool_selection/LLMToolSelectorMiddleware/wrap_model_call)
- [`awrap_model_call()`](https://reference.langchain.com/python/langchain/agents/middleware/tool_selection/LLMToolSelectorMiddleware/awrap_model_call)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/tool_selection.py#L123)
