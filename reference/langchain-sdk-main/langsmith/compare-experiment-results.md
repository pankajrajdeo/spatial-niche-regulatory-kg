---
title: "How to compare experiment results"
description: "When you are iterating on your LLM application (such as changing the model or the prompt), you may want to compare the results of different experiments."
source: "https://docs.langchain.com/langsmith/compare-experiment-results"
category: "docs"
tags: [docs, langsmith, compare-experiment-results]
---

# How to compare experiment results

When you are iterating on your LLM application (such as changing the model or the prompt), you may want to compare the results of different [*experiments*](evaluation-concepts.md#experiment).

LangSmith supports a comparison view that lets you identify key differences, regressions, and improvements between different experiments.

## Open the comparison view

1. To access the experiment comparison view, navigate to the **Datasets & Experiments** page.
2. Select a dataset, which will open the **Experiments** tab.
3. Select two or more experiments and then click **Compare**.

<img src="https://mintcdn.com/langchain-5e9cc07a/1hHTBw6gWTjwKQ8j/langsmith/images/compare-select-light.png?fit=max&auto=format&n=1hHTBw6gWTjwKQ8j&q=85&s=a0afa6f50aa177479c59dfb5918e23b2" alt="The Experiments view in the UI with 3 experiments selected and the Compare button highlighted, in light mode." width="2558" height="1668" data-path="langsmith/images/compare-select-light.png" />

<img src="https://mintcdn.com/langchain-5e9cc07a/1hHTBw6gWTjwKQ8j/langsmith/images/compare-select-dark.png?fit=max&auto=format&n=1hHTBw6gWTjwKQ8j&q=85&s=9c03785dba917b9a9c1fde453c68a881" alt="The Experiments view in the UI with 3 experiments selected and the Compare button highlighted, in dark mode." width="2552" height="1664" data-path="langsmith/images/compare-select-dark.png" />

## Adjust the table display

You can toggle between different display options on the top right of the comparison view.

<img src="https://mintcdn.com/langchain-5e9cc07a/Tdk8epB4BZgbugRX/langsmith/images/comparison-table-display-options-light.png?fit=max&auto=format&n=Tdk8epB4BZgbugRX&q=85&s=3a2df7e04c17d1c97d3e377af178f7c6" alt="Table display options, in light mode." width="477" height="170" data-path="langsmith/images/comparison-table-display-options-light.png" />

<img src="https://mintcdn.com/langchain-5e9cc07a/Tdk8epB4BZgbugRX/langsmith/images/comparison-table-display-options-dark.png?fit=max&auto=format&n=Tdk8epB4BZgbugRX&q=85&s=30a94735be39598d8a5735a2201a7e55" alt="Table display options, in dark mode." width="469" height="165" data-path="langsmith/images/comparison-table-display-options-dark.png" />

### Filters

Click the  icon to apply filters to the comparison view to narrow down specific examples. Common examples for filters include:

* Examples that contain specific `input` / `output`.
* Runs with status `success` or `error`.
* Runs that take more than x seconds in `latency`.
* Specific `metadata`, `tag`, or `feedback`.

In addition to applying filters on the overall experiment view, you can apply filters on individual columns as well. Select the  icon at the top of any column to view the available filters for that column's data.

### Columns

Click the  icon to show or hide individual feedback keys or metrics in the comparison view.

### Table views

Select one of three table view icons at the top right of the comparison view:

* **Compact**: Shows a preview of the experiment results for each example.
* **Full**: Shows the full text of the input, output, and reference output for each run. If the output is too long to display in the table, you can click **Expand** to view the full content.
* **Diff**: Shows the text difference between experiment outputs for each run. This is only supported for 2 experiments at a time. See [View side-by-side diffs](#view-side-by-side-diffs) for more details.

### Display types

There are three built-in experiment views that cover several display types: **Default**, **YAML**, **JSON**.

## View regressions and improvements

In the comparison view, red highlights runs that *regressed* on any feedback key against your source experiment, while green highlights runs that *improved*. At the top of each feedback column, you can see how many runs did better or worse than your source experiment.

Click the regression or improvement buttons at the top of each column to show only runs that regressed or improved in that experiment.

<img src="https://mintcdn.com/langchain-5e9cc07a/bhZ1YZGp3sIXMhGI/langsmith/images/regression-view-light.png?fit=max&auto=format&n=bhZ1YZGp3sIXMhGI&q=85&s=7328cf7a58d50e9c1af1c7b12cbd36fa" alt="The comparison view comparing 4 experiments with the regressions and improvements in red and green respectively." width="1294" height="777" data-path="langsmith/images/regression-view-light.png" />

<img src="https://mintcdn.com/langchain-5e9cc07a/bhZ1YZGp3sIXMhGI/langsmith/images/regression-view-dark.png?fit=max&auto=format&n=bhZ1YZGp3sIXMhGI&q=85&s=1c9321a7bd96092632967eae55aca6a9" alt="The comparison view comparing 4 experiments with the regressions and improvements in red and green respectively." width="1294" height="766" data-path="langsmith/images/regression-view-dark.png" />

## View side-by-side diffs

When comparing two experiments, for JSON and YAML display styles, you can toggle on the experiment diff mode to compare experiment outputs. The diff mode highlights modifications between outputs, and can be particularly useful for structured output comparisons.

<img src="https://mintcdn.com/langchain-5e9cc07a/Tdk8epB4BZgbugRX/langsmith/images/comparison-diff-view-light.png?fit=max&auto=format&n=Tdk8epB4BZgbugRX&q=85&s=2ddb234fd3779b443b9e41f7addeef21" alt="The comparison diff mode in light." width="1038" height="758" data-path="langsmith/images/comparison-diff-view-light.png" />

<img src="https://mintcdn.com/langchain-5e9cc07a/Tdk8epB4BZgbugRX/langsmith/images/comparison-diff-view-dark.png?fit=max&auto=format&n=Tdk8epB4BZgbugRX&q=85&s=de5881d56cade5557d879a1f910dd59e" alt="The comparison diff mode in dark." width="1017" height="810" data-path="langsmith/images/comparison-diff-view-dark.png" />

## Update source experiment and metric

To track regressions across experiments, you can:

1. At the top of the comparison view, hover over an experiment icon and select **Set as source experiment** from the dropdown. You can also add or remove experiments from this dropdown. By default, the first selected experiment is set as the source.

   <img src="https://mintcdn.com/langchain-5e9cc07a/XfIIVcx3AjKjd794/langsmith/images/set-source-experiment-light.png?fit=max&auto=format&n=XfIIVcx3AjKjd794&q=85&s=8d251f120d6df74241555b9a859ad066" alt="Setting a source experiment from the experiment icons at the top of the Comparison view." width="873" height="484" data-path="langsmith/images/set-source-experiment-light.png" />

   <img src="https://mintcdn.com/langchain-5e9cc07a/XfIIVcx3AjKjd794/langsmith/images/set-source-experiment-dark.png?fit=max&auto=format&n=XfIIVcx3AjKjd794&q=85&s=cce0d6e5a7c972a8493abfcfd0dff8d4" alt="Setting a source experiment from the experiment icons at the top of the Comparison view." width="892" height="489" data-path="langsmith/images/set-source-experiment-dark.png" />

2. Within the **Feedback** columns, you can configure whether a higher score is better for each feedback key. This preference will be stored. By default, a higher score is assumed to be better.

   <img src="https://mintcdn.com/langchain-5e9cc07a/3sTv76KEq6zVyh80/langsmith/images/comparison-feedback-score-light.png?fit=max&auto=format&n=3sTv76KEq6zVyh80&q=85&s=1d860f0f7de66370d9afb00985d9a757" alt="Dropdown for feedback metric column, configuring whether a higher score is better, in light mode." width="621" height="233" data-path="langsmith/images/comparison-feedback-score-light.png" />

   <img src="https://mintcdn.com/langchain-5e9cc07a/3sTv76KEq6zVyh80/langsmith/images/comparison-feedback-score-dark.png?fit=max&auto=format&n=3sTv76KEq6zVyh80&q=85&s=0a8acf05f77a949c338df2a41e531b9f" alt="Dropdown for feedback metric column, configuring whether a higher score is better, in dark mode." width="602" height="188" data-path="langsmith/images/comparison-feedback-score-dark.png" />

## Expand details panel

Click on any row to open a details panel for that example for the compared experiments.

Use the toggle in the top right of the panel to switch between two modes:

* **Details**: Shows feedback keys and scores, along with a metrics summary for the example, as well as the input, output, and reference output, and attributes for each experiment.

  <img src="https://mintcdn.com/langchain-5e9cc07a/Tdk8epB4BZgbugRX/langsmith/images/expanded-view-details-light.png?fit=max&auto=format&n=Tdk8epB4BZgbugRX&q=85&s=ea0b5751150db5cdf34f1c7dbfd43fb0" alt="An example in the expanded Comparing Experiments view, in light mode." width="1863" height="906" data-path="langsmith/images/expanded-view-details-light.png" />

  <img src="https://mintcdn.com/langchain-5e9cc07a/Tdk8epB4BZgbugRX/langsmith/images/expanded-view-details-dark.png?fit=max&auto=format&n=Tdk8epB4BZgbugRX&q=85&s=6f9f684e16e2e4dd2721ccfbdd9fc38f" alt="An example in the expanded Comparing Experiments view, in dark mode." width="1858" height="904" data-path="langsmith/images/expanded-view-details-dark.png" />

* **Traces**: Shows traces for each experiment side by side.

  <img src="https://mintcdn.com/langchain-5e9cc07a/Tdk8epB4BZgbugRX/langsmith/images/expanded-view-traces-light.png?fit=max&auto=format&n=Tdk8epB4BZgbugRX&q=85&s=a775783ae9395da8cc2daea6855bef53" alt="An example in the expanded Comparing Experiments view, in light mode." width="1866" height="845" data-path="langsmith/images/expanded-view-traces-light.png" />

  <img src="https://mintcdn.com/langchain-5e9cc07a/Tdk8epB4BZgbugRX/langsmith/images/expanded-view-traces-dark.png?fit=max&auto=format&n=Tdk8epB4BZgbugRX&q=85&s=789e3f2857e8a3c41dae928091bbcb96" alt="An example in the expanded Comparing Experiments view, in dark mode." width="1872" height="846" data-path="langsmith/images/expanded-view-traces-dark.png" />

When comparing more than two experiments, the panel displays two experiments at a time. Use the header to switch which experiment you are comparing against.

## Use experiment metadata as chart labels

You can configure the x-axis labels for the charts based on [experiment metadata](filter-experiments-ui.md#background-add-metadata-to-your-experiments).

Select a metadata key from the **Charts** dropdown at the top-right of the comparison view to change the x-axis labels.

<img src="https://mintcdn.com/langchain-5e9cc07a/PTrqmKVkPbIbL9pX/langsmith/images/metadata-in-charts-light.png?fit=max&auto=format&n=PTrqmKVkPbIbL9pX&q=85&s=5d854c56e536fc7e60f2cebc4f3d2711" alt="x-axis dropdown highlighted with a list of the metadata attached to the experiment, in light mode." width="426" height="513" data-path="langsmith/images/metadata-in-charts-light.png" />

<img src="https://mintcdn.com/langchain-5e9cc07a/PTrqmKVkPbIbL9pX/langsmith/images/metadata-in-charts-dark.png?fit=max&auto=format&n=PTrqmKVkPbIbL9pX&q=85&s=e88360d00946191ce316fafe276984c3" alt="x-axis dropdown highlighted with a list of the metadata attached to the experiment, in dark mode." width="406" height="478" data-path="langsmith/images/metadata-in-charts-dark.png" />

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/compare-experiment-results.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
