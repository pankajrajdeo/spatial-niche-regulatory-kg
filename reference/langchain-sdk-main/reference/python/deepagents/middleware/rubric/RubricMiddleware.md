---
title: "RubricMiddleware"
description: "Middleware that drives self-evaluated iteration against a rubric."
source: "https://reference.langchain.com/python/deepagents/middleware/rubric/RubricMiddleware"
category: "reference"
tags: [reference, deepagents, middleware, rubric, rubricmiddleware]
---

# RubricMiddleware

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/rubric/RubricMiddleware)

Middleware that drives self-evaluated iteration against a rubric.

The middleware activates only when a caller passes a `rubric` on
invocation state. With no rubric, both `before_agent` and `after_agent`
return without modifying state, so the middleware is safe to include
unconditionally in a `create_deep_agent` stack.

!!! note "Observing non-satisfied terminations"

    When grading ends with `failed`, `max_iterations_reached`, or
    `grader_error`, the middleware does **not** mutate the response
    messages. The last `AIMessage` in the agent's output is whatever
    the model produced just before the grader gave up. Callers who
    need to branch on non-satisfied termination must inspect one of:

    - `_rubric_status` on the returned state (or `agent.get_state(...)`
        on a checkpointed thread),
    - the `on_evaluation` callback,
    - the `rubric_evaluation_end` stream event.

    An info log is also emitted when `max_iterations_reached` fires.

## Signature

```python
RubricMiddleware(
    self,
    *,
    model: str | BaseChatModel,
    system_prompt: str | None = None,
    tools: Sequence[BaseTool] | None = None,
    grader_middleware: Sequence[AgentMiddleware[Any, Any, Any]] | None = None,
    grader_context_schema: type[Any] | None = None,
    grader_state_schema: type[AgentState[Any]] | None = None,
    prepare_messages_for_grader: Callable[[list[AnyMessage]], list[AnyMessage]] | None = None,
    build_grader_state: Callable[[RubricState, int], Mapping[str, Any]] | None = None,
    max_iterations: int = 3,
    on_evaluation: Callable[[RubricEvaluation], None] | None = None,
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `model` | `str \| BaseChatModel` | Yes | Model used by the grader sub-agent.  Accepts either a model string like `"provider:model-id"` or a `BaseChatModel` instance. |
| `system_prompt` | `str \| None` | No | Custom grading instructions; falls back to the built-in grader prompt when not set. (default: `None`) |
| `tools` | `Sequence[BaseTool] \| None` | No | Tools the grader may call before producing its `GraderResponse`.  With none, the grader reasons from the transcript alone. (default: `None`) |
| `grader_middleware` | `Sequence[AgentMiddleware[Any, Any, Any]] \| None` | No | Middleware applied to the nested grader agent. (default: `None`) |
| `grader_context_schema` | `type[Any] \| None` | No | Runtime context schema for the nested grader. (default: `None`) |
| `grader_state_schema` | `type[AgentState[Any]] \| None` | No | State schema for the nested grader. Use this when `build_grader_state` adds custom state fields. (default: `None`) |
| `prepare_messages_for_grader` | `Callable[[list[AnyMessage]], list[AnyMessage]] \| None` | No | Optional transform applied to the transcript messages before the SDK builds the sanitized grader payload. (default: `None`) |
| `build_grader_state` | `Callable[[RubricState, int], Mapping[str, Any]] \| None` | No | Optional callback that adds custom fields to the nested grader input. It cannot replace the SDK-owned `messages` field. (default: `None`) |
| `max_iterations` | `int` | No | Maximum grader iterations per rubric attempt; must be a positive integer.  When the cap is reached without a `satisfied` verdict, the agent terminates with status `'max_iterations_reached'` (see the note above on how to observe this). (default: `3`) |
| `on_evaluation` | `Callable[[RubricEvaluation], None] \| None` | No | Optional callback one can invoke with each `RubricEvaluation` after grading.  Exceptions raised by the callback are logged at error level and suppressed; do not use this callback to enforce control flow. (default: `None`) |

## Extends

- `AgentMiddleware[RubricState, ContextT, ResponseT]`

## Constructors

```python
__init__(
    self,
    *,
    model: str | BaseChatModel,
    system_prompt: str | None = None,
    tools: Sequence[BaseTool] | None = None,
    grader_middleware: Sequence[AgentMiddleware[Any, Any, Any]] | None = None,
    grader_context_schema: type[Any] | None = None,
    grader_state_schema: type[AgentState[Any]] | None = None,
    prepare_messages_for_grader: Callable[[list[AnyMessage]], list[AnyMessage]] | None = None,
    build_grader_state: Callable[[RubricState, int], Mapping[str, Any]] | None = None,
    max_iterations: int = 3,
    on_evaluation: Callable[[RubricEvaluation], None] | None = None,
) -> None
```

| Name | Type |
|------|------|
| `model` | `str \| BaseChatModel` |
| `system_prompt` | `str \| None` |
| `tools` | `Sequence[BaseTool] \| None` |
| `grader_middleware` | `Sequence[AgentMiddleware[Any, Any, Any]] \| None` |
| `grader_context_schema` | `type[Any] \| None` |
| `grader_state_schema` | `type[AgentState[Any]] \| None` |
| `prepare_messages_for_grader` | `Callable[[list[AnyMessage]], list[AnyMessage]] \| None` |
| `build_grader_state` | `Callable[[RubricState, int], Mapping[str, Any]] \| None` |
| `max_iterations` | `int` |
| `on_evaluation` | `Callable[[RubricEvaluation], None] \| None` |

## Properties

- `trace_policy`
- `state_schema`
- `max_iterations`

## Methods

- [`before_agent()`](https://reference.langchain.com/python/deepagents/middleware/rubric/RubricMiddleware/before_agent)
- [`abefore_agent()`](https://reference.langchain.com/python/deepagents/middleware/rubric/RubricMiddleware/abefore_agent)
- [`after_agent()`](https://reference.langchain.com/python/deepagents/middleware/rubric/RubricMiddleware/after_agent)
- [`aafter_agent()`](https://reference.langchain.com/python/deepagents/middleware/rubric/RubricMiddleware/aafter_agent)

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/rubric.py#L488)
