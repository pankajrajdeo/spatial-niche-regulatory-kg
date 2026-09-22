---
title: "load"
description: "Revive a LangChain class from a JSON object."
source: "https://reference.langchain.com/python/langchain-core/load/load/load"
category: "reference"
tags: [reference, langchain-core, load]
---

# load

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/load/load/load)

Revive a LangChain class from a JSON object.

Use this if you already have a parsed JSON object, eg. from `json.load` or
`orjson.loads`.

Only classes in the allowlist can be instantiated. The default allowlist
includes core LangChain types (messages, prompts, documents, etc.). See
`langchain_core.load.mapping` for the full list.

!!! warning "Do not use with untrusted input"

    A serialized payload may carry constructor kwargs that affect runtime
    behavior (custom `base_url`, headers, model name, etc.), so it should be
    treated as executable configuration rather than plain text. For example,
    deserializing a model whose `base_url` points at an attacker-controlled
    host can result in Server-Side Request Forgery (SSRF); this is expected
    behavior, since `load()` faithfully reconstructs the configuration in
    the manifest. If the source is untrusted, avoid calling `load()` on it;
    if you must, pass `allowed_objects='messages'` or an explicit list of
    message classes. See the module-level threat model for details.

## Signature

```python
load(
    obj: Any,
    *,
    allowed_objects: Iterable[AllowedObject] | Literal['all', 'core', 'messages'] | None = None,
    secrets_map: dict[str, str] | None = None,
    valid_namespaces: list[str] | None = None,
    secrets_from_env: bool = False,
    additional_import_mappings: dict[tuple[str, ...], tuple[str, ...]] | None = None,
    ignore_unserializable_fields: bool = False,
    init_validator: InitValidator | None = default_init_validator,
) -> Any
```

## Description

**Example:**

```python
from langchain_core.load import load, dumpd
from langchain_core.messages import AIMessage

msg = AIMessage(content="Hello")
data = dumpd(msg)

# Deserialize using default allowlist
loaded = load(data)

# Or with explicit allowlist
loaded = load(data, allowed_objects=[AIMessage])

# Or extend defaults with additional mappings
loaded = load(
    data,
    additional_import_mappings={
        ("my_pkg", "MyClass"): ("my_pkg", "module", "MyClass"),
    },
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `obj` | `Any` | Yes | The object to load. |
| `allowed_objects` | `Iterable[AllowedObject] \| Literal['all', 'core', 'messages'] \| None` | No | Allowlist of classes that can be deserialized.  - Explicit list of classes (recommended for untrusted input): only     those specific classes are allowed. - `'messages'`: chat-message classes only. Safe for untrusted input. - `'core'` (current default): unsafe with untrusted manifests.     Classes defined in the serialization mappings under     `langchain_core`. - `'all'`: unsafe with untrusted manifests. Every class in the     serialization mappings, including partner chat models and LLMs     and their constructor kwargs. See `langchain_core.load.mapping`     for the full list. - `[]`: Disallow all deserialization (will raise on any object). (default: `None`) |
| `secrets_map` | `dict[str, str] \| None` | No | A map of secrets to load.  Only include the specific secrets the serialized object requires.  If a secret is not found in the map, it will be loaded from the environment if `secrets_from_env` is `True`. (default: `None`) |
| `valid_namespaces` | `list[str] \| None` | No | Additional namespaces (modules) to allow during deserialization, beyond the default trusted namespaces. (default: `None`) |
| `secrets_from_env` | `bool` | No | Whether to load secrets from the environment.  A crafted payload can name arbitrary environment variables in its `secret` fields, so enabling this on untrusted data can leak sensitive values. Keep this `False` (the default) unless the serialized data is fully trusted. (default: `False`) |
| `additional_import_mappings` | `dict[tuple[str, ...], tuple[str, ...]] \| None` | No | A dictionary of additional namespace mappings.  You can use this to override default mappings or add new mappings.  When `allowed_objects` is `None` (using defaults), paths from these mappings are also added to the allowed class paths. (default: `None`) |
| `ignore_unserializable_fields` | `bool` | No | Whether to ignore unserializable fields. (default: `False`) |
| `init_validator` | `InitValidator \| None` | No | Optional callable to validate kwargs before instantiation.  If provided, this function is called with `(class_path, kwargs)` where `class_path` is the class path tuple and `kwargs` is the kwargs dict. The validator should raise an exception if the object should not be deserialized, otherwise return `None`.  Defaults to `default_init_validator` which blocks jinja2 templates. (default: `default_init_validator`) |

## Returns

`Any`

Revived LangChain objects.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/load/load.py#L682)
