---
title: "Annotate traces and runs inline"
description: "LangSmith allows you to manually annotate traces with feedback within the application. This can be useful for adding context to a trace, such as a user's comment or a note about a specific issue. You..."
source: "https://docs.langchain.com/langsmith/annotate-traces-inline"
category: "docs"
tags: [docs, langsmith, annotate-traces-inline]
---

# Annotate traces and runs inline

LangSmith allows you to manually annotate traces with feedback within the application. This can be useful for adding context to a trace, such as a user's comment or a note about a specific issue.
You can annotate a trace either inline or by sending the trace to an annotation queue, which allows you to closely inspect and log feedbacks to runs one at a time.
Feedback tags are associated with your [workspace](administration-overview.md#workspaces).

> [!NOTE]
> **You can attach user feedback to ANY intermediate run (span) of the trace, not just the root span.**
>
> This is useful for critiquing specific parts of the LLM application, such as the retrieval step or generation step of the RAG pipeline.

To annotate a trace inline, open the three-dot menu (`...`) in the trace view for any particular run that is part of the trace, then click **Notes**.

This will open up a pane that allows you to choose from feedback tags associated with your workspace and add a score for particular tags. You can also add a standalone comment. Follow [Set up feedback criteria](set-up-feedback-criteria.md) to set up feedback tags for your workspace.
You can also set up new feedback criteria from within the pane itself.

Inline feedback and notes in the LangSmith UI do not change the trace's [retention tier](usage-and-billing.md#data-retention-auto-upgrades); the trace keeps the retention configured for its project unless another action explicitly extends retention.

<img src="https://mintcdn.com/langchain-5e9cc07a/E8FdemkcQxROovD9/langsmith/images/annotation-sidebar.png?fit=max&auto=format&n=E8FdemkcQxROovD9&q=85&s=6a16e79d91b435f6c5de94d0d58daa59" alt="Annotation sidebar" width="1376" height="758" data-path="langsmith/images/annotation-sidebar.png" />

You can use the labeled keyboard shortcuts to streamline the annotation process.

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/annotate-traces-inline.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
