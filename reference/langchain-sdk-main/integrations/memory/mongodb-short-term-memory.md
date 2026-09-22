---
title: "Short-term memory with MongoDB Atlas"
description: "Persist agent short-term memory with MongoDBSaver and MongoDB Atlas."
source: "https://docs.langchain.com/oss/python/integrations/memory/mongodb-short-term-memory"
category: "docs"
tags: [docs, integrations, memory, mongodb-short-term-memory]
---

# Short-term memory with MongoDB Atlas

> Persist agent short-term memory with MongoDBSaver and MongoDB Atlas.

[Short-term memory](../../langchain/short-term-memory.md) lets your agent remember previous interactions within a single thread or conversation. This guide shows how to use [MongoDB Atlas](https://www.mongodb.com/docs/atlas/) as the persistent checkpointer backend.

MongoDB stores conversation state as documents in a collection, so threads can resume across process restarts and deployments.

> [!TIP]
> Need to remember information **across** conversations? Use [long-term memory with MongoDB Atlas](mongodb-long-term-memory.md) to store and recall data across different threads and sessions.

## Setup

### Installation

**pip**

```bash
pip install -U langgraph-checkpoint-mongodb pymongo
```

**uv**

```bash
uv add langgraph-checkpoint-mongodb pymongo
```

### Credentials

Set your Atlas connection string:

```python
import getpass
import os

if not os.environ.get("MONGODB_ATLAS_URI"):
    os.environ["MONGODB_ATLAS_URI"] = getpass.getpass("Enter your MongoDB Atlas URI: ")
```

If you want automated tracing of your model calls, set your [LangSmith](../../langsmith/home.md) API key:

```python
if not os.environ.get("LANGSMITH_API_KEY"):
    os.environ["LANGSMITH_API_KEY"] = getpass.getpass("Enter your LangSmith API key: ")
os.environ["LANGSMITH_TRACING"] = "true"
```

## Usage

Create a `MongoDBSaver` with `from_conn_string` and pass it to `create_agent`. The context manager creates the required collections and indexes when it opens. You do not call a separate `setup()` method (unlike the Postgres checkpointer).

```python
import os

from langchain.agents import create_agent
from langgraph.checkpoint.mongodb import MongoDBSaver

def get_user_info() -> str:
    """Look up information about the current user."""
    return "No user profile on file."

MONGODB_ATLAS_URI = os.environ["MONGODB_ATLAS_URI"]

with MongoDBSaver.from_conn_string(MONGODB_ATLAS_URI) as checkpointer:
    agent = create_agent(
        "anthropic:claude-sonnet-4-6",
        tools=[get_user_info],
        checkpointer=checkpointer,
    )

    thread_config = {"configurable": {"thread_id": "1"}}
    response = agent.invoke(
        {"messages": [{"role": "user", "content": "Hi! My name is Bob."}]},
        thread_config,
    )["messages"][-1].content

    print(response)

    response = agent.invoke(
        {"messages": [{"role": "user", "content": "What's my name?"}]},
        thread_config,
    )["messages"][-1].content

    print(response)
```

`MongoDBSaver` also exposes async methods such as `aget` and `aput` for use in async graphs. There is no separate `AsyncMongoDBSaver` class.

## Next steps

* Customize agent state, trim or summarize history, and access memory from tools in the [short-term memory](../../langchain/short-term-memory.md) guide. Pass the same `MongoDBSaver` as `checkpointer`.
* See the [checkpointer integrations](../checkpointers.md) list for other backends.
* For cross-thread persistence, see [long-term memory with MongoDB Atlas](mongodb-long-term-memory.md).

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/memory/mongodb-short-term-memory.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
