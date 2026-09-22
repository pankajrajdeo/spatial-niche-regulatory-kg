---
title: "Quickstart"
description: "Install OpenWiki, configure a model provider, and generate your first wiki."
source: "https://docs.langchain.com/oss/openwiki/quickstart"
category: "docs"
tags: [docs, openwiki, quickstart]
---

# Quickstart

> Install OpenWiki, configure a model provider, and generate your first wiki.

OpenWiki is a CLI that writes and maintains a Markdown wiki for your codebase or personal knowledge. Coding agents use that wiki as durable context, so they spend less time and fewer tokens rediscovering architecture, integrations, and other repository details. Humans can read the same docs, but agents are the primary audience. This guide covers installation, provider setup, and your first documentation run. For a feature overview, see [OpenWiki overview](overview.md).

## Install and generate repository docs

### Install the CLI
```bash
npm install -g openwiki
```

On Windows, prefer `npm` or `pnpm`. Installing with Bun can fall back to compiling the native `better-sqlite3` dependency and may require Visual Studio Build Tools with the Desktop development with C++ workload.

### Initialize in your repository
From the repository root, run the following command:

```bash
openwiki --init
```

On the first interactive run, OpenWiki prompts for:

* An inference provider and model
* The provider API key (or equivalent credentials)
* An optional LangSmith API key for tracing
* LangSmith projects to enrich the wiki from runtime traces

OpenWiki saves its configuration and secrets to `~/.openwiki/.env`.

Running `--init` again regenerates the repository wiki and Claims from scratch while preserving `openwiki/INSTRUCTIONS.md`. Interrupted runs on a persistent checkout resume from `openwiki/.run.json`.

To run OpenWiki inside Codex, Claude Code, OpenCode, or Cursor instead of a standalone model session, see [Coding-agent integrations](integrations.md).

### Review the generated wiki
OpenWiki writes documentation to `openwiki/` in the repository, including a quickstart entrypoint and topic pages. It also maintains an `AGENTS.md` and `CLAUDE.md` at the repository root, adding a block that instructs coding agents to consult the wiki for codebase context. Factual pages are grounded with Claims under `openwiki/.claims/`.

Repository-specific wiki instructions live in `openwiki/INSTRUCTIONS.md`. OpenWiki reads this file for scope and priorities. To change it, edit the file, or ask OpenWiki in chat to change the brief (for example, `openwiki "Update openwiki/INSTRUCTIONS.md to focus on the public API"`). Normal `--init` and `--update` runs do not rewrite it.

To explore the wiki in a browser, run:

```bash
openwiki visualize
```

This opens a local interactive node graph with a side-by-side Markdown reader. See [Visualize your wiki](visualize.md).

### Keep docs up to date
Refresh documentation after code changes:

```bash
openwiki --update
```

In code mode, updates also reconcile stale Claims when source evidence changes. For automated updates in CI, see [Automate updates](automate-updates.md).

## Personal wiki (optional)

To initialize a local personal brain instead of repository docs:

```bash
openwiki personal --init
```

Personal mode writes to `~/.openwiki/wiki` and can ingest configured connectors such as local git repositories, Custom MCP, Gmail, Notion, web search, Hacker News, and X/Twitter. See [Personal mode](personal-mode.md).

## Interactive and one-shot runs

Bare `openwiki` opens an interactive session in code mode for the current repository. Pass a message to start with a request:

```bash
openwiki "Please generate documentation for this repository"
```

Use `-p` / `--print` for a one-shot non-interactive run that prints the final assistant output and exits:

```bash
openwiki -p "Summarize what you can do"
```

In chat, use `/api-key` to update the current provider API key, `/langsmith-key` to update or clear LangSmith tracing credentials, and `/effort` to set reasoning effort for supported models.

## Trace with LangSmith

During onboarding, provide a LangSmith API key to trace OpenWiki runs to a LangSmith project named `openwiki`. You can also set these values in `~/.openwiki/.env` or the process environment:

```bash
LANGSMITH_API_KEY=your-key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=openwiki
```

To enrich the repository wiki from LangSmith traces (separate from tracing OpenWiki itself), see [LangSmith connector](code-mode.md#langsmith-connector).

## Next steps

* [Code mode](code-mode.md): repository wikis, Claims, OKF output, and agent instruction files
* [Coding-agent integrations](integrations.md): run OpenWiki inside Codex, Claude Code, OpenCode, or Cursor
* [Personal mode](personal-mode.md): local brain and connectors
* [Model providers](providers.md): supported providers and credentials
* [Automate updates](automate-updates.md): GitHub Actions, GitLab CI, and Bitbucket Pipelines
* [CLI reference](cli-reference.md): commands and flags

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/openwiki/quickstart.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
