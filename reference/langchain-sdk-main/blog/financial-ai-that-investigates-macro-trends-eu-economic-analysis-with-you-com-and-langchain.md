---
title: "EU macroeconomic analysis with Deep Agents, LangSmith, and the You.com Finance Research API"
description: "A Deep Agents research agent analyzes GDP across all 27 EU states, flags outliers like Ireland and Germany, and writes a cited briefing in about 45 minutes."
source: "https://www.langchain.com/blog/financial-ai-that-investigates-macro-trends-eu-economic-analysis-with-you-com-and-langchain"
category: "blog"
published: "2026-05-20T18:00:00.000Z"
author: "LangChain Accounts"
tags: [blog, financial-ai-that-investigates-macro-trends-eu-economic-analysis-with-you-com-and-langchain]
---

# EU macroeconomic analysis with Deep Agents, LangSmith, and the You.com Finance Research API

This macroeconomic research agent analyzes GDP data across all 27 EU member states, detects anomalies, investigates structural and cyclical drivers at the sector level, and produces a 13-section cited briefing in approximately 45 minutes. [Deep Agents](../deepagents/overview.md) orchestrates each research layer, [LangSmith](https://smith.langchain.com) captures every step, and every finding traces back to the primary source that produced it.

The You.com Finance Research API scores [87.29%](https://you.com/resources/introducing-the-finance-research-api-agentic-research-no-infra-required) on [FinSearchComp (arXiv 2509.13160)](https://arxiv.org/abs/2509.13160), a public financial services benchmark, with a full 27-country GDP run costing roughly $2.20 in API calls. It combines licensed structured data from providers including S&P Global with live web intelligence across central bank commentary, regulatory signals, and sector-level analysis.
