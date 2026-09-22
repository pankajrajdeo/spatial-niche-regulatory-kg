---
title: "adispatch_custom_event"
description: "Dispatch an adhoc event to the handlers."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/adispatch_custom_event"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, adispatch_custom_event]
---

# adispatch_custom_event

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/adispatch_custom_event)

Dispatch an adhoc event to the handlers.

## Signature

```python
adispatch_custom_event(
    name: str,
    data: Any,
    *,
    config: RunnableConfig | None = None,
) -> None
```

## Description

**Example:**

```python
from langchain_core.callbacks import (
    AsyncCallbackHandler,
    adispatch_custom_event
)
from langchain_core.runnable import RunnableLambda

class CustomCallbackManager(AsyncCallbackHandler):
    async def on_custom_event(
        self,
        name: str,
        data: Any,
        *,
        run_id: UUID,
        tags: list[str] | None = None,
        metadata: dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> None:
        print(f"Received custom event: {name} with data: {data}")

callback = CustomCallbackManager()

async def foo(inputs):
    await adispatch_custom_event("my_event", {"bar": "buzz})
    return inputs

foo_ = RunnableLambda(foo)
await foo_.ainvoke({"a": "1"}, {"callbacks": [CustomCallbackManager()]})
```

Example: Use with astream events

```python
    from langchain_core.callbacks import (
        AsyncCallbackHandler,
        adispatch_custom_event
    )
    from langchain_core.runnable import RunnableLambda

    class CustomCallbackManager(AsyncCallbackHandler):
        async def on_custom_event(
            self,
            name: str,
            data: Any,
            *,
            run_id: UUID,
            tags: list[str] | None = None,
            metadata: dict[str, Any] | None = None,
            **kwargs: Any,
        ) -> None:
            print(f"Received custom event: {name} with data: {data}")

    callback = CustomCallbackManager()

    async def foo(inputs):
        await adispatch_custom_event("event_type_1", {"bar": "buzz})
        await adispatch_custom_event("event_type_2", 5)
        return inputs

    foo_ = RunnableLambda(foo)

    async for event in foo_.ainvoke_stream(
        {"a": "1"},
        version="v2",
        config={"callbacks": [CustomCallbackManager()]}
    ):
        print(event)
```

!!! warning

    If using python 3.10 and async, you MUST specify the `config` parameter or the
    function will raise an error. This is due to a limitation in asyncio for python
    3.10 that prevents LangChain from automatically propagating the config object on
    the user's behalf.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `name` | `str` | Yes | The name of the adhoc event. |
| `data` | `Any` | Yes | The data for the adhoc event.  Free form data. Ideally should be JSON serializable to avoid serialization issues downstream, but this is not enforced. |
| `config` | `RunnableConfig \| None` | No | Optional config object.  Mirrors the async API but not strictly needed. (default: `None`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/manager.py#L2614)
