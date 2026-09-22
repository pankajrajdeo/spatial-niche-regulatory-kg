---
title: "assign"
description: "Assigns new fields to the dict output of this Runnable."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/assign"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnable, assign]
---

# assign

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/assign)

Assigns new fields to the `dict` output of this `Runnable`.

```python
from langchain_core.language_models.fake import FakeStreamingListLLM
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import SystemMessagePromptTemplate
from langchain_core.runnables import Runnable
from operator import itemgetter

prompt = (
    SystemMessagePromptTemplate.from_template("You are a nice assistant.")
    + "{question}"
)
model = FakeStreamingListLLM(responses=["foo-lish"])

chain: Runnable = prompt | model | {"str": StrOutputParser()}

chain_with_assign = chain.assign(hello=itemgetter("str") | model)

print(chain_with_assign.input_schema.model_json_schema())
# {'title': 'PromptInput', 'type': 'object', 'properties':
{'question': {'title': 'Question', 'type': 'string'}}}
print(chain_with_assign.output_schema.model_json_schema())
# {'title': 'RunnableSequenceOutput', 'type': 'object', 'properties':
{'str': {'title': 'Str',
'type': 'string'}, 'hello': {'title': 'Hello', 'type': 'string'}}}
```

## Signature

```python
assign(
    self,
    **kwargs: Runnable[dict[str, Any], Any] | Callable[[dict[str, Any]], Any] | Mapping[str, Runnable[dict[str, Any], Any] | Callable[[dict[str, Any]], Any]] = {},
) -> RunnableSerializable[Any, Any]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `**kwargs` | `Runnable[dict[str, Any], Any] \| Callable[[dict[str, Any]], Any] \| Mapping[str, Runnable[dict[str, Any], Any] \| Callable[[dict[str, Any]], Any]]` | No | A mapping of keys to `Runnable` or `Runnable`-like objects that will be invoked with the entire output dict of this `Runnable`. (default: `{}`) |

## Returns

`RunnableSerializable[Any, Any]`

A new `Runnable`.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/base.py#L836)
