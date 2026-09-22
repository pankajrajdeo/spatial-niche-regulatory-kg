---
title: "create_metadata_for_update_state_api"
description: "Advance counters_since_delta_snapshot for update_state on a non-fresh thread."
source: "https://reference.langchain.com/python/langgraph/pregel/_checkpoint/create_metadata_for_update_state_api"
category: "reference"
tags: [reference, langgraph, pregel, checkpoint, create_metadata_for_update_state_api]
---

# create_metadata_for_update_state_api

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_checkpoint/create_metadata_for_update_state_api)

Advance ``counters_since_delta_snapshot`` for update_state on a non-fresh thread.

Mirrors the per-superstep counter bump in ``_loop._put_checkpoint``.

## Signature

```python
create_metadata_for_update_state_api(
    channels: Mapping[str, BaseChannel],
    updated_channels: set[str],
    *,
    prev_metadata: Mapping[str, Any] | None,
) -> dict[str, tuple[int, int]]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/pregel/_checkpoint.py#L92)
