---
title: "Serializable"
description: "Serializable base class."
source: "https://reference.langchain.com/python/langchain-core/load/serializable/Serializable"
category: "reference"
tags: [reference, langchain-core, load, serializable]
---

# Serializable

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/load/serializable/Serializable)

Serializable base class.

This class is used to serialize objects to JSON.

It relies on the following methods and properties:

- [`is_lc_serializable`][langchain_core.load.serializable.Serializable.is_lc_serializable]: Is this class serializable?

    By design, even if a class inherits from `Serializable`, it is not serializable
    by default. This is to prevent accidental serialization of objects that should
    not be serialized.
- [`get_lc_namespace`][langchain_core.load.serializable.Serializable.get_lc_namespace]: Get the namespace of the LangChain object.

    During deserialization, this namespace is used to identify
    the correct class to instantiate.

    Please see the `Reviver` class in `langchain_core.load.load` for more details.

    During deserialization an additional mapping is handle classes that have moved
    or been renamed across package versions.

- [`lc_secrets`][langchain_core.load.serializable.Serializable.lc_secrets]: A map of constructor argument names to secret ids.
- [`lc_attributes`][langchain_core.load.serializable.Serializable.lc_attributes]: List of additional attribute names that should be included
    as part of the serialized representation.

## Signature

```python
Serializable(
    self,
    *args: Any = (),
    **kwargs: Any = {},
)
```

## Extends

- `BaseModel`
- `ABC`

## Constructors

```python
__init__(
    self,
    *args: Any = (),
    **kwargs: Any = {},
) -> None
```

## Properties

- `lc_secrets`
- `lc_attributes`
- `model_config`

## Methods

- [`is_lc_serializable()`](https://reference.langchain.com/python/langchain-core/load/serializable/Serializable/is_lc_serializable)
- [`get_lc_namespace()`](https://reference.langchain.com/python/langchain-core/load/serializable/Serializable/get_lc_namespace)
- [`lc_id()`](https://reference.langchain.com/python/langchain-core/load/serializable/Serializable/lc_id)
- [`to_json()`](https://reference.langchain.com/python/langchain-core/load/serializable/Serializable/to_json)
- [`to_json_not_implemented()`](https://reference.langchain.com/python/langchain-core/load/serializable/Serializable/to_json_not_implemented)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/load/serializable.py#L106)
