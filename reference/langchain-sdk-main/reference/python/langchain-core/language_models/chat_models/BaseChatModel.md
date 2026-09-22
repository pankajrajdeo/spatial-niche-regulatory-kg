---
title: "BaseChatModel"
description: "Base class for chat models."
source: "https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel"
category: "reference"
tags: [reference, langchain-core, language_models, chat_models, basechatmodel]
---

# BaseChatModel

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel)

Base class for chat models.

## Signature

```python
BaseChatModel(
    self,
    *args: Any = (),
    **kwargs: Any = {},
)
```

## Description

**Key imperative methods:**

Methods that actually call the underlying model.

This table provides a brief overview of the main imperative methods. Please see the base `Runnable` reference for full documentation.

| Method                 | Input                                                        | Output                                                     | Description                                                                      |
| ---------------------- | ------------------------------------------------------------ | ---------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `invoke`               | `str` \| `list[dict | tuple | BaseMessage]` \| `PromptValue` | `BaseMessage`                                              | A single chat model call.                                                        |
| `ainvoke`              | `'''`                                                        | `BaseMessage`                                              | Defaults to running `invoke` in an async executor.                               |
| `stream`               | `'''`                                                        | `Iterator[BaseMessageChunk]`                               | Defaults to yielding output of `invoke`.                                         |
| `astream`              | `'''`                                                        | `AsyncIterator[BaseMessageChunk]`                          | Defaults to yielding output of `ainvoke`.                                        |
| `astream_events`       | `'''`                                                        | `AsyncIterator[StreamEvent]`                               | Event types: `on_chat_model_start`, `on_chat_model_stream`, `on_chat_model_end`. |
| `batch`                | `list[''']`                                                  | `list[BaseMessage]`                                        | Defaults to running `invoke` in concurrent threads.                              |
| `abatch`               | `list[''']`                                                  | `list[BaseMessage]`                                        | Defaults to running `ainvoke` in concurrent threads.                             |
| `batch_as_completed`   | `list[''']`                                                  | `Iterator[tuple[int, Union[BaseMessage, Exception]]]`      | Defaults to running `invoke` in concurrent threads.                              |
| `abatch_as_completed`  | `list[''']`                                                  | `AsyncIterator[tuple[int, Union[BaseMessage, Exception]]]` | Defaults to running `ainvoke` in concurrent threads.                             |

**Key declarative methods:**

Methods for creating another `Runnable` using the chat model.

This table provides a brief overview of the main declarative methods. Please see the reference for each method for full documentation.

| Method                       | Description                                                                                |
| ---------------------------- | ------------------------------------------------------------------------------------------ |
| `bind_tools`                 | Create chat model that can call tools.                                                     |
| `with_structured_output`     | Create wrapper that structures model output using schema.                                  |
| `with_retry`                 | Create wrapper that retries model calls on failure.                                        |
| `with_fallbacks`             | Create wrapper that falls back to other models on failure.                                 |
| `configurable_fields`        | Specify init args of the model that can be configured at runtime via the `RunnableConfig`. |
| `configurable_alternatives`  | Specify alternative models which can be swapped in at runtime via the `RunnableConfig`.    |

**Creating custom chat model:**

Custom chat model implementations should inherit from this class.
Please reference the table below for information about which
methods and properties are required or optional for implementations.

| Method/Property                  | Description                                                        | Required          |
| -------------------------------- | ------------------------------------------------------------------ | ----------------- |
| `_generate`                      | Use to generate a chat result from a prompt                        | Required          |
| `_llm_type` (property)           | Used to uniquely identify the type of the model. Used for logging. | Required          |
| `_identifying_params` (property) | Represent model parameterization for tracing purposes.             | Optional          |
| `_stream`                        | Use to implement streaming                                         | Optional          |
| `_agenerate`                     | Use to implement a native async method                             | Optional          |
| `_astream`                       | Use to implement async version of `_stream`                        | Optional          |

## Extends

- `BaseLanguageModel[AIMessage]`
- `ABC`

## Properties

- `rate_limiter`
- `disable_streaming`
- `output_version`
- `profile`
- `model_config`
- `OutputType`

## Methods

- [`invoke()`](https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel/invoke)
- [`ainvoke()`](https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel/ainvoke)
- [`stream()`](https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel/stream)
- [`astream()`](https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel/astream)
- [`stream_events()`](https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel/stream_events)
- [`astream_events()`](https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel/astream_events)
- [`generate()`](https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel/generate)
- [`agenerate()`](https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel/agenerate)
- [`generate_prompt()`](https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel/generate_prompt)
- [`agenerate_prompt()`](https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel/agenerate_prompt)
- [`dict()`](https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel/dict)
- [`asdict()`](https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel/asdict)
- [`bind()`](https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel/bind)
- [`bind_tools()`](https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel/bind_tools)
- [`with_structured_output()`](https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel/with_structured_output)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/language_models/chat_models.py#L284)
