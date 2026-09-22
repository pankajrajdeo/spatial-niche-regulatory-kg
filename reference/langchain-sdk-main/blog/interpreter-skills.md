---
title: "Building workflows for agents with Skills and Interpreters"
description: "Interpreter skills extend agent skills with a TypeScript module the agent can import and run. This lets you build more capable workflows with your agents."
source: "https://www.langchain.com/blog/interpreter-skills"
category: "blog"
published: "2026-05-29T17:00:00.000Z"
author: "LangChain Accounts"
tags: [blog, interpreter-skills]
---

# Building workflows for agents with Skills and Interpreters

- **Skills can now direct the harness, not just the model. **Because interpreter code can talk to the agent loop directly, a skill can spawn subagents, manage a task graph, and handle partial failures as one reviewed workflow
- **Skills can now become both a set of instructions and an API.** A normal skill tells the agent *how* to do a task and hopes it follows along. An interpreter skill ships a module, so the determinsitc part lives in code that can be reviewed and iterated on, while the model decides when to call it and what inputs to pass
- **Agent work can now be more easily evaluated.** Instead of asking "did the agent generally follow instructions?", you can ask more concrete questions like "did it call the expected function?"
