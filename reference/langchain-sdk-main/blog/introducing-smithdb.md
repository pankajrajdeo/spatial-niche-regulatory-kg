---
title: "We built SmithDB, the data layer for agent observability"
description: "Introducing SmithDB: LangSmith&#39;s purpose-built distributed database for agent observability, delivering up to 12x faster performance with full portability."
source: "https://www.langchain.com/blog/introducing-smithdb"
category: "blog"
published: "2026-05-13T17:39:00.000Z"
author: "LangChain Accounts"
tags: [blog, introducing-smithdb]
---

# We built SmithDB, the data layer for agent observability

- **Agent traces have outgrown traditional observability stores** — modern agent traces contain hundreds of nested spans, multi-modal content, and spans that stay open for hours, creating data volumes and query patterns that general-purpose databases were never designed to handle.
- **SmithDB delivers industry-leading performance across every key observability workload** — with P50 latencies of 92ms for trace tree loads, 400ms for full-text search, and 82ms for run filtering, it makes core LangSmith experiences up to 15x faster than before.
- **A portable, scalable architecture built for enterprise needs** — backed by object storage with stateless ingestion and query services, SmithDB scales by adding compute rather than managing local disks, making it straightforward to deploy in self-hosted and multi-cloud environments.
