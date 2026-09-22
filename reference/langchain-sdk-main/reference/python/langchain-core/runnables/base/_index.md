---
title: "reference/python/langchain-core/runnables/base"
description: "Index of 42 pages and 10 subdirectories under reference/python/langchain-core/runnables/base."
category: "index"
tags: [index, reference, python, langchain-core, runnables, base]
---

# reference/python/langchain-core/runnables/base

42 pages here, 202 pages including subdirectories.

## Directories

- [Runnable/](Runnable/_index.md) - 40 pages
- [RunnableBinding/](RunnableBinding/_index.md) - 5 pages
- [RunnableBindingBase/](RunnableBindingBase/_index.md) - 28 pages
- [RunnableEach/](RunnableEach/_index.md) - 5 pages
- [RunnableEachBase/](RunnableEachBase/_index.md) - 13 pages
- [RunnableGenerator/](RunnableGenerator/_index.md) - 11 pages
- [RunnableLambda/](RunnableLambda/_index.md) - 16 pages
- [RunnableParallel/](RunnableParallel/_index.md) - 16 pages
- [RunnableSequence/](RunnableSequence/_index.md) - 21 pages
- [RunnableSerializable/](RunnableSerializable/_index.md) - 5 pages

## Files

- [Other](Other.md) - View source on GitHub
- [Runnable](Runnable.md) - A unit of work that can be invoked, batched, streamed, transformed and composed.
- [RunnableBinding](RunnableBinding.md) - Wrap a Runnable with additional functionality.
- [RunnableBindingBase](RunnableBindingBase.md) - Runnable that delegates calls to another Runnable with a set of kwargs.
- [RunnableEach](RunnableEach.md) - RunnableEach class.
- [RunnableEachBase](RunnableEachBase.md) - RunnableEachBase class.
- [RunnableGenerator](RunnableGenerator.md) - Runnable that runs a generator function.
- [RunnableLambda](RunnableLambda.md) - RunnableLambda converts a python callable into a Runnable.
- [RunnableLike](RunnableLike.md) - Type Alias in langchain_core
- [RunnableMap](RunnableMap.md) - View source on GitHub
- [RunnableParallel](RunnableParallel.md) - Runnable that runs a mapping of Runnables in parallel.
- [RunnableSequence](RunnableSequence.md) - Sequence of Runnable objects, where the output of one is the input of the next.
- [RunnableSerializable](RunnableSerializable.md) - Runnable that can be serialized to JSON.
- [acall_func_with_variable_args](acall_func_with_variable_args.md) - Async call function that may optionally accept a run_manager and/or config.
- [accepts_config](accepts_config.md) - Check if a callable accepts a config argument.
- [accepts_run_manager](accepts_run_manager.md) - Check if a callable accepts a run_manager argument.
- [call_func_with_variable_args](call_func_with_variable_args.md) - Call function that may optionally accept a run_manager and/or config.
- [chain](chain.md) - Decorate a function to make it a Runnable.
- [coerce_to_runnable](coerce_to_runnable.md) - Coerce a Runnable-like object into a Runnable.
- [coro_with_context](coro_with_context.md) - Await a coroutine with a context.
- [create_model_v2](create_model_v2.md) - Create a Pydantic model with the given field definitions.
- [ensure_config](ensure_config.md) - Ensure that a config is a dict with all keys present.
- [gated_coro](gated_coro.md) - Run a coroutine with a semaphore.
- [gather_with_concurrency](gather_with_concurrency.md) - Gather coroutines with a limit on the number of concurrent coroutines.
- [get_async_callback_manager_for_config](get_async_callback_manager_for_config.md) - Get an async callback manager for a config.
- [get_callback_manager_for_config](get_callback_manager_for_config.md) - Get a callback manager for a config.
- [get_config_list](get_config_list.md) - Get a list of configs from a single config or a list of configs.
- [get_executor_for_config](get_executor_for_config.md) - Get an executor for a config.
- [get_fields](get_fields.md) - Return the field names of a Pydantic model.
- [get_function_first_arg_dict_keys](get_function_first_arg_dict_keys.md) - Get the keys of the first argument of a function if it is a dict.
- [get_function_nonlocals](get_function_nonlocals.md) - Get the nonlocal variables accessed by a function.
- [get_lambda_source](get_lambda_source.md) - Get the source code of a lambda function.
- [get_unique_config_specs](get_unique_config_specs.md) - Get the unique config specs from a sequence of config specs.
- [indent_lines_after_first](indent_lines_after_first.md) - Indent all lines of text after the first line.
- [is_async_callable](is_async_callable.md) - Check if a function is async.
- [is_async_generator](is_async_generator.md) - Check if a function is an async generator.
- [merge_configs](merge_configs.md) - Merge multiple configs into one.
- [model_json_schema](model_json_schema.md) - Return the JSON schema of a Pydantic model class of either major version.
- [patch_config](patch_config.md) - Patch a config with new values.
- [run_in_executor](run_in_executor.md) - Run a function in an executor.
- [set_config_context](set_config_context.md) - Set the child Runnable config + tracing context.
- [warn_deprecated](warn_deprecated.md) - Display a standardized deprecation.
