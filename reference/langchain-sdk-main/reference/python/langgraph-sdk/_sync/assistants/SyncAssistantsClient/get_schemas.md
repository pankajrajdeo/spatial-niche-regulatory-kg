---
title: "get_schemas"
description: "Get the schemas of an assistant by ID."
source: "https://reference.langchain.com/python/langgraph-sdk/_sync/assistants/SyncAssistantsClient/get_schemas"
category: "reference"
tags: [reference, langgraph-sdk, sync, assistants, syncassistantsclient, get_schemas]
---

# get_schemas

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_sync/assistants/SyncAssistantsClient/get_schemas)

Get the schemas of an assistant by ID.

## Signature

```python
get_schemas(
    self,
    assistant_id: str,
    *,
    headers: Mapping[str, str] | None = None,
    params: QueryParamTypes | None = None,
) -> GraphSchema
```

## Description

???+ example "Example Usage"

```python
client = get_sync_client(url="http://localhost:2024")
schema = client.assistants.get_schemas(
    assistant_id="my_assistant_id"
)
print(schema)
```
```shell
----------------------------------------------------------------------------------------------------------------------------

{
    'graph_id': 'agent',
    'state_schema':
        {
            'title': 'LangGraphInput',
            '$ref': '#/definitions/AgentState',
            'definitions':
                {
                    'BaseMessage':
                        {
                            'title': 'BaseMessage',
                            'description': 'Base abstract Message class. Messages are the inputs and outputs of ChatModels.',
                            'type': 'object',
                            'properties':
                                {
                                 'content':
                                    {
                                        'title': 'Content',
                                        'anyOf': [
                                            {'type': 'string'},
                                            {'type': 'array','items': {'anyOf': [{'type': 'string'}, {'type': 'object'}]}}
                                        ]
                                    },
                                'additional_kwargs':
                                    {
                                        'title': 'Additional Kwargs',
                                        'type': 'object'
                                    },
                                'response_metadata':
                                    {
                                        'title': 'Response Metadata',
                                        'type': 'object'
                                    },
                                'type':
                                    {
                                        'title': 'Type',
                                        'type': 'string'
                                    },
                                'name':
                                    {
                                        'title': 'Name',
                                        'type': 'string'
                                    },
                                'id':
                                    {
                                        'title': 'Id',
                                        'type': 'string'
                                    }
                                },
                            'required': ['content', 'type']
                        },
                    'AgentState':
                        {
                            'title': 'AgentState',
                            'type': 'object',
                            'properties':
                                {
                                    'messages':
                                        {
                                            'title': 'Messages',
                                            'type': 'array',
                                            'items': {'$ref': '#/definitions/BaseMessage'}
                                        }
                                },
                            'required': ['messages']
                        }
                }
        },
    'config_schema':
        {
            'title': 'Configurable',
            'type': 'object',
            'properties':
                {
                    'model_name':
                        {
                            'title': 'Model Name',
                            'enum': ['anthropic', 'openai'],
                            'type': 'string'
                        }
                }
        },
    'context_schema':
        {
            'title': 'Context',
            'type': 'object',
            'properties':
                {
                    'model_name':
                        {
                            'title': 'Model Name',
                            'enum': ['anthropic', 'openai'],
                            'type': 'string'
                        }
                }
        }
}
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `assistant_id` | `str` | Yes | The ID of the assistant to get the schema of. |
| `headers` | `Mapping[str, str] \| None` | No | Optional custom headers to include with the request. (default: `None`) |
| `params` | `QueryParamTypes \| None` | No | Optional query parameters to include with the request. (default: `None`) |

## Returns

`GraphSchema`

The graph schema for the assistant.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_sync/assistants.py#L147)
