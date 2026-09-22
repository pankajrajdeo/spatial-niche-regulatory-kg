---
title: "Using skills with Deep Agents"
description: "Learn how to use agent skills with Deep Agents CLI to build token-efficient AI agents. Discover, load, and execute skills dynamically."
source: "https://www.langchain.com/blog/using-skills-with-deep-agents"
category: "blog"
published: "2025-11-25T16:45:09.000Z"
author: "LangChain Accounts"
tags: [blog, using-skills-with-deep-agents]
---

# Using skills with Deep Agents

tl;dr: Anthropic recently introduced the idea of [agent skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills?ref=blog.langchain.com). Skills are simply folders containing a [SKILL.md](http://skill.md/?ref=blog.langchain.com) file along with any associated files (e.g., documents or scripts) that an agent can discover and load dynamically to perform better at specific tasks. **We've added skills support** to [deepagents-CLI](https://github.com/langchain-ai/deepagents/tree/master/libs/deepagents-cli?ref=blog.langchain.com).

### The Rise of Generalist Agents

General purpose agents like Claude Code and Manus have gained widespread adoption. While we might expect generalist agents to use many tools, a surprising trend emerged: they use remarkably *few* tools. Claude Code uses [about a dozen](https://www.notion.so/177808527b1780cda055dad7024c8e65?pvs=21&ref=blog.langchain.com) and Manus uses [less than 20](https://www.youtube.com/watch?v=6_BcCthVvb8&ref=blog.langchain.com).

How can generalist agents get away with using a small number of tools? The key insight is giving agents access to a computer. With [bash](https://x.com/trq212/status/1982869394482139206?s=20&ref=blog.langchain.com) and [filesystem tools](https://blog.langchain.com/how-agents-can-use-filesystems-for-context-engineering/), agents can perform actions just as humans would without needing specialized bound tools for every task.

We've applied these principles in [deepagents](https://github.com/langchain-ai/deepagents/tree/master?ref=blog.langchain.com), our open source agent harness with filesystem operations and code execution. See our overview video [here](https://www.youtube.com/watch?v=IVts6ztrkFg&ref=blog.langchain.com) and associated [slides](https://docs.google.com/presentation/d/10RyhGsScWhfqKk4PbYOljPiotoa8xcWNw9pAujJ0sAc/edit?slide=id.g398124b6427_0_0&ref=blog.langchain.com#slide=id.g398124b6427_0_0).

![Deep Agents overview](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa36431a71bcb2862dab_image--2-.png)

### Generalist Agents With Skills

How can generalist agents with few tools perform diverse actions? In our webinar, [Manus discussed an approach](https://rlancemartin.github.io/2025/10/15/manus/?ref=blog.langchain.com): **offload actions from tools to the filesystem**. Instead of many tools, give agents a computer with scripts / instructions for a wide set of actions. The agent can just use its filesystem and shell tool to perform many actions using these resources.

Anthropic skills just follows this same pattern. Skills are just a collection of folders, each with a `SKILL.md` file containing YAML frontmatter and Markdown instructions. Here is a figure from [Anthropic’s blog post](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills?ref=blog.langchain.com) highlighting the structure of a [`SKILL.md`](http://skill.md/?ref=blog.langchain.com) file:

![Bundling additional content](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa36431a71bcb2862dae_image--3-.png)

Skills offer two advantages over traditional tools: The first benefit is ***token efficiency*.** Skills are progressively disclosed. Only YAML frontmatter loads by default; agents read the full `SKILL.md` only when needed. Traditional tools require all definitions upfront in context, which can bloat the context window. You can see this figure from [Anthropic’s blog post](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills?ref=blog.langchain.com) as an illustration of this:

![Skills and the Context Window](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa36431a71bcb2862da7_image--4-.png)

The second benefit is ***reduced cognitive load.*** Agents call a small set of atomic tools instead of navigating many potentially overlapping tools — a common source of context confusion. Here is table comparing skills to tools, and the associated benefit of skills for encoding actions.

![Comparing skills to tools](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa36431a71bcb2862da2_Screenshot-2025-11-24-at-6.39.01---PM.png)

Skills enable powerful capabilities beyond reducing token usage. As[Barry Zhang of Anthropic mentions](https://www.youtube.com/live/xmbSQz-PNMM?si=6B0YIg7J6HHisYAS&t=2277&ref=blog.langchain.com), skills are a step toward continuous learning: agents can create new skills on the fly as they encounter novel tasks. Skills are also easily shareable across agents and composable within sessions, allowing agents to pull in multiple skills as needed.

### Deep Agents CLI + Skills

Our deepagent-CLI is an [open source coding assistant](https://github.com/langchain-ai/deepagents/tree/master/libs/deepagents-cli?ref=blog.langchain.com) that can use your local filesystem, just like Claude Code. We’ve added skills to the deepagent-CLI, making it possible to use the [large](https://github.com/anthropics/skills?ref=blog.langchain.com) and [growing](https://skillsmp.com/?ref=blog.langchain.com) collection of public skills.

Just create a skills folder for you agent and copy any example skills [from our repo](https://github.com/langchain-ai/deepagents/tree/master/libs/deepagents-cli/examples/skills?ref=blog.langchain.com):

`mkdir -p ~/.deepagents/agent/skills
cp -r examples/skills/web-research ~/.deepagents/agent/skills/
`

These skills are default loaded into the deepagent CLI at startup, and you can see all available skills by simply running `deepagents skills list` in your terminal:

![Deep Agents skills list](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa36431a71bcb2862db1_image--5-.png)

When you give deepagents requests related to any of the skills, it will automatically read the relevant [`SKILL.md`](http://skill.md/?ref=blog.langchain.com) file execute the skill. For a complete overview of skills, see our video here and see the [README](https://github.com/langchain-ai/deepagents/tree/master/libs/deepagents-cli?ref=blog.langchain.com#skills).
