---
title: "EvaluatorCallbackHandler"
description: "Tracer that runs a run evaluator whenever a run is persisted."
source: "https://reference.langchain.com/python/langchain-core/tracers/evaluation/EvaluatorCallbackHandler"
category: "reference"
tags: [reference, langchain-core, tracers, evaluation, evaluatorcallbackhandler]
---

# EvaluatorCallbackHandler

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/evaluation/EvaluatorCallbackHandler)

Tracer that runs a run evaluator whenever a run is persisted.

## Signature

```python
EvaluatorCallbackHandler(
    self,
    evaluators: Sequence[langsmith.RunEvaluator],
    client: langsmith.Client | None = None,
    example_id: UUID | str | None = None,
    skip_unfinished: bool = True,
    project_name: str | None = 'evaluators',
    max_concurrency: int | None = None,
    **kwargs: Any = {},
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `evaluators` | `Sequence[langsmith.RunEvaluator]` | Yes | The run evaluators to apply to all top level runs. |
| `client` | `langsmith.Client \| None` | No | The LangSmith client instance to use for evaluating the runs.  If not specified, a new instance will be created. (default: `None`) |
| `example_id` | `UUID \| str \| None` | No | The example ID to be associated with the runs. (default: `None`) |
| `skip_unfinished` | `bool` | No | Whether to skip unfinished runs. (default: `True`) |
| `project_name` | `str \| None` | No | The LangSmith project name to be organize eval chain runs under. (default: `'evaluators'`) |
| `max_concurrency` | `int \| None` | No | The maximum number of concurrent evaluators to run. (default: `None`) |

## Extends

- `BaseTracer`

## Constructors

```python
__init__(
    self,
    evaluators: Sequence[langsmith.RunEvaluator],
    client: langsmith.Client | None = None,
    example_id: UUID | str | None = None,
    skip_unfinished: bool = True,
    project_name: str | None = 'evaluators',
    max_concurrency: int | None = None,
    **kwargs: Any = {},
) -> None
```

| Name | Type |
|------|------|
| `evaluators` | `Sequence[langsmith.RunEvaluator]` |
| `client` | `langsmith.Client \| None` |
| `example_id` | `UUID \| str \| None` |
| `skip_unfinished` | `bool` |
| `project_name` | `str \| None` |
| `max_concurrency` | `int \| None` |

## Properties

- `name`
- `example_id`
- `client`
- `evaluators`
- `executor`
- `futures`
- `skip_unfinished`
- `project_name`
- `logged_eval_results`
- `lock`

## Methods

- [`wait_for_futures()`](https://reference.langchain.com/python/langchain-core/tracers/evaluation/EvaluatorCallbackHandler/wait_for_futures)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/tracers/evaluation.py#L38)
