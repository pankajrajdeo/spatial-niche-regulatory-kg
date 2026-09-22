---
title: "LangChainTracer"
description: "Implementation of the SharedTracer that POSTS to the LangChain endpoint."
source: "https://reference.langchain.com/python/langchain-core/tracers/langchain/LangChainTracer"
category: "reference"
tags: [reference, langchain-core, tracers, langchain, langchaintracer]
---

# LangChainTracer

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/langchain/LangChainTracer)

Implementation of the `SharedTracer` that `POSTS` to the LangChain endpoint.

## Signature

```python
LangChainTracer(
    self,
    example_id: UUID | str | None = None,
    project_name: str | None = None,
    client: Client | None = None,
    tags: list[str] | None = None,
    *,
    metadata: Mapping[str, str] | None = None,
    **kwargs: Any = {},
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `example_id` | `UUID \| str \| None` | No | The example ID. (default: `None`) |
| `project_name` | `str \| None` | No | The project name.  Defaults to the tracer project. (default: `None`) |
| `client` | `Client \| None` | No | The client.  Defaults to the global client. (default: `None`) |
| `tags` | `list[str] \| None` | No | The tags.  Defaults to an empty list. (default: `None`) |
| `metadata` | `Mapping[str, str] \| None` | No | Additional metadata to include if it isn't already in the run.  Defaults to None. (default: `None`) |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

## Extends

- `BaseTracer`

## Constructors

```python
__init__(
    self,
    example_id: UUID | str | None = None,
    project_name: str | None = None,
    client: Client | None = None,
    tags: list[str] | None = None,
    *,
    metadata: Mapping[str, str] | None = None,
    **kwargs: Any = {},
) -> None
```

| Name | Type |
|------|------|
| `example_id` | `UUID \| str \| None` |
| `project_name` | `str \| None` |
| `client` | `Client \| None` |
| `tags` | `list[str] \| None` |
| `metadata` | `Mapping[str, str] \| None` |

## Properties

- `run_inline`
- `example_id`
- `project_name`
- `client`
- `tags`
- `latest_run`
- `run_has_token_event_map`
- `tracing_metadata`

## Methods

- [`copy_with_metadata_defaults()`](https://reference.langchain.com/python/langchain-core/tracers/langchain/LangChainTracer/copy_with_metadata_defaults)
- [`on_chat_model_start()`](https://reference.langchain.com/python/langchain-core/tracers/langchain/LangChainTracer/on_chat_model_start)
- [`get_run_url()`](https://reference.langchain.com/python/langchain-core/tracers/langchain/LangChainTracer/get_run_url)
- [`wait_for_futures()`](https://reference.langchain.com/python/langchain-core/tracers/langchain/LangChainTracer/wait_for_futures)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/tracers/langchain.py#L134)
