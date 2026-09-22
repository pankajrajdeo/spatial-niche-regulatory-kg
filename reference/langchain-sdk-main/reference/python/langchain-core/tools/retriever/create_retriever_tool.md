---
title: "create_retriever_tool"
description: "Create a tool to do retrieval of documents."
source: "https://reference.langchain.com/python/langchain-core/tools/retriever/create_retriever_tool"
category: "reference"
tags: [reference, langchain-core, tools, retriever, create_retriever_tool]
---

# create_retriever_tool

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tools/retriever/create_retriever_tool)

Create a tool to do retrieval of documents.

## Signature

```python
create_retriever_tool(
    retriever: BaseRetriever,
    name: str,
    description: str,
    *,
    document_prompt: BasePromptTemplate[str] | None = None,
    document_separator: str = '\n\n',
    response_format: Literal['content', 'content_and_artifact'] = 'content',
) -> StructuredTool
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `retriever` | `BaseRetriever` | Yes | The retriever to use for the retrieval |
| `name` | `str` | Yes | The name for the tool.  This will be passed to the language model, so should be unique and somewhat descriptive. |
| `description` | `str` | Yes | The description for the tool.  This will be passed to the language model, so should be descriptive. |
| `document_prompt` | `BasePromptTemplate[str] \| None` | No | The prompt to use for the document. (default: `None`) |
| `document_separator` | `str` | No | The separator to use between documents. (default: `'\n\n'`) |
| `response_format` | `Literal['content', 'content_and_artifact']` | No | The tool response format.  If `'content'` then the output of the tool is interpreted as the contents of a `ToolMessage`. If `'content_and_artifact'` then the output is expected to be a two-tuple corresponding to the `(content, artifact)` of a `ToolMessage` (artifact being a list of documents in this case). (default: `'content'`) |

## Returns

`StructuredTool`

Tool class to pass to an agent.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/tools/retriever.py#L31)
