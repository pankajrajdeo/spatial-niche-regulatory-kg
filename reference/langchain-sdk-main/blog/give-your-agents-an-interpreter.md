---
title: "Give Your Agents an Interpreter"
description: "Deep Agents now supports interpreters: small embedded runtimes where agents write code to coordinate tools, hold working state, and decide what enters model context."
source: "https://www.langchain.com/blog/give-your-agents-an-interpreter"
category: "blog"
published: "2026-05-20T18:00:00.000Z"
author: "LangChain Accounts"
tags: [blog, give-your-agents-an-interpreter]
---

# Give Your Agents an Interpreter

- **Interpreters sit between serial tool calls and full sandboxes.** Agents get code-level composition over scoped capabilities without inheriting a whole environment.
- **Interpreter state is a third context surface.** Message history is for what the model reasons over now, the filesystem is for durable artifacts, interpreter state is for live working values that don't need to be model input yet.
- **Programmatic tool calling drops in as middleware.** Allowlisted tools appear under a `tools` namespace inside the interpreter, work with any model, and used up to 35% fewer tokens on some tasks in early testing.
