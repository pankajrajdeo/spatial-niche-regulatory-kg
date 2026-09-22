---
title: "get_lc_namespace"
description: "Get the namespace of the LangChain object."
source: "https://reference.langchain.com/python/langchain-core/load/serializable/Serializable/get_lc_namespace"
category: "reference"
tags: [reference, langchain-core, load, serializable, get_lc_namespace]
---

# get_lc_namespace

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/load/serializable/Serializable/get_lc_namespace)

Get the namespace of the LangChain object.

The default implementation splits `cls.__module__` on `'.'`, e.g.
`langchain_openai.chat_models` becomes
`["langchain_openai", "chat_models"]`. This value is used by `lc_id` to
build the serialization identifier.

New partner packages should **not** override this method. The default
behavior is correct for any class whose module path already reflects
its package name. Some older packages (e.g. `langchain-openai`,
`langchain-anthropic`) override it to return a legacy-style namespace
like `["langchain", "chat_models", "openai"]`, matching the module
paths that existed before those integrations were split out of the
main `langchain` package. Those overrides are kept for
backwards-compatible deserialization; new packages should not copy them.

Deserialization mapping is handled separately by
`SERIALIZABLE_MAPPING` in `langchain_core.load.mapping`.

## Signature

```python
get_lc_namespace(
    cls,
) -> list[str]
```

## Returns

`list[str]`

The namespace.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/load/serializable.py#L151)
