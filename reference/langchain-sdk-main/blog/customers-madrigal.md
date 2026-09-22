---
title: "How Madrigal Built a Flexible and Scalable Multi-Agent Research and Intelligence Platform for Pharma with LangChain and LangSmith"
description: "See how Madrigal Pharmaceuticals built a modular, multi-agent research platform on LangChain and LangGraph. They deployed on LangSmith and went from prototype to enterprise deployment in weeks."
source: "https://www.langchain.com/blog/customers-madrigal"
category: "blog"
published: "2026-04-29T16:00:00.000Z"
author: "LangChain Accounts"
tags: [blog, customers-madrigal]
---

# How Madrigal Built a Flexible and Scalable Multi-Agent Research and Intelligence Platform for Pharma with LangChain and LangSmith

- **Abstracting data sources is what makes multi-agent systems scale.** Madrigal normalized every data source into a consistent tool interface. Agents don't care where data came from; they just use it. That abstraction is what lets you add new domains without rewriting orchestration logic.
- **Modular skills turn a single use case into a platform.** Instead of hardcoding workflows, Madrigal built each capability as a swappable skill. When a new need emerged, they defined a new skill, not a new system. New use cases went from weeks of development to hours, and deployment complexity didn't grow with scope.
- **Observability is what closes the loop between prototype and production.** LangSmith tracing gave Madrigal visibility into every tool call, retrieved chunk, and agent decision. More importantly, production failures fed automatically back into their eval suite so the system learned from real errors, not synthetic test cases.
