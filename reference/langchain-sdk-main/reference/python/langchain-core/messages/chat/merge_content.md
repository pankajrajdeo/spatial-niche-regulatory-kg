---
title: "merge_content"
description: "Merge multiple message contents."
source: "https://reference.langchain.com/python/langchain-core/messages/chat/merge_content"
category: "reference"
tags: [reference, langchain-core, messages, chat, merge_content]
---

# merge_content

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/base/merge_content)

Merge multiple message contents.

## Signature

```python
merge_content(
    first_content: str | list[str | dict[Any, Any]],
    *contents: str | list[str | dict[Any, Any]] = (),
) -> str | list[str | dict[Any, Any]]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `first_content` | `str \| list[str \| dict[Any, Any]]` | Yes | The first `content`. Can be a string or a list. |
| `contents` | `str \| list[str \| dict[Any, Any]]` | No | The other `content`s. Can be a string or a list. (default: `()`) |

## Returns

`str | list[str | dict[Any, Any]]`

The merged content.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/base.py#L366)
