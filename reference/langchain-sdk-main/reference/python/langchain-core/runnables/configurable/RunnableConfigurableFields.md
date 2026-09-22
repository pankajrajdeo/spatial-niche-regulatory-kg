---
title: "RunnableConfigurableFields"
description: "Runnable that can be dynamically configured."
source: "https://reference.langchain.com/python/langchain-core/runnables/configurable/RunnableConfigurableFields"
category: "reference"
tags: [reference, langchain-core, runnables, configurable, runnableconfigurablefields]
---

# RunnableConfigurableFields

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/configurable/RunnableConfigurableFields)

`Runnable` that can be dynamically configured.

A `RunnableConfigurableFields` should be initiated using the
`configurable_fields` method of a `Runnable`.

Here is an example of using a `RunnableConfigurableFields` with LLMs:

```python
    from langchain_core.prompts import PromptTemplate
    from langchain_core.runnables import ConfigurableField
    from langchain_openai import ChatOpenAI

    model = ChatOpenAI(temperature=0).configurable_fields(
        temperature=ConfigurableField(
            id="temperature",
            name="LLM Temperature",
            description="The temperature of the LLM",
        )
    )
    # This creates a RunnableConfigurableFields for a chat model.

    # When invoking the created RunnableSequence, you can pass in the
    # value for your ConfigurableField's id which in this case
    # will be change in temperature

    prompt = PromptTemplate.from_template("Pick a random number above {x}")
    chain = prompt | model

    chain.invoke({"x": 0})
    chain.invoke({"x": 0}, config={"configurable": {"temperature": 0.9}})
```

Here is an example of using a `RunnableConfigurableFields` with `HubRunnables`:

```python
    from langchain_core.prompts import PromptTemplate
    from langchain_core.runnables import ConfigurableField
    from langchain_openai import ChatOpenAI
    from langchain.runnables.hub import HubRunnable

    prompt = HubRunnable("rlm/rag-prompt").configurable_fields(
        owner_repo_commit=ConfigurableField(
            id="hub_commit",
            name="Hub Commit",
            description="The Hub commit to pull from",
        )
    )

    prompt.invoke({"question": "foo", "context": "bar"})

    # Invoking prompt with `with_config` method

    prompt.invoke(
        {"question": "foo", "context": "bar"},
        config={"configurable": {"hub_commit": "rlm/rag-prompt-llama"}},
    )
```

## Signature

```python
RunnableConfigurableFields(
    self,
    *args: Any = (),
    **kwargs: Any = {},
)
```

## Extends

- `DynamicRunnable[Input, Output]`

## Properties

- `fields`
- `config_specs`

## Methods

- [`configurable_fields()`](https://reference.langchain.com/python/langchain-core/runnables/configurable/RunnableConfigurableFields/configurable_fields)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/configurable.py#L317)
