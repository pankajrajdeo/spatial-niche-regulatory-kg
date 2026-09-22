---
title: "Manage evaluators"
description: "View and manage evaluators at the workspace level in LangSmith."
source: "https://docs.langchain.com/langsmith/evaluators"
category: "docs"
tags: [docs, langsmith, evaluators]
---

# Manage evaluators

> View and manage evaluators at the workspace level in LangSmith.

[Evaluators](evaluation-concepts.md#evaluators) in LangSmith are [workspace-level](administration-overview.md#workspaces) resources. You can attach a single evaluator to multiple [tracing projects](observability-concepts.md#projects) and [datasets](evaluation-concepts.md#datasets), so you can apply consistent evaluation logic across your work without recreating it each time.

> [!TIP]
> Evaluator scores are a high-priority signal for the [LangSmith Engine](engine.md): it pulls low-scoring traces when choosing what to analyze, so attaching an evaluator to a project sharpens the issues Engine finds there.

## View evaluators

In the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-evaluators), select **Evaluators** in the left sidebar to view all evaluators in your workspace.

The evaluators table shows the following columns:

| Column                            | Description                                                                                                                                                                     |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name                              | The evaluator name                                                                                                                                                              |
| Type                              | **LLM as a judge** or **Code**. Composite score evaluators are scoped to individual tracing projects and datasets and do not appear here.                                       |
| Feedback Key                      | The feedback key the evaluator produces                                                                                                                                         |
| Projects & Datasets               | Tracing projects and datasets this evaluator is attached to                                                                                                                     |
| Evaluator Trace Count (this week) | Number of traces this evaluator ran on in the past week. Only shown when spend tracking is enabled; **–** for Code evaluators or evaluators with no attached rules.             |
| Spend (this week)                 | Estimated USD spend for this evaluator in the past week. Only shown when spend tracking is enabled; **–** for Code evaluators or evaluators with no attached rules.             |
| Spend Status                      | Whether the evaluator is **Under limits**, **Unlimited**, or has hit one or more configured spend limits. Only shown when spend tracking is enabled; **–** for Code evaluators. |
| Created By                        | The workspace member who created the evaluator                                                                                                                                  |
| Updated At                        | When the evaluator was last modified                                                                                                                                            |
| Created At                        | When the evaluator was created                                                                                                                                                  |

## Create an evaluator

You can create an evaluator in the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-evaluators) or programmatically with the [SDK](#create-an-evaluator-with-the-sdk). Evaluators created either way are workspace-level resources that appear in the **Evaluators** table.

### Create an evaluator in the UI

1. In the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-evaluators), select **Evaluators** in the left sidebar.
2. Click **+ Evaluator** to open the new evaluator panel.
3. The panel lets you:
   * **Create from scratch**: Build a new [LLM-as-a-Judge](llm-as-judge.md) or [Code](online-evaluations-code.md) evaluator.
   * **Add a LangChain Tuned Evaluator**: Attach a [specialized judge managed by LangChain](tuned-evaluators.md) to a compatible tracing project without configuring a prompt, model, or API key.
   * **Create from a template**: Start from a ready-made evaluator (also known as a prebuilt evaluator) for common evaluation patterns. A **Recommended** section surfaces popular templates first, followed by templates organized by the following categories:

     | Category          | Description                                          |
     | ----------------- | ---------------------------------------------------- |
     | Security          | Detect leaks, injections, and adversarial inputs.    |
     | Safety            | Evaluate content safety and moderation.              |
     | Quality           | Measure output quality and accuracy.                 |
     | Conversation      | Evaluate conversational quality and user experience. |
     | Trajectory        | Evaluate agent tool use and decision paths.          |
     | Image Evaluations | Evaluate image content quality and safety.           |
     | Voice Evaluation  | Evaluate voice and audio interaction quality.        |

You can also add an evaluator directly from a [tracing project](observability-concepts.md#projects) or [dataset](evaluation-concepts.md#datasets). In that flow, you can additionally **attach an existing evaluator** from your workspace, or create a [Composite](composite-evaluators-ui.md) evaluator. Refer to [Set up LLM-as-a-judge online evaluators](online-evaluations-llm-as-judge.md) and [Automatically run evaluators on experiments](bind-evaluator-to-dataset.md).

### Create an evaluator with the SDK

Use the LangSmith SDK to create evaluators programmatically. The SDK is available for [Python](smith-python-sdk.md) and [TypeScript](smith-js-ts-sdk.md). Evaluators created through the SDK appear in the **Evaluators** table alongside those created in the UI.

> [!NOTE]
> Managing evaluators through the SDK requires `langsmith>=0.9.8` (Python, PyPI) or `langsmith>=0.7.16` (TypeScript, npm).

**Python**

```python
import asyncio

from langsmith import Client

async def main():
    client = Client()

    created = await client.evaluators.create(
        name="Correctness evaluator",
        type="code",
        code_evaluator={
            "code": "def perform_eval(run, example):\n    return {'score': 1}",
            "language": "python",
        },
    )
    print("Created evaluator:", created.evaluator.id)

asyncio.run(main())
```

**TypeScript**

```typescript
import { Client } from "langsmith";

const client = new Client();

const created = await client.evaluators.create({
  name: "Correctness evaluator",
  type: "code",
  code_evaluator: {
    code: "def perform_eval(run, example):\n    return {'score': 1}",
    language: "python",
  },
});
console.log("Created evaluator:", created.evaluator?.id);
```

To create an LLM-as-a-judge evaluator and to retrieve, update, list, or delete evaluators, refer to [Manage evaluators with the SDK](manage-evaluators-sdk.md).

## View evaluator details

Click any evaluator in the table to open its detail view. The detail view has four tabs:

* **Overview**: The evaluator's feedback configuration and prompt or code definition.
* **Traces**: Traces processed by this evaluator across all attached resources.
* **Logs**: Execution logs for this evaluator across all attached resources.
* **Projects & Datasets**: The tracing projects and datasets this evaluator is attached to, with each attachment's [weekly spend and limit](evaluator-spend.md).

## Edit an evaluator

Open an evaluator. In the **Overview** tab, click the **Edit evaluator**  icon to open the **Configure Evaluator** panel. Update the evaluator's configuration. Click **Save**.

Because the evaluator is shared, changes apply across all tracing projects and datasets it is attached to.

## Manage evaluator trace retention

When an online evaluator scores a trace, it attaches feedback to the trace. This can auto-upgrade the trace to [extended retention](usage-and-billing.md#data-retention-auto-upgrades), depending on the evaluator's retention setting. Extended retention keeps the trace longer but costs more. When you set up an online evaluator on a [tracing project](observability-concepts.md#projects), you can opt out of this upgrade so that scored traces stay at the project's base retention.

This control is available only when the project's [default retention](billing.md#change-project-level-default-retention) is the [base tier](usage-and-billing.md#how-it-works). If the project defaults to extended retention ([set at the project or workspace level](data-purging-compliance.md#data-retention)), traces scored by the evaluator follow that default and the option is locked.

To opt out of extending retention for scored traces:

1. When you [create](#create-an-evaluator) or [edit](#edit-an-evaluator) an online evaluator, set the source to a [tracing project](observability-concepts.md#projects), rather than a [dataset](evaluation-concepts.md#datasets).
2. Expand the **Advanced** section in the evaluator configuration panel.
3. Clear **Extend trace retention**.

The change applies to traces scored after you save the evaluator. Existing scored traces keep their current retention tier.

The **Extend trace retention** toggle described above applies to both trace-level and thread-level (multi-turn) online evaluators. For more information on multi-turn evaluators, see [Set up multi-turn online evaluators](online-evaluations-multi-turn.md).

## Include extended stats

Use **Include extended stats (feedback, costs, tokens)** in a [run-level evaluator](online-evaluations-llm-as-judge.md) to evaluate feedback statistics, token usage, or cost data from the run. The `feedback_stats` field contains feedback statistics, including the number and average for each feedback key. This option is not available for [multi-turn (thread-level) evaluators](online-evaluations-multi-turn.md).

LangSmith fetches additional data for evaluators with this option enabled. Enable it only when your evaluation logic or prompt requires these fields.

To include extended stats:

1. When you [create](#create-an-evaluator) or [edit](#edit-an-evaluator) a run-level evaluator, expand the **Advanced** section in the evaluator configuration panel.
2. Select **Include extended stats (feedback, costs, tokens)**.

### Access extended stats

[Code evaluators](online-evaluations-code.md) receive these fields in the `run` object, including `feedback_stats`, `total_tokens`, and `total_cost`. They also receive [individual feedback records](feedback-data-format.md) in `run["feedback"]`, regardless of whether you enable extended stats. For [LLM-as-a-judge evaluators](online-evaluations-llm-as-judge.md), map the corresponding `run.*` field to a prompt variable. For example, map `{{correctness_average}}` to `run.feedback_stats.correctness.avg` to include a `correctness` feedback average in the prompt. The available `run.*` fields also include prompt and completion token, cost, and detail fields. For the full run data schema, see [Run data format](run-data-format.md).

### Chain evaluators

Extended stats can be used to chain evaluators, where a code evaluator reads a score that another evaluator already produced. Filter the second evaluator on the first evaluator's feedback key (for example, `has(feedback_key, "answer_usefulness")`), then enable extended stats. The filter makes the code evaluator run only after the score exists, and extended stats make the score readable at `run["feedback_stats"]["answer_usefulness"]["avg"]`.

The filter matches on the feedback key rather than the evaluator that produced it, so feedback from any source with that key triggers the code evaluator. To configure the filter, see [Apply a filter to runs that trigger the evaluator](online-evaluations-code.md#configure-online-evaluators).

## Delete an evaluator

You cannot delete an evaluator while it is attached to a tracing project or dataset. To delete an evaluator:

1. In the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-evaluators), select **Evaluators** in the left sidebar.
2. Select the evaluator you want to delete.
3. Open the **Projects & Datasets** tab. For each attached tracing project and dataset, select **Detach** in the **Actions** menu at the right of the row.
4. Return to the **Evaluators** page and click **Delete** at the top of the page.

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/evaluators.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
