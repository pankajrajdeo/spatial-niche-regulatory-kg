---
title: "How many of your agent&#39;s calls actually need a frontier model?"
description: "We benchmarked NVIDIA NeMo Switchyard on 145 agent tasks. Only 7% of turns needed a frontier model, and routing cut cost 74% for six points of accuracy."
source: "https://www.langchain.com/blog/switchyard-agent-routing-benchmark"
category: "blog"
published: "2026-08-11T18:00:00.000Z"
author: "LangChain Accounts"
tags: [blog, switchyard-agent-routing-benchmark]
---

# How many of your agent&#39;s calls actually need a frontier model?

1. **Not all turns need your best model.** We measured 7%, and those calls carried 68% of the bill
2. **Routing is a trade.** 74% cheaper for about six points of accuracy reduction
3. **Run the cost tradeoff formula before you build anything.** Judge cost divided by the price gap gives the offload you need. If your two models are close in price, that number climbs past 100% and routing cannot pay unless you host the cheap model yourself
