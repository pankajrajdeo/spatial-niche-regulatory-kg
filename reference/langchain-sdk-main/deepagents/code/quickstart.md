---
title: "Quickstart"
description: "Install Deep Agents Code, run your first task, and use interactive or non-interactive modes"
source: "https://docs.langchain.com/oss/deepagents/code/quickstart"
category: "docs"
tags: [docs, deepagents, code, quickstart]
---

# Quickstart

> Install Deep Agents Code, run your first task, and use interactive or non-interactive modes

Deep Agents Code (`dcode`) is a terminal coding agent built on the [Deep Agents SDK](../quickstart.md). This guide covers installation, your first task, daily interactive use, automation with piping, and LangSmith tracing. For a feature overview, see [Deep Agents Code overview](overview.md). For `config.toml` and provider settings, see [Configuration](configuration.md).

## Install and run your first task

### Install and launch
```bash
curl -LsSf https://langch.in/dcode | bash
```

### Add provider credentials
Deep Agents Code works with any tool-calling LLM. OpenAI, Anthropic, and Google are available out of the box.

Use the `/auth` command to connect with a provider. See [Providers](providers.md) for the full list and credential details.

> [!NOTE]
> Web search uses [Tavily](https://tavily.com). Add a key with `/auth`. See [Enable web search](credentials.md#enable-web-search-with-tavily).

### Give the agent a task
```txt
Create a Python script that prints "Hello, World!"
```

The agent interprets the query and proposes changes with diffs for your approval before modifying files. If needed, it can run shell commands to test the code, check documentation, or search the web for up-to-date information.

### Enable tracing (optional)
To log agent operations, tool calls, and decisions in LangSmith, run `/auth` and add your LangSmith API key. Tracing is enabled on the next launch.

For project naming, advanced options, and CI or headless setup, see [Trace with LangSmith](#trace-with-langsmith).

> [!NOTE]
> Deep Agents Code is not officially supported on Windows. Windows users can try running it under [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install).

## Interactive mode

Type naturally as you would in a chat interface.
The agent uses its built-in tools, skills, and memory to help you with tasks.

<details>
<summary>Slash commands</summary>

Use these commands within a Deep Agents Code session:

* `/model`: Switch models or open the interactive model selector.
* `/effort`: Set reasoning effort for the current model.
* `/agents`: Hot-swap between pre-configured agents without relaunching. See [Command reference](cli-reference.md#command-line-options) for related flags.
* `/auth`: Manage stored API keys for model providers and services (such as Tavily web search). See [Provider credentials](credentials.md) for details.
* `/goal <objective>`: Draft acceptance criteria from a measurable objective. See [Goals and rubrics](goals-and-rubrics.md).
* `/rubric`: Set explicit acceptance criteria for grading. See [Goals and rubrics](goals-and-rubrics.md).
* `/remember [context]`: Review conversation and update memory and skills. Optionally pass additional context.
* `/skill:<name> [args]`: Directly invoke a skill by name. The skill's `SKILL.md` instructions are injected into the prompt along with any arguments you provide.
* `/skill-creator [task]`: Guide for creating effective agent skills.
* `/offload` (alias `/compact`) - Free up context window space by offloading messages to storage with a summary placeholder. The agent can retrieve the full history from the offloaded file if needed.
* `/context`: Open a color-coded context-window usage report with model capacity, usage categories, and remaining space.
* `/context-doctor`: Audit the context injected into the session and its estimated token cost. See [Audit injected context](cli-reference.md#audit-injected-context).
* `/tools`: List the built-in and MCP tools available to the current agent. See [List available tools](cli-reference.md#list-available-tools).
* `/extensions`: List loaded [Python extensions](extensions.md), their registrations, and their source paths. Requires `DEEPAGENTS_CODE_EXPERIMENTAL=1`.
* `/cost`: Show the thread's estimated cost. See [Track thread cost](cli-reference.md#track-thread-cost).
* `/tokens`: Display current context window token usage breakdown.
* `/clear`: Start a fresh thread.
* `/force-clear`: Recover a stuck session with a fresh thread.
* `/copy`: Copy the latest assistant message to the clipboard.
* `/prompts`: Search, preview, copy, and reuse previously submitted prompts.
* `/threads`: Browse and resume previous conversation threads.
* `/mcp [login <server> | reconnect]`: Show active MCP servers and tools. `login <server>` runs the OAuth flow for a server; `reconnect` loads deferred logins.
* `/plugins`: Manage [plugins and marketplaces](plugins.md).
* `/notifications`: Configure startup warning preferences.
* `/reload`: Re-read `.env` files, refresh configuration, and re-discover skills without restarting. This also reloads plugin skills and MCP configuration. Conversation state is preserved. See [`DEEPAGENTS_CODE_` prefix](configuration.md#deepagents_code_-prefix) for override behavior.
* `/theme`: Open the interactive theme selector to switch color themes. Built-in themes are available plus any [user-defined themes](configuration.md#themes).
* `/scrollbar`: Show or hide the chat scrollbar.
* `/line-numbers`: Show or hide file-relative line numbers in new diffs. See [Diff line numbers](config-file.md#diff-line-numbers).
* `/update`: Check for and install Deep Agents Code updates inline. Detects your install method (uv, Homebrew, pip) and runs the appropriate upgrade command.
* `/auto-update`: Toggle automatic updates on or off.
* `/install`: Install an optional integration.
* `/trace`: Open the current thread in LangSmith.
* `/editor`: Open the current prompt in your external editor (`$VISUAL` / `$EDITOR`). See [External editor](#external-editor).
* `/restart`: Restart the agent server.
* `/timestamps`: Toggle message timestamp footers.
* `/changelog`: Open Deep Agents Code changelog in your browser.
* `/docs`: Open the documentation in your browser.
* `/feedback`: Send feedback or report an issue.
* `/version` (alias `/about`) - Show installed `deepagents-code` and SDK versions.
* `/help`: Show help and available commands.
* `/quit`: Exit application.

</details>

<details>
<summary>Shell commands</summary>

Type `!` to enter shell mode, then type your command.

```bash
git status
npm test
ls -la
```

</details>

<details>
<summary>Keyboard shortcuts</summary>

**General**

| Shortcut                                              | Action                                                      |
| ----------------------------------------------------- | ----------------------------------------------------------- |
| `Enter`                                               | Submit prompt                                               |
| `Shift+Enter`, `Ctrl+J`, `Alt+Enter`, or `Ctrl+Enter` | Insert newline                                              |
| `@filename`                                           | Auto-complete files and inject content                      |
| `Shift+Tab`                                           | Cycle [approval modes](approval-modes.md) |
| `Ctrl+G`                                              | Open prompt in external editor                              |
| `Ctrl+T`                                              | Expand or collapse the subagent panel when one is present   |
| `Ctrl+N`                                              | Review pending notifications when the panel is open         |
| `Ctrl+O`                                              | Expand/collapse the most recent tool output                 |
| `Escape`                                              | Interrupt current operation                                 |
| `Ctrl+C`                                              | Interrupt or quit                                           |
| `Ctrl+D`                                              | Exit                                                        |

**Text editing in the prompt**

The chat input uses standard readline-style bindings:

| Shortcut                     | Action                              |
| ---------------------------- | ----------------------------------- |
| `Ctrl+A` or `Home`           | Move cursor to start of line        |
| `Ctrl+E` or `End`            | Move cursor to end of line          |
| `Ctrl+U`                     | Delete from cursor to start of line |
| `Ctrl+K`                     | Delete from cursor to end of line   |
| `Ctrl+W` or `Ctrl+Backspace` | Delete word to the left             |
| `Ctrl+Left` / `Ctrl+Right`   | Move cursor one word left/right     |

**Search prompt history**

Prompt history search lets you find and reuse previously submitted prompts without leaving the chat input. Press `Ctrl+R` to open an inline search of prompts stored on your machine.

> [!NOTE]
> **macOS `Cmd+Left` / `Cmd+Right` / `Cmd+Delete`**
>
> Terminal emulators intercept `Cmd`-modified keys before they reach the running application, so Deep Agents Code never receives them directly. Instead, the terminal translates them into the readline shortcuts above.
>
> * **Ghostty:** Works out of the box. `Cmd+Left`, `Cmd+Right`, and `Cmd+Delete` are translated to `Ctrl+A`, `Ctrl+E`, and `Ctrl+U` by default.
> * **iTerm2:** Not bound by default. Add the following under **Settings > Profiles > Keys > Key Mappings** as `Send Text with vim special chars`:
>   * `Cmd+Left` → `\x01` (Ctrl+A)
>   * `Cmd+Right` → `\x05` (Ctrl+E)
>   * `Cmd+Delete` → `\x15` (Ctrl+U)
> * **Terminal.app:** No native UI for this remap. Use the `Ctrl`-based shortcuts directly.
>
> Word-wise motion (`Option+Left` / `Option+Right`) is handled the same way: terminals send `Esc+b` / `Esc+f`, which Deep Agents Code interprets as word-left/right.

</details>

### Inspect context-window usage

Run `/context` to open a color-coded report of the current model's context-window usage. The report shows the model's context limit, used tokens, remaining capacity, and a breakdown between the conversation and system prompt plus tools when those values are available.

Provider-reported totals remain distinct from local conversation estimates. When a provider total is unavailable, the report labels the conversation count as an estimate and marks the total usage as unavailable. Use `/tokens` when you want a text summary in the conversation transcript instead.

When usage grows faster than expected, run `/context-doctor` to attribute tokens to each injected component: the base system prompt, memory files, the skills index, built-in tool schemas, and MCP tool schemas. To confirm which tools the agent can currently call, run `/tools`. For the thread's running cost estimate, run `/cost`; the same figure appears in the status bar. See [Diagnose and audit a session](cli-reference.md#diagnose-and-audit-a-session).

### External editor

Press `Ctrl+G` or type `/editor` to compose prompts in an external editor. Deep Agents Code checks `$VISUAL`, then `$EDITOR`, then falls back to `vi` (macOS/Linux) or `notepad` (Windows). GUI editors (VS Code, Cursor, Zed, etc.) automatically receive a `--wait` flag so Deep Agents Code blocks until you close the file.

```bash
# Set in your shell profile (~/.zshrc, ~/.bashrc, etc.)
export VISUAL="code"    # GUI editor (--wait auto-injected)
export EDITOR="nvim"    # Terminal fallback
```

## Non-interactive mode and piping

Use `-n` to run a single task without launching the interactive UI:

```bash
dcode -n "Write a Python script that prints hello world"
```

Each non-interactive run starts a fresh thread—conversation history does not carry between invocations. File-based state (memory, skills, configuration) persists.

You can also pipe input via stdin. When input is piped, Deep Agents Code automatically runs non-interactively:

```bash
echo "Explain this code" | dcode
cat error.log | dcode -n "What's causing this error?"
git diff | dcode -n "Review these changes"
git diff | dcode --skill code-review -n 'summarize changes'
```

When you combine piped input with `-n` or `-m`, the piped content appears first, followed by the text you pass to the flag.

> [!NOTE]
> The maximum piped input size is 10 MiB.

Shell execution is disabled by default in non-interactive mode. Use `-S`/`--shell-allow-list` to enable specific commands (e.g., `-S "pytest,git,make"`), `recommended` for safe defaults, or `all` to permit any command.

<details>
<summary>Cap turn count</summary>

Long-running or misbehaving agents in CI/CD pipelines can loop indefinitely. `--max-turns N` gives operators a hard upper bound without having to touch SDK internals:

```bash
dcode -n "fix the failing tests" --max-turns 10
```

`N` must be a positive integer, and overrides the internal safety default that otherwise caps runaway loops. Exits with code 124 (matching GNU `timeout`) when the budget is exceeded, so CI can distinguish a budget hit from a generic failure. Requires `-n` or piped stdin; otherwise exits with code 2.

For a time-based limit instead of (or in addition to) a turn-count limit, see [Cap wall-clock time with `--timeout`](#non-interactive-mode-and-piping).

</details>

<details>
<summary>Cap wall-clock time</summary>

`--timeout SECONDS` enforces a hard wall-clock limit on a non-interactive run. It complements `--max-turns` (turn count) with a time-based budget—whichever limit is hit first cancels the agent.

```bash
# Fail fast in CI if the task takes more than 2 minutes
dcode -n "run the test suite and summarise failures" --timeout 120

# Combine with --max-turns—whichever limit is hit first stops the agent
dcode -n "refactor auth module" --timeout 300 --max-turns 20
```

On expiry the agent is cancelled and the process exits with code 124, the same code used by `--max-turns`, so CI can treat both budget hits uniformly. Requires `-n` or piped stdin; otherwise exits with code 2.

</details>

<details>
<summary>Clean output and buffering</summary>

Use `-q` for clean output suitable for piping into other commands, and `--no-stream` to buffer the full response (instead of streaming) before writing to stdout:

```bash
dcode -n "Generate a .gitignore for Python" -q > .gitignore
dcode -n "List dependencies" -q --no-stream | sort
```

In non-interactive mode, the agent is instructed to make reasonable assumptions and proceed autonomously rather than ask clarifying questions. It also favors non-interactive command variants (e.g., `npm init -y`, `apt-get install -y`).

</details>

<details>
<summary>Shell execution examples</summary>

```bash
# Allow specific commands (validated against the list)
dcode -n "Run the tests and fix failures" -S "pytest,git,make"

# Use the curated safe-command list
dcode -n "Build the project" -S recommended

# Allow any shell command
dcode -n "Fix the build" -S all
```

</details>

> [!WARNING]
> **Use with caution.**
>
> `-S all` (or `--shell-allow-list all`) lets the agent execute arbitrary shell commands with no human confirmation.

## Trace with LangSmith

Enable [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-deepagents-code-quickstart) tracing to see agent operations, tool calls, and decisions in a LangSmith project.

Run `/auth` and add your LangSmith API key. Tracing is enabled on the next launch and persists across sessions. See [Provider credentials](credentials.md#use-%2Fauth-recommended) for details on the credential manager.

To customize the project name or configure tracing without the TUI, add keys to `~/.deepagents/.env` so tracing is enabled in every session without per-shell exports:

```bash
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=lsv2_...
DEEPAGENTS_CODE_LANGSMITH_PROJECT=deepagents-code  # Project for Deep Agents Code's own traces; defaults to "deepagents-code"
```

Use `DEEPAGENTS_CODE_LANGSMITH_PROJECT` to name the project that receives Deep Agents Code's own traces. It is scoped to Deep Agents Code, so it is not affected by a `LANGSMITH_PROJECT` set in a project's `.env` (which routes that project's application traces; see **Separate agent traces from app traces** below).

To override the project for a specific working directory, add `DEEPAGENTS_CODE_LANGSMITH_PROJECT` to a `.env` in that directory. See [environment variables](configuration.md#environment-variables) for the full loading order.

For CI, headless runs, or temporary overrides, set shell environment variables instead. Shell exports always take precedence over `.env` values:

```bash
export LANGSMITH_TRACING=false
```

<details>
<summary>Separate agent traces from app traces</summary>

Deep Agents Code can produce two kinds of LangSmith traces:

* `Agent traces` are Deep Agents Code's own model calls, tool calls, orchestration, and middleware.
* `Shell-command traces` are traces emitted by code that Deep Agents Code runs for you in a shell, such as tests, scripts, or a local LangGraph app.

To send Deep Agents Code's own traces to a dedicated project, set `DEEPAGENTS_CODE_LANGSMITH_PROJECT`:

```bash
# Example value; use any LangSmith project name you want.
DEEPAGENTS_CODE_LANGSMITH_PROJECT=deepagents-code
```

Then configure `LANGSMITH_PROJECT` for your application traces:

```bash
LANGSMITH_PROJECT=customer-support-agent
```

For example, suppose you ask Deep Agents Code to debug a failing LangGraph test:

```bash
uv run pytest tests/test_escalation_flow.py
```

If that test runs your app with LangSmith tracing enabled, those app traces are created by the shell process and go to `customer-support-agent`. Deep Agents Code's own reasoning and tool-use traces go to `deepagents-code`.

You can also scope LangSmith credentials to Deep Agents Code using the [`DEEPAGENTS_CODE_` prefix](configuration.md#deepagents_code_-prefix) (e.g., `DEEPAGENTS_CODE_LANGSMITH_API_KEY`).

</details>

<details>
<summary>Dual-write traces to a second project</summary>

To mirror agent traces to a second LangSmith project, set `DEEPAGENTS_CODE_LANGSMITH_REPLICA_PROJECTS`. This is useful for sending the same traces to both a personal project and a shared team project.

```bash
DEEPAGENTS_CODE_LANGSMITH_REPLICA_PROJECTS=team-shared
```

When set and tracing is active, each agent run is written to both the primary project (`DEEPAGENTS_CODE_LANGSMITH_PROJECT`, or `deepagents-code` by default) and the project you name here. Leave the variable unset to write to a single project as usual.

</details>

When configured, Deep Agents Code displays a status line with a link to the LangSmith project. In supported terminals, click the link to open it directly. You can also use `/trace` to print the URL and open it in your browser.

```sh
✓ LangSmith tracing: 'my-project'
```

> [!TIP]
> We recommend you also set up [LangSmith Engine](../../langsmith/engine.md), which monitors your traces, detects issues, and proposes fixes.

## See also

* [Deep Agents Code overview](overview.md)
* [Configuration](configuration.md)
* [Provider credentials](credentials.md)
* [CLI reference](cli-reference.md)
* [Providers](providers.md)
* [Memory and skills](memory-and-skills.md)

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/code/quickstart.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
