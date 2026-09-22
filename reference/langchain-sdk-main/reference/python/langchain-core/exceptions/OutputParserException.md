---
title: "OutputParserException"
description: "Exception that output parsers should raise to signify a parsing error."
source: "https://reference.langchain.com/python/langchain-core/exceptions/OutputParserException"
category: "reference"
tags: [reference, langchain-core, exceptions, outputparserexception]
---

# OutputParserException

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/exceptions/OutputParserException)

Exception that output parsers should raise to signify a parsing error.

This exists to differentiate parsing errors from other code or execution errors
that also may arise inside the output parser.

`OutputParserException` will be available to catch and handle in ways to fix the
parsing error, while other errors will be raised.

## Signature

```python
OutputParserException(
    self,
    error: Any,
    observation: str | None = None,
    llm_output: str | None = None,
    send_to_llm: bool = False,
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `error` | `Any` | Yes | The error that's being re-raised or an error message. |
| `observation` | `str \| None` | No | String explanation of error which can be passed to a model to try and remediate the issue. (default: `None`) |
| `llm_output` | `str \| None` | No | String model output which is error-ing. (default: `None`) |
| `send_to_llm` | `bool` | No | Whether to send the observation and llm_output back to an Agent after an `OutputParserException` has been raised.  This gives the underlying model driving the agent the context that the previous output was improperly structured, in the hopes that it will update the output to the correct format. (default: `False`) |

## Extends

- `ValueError`
- `LangChainException`

## Constructors

```python
__init__(
    self,
    error: Any,
    observation: str | None = None,
    llm_output: str | None = None,
    send_to_llm: bool = False,
)
```

| Name | Type |
|------|------|
| `error` | `Any` |
| `observation` | `str \| None` |
| `llm_output` | `str \| None` |
| `send_to_llm` | `bool` |

## Properties

- `observation`
- `llm_output`
- `send_to_llm`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/exceptions.py#L15)
