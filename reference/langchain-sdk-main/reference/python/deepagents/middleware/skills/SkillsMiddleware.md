---
title: "SkillsMiddleware"
description: "Middleware for loading and exposing agent skills to the system prompt."
source: "https://reference.langchain.com/python/deepagents/middleware/skills/SkillsMiddleware"
category: "reference"
tags: [reference, deepagents, middleware, skills, skillsmiddleware]
---

# SkillsMiddleware

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/skills/SkillsMiddleware)

Middleware for loading and exposing agent skills to the system prompt.

Loads skills from backend sources and injects them into the system prompt
using progressive disclosure (metadata first, full content on demand).

Skills are loaded in source order with later sources overriding
earlier ones.

## Signature

```python
SkillsMiddleware(
    self,
    *,
    backend: BackendProtocol,
    sources: Sequence[SkillSource],
    system_prompt: str | None = SKILLS_SYSTEM_PROMPT,
)
```

## Description

**Example:**

```python
from deepagents.backends.filesystem import FilesystemBackend

backend = FilesystemBackend(root_dir="/path/to/skills")
middleware = SkillsMiddleware(
    backend=backend,
    sources=[
        "/path/to/skills/user/",
        "/path/to/skills/project/",
        # Pass a (path, label) tuple to disambiguate sources whose
        # leaf directories would otherwise collide
        ("/home/me/.claude/skills", "User Claude"),
        ("/repo/.claude/skills", "Project Claude"),
    ],
)
```

See constructor for the full argument list.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `backend` | `BackendProtocol` | Yes | Backend instance (e.g. `StateBackend()`). |
| `sources` | `Sequence[SkillSource]` | Yes | List of skill sources.  Each entry is either a bare path (e.g. `'/skills/user/'`) or a `(path, label)` tuple (e.g. `('/home/me/.claude/skills', 'User Claude')`). Labels are rendered as `**{label} Skills**` in the system prompt (do not include the trailing `Skills` in your label). |
| `system_prompt` | `str \| None` | No | System-prompt fragment template. Must contain `{skills_locations}`, `{skills_load_warnings}`, and `{skills_list}` slots for runtime substitution. Pass `None` to skip appending entirely (skills are still loaded into `state["skills_metadata"]`). (default: `SKILLS_SYSTEM_PROMPT`) |

## Extends

- `AgentMiddleware[SkillsState, ContextT, ResponseT]`

## Constructors

```python
__init__(
    self,
    *,
    backend: BackendProtocol,
    sources: Sequence[SkillSource],
    system_prompt: str | None = SKILLS_SYSTEM_PROMPT,
) -> None
```

| Name | Type |
|------|------|
| `backend` | `BackendProtocol` |
| `sources` | `Sequence[SkillSource]` |
| `system_prompt` | `str \| None` |

## Properties

- `trace_policy`
- `state_schema`
- `sources`
- `source_labels`
- `system_prompt_template`

## Methods

- [`modify_request()`](https://reference.langchain.com/python/deepagents/middleware/skills/SkillsMiddleware/modify_request)
- [`before_agent()`](https://reference.langchain.com/python/deepagents/middleware/skills/SkillsMiddleware/before_agent)
- [`abefore_agent()`](https://reference.langchain.com/python/deepagents/middleware/skills/SkillsMiddleware/abefore_agent)
- [`wrap_model_call()`](https://reference.langchain.com/python/deepagents/middleware/skills/SkillsMiddleware/wrap_model_call)
- [`awrap_model_call()`](https://reference.langchain.com/python/deepagents/middleware/skills/SkillsMiddleware/awrap_model_call)

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/skills.py#L766)
