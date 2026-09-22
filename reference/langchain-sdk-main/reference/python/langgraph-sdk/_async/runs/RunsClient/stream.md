---
title: "stream"
description: "Create a run and stream the results."
source: "https://reference.langchain.com/python/langgraph-sdk/_async/runs/RunsClient/stream"
category: "reference"
tags: [reference, langgraph-sdk, async, runs, runsclient, stream]
---

# stream

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_async/runs/RunsClient/stream)

Create a run and stream the results.

## Signature

```python
stream(
    self,
    thread_id: str | None,
    assistant_id: str,
    *,
    input: Input | None = None,
    command: Command | None = None,
    stream_mode: StreamMode | Sequence[StreamMode] = 'values',
    stream_subgraphs: bool = False,
    stream_resumable: bool = False,
    metadata: Mapping[str, Any] | None = None,
    config: Config | None = None,
    context: Context | None = None,
    checkpoint: Checkpoint | None = None,
    checkpoint_id: str | None = None,
    checkpoint_during: bool | None = None,
    interrupt_before: All | Sequence[str] | None = None,
    interrupt_after: All | Sequence[str] | None = None,
    feedback_keys: Sequence[str] | None = None,
    on_disconnect: DisconnectMode | None = None,
    on_completion: OnCompletionBehavior | None = None,
    webhook: str | None = None,
    multitask_strategy: MultitaskStrategy | None = None,
    if_not_exists: IfNotExists | None = None,
    after_seconds: int | None = None,
    langsmith_tracing: LangSmithTracing | None = None,
    headers: Mapping[str, str] | None = None,
    params: QueryParamTypes | None = None,
    on_run_created: Callable[[RunCreateMetadata], None] | None = None,
    durability: Durability | None = None,
    version: StreamVersion = 'v1',
) -> AsyncIterator[StreamPart | StreamPartV2]
```

## Description

???+ example "Example Usage"

```python
client = get_client(url="http://localhost:2024)
async for chunk in client.runs.stream(
    thread_id=None,
    assistant_id="agent",
    input={"messages": [{"role": "user", "content": "how are you?"}]},
    stream_mode=["values","debug"],
    metadata={"name":"my_run"},
    context={"model_name": "anthropic"},
    interrupt_before=["node_to_stop_before_1","node_to_stop_before_2"],
    interrupt_after=["node_to_stop_after_1","node_to_stop_after_2"],
    feedback_keys=["my_feedback_key_1","my_feedback_key_2"],
    webhook="https://my.fake.webhook.com",
    multitask_strategy="interrupt"
):
    print(chunk)
```

```shell

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

StreamPart(event='metadata', data={'run_id': '1ef4a9b8-d7da-679a-a45a-872054341df2'})
StreamPart(event='values', data={'messages': [{'content': 'how are you?', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': 'fe0a5778-cfe9-42ee-b807-0adaa1873c10', 'example': False}]})
StreamPart(event='values', data={'messages': [{'content': 'how are you?', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': 'fe0a5778-cfe9-42ee-b807-0adaa1873c10', 'example': False}, {'content': "I'm doing well, thanks for asking! I'm an AI assistant created by Anthropic to be helpful, honest, and harmless.", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-159b782c-b679-4830-83c6-cef87798fe8b', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}]})
StreamPart(event='end', data=None)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `thread_id` | `str \| None` | Yes | the thread ID to assign to the thread. If `None` will create a stateless run. |
| `assistant_id` | `str` | Yes | The assistant ID or graph name to stream from. If using graph name, will default to first assistant created from that graph. |
| `input` | `Input \| None` | No | The input to the graph. (default: `None`) |
| `command` | `Command \| None` | No | A command to execute. Cannot be combined with input. (default: `None`) |
| `stream_mode` | `StreamMode \| Sequence[StreamMode]` | No | The stream mode(s) to use. (default: `'values'`) |
| `stream_subgraphs` | `bool` | No | Whether to stream output from subgraphs. (default: `False`) |
| `stream_resumable` | `bool` | No | Whether the stream is considered resumable. If true, the stream can be resumed and replayed in its entirety even after disconnection. (default: `False`) |
| `metadata` | `Mapping[str, Any] \| None` | No | Metadata to assign to the run. (default: `None`) |
| `config` | `Config \| None` | No | The configuration for the assistant. (default: `None`) |
| `context` | `Context \| None` | No | Static context to add to the assistant. !!! version-added "Added in version 0.6.0" (default: `None`) |
| `checkpoint` | `Checkpoint \| None` | No | The checkpoint to resume from. (default: `None`) |
| `checkpoint_during` | `bool \| None` | No | (deprecated) Whether to checkpoint during the run (or only at the end/interruption). (default: `None`) |
| `interrupt_before` | `All \| Sequence[str] \| None` | No | Nodes to interrupt immediately before they get executed. (default: `None`) |
| `interrupt_after` | `All \| Sequence[str] \| None` | No | Nodes to Nodes to interrupt immediately after they get executed. (default: `None`) |
| `feedback_keys` | `Sequence[str] \| None` | No | Feedback keys to assign to run. (default: `None`) |
| `on_disconnect` | `DisconnectMode \| None` | No | The disconnect mode to use. Must be one of 'cancel' or 'continue'. (default: `None`) |
| `on_completion` | `OnCompletionBehavior \| None` | No | Whether to delete or keep the thread created for a stateless run. Must be one of 'delete' or 'keep'. (default: `None`) |
| `webhook` | `str \| None` | No | Webhook to call after LangGraph API call is done. (default: `None`) |
| `multitask_strategy` | `MultitaskStrategy \| None` | No | Multitask strategy to use. Must be one of 'reject', 'interrupt', 'rollback', or 'enqueue'. (default: `None`) |
| `if_not_exists` | `IfNotExists \| None` | No | How to handle missing thread. Defaults to 'reject'. Must be either 'reject' (raise error if missing), or 'create' (create new thread). (default: `None`) |
| `after_seconds` | `int \| None` | No | The number of seconds to wait before starting the run. Use to schedule future runs. (default: `None`) |
| `langsmith_tracing` | `LangSmithTracing \| None` | No | LangSmith tracing configuration. Allows routing traces to a specific project or associating with a dataset example. (default: `None`) |
| `headers` | `Mapping[str, str] \| None` | No | Optional custom headers to include with the request. (default: `None`) |
| `params` | `QueryParamTypes \| None` | No | Optional query parameters to include with the request. (default: `None`) |
| `on_run_created` | `Callable[[RunCreateMetadata], None] \| None` | No | Callback when a run is created. (default: `None`) |
| `durability` | `Durability \| None` | No | The durability to use for the run. Values are "sync", "async", or "exit". "async" means checkpoints are persisted async while next graph step executes, replaces checkpoint_during=True "sync" means checkpoints are persisted sync after graph step executes, replaces checkpoint_during=False "exit" means checkpoints are only persisted when the run exits, does not save intermediate steps (default: `None`) |
| `version` | `StreamVersion` | No | Stream format version. "v1" (default) returns raw SSE StreamPart NamedTuples. "v2" returns typed dicts with `type`, `ns`, and `data` keys. (default: `'v1'`) |

## Returns

`AsyncIterator[StreamPart | StreamPartV2]`

Asynchronous iterator of stream results.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_async/runs.py#L195)
