---
title: "reference/python/langchain-core/exceptions"
description: "Index of 15 pages and 7 subdirectories under reference/python/langchain-core/exceptions."
category: "index"
tags: [index, reference, python, langchain-core, exceptions]
---

# reference/python/langchain-core/exceptions

15 pages here, 30 pages including subdirectories.

## Directories

- [ErrorCode/](ErrorCode/_index.md) - 7 pages
- [ModelAPIError/](ModelAPIError/_index.md) - 1 page
- [ModelConnectionError/](ModelConnectionError/_index.md) - 1 page
- [ModelError/](ModelError/_index.md) - 1 page
- [ModelRateLimitError/](ModelRateLimitError/_index.md) - 1 page
- [ModelTimeoutError/](ModelTimeoutError/_index.md) - 1 page
- [OutputParserException/](OutputParserException/_index.md) - 3 pages

## Files

- [ContextOverflowError](ContextOverflowError.md) - Exception raised when input exceeds the model's context limit.
- [ErrorCode](ErrorCode.md) - Error codes.
- [LangChainException](LangChainException.md) - General LangChain exception.
- [ModelAPIError](ModelAPIError.md) - Exception raised when a model provider reports a server failure (HTTP 5xx).
- [ModelAuthenticationError](ModelAuthenticationError.md) - Exception raised when model provider authentication fails (HTTP 401).
- [ModelConnectionError](ModelConnectionError.md) - Exception raised when a model provider cannot be reached.
- [ModelError](ModelError.md) - Base exception for failures related to model invocation.
- [ModelInvalidRequestError](ModelInvalidRequestError.md) - Exception raised when a provider rejects a request as invalid (e.g. HTTP 400).
- [ModelNotFoundError](ModelNotFoundError.md) - Exception raised when the requested model cannot be found (HTTP 404).
- [ModelPermissionDeniedError](ModelPermissionDeniedError.md) - Exception raised when credentials lack permission for a request (HTTP 403).
- [ModelRateLimitError](ModelRateLimitError.md) - Exception raised when a model provider rate limit is exceeded (HTTP 429).
- [ModelTimeoutError](ModelTimeoutError.md) - Exception raised when a model request times out.
- [OutputParserException](OutputParserException.md) - Exception that output parsers should raise to signify a parsing error.
- [TracerException](TracerException.md) - Base class for exceptions in tracers module.
- [create_message](create_message.md) - Create a message with a link to the LangChain troubleshooting guide.
