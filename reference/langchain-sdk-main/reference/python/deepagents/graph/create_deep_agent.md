---
title: "create_deep_agent"
description: "Create a deep agent."
source: "https://reference.langchain.com/python/deepagents/graph/create_deep_agent"
category: "reference"
tags: [reference, deepagents, graph, create_deep_agent]
---

# create_deep_agent

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/graph/create_deep_agent)

Create a deep agent.

By default, this agent has access to the following tools:

- `ls`, `read_file`, `write_file`, `edit_file`, `glob`, `grep`: file operations
- `execute`: run shell commands
- `task`: call subagents

The `execute` tool allows running shell commands if the backend implements
[`SandboxBackendProtocol`][deepagents.backends.protocol.SandboxBackendProtocol].
For non-sandbox backends, the `execute` tool will return an error message.

## Signature

```python
create_deep_agent(
    model: str | BaseChatModel | None = None,
    tools: Sequence[BaseTool | Callable | dict[str, Any]] | None = None,
    *,
    system_prompt: str | SystemMessage | None = None,
    middleware: Sequence[AgentMiddleware[StateT_co, ContextT]] = (),
    subagents: Sequence[SubAgent | CompiledSubAgent | AsyncSubAgent] | None = None,
    skills: list[str] | None = None,
    memory: list[str] | None = None,
    permissions: list[FilesystemPermission] | None = None,
    backend: BackendProtocol | None = None,
    interrupt_on: dict[str, bool | InterruptOnConfig] | None = None,
    response_format: ResponseFormat[ResponseT] | type[ResponseT] | dict[str, Any] | None = None,
    state_schema: type[DeepAgentState] | None = None,
    context_schema: type[ContextT] | None = None,
    checkpointer: Checkpointer | None = None,
    store: BaseStore | None = None,
    debug: bool = False,
    name: str | None = None,
    cache: BaseCache | None = None,
) -> CompiledStateGraph[AgentState[ResponseT], ContextT, InputAgentState, OutputAgentState[ResponseT]]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `model` | `str \| BaseChatModel \| None` | No | The model to use.  !!! deprecated      Specify a model explicitly.      Passing `model=None` (relying on the default     `claude-sonnet-4-6`) is deprecated since `0.5.3` and will     be removed in `deepagents==1.0.0`. The parameter type     will change from `BaseChatModel \| str \| None` to     `BaseChatModel \| str`. See     [Models](../../../../deepagents/models.md).  Accepts a `provider:model` string (e.g., `openai:gpt-5.5`); see [`init_chat_model`][langchain.chat_models.init_chat_model(model_provider)] for supported values. You can also pass a pre-initialized [`BaseChatModel`][langchain.chat_models.BaseChatModel] instance directly.  !!! note "OpenAI Models and Data Retention"      If an `openai:` model is used, the agent will use the OpenAI     Responses API by default. To use OpenAI chat completions     instead, initialize the model with     `init_chat_model("openai:...", use_responses_api=False)` and     pass the initialized model instance here.      To disable data retention with the Responses API, use     `init_chat_model("openai:...", use_responses_api=True, store=False, include=["reasoning.encrypted_content"])`     and pass the initialized model instance here. (default: `None`) |
| `tools` | `Sequence[BaseTool \| Callable \| dict[str, Any]] \| None` | No | Additional tools the agent should have access to.  These are merged with the built-in tool suite listed above (filesystem tools, `execute`, and `task`).  Passing tools here is additive — it never removes a built-in. To stop offering a built-in tool to the model, register a [`HarnessProfile`][deepagents.HarnessProfile] with `excluded_tools`. To remove one entirely, pass your own [`FilesystemMiddleware`][deepagents.middleware.filesystem.FilesystemMiddleware] with `tools=[...]`. (default: `None`) |
| `system_prompt` | `str \| SystemMessage \| None` | No | Caller-authored system instructions (`USER`) placed first in the system prompt sent to the model.  The final authored prompt is assembled as `USER` -> `BASE` -> `SUFFIX`. `BASE` is empty unless the active [`HarnessProfile`][deepagents.HarnessProfile] defines `base_system_prompt`, and `SUFFIX` is the profile's optional `system_prompt_suffix`. Parts are separated by blank lines.  With `system_prompt=None` and no profile `base_system_prompt` or `system_prompt_suffix`, the model receives an empty authored system prompt.  Passing a `SystemMessage` preserves any `cache_control` markers on its existing content blocks — useful for explicit Anthropic prompt-cache breakpoints. When profile content is present, its assembled `BASE` and `SUFFIX` are appended as an additional text content block after the caller's blocks.  See [Prompt assembly](https://docs.langchain.com/oss/deepagents/customization#prompt-assembly) for the full case-by-case breakdown. (default: `None`) |
| `middleware` | `Sequence[AgentMiddleware[StateT_co, ContextT]]` | No | Additional middleware to apply after the base stack but before the tail middleware. The full ordering is:  Base stack:  - [`SkillsMiddleware`][deepagents.middleware.skills.SkillsMiddleware] (if `skills` is provided) - [`FilesystemMiddleware`][deepagents.middleware.filesystem.FilesystemMiddleware] - [`SubAgentMiddleware`][deepagents.middleware.subagents.SubAgentMiddleware]     (if any inline subagents — declarative     [`SubAgent`][deepagents.middleware.subagents.SubAgent] or     [`CompiledSubAgent`][deepagents.middleware.subagents.CompiledSubAgent]     — are available) - [`SummarizationMiddleware`][langchain.agents.middleware.SummarizationMiddleware] - [`PatchToolCallsMiddleware`][deepagents.middleware.patch_tool_calls.PatchToolCallsMiddleware] - [`AsyncSubAgentMiddleware`][deepagents.middleware.async_subagents.AsyncSubAgentMiddleware] (if async `subagents` are provided)  *User middleware is inserted here.*  Tail stack:  - Harness profile `extra_middleware` (if any) - `_ToolExclusionMiddleware` (if profile has `excluded_tools`) - [`AnthropicPromptCachingMiddleware`][langchain_anthropic.middleware.AnthropicPromptCachingMiddleware] (unconditional; no-ops for     non-Anthropic models) - [`BedrockPromptCachingMiddleware`](https://reference.langchain.com/python/langchain-aws/middleware/prompt_caching/BedrockPromptCachingMiddleware)     when `langchain-aws` is installed (no-ops for non-Bedrock models) - [`FireworksPromptCachingMiddleware`](https://reference.langchain.com/python/integrations/langchain_fireworks/middleware/prompt_caching/FireworksPromptCachingMiddleware)     when `langchain-fireworks` is installed (no-ops for non-Fireworks models) - [`MemoryMiddleware`][deepagents.middleware.memory.MemoryMiddleware] (if `memory` is provided) - [`HumanInTheLoopMiddleware`][langchain.agents.middleware.HumanInTheLoopMiddleware] (if `interrupt_on` is provided)  After assembly, any entries in the profile's `excluded_middleware` are filtered from the final stack. Class entries match exact type; string entries match `AgentMiddleware.name` exactly (e.g. `"SummarizationMiddleware"` drops the summarization middleware via its public alias). Entries that match nothing in the assembled stack raise `ValueError`, as does excluding any class in the harness's protected scaffolding set (e.g., [`FilesystemMiddleware`][deepagents.middleware.filesystem.FilesystemMiddleware] or [`SubAgentMiddleware`][deepagents.middleware.subagents.SubAgentMiddleware]).  To run without the `task` tool, set `general_purpose_subagent=GeneralPurposeSubagentProfile(enabled=False)` on the active harness profile and pass no synchronous subagents via `subagents=`. Async subagents are unaffected. (default: `()`) |
| `subagents` | `Sequence[SubAgent \| CompiledSubAgent \| AsyncSubAgent] \| None` | No | Subagent specs available to the main agent.  This collection supports three forms:  - [`SubAgent`][deepagents.middleware.subagents.SubAgent]: A declarative synchronous subagent spec. - [`CompiledSubAgent`][deepagents.middleware.subagents.CompiledSubAgent]: A pre-compiled runnable subagent. - [`AsyncSubAgent`][deepagents.middleware.async_subagents.AsyncSubAgent]: A remote/background subagent spec.  `SubAgent` entries are invoked through the `task` tool. They should provide `name` and `description`, and may also override `system_prompt`, `tools`, `model`, `middleware`, `interrupt_on`, `skills`, `permissions`, and `response_format`. See `interrupt_on` below for inheritance and override behavior.  Setting `mode="fork"` on a `SubAgent` is experimental. A fork continues the parent's conversation and rebuilds its system prompt instead of starting isolated; any `system_prompt` of its own is appended to the inherited one, and it cannot define `skills`.  `CompiledSubAgent` entries are also exposed through the `task` tool, but provide a pre-built `runnable` instead of a declarative prompt and tool configuration.  `AsyncSubAgent` entries are identified by their async-subagent fields (`graph_id`, and optionally `url`/`headers`) and are routed into `AsyncSubAgentMiddleware` instead of `SubAgentMiddleware`. They should provide `name`, `description`, and `graph_id`, and may optionally include `url` and `headers`. These subagents run as background tasks and expose the async subagent tools for launching, checking, updating, cancelling, and listing tasks.  If no subagent named `general-purpose` is provided, a default general-purpose synchronous subagent is added automatically unless the active harness profile disables it. With no synchronous subagents in play — none passed and the default disabled via `general_purpose_subagent=GeneralPurposeSubagentProfile(enabled=False)` — the `task` tool is not exposed. Async subagents are independent. (default: `None`) |
| `skills` | `list[str] \| None` | No | List of skill source paths (e.g., `["/skills/user/", "/skills/project/"]`).  Paths must be specified using POSIX conventions (forward slashes) and are relative to the backend's root. When using `StateBackend` (default), provide skill files via `invoke(files={...})`. With `FilesystemBackend`, skills are loaded from disk relative to the backend's `root_dir`. Later sources override earlier ones for skills with the same name (last one wins). (default: `None`) |
| `memory` | `list[str] \| None` | No | List of memory file paths (`AGENTS.md` files) to load (e.g., `["/memory/AGENTS.md"]`).  Display names are automatically derived from paths.  Memory is loaded at agent startup and added into the system prompt. (default: `None`) |
| `permissions` | `list[FilesystemPermission] \| None` | No | List of `FilesystemPermission` rules for the main agent and its subagents.  Rules are evaluated in declaration order; the first match wins. If no rule matches, the call is allowed.  Each rule's `mode` can be:  - `"allow"` (default): the call proceeds. - `"deny"`: the tool returns a permission-denied error. - `"interrupt"`: the call pauses for human approval via     `HumanInTheLoopMiddleware`. A `HumanInTheLoopMiddleware` is     auto-installed when any interrupt-mode rule is present, and the     generated `interrupt_on` entries are merged with the     `interrupt_on` argument below (user-supplied entries win per     tool name). Requires a `langchain` version that supports the     `when` predicate on `InterruptOnConfig`.  Subagents inherit these rules unless they specify their own `permissions` field, which replaces the parent's rules entirely.  `FilesystemMiddleware` applies these permissions at the tool level for its built-in filesystem tools, not at the backend level. Direct backend usage does not currently incorporate `permissions`. (default: `None`) |
| `backend` | `BackendProtocol \| None` | No | Optional backend for file storage and execution.  Pass a `Backend` instance (e.g. `StateBackend()`).  For execution support, use a backend that implements [`SandboxBackendProtocol`][deepagents.backends.protocol.SandboxBackendProtocol]. (default: `None`) |
| `interrupt_on` | `dict[str, bool \| InterruptOnConfig] \| None` | No | Mapping of tool names to interrupt configs.  Pass to pause agent execution at specified tool calls for human approval or modification.  This config always applies to the main agent.  For subagents: - Declarative `SubAgent` specs inherit the top-level `interrupt_on`     config by default. - If a declarative `SubAgent` provides its own `interrupt_on`, that     subagent-specific config overrides the inherited     top-level config. - `CompiledSubAgent` runnables do not inherit top-level     `interrupt_on`; configure human-in-the-loop behavior inside the     compiled runnable itself. - Remote `AsyncSubAgent` specs do not inherit top-level     `interrupt_on`; configure any approval behavior on the remote     subagent itself.  For example, `interrupt_on={"edit_file": True}` pauses before every edit. (default: `None`) |
| `response_format` | `ResponseFormat[ResponseT] \| type[ResponseT] \| dict[str, Any] \| None` | No | A structured output response format to use for the agent. (default: `None`) |
| `state_schema` | `type[DeepAgentState] \| None` | No | Custom state schema for the agent graph. Must be a `TypedDict` subclass of [`DeepAgentState`][deepagents.graph.DeepAgentState] so the built-in `DeltaChannel` reducer on `messages` is preserved.  Generally, prefer defining state extensions with middleware so the extra fields stay scoped to the hooks and tools that use them.  When provided, this schema is used as the base graph schema and is merged with state schemas contributed by middleware. It is also forwarded when compiling declarative [`SubAgent`][deepagents.middleware.subagents.SubAgent] specs for the `task` tool, so subagents see the same custom fields as the parent.  [`CompiledSubAgent`][deepagents.middleware.subagents.CompiledSubAgent] runnables do not inherit this schema because they are already compiled — compile those runnables with a compatible state schema if they need access to the same custom state fields. Remote [`AsyncSubAgent`][deepagents.middleware.async_subagents.AsyncSubAgent] specs likewise use the schema configured on the remote graph.  ```python from deepagents.graph import DeepAgentState   class MyState(DeepAgentState):     page_url: str     file_urls: list[str]   agent = create_deep_agent(model=..., state_schema=MyState) ``` (default: `None`) |
| `context_schema` | `type[ContextT] \| None` | No | Schema class that defines immutable run-scoped context.  Passed through to [`create_agent`][langchain.agents.create_agent]. (default: `None`) |
| `checkpointer` | `Checkpointer \| None` | No | Optional `Checkpointer` for persisting agent state between runs.  Passed through to [`create_agent`][langchain.agents.create_agent]. (default: `None`) |
| `store` | `BaseStore \| None` | No | Optional store for persistent storage (required if backend uses `StoreBackend`).  Passed through to [`create_agent`][langchain.agents.create_agent]. (default: `None`) |
| `debug` | `bool` | No | Whether to enable debug mode.  Passed through to [`create_agent`][langchain.agents.create_agent]. (default: `False`) |
| `name` | `str \| None` | No | The name of the agent.  Passed through to [`create_agent`][langchain.agents.create_agent]. (default: `None`) |
| `cache` | `BaseCache \| None` | No | The cache to use for the agent.  Passed through to [`create_agent`][langchain.agents.create_agent]. (default: `None`) |

## Returns

`CompiledStateGraph[AgentState[ResponseT], ContextT, InputAgentState, OutputAgentState[ResponseT]]`

A configured deep agent.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/graph.py#L271)
