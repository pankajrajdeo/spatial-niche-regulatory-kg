---
title: "RunnableWithMessageHistory"
description: "Runnable that manages chat message history for another Runnable."
source: "https://reference.langchain.com/python/langchain-core/runnables/history/RunnableWithMessageHistory"
category: "reference"
tags: [reference, langchain-core, runnables, history, runnablewithmessagehistory]
---

# RunnableWithMessageHistory

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/history/RunnableWithMessageHistory)

`Runnable` that manages chat message history for another `Runnable`.

A chat message history is a sequence of messages that represent a conversation.

`RunnableWithMessageHistory` wraps another `Runnable` and manages the chat message
history for it; it is responsible for reading and updating the chat message
history.

The formats supported for the inputs and outputs of the wrapped `Runnable`
are described below.

`RunnableWithMessageHistory` must always be called with a config that contains
the appropriate parameters for the chat message history factory.

By default, the `Runnable` is expected to take a single configuration parameter
called `session_id` which is a string. This parameter is used to create a new
or look up an existing chat message history that matches the given `session_id`.

In this case, the invocation would look like this:

`with_history.invoke(..., config={"configurable": {"session_id": "bar"}})`
; e.g., `{"configurable": {"session_id": "<SESSION_ID>"}}`.

The configuration can be customized by passing in a list of
`ConfigurableFieldSpec` objects to the `history_factory_config` parameter (see
example below).

In the examples, we will use a chat message history with an in-memory
implementation to make it easy to experiment and see the results.

For production use cases, you will want to use a persistent implementation
of chat message history, such as `RedisChatMessageHistory`.

Example: Chat message history with an in-memory implementation for testing.

```python
    from operator import itemgetter

    from langchain_openai.chat_models import ChatOpenAI

    from langchain_core.chat_history import BaseChatMessageHistory
    from langchain_core.documents import Document
    from langchain_core.messages import BaseMessage, AIMessage
    from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
    from pydantic import BaseModel, Field
    from langchain_core.runnables import (
        RunnableLambda,
        ConfigurableFieldSpec,
        RunnablePassthrough,
    )
    from langchain_core.runnables.history import RunnableWithMessageHistory

    class InMemoryHistory(BaseChatMessageHistory, BaseModel):
        """In memory implementation of chat message history."""

        messages: list[BaseMessage] = Field(default_factory=list)

        def add_messages(self, messages: list[BaseMessage]) -> None:
            """Add a list of messages to the store"""
            self.messages.extend(messages)

        def clear(self) -> None:
            self.messages = []

    # Here we use a global variable to store the chat message history.
    # This will make it easier to inspect it to see the underlying results.
    store = {}

    def get_by_session_id(session_id: str) -> BaseChatMessageHistory:
        if session_id not in store:
            store[session_id] = InMemoryHistory()
        return store[session_id]

    history = get_by_session_id("1")
    history.add_message(AIMessage(content="hello"))
    print(store)  # noqa: T201

```

Example where the wrapped `Runnable` takes a dictionary input:

```python
    from typing import Optional

    from langchain_anthropic import ChatAnthropic
    from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
    from langchain_core.runnables.history import RunnableWithMessageHistory

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You're an assistant who's good at {ability}"),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{question}"),
        ]
    )

    chain = prompt | ChatAnthropic(model="claude-2")

    chain_with_history = RunnableWithMessageHistory(
        chain,
        # Uses the get_by_session_id function defined in the example
        # above.
        get_by_session_id,
        input_messages_key="question",
        history_messages_key="history",
    )

    print(
        chain_with_history.invoke(  # noqa: T201
            {"ability": "math", "question": "What does cosine mean?"},
            config={"configurable": {"session_id": "foo"}},
        )
    )

    # Uses the store defined in the example above.
    print(store)  # noqa: T201

    print(
        chain_with_history.invoke(  # noqa: T201
            {"ability": "math", "question": "What's its inverse"},
            config={"configurable": {"session_id": "foo"}},
        )
    )

    print(store)  # noqa: T201
```

Example where the session factory takes two keys (`user_id` and `conversation_id`):

```python
    store = {}

    def get_session_history(
        user_id: str, conversation_id: str
    ) -> BaseChatMessageHistory:
        if (user_id, conversation_id) not in store:
            store[(user_id, conversation_id)] = InMemoryHistory()
        return store[(user_id, conversation_id)]

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You're an assistant who's good at {ability}"),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{question}"),
        ]
    )

    chain = prompt | ChatAnthropic(model="claude-2")

    with_message_history = RunnableWithMessageHistory(
        chain,
        get_session_history=get_session_history,
        input_messages_key="question",
        history_messages_key="history",
        history_factory_config=[
            ConfigurableFieldSpec(
                id="user_id",
                annotation=str,
                name="User ID",
                description="Unique identifier for the user.",
                default="",
                is_shared=True,
            ),
            ConfigurableFieldSpec(
                id="conversation_id",
                annotation=str,
                name="Conversation ID",
                description="Unique identifier for the conversation.",
                default="",
                is_shared=True,
            ),
        ],
    )

    with_message_history.invoke(
        {"ability": "math", "question": "What does cosine mean?"},
        config={"configurable": {"user_id": "123", "conversation_id": "1"}},
    )
```

## Signature

```python
RunnableWithMessageHistory(
    self,
    runnable: Runnable[list[BaseMessage], str | BaseMessage | MessagesOrDictWithMessages] | Runnable[dict[str, Any], str | BaseMessage | MessagesOrDictWithMessages] | LanguageModelLike,
    get_session_history: GetSessionHistoryCallable,
    *,
    input_messages_key: str | None = None,
    output_messages_key: str | None = None,
    history_messages_key: str | None = None,
    history_factory_config: Sequence[ConfigurableFieldSpec] | None = None,
    **kwargs: Any = {},
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `runnable` | `Runnable[list[BaseMessage], str \| BaseMessage \| MessagesOrDictWithMessages] \| Runnable[dict[str, Any], str \| BaseMessage \| MessagesOrDictWithMessages] \| LanguageModelLike` | Yes | The base `Runnable` to be wrapped.  Must take as input one of:  1. A list of `BaseMessage` 2. A `dict` with one key for all messages 3. A `dict` with one key for the current input string/message(s) and     a separate key for historical messages. If the input key points     to a string, it will be treated as a `HumanMessage` in history.  Must return as output one of:  1. A string which can be treated as an `AIMessage` 2. A `BaseMessage` or sequence of `BaseMessage` 3. A `dict` with a key for a `BaseMessage` or sequence of     `BaseMessage` |
| `get_session_history` | `GetSessionHistoryCallable` | Yes | Function that returns a new `BaseChatMessageHistory`.  This function should either take a single positional argument `session_id` of type string and return a corresponding chat message history instance.  ```python def get_session_history(     session_id: str, *, user_id: str \| None = None ) -> BaseChatMessageHistory: ... ```  Or it should take keyword arguments that match the keys of `session_history_config_specs` and return a corresponding chat message history instance.  ```python def get_session_history(     *,     user_id: str,     thread_id: str, ) -> BaseChatMessageHistory: ... ``` |
| `input_messages_key` | `str \| None` | No | Must be specified if the base runnable accepts a `dict` as input. (default: `None`) |
| `output_messages_key` | `str \| None` | No | Must be specified if the base runnable returns a `dict` as output. (default: `None`) |
| `history_messages_key` | `str \| None` | No | Must be specified if the base runnable accepts a `dict` as input and expects a separate key for historical messages. (default: `None`) |
| `history_factory_config` | `Sequence[ConfigurableFieldSpec] \| None` | No | Configure fields that should be passed to the chat history factory. See `ConfigurableFieldSpec` for more details.  Specifying these allows you to pass multiple config keys into the `get_session_history` factory. (default: `None`) |
| `**kwargs` | `Any` | No | Arbitrary additional kwargs to pass to parent class `RunnableBindingBase` init. (default: `{}`) |

## Extends

- `RunnableBindingBase[Any, Any]`

## Constructors

```python
__init__(
    self,
    runnable: Runnable[list[BaseMessage], str | BaseMessage | MessagesOrDictWithMessages] | Runnable[dict[str, Any], str | BaseMessage | MessagesOrDictWithMessages] | LanguageModelLike,
    get_session_history: GetSessionHistoryCallable,
    *,
    input_messages_key: str | None = None,
    output_messages_key: str | None = None,
    history_messages_key: str | None = None,
    history_factory_config: Sequence[ConfigurableFieldSpec] | None = None,
    **kwargs: Any = {},
) -> None
```

| Name | Type |
|------|------|
| `runnable` | `Runnable[list[BaseMessage], str \| BaseMessage \| MessagesOrDictWithMessages] \| Runnable[dict[str, Any], str \| BaseMessage \| MessagesOrDictWithMessages] \| LanguageModelLike` |
| `get_session_history` | `GetSessionHistoryCallable` |
| `input_messages_key` | `str \| None` |
| `output_messages_key` | `str \| None` |
| `history_messages_key` | `str \| None` |
| `history_factory_config` | `Sequence[ConfigurableFieldSpec] \| None` |

## Properties

- `get_session_history`
- `input_messages_key`
- `output_messages_key`
- `history_messages_key`
- `history_factory_config`
- `config_specs`
- `OutputType`

## Methods

- [`get_input_schema()`](https://reference.langchain.com/python/langchain-core/runnables/history/RunnableWithMessageHistory/get_input_schema)
- [`get_output_schema()`](https://reference.langchain.com/python/langchain-core/runnables/history/RunnableWithMessageHistory/get_output_schema)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/history.py#L39)
