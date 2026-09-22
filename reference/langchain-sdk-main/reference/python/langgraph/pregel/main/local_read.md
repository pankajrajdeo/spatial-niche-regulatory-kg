---
title: "local_read"
description: "Function injected under CONFIG_KEY_READ in task config, to read current state. Used by conditional edges to read a copy of the state with reflecting the writes from that node only."
source: "https://reference.langchain.com/python/langgraph/pregel/main/local_read"
category: "reference"
tags: [reference, langgraph, pregel, main, local_read]
---

# local_read

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_algo/local_read)

Function injected under CONFIG_KEY_READ in task config, to read current state.
Used by conditional edges to read a copy of the state with reflecting the writes
from that node only.

## Signature

```python
local_read(
    scratchpad: PregelScratchpad,
    channels: Mapping[str, BaseChannel],
    managed: ManagedValueMapping,
    task: WritesProtocol,
    select: list[str] | str,
    fresh: bool = False,
) -> dict[str, Any] | Any
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/pregel/_algo.py#L188)
