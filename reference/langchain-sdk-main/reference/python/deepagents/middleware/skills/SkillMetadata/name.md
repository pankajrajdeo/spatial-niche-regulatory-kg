---
title: "name"
description: "Skill identifier."
source: "https://reference.langchain.com/python/deepagents/middleware/skills/SkillMetadata/name"
category: "reference"
tags: [reference, deepagents, middleware, skills, skillmetadata, name]
---

# name

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/skills/SkillMetadata/name)

Skill identifier.

Constraints per Agent Skills specification:

- 1-64 characters
- Unicode lowercase alphanumeric and hyphens only (`a-z` and `-`).
- Must not start or end with `-`
- Must not contain consecutive `--`
- Must match the parent directory name containing the `SKILL.md` file

## Signature

```python
name: str
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/skills.py#L239)
