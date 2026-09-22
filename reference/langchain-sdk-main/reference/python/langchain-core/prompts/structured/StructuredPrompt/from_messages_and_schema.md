---
title: "from_messages_and_schema"
description: "Create a chat prompt template from a variety of message formats."
source: "https://reference.langchain.com/python/langchain-core/prompts/structured/StructuredPrompt/from_messages_and_schema"
category: "reference"
tags: [reference, langchain-core, prompts, structured, structuredprompt, from_messages_and_schema]
---

# from_messages_and_schema

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/structured/StructuredPrompt/from_messages_and_schema)

Create a chat prompt template from a variety of message formats.

## Signature

```python
from_messages_and_schema(
    cls,
    messages: Sequence[MessageLikeRepresentation],
    schema: dict[str, Any] | type,
    **kwargs: Any = {},
) -> ChatPromptTemplate
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `messages` | `Sequence[MessageLikeRepresentation]` | Yes | Sequence of message representations.  A message can be represented using the following formats:  1. `BaseMessagePromptTemplate` 2. `BaseMessage` 3. 2-tuple of `(message type, template)`; e.g.,     `("human", "{user_input}")` 4. 2-tuple of `(message class, template)` 5. A string which is shorthand for `("human", template)`; e.g.,     `"{user_input}"` |
| `schema` | `dict[str, Any] \| type` | Yes | A dictionary representation of function call, or a Pydantic model. |
| `**kwargs` | `Any` | No | Any additional kwargs to pass through to `ChatModel.with_structured_output(schema, **kwargs)`. (default: `{}`) |

## Returns

`ChatPromptTemplate`

A structured prompt template

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/prompts/structured.py#L96)
