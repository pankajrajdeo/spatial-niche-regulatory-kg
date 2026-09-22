---
title: "SkillMetadata"
description: "Metadata for a skill per Agent Skills specification (https://agentskills.io/specification)."
source: "https://reference.langchain.com/python/deepagents/middleware/skills/SkillMetadata"
category: "reference"
tags: [reference, deepagents, middleware, skills, skillmetadata]
---

# SkillMetadata

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/skills/SkillMetadata)

Metadata for a skill per Agent Skills specification (https://agentskills.io/specification).

## Signature

```python
SkillMetadata()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    path: str,
    name: str,
    description: str,
    license: str | None,
    compatibility: str | None,
    metadata: dict[str, str],
    allowed_tools: list[str],
)
```

| Name | Type |
|------|------|
| `path` | `str` |
| `name` | `str` |
| `description` | `str` |
| `license` | `str \| None` |
| `compatibility` | `str \| None` |
| `metadata` | `dict[str, str]` |
| `allowed_tools` | `list[str]` |

## Properties

- `path`
- `name`
- `description`
- `license`
- `compatibility`
- `metadata`
- `allowed_tools`

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/skills.py#L233)
