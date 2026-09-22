---
title: "skills"
description: "Skills middleware for loading and exposing agent skills to the system prompt."
source: "https://reference.langchain.com/python/deepagents/middleware/skills"
category: "reference"
tags: [reference, deepagents, middleware, skills]
---

# skills

> **Module** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/skills)

Skills middleware for loading and exposing agent skills to the system prompt.

This module implements Anthropic's agent skills pattern with progressive disclosure,
loading skills from backend storage via configurable sources.

## Architecture

Skills are loaded from one or more **sources** - paths in a backend where skills are
organized. Sources are loaded in order, with later sources overriding earlier ones
when skills have the same name (last one wins). This enables layering: base -> user
-> project -> team skills.

The middleware uses backend APIs exclusively (no direct filesystem access), making it
portable across different storage backends (filesystem, state, remote storage, etc.).

For StateBackend (ephemeral/in-memory):
```python
SkillsMiddleware(backend=StateBackend(), ...)
```

## Skill Structure

Each skill is a directory containing a SKILL.md file with YAML frontmatter:

```
/skills/user/web-research/
├── SKILL.md          # Required: YAML frontmatter + markdown instructions
└── helper.py         # Optional: supporting files
```

SKILL.md format:
```markdown
---
name: web-research
description: Structured approach to conducting thorough web research
license: MIT
---

# Web Research Skill

## When to Use
- User asks you to research a topic
...
```

## Skill Metadata (SkillMetadata)

Parsed from YAML frontmatter per Agent Skills specification:
- `name`: Skill identifier (max 64 chars, lowercase alphanumeric and hyphens)
- `description`: What the skill does (max 1024 chars)
- `path`: Backend path to the SKILL.md file
- Optional: `license`, `compatibility`, `metadata`, `allowed_tools`

## Sources

Sources point to skill directories in the backend. Each source is either a bare
path or a `(path, label)` tuple. With a bare path the label is derived from the
last path component capitalized (e.g., `/skills/user/` -> `User`), with two
special cases: `built_in_skills` collapses to `Built-in`, and a literal `skills`
leaf climbs one level so `~/.claude/skills` renders as `Claude` rather than the
duplicative `Skills Skills`. Pass an explicit tuple to disambiguate sources
whose leaf directories would collide (e.g. user- vs project-scoped
`.claude/skills`).

Example sources:
```python
[
    "/skills/user/",
    "/skills/project/",
    ("/home/me/.claude/skills", "User Claude"),
    ("/repo/.claude/skills", "Project Claude"),
]
```

## Path Conventions

All paths use POSIX conventions (forward slashes) via `PurePosixPath`:
- Backend paths: "/skills/user/web-research/SKILL.md"
- Virtual, platform-independent
- Backends handle platform-specific conversions as needed

## Usage

```python
from deepagents.backends.state import StateBackend
from deepagents.middleware.skills import SkillsMiddleware

middleware = SkillsMiddleware(
    backend=my_backend,
    sources=[
        "/skills/base/",
        "/skills/user/",
        "/skills/project/",
        ("/repo/.claude/skills", "Project Claude"),
    ],
)
```

## Properties

- `FILE_NOT_FOUND`
- `logger`
- `MAX_SKILL_FILE_SIZE`
- `MAX_SKILLS_LOAD_WARNINGS`
- `MAX_SKILL_LOAD_WARNING_LENGTH`
- `MAX_SKILL_NAME_LENGTH`
- `MAX_SKILL_DESCRIPTION_LENGTH`
- `MAX_SKILL_COMPATIBILITY_LENGTH`
- `SKILLS_SYSTEM_PROMPT`

## Methods

- [`to_posix_path()`](https://reference.langchain.com/python/deepagents/middleware/skills/to_posix_path)
- [`append_to_system_message()`](https://reference.langchain.com/python/deepagents/middleware/skills/append_to_system_message)

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/skills.py)
