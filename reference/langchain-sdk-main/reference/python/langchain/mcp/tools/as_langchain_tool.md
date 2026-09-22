---
title: "as_langchain_tool"
description: "Convert one MCP tool into a LangChain tool."
source: "https://reference.langchain.com/python/langchain/mcp/tools/as_langchain_tool"
category: "reference"
tags: [reference, langchain, mcp, tools, as_langchain_tool]
---

# as_langchain_tool

> **Function** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/mcp/tools/as_langchain_tool)

Convert one MCP tool into a LangChain tool.

The returned tool calls the MCP tool through `client` on every invocation.
FastMCP clients are reentrant, so the tool can open the client itself
whether or not a connection is already held elsewhere.

A server that needs input mid-call is answered with a LangGraph
`interrupt()` when `client` carries the interrupt-driving sentinel handler
that `MCPAdapter` installs — so a human answers and the call resumes, see
`langchain.mcp.elicitation`. A client that carries a different handler (a
caller's own) uses that handler instead, and one with no handler simply
never gets asked. Which path a call takes is read off the client, so the
behavior matches whatever it was armed with.

An MCP tool that runs and reports failure reaches the model as a
`ToolMessage` with `status="error"`, carrying the server's own error
content, so an agent can correct itself and retry. Transport failures and
unconvertible content propagate instead, since a model cannot act on them.

## Signature

```python
as_langchain_tool(
    tool: Tool,
    client: Client[Any] | ClientGroup,
) -> BaseTool
```

## Description

**Example:**

```python
from fastmcp import Client

from langchain.mcp import as_langchain_tool

client = Client("https://example.com/mcp")
async with client:
    mcp_tools = await client.list_tools()
tools = [await as_langchain_tool(t, client) for t in mcp_tools]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `tool` | `Tool` | Yes | An MCP tool, as returned by `fastmcp.Client.list_tools`. |
| `client` | `Client[Any] \| ClientGroup` | Yes | The FastMCP client to call the tool through. |

## Returns

`BaseTool`

A LangChain tool that invokes the MCP tool asynchronously.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/mcp/tools.py#L234)
