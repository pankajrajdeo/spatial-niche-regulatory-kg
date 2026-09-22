---
title: "How Similarweb Evaluates Long-Form Agent Research Reports with LangSmith"
description: "Learn how Similarweb uses LangSmith to evaluate long-form agent research reports with rubrics, faithfulness checks, traces, and baseline comparisons."
source: "https://www.langchain.com/blog/how-similarweb-evaluates-long-form-agent-research-reports-with-langsmith"
category: "blog"
published: "2026-07-29T15:30:00.000Z"
author: "LangChain Accounts"
tags: [blog, how-similarweb-evaluates-long-form-agent-research-reports-with-langsmith]
---

# How Similarweb Evaluates Long-Form Agent Research Reports with LangSmith

- Match the evaluation method to the output. Golden answers work for focused questions, while long-form reports need rubrics, faithfulness checks, and baseline comparisons.
- Treat scores as signals, not answers. Similarweb used LangSmith to connect each score to evaluator comments, traces, and A/B comparisons.
- Calibrate rubrics before trusting results. Poorly weighted criteria can make a good agent update look like a regression.
