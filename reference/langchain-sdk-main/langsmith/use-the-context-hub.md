---
title: "Use the Context Hub"
description: "Learn how to create, view, and promote context in the LangSmith Context Hub."
source: "https://docs.langchain.com/langsmith/use-the-context-hub"
category: "docs"
tags: [docs, langsmith, use-the-context-hub]
---

# Use the Context Hub

> Learn how to create, view, and promote context in the LangSmith Context Hub.

The **Context Hub** gives your team version-controlled, environment-aware management of the instructions and tools your agents use in production. A *context* is a versioned bundle of agent instructions and tools, either a skill or a full agent, that you manage in LangSmith.

Use this guide to create your first context, view its files and history, and promote it to an environment so your agents can pull it.

## 1. Open the Context Hub

> [!NOTE]
> If you don't see **Context** in the left-hand navigation, verify that Context Hub is enabled for your workspace and that you have the required permissions.

In the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-use-the-context-hub), select **Context** in the
left-hand navigation. The Context Hub lists every agent and skill in your workspace.

<img src="https://mintcdn.com/langchain-5e9cc07a/VMau0Ih_5sR7Yf36/langsmith/images/context-hub-home.png?fit=max&auto=format&n=VMau0Ih_5sR7Yf36&q=85&s=7067ab68c361e53e17514009ae3405b0" alt="The Context Hub home view listing existing Agent and Skill contexts with their commit metadata." width="2396" height="1102" data-path="langsmith/images/context-hub-home.png" />

## 2. Create a context

1. Click **+ Create** in the top left of the Context Hub.

2. Choose the context type:

   * **Agent:** a full agent bundle including an `AGENTS.md` file and tools.
   * **Skill:** a reusable capability that agents can use, including a `SKILL.md` file.

   <img src="https://mintcdn.com/langchain-5e9cc07a/VMau0Ih_5sR7Yf36/langsmith/images/context-hub-create-context.png?fit=max&auto=format&n=VMau0Ih_5sR7Yf36&q=85&s=8ff29b4fac4c167d55ca593fb943a02a" alt="The Create dropdown showing the Agent and Skill context type options." width="360" data-path="langsmith/images/context-hub-create-context.png" />

3. Fill in a name and description. For skills, a description is required. You can also enter the initial file contents (`SKILL.md` for a skill, `AGENTS.md` for an agent) now, or add them after creation. Click **Create Agent** or **Create Skill**. LangSmith creates the repo and opens it for editing.

## 3. View a context

Click on an agent or skill from the Context Hub to view it.

<img src="https://mintcdn.com/langchain-5e9cc07a/VMau0Ih_5sR7Yf36/langsmith/images/context-hub-agent-view.png?fit=max&auto=format&n=VMau0Ih_5sR7Yf36&q=85&s=a333c5d93ad3532eb10c30053f53c267" alt="An Agent context with an AGENTS.md file open, showing the environments panel, commit history, and file tree." width="2416" height="1308" data-path="langsmith/images/context-hub-agent-view.png" />

The middle panel shows the file tree for the current commit and the right panel previews the selected file. Click a file in the middle panel to open it.

Markdown files open in **Preview**, which is a read-only rendering. To change a file, switch to the **Edit** tab in the top right of the right panel: it shows the exact text in the file. Save your changes to create a new commit.

Each saved change creates a new **commit** in the **Commit History** panel on
the left, so you can browse, compare, and revert prior versions without losing
work.

## 4. Tag and promote a commit

Once a commit is ready to ship, promote it to an environment so downstream
agents can pull it.

> [!NOTE]
> Context Hub currently supports two environment tags for promotion: `staging` and `production`.

1. With the target commit selected, click **Promote** in the top right.

2. Choose the destination environment:

   * **Promote to Production:** the commit your production agents pull.
   * **Promote to Staging:** a pre-production environment for validation.

   <img src="https://mintcdn.com/langchain-5e9cc07a/VMau0Ih_5sR7Yf36/langsmith/images/context-hub-promote.png?fit=max&auto=format&n=VMau0Ih_5sR7Yf36&q=85&s=96dc0abf55f702cb873f78eaa99429fe" alt="The Promote dropdown with options to promote a commit to Production or Staging." width="300" data-path="langsmith/images/context-hub-promote.png" />

3. The environment label (for example, `Production 7ca95573`) moves to the
   promoted commit. Use the **Tag** button next to **Promote** to attach a
   human-readable label to any commit for easy reference.

Agent runtimes that resolve context by environment tag (for example, `:production`) now pull this promoted commit.

## Next steps

* [Context engineering concepts](context-engineering-concepts.md): learn about skills, agents, versioning, and sharing.
* [Manage contexts with the SDK](manage-contexts-sdk.md): push, pull, list, and delete contexts programmatically.
* [Configure commit webhooks](context-hub-webhooks.md): send workspace Context Hub commits to an external HTTPS endpoint.
* [Mount a Context Hub repo in a sandbox](sandbox-mounts.md#mount-a-context-hub-repo): give sandbox code read-only filesystem access to a repo that stays in sync as it changes.

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/use-the-context-hub.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
