---
title: "Set up composite online evaluators"
description: "Online evaluations provide real-time feedback on your production traces. This is useful to continuously monitor the performance of your application: to identify issues, measure improvements, and..."
source: "https://docs.langchain.com/langsmith/online-evaluations-composite"
category: "docs"
tags: [docs, langsmith, online-evaluations-composite]
---

# Set up composite online evaluators

[Online evaluations](evaluation-concepts.md#online-evaluations) provide real-time feedback on your production [traces](observability-concepts.md#traces). This is useful to continuously monitor the performance of your application: to identify issues, measure improvements, and ensure consistent quality over time.

[**Composite evaluators**](composite-evaluators-ui.md) are a way to combine multiple evaluator scores into a single [score](evaluation-concepts.md#evaluator-outputs). This is useful when you want to evaluate multiple aspects of your application and combine the results into a single result.

When an online evaluator runs on any run within a trace, the trace will be auto-upgraded to [extended data retention](usage-and-billing.md#data-retention-auto-upgrades). This upgrade will impact trace pricing, but ensures that traces meeting your evaluation criteria (typically those most valuable for analysis) are preserved for investigation. 

## View online evaluators

Head to the **Tracing Projects** tab and select a tracing project. To view existing online evaluators for that project, click on the **Evaluators** tab.

## Configure composite online evaluators

You can create composite evaluators on a [tracing project](observability-concepts.md#projects) for [online evaluations](evaluation-concepts.md#online-evaluations). With composite evaluators in the UI, you can compute a weighted average or weighted sum of multiple evaluator scores, with configurable weights.

### 1. Navigate to the tracing project

To start configuring a composite evaluator, navigate to the **Tracing** page and select a tracing project.

From the tracing project view, navigate to the **Evaluators** tab. Click **+ Evaluator** to open the **Add Evaluator** panel. Click **Composite Score** under **Create from scratch**.

### 2. Configure the composite evaluator

1. Name your evaluator.
2. Select an aggregation method, either **Average** or **Sum**.
   * **Average**: ∑(weight\*score) / ∑(weight).
   * **Sum**: ∑(weight\*score).
3. Add the feedback keys you want to include in the composite score.
4. Add the weights for the feedback keys. By default, the weights are equal for each feedback key. Adjust the weights to increase or decrease the importance of specific feedback keys in the final score.
5. Click **Create** to save the evaluator.

 If you need to adjust the weights for the composite scores, they can be updated after the evaluator is created. The resulting scores will be updated for all runs that have the evaluator configured. 

### 3. View composite evaluator results

Composite scores are attached to a run as **feedback**, similarly to feedback from a single evaluator.

**On a tracing project**:

* Composite scores appear as feedback on runs.
* [Filter for runs](filter-traces.md) with a composite score, or where the composite score meets a certain threshold.
* [Create a chart](dashboards.md#custom-dashboards) to visualize trends in the composite score over time.

 If any of the constituent evaluators are not configured on the run, the composite score will not be calculated for that run. 

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/online-evaluations-composite.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
