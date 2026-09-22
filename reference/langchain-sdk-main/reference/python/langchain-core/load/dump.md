---
title: "dump"
description: "Serialize LangChain objects to JSON."
source: "https://reference.langchain.com/python/langchain-core/load/dump"
category: "reference"
tags: [reference, langchain-core, load, dump]
---

# dump

> **Module** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/load/dump)

Serialize LangChain objects to JSON.

Provides `dumps` (to JSON string) and `dumpd` (to dict) for serializing
`Serializable` objects.

## Escaping

During serialization, plain dicts (user data) that contain an `'lc'` key are escaped
by wrapping them: `{"__lc_escaped__": {...original...}}`. This prevents injection
attacks where malicious data could trick the deserializer into instantiating
arbitrary classes. The escape marker is removed during deserialization.

This is an allowlist approach: only dicts explicitly produced by
`Serializable.to_json()` are treated as LC objects; everything else is escaped if it
could be confused with the LC format.

## Methods

- [`to_json_not_implemented()`](https://reference.langchain.com/python/langchain-core/load/dump/to_json_not_implemented)
- [`default()`](https://reference.langchain.com/python/langchain-core/load/dump/default)
- [`dumps()`](https://reference.langchain.com/python/langchain-core/load/dump/dumps)
- [`dumpd()`](https://reference.langchain.com/python/langchain-core/load/dump/dumpd)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/load/dump.py)
