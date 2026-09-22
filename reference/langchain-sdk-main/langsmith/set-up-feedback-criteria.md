---
title: "Set up feedback criteria"
description: "Recommended Reading"
source: "https://docs.langchain.com/langsmith/set-up-feedback-criteria"
category: "docs"
tags: [docs, langsmith, set-up-feedback-criteria]
---

# Set up feedback criteria

> [!TIP]
> **Recommended Reading**
>
> Before diving into this content, it might be helpful to read the following:
>
> * [Conceptual guide on tracing and feedback](observability-concepts.md)
> * [Reference guide on feedback data format](feedback-data-format.md)

Feedback criteria are represented in the application as feedback tags. For human feedback, you can set up new feedback criteria as continuous feedback or categorical feedback.

> [!NOTE]
> You can also manage feedback configs programmatically with the SDK. Refer to [Manage feedback & annotation queues programmatically](annotation-queues-sdk.md).

> [!TIP]
> For free-form acceptance criteria a reviewer writes per-run (rather than a fixed set of rubric scores), refer to [Use assertions](assertions.md).

To set up a new feedback criteria, follow [this link](https://smith.langchain.com/settings/workspaces/feedbacks) to view all existing tags for your workspace, then click **New Tag**.

## Continuous feedback

For continuous feedback, you can enter a feedback tag name, then select a minimum and maximum value. Every value, including floating-point numbers, within this range will be accepted as feedback scores.

<img src="https://mintcdn.com/langchain-5e9cc07a/aKRoUGXX6ygp4DlC/langsmith/images/cont-feedback.png?fit=max&auto=format&n=aKRoUGXX6ygp4DlC&q=85&s=44798176648f0a65e873fddecc90d43d" alt="Cont feedback" width="350" height="529" data-path="langsmith/images/cont-feedback.png" />

## Categorical feedback

For categorical feedback, you can enter a feedback tag name, then add a list of categories, each category mapping to a score. When you provide feedback, you can select one of these categories as the feedback score.
Both the category label and the score will be logged as feedback in `value` and `score` fields, respectively.

<img src="https://mintcdn.com/langchain-5e9cc07a/E8FdemkcQxROovD9/langsmith/images/cat-feedback.png?fit=max&auto=format&n=E8FdemkcQxROovD9&q=85&s=6ec5030c3ba55b1fb12d60bca91719f7" alt="Cat feedback" width="470" height="465" data-path="langsmith/images/cat-feedback.png" />

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/set-up-feedback-criteria.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
