---
title: "main"
description: "- CACHE_NS_WRITES - CONF - CONFIG_KEY_CACHE - CONFIG_KEY_CHECKPOINT_ID - CONFIG_KEY_CHECKPOINT_NS - CONFIG_KEY_CHECKPOINTER - CONFIG_KEY_DURABILITY - CONFIG_KEY_NODE_FINISHED - CONFIG_KEY_READ -..."
source: "https://reference.langchain.com/python/langgraph/pregel/main"
category: "reference"
tags: [reference, langgraph, pregel, main]
---

# main

> **Module** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/main)

## Properties

- `CACHE_NS_WRITES`
- `CONF`
- `CONFIG_KEY_CACHE`
- `CONFIG_KEY_CHECKPOINT_ID`
- `CONFIG_KEY_CHECKPOINT_NS`
- `CONFIG_KEY_CHECKPOINTER`
- `CONFIG_KEY_DURABILITY`
- `CONFIG_KEY_NODE_FINISHED`
- `CONFIG_KEY_READ`
- `CONFIG_KEY_RUNNER_SUBMIT`
- `CONFIG_KEY_RUNTIME`
- `CONFIG_KEY_SEND`
- `CONFIG_KEY_STREAM`
- `CONFIG_KEY_STREAM_MESSAGES_V2`
- `CONFIG_KEY_TASK_ID`
- `CONFIG_KEY_THREAD_ID`
- `ERROR`
- `INPUT`
- `INTERRUPT`
- `NS_END`
- `NS_SEP`
- `NULL_TASK_ID`
- `PUSH`
- `TASKS`
- `MISSING`
- `END`
- `ManagedValueSpec`
- `DEFAULT_BOUND`
- `StreamChunk`
- `DEFAULT_RUNTIME`
- `All`
- `Durability`
- `StreamMode`
- `StreamPart`
- `ContextT`
- `InputT`
- `OutputT`
- `StateT`

## Methods

- [`ensure_config()`](https://reference.langchain.com/python/langgraph/pregel/main/ensure_config)
- [`merge_configs()`](https://reference.langchain.com/python/langgraph/pregel/main/merge_configs)
- [`patch_checkpoint_map()`](https://reference.langchain.com/python/langgraph/pregel/main/patch_checkpoint_map)
- [`patch_config()`](https://reference.langchain.com/python/langgraph/pregel/main/patch_config)
- [`patch_configurable()`](https://reference.langchain.com/python/langgraph/pregel/main/patch_configurable)
- [`recast_checkpoint_ns()`](https://reference.langchain.com/python/langgraph/pregel/main/recast_checkpoint_ns)
- [`create_model()`](https://reference.langchain.com/python/langgraph/pregel/main/create_model)
- [`coerce_to_runnable()`](https://reference.langchain.com/python/langgraph/pregel/main/coerce_to_runnable)
- [`coerce_timeout_policy()`](https://reference.langchain.com/python/langgraph/pregel/main/coerce_timeout_policy)
- [`get_async_graph_callback_manager_for_config()`](https://reference.langchain.com/python/langgraph/pregel/main/get_async_graph_callback_manager_for_config)
- [`get_sync_graph_callback_manager_for_config()`](https://reference.langchain.com/python/langgraph/pregel/main/get_sync_graph_callback_manager_for_config)
- [`get_config()`](https://reference.langchain.com/python/langgraph/pregel/main/get_config)
- [`create_error_message()`](https://reference.langchain.com/python/langgraph/pregel/main/create_error_message)
- [`apply_writes()`](https://reference.langchain.com/python/langgraph/pregel/main/apply_writes)
- [`local_read()`](https://reference.langchain.com/python/langgraph/pregel/main/local_read)
- [`prepare_next_tasks()`](https://reference.langchain.com/python/langgraph/pregel/main/prepare_next_tasks)
- [`identifier()`](https://reference.langchain.com/python/langgraph/pregel/main/identifier)
- [`achannels_from_checkpoint()`](https://reference.langchain.com/python/langgraph/pregel/main/achannels_from_checkpoint)
- [`channels_from_checkpoint()`](https://reference.langchain.com/python/langgraph/pregel/main/channels_from_checkpoint)
- [`copy_checkpoint()`](https://reference.langchain.com/python/langgraph/pregel/main/copy_checkpoint)
- [`create_checkpoint()`](https://reference.langchain.com/python/langgraph/pregel/main/create_checkpoint)
- [`create_checkpoint_plan_for_update_state_api()`](https://reference.langchain.com/python/langgraph/pregel/main/create_checkpoint_plan_for_update_state_api)
- [`empty_checkpoint()`](https://reference.langchain.com/python/langgraph/pregel/main/empty_checkpoint)
- [`get_updated_channels_from_tasks()`](https://reference.langchain.com/python/langgraph/pregel/main/get_updated_channels_from_tasks)
- [`draw_graph()`](https://reference.langchain.com/python/langgraph/pregel/main/draw_graph)
- [`map_input()`](https://reference.langchain.com/python/langgraph/pregel/main/map_input)
- [`read_channels()`](https://reference.langchain.com/python/langgraph/pregel/main/read_channels)
- [`get_new_channel_versions()`](https://reference.langchain.com/python/langgraph/pregel/main/get_new_channel_versions)
- [`validate_timeout_supported()`](https://reference.langchain.com/python/langgraph/pregel/main/validate_timeout_supported)
- [`validate_graph()`](https://reference.langchain.com/python/langgraph/pregel/main/validate_graph)
- [`validate_keys()`](https://reference.langchain.com/python/langgraph/pregel/main/validate_keys)
- [`get_bolded_text()`](https://reference.langchain.com/python/langgraph/pregel/main/get_bolded_text)
- [`get_colored_text()`](https://reference.langchain.com/python/langgraph/pregel/main/get_colored_text)
- [`tasks_w_writes()`](https://reference.langchain.com/python/langgraph/pregel/main/tasks_w_writes)
- [`ensure_valid_checkpointer()`](https://reference.langchain.com/python/langgraph/pregel/main/ensure_valid_checkpointer)

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/pregel/main.py)
