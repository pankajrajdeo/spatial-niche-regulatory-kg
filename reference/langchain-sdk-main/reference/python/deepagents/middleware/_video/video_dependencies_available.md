---
title: "video_dependencies_available"
description: "Return whether the optional video dependencies appear to be installed."
source: "https://reference.langchain.com/python/deepagents/middleware/_video/video_dependencies_available"
category: "reference"
tags: [reference, deepagents, middleware, video, video_dependencies_available]
---

# video_dependencies_available

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/_video/video_dependencies_available)

Return whether the optional video dependencies appear to be installed.

Uses `importlib.util.find_spec`, which checks that `av` and Pillow are
*discoverable* rather than performing a full import. A discoverable but
broken install (e.g. a compiled extension that fails to load) is reported as
available here and surfaces later, at actual extraction time, as a
`VideoExtractionError` carrying `MISSING_VIDEO_HINT`.

## Signature

```python
video_dependencies_available() -> bool
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/_video.py#L40)
