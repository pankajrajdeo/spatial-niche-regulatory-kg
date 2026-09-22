---
title: "Delta Channels: Evolving our Runtime for Long-Running Agents"
description: "Long-running agents have a storage problem: checkpointing full state at every step grows at O(N²). DeltaChannel is a new primitive in LangGraph 1.2 that checkpoints only the diff each step and writes..."
source: "https://www.langchain.com/blog/delta-channels-evolving-agent-runtime"
category: "blog"
published: "2026-05-12T19:00:00.000Z"
author: "LangChain Accounts"
tags: [blog, delta-channels-evolving-agent-runtime]
---

# Delta Channels: Evolving our Runtime for Long-Running Agents

- Checkpoint storage under the default full-snapshot model grows at O(N²) — for agents with long message histories and filesystem-backed context, this becomes a real operational cost fast.
- `DeltaChannel` stores only the delta each step and writes periodic full snapshots every K steps, bounding resume latency while keeping storage costs flat as sessions grow longer.
- The upgrade is transparent: existing threads continue to work, both `messages` and `files` are delta-backed by default in Deep Agents v0.6, and the full LangGraph API surface (interrupts, time-travel, tooling) is unchanged.
