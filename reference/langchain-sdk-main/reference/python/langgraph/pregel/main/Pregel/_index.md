---
title: "reference/python/langgraph/pregel/main/Pregel"
description: "Index of 56 pages and 0 subdirectories under reference/python/langgraph/pregel/main/Pregel."
category: "index"
tags: [index, reference, python, langgraph, pregel, main, pregel]
---

# reference/python/langgraph/pregel/main/Pregel

56 pages here.

## Files

- [InputType](InputType.md) - View source on GitHub
- [OutputType](OutputType.md) - View source on GitHub
- [abulk_update_state](abulk_update_state.md) - Asynchronously apply updates to the graph state in bulk. Requires a checkpointer to be set.
- [aclear_cache](aclear_cache.md) - Asynchronously clear the cache for the given nodes.
- [aget_graph](aget_graph.md) - Return a drawable representation of the computation graph.
- [aget_state](aget_state.md) - Get the current state of the graph.
- [aget_state_history](aget_state_history.md) - Asynchronously get the history of the state of the graph.
- [aget_subgraphs](aget_subgraphs.md) - Get the subgraphs of the graph.
- [ainvoke](ainvoke.md) - Asynchronously run the graph with a single input and config.
- [astream](astream.md) - Asynchronously stream graph steps for a single input.
- [astream_events](astream_events.md) - Async variant of stream_events.
- [aupdate_state](aupdate_state.md) - Asynchronously update the state of the graph with the given values, as if they came from node as_node. If as_node is not provided, it will be set to the last node that updated the state, if not...
- [bulk_update_state](bulk_update_state.md) - Apply updates to the graph state in bulk. Requires a checkpointer to be set.
- [cache](cache.md) - Cache to use for storing node results.
- [cache_policy](cache_policy.md) - Cache policy to use for all nodes. Can be overridden by individual nodes.
- [channels](channels.md) - View source on GitHub
- [checkpointer](checkpointer.md) - Checkpointer used to save and load graph state.
- [clear_cache](clear_cache.md) - Clear the cache for the given nodes.
- [config](config.md) - View source on GitHub
- [config_schema](config_schema.md) - config_schema is deprecated. Use get_context_jsonschema for the relevant schema instead.
- [context_schema](context_schema.md) - Specifies the schema for the context object that will be passed to the workflow.
- [copy](copy.md) - View source on GitHub
- [debug](debug.md) - Whether to print debug information during execution.
- [get_config_jsonschema](get_config_jsonschema.md) - get_config_jsonschema is deprecated. Use get_context_jsonschema instead.
- [get_context_jsonschema](get_context_jsonschema.md) - View source on GitHub
- [get_graph](get_graph.md) - Return a drawable representation of the computation graph.
- [get_input_jsonschema](get_input_jsonschema.md) - View source on GitHub
- [get_input_schema](get_input_schema.md) - View source on GitHub
- [get_output_jsonschema](get_output_jsonschema.md) - View source on GitHub
- [get_output_schema](get_output_schema.md) - View source on GitHub
- [get_state](get_state.md) - Get the current state of the graph.
- [get_state_history](get_state_history.md) - Get the history of the state of the graph.
- [get_subgraphs](get_subgraphs.md) - Get the subgraphs of the graph.
- [input_channels](input_channels.md) - View source on GitHub
- [interrupt_after_nodes](interrupt_after_nodes.md) - View source on GitHub
- [interrupt_before_nodes](interrupt_before_nodes.md) - View source on GitHub
- [invoke](invoke.md) - Run the graph with a single input and config.
- [name](name.md) - View source on GitHub
- [node_error_handler_map](node_error_handler_map.md) - View source on GitHub
- [nodes](nodes.md) - View source on GitHub
- [output_channels](output_channels.md) - View source on GitHub
- [retry_policy](retry_policy.md) - Retry policies to use when running tasks. Empty set disables retries.
- [step_timeout](step_timeout.md) - Maximum time to wait for a step to complete, in seconds.
- [store](store.md) - Memory store to use for SharedValues.
- [stream](stream.md) - Stream graph steps for a single input.
- [stream_channels](stream_channels.md) - Channels to stream, defaults to all channels not in reserved channels
- [stream_channels_asis](stream_channels_asis.md) - View source on GitHub
- [stream_channels_list](stream_channels_list.md) - View source on GitHub
- [stream_eager](stream_eager.md) - Whether to force emitting stream events eagerly, automatically turned on for stream_mode "messages" and "custom".
- [stream_events](stream_events.md) - Stream events from this graph.
- [stream_mode](stream_mode.md) - Mode to stream output, defaults to 'values'.
- [stream_transformers](stream_transformers.md) - View source on GitHub
- [trigger_to_nodes](trigger_to_nodes.md) - View source on GitHub
- [update_state](update_state.md) - Update the state of the graph with the given values, as if they came from node as_node. If as_node is not provided, it will be set to the last node that updated the state, if not ambiguous.
- [validate](validate.md) - View source on GitHub
- [with_config](with_config.md) - Create a copy of the Pregel object with an updated config.
