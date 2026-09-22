---
title: "description"
description: "The description attached to the request for human input."
source: "https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/InterruptOnConfig/description"
category: "reference"
tags: [reference, langchain, agents, middleware, human_in_the_loop, interruptonconfig, description]
---

# description

> **Attribute** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/InterruptOnConfig/description)

The description attached to the request for human input.

Can be either:

- A static string describing the approval request
- A callable that dynamically generates the description based on agent state,
    runtime, and tool call information

## Signature

```python
description: NotRequired[str | _DescriptionFactory]
```

## Description

**Example:**

```python
# Static string description
config = InterruptOnConfig(
    allowed_decisions=["approve", "reject"],
    description="Please review this tool execution"
)

# Dynamic callable description
def format_tool_description(
    tool_call: ToolCall,
    state: AgentState,
    runtime: Runtime[ContextT]
) -> str:
    import json
    return (
        f"Tool: {tool_call['name']}\n"
        f"Arguments:\n{json.dumps(tool_call['args'], indent=2)}"
    )

config = InterruptOnConfig(
    allowed_decisions=["approve", "edit", "reject"],
    description=format_tool_description
)
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/human_in_the_loop.py#L171)
