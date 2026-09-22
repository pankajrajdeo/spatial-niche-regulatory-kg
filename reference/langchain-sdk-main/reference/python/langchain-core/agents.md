---
title: "agents"
description: "Schema definitions for representing agent actions, observations, and return values."
source: "https://reference.langchain.com/python/langchain-core/agents"
category: "reference"
tags: [reference, langchain-core, agents]
---

# agents

> **Module** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/agents)

Schema definitions for representing agent actions, observations, and return values.

!!! warning

    The schema definitions are provided for backwards compatibility.

!!! warning

    New agents should be built using the
    [`langchain` library](https://pypi.org/project/langchain/), which provides a
    simpler and more flexible way to define agents.

    See docs on [building agents](../../../langchain/agents.md).

Agents use language models to choose a sequence of actions to take.

A basic agent works in the following manner:

1. Given a prompt an agent uses an LLM to request an action to take
    (e.g., a tool to run).
2. The agent executes the action (e.g., runs the tool), and receives an observation.
3. The agent returns the observation to the LLM, which can then be used to generate
    the next action.
4. When the agent reaches a stopping condition, it returns a final return value.

The schemas for the agents themselves are defined in `langchain.agents.agent`.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/agents.py)
