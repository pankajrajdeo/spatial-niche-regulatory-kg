---
title: "KWARGS_CONFIG_KEYS"
description: "List of kwargs that can be passed to functions, and their corresponding config keys, default values and type annotations."
source: "https://reference.langchain.com/python/langgraph/_internal/_runnable/KWARGS_CONFIG_KEYS"
category: "reference"
tags: [reference, langgraph, internal, runnable, kwargs_config_keys]
---

# KWARGS_CONFIG_KEYS

> **Attribute** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/_internal/_runnable/KWARGS_CONFIG_KEYS)

List of kwargs that can be passed to functions, and their corresponding
config keys, default values and type annotations.

Used to configure keyword arguments that can be injected at runtime
from the `Runtime` object as kwargs to `invoke`, `ainvoke`, `stream` and `astream`.

For a keyword to be injected from the config object, the function signature
must contain a kwarg with the same name and a matching type annotation.

Each tuple contains:
- the name of the kwarg in the function signature
- the type annotation(s) for the kwarg
- the `Runtime` attribute for fetching the value (N/A if not applicable)

This is fully internal and should be further refactored to use `get_type_hints`
to resolve forward references and optional types formatted like BaseStore | None.

## Signature

```python
KWARGS_CONFIG_KEYS: tuple[tuple[str, tuple[Any, ...], str, Any], ...] = (('config', (RunnableConfig, 'RunnableConfig', Optional[RunnableConfig], 'Optional[RunnableConfig]', inspect.Parameter.empty), 'N/A', inspect.Parameter.empty), ('writer', (StreamWriter, 'StreamWriter', inspect.Parameter.empty), 'stream_writer', lambda _: None), ('store', (BaseStore, 'BaseStore', inspect.Parameter.empty), 'store', inspect.Parameter.empty), ('store', (Optional[BaseStore], 'Optional[BaseStore]'), 'store', None), ('previous', (ANY_TYPE,), 'previous', inspect.Parameter.empty), ('runtime', (ANY_TYPE,), 'N/A', inspect.Parameter.empty), ('error', (NodeError, 'NodeError'), 'N/A', None))
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/_internal/_runnable.py#L168)
