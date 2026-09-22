---
title: "Managed Deep Agents project structure"
description: "Understand the project layout for Managed Deep Agents."
source: "https://docs.langchain.com/langsmith/python/managed-deep-agents-project-structure"
category: "docs"
tags: [docs, langsmith, managed-deep-agents-project-structure]
---

# Managed Deep Agents project structure

> Understand the project layout for Managed Deep Agents.

A Managed Deep Agents project is a normal Python package with one required root agent entry. Other paths are either ordinary modules you import, or files and directories that MDA discovers to enable managed capabilities.

> [!NOTE]
> Managed Deep Agents is in **public [beta](../release-stages.md)** and available on [LangSmith Cloud](../cloud.md) in the US region only.

## Project layout

**Project layout**

```text
my-agent/
├── agent.py                        # Core agent definition

├── instructions.md                 # Managed context
├── skills/
│   └── <name>/
│       └── SKILL.md

├── tools/                          # Application code
│   └── mcp.py                      # MCP server declaration
├── middleware/

├── channels/                       # Managed configuration
│   └── <name>.py
├── schedules/
│   └── <name>.py
├── sandbox/
│   └── __init__.py
├── identity.py
├── memory.py

├── pyproject.toml                  # Dependencies
├── .env                            # Local and deploy secrets

└── evals/                          # Harbor workspace
    ├── harbor-job.json
    └── <task>/                     # Harbor task
        ├── Task.md
        ├── instruction.md
        ├── environment/
        └── tests/
```

The only required file is `agent.py` at the project root containing the [agent definition](managed-deep-agents-agent-definition.md) as a named `agent`. It must export a named `agent` created with `define_deep_agent`. Use only one agent entry in a project.

## How MDA treats project files

* **Managed context**: [`instructions.md`](managed-deep-agents-instructions.md) defines the system prompt. Each directory under [`skills/`](managed-deep-agents-skills.md) contains task-specific instructions, such as a `SKILL.md` and any supporting files. MDA syncs both `instructions.md` and `skills/` to [Context Hub](managed-deep-agents-context-hub.md). Optional [durable memory](managed-deep-agents-memory.md) is also backed by Context Hub.

* **Application code**: Files under [`tools/`](managed-deep-agents-tools.md) and [`middleware/`](managed-deep-agents-middleware.md) are ordinary project modules. Import them from the agent entry. Other local modules work the same way.

* **Managed configuration**: Certain paths enable capabilities when present. For `channels/` and `schedules/`, only direct children are managed declarations; nested modules are not.

  | Path                  | Enables                                                                         |
  | --------------------- | ------------------------------------------------------------------------------- |
  | `identity.py`         | [Caller authentication](managed-deep-agents-identity.md)         |
  | `memory.py`           | [Durable memory](managed-deep-agents-memory.md)                  |
  | `channels/<name>.py`  | [Messaging channels](managed-deep-agents-channels.md)            |
  | `tools/mcp.py`        | [MCP connectors](managed-deep-agents-mcp-connectors.md)          |
  | `schedules/<name>.py` | [Cron schedules](managed-deep-agents-schedules.md)               |
  | `sandbox/__init__.py` | [Sandbox filesystem and shell](managed-deep-agents-sandboxes.md) |

  `tools/` holds ordinary modules with one exception. `tools/mcp.py` is a managed declaration and exports a module-level `mcp`. Every other module under `tools/` is application code you import.

* **Dependencies and secrets**: Declare dependencies in `pyproject.toml`. MDA loads `.env` locally and forwards non-reserved values as deployment secrets. Reserved platform variables and `.env` files are not included in the build archive. For more information, see [Deploy a Managed Deep Agent](managed-deep-agents-deploy.md).

* **Evals**: Managed Deep Agents [evals](managed-deep-agents-evals.md) are Harbor evals. Run `mda evals init -i` and develop tasks with a coding agent and the `eval-engineering` skill. Generated runtime files stay under `.mda/evals/` and are not included in the deployed agent build.

## Next steps

#### [Quickstart](managed-deep-agents-quickstart.md)
Create and deploy your first Managed Deep Agent with the `mda` CLI.

#### [Tutorial](managed-deep-agents-tutorial.md)
Add durable memory and a daily schedule to the quickstart research assistant.

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/managed-deep-agents-project-structure.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
