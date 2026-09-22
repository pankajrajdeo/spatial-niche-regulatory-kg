---
title: "LangSmithLoader"
description: "Load LangSmith Dataset examples as Document objects."
source: "https://reference.langchain.com/python/langchain-core/document_loaders/langsmith/LangSmithLoader"
category: "reference"
tags: [reference, langchain-core, document_loaders, langsmith, langsmithloader]
---

# LangSmithLoader

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/document_loaders/langsmith/LangSmithLoader)

Load LangSmith Dataset examples as `Document` objects.

Loads the example inputs as the `Document` page content and places the entire
example into the `Document` metadata. This allows you to easily create few-shot
example retrievers from the loaded documents.

??? example "Lazy loading"

```python
    from langchain_core.document_loaders import LangSmithLoader

    loader = LangSmithLoader(dataset_id="...", limit=100)
    docs = []
    for doc in loader.lazy_load():
        docs.append(doc)
```

```python
    # -> [Document("...", metadata={"inputs": {...}, "outputs": {...}, ...}), ...]
```

## Signature

```python
LangSmithLoader(
    self,
    *,
    dataset_id: uuid.UUID | str | None = None,
    dataset_name: str | None = None,
    example_ids: Sequence[uuid.UUID | str] | None = None,
    as_of: datetime.datetime | str | None = None,
    splits: Sequence[str] | None = None,
    inline_s3_urls: bool = True,
    offset: int = 0,
    limit: int | None = None,
    metadata: dict[str, Any] | None = None,
    filter: str | None = None,
    content_key: str = '',
    format_content: Callable[..., str] | None = None,
    client: LangSmithClient | None = None,
    **client_kwargs: Any = {},
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `dataset_id` | `uuid.UUID \| str \| None` | No | The ID of the dataset to filter by. (default: `None`) |
| `dataset_name` | `str \| None` | No | The name of the dataset to filter by. (default: `None`) |
| `content_key` | `str` | No | The inputs key to set as `Document` page content.  `'.'` characters are interpreted as nested keys, e.g. `content_key="first.second"` will result in `Document(page_content=format_content(example.inputs["first"]["second"]))` (default: `''`) |
| `format_content` | `Callable[..., str] \| None` | No | Function for converting the content extracted from the example inputs into a string.  Defaults to JSON-encoding the contents. (default: `None`) |
| `example_ids` | `Sequence[uuid.UUID \| str] \| None` | No | The IDs of the examples to filter by. (default: `None`) |
| `as_of` | `datetime.datetime \| str \| None` | No | The dataset version tag or timestamp to retrieve the examples as of.  Response examples will only be those that were present at the time of the tagged (or timestamped) version. (default: `None`) |
| `splits` | `Sequence[str] \| None` | No | A list of dataset splits, which are divisions of your dataset such as `train`, `test`, or `validation`.  Returns examples only from the specified splits. (default: `None`) |
| `inline_s3_urls` | `bool` | No | Whether to inline S3 URLs. (default: `True`) |
| `offset` | `int` | No | The offset to start from. (default: `0`) |
| `limit` | `int \| None` | No | The maximum number of examples to return. (default: `None`) |
| `metadata` | `dict[str, Any] \| None` | No | Metadata to filter by. (default: `None`) |
| `filter` | `str \| None` | No | A structured filter string to apply to the examples. (default: `None`) |
| `client` | `LangSmithClient \| None` | No | LangSmith Client.  If not provided will be initialized from below args. (default: `None`) |
| `client_kwargs` | `Any` | No | Keyword args to pass to LangSmith client init.  Should only be specified if `client` isn't. (default: `{}`) |

## Extends

- `BaseLoader`

## Constructors

```python
__init__(
    self,
    *,
    dataset_id: uuid.UUID | str | None = None,
    dataset_name: str | None = None,
    example_ids: Sequence[uuid.UUID | str] | None = None,
    as_of: datetime.datetime | str | None = None,
    splits: Sequence[str] | None = None,
    inline_s3_urls: bool = True,
    offset: int = 0,
    limit: int | None = None,
    metadata: dict[str, Any] | None = None,
    filter: str | None = None,
    content_key: str = '',
    format_content: Callable[..., str] | None = None,
    client: LangSmithClient | None = None,
    **client_kwargs: Any = {},
) -> None
```

| Name | Type |
|------|------|
| `dataset_id` | `uuid.UUID \| str \| None` |
| `dataset_name` | `str \| None` |
| `example_ids` | `Sequence[uuid.UUID \| str] \| None` |
| `as_of` | `datetime.datetime \| str \| None` |
| `splits` | `Sequence[str] \| None` |
| `inline_s3_urls` | `bool` |
| `offset` | `int` |
| `limit` | `int \| None` |
| `metadata` | `dict[str, Any] \| None` |
| `filter` | `str \| None` |
| `content_key` | `str` |
| `format_content` | `Callable[..., str] \| None` |
| `client` | `LangSmithClient \| None` |

## Properties

- `content_key`
- `format_content`
- `dataset_id`
- `dataset_name`
- `example_ids`
- `as_of`
- `splits`
- `inline_s3_urls`
- `offset`
- `limit`
- `metadata`
- `filter`

## Methods

- [`lazy_load()`](https://reference.langchain.com/python/langchain-core/document_loaders/langsmith/LangSmithLoader/lazy_load)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/document_loaders/langsmith.py#L17)
