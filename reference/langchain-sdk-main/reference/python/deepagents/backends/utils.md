---
title: "utils"
description: "Shared utility functions for memory backend implementations."
source: "https://reference.langchain.com/python/deepagents/backends/utils"
category: "reference"
tags: [reference, deepagents, backends, utils]
---

# utils

> **Module** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/utils)

Shared utility functions for memory backend implementations.

This module contains both user-facing string formatters and structured
helpers used by backends and the composite router. Structured helpers
enable composition without fragile string parsing.

## Properties

- `logger`
- `EMPTY_CONTENT_WARNING`
- `EMPTY_OLD_STRING_ERROR`
- `MAX_VIDEO_INPUT_BYTES`
- `FileType`
- `MAX_LINE_LENGTH`
- `TOOL_RESULT_TOKEN_LIMIT`
- `TRUNCATION_GUIDANCE`
- `FileInfo`
- `GrepMatch`

## Methods

- [`compile_grep_include_glob()`](https://reference.langchain.com/python/deepagents/backends/utils/compile_grep_include_glob)
- [`sanitize_tool_call_id()`](https://reference.langchain.com/python/deepagents/backends/utils/sanitize_tool_call_id)
- [`format_content_with_line_numbers()`](https://reference.langchain.com/python/deepagents/backends/utils/format_content_with_line_numbers)
- [`check_empty_content()`](https://reference.langchain.com/python/deepagents/backends/utils/check_empty_content)
- [`file_data_to_string()`](https://reference.langchain.com/python/deepagents/backends/utils/file_data_to_string)
- [`create_file_data()`](https://reference.langchain.com/python/deepagents/backends/utils/create_file_data)
- [`update_file_data()`](https://reference.langchain.com/python/deepagents/backends/utils/update_file_data)
- [`normalize_read_bounds()`](https://reference.langchain.com/python/deepagents/backends/utils/normalize_read_bounds)
- [`slice_read_response()`](https://reference.langchain.com/python/deepagents/backends/utils/slice_read_response)
- [`perform_string_replacement()`](https://reference.langchain.com/python/deepagents/backends/utils/perform_string_replacement)
- [`truncate_if_too_long()`](https://reference.langchain.com/python/deepagents/backends/utils/truncate_if_too_long)
- [`to_posix_path()`](https://reference.langchain.com/python/deepagents/backends/utils/to_posix_path)
- [`validate_path()`](https://reference.langchain.com/python/deepagents/backends/utils/validate_path)
- [`grep_matches_from_files()`](https://reference.langchain.com/python/deepagents/backends/utils/grep_matches_from_files)
- [`build_grep_results_dict()`](https://reference.langchain.com/python/deepagents/backends/utils/build_grep_results_dict)
- [`format_grep_matches()`](https://reference.langchain.com/python/deepagents/backends/utils/format_grep_matches)
- [`regex_literal_hint()`](https://reference.langchain.com/python/deepagents/backends/utils/regex_literal_hint)

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/utils.py)
