---
title: "Implement a LangChain integration"
description: "Integration packages are Python packages that users can install for use in their projects. They implement one or more components that adhere to the LangChain interface standards."
source: "https://docs.langchain.com/oss/python/contributing/implement-langchain"
category: "docs"
tags: [docs, contributing, implement-langchain]
---

# Implement a LangChain integration

Integration packages are Python packages that users can install for use in their projects. They implement one or more components that adhere to the LangChain interface standards.

LangChain components are subclasses of base classes in [`langchain-core`](https://github.com/langchain-ai/langchain/tree/master/libs/core). Examples include [chat models](../integrations/chat.md), [tools](../integrations/tools.md), [retrievers](../integrations/retrievers.md), and more.

Your integration package will typically implement a subclass of at least one of these components. Expand the tabs below to see details on each.

#### Chat Models
Chat models are subclasses of the [`BaseChatModel`](https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel) class. They implement methods for generating chat completions, handling message formatting, and managing model parameters.

> [!WARNING]
> The chat model integration guide is currently WIP. In the meantime, read the [chat model conceptual guide](../langchain/models.md) for details on how LangChain chat models function. You may also refer to existing integrations in the [LangChain repo](https://github.com/langchain-ai/langchain/tree/master/libs/partners)

#### Embeddings
Embedding models are subclasses of the [`Embeddings`](https://reference.langchain.com/python/langchain-core/embeddings/embeddings/Embeddings) class.

> [!WARNING]
> The embedding model integration guide is currently WIP. In the meantime, read the [embedding model conceptual guide](../integrations/embeddings.md) for details on how LangChain embedding models function.

#### Tools
Tools are used in 2 main ways:

1. To define an "input schema" or "args schema" to pass to a chat model's tool calling feature along with a text request, such that the chat model can generate a "tool call", or parameters to call the tool with.
2. To take a "tool call" as generated above, and take some action and return a response that can be passed back to the chat model as a ToolMessage.

The Tools class must inherit from the [`BaseTool`](https://reference.langchain.com/python/langchain-core/tools/base/BaseTool) base class. This interface has 3 properties and 2 methods that should be implemented in a subclass.

> [!WARNING]
> The tools integration guide is currently WIP. In the meantime, read the [tools conceptual guide](../langchain/tools.md) for details on how LangChain tools function.

#### Middleware
[Middleware](../langchain/middleware/overview.md) lets you customize agent behavior by hooking into model calls, tool calls, and agent lifecycle events. Middleware classes subclass the [`AgentMiddleware`](https://reference.langchain.com/python/langchain/agents/middleware/types/AgentMiddleware) base class.

Read the [custom middleware guide](../langchain/middleware/custom.md) to understand hooks, state updates, and middleware patterns before building an integration.

Middleware integrations typically fall into two categories:

| Type                  | Description                                | Examples                                                  |
| --------------------- | ------------------------------------------ | --------------------------------------------------------- |
| **Provider-specific** | Leverages a provider's unique capabilities | Prompt caching, native tool execution, content moderation |
| **Cross-provider**    | Works with any model or tool               | Rate limiting, PII detection, logging, guardrails         |

Provider-specific middleware lives in the provider's integration package (for example `langchain-anthropic`). Cross-provider middleware can be published as a standalone package.

You can also use these existing middleware integrations as reference:

#### [OpenAI content moderation](../integrations/middleware/openai.md)
Single middleware with configuration options and exit behaviors.

#### [Anthropic middleware](../integrations/middleware/anthropic.md)
Multiple middleware classes for prompt caching, tools, memory, and file search.

#### [AWS prompt caching](../integrations/middleware/aws.md)
Provider-specific prompt caching with model behavior tables.

#### [Custom middleware guide](../langchain/middleware/custom.md)
Full reference for hooks, state updates, and patterns.

#### Checkpointers
Checkpointers enable [persistence](../langgraph/persistence.md) in LangGraph, allowing agents to save and resume state across interactions.

See existing checkpointer integrations in the [LangGraph repo](https://github.com/langchain-ai/langgraph/tree/main/libs) for implementation examples.

#### Sandboxes
Sandbox integrations enable [Deep Agents](../deepagents/overview.md) to run code in isolated environments.

Implement the [`SandboxBackendProtocol`](https://reference.langchain.com/python/deepagents/backends/protocol/SandboxBackendProtocol) from Deep Agents. This protocol includes `execute()`, async variants, and the filesystem tool methods such as `ls`, `read`, `write`, `edit`, `glob`, and `grep`.

In practice, if your sandbox environment can run shell commands and has `python3` available, you should usually subclass [`BaseSandbox`](https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox). `BaseSandbox` provides the filesystem operations through `python3`, so you mainly need to implement `execute()`, `upload_files()`, `download_files()`, and `id`.

**Example BaseSandbox scaffold**

```python
from __future__ import annotations

from deepagents.backends.protocol import (
    ExecuteResponse,
    FileDownloadResponse,
    FileUploadResponse,
)
from deepagents.backends.sandbox import BaseSandbox  # [!code highlight]

class MySandbox(BaseSandbox):
    def __init__(self, client: MySandboxSdkClient) -> None:
        self._client = client

    @property
    def id(self) -> str:
        return self._client.sandbox_id

    def execute(
        self,
        command: str,
        *,
        timeout: int | None = None,
    ) -> ExecuteResponse:
        # Execute `command` in your sandbox and map the provider response
        # into ExecuteResponse.
        result = self._client.run(command=command, timeout=timeout)
        output = result.stdout or ""
        if result.stderr:
            output += f"\n<stderr>{result.stderr}</stderr>"
        return ExecuteResponse(
            output=output,
            exit_code=result.exit_code,
            truncated=False,
        )

    def upload_files(
        self,
        files: list[tuple[str, bytes]],
    ) -> list[FileUploadResponse]:
        # Validate paths, batch requests where possible, and map provider
        # results back into FileUploadResponse objects in input order.
        # Only catch and normalize errors that an LLM can plausibly retry
        # or fix, such as invalid_path or file_not_found.
        return self._client.upload_files(files)

    def download_files(self, paths: list[str]) -> list[FileDownloadResponse]:
        # Validate paths, batch requests where possible, and map provider
        # results back into FileDownloadResponse objects in input order.
        # Only catch and normalize errors that an LLM can plausibly retry
        # or fix, such as invalid_path or file_not_found.
        return self._client.download_files(paths)

    async def aexecute(
        self,
        command: str,
        *,
        timeout: int | None = None,
    ) -> ExecuteResponse:
        ...

    async def aupload_files(
        self,
        files: list[tuple[str, bytes]],
    ) -> list[FileUploadResponse]:
        ...

    async def adownload_files(
        self,
        paths: list[str],
    ) -> list[FileDownloadResponse]:
        ...
```

## Test your integration

Validate your integration with the [sandbox standard test suite](standard-tests-langchain.md#sandbox-integrations). The Python suite uses `SandboxIntegrationTests` from `langchain_tests.integration_tests`; subclass it and provide a `sandbox` fixture that yields a clean `SandboxBackendProtocol` instance.

**Example sandbox standard test setup**

```python
from __future__ import annotations

from collections.abc import Iterator

import pytest
from deepagents.backends.protocol import SandboxBackendProtocol
from langchain_tests.integration_tests import SandboxIntegrationTests

from langchain_myprovider import MySandbox
from myprovider_sdk import MySandboxSdkClient

class TestMySandboxStandard(SandboxIntegrationTests):
    @pytest.fixture(scope="class")
    def sandbox(self) -> Iterator[SandboxBackendProtocol]:
        client = MySandboxSdkClient()
        backend = MySandbox(client=client)
        try:
            yield backend
        finally:
            # Replace this with your provider's cleanup logic.
            client.delete_sandbox(backend.id)
```

Put this in a file such as `tests/integration_tests/test_sandbox.py`. The standard suite will handle the actual filesystem and command-execution assertions for you.

**Reference implementation:** See the [Daytona partner integration](https://github.com/langchain-ai/deepagents/tree/main/libs/partners/daytona), which subclasses `BaseSandbox` and implements `execute()`, `upload_files()`, `download_files()`, and `id`.

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/contributing/implement-langchain.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
