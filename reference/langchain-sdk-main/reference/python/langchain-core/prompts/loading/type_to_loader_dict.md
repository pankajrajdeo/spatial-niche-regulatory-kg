---
title: "type_to_loader_dict"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langchain-core/prompts/loading/type_to_loader_dict"
category: "reference"
tags: [reference, langchain-core, prompts, loading, type_to_loader_dict]
---

# type_to_loader_dict

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/loading/type_to_loader_dict)

## Signature

```python
type_to_loader_dict: dict[str, Callable[..., BasePromptTemplate[str]]] = {'prompt': _load_prompt, 'few_shot': _load_few_shot_prompt, 'chat': _load_chat_prompt}
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/prompts/loading.py#L292)
