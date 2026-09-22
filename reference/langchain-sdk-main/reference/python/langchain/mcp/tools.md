---
title: "tools"
description: "Convert MCP tools and tool results into LangChain-native values."
source: "https://reference.langchain.com/python/langchain/mcp/tools"
category: "reference"
tags: [reference, langchain, mcp, tools]
---

# tools

> **Module** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/mcp/tools)

Convert MCP tools and tool results into LangChain-native values.

Tool results follow `langchain-mcp-adapters`, so a call made through
`langchain.mcp` reaches a model in the same shape as one loaded by that
package. Tool *metadata* is richer here: it is grouped under a single `mcp`
namespace with the tool's annotations and `_meta` under `mcp.tool` and the
serving server's identity under `mcp.server`.

## Methods

- [`as_langchain_tool()`](https://reference.langchain.com/python/langchain/mcp/tools/as_langchain_tool)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/mcp/tools.py)
