---
title: "MessagesPlaceholder"
description: "Prompt template that assumes variable is already list of messages."
source: "https://reference.langchain.com/python/langchain-core/prompts/chat/MessagesPlaceholder"
category: "reference"
tags: [reference, langchain-core, prompts, chat, messagesplaceholder]
---

# MessagesPlaceholder

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/chat/MessagesPlaceholder)

Prompt template that assumes variable is already list of messages.

A placeholder which can be used to pass in a list of messages.

!!! example "Direct usage"

```python
    from langchain_core.prompts import MessagesPlaceholder

    prompt = MessagesPlaceholder("history")
    prompt.format_messages()  # raises KeyError

    prompt = MessagesPlaceholder("history", optional=True)
    prompt.format_messages()  # returns empty list []

    prompt.format_messages(
        history=[
            ("system", "You are an AI assistant."),
            ("human", "Hello!"),
        ]
    )
    # -> [
    #     SystemMessage(content="You are an AI assistant."),
    #     HumanMessage(content="Hello!"),
    # ]
```

!!! example "Building a prompt with chat history"

```python
    from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant."),
            MessagesPlaceholder("history"),
            ("human", "{question}"),
        ]
    )
    prompt.invoke(
        {
            "history": [("human", "what's 5 + 2"), ("ai", "5 + 2 is 7")],
            "question": "now multiply that by 4",
        }
    )
    # -> ChatPromptValue(messages=[
    #     SystemMessage(content="You are a helpful assistant."),
    #     HumanMessage(content="what's 5 + 2"),
    #     AIMessage(content="5 + 2 is 7"),
    #     HumanMessage(content="now multiply that by 4"),
    # ])
```

!!! example "Limiting the number of messages"

```python
    from langchain_core.prompts import MessagesPlaceholder

    prompt = MessagesPlaceholder("history", n_messages=1)

    prompt.format_messages(
        history=[
            ("system", "You are an AI assistant."),
            ("human", "Hello!"),
        ]
    )
    # -> [
    #     HumanMessage(content="Hello!"),
    # ]
```

## Signature

```python
MessagesPlaceholder(
    self,
    variable_name: str,
    *,
    optional: bool = False,
    **kwargs: Any = {},
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `variable_name` | `str` | Yes | Name of variable to use as messages. |
| `optional` | `bool` | No | Whether `format_messages` must be provided.  If `True` format_messages can be called with no arguments and will return an empty list.  If `False` then a named argument with name `variable_name` must be passed in, even if the value is an empty list. (default: `False`) |

## Extends

- `BaseMessagePromptTemplate`

## Constructors

```python
__init__(
    self,
    variable_name: str,
    *,
    optional: bool = False,
    **kwargs: Any = {},
) -> None
```

| Name | Type |
|------|------|
| `variable_name` | `str` |
| `optional` | `bool` |

## Properties

- `variable_name`
- `optional`
- `n_messages`
- `input_variables`

## Methods

- [`format_messages()`](https://reference.langchain.com/python/langchain-core/prompts/chat/MessagesPlaceholder/format_messages)
- [`pretty_repr()`](https://reference.langchain.com/python/langchain-core/prompts/chat/MessagesPlaceholder/pretty_repr)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/prompts/chat.py#L53)
