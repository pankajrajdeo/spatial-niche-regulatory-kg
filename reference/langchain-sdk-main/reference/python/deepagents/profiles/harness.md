---
title: "harness"
description: "Harness profile package: HarnessProfile API and built-in registrations."
source: "https://reference.langchain.com/python/deepagents/profiles/harness"
category: "reference"
tags: [reference, deepagents, profiles, harness]
---

# harness

> **Module** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/harness)

Harness profile package: `HarnessProfile` API and built-in registrations.

Individual built-in modules expose a zero-arg `register()` callable; the lazy
`_builtin_profiles` bootstrap invokes them once on first profile-registry
access. Built-ins must not register at module import time — registration runs
under the bootstrap mutex, so a top-level call would race with concurrent
lookups and bypass the additive-merge semantics.

## Methods

- [`register_harness_profile()`](https://reference.langchain.com/python/deepagents/profiles/harness/register_harness_profile)

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/profiles/harness/__init__.py)
