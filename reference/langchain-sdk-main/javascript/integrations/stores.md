---
title: "Store integrations"
description: "Integrate with stores using LangChain JavaScript."
source: "https://docs.langchain.com/oss/javascript/integrations/stores"
category: "docs"
tags: [docs, javascript, integrations, stores]
---

# Store integrations

> Integrate with stores using LangChain JavaScript.

## Overview

LangChain provides a key-value store interface for storing and retrieving data by key. The key-value store interface in LangChain is primarily used for caching [embeddings](embeddings.md).

## Interface

All [`BaseStores`](https://reference.langchain.com/javascript/langchain-core/stores/BaseStore) are **generic** and support the following interface, where `K` represents the key type and `V` represents the value type:

* `mget(keys: K[]): Promise<(V | undefined)[]>`: get the values for multiple keys, returning `undefined` if a key does not exist
* `mset(keyValuePairs: [K, V][]): Promise<void>`: set the values for multiple keys
* `mdelete(keys: K[]): Promise<void>`: delete multiple keys
* `yieldKeys(prefix?: string): AsyncGenerator`: asynchronously yield all keys in the store, optionally filtering by a prefix

The generic nature of the interface allows you to use different types for keys and values. For example, `BaseStore<string, BaseMessage>` would store messages with string keys, while `BaseStore<string, number[]>` would store arrays of numbers.

> [!NOTE]
> Base stores are designed to work with **multiple** key-value pairs at once for efficiency. This saves on network round-trips and may allow for more efficient batch operations in the underlying store.

## Built-in stores for local development

#### [InMemoryStore](stores/in_memory.md)

#### [LocalFileStore](stores/file_system.md)

## Custom stores

You can also implement your own custom store by extending the [`BaseStore`](https://reference.langchain.com/javascript/langchain-core/stores/BaseStore) class. See the [store interface documentation](https://reference.langchain.com/javascript/langchain-core/stores/BaseStore) for more details.

## All key-value stores

| Integration                                                         | Downloads                             |
| :------------------------------------------------------------------ | :------------------------------------ |
| [`InMemoryStore`](stores/in_memory.md)    | <span data-sort-value="-1">N/A</span> |
| [`LocalFileStore`](stores/file_system.md) | <span data-sort-value="-1">N/A</span> |

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/stores/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
