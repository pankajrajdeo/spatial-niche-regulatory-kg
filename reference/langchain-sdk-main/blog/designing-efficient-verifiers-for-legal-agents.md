---
title: "Designing Efficient Verifiers for Legal Agents"
description: "A Harvey and LangChain Labs study on making LLM verifiers cheaper and more reliable for legal-agent evaluation and post-training."
source: "https://www.langchain.com/blog/designing-efficient-verifiers-for-legal-agents"
category: "blog"
published: "2026-06-02T16:45:00.000Z"
author: "LangChain Accounts"
tags: [blog, designing-efficient-verifiers-for-legal-agents]
---

# Designing Efficient Verifiers for Legal Agents

- Verifiers can be a cost bottleneck for running agent evaluations and RL post-training at scale.
- We find we can reduce verifier costs by an order of magnitude by batching verifiers and using open models.
- Tuning prompts for verifiers allow us to target particular behavior further.
