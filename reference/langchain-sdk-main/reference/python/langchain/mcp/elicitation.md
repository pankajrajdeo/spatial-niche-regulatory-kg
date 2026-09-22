---
title: "elicitation"
description: "Answer MCP elicitation requests with a LangGraph interrupt."
source: "https://reference.langchain.com/python/langchain/mcp/elicitation"
category: "reference"
tags: [reference, langchain, mcp, elicitation]
---

# elicitation

> **Module** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/mcp/elicitation)

Answer MCP elicitation requests with a LangGraph interrupt.

A server needing input mid-call returns an `InputRequiredResult` and expects the
`tools/call` to be retried with answers. This module drives that loop, sourcing
each answer from `interrupt()` so the human reviewing the agent answers too.

We drive the loop here rather than via the SDK's `run_input_required_driver`
because that driver answers from callbacks run concurrently in a task group:
LangGraph matches resume values to `interrupt()` calls by order, so concurrent
firing scrambles the matching, and FastMCP would swallow the `GraphInterrupt` as
an MCP error. Calling `interrupt()` from this frame keeps one per round.

Only elicitation is answered. Sampling, roots, and continuation rounds are
refused rather than half-served.

## Properties

- `ELICITATION_INTERRUPT_TYPE`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/mcp/elicitation.py)
