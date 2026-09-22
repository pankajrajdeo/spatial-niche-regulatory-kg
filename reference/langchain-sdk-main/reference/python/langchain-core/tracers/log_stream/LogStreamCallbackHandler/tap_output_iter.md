---
title: "tap_output_iter"
description: "Tap an output iterator to stream its values to the log."
source: "https://reference.langchain.com/python/langchain-core/tracers/log_stream/LogStreamCallbackHandler/tap_output_iter"
category: "reference"
tags: [reference, langchain-core, tracers, log_stream, logstreamcallbackhandler, tap_output_iter]
---

# tap_output_iter

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/log_stream/LogStreamCallbackHandler/tap_output_iter)

Tap an output iterator to stream its values to the log.

## Signature

```python
tap_output_iter(
    self,
    run_id: UUID,
    output: Iterator[T],
) -> Iterator[T]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `run_id` | `UUID` | Yes | The ID of the run. |
| `output` | `Iterator[T]` | Yes | The output iterator. |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/tracers/log_stream.py#L355)
