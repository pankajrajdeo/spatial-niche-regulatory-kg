---
title: "permissions"
description: "List of FilesystemPermission rules for this subagent."
source: "https://reference.langchain.com/python/deepagents/middleware/subagents/SubAgent/permissions"
category: "reference"
tags: [reference, deepagents, middleware, subagents, subagent, permissions]
---

# permissions

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/subagents/SubAgent/permissions)

List of `FilesystemPermission` rules for this subagent.

If omitted, inherits the parent agent's permissions. If specified, replaces
the parent's permissions entirely for this subagent.

Rules are evaluated in declaration order; the first match wins.
`FilesystemMiddleware` enforces these rules for the built-in filesystem
tools on the subagent stack.

## Signature

```python
permissions: NotRequired[list[FilesystemPermission]]
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/subagents.py#L152)
