---
title: "push_message"
description: "Write a message manually to the messages / messages-tuple stream mode."
source: "https://reference.langchain.com/python/langgraph/graph/message/push_message"
category: "reference"
tags: [reference, langgraph, graph, message, push_message]
---

# push_message

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/graph/message/push_message)

Write a message manually to the `messages` / `messages-tuple` stream mode.

Will automatically write to the channel specified in the `state_key` unless `state_key` is `None`.

## Signature

```python
push_message(
    message: MessageLikeRepresentation | BaseMessageChunk,
    *,
    state_key: str | None = 'messages',
) -> AnyMessage
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/graph/message.py#L392)
