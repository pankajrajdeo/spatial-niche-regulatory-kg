---
title: "How to retry failed runs in experiments (Python only)"
description: "When running evaluations on large datasets, you may encounter failures on a small subset of examples due to rate limits, network issues, or other transient errors. Rather than re-running the entire..."
source: "https://docs.langchain.com/langsmith/evaluate-with-retry"
category: "docs"
tags: [docs, langsmith, evaluate-with-retry]
---

# How to retry failed runs in experiments (Python only)

When running [evaluations](evaluation-concepts.md#evaluation-lifecycle) on large [datasets](evaluation-concepts.md#datasets), you may encounter failures on a small subset of examples due to rate limits, network issues, or other transient errors. Rather than re-running the entire evaluation, you can identify and retry only the failed examples on an [experiment](evaluation-concepts.md#experiment).

This guide shows an approach to build retry logic into your evaluation workflow and to retry only the failed examples. You can use the `error_handling='ignore'` parameter to skip logging errored runs, then automatically identify unsuccessful examples and re-run them in Python.

## Step 1. Run the initial evaluation

Run the initial evaluation, ignoring errors to  prevent errored runs from being logged:

```python
from langsmith import Client

client = Client()

# Run initial evaluation, ignoring errors
# error_handling='ignore' prevents errored runs from being logged
results = await client.aevaluate(
    target,
    data="dataset",
    evaluators=[your_evaluators],
    error_handling='ignore'
)
```

## Step 2. Retry on failed examples and log to same experiment

Fetch all the unsuccessful examples:

```python
# Identify unsuccessful examples
runs = client.list_runs(project_name=results.experiment_name)
successful_example_ids = [r.reference_example_id for r in runs]
unsuccessful_examples = (e for e in client.list_examples(dataset_name="dataset") if e.id not in successful_examples)
```

Next, re-run all the failed examples and log them to the same experiment:

```python
# Retry only the failed examples, log
results_retry = await client.aevaluate(
    target,
    unsuccessful_examples,
    evaluators=[your_evaluators],
    experiment=results.experiment_name,
    error_handling='ignore'
)
```

## Related topics

* [Run an evaluation](evaluate-llm-application.md)
* [Run an evaluation asynchronously](evaluation-async.md)
* [Handle model rate limits](handle-model-rate-limiting.md)
* [Experiment configuration](experiment-configuration.md)
* [Evaluate existing experiment](evaluate-existing-experiment.md)

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/evaluate-with-retry.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
