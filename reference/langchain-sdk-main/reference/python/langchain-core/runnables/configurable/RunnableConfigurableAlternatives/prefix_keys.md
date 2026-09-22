---
title: "prefix_keys"
description: "Whether to prefix configurable fields of each alternative with a namespace of the form ==, e.g. a key named \"temperature\" used by the alternative named \"gpt3\" becomes \"model==gpt3/temperature\"."
source: "https://reference.langchain.com/python/langchain-core/runnables/configurable/RunnableConfigurableAlternatives/prefix_keys"
category: "reference"
tags: [reference, langchain-core, runnables, configurable, runnableconfigurablealternatives, prefix_keys]
---

# prefix_keys

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/configurable/RunnableConfigurableAlternatives/prefix_keys)

Whether to prefix configurable fields of each alternative with a namespace
of the form <which.id>==<alternative_key>, e.g. a key named "temperature" used by
the alternative named "gpt3" becomes "model==gpt3/temperature".

## Signature

```python
prefix_keys: bool
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/configurable.py#L544)
