---
title: "ExtendedModelResponse"
description: "Model response with an optional 'Command' from 'wrap_model_call' middleware."
source: "https://reference.langchain.com/python/langchain/agents/middleware/types/ExtendedModelResponse"
category: "reference"
tags: [reference, langchain, agents, middleware, types, extendedmodelresponse]
---

# ExtendedModelResponse

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/types/ExtendedModelResponse)

Model response with an optional 'Command' from 'wrap_model_call' middleware.

Use this to return a 'Command' alongside the model response from a
'wrap_model_call' handler. The command is applied as an additional state
update after the model node completes, using the graph's reducers (e.g.
'add_messages' for the 'messages' key).

Because each 'Command' is applied through the reducer, messages in the
command are **added alongside** the model response messages rather than
replacing them. For non-reducer state fields, later commands overwrite
earlier ones (outermost middleware wins over inner).

## Signature

```python
ExtendedModelResponse(
    self,
    model_response: ModelResponse[ResponseT],
    command: Command[Any] | None = None,
)
```

## Extends

- `Generic[ResponseT]`

## Constructors

```python
__init__(
    self,
    model_response: ModelResponse[ResponseT],
    command: Command[Any] | None = None,
) -> None
```

| Name | Type |
|------|------|
| `model_response` | `ModelResponse[ResponseT]` |
| `command` | `Command[Any] \| None` |

## Properties

- `model_response`
- `command`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/types.py#L290)
