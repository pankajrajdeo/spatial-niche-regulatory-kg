---
title: "reference/python/deepagents/middleware/filesystem"
description: "Index of 49 pages and 12 subdirectories under reference/python/deepagents/middleware/filesystem."
category: "index"
tags: [index, reference, python, deepagents, middleware, filesystem]
---

# reference/python/deepagents/middleware/filesystem

49 pages here, 83 pages including subdirectories.

## Directories

- [DeleteSchema/](DeleteSchema/_index.md) - 1 page
- [EditFileSchema/](EditFileSchema/_index.md) - 4 pages
- [ExecuteSchema/](ExecuteSchema/_index.md) - 2 pages
- [FilesystemMiddleware/](FilesystemMiddleware/_index.md) - 8 pages
- [FilesystemPermission/](FilesystemPermission/_index.md) - 3 pages
- [FilesystemState/](FilesystemState/_index.md) - 1 page
- [GlobSchema/](GlobSchema/_index.md) - 2 pages
- [GrepSchema/](GrepSchema/_index.md) - 5 pages
- [LsSchema/](LsSchema/_index.md) - 1 page
- [ReadFileSchema/](ReadFileSchema/_index.md) - 3 pages
- [ReadVideoFileSchema/](ReadVideoFileSchema/_index.md) - 2 pages
- [WriteFileSchema/](WriteFileSchema/_index.md) - 2 pages

## Files

- [DEFAULT_READ_LIMIT](DEFAULT_READ_LIMIT.md) - View source on GitHub
- [DEFAULT_READ_OFFSET](DEFAULT_READ_OFFSET.md) - View source on GitHub
- [DELETE_TOOL_DESCRIPTION](DELETE_TOOL_DESCRIPTION.md) - View source on GitHub
- [DeleteSchema](DeleteSchema.md) - Input schema for the delete tool.
- [EDIT_FILE_TOOL_DESCRIPTION](EDIT_FILE_TOOL_DESCRIPTION.md) - View source on GitHub
- [EMPTY_CONTENT_WARNING](EMPTY_CONTENT_WARNING.md) - View source on GitHub
- [EXECUTE_TOOL_DESCRIPTION](EXECUTE_TOOL_DESCRIPTION.md) - View source on GitHub
- [EditFileSchema](EditFileSchema.md) - Input schema for the edit_file tool.
- [ExecuteSchema](ExecuteSchema.md) - Input schema for the execute tool.
- [FilesystemMiddleware](FilesystemMiddleware.md) - Middleware for providing filesystem and optional execution tools to an agent.
- [FilesystemOperation](FilesystemOperation.md) - Classification of filesystem tools as read-only or mutating.
- [FilesystemPermission](FilesystemPermission.md) - A single access rule for filesystem operations.
- [FilesystemState](FilesystemState.md) - State for the filesystem middleware.
- [FsToolName](FsToolName.md) - Names of the built-in filesystem tools that can be passed to FilesystemMiddleware(tools=...).
- [GLOB_PATHLESS_DENIED_HINT](GLOB_PATHLESS_DENIED_HINT.md) - View source on GitHub
- [GLOB_TIMEOUT](GLOB_TIMEOUT.md) - View source on GitHub
- [GLOB_TOOL_DESCRIPTION](GLOB_TOOL_DESCRIPTION.md) - View source on GitHub
- [GLOB_TRUNCATION_NOTE](GLOB_TRUNCATION_NOTE.md) - View source on GitHub
- [GLOB_UNREADABLE_NOTE](GLOB_UNREADABLE_NOTE.md) - View source on GitHub
- [GREP_GLOB_DESCRIPTION](GREP_GLOB_DESCRIPTION.md) - View source on GitHub
- [GREP_OUTPUT_MODE_DESCRIPTION](GREP_OUTPUT_MODE_DESCRIPTION.md) - View source on GitHub
- [GREP_TOOL_DESCRIPTION](GREP_TOOL_DESCRIPTION.md) - View source on GitHub
- [GREP_TRUNCATION_NOTE](GREP_TRUNCATION_NOTE.md) - View source on GitHub
- [GlobSchema](GlobSchema.md) - Input schema for the glob tool.
- [GrepSchema](GrepSchema.md) - Input schema for the grep tool.
- [LIST_FILES_TOOL_DESCRIPTION](LIST_FILES_TOOL_DESCRIPTION.md) - View source on GitHub
- [LsSchema](LsSchema.md) - Input schema for the ls tool.
- [NO_LINES_REQUESTED_WARNING](NO_LINES_REQUESTED_WARNING.md) - Reported when a read requested zero lines.
- [NUM_CHARS_PER_TOKEN](NUM_CHARS_PER_TOKEN.md) - View source on GitHub
- [READ_FILE_TOOL_DESCRIPTION](READ_FILE_TOOL_DESCRIPTION.md) - View source on GitHub
- [READ_FILE_TRUNCATION_MSG](READ_FILE_TRUNCATION_MSG.md) - View source on GitHub
- [READ_FILE_VIDEO_TOOL_DESCRIPTION](READ_FILE_VIDEO_TOOL_DESCRIPTION.md) - View source on GitHub
- [ReadFileSchema](ReadFileSchema.md) - Input schema for the read_file tool.
- [ReadVideoFileSchema](ReadVideoFileSchema.md) - Input schema for read_file when the optional video frame extraction is available.
- [TOOLS_EXCLUDED_FROM_EVICTION](TOOLS_EXCLUDED_FROM_EVICTION.md) - View source on GitHub
- [TOO_LARGE_HUMAN_MSG](TOO_LARGE_HUMAN_MSG.md) - View source on GitHub
- [WRITE_FILE_TOOL_DESCRIPTION](WRITE_FILE_TOOL_DESCRIPTION.md) - View source on GitHub
- [WriteFileSchema](WriteFileSchema.md) - Input schema for the write_file tool.
- [append_to_system_message](append_to_system_message.md) - Append text to a system message.
- [check_empty_content](check_empty_content.md) - Check if content is empty and return warning message.
- [execute_accepts_timeout](execute_accepts_timeout.md) - Check whether a backend class's execute accepts a timeout kwarg.
- [extract_video_frames](extract_video_frames.md) - Decode sampled frames from a video byte payload.
- [format_grep_matches](format_grep_matches.md) - Format structured grep matches using existing formatting logic.
- [regex_literal_hint](regex_literal_hint.md) - Return a hint when a pattern looks like an (unsupported) regex.
- [sanitize_tool_call_id](sanitize_tool_call_id.md) - Sanitize tool_call_id to prevent path traversal and separator issues.
- [supports_execution](supports_execution.md) - Check if a backend supports command execution.
- [truncate_if_too_long](truncate_if_too_long.md) - Truncate list or string result if it exceeds token limit (rough estimate: 4 chars/token).
- [validate_path](validate_path.md) - Validate and normalize file path for security.
- [video_dependencies_available](video_dependencies_available.md) - Return whether the optional video dependencies appear to be installed.
