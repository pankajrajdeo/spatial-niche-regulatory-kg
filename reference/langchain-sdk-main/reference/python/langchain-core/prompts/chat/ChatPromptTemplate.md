---
title: "ChatPromptTemplate"
description: "Prompt template for chat models."
source: "https://reference.langchain.com/python/langchain-core/prompts/chat/ChatPromptTemplate"
category: "reference"
tags: [reference, langchain-core, prompts, chat, chatprompttemplate]
---

# ChatPromptTemplate

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/chat/ChatPromptTemplate)

Prompt template for chat models.

Use to create flexible templated prompts for chat models.

!!! example

```python
    from langchain_core.prompts import ChatPromptTemplate

    template = ChatPromptTemplate(
        [
            ("system", "You are a helpful AI bot. Your name is {name}."),
            ("human", "Hello, how are you doing?"),
            ("ai", "I'm doing well, thanks!"),
            ("human", "{user_input}"),
        ]
    )

    prompt_value = template.invoke(
        {
            "name": "Bob",
            "user_input": "What is your name?",
        }
    )
    # Output:
    # ChatPromptValue(
    #    messages=[
    #        SystemMessage(content='You are a helpful AI bot. Your name is Bob.'),
    #        HumanMessage(content='Hello, how are you doing?'),
    #        AIMessage(content="I'm doing well, thanks!"),
    #        HumanMessage(content='What is your name?')
    #    ]
    # )
```

!!! note "Messages Placeholder"

```python
    # In addition to Human/AI/Tool/Function messages,
    # you can initialize the template with a MessagesPlaceholder
    # either using the class directly or with the shorthand tuple syntax:

    template = ChatPromptTemplate(
        [
            ("system", "You are a helpful AI bot."),
            # Means the template will receive an optional list of messages under
            # the "conversation" key
            ("placeholder", "{conversation}"),
            # Equivalently:
            # MessagesPlaceholder(variable_name="conversation", optional=True)
        ]
    )

    prompt_value = template.invoke(
        {
            "conversation": [
                ("human", "Hi!"),
                ("ai", "How can I assist you today?"),
                ("human", "Can you make me an ice cream sundae?"),
                ("ai", "No."),
            ]
        }
    )

    # Output:
    # ChatPromptValue(
    #    messages=[
    #        SystemMessage(content='You are a helpful AI bot.'),
    #        HumanMessage(content='Hi!'),
    #        AIMessage(content='How can I assist you today?'),
    #        HumanMessage(content='Can you make me an ice cream sundae?'),
    #        AIMessage(content='No.'),
    #    ]
    # )
```

!!! note "Single-variable template"

    If your prompt has only a single input variable (i.e., one instance of
    `'{variable_nams}'`), and you invoke the template with a non-dict object, the
    prompt template will inject the provided argument into that variable location.

```python
    from langchain_core.prompts import ChatPromptTemplate

    template = ChatPromptTemplate(
        [
            ("system", "You are a helpful AI bot. Your name is Carl."),
            ("human", "{user_input}"),
        ]
    )

    prompt_value = template.invoke("Hello, there!")
    # Equivalent to
    # prompt_value = template.invoke({"user_input": "Hello, there!"})

    # Output:
    #  ChatPromptValue(
    #     messages=[
    #         SystemMessage(content='You are a helpful AI bot. Your name is Carl.'),
    #         HumanMessage(content='Hello, there!'),
    #     ]
    # )
```

## Signature

```python
ChatPromptTemplate(
    self,
    messages: Sequence[MessageLikeRepresentation],
    *,
    template_format: PromptTemplateFormat = 'f-string',
    **kwargs: Any = {},
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `messages` | `Sequence[MessageLikeRepresentation]` | Yes | Sequence of message representations.  A message can be represented using the following formats:  1. `BaseMessagePromptTemplate` 2. `BaseMessage` 3. 2-tuple of `(message type, template)`; e.g.,     `('human', '{user_input}')` 4. 2-tuple of `(message class, template)` 5. A string which is shorthand for `('human', template)`; e.g.,     `'{user_input}'` |
| `template_format` | `PromptTemplateFormat` | No | Format of the template. (default: `'f-string'`) |
| `**kwargs` | `Any` | No | Additional keyword arguments passed to `BasePromptTemplate`, including (but not limited to):  - `input_variables`: A list of the names of the variables whose values     are required as inputs to the prompt. - `optional_variables`: A list of the names of the variables for     placeholder or `MessagePlaceholder` that are optional.      These variables are auto inferred from the prompt and user need not     provide them.  - `partial_variables`: A dictionary of the partial variables the prompt     template carries.      Partial variables populate the template so that you don't need to     pass them in every time you call the prompt.  - `validate_template`: Whether to validate the template. - `input_types`: A dictionary of the types of the variables the prompt     template expects.      If not provided, all variables are assumed to be strings. (default: `{}`) |

## Extends

- `BaseChatPromptTemplate`

## Constructors

```python
__init__(
    self,
    messages: Sequence[MessageLikeRepresentation],
    *,
    template_format: PromptTemplateFormat = 'f-string',
    **kwargs: Any = {},
) -> None
```

| Name | Type |
|------|------|
| `messages` | `Sequence[MessageLikeRepresentation]` |
| `template_format` | `PromptTemplateFormat` |

## Properties

- `messages`
- `validate_template`

## Methods

- [`get_lc_namespace()`](https://reference.langchain.com/python/langchain-core/prompts/chat/ChatPromptTemplate/get_lc_namespace)
- [`validate_input_variables()`](https://reference.langchain.com/python/langchain-core/prompts/chat/ChatPromptTemplate/validate_input_variables)
- [`from_template()`](https://reference.langchain.com/python/langchain-core/prompts/chat/ChatPromptTemplate/from_template)
- [`from_messages()`](https://reference.langchain.com/python/langchain-core/prompts/chat/ChatPromptTemplate/from_messages)
- [`format_messages()`](https://reference.langchain.com/python/langchain-core/prompts/chat/ChatPromptTemplate/format_messages)
- [`aformat_messages()`](https://reference.langchain.com/python/langchain-core/prompts/chat/ChatPromptTemplate/aformat_messages)
- [`partial()`](https://reference.langchain.com/python/langchain-core/prompts/chat/ChatPromptTemplate/partial)
- [`append()`](https://reference.langchain.com/python/langchain-core/prompts/chat/ChatPromptTemplate/append)
- [`extend()`](https://reference.langchain.com/python/langchain-core/prompts/chat/ChatPromptTemplate/extend)
- [`save()`](https://reference.langchain.com/python/langchain-core/prompts/chat/ChatPromptTemplate/save)
- [`pretty_repr()`](https://reference.langchain.com/python/langchain-core/prompts/chat/ChatPromptTemplate/pretty_repr)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/prompts/chat.py#L794)
