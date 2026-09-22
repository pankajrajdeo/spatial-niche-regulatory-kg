---
title: "CronClient"
description: "Client for managing recurrent runs (cron jobs) in LangGraph."
source: "https://reference.langchain.com/python/langgraph-sdk/_async/cron/CronClient"
category: "reference"
tags: [reference, langgraph-sdk, async, cron, cronclient]
---

# CronClient

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_async/cron/CronClient)

Client for managing recurrent runs (cron jobs) in LangGraph.

A run is a single invocation of an assistant with optional input, config, and context.
This client allows scheduling recurring runs to occur automatically.

???+ example "Example Usage"

```python
    client = get_client(url="http://localhost:2024"))
    cron_job = await client.crons.create_for_thread(
        thread_id="thread_123",
        assistant_id="asst_456",
        schedule="0 9 * * *",
        input={"message": "Daily update"}
    )
```

!!! note "Feature Availability"

    The crons client functionality is not supported on all licenses.
    Please check the relevant license documentation for the most up-to-date
    details on feature availability.

## Signature

```python
CronClient(
    self,
    http_client: HttpClient,
)
```

## Constructors

```python
__init__(
    self,
    http_client: HttpClient,
) -> None
```

| Name | Type |
|------|------|
| `http_client` | `HttpClient` |

## Properties

- `http`

## Methods

- [`create_for_thread()`](https://reference.langchain.com/python/langgraph-sdk/_async/cron/CronClient/create_for_thread)
- [`create()`](https://reference.langchain.com/python/langgraph-sdk/_async/cron/CronClient/create)
- [`delete()`](https://reference.langchain.com/python/langgraph-sdk/_async/cron/CronClient/delete)
- [`update()`](https://reference.langchain.com/python/langgraph-sdk/_async/cron/CronClient/update)
- [`search()`](https://reference.langchain.com/python/langgraph-sdk/_async/cron/CronClient/search)
- [`count()`](https://reference.langchain.com/python/langgraph-sdk/_async/cron/CronClient/count)

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_async/cron.py#L34)
