---
title: "Runnable"
description: "A unit of work that can be invoked, batched, streamed, transformed and composed."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/Runnable"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnable]
---

# Runnable

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable)

A unit of work that can be invoked, batched, streamed, transformed and composed.

Key Methods
===========

- `invoke`/`ainvoke`: Transforms a single input into an output.
- `batch`/`abatch`: Efficiently transforms multiple inputs into outputs.
- `stream`/`astream`: Streams output from a single input as it's produced.
- `astream_log`: Streams output and selected intermediate results from an
    input.

Built-in optimizations:

- **Batch**: By default, batch runs invoke() in parallel using a thread pool
    executor. Override to optimize batching.

- **Async**: Methods with `'a'` prefix are asynchronous. By default, they execute
    the sync counterpart using asyncio's thread pool.
    Override for native async.

All methods accept an optional config argument, which can be used to configure
execution, add tags and metadata for tracing and debugging etc.

Runnables expose schematic information about their input, output and config via
the `input_schema` property, the `output_schema` property and `config_schema`
method.

Composition
===========

Runnable objects can be composed together to create chains in a declarative way.

Any chain constructed this way will automatically have sync, async, batch, and
streaming support.

The main composition primitives are `RunnableSequence` and `RunnableParallel`.

**`RunnableSequence`** invokes a series of runnables sequentially, with
one Runnable's output serving as the next's input. Construct using
the `|` operator or by passing a list of runnables to `RunnableSequence`.

**`RunnableParallel`** invokes runnables concurrently, providing the same input
to each. Construct it using a dict literal within a sequence or by passing a
dict to `RunnableParallel`.

For example,

```python
from langchain_core.runnables import RunnableLambda

# A RunnableSequence constructed using the `|` operator
sequence = RunnableLambda(lambda x: x + 1) | RunnableLambda(lambda x: x * 2)
sequence.invoke(1)  # 4
sequence.batch([1, 2, 3])  # [4, 6, 8]

# A sequence that contains a RunnableParallel constructed using a dict literal
sequence = RunnableLambda(lambda x: x + 1) | {
    "mul_2": RunnableLambda(lambda x: x * 2),
    "mul_5": RunnableLambda(lambda x: x * 5),
}
sequence.invoke(1)  # {'mul_2': 4, 'mul_5': 10}
```

Standard Methods
================

All `Runnable`s expose additional methods that can be used to modify their
behavior (e.g., add a retry policy, add lifecycle listeners, make them
configurable, etc.).

These methods will work on any `Runnable`, including `Runnable` chains
constructed by composing other `Runnable`s.
See the individual methods for details.

For example,

```python
from langchain_core.runnables import RunnableLambda

import random

def add_one(x: int) -> int:
    return x + 1

def buggy_double(y: int) -> int:
    """Buggy code that will fail 70% of the time"""
    if random.random() > 0.3:
        print('This code failed, and will probably be retried!')  # noqa: T201
        raise ValueError('Triggered buggy code')
    return y * 2

sequence = (
    RunnableLambda(add_one) |
    RunnableLambda(buggy_double).with_retry( # Retry on failure
        stop_after_attempt=10,
        wait_exponential_jitter=False
    )
)

print(sequence.input_schema.model_json_schema()) # Show inferred input schema
print(sequence.output_schema.model_json_schema()) # Show inferred output schema
print(sequence.invoke(2)) # invoke the sequence (note the retry above!!)
```

Debugging and tracing
=====================

As the chains get longer, it can be useful to be able to see intermediate results
to debug and trace the chain.

You can set the global debug flag to True to enable debug output for all chains:

```python
from langchain_core.globals import set_debug

set_debug(True)
```

Alternatively, you can pass existing or custom callbacks to any given chain:

```python
from langchain_core.tracers import ConsoleCallbackHandler

chain.invoke(..., config={"callbacks": [ConsoleCallbackHandler()]})
```

For a UI (and much more) checkout [LangSmith](../../../../../langsmith/home.md).

## Signature

```python
Runnable()
```

## Extends

- `ABC`
- `Generic[Input, Output]`

## Properties

- `name`
- `InputType`
- `OutputType`
- `input_schema`
- `output_schema`
- `config_specs`

## Methods

- [`get_name()`](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/get_name)
- [`get_input_schema()`](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/get_input_schema)
- [`get_input_jsonschema()`](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/get_input_jsonschema)
- [`get_output_schema()`](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/get_output_schema)
- [`get_output_jsonschema()`](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/get_output_jsonschema)
- [`config_schema()`](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/config_schema)
- [`get_config_jsonschema()`](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/get_config_jsonschema)
- [`get_graph()`](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/get_graph)
- [`get_prompts()`](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/get_prompts)
- [`pipe()`](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/pipe)
- [`pick()`](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/pick)
- [`assign()`](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/assign)
- [`invoke()`](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/invoke)
- [`ainvoke()`](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/ainvoke)
- [`batch()`](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/batch)
- [`batch_as_completed()`](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/batch_as_completed)
- [`abatch()`](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/abatch)
- [`abatch_as_completed()`](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/abatch_as_completed)
- [`stream()`](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/stream)
- [`astream()`](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/astream)
- [`astream_log()`](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/astream_log)
- [`astream_events()`](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/astream_events)
- [`stream_events()`](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/stream_events)
- [`transform()`](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/transform)
- [`atransform()`](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/atransform)
- [`bind()`](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/bind)
- [`with_config()`](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/with_config)
- [`with_listeners()`](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/with_listeners)
- [`with_alisteners()`](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/with_alisteners)
- [`with_types()`](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/with_types)
- [`with_retry()`](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/with_retry)
- [`map()`](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/map)
- [`with_fallbacks()`](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/with_fallbacks)
- [`as_tool()`](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/as_tool)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/base.py#L133)
