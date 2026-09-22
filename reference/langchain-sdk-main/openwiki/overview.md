---
title: "OpenWiki"
description: "CLI that writes and maintains agent wikis so coding agents work faster"
source: "https://docs.langchain.com/oss/openwiki/overview"
category: "docs"
tags: [docs, openwiki]
---

# OpenWiki

> CLI that writes and maintains agent wikis so coding agents work faster

OpenWiki is an open source CLI that writes and maintains a Markdown wiki about your codebase or personal knowledge. The wiki captures details such as architecture, integrations, evals, and workflows so [coding agents](../deepagents/overview.md) can use it as durable context instead of rediscovering the repository on every task.

That makes agent work faster and cheaper in tokens: agents read a curated wiki first, then inspect source only where they need more detail. Humans can browse the same Markdown (and the local [visualizer](visualize.md)), but the primary audience is agents.

OpenWiki is built on [Deep Agents](../deepagents/overview.md) and supports tracing with [LangSmith](../langsmith/observability-quickstart.md).

## Get started

Install the CLI, then initialize documentation for the current repository:

```bash
npm install -g openwiki
openwiki --init
```

See the [Quickstart](quickstart.md) to choose a model provider, generate docs, and keep them up to date. To run OpenWiki inside Codex, Claude Code, OpenCode, or Cursor instead of a standalone model session, see [Coding-agent integrations](integrations.md).

## Modes

OpenWiki has two modes:

| Mode               | Command                      | Output                                | Use when                                                        |
| ------------------ | ---------------------------- | ------------------------------------- | --------------------------------------------------------------- |
| **Code** (default) | `openwiki` / `openwiki code` | `openwiki/` in the current repository | You want repository context and documentation for coding agents |
| **Personal**       | `openwiki personal`          | `~/.openwiki/wiki`                    | You want a local personal brain from configured sources         |

Bare `openwiki --init` and `openwiki --update` run in code mode. Use `openwiki personal --init` or `openwiki personal --update` for the personal wiki.

## Capabilities

#### [Repository wikis](code-mode.md)
Generate Markdown docs under `openwiki/`, then wire them into `AGENTS.md` and `CLAUDE.md` so coding agents can find them.

#### [Coding-agent integrations](integrations.md)
Run OpenWiki inside Codex, Claude Code, OpenCode, or Cursor using the host model and repository tools.

#### [Personal brain](personal-mode.md)
Build a local wiki from git repos, Custom MCP, Gmail, Notion, web search, Hacker News, and X/Twitter.

#### [Grounded Claims](code-mode.md#grounded-claims)
Track material facts back to versioned source evidence and refresh pages when that evidence changes.

#### [Automatic updates](automate-updates.md)
Refresh docs from GitHub Actions, GitLab CI, or Bitbucket Pipelines and open a PR when content changes.

#### [Model providers](providers.md)
Use OpenAI, Anthropic, Gemini, Bedrock, OpenRouter, GitHub Copilot, and other providers out of the box.

#### [Open Knowledge Format](code-mode.md#open-knowledge-format)
Emit OKF v0.2 Markdown bundles with front matter, indexes, and linked concepts.

#### [LangSmith tracing](quickstart.md#trace-with-langsmith)
Trace documentation runs with LangSmith.

## Next steps

#### [Quickstart](quickstart.md)
Install OpenWiki, configure a provider, and generate your first wiki.

#### [CLI reference](cli-reference.md)
Review commands, flags, and connector subcommands.

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/openwiki/overview.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
