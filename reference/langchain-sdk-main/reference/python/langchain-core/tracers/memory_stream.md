---
title: "memory_stream"
description: "Module implements a memory stream for communication between two co-routines."
source: "https://reference.langchain.com/python/langchain-core/tracers/memory_stream"
category: "reference"
tags: [reference, langchain-core, tracers, memory_stream]
---

# memory_stream

> **Module** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/memory_stream)

Module implements a memory stream for communication between two co-routines.

This module provides a way to communicate between two co-routines using a memory
channel. The writer and reader can be in the same event loop or in different event
loops. When they're in different event loops, they will also be in different threads.

Useful in situations when there's a mix of synchronous and asynchronous used in the
code.

## Properties

- `T`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/tracers/memory_stream.py)
