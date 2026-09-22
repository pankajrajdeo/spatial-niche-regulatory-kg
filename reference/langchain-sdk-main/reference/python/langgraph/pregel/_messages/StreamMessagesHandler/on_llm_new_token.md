---
title: "on_llm_new_token"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langgraph/pregel/_messages/StreamMessagesHandler/on_llm_new_token"
category: "reference"
tags: [reference, langgraph, pregel, messages, streammessageshandler, on_llm_new_token]
---

# on_llm_new_token

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_messages/StreamMessagesHandler/on_llm_new_token)

## Signature

```python
on_llm_new_token(
    self,
    token: str,
    *,
    chunk: ChatGenerationChunk | None = None,
    run_id: UUID,
    parent_run_id: UUID | None = None,
    tags: list[str] | None = None,
    **kwargs: Any = {},
) -> Any
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/pregel/_messages.py#L151)
