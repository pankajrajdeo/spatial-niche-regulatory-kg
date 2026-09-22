---
title: "reference/python/langgraph/pregel/_read/PregelNode"
description: "Index of 22 pages and 0 subdirectories under reference/python/langgraph/pregel/_read/PregelNode."
category: "index"
tags: [index, reference, python, langgraph, pregel, read, pregelnode]
---

# reference/python/langgraph/pregel/_read/PregelNode

22 pages here.

## Files

- [ainvoke](ainvoke.md) - View source on GitHub
- [astream](astream.md) - View source on GitHub
- [bound](bound.md) - The main logic of the node. This will be invoked with the input from channels.
- [cache_policy](cache_policy.md) - The cache policy to use when invoking the node.
- [channels](channels.md) - The channels that will be passed as input to bound. If a str, the node will be invoked with its value if it isn't empty. If a list, the node will be invoked with a dict of those channels' values.
- [copy](copy.md) - View source on GitHub
- [error_handler_node](error_handler_node.md) - Optional handler node name for failures from this node.
- [flat_writers](flat_writers.md) - Get writers with optimizations applied. Dedupes consecutive ChannelWrites.
- [input_cache_key](input_cache_key.md) - Get a cache key for the input to the node. This is used to avoid calculating the same input multiple times.
- [invoke](invoke.md) - View source on GitHub
- [is_error_handler](is_error_handler.md) - Whether this node is registered as an error handler node.
- [mapper](mapper.md) - A function to transform the input before passing it to bound.
- [metadata](metadata.md) - Metadata to attach to the node for tracing.
- [node](node.md) - Get a runnable that combines bound and writers.
- [retry_policy](retry_policy.md) - The retry policies to use when invoking the node.
- [stream](stream.md) - View source on GitHub
- [subgraphs](subgraphs.md) - Subgraphs used by the node.
- [tags](tags.md) - Tags to attach to the node for tracing.
- [timeout](timeout.md) - Timeout policy for a single invocation.
- [trace_policy](trace_policy.md) - Optional policy controlling what this node records on its trace run.
- [triggers](triggers.md) - If any of these channels is written to, this node will be triggered in the next step.
- [writers](writers.md) - A list of writers that will be executed after bound, responsible for taking the output of bound and writing it to the appropriate channels.
