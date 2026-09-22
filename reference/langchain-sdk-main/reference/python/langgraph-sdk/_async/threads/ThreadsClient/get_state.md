---
title: "get_state"
description: "Get the state of a thread."
source: "https://reference.langchain.com/python/langgraph-sdk/_async/threads/ThreadsClient/get_state"
category: "reference"
tags: [reference, langgraph-sdk, async, threads, threadsclient, get_state]
---

# get_state

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_async/threads/ThreadsClient/get_state)

Get the state of a thread.

## Signature

```python
get_state(
    self,
    thread_id: str,
    checkpoint: Checkpoint | None = None,
    checkpoint_id: str | None = None,
    *,
    subgraphs: bool = False,
    headers: Mapping[str, str] | None = None,
    params: QueryParamTypes | None = None,
) -> ThreadState
```

## Description

???+ example "Example Usage"

```python
client = get_client(url="http://localhost:2024)
thread_state = await client.threads.get_state(
    thread_id="my_thread_id",
    checkpoint_id="my_checkpoint_id"
)
print(thread_state)
```

```shell
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

{
    'values': {
        'messages': [
            {
                'content': 'how are you?',
                'additional_kwargs': {},
                'response_metadata': {},
                'type': 'human',
                'name': None,
                'id': 'fe0a5778-cfe9-42ee-b807-0adaa1873c10',
                'example': False
            },
            {
                'content': "I'm doing well, thanks for asking! I'm an AI assistant created by Anthropic to be helpful, honest, and harmless.",
                'additional_kwargs': {},
                'response_metadata': {},
                'type': 'ai',
                'name': None,
                'id': 'run-159b782c-b679-4830-83c6-cef87798fe8b',
                'example': False,
                'tool_calls': [],
                'invalid_tool_calls': [],
                'usage_metadata': None
            }
        ]
    },
    'next': [],
    'checkpoint':
        {
            'thread_id': 'e2496803-ecd5-4e0c-a779-3226296181c2',
            'checkpoint_ns': '',
            'checkpoint_id': '1ef4a9b8-e6fb-67b1-8001-abd5184439d1'
        }
    'metadata':
        {
            'step': 1,
            'run_id': '1ef4a9b8-d7da-679a-a45a-872054341df2',
            'source': 'loop',
            'writes':
                {
                    'agent':
                        {
                            'messages': [
                                {
                                    'id': 'run-159b782c-b679-4830-83c6-cef87798fe8b',
                                    'name': None,
                                    'type': 'ai',
                                    'content': "I'm doing well, thanks for asking! I'm an AI assistant created by Anthropic to be helpful, honest, and harmless.",
                                    'example': False,
                                    'tool_calls': [],
                                    'usage_metadata': None,
                                    'additional_kwargs': {},
                                    'response_metadata': {},
                                    'invalid_tool_calls': []
                                }
                            ]
                        }
                },
    'user_id': None,
    'graph_id': 'agent',
    'thread_id': 'e2496803-ecd5-4e0c-a779-3226296181c2',
    'created_by': 'system',
    'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca'},
    'created_at': '2024-07-25T15:35:44.184703+00:00',
    'parent_config':
        {
            'thread_id': 'e2496803-ecd5-4e0c-a779-3226296181c2',
            'checkpoint_ns': '',
            'checkpoint_id': '1ef4a9b8-d80d-6fa7-8000-9300467fad0f'
        }
}
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `thread_id` | `str` | Yes | The ID of the thread to get the state of. |
| `checkpoint` | `Checkpoint \| None` | No | The checkpoint to get the state of. (default: `None`) |
| `checkpoint_id` | `str \| None` | No | (deprecated) The checkpoint ID to get the state of. (default: `None`) |
| `subgraphs` | `bool` | No | Include subgraphs states. (default: `False`) |
| `headers` | `Mapping[str, str] \| None` | No | Optional custom headers to include with the request. (default: `None`) |
| `params` | `QueryParamTypes \| None` | No | Optional query parameters to include with the request. (default: `None`) |

## Returns

`ThreadState`

The thread of the state.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_async/threads.py#L485)
