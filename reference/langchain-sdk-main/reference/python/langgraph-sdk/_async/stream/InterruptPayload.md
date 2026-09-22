---
title: "InterruptPayload"
description: "Payload surfaced when the server requests human input for a thread."
source: "https://reference.langchain.com/python/langgraph-sdk/_async/stream/InterruptPayload"
category: "reference"
tags: [reference, langgraph-sdk, async, stream, interruptpayload]
---

# InterruptPayload

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_async/stream/InterruptPayload)

Payload surfaced when the server requests human input for a thread.

## Signature

```python
InterruptPayload()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    interrupt_id: str,
    value: Any,
    namespace: list[str],
)
```

| Name | Type |
|------|------|
| `interrupt_id` | `str` |
| `value` | `Any` |
| `namespace` | `list[str]` |

## Properties

- `interrupt_id`
- `value`
- `namespace`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_async/stream.py#L47)
