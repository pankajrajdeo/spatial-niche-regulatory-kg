---
title: "Add instructions to Managed Deep Agents"
description: "Define the system prompt for a managed deep agent in instructions.md."
source: "https://docs.langchain.com/langsmith/javascript/managed-deep-agents-instructions"
category: "docs"
tags: [docs, langsmith, javascript, managed-deep-agents-instructions]
---

# Add instructions to Managed Deep Agents

> Define the system prompt for a managed deep agent in instructions.md.

Instructions define always-on agent behavior. They form the core of the agent's system prompt.

> [!NOTE]
> Managed Deep Agents is in **public [beta](../release-stages.md)** and available on [LangSmith Cloud](../cloud.md) in the US region only.

Put the instructions for your agent into `instructions.md` at the project root:

```text
my-agent/
  instructions.md
```

For the full project layout, see [Project structure](managed-deep-agents-project-structure.md).

## Add instructions

Create or modify `instructions.md` to define the agent's role, behavior, constraints, and guidance for using its tools:

**instructions.md**

```markdown
# Assistant

You are a helpful assistant.
```

MDA inserts instructions into the agent's system prompt on every run.
The agent cannot modify these instructions at runtime.

## Deployment

When you run `mda deploy`, MDA syncs `instructions.md` to the agent's [Context Hub](managed-deep-agents-context-hub.md).

You can then edit the instructions in the LangSmith UI and have those changes apply to the agent.

It is best to keep the `instructions.md` file in the repo as the source of truth for lasting changes, as later deployments sync the project copy again.

For what syncs, what does not, and how to open the repo from a deployment, see [Context Hub](managed-deep-agents-context-hub.md).

## When to use instructions

| Concept                                                        | Role                           | Loaded when                    |
| -------------------------------------------------------------- | ------------------------------ | ------------------------------ |
| **Instructions**                                               | Always-on system prompt        | Every run                      |
| **[Skills](managed-deep-agents-skills.md)** | Task-specific procedures       | When the agent selects them    |
| **[Memory](managed-deep-agents-memory.md)** | Knowledge the agent can update | When durable memory is enabled |

For more information, see [Project structure](managed-deep-agents-project-structure.md).

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/managed-deep-agents-instructions.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
