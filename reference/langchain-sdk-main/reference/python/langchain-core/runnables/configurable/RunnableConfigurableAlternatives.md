---
title: "RunnableConfigurableAlternatives"
description: "Runnable that can be dynamically configured."
source: "https://reference.langchain.com/python/langchain-core/runnables/configurable/RunnableConfigurableAlternatives"
category: "reference"
tags: [reference, langchain-core, runnables, configurable, runnableconfigurablealternatives]
---

# RunnableConfigurableAlternatives

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/configurable/RunnableConfigurableAlternatives)

`Runnable` that can be dynamically configured.

A `RunnableConfigurableAlternatives` should be initiated using the
`configurable_alternatives` method of a `Runnable` or can be
initiated directly as well.

Here is an example of using a `RunnableConfigurableAlternatives` that uses
alternative prompts to illustrate its functionality:

```python
    from langchain_core.runnables import ConfigurableField
    from langchain_openai import ChatOpenAI

    # This creates a RunnableConfigurableAlternatives for Prompt Runnable
    # with two alternatives.
    prompt = PromptTemplate.from_template(
        "Tell me a joke about {topic}"
    ).configurable_alternatives(
        ConfigurableField(id="prompt"),
        default_key="joke",
        poem=PromptTemplate.from_template("Write a short poem about {topic}"),
    )

    # When invoking the created RunnableSequence, you can pass in the
    # value for your ConfigurableField's id which in this case will either be
    # `joke` or `poem`.
    chain = prompt | ChatOpenAI(model="gpt-5.4-mini")

    # The `with_config` method brings in the desired Prompt Runnable in your
    # Runnable Sequence.
    chain.with_config(configurable={"prompt": "poem"}).invoke({"topic": "bears"})
```

Equivalently, you can initialize `RunnableConfigurableAlternatives` directly
and use in LCEL in the same way:

```python
    from langchain_core.runnables import ConfigurableField
    from langchain_core.runnables.configurable import (
        RunnableConfigurableAlternatives,
    )
    from langchain_openai import ChatOpenAI

    prompt = RunnableConfigurableAlternatives(
        which=ConfigurableField(id="prompt"),
        default=PromptTemplate.from_template("Tell me a joke about {topic}"),
        default_key="joke",
        prefix_keys=False,
        alternatives={
            "poem": PromptTemplate.from_template("Write a short poem about {topic}")
        },
    )
    chain = prompt | ChatOpenAI(model="gpt-5.4-mini")
    chain.with_config(configurable={"prompt": "poem"}).invoke({"topic": "bears"})
```

## Signature

```python
RunnableConfigurableAlternatives(
    self,
    *args: Any = (),
    **kwargs: Any = {},
)
```

## Extends

- `DynamicRunnable[Input, Output]`

## Properties

- `which`
- `alternatives`
- `default_key`
- `prefix_keys`
- `config_specs`

## Methods

- [`configurable_fields()`](https://reference.langchain.com/python/langchain-core/runnables/configurable/RunnableConfigurableAlternatives/configurable_fields)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/configurable.py#L474)
