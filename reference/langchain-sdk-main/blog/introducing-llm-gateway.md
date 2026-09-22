---
title: "LangSmith LLM Gateway: runtime governance built into the agent lifecycle"
description: "Introducing LangSmith LLM Gateway: runtime governance for AI agents with spend limits, PII redaction, and trace continuity, built directly into LangSmith."
source: "https://www.langchain.com/blog/introducing-llm-gateway"
category: "blog"
published: "2026-05-13T17:33:00.000Z"
author: "LangChain Accounts"
tags: [blog, introducing-llm-gateway]
---

# LangSmith LLM Gateway: runtime governance built into the agent lifecycle

- **LLM Gateway sits between your agents and LLM providers** — it enforces spend limits and redacts PII *before* requests reach the model, stopping problems at the source rather than just logging them after the fact.
- **Governance lives where you already work** — policy violations surface as traceable events inside LangSmith, so you can go from a blocked request to the triggering trace to a fix without switching tools.
- **Setup is a one-line change** — swap your `base_url` to the LangSmith Gateway endpoint, add your provider keys to workspace secrets, and set policies in the UI. No separate infrastructure required.
