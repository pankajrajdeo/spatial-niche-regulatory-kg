---
title: "wait"
description: "Create a run, wait until it finishes and return the final state."
source: "https://reference.langchain.com/python/langgraph-sdk/_sync/runs/SyncRunsClient/wait"
category: "reference"
tags: [reference, langgraph-sdk, sync, runs, syncrunsclient, wait]
---

# wait

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_sync/runs/SyncRunsClient/wait)

Create a run, wait until it finishes and return the final state.

## Signature

```python
wait(
    self,
    thread_id: str | None,
    assistant_id: str,
    *,
    input: Input | None = None,
    command: Command | None = None,
    metadata: Mapping[str, Any] | None = None,
    config: Config | None = None,
    context: Context | None = None,
    checkpoint_during: bool | None = None,
    checkpoint: Checkpoint | None = None,
    checkpoint_id: str | None = None,
    interrupt_before: All | Sequence[str] | None = None,
    interrupt_after: All | Sequence[str] | None = None,
    webhook: str | None = None,
    on_disconnect: DisconnectMode | None = None,
    on_completion: OnCompletionBehavior | None = None,
    multitask_strategy: MultitaskStrategy | None = None,
    if_not_exists: IfNotExists | None = None,
    after_seconds: int | None = None,
    langsmith_tracing: LangSmithTracing | None = None,
    raise_error: bool = True,
    headers: Mapping[str, str] | None = None,
    params: QueryParamTypes | None = None,
    on_run_created: Callable[[RunCreateMetadata], None] | None = None,
    durability: Durability | None = None,
) -> builtins.list[dict] | dict[str, Any]
```

## Description

???+ example "Example Usage"

```python

final_state_of_run = client.runs.wait(
    thread_id=None,
    assistant_id="agent",
    input={"messages": [{"role": "user", "content": "how are you?"}]},
    metadata={"name":"my_run"},
    context={"model_name": "anthropic"},
    interrupt_before=["node_to_stop_before_1","node_to_stop_before_2"],
    interrupt_after=["node_to_stop_after_1","node_to_stop_after_2"],
    webhook="https://my.fake.webhook.com",
    multitask_strategy="interrupt"
)
print(final_state_of_run)
```

```shell

-------------------------------------------------------------------------------------------------------------------------------------------

{
    'messages': [
        {
            'content': 'how are you?',
            'additional_kwargs': {},
            'response_metadata': {},
            'type': 'human',
            'name': None,
            'id': 'f51a862c-62fe-4866-863b-b0863e8ad78a',
            'example': False
        },
        {
            'content': "I'm doing well, thanks for asking! I'm an AI assistant created by Anthropic to be helpful, honest, and harmless.",
            'additional_kwargs': {},
            'response_metadata': {},
            'type': 'ai',
            'name': None,
            'id': 'run-bf1cd3c6-768f-4c16-b62d-ba6f17ad8b36',
            'example': False,
            'tool_calls': [],
            'invalid_tool_calls': [],
            'usage_metadata': None
        }
    ]
}
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `thread_id` | `str \| None` | Yes | the thread ID to create the run on. If `None` will create a stateless run. |
| `assistant_id` | `str` | Yes | The assistant ID or graph name to run. If using graph name, will default to first assistant created from that graph. |
| `input` | `Input \| None` | No | The input to the graph. (default: `None`) |
| `command` | `Command \| None` | No | The command to execute. (default: `None`) |
| `metadata` | `Mapping[str, Any] \| None` | No | Metadata to assign to the run. (default: `None`) |
| `config` | `Config \| None` | No | The configuration for the assistant. (default: `None`) |
| `context` | `Context \| None` | No | Static context to add to the assistant. !!! version-added "Added in version 0.6.0" (default: `None`) |
| `checkpoint` | `Checkpoint \| None` | No | The checkpoint to resume from. (default: `None`) |
| `checkpoint_during` | `bool \| None` | No | (deprecated) Whether to checkpoint during the run (or only at the end/interruption). (default: `None`) |
| `interrupt_before` | `All \| Sequence[str] \| None` | No | Nodes to interrupt immediately before they get executed. (default: `None`) |
| `interrupt_after` | `All \| Sequence[str] \| None` | No | Nodes to Nodes to interrupt immediately after they get executed. (default: `None`) |
| `webhook` | `str \| None` | No | Webhook to call after LangGraph API call is done. (default: `None`) |
| `on_disconnect` | `DisconnectMode \| None` | No | The disconnect mode to use. Must be one of 'cancel' or 'continue'. (default: `None`) |
| `on_completion` | `OnCompletionBehavior \| None` | No | Whether to delete or keep the thread created for a stateless run. Must be one of 'delete' or 'keep'. (default: `None`) |
| `multitask_strategy` | `MultitaskStrategy \| None` | No | Multitask strategy to use. Must be one of 'reject', 'interrupt', 'rollback', or 'enqueue'. (default: `None`) |
| `if_not_exists` | `IfNotExists \| None` | No | How to handle missing thread. Defaults to 'reject'. Must be either 'reject' (raise error if missing), or 'create' (create new thread). (default: `None`) |
| `after_seconds` | `int \| None` | No | The number of seconds to wait before starting the run. Use to schedule future runs. (default: `None`) |
| `langsmith_tracing` | `LangSmithTracing \| None` | No | LangSmith tracing configuration. Allows routing traces to a specific project or associating with a dataset example. (default: `None`) |
| `raise_error` | `bool` | No | Whether to raise an error if the run fails. (default: `True`) |
| `headers` | `Mapping[str, str] \| None` | No | Optional custom headers to include with the request. (default: `None`) |
| `on_run_created` | `Callable[[RunCreateMetadata], None] \| None` | No | Optional callback to call when a run is created. (default: `None`) |
| `durability` | `Durability \| None` | No | The durability to use for the run. Values are "sync", "async", or "exit". "async" means checkpoints are persisted async while next graph step executes, replaces checkpoint_during=True "sync" means checkpoints are persisted sync after graph step executes, replaces checkpoint_during=False "exit" means checkpoints are only persisted when the run exits, does not save intermediate steps (default: `None`) |

## Returns

`builtins.list[dict] | dict[str, Any]`

The output of the `Run`.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_sync/runs.py#L673)
