---
title: "validate_interleave_channels"
description: "Reject reserved protocol channel names before they hit the fallback."
source: "https://reference.langchain.com/python/langgraph-sdk/stream/decoders/validate_interleave_channels"
category: "reference"
tags: [reference, langgraph-sdk, stream, decoders, validate_interleave_channels]
---

# validate_interleave_channels

> **Function** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/stream/decoders/validate_interleave_channels)

Reject reserved protocol channel names before they hit the fallback.

Genuine extension names pass through untouched; only names that
``infer_channel`` treats as built-in methods without an interleave decoder
are rejected, so a typo'd or unsupported protocol channel surfaces an error
instead of an empty stream.

## Signature

```python
validate_interleave_channels(
    channels: list[str],
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/stream/decoders.py#L34)
