---
title: "mapping"
description: "Serialization mapping."
source: "https://reference.langchain.com/python/langchain-core/load/mapping"
category: "reference"
tags: [reference, langchain-core, load, mapping]
---

# mapping

> **Module** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/load/mapping)

Serialization mapping.

This file contains a mapping between the `lc_namespace` path for a given
subclass that implements from `Serializable` to the namespace
where that class is actually located.

This mapping helps maintain the ability to serialize and deserialize
well-known LangChain objects even if they are moved around in the codebase
across different LangChain versions.

For example, the code for the `AIMessage` class is located in
`langchain_core.messages.ai.AIMessage`. This message is associated with the
`lc_namespace` of `["langchain", "schema", "messages", "AIMessage"]`,
because this code was originally in `langchain.schema.messages.AIMessage`.

The mapping allows us to deserialize an `AIMessage` created with an older
version of LangChain where the code was in a different location.

## Properties

- `SERIALIZABLE_MAPPING`
- `OLD_CORE_NAMESPACES_MAPPING`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/load/mapping.py)
