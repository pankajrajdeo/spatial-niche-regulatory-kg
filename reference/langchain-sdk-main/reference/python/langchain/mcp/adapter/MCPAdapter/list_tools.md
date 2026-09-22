---
title: "list_tools"
description: "Discover and adapt MCP tools for use with LangChain."
source: "https://reference.langchain.com/python/langchain/mcp/adapter/MCPAdapter/list_tools"
category: "reference"
tags: [reference, langchain, mcp, adapter, mcpadapter, list_tools]
---

# list_tools

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/mcp/adapter/MCPAdapter/list_tools)

Discover and adapt MCP tools for use with LangChain.

## Signature

```python
list_tools(
    self,
    *,
    cache_mode: CacheMode = 'use',
) -> list[BaseTool]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `cache_mode` | `CacheMode` | No | How discovery interacts with the client-side response cache (SEP-2549). `use` serves a cached tool list when one is present and still within the server's TTL hint, `refresh` calls the server and repopulates the cache, and `bypass` skips the cache entirely. The cache and its per-principal isolation are configured on the client itself (`Client(cache=...)`); this only selects how discovery reads it. Defaults to `use` so a configured cache is honored — note this differs from a bare `ClientGroup.list_tools()`, whose own default is `refresh`. (default: `'use'`) |

## Returns

`list[BaseTool]`

LangChain tools that invoke the corresponding MCP tools
asynchronously. Each holds the adapter's client, so the tools
stay callable after this adapter's context exits.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/mcp/adapter.py#L221)
