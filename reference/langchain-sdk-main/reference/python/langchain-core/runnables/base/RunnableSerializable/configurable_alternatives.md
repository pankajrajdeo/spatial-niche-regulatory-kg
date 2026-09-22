---
title: "configurable_alternatives"
description: "Configure alternatives for Runnable objects that can be set at runtime."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/RunnableSerializable/configurable_alternatives"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnableserializable, configurable_alternatives]
---

# configurable_alternatives

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableSerializable/configurable_alternatives)

Configure alternatives for `Runnable` objects that can be set at runtime.

## Signature

```python
configurable_alternatives(
    self,
    which: ConfigurableField,
    *,
    default_key: str = 'default',
    prefix_keys: bool = False,
    **kwargs: Runnable[Input, Output] | Callable[[], Runnable[Input, Output]] = {},
) -> RunnableSerializable[Input, Output]
```

## Description

!!! example

```python
from langchain_anthropic import ChatAnthropic
from langchain_core.runnables.utils import ConfigurableField
from langchain_openai import ChatOpenAI

model = ChatAnthropic(
    model_name="claude-sonnet-4-5-20250929"
).configurable_alternatives(
    ConfigurableField(id="llm"),
    default_key="anthropic",
    openai=ChatOpenAI(),
)

# uses the default model ChatAnthropic
print(model.invoke("which organization created you?").content)

# uses ChatOpenAI
print(
    model.with_config(configurable={"llm": "openai"})
    .invoke("which organization created you?")
    .content
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `which` | `ConfigurableField` | Yes | The `ConfigurableField` instance that will be used to select the alternative. |
| `default_key` | `str` | No | The default key to use if no alternative is selected. (default: `'default'`) |
| `prefix_keys` | `bool` | No | Whether to prefix the keys with the `ConfigurableField` id. (default: `False`) |
| `**kwargs` | `Runnable[Input, Output] \| Callable[[], Runnable[Input, Output]]` | No | A dictionary of keys to `Runnable` instances or callables that return `Runnable` instances. (default: `{}`) |

## Returns

`RunnableSerializable[Input, Output]`

A new `Runnable` with the alternatives configured.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/base.py#L2913)
