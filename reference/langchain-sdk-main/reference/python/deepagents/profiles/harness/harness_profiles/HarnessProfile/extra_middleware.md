---
title: "extra_middleware"
description: "Middleware appended to every runtime middleware stack."
source: "https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/HarnessProfile/extra_middleware"
category: "reference"
tags: [reference, deepagents, profiles, harness, harness_profiles, harnessprofile, extra_middleware]
---

# extra_middleware

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/HarnessProfile/extra_middleware)

Middleware appended to every runtime middleware stack.

Applied to the main agent, the auto-added `general-purpose` subagent, and
declarative synchronous subagents created from `SubAgent` specs —
i.e., the stacks that `create_deep_agent` assembles itself.

Appended after the SDK defaults and any caller-supplied `middleware`, and
before profile tool exclusions, prompt caching, memory, and
human-in-the-loop middleware. This lets profiles tune the final request
surface after extra middleware has added any tools or prompt behavior.

*Not* applied to `CompiledSubAgent` runnables or `AsyncSubAgent` entries.
A `CompiledSubAgent` is passed in pre-built (its `runnable` is already a
compiled graph with its own middleware chain), so `create_deep_agent` has
nothing to append to. An `AsyncSubAgent` runs out-of-process against a
remote deployment and its middleware is configured on that remote graph,
not here. In both cases, injecting local middleware would either fail
silently or violate the caller's explicit configuration.

May be a static sequence or a zero-arg factory that returns one. Use a
factory when middleware instances should not be shared across stacks. This
field is runtime-only and intentionally absent from `HarnessProfileConfig`.

## Signature

```python
extra_middleware: Sequence[AgentMiddleware] | Callable[[], Sequence[AgentMiddleware]] = ()
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/profiles/harness/harness_profiles.py#L690)
