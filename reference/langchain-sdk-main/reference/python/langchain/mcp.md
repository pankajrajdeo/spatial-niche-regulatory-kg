---
title: "mcp"
description: "LangChain MCP adapters for connecting MCP servers with LangChain applications."
source: "https://reference.langchain.com/python/langchain/mcp"
category: "reference"
tags: [reference, langchain, mcp]
---

# mcp

> **Module** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/mcp)

LangChain MCP adapters for connecting MCP servers with LangChain applications.

Interrupt-driven elicitation has its own types — the interrupt payload, the
answers a run resumes with, and the discriminator to recognize them by. Import
those from `langchain.mcp.elicitation`.

!!! warning "This namespace is in beta"

    `langchain.mcp` is actively being worked on and its API may change. Importing
    from it raises a `LangChainBetaWarning` once per process. Silence it with
    `warnings.filterwarnings("ignore", category=LangChainBetaWarning)`, or scope
    the suppression with `langchain_core._api.suppress_langchain_beta_warning()`.

## Methods

- [`as_langchain_tool()`](https://reference.langchain.com/python/langchain/mcp/as_langchain_tool)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/mcp/__init__.py)
