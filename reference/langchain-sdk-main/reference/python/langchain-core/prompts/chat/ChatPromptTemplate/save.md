---
title: "save"
description: "Save prompt to file."
source: "https://reference.langchain.com/python/langchain-core/prompts/chat/ChatPromptTemplate/save"
category: "reference"
tags: [reference, langchain-core, prompts, chat, chatprompttemplate, save]
---

# save

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/chat/ChatPromptTemplate/save)

Save prompt to file.

## Signature

```python
save(
    self,
    file_path: Path | str,
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `file_path` | `Path \| str` | Yes | path to file. |

## ⚠️ Deprecated

Deprecated since version 1.2.21. Use Use `dumpd`/`dumps` from `langchain_core.load` to serialize prompts and `load`/`loads` to deserialize them. instead. Will be removed in version 2.0.0.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/prompts/chat.py#L1313)
