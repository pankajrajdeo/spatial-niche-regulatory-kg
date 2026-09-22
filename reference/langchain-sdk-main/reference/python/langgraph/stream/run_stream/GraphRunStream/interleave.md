---
title: "interleave"
description: "Iterate multiple projections in arrival order, yielding (name, item)."
source: "https://reference.langchain.com/python/langgraph/stream/run_stream/GraphRunStream/interleave"
category: "reference"
tags: [reference, langgraph, stream, run_stream, graphrunstream, interleave]
---

# interleave

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/stream/run_stream/GraphRunStream/interleave)

Iterate multiple projections in arrival order, yielding ``(name, item)``.

Items are ordered by a monotonic push stamp assigned when each
transformer pushes into its `StreamChannel`. This gives strict
arrival ordering across projections, unlike round-robin.

## Signature

```python
interleave(
    self,
    *names: str = (),
) -> Iterator[tuple[str, Any]]
```

## Description

Each named channel is locked for the duration of iteration and
released when the generator completes, is closed, or raises.
Channels cannot be subscribed concurrently — use `.tee(n)` if
you need fan-out.

**Example:**

```python
for name, item in run.interleave("messages", "values"):
    if name == "messages":
        print("msg:", item)
    else:
        print("val:", item)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `*names` | `str` | No | Projection keys to interleave. Must match keys in ``extensions``. (default: `()`) |

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/stream/run_stream.py#L221)
