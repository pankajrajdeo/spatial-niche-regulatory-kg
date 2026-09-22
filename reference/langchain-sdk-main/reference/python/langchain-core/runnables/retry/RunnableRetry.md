---
title: "RunnableRetry"
description: "Retry a Runnable if it fails."
source: "https://reference.langchain.com/python/langchain-core/runnables/retry/RunnableRetry"
category: "reference"
tags: [reference, langchain-core, runnables, retry, runnableretry]
---

# RunnableRetry

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/retry/RunnableRetry)

Retry a Runnable if it fails.

RunnableRetry can be used to add retry logic to any object
that subclasses the base Runnable.

Such retries are especially useful for network calls that may fail
due to transient errors.

The RunnableRetry is implemented as a RunnableBinding. The easiest
way to use it is through the `.with_retry()` method on all Runnables.

Example:
Here's an example that uses a RunnableLambda to raise an exception

```python
    import time

    def foo(input) -> None:
        '''Fake function that raises an exception.'''
        raise ValueError(f"Invoking foo failed. At time {time.time()}")

    runnable = RunnableLambda(foo)

    runnable_with_retries = runnable.with_retry(
        retry_if_exception_type=(ValueError,),  # Retry only on ValueError
        wait_exponential_jitter=True,  # Add jitter to the exponential backoff
        stop_after_attempt=2,  # Try twice
        exponential_jitter_params={"initial": 2},  # if desired, customize backoff
    )

    # The method invocation above is equivalent to the longer form below:

    runnable_with_retries = RunnableRetry(
        bound=runnable,
        retry_exception_types=(ValueError,),
        max_attempt_number=2,
        wait_exponential_jitter=True,
        exponential_jitter_params={"initial": 2},
    )
```

This logic can be used to retry any Runnable, including a chain of Runnables,
but in general it's best practice to keep the scope of the retry as small as
possible. For example, if you have a chain of Runnables, you should only retry
the Runnable that is likely to fail, not the entire chain.

## Signature

```python
RunnableRetry(
    self,
    *,
    bound: Runnable[Input, Output],
    kwargs: Mapping[str, Any] | None = None,
    config: RunnableConfig | None = None,
    config_factories: list[Callable[[RunnableConfig], RunnableConfig]] | None = None,
    custom_input_type: type[Input] | BaseModel | None = None,
    custom_output_type: type[Output] | BaseModel | None = None,
    **other_kwargs: Any = {},
)
```

## Description

**Example:**

```python
from langchain_core.chat_models import ChatOpenAI
from langchain_core.prompts import PromptTemplate

template = PromptTemplate.from_template("tell me a joke about {topic}.")
model = ChatOpenAI(temperature=0.5)

# Good
chain = template | model.with_retry()

# Bad
chain = template | model
retryable_chain = chain.with_retry()
```

## Extends

- `RunnableBindingBase[Input, Output]`

## Properties

- `retry_exception_types`
- `wait_exponential_jitter`
- `exponential_jitter_params`
- `max_attempt_number`

## Methods

- [`invoke()`](https://reference.langchain.com/python/langchain-core/runnables/retry/RunnableRetry/invoke)
- [`ainvoke()`](https://reference.langchain.com/python/langchain-core/runnables/retry/RunnableRetry/ainvoke)
- [`batch()`](https://reference.langchain.com/python/langchain-core/runnables/retry/RunnableRetry/batch)
- [`abatch()`](https://reference.langchain.com/python/langchain-core/runnables/retry/RunnableRetry/abatch)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/retry.py#L48)
