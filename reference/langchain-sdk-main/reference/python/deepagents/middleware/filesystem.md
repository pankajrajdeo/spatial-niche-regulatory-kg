---
title: "filesystem"
description: "Middleware for providing filesystem tools to an agent."
source: "https://reference.langchain.com/python/deepagents/middleware/filesystem"
category: "reference"
tags: [reference, deepagents, middleware, filesystem]
---

# filesystem

> **Module** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/filesystem)

Middleware for providing filesystem tools to an agent.

## Properties

- `GlobTruncationReason`
- `MAX_VIDEO_INPUT_BYTES`
- `FileType`
- `TOO_LARGE_TOOL_MSG`
- `FilesystemOperation`
- `EMPTY_CONTENT_WARNING`
- `NO_LINES_REQUESTED_WARNING`
- `GLOB_TIMEOUT`
- `GREP_TRUNCATION_NOTE`
- `GLOB_TRUNCATION_NOTE`
- `GLOB_UNREADABLE_NOTE`
- `GLOB_PATHLESS_DENIED_HINT`
- `DEFAULT_READ_OFFSET`
- `DEFAULT_READ_LIMIT`
- `READ_FILE_TRUNCATION_MSG`
- `NUM_CHARS_PER_TOKEN`
- `GREP_GLOB_DESCRIPTION`
- `GREP_OUTPUT_MODE_DESCRIPTION`
- `LIST_FILES_TOOL_DESCRIPTION`
- `READ_FILE_TOOL_DESCRIPTION`
- `READ_FILE_VIDEO_TOOL_DESCRIPTION`
- `EDIT_FILE_TOOL_DESCRIPTION`
- `WRITE_FILE_TOOL_DESCRIPTION`
- `DELETE_TOOL_DESCRIPTION`
- `GLOB_TOOL_DESCRIPTION`
- `GREP_TOOL_DESCRIPTION`
- `EXECUTE_TOOL_DESCRIPTION`
- `FsToolName`
- `TOOLS_EXCLUDED_FROM_EVICTION`
- `TOO_LARGE_HUMAN_MSG`

## Methods

- [`execute_accepts_timeout()`](https://reference.langchain.com/python/deepagents/middleware/filesystem/execute_accepts_timeout)
- [`check_empty_content()`](https://reference.langchain.com/python/deepagents/middleware/filesystem/check_empty_content)
- [`format_grep_matches()`](https://reference.langchain.com/python/deepagents/middleware/filesystem/format_grep_matches)
- [`regex_literal_hint()`](https://reference.langchain.com/python/deepagents/middleware/filesystem/regex_literal_hint)
- [`sanitize_tool_call_id()`](https://reference.langchain.com/python/deepagents/middleware/filesystem/sanitize_tool_call_id)
- [`truncate_if_too_long()`](https://reference.langchain.com/python/deepagents/middleware/filesystem/truncate_if_too_long)
- [`validate_path()`](https://reference.langchain.com/python/deepagents/middleware/filesystem/validate_path)
- [`append_to_system_message()`](https://reference.langchain.com/python/deepagents/middleware/filesystem/append_to_system_message)
- [`extract_video_frames()`](https://reference.langchain.com/python/deepagents/middleware/filesystem/extract_video_frames)
- [`video_dependencies_available()`](https://reference.langchain.com/python/deepagents/middleware/filesystem/video_dependencies_available)
- [`supports_execution()`](https://reference.langchain.com/python/deepagents/middleware/filesystem/supports_execution)

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/filesystem.py)
