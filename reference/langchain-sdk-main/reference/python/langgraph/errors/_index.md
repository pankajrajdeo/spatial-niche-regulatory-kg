---
title: "reference/python/langgraph/errors"
description: "Index of 14 pages and 6 subdirectories under reference/python/langgraph/errors."
category: "index"
tags: [index, reference, python, langgraph, errors]
---

# reference/python/langgraph/errors

14 pages here, 30 pages including subdirectories.

## Directories

- [ErrorCode/](ErrorCode/_index.md) - 5 pages
- [GraphDrained/](GraphDrained/_index.md) - 1 page
- [NodeCancelledError/](NodeCancelledError/_index.md) - 1 page
- [NodeError/](NodeError/_index.md) - 2 pages
- [NodeTimeoutError/](NodeTimeoutError/_index.md) - 6 pages
- [ParentCommand/](ParentCommand/_index.md) - 1 page

## Files

- [EmptyInputError](EmptyInputError.md) - Raised when graph receives an empty input.
- [ErrorCode](ErrorCode.md) - - Enum
- [GraphBubbleUp](GraphBubbleUp.md) - - Exception
- [GraphDrained](GraphDrained.md) - Raised when a graph run exits early due to a drain request.
- [GraphInterrupt](GraphInterrupt.md) - Raised when a subgraph is interrupted, suppressed by the root graph. Never raised directly, or surfaced to the user.
- [GraphRecursionError](GraphRecursionError.md) - Raised when the graph has exhausted the maximum number of steps.
- [InvalidUpdateError](InvalidUpdateError.md) - Raised when attempting to update a channel with an invalid set of updates.
- [NodeCancelledError](NodeCancelledError.md) - Raised when a node body raises asyncio.CancelledError itself.
- [NodeError](NodeError.md) - Failure context passed to a node-level error handler.
- [NodeInterrupt](NodeInterrupt.md) - Raised by a node to interrupt execution.
- [NodeTimeoutError](NodeTimeoutError.md) - Raised when a node invocation exceeds one of its configured timeouts.
- [ParentCommand](ParentCommand.md) - - GraphBubbleUp
- [TaskNotFound](TaskNotFound.md) - Raised when the executor is unable to find a task (for distributed mode).
- [create_error_message](create_error_message.md) - View source on GitHub
