---
title: "RunnableWithFallbacks"
description: "Runnable that can fallback to other Runnable objects if it fails."
source: "https://reference.langchain.com/python/langchain-core/runnables/fallbacks/RunnableWithFallbacks"
category: "reference"
tags: [reference, langchain-core, runnables, fallbacks, runnablewithfallbacks]
---

# RunnableWithFallbacks

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/fallbacks/RunnableWithFallbacks)

`Runnable` that can fallback to other `Runnable` objects if it fails.

External APIs (e.g., APIs for a language model) may at times experience
degraded performance or even downtime.

In these cases, it can be useful to have a fallback `Runnable` that can be
used in place of the original `Runnable` (e.g., fallback to another LLM provider).

Fallbacks can be defined at the level of a single `Runnable`, or at the level
of a chain of `Runnable`s. Fallbacks are tried in order until one succeeds or
all fail.

While you can instantiate a `RunnableWithFallbacks` directly, it is usually
more convenient to use the `with_fallbacks` method on a `Runnable`.

## Signature

```python
RunnableWithFallbacks(
    self,
    *args: Any = (),
    **kwargs: Any = {},
)
```

## Description

**Example:**

```python
from langchain_core.chat_models.openai import ChatOpenAI
from langchain_core.chat_models.anthropic import ChatAnthropic

model = ChatAnthropic(model="claude-sonnet-4-6").with_fallbacks(
    [ChatOpenAI(model="gpt-5.4-mini")]
)
# Will usually use ChatAnthropic, but fallback to ChatOpenAI
# if ChatAnthropic fails.
model.invoke("hello")

# And you can also use fallbacks at the level of a chain.
# Here if both LLM providers fail, we'll fallback to a good hardcoded
# response.

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parser import StrOutputParser
from langchain_core.runnables import RunnableLambda

def when_all_is_lost(inputs):
    return (
        "Looks like our LLM providers are down. "
        "Here's a nice 🦜️ emoji for you instead."
    )

chain_with_fallback = (
    PromptTemplate.from_template("Tell me a joke about {topic}")
    | model
    | StrOutputParser()
).with_fallbacks([RunnableLambda(when_all_is_lost)])
```

## Extends

- `RunnableSerializable[Input, Output]`

## Properties

- `runnable`
- `fallbacks`
- `exceptions_to_handle`
- `exception_key`
- `model_config`
- `InputType`
- `OutputType`
- `config_specs`
- `runnables`

## Methods

- [`get_input_schema()`](https://reference.langchain.com/python/langchain-core/runnables/fallbacks/RunnableWithFallbacks/get_input_schema)
- [`get_output_schema()`](https://reference.langchain.com/python/langchain-core/runnables/fallbacks/RunnableWithFallbacks/get_output_schema)
- [`is_lc_serializable()`](https://reference.langchain.com/python/langchain-core/runnables/fallbacks/RunnableWithFallbacks/is_lc_serializable)
- [`get_lc_namespace()`](https://reference.langchain.com/python/langchain-core/runnables/fallbacks/RunnableWithFallbacks/get_lc_namespace)
- [`invoke()`](https://reference.langchain.com/python/langchain-core/runnables/fallbacks/RunnableWithFallbacks/invoke)
- [`ainvoke()`](https://reference.langchain.com/python/langchain-core/runnables/fallbacks/RunnableWithFallbacks/ainvoke)
- [`batch()`](https://reference.langchain.com/python/langchain-core/runnables/fallbacks/RunnableWithFallbacks/batch)
- [`abatch()`](https://reference.langchain.com/python/langchain-core/runnables/fallbacks/RunnableWithFallbacks/abatch)
- [`stream()`](https://reference.langchain.com/python/langchain-core/runnables/fallbacks/RunnableWithFallbacks/stream)
- [`astream()`](https://reference.langchain.com/python/langchain-core/runnables/fallbacks/RunnableWithFallbacks/astream)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/fallbacks.py#L37)
