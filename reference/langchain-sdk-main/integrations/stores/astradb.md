---
title: "AstraDBByteStore integration"
description: "Integrate with the AstraDBByteStore store using LangChain Python."
source: "https://docs.langchain.com/oss/python/integrations/stores/astradb"
category: "docs"
tags: [docs, integrations, stores, astradb]
---

# AstraDBByteStore integration

> Integrate with the AstraDBByteStore store using LangChain Python.

This will help you get started with Astra DB [key-value stores](../stores.md). For detailed documentation of all `AstraDBByteStore` features and configurations head to the [API reference](https://reference.langchain.com/python/langchain-astradb/storage/AstraDBByteStore).

## Overview

> [DataStax Astra DB](https://docs.datastax.com/en/astra-db-serverless/index.html) is a serverless
> AI-ready database built on `Apache Cassandra®` and made conveniently available
> through an easy-to-use JSON API.

### Integration details

| Class                                                                                                   | Package                                                                         | Local | JS support |                                              Downloads                                             |                                             Version                                             |
| :------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------ | :---: | :--------: | :------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------: |
| [`AstraDBByteStore`](https://reference.langchain.com/python/langchain-astradb/storage/AstraDBByteStore) | [`langchain-astradb`](https://reference.langchain.com/python/langchain-astradb) |   ❌   |      ❌     | ![PyPI - Downloads](https://img.shields.io/pypi/dm/langchain_astradb?style=flat-square\&label=%20) | ![PyPI - Version](https://img.shields.io/pypi/v/langchain_astradb?style=flat-square\&label=%20) |

## Setup

To create an `AstraDBByteStore` byte store, you'll need to [create a DataStax account](https://www.datastax.com/products/datastax-astra).

### Credentials

After signing up, set the following credentials:

```python
from getpass import getpass

ASTRA_DB_API_ENDPOINT = getpass("ASTRA_DB_API_ENDPOINT = ")
ASTRA_DB_APPLICATION_TOKEN = getpass("ASTRA_DB_APPLICATION_TOKEN = ")
```

### Installation

The LangChain AstraDB integration lives in the `langchain-astradb` package:

```python
pip install -qU langchain-astradb
```

## Instantiation

Now we can instantiate our byte store:

```python
from langchain_astradb import AstraDBByteStore

kv_store = AstraDBByteStore(
    api_endpoint=ASTRA_DB_API_ENDPOINT,
    token=ASTRA_DB_APPLICATION_TOKEN,
    collection_name="my_store",
)
```

## Usage

You can set data under keys like this using the `mset` method:

```python
kv_store.mset(
    [
        ["key1", b"value1"],
        ["key2", b"value2"],
    ]
)

kv_store.mget(
    [
        "key1",
        "key2",
    ]
)
```

```text
[b'value1', b'value2']
```

And you can delete data using the `mdelete` method:

```python
kv_store.mdelete(
    [
        "key1",
        "key2",
    ]
)

kv_store.mget(
    [
        "key1",
        "key2",
    ]
)
```

```text
[None, None]
```

You can use an `AstraDBByteStore` anywhere you'd use other ByteStores.

***

## API reference

For detailed documentation of all `AstraDBByteStore` features and configurations, head to the [API reference](https://reference.langchain.com/python/langchain-astradb/storage/AstraDBByteStore)

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/stores/astradb.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
