---
title: "spawn"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langchain/agents/middleware/_execution/CodexSandboxExecutionPolicy/spawn"
category: "reference"
tags: [reference, langchain, agents, middleware, execution, codexsandboxexecutionpolicy, spawn]
---

# spawn

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/_execution/CodexSandboxExecutionPolicy/spawn)

## Signature

```python
spawn(
    self,
    *,
    workspace: Path,
    env: Mapping[str, str],
    command: Sequence[str],
) -> subprocess.Popen[str]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/_execution.py#L210)
