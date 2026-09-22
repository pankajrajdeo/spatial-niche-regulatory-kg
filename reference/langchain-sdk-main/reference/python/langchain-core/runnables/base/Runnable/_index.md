---
title: "reference/python/langchain-core/runnables/base/Runnable"
description: "Index of 40 pages and 0 subdirectories under reference/python/langchain-core/runnables/base/Runnable."
category: "index"
tags: [index, reference, python, langchain-core, runnables, base, runnable]
---

# reference/python/langchain-core/runnables/base/Runnable

40 pages here.

## Files

- [InputType](InputType.md) - Input type.
- [OutputType](OutputType.md) - Output Type.
- [abatch](abatch.md) - Default implementation runs ainvoke in parallel using asyncio.gather.
- [abatch_as_completed](abatch_as_completed.md) - Run ainvoke in parallel on a list of inputs.
- [ainvoke](ainvoke.md) - Transform a single input into an output.
- [as_tool](as_tool.md) - Create a BaseTool from a Runnable.
- [assign](assign.md) - Assigns new fields to the dict output of this Runnable.
- [astream](astream.md) - Default implementation of astream, which calls ainvoke.
- [astream_events](astream_events.md) - Generate a stream of events.
- [astream_log](astream_log.md) - Stream all output from a Runnable, as reported to the callback system.
- [atransform](atransform.md) - Transform inputs to outputs.
- [batch](batch.md) - Default implementation runs invoke in parallel using a thread pool executor.
- [batch_as_completed](batch_as_completed.md) - Run invoke in parallel on a list of inputs.
- [bind](bind.md) - Bind arguments to a Runnable, returning a new Runnable.
- [config_schema](config_schema.md) - The type of config this Runnable accepts specified as a Pydantic model.
- [config_specs](config_specs.md) - List configurable fields for this Runnable.
- [get_config_jsonschema](get_config_jsonschema.md) - Get a JSON schema that represents the config of the Runnable.
- [get_graph](get_graph.md) - Return a graph representation of this Runnable.
- [get_input_jsonschema](get_input_jsonschema.md) - Get a JSON schema that represents the input to the Runnable.
- [get_input_schema](get_input_schema.md) - Get a Pydantic model that can be used to validate input to the Runnable.
- [get_name](get_name.md) - Get the name of the Runnable.
- [get_output_jsonschema](get_output_jsonschema.md) - Get a JSON schema that represents the output of the Runnable.
- [get_output_schema](get_output_schema.md) - Get a Pydantic model that can be used to validate output to the Runnable.
- [get_prompts](get_prompts.md) - Return a list of prompts used by this Runnable.
- [input_schema](input_schema.md) - The type of input this Runnable accepts specified as a Pydantic model.
- [invoke](invoke.md) - Transform a single input into an output.
- [map](map.md) - Return a new Runnable that maps a list of inputs to a list of outputs.
- [name](name.md) - The name of the Runnable. Used for debugging and tracing.
- [output_schema](output_schema.md) - Output schema.
- [pick](pick.md) - Pick keys from the output dict of this Runnable.
- [pipe](pipe.md) - Pipe Runnable objects.
- [stream](stream.md) - Default implementation of stream, which calls invoke.
- [stream_events](stream_events.md) - Generate a stream of events synchronously.
- [transform](transform.md) - Transform inputs to outputs.
- [with_alisteners](with_alisteners.md) - Bind async lifecycle listeners to a Runnable.
- [with_config](with_config.md) - Bind config to a Runnable, returning a new Runnable.
- [with_fallbacks](with_fallbacks.md) - Add fallbacks to a Runnable, returning a new Runnable.
- [with_listeners](with_listeners.md) - Bind lifecycle listeners to a Runnable, returning a new Runnable.
- [with_retry](with_retry.md) - Create a new Runnable that retries the original Runnable on exceptions.
- [with_types](with_types.md) - Bind input and output types to a Runnable, returning a new Runnable.
