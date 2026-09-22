---
title: "with_structured_output"
description: "Model wrapper that returns outputs formatted to match the given schema."
source: "https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel/with_structured_output"
category: "reference"
tags: [reference, langchain-core, language_models, chat_models, basechatmodel, with_structured_output]
---

# with_structured_output

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel/with_structured_output)

Model wrapper that returns outputs formatted to match the given schema.

## Signature

```python
with_structured_output(
    self,
    schema: builtins.dict[str, Any] | type,
    *,
    include_raw: bool = False,
    **kwargs: Any = {},
) -> Runnable[LanguageModelInput, builtins.dict[str, Any] | BaseModel]
```

## Description

???+ example "Pydantic schema (`include_raw=False`)"

```python
    from pydantic import BaseModel

    class AnswerWithJustification(BaseModel):
        '''An answer to the user question along with justification for the answer.'''

        answer: str
        justification: str

    model = ChatModel(model="model-name", temperature=0)
    structured_model = model.with_structured_output(AnswerWithJustification)

    structured_model.invoke(
        "What weighs more a pound of bricks or a pound of feathers"
    )

    # -> AnswerWithJustification(
    #     answer='They weigh the same',
    #     justification='Both a pound of bricks and a pound of feathers weigh one pound. The weight is the same, but the volume or density of the objects may differ.'
    # )
```

??? example "Pydantic schema (`include_raw=True`)"

```python
    from pydantic import BaseModel

    class AnswerWithJustification(BaseModel):
        '''An answer to the user question along with justification for the answer.'''

        answer: str
        justification: str

    model = ChatModel(model="model-name", temperature=0)
    structured_model = model.with_structured_output(
        AnswerWithJustification, include_raw=True
    )

    structured_model.invoke(
        "What weighs more a pound of bricks or a pound of feathers"
    )
    # -> {
    #     'raw': AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_Ao02pnFYXD6GN1yzc0uXPsvF', 'function': {'arguments': '{"answer":"They weigh the same.","justification":"Both a pound of bricks and a pound of feathers weigh one pound. The weight is the same, but the volume or density of the objects may differ."}', 'name': 'AnswerWithJustification'}, 'type': 'function'}]}),
    #     'parsed': AnswerWithJustification(answer='They weigh the same.', justification='Both a pound of bricks and a pound of feathers weigh one pound. The weight is the same, but the volume or density of the objects may differ.'),
    #     'parsing_error': None
    # }
```

??? example "Dictionary schema (`include_raw=False`)"

```python
    from pydantic import BaseModel
    from langchain_core.utils.function_calling import convert_to_openai_tool

    class AnswerWithJustification(BaseModel):
        '''An answer to the user question along with justification for the answer.'''

        answer: str
        justification: str

    dict_schema = convert_to_openai_tool(AnswerWithJustification)
    model = ChatModel(model="model-name", temperature=0)
    structured_model = model.with_structured_output(dict_schema)

    structured_model.invoke(
        "What weighs more a pound of bricks or a pound of feathers"
    )
    # -> {
    #     'answer': 'They weigh the same',
    #     'justification': 'Both a pound of bricks and a pound of feathers weigh one pound. The weight is the same, but the volume and density of the two substances differ.'
    # }
```

!!! warning "Behavior changed in `langchain-core` 0.2.26"

    Added support for `TypedDict` class.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `schema` | `builtins.dict[str, Any] \| type` | Yes | The output schema. Can be passed in as:  - An OpenAI function/tool schema, - A JSON Schema, - A `TypedDict` class, - Or a Pydantic class.  If `schema` is a Pydantic class then the model output will be a Pydantic instance of that class, and the model-generated fields will be validated by the Pydantic class. Otherwise the model output will be a dict and will not be validated.  See `langchain_core.utils.function_calling.convert_to_openai_tool` for more on how to properly specify types and descriptions of schema fields when specifying a Pydantic or `TypedDict` class. |
| `include_raw` | `bool` | No |  If `False` then only the parsed structured output is returned.  If an error occurs during model output parsing it will be raised.  If `True` then both the raw model response (a `BaseMessage`) and the parsed model response will be returned.  If an error occurs during output parsing it will be caught and returned as well.  The final output is always a `dict` with keys `'raw'`, `'parsed'`, and `'parsing_error'`. (default: `False`) |

## Returns

`Runnable[LanguageModelInput, builtins.dict[str, Any] | BaseModel]`

A `Runnable` that takes same inputs as a
`langchain_core.language_models.chat.BaseChatModel`. If `include_raw` is
`False` and `schema` is a Pydantic class, `Runnable` outputs an instance
of `schema` (i.e., a Pydantic object). Otherwise, if `include_raw` is
`False` then `Runnable` outputs a `dict`.

If `include_raw` is `True`, then `Runnable` outputs a `dict` with keys:

- `'raw'`: `BaseMessage`
- `'parsed'`: `None` if there was a parsing error, otherwise the type
    depends on the `schema` as described above.
- `'parsing_error'`: `BaseException | None`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/language_models/chat_models.py#L2385)
