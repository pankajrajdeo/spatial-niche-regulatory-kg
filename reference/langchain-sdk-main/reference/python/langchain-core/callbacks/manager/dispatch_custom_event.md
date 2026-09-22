---
title: "dispatch_custom_event"
description: "Dispatch an adhoc event."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/dispatch_custom_event"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, dispatch_custom_event]
---

# dispatch_custom_event

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/dispatch_custom_event)

Dispatch an adhoc event.

## Signature

```python
dispatch_custom_event(
    name: str,
    data: Any,
    *,
    config: RunnableConfig | None = None,
) -> None
```

## Description

**Example:**

```python
from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.callbacks import dispatch_custom_event
from langchain_core.runnable import RunnableLambda

class CustomCallbackManager(BaseCallbackHandler):
    def on_custom_event(
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

def foo(inputs):
    dispatch_custom_event("my_event", {"bar": "buzz})
    return inputs

foo_ = RunnableLambda(foo)
foo_.invoke({"a": "1"}, {"callbacks": [CustomCallbackManager()]})
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `name` | `str` | Yes | The name of the adhoc event. |
| `data` | `Any` | Yes | The data for the adhoc event.  Free form data. Ideally should be JSON serializable to avoid serialization issues downstream, but this is not enforced. |
| `config` | `RunnableConfig \| None` | No | Optional config object.  Mirrors the async API but not strictly needed. (default: `None`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/manager.py#L2739)
