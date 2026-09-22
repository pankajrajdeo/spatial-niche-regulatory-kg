---
title: "abefore_agent"
description: "Load skills metadata before agent execution (async)."
source: "https://reference.langchain.com/python/deepagents/middleware/skills/SkillsMiddleware/abefore_agent"
category: "reference"
tags: [reference, deepagents, middleware, skills, skillsmiddleware, abefore_agent]
---

# abefore_agent

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/skills/SkillsMiddleware/abefore_agent)

Load skills metadata before agent execution (async).

Loads skills once per session from all configured sources. If
`skills_metadata` is already present in state (from a prior turn or
checkpointed session), the load is skipped and `None` is returned.

Skills are loaded in source order with later sources overriding
earlier ones if they contain skills with the same name (last one wins).

## Signature

```python
abefore_agent(
    self,
    state: SkillsState,
    runtime: Runtime,
    config: RunnableConfig,
) -> SkillsStateUpdate | None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `state` | `SkillsState` | Yes | Current agent state. |
| `runtime` | `Runtime` | Yes | Runtime context. |
| `config` | `RunnableConfig` | Yes | Runnable config. |

## Returns

`SkillsStateUpdate | None`

State update with `skills_metadata` populated, or `None` if already present.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/skills.py#L978)
