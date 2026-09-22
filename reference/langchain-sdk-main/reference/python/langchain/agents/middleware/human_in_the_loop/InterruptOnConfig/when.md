---
title: "when"
description: "Optional predicate controlling whether to interrupt for a given tool call."
source: "https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/InterruptOnConfig/when"
category: "reference"
tags: [reference, langchain, agents, middleware, human_in_the_loop, interruptonconfig, when]
---

# when

> **Attribute** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/InterruptOnConfig/when)

Optional predicate controlling whether to interrupt for a given tool call.

Receives a `ToolCallRequest` and returns `True` to interrupt or `False` to
auto-approve. The predicate is called during `after_model` before the tool
call is added to the batched human-in-the-loop request.

The request is constructed with `tool=None` and a new `ToolRuntime`. The
`ToolRuntime` copies `context`, `store`, `stream_writer`, `execution_info`,
and `server_info` from the node-level `Runtime`, while `tool_call_id` is
populated from the current tool call. The `tools` argument is not supplied,
so it uses its default empty list.

## Signature

```python
when: NotRequired[Callable[[ToolCallRequest], bool]]
```

## Description

**Example:**

```python
# Only interrupt delete_file calls targeting /etc
config = InterruptOnConfig(
    allowed_decisions=["approve", "reject"],
    when=lambda req: req.tool_call["args"].get("path", "").startswith("/etc"),
)
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/human_in_the_loop.py#L209)
