---
title: "tool"
description: "Convert Python functions and Runnables to LangChain tools."
source: "https://reference.langchain.com/python/langchain-core/tools/convert/tool"
category: "reference"
tags: [reference, langchain-core, tools, convert, tool]
---

# tool

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tools/convert/tool)

Convert Python functions and `Runnables` to LangChain tools.

Can be used as a decorator with or without arguments to create tools from functions.

Functions can have any signature - the tool will automatically infer input schemas
unless disabled.

!!! note "Requirements"

    - Functions should have type hints for proper schema inference.
    - Functions may accept multiple arguments and return types are flexible;
        outputs will be serialized if needed.
    - When using with `Runnable`, a string name must be provided.

!!! warning "Reserved argument names"

    Avoid naming tool arguments `config`, `run_manager`, or `callbacks`. These
    collide with values LangChain injects into tools at call time. A `config`
    argument is shadowed by the injected `RunnableConfig`, so the tool fails
    at call time with `TypeError: ... missing 1 required positional argument:
    'config'`, while `run_manager` and `callbacks` are silently dropped from
    the generated schema. To access runtime information (state, context, store,
    config), add a `ToolRuntime` parameter instead.

## Signature

```python
tool(
    name_or_callable: str | Callable[..., Any] | None = None,
    runnable: Runnable[Any, Any] | None = None,
    *args: Any = (),
    description: str | None = None,
    return_direct: bool = False,
    args_schema: ArgsSchema | None = None,
    infer_schema: bool = True,
    response_format: Literal['content', 'content_and_artifact'] = 'content',
    parse_docstring: bool = False,
    error_on_invalid_docstring: bool = True,
    extras: dict[str, Any] | None = None,
) -> BaseTool | Callable[[Callable[..., Any] | Runnable[Any, Any]], BaseTool]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `name_or_callable` | `str \| Callable[..., Any] \| None` | No | Optional name of the tool or the `Callable` to be converted to a tool.  Overrides the function's name.  Must be provided as a positional argument. (default: `None`) |
| `runnable` | `Runnable[Any, Any] \| None` | No | Optional `Runnable` to convert to a tool.  Must be provided as a positional argument. (default: `None`) |
| `description` | `str \| None` | No | Optional description for the tool.  Precedence for the tool description value is as follows:  - This `description` argument (used even if docstring and/or `args_schema`     are provided) - Tool function docstring (used even if `args_schema` is provided) - `args_schema` description (used only if `description` and docstring are     not provided) (default: `None`) |
| `*args` | `Any` | No | Extra positional arguments.  Must be empty. (default: `()`) |
| `return_direct` | `bool` | No | Whether to return directly from the tool rather than continuing the agent loop. (default: `False`) |
| `args_schema` | `ArgsSchema \| None` | No | Optional argument schema for user to specify. (default: `None`) |
| `infer_schema` | `bool` | No | Whether to infer the schema of the arguments from the function's signature.  This also makes the resultant tool accept a dictionary input to its `run()` function. (default: `True`) |
| `response_format` | `Literal['content', 'content_and_artifact']` | No | The tool response format.  If `'content'`, then the output of the tool is interpreted as the contents of a `ToolMessage`.  If `'content_and_artifact'`, then the output is expected to be a two-tuple corresponding to the `(content, artifact)` of a `ToolMessage`. (default: `'content'`) |
| `parse_docstring` | `bool` | No | If `infer_schema` and `parse_docstring`, will attempt to parse parameter descriptions from Google Style function docstrings. (default: `False`) |
| `error_on_invalid_docstring` | `bool` | No | If `parse_docstring` is provided, configure whether to raise `ValueError` on invalid Google Style docstrings. (default: `True`) |
| `extras` | `dict[str, Any] \| None` | No | Optional provider-specific extra fields for the tool.  Used to pass configuration that doesn't fit into standard tool fields. Chat models should process known extras when constructing model payloads.  !!! example      For example, Anthropic-specific fields like `cache_control`,     `defer_loading`, or `input_examples`. (default: `None`) |

## Returns

`BaseTool | Callable[[Callable[..., Any] | Runnable[Any, Any]], BaseTool]`

The tool.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/tools/convert.py#L77)
