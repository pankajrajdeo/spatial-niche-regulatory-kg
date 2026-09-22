---
title: "load"
description: "Load LangChain objects from JSON strings or objects."
source: "https://reference.langchain.com/python/langchain-core/load/load"
category: "reference"
tags: [reference, langchain-core, load]
---

# load

> **Module** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/load/load)

Load LangChain objects from JSON strings or objects.

## How it works

Each `Serializable` LangChain object has a unique identifier (its "class path"), which
is a list of strings representing the module path and class name. For example:

- `AIMessage` -> `["langchain_core", "messages", "ai", "AIMessage"]`
- `ChatPromptTemplate` -> `["langchain_core", "prompts", "chat", "ChatPromptTemplate"]`

When deserializing, the class path from the JSON `'id'` field is checked against an
allowlist. If the class is not in the allowlist, deserialization raises a `ValueError`.

## Threat model

A serialized LangChain payload crosses a trust boundary because the manifest
may contain serialized objects and configuration that affect runtime behavior.
For example, a payload can configure a chat model with a custom `base_url`,
custom headers, a different model name, or other constructor arguments. These
are supported features, but they also mean the payload contents should be
treated as executable configuration rather than plain text.

Concretely, deserialization instantiates Python objects, so any constructor
(`__init__`) or validator on an allowed class can run during `load()`. A
crafted payload that is allowed to reach an unintended class — or an intended
class with attacker-controlled kwargs — could cause network calls, file
operations, or environment-variable access while the object is being built.

!!! warning "Do not use with untrusted input"

    If the source is untrusted, avoid calling `load()` / `loads()` on it. If
    you must, restrict `allowed_objects` to types that do not execute logic
    during init — `allowed_objects='messages'` (or an explicit list of
    message classes) is the safe choice. Keep `secrets_from_env=False`.

The `allowed_objects` parameter controls which classes can be deserialized:

- **Explicit list of classes** (recommended for untrusted input): only those
    specific classes are allowed.
- **`'messages'`**: chat-message classes only (e.g. `AIMessage`,
    `HumanMessage`). Safe for untrusted input.
- **`'core'` (current default)** — *unsafe with untrusted manifests.*
    Classes defined in the serialization mappings under `langchain_core`
    (messages, documents, prompts, etc.).
- **`'all'`** — *unsafe with untrusted manifests.* Every class in the
    serialization mappings, including partner chat models and LLMs and their
    constructor kwargs (endpoint URLs, headers, model names, etc.).

!!! note "Side effects in allowed classes"

    Deserialization calls `__init__` on allowed classes. If those classes perform
    side effects during initialization (network calls, file operations, etc.),
    those side effects will occur. The allowlist prevents instantiation of
    classes outside the allowlist, but does not sandbox the allowed classes
    themselves or constrain their constructor kwargs.

    For example, an untrusted manifest could deserialize a chat model whose
    `base_url` (or `endpoint_url`) points at an attacker-controlled host. Any
    request that model makes is then directed there — a Server-Side Request
    Forgery (SSRF) vector. This is *expected behavior*: deserialization
    faithfully reconstructs the configuration carried by the manifest, custom
    endpoints included, and LangChain does not special-case or strip such
    kwargs. The mitigation is to **only deserialize manifests you trust**,
    and for untrusted input to restrict `allowed_objects` to `'messages'`
    or an explicit list of classes that take no endpoint configuration.

Import paths are also validated against trusted namespaces before any module is
imported.

### Best practices

- Use the most restrictive `allowed_objects` possible. For untrusted input,
    pass an explicit list of classes or `'messages'`. `'core'` and `'all'`
    are unsafe with untrusted manifests — only use them when the source
    serves the entire payload, including its configuration.
- Keep `secrets_from_env` set to `False` (the default). If you must use it,
    ensure the serialized data comes from a fully trusted source, as a crafted
    payload can read arbitrary environment variables.
- When using `secrets_map`, include only the specific secrets that the
    serialized object requires.

### Injection protection (escape-based)

During serialization, plain dicts that contain an `'lc'` key are escaped by wrapping
them: `{"__lc_escaped__": {...}}`. During deserialization, escaped dicts are unwrapped
and returned as plain dicts, NOT instantiated as LC objects.

This is an allowlist approach: only dicts explicitly produced by
`Serializable.to_json()` (which are NOT escaped) are treated as LC objects;
everything else is user data.

Even if an attacker's payload includes `__lc_escaped__` wrappers, it will be unwrapped
to plain dicts and NOT instantiated as malicious objects.

## Examples

```python
from langchain_core.load import load
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import AIMessage, HumanMessage

# Use default allowlist (classes from mappings) - recommended
obj = load(data)

# Allow only specific classes (most restrictive)
obj = load(
    data,
    allowed_objects=[
        ChatPromptTemplate,
        AIMessage,
        HumanMessage,
    ],
)
```

## Properties

- `OLD_CORE_NAMESPACES_MAPPING`
- `SERIALIZABLE_MAPPING`
- `DEFAULT_NAMESPACES`
- `DISALLOW_LOAD_FROM_PATH`
- `ALL_SERIALIZABLE_MAPPINGS`
- `AllowedObject`
- `InitValidator`

## Methods

- [`beta()`](https://reference.langchain.com/python/langchain-core/load/load/beta)
- [`warn_deprecated()`](https://reference.langchain.com/python/langchain-core/load/load/warn_deprecated)
- [`default_init_validator()`](https://reference.langchain.com/python/langchain-core/load/load/default_init_validator)
- [`loads()`](https://reference.langchain.com/python/langchain-core/load/load/loads)
- [`load()`](https://reference.langchain.com/python/langchain-core/load/load/load)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/load/load.py)
