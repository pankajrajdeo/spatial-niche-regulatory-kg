---
title: "Tuning the harness, not the model: a Nemotron 3 Ultra playbook"
description: "We tuned an Nemotron 3 Ultra&#39;s harness to match Opus 4.8&#39;s best agent run at ~8x lower cost, changing only the scaffolding around it."
source: "https://www.langchain.com/blog/tuning-the-harness-not-the-model-a-nemotron-3-ultra-playbook"
category: "blog"
published: "2026-07-08T14:59:00.000Z"
author: "LangChain Accounts"
tags: [blog, tuning-the-harness-not-the-model-a-nemotron-3-ultra-playbook]
---

# Tuning the harness, not the model: a Nemotron 3 Ultra playbook

- **Near-frontier agent quality at a fraction of the cost.** Tuning the harness alone took Nemotron 3 Ultra to a best run of 0.86 on the Deep Agents suite, nearly matching Opus 4.8's best of 0.87, at roughly 10x lower cost per run (about $4.48 against $43.48 on the full suite) with latency at parity.**‍**
- **Evals are the training data for harness work.** Every change ran through a trace-driven loop, screened cheaply first, and earned its place only if the win repeated across trials and regressed nothing else.**‍**
- **Fit decides how much capability reaches the task. **A matched harness lets the model spend its capability on the work; a mismatched one makes it fight the scaffolding, and the gap between the two shows up in the score without touching the weights.**‍**
- **Harness tuning has a ceiling.** It fixes failures that come from the scaffolding, but it can't add what isn't in the weights, so a result that stays flat through every harness change points to post-training rather than another hook.
