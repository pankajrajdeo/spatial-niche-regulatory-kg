---
title: "Reviver"
description: "Reviver for JSON objects."
source: "https://reference.langchain.com/python/langchain-core/load/load/Reviver"
category: "reference"
tags: [reference, langchain-core, load, reviver]
---

# Reviver

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/load/load/Reviver)

Reviver for JSON objects.

Used as the `object_hook` for `json.loads` to reconstruct LangChain objects from
their serialized JSON representation.

Only classes in the allowlist can be instantiated.

## Signature

```python
Reviver(
    self,
    allowed_objects: Iterable[AllowedObject] | Literal['all', 'core', 'messages'] | None = None,
    secrets_map: dict[str, str] | None = None,
    valid_namespaces: list[str] | None = None,
    secrets_from_env: bool = False,
    additional_import_mappings: dict[tuple[str, ...], tuple[str, ...]] | None = None,
    *,
    ignore_unserializable_fields: bool = False,
    init_validator: InitValidator | None = default_init_validator,
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `allowed_objects` | `Iterable[AllowedObject] \| Literal['all', 'core', 'messages'] \| None` | No | Allowlist of classes that can be deserialized. - Explicit list of classes (recommended for untrusted input):     only those specific classes are allowed. - `'messages'`: chat-message classes only (e.g. `AIMessage`,     `HumanMessage`). Safe for untrusted input. - `'core'` (current default): unsafe with untrusted manifests.     Classes defined in the serialization mappings under     `langchain_core`. - `'all'`: unsafe with untrusted manifests. Every class in the     serialization mappings, including partner chat models and     LLMs and their constructor kwargs. See     `langchain_core.load.mapping` for the full list. (default: `None`) |
| `secrets_map` | `dict[str, str] \| None` | No | A map of secrets to load.  Only include the specific secrets the serialized object requires. If a secret is not found in the map, it will be loaded from the environment if `secrets_from_env` is `True`. (default: `None`) |
| `valid_namespaces` | `list[str] \| None` | No | Additional namespaces (modules) to allow during deserialization, beyond the default trusted namespaces. (default: `None`) |
| `secrets_from_env` | `bool` | No | Whether to load secrets from the environment.  A crafted payload can name arbitrary environment variables in its `secret` fields, so enabling this on untrusted data can leak sensitive values. Keep this `False` (the default) unless the serialized data is fully trusted. (default: `False`) |
| `additional_import_mappings` | `dict[tuple[str, ...], tuple[str, ...]] \| None` | No | A dictionary of additional namespace mappings.  You can use this to override default mappings or add new mappings.  When `allowed_objects` is `None` (using defaults), paths from these mappings are also added to the allowed class paths. (default: `None`) |
| `ignore_unserializable_fields` | `bool` | No | Whether to ignore unserializable fields. (default: `False`) |
| `init_validator` | `InitValidator \| None` | No | Optional callable to validate kwargs before instantiation.  If provided, this function is called with `(class_path, kwargs)` where `class_path` is the class path tuple and `kwargs` is the kwargs dict. The validator should raise an exception if the object should not be deserialized, otherwise return `None`.  Defaults to `default_init_validator` which blocks jinja2 templates. (default: `default_init_validator`) |

## Constructors

```python
__init__(
    self,
    allowed_objects: Iterable[AllowedObject] | Literal['all', 'core', 'messages'] | None = None,
    secrets_map: dict[str, str] | None = None,
    valid_namespaces: list[str] | None = None,
    secrets_from_env: bool = False,
    additional_import_mappings: dict[tuple[str, ...], tuple[str, ...]] | None = None,
    *,
    ignore_unserializable_fields: bool = False,
    init_validator: InitValidator | None = default_init_validator,
) -> None
```

| Name | Type |
|------|------|
| `allowed_objects` | `Iterable[AllowedObject] \| Literal['all', 'core', 'messages'] \| None` |
| `secrets_map` | `dict[str, str] \| None` |
| `valid_namespaces` | `list[str] \| None` |
| `secrets_from_env` | `bool` |
| `additional_import_mappings` | `dict[tuple[str, ...], tuple[str, ...]] \| None` |
| `ignore_unserializable_fields` | `bool` |
| `init_validator` | `InitValidator \| None` |

## Properties

- `secrets_from_env`
- `secrets_map`
- `valid_namespaces`
- `additional_import_mappings`
- `import_mappings`
- `allowed_class_paths`
- `ignore_unserializable_fields`
- `init_validator`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/load/load.py#L336)
