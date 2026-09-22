---
title: "extract_video_frames"
description: "Decode sampled frames from a video byte payload."
source: "https://reference.langchain.com/python/deepagents/middleware/filesystem/extract_video_frames"
category: "reference"
tags: [reference, deepagents, middleware, filesystem, extract_video_frames]
---

# extract_video_frames

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/_video/extract_video_frames)

Decode sampled frames from a video byte payload.

## Signature

```python
extract_video_frames(
    content: bytes,
    *,
    offset_seconds: float,
    duration_seconds: float,
    sampling_rate: float,
) -> list[ContentBlock]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `content` | `bytes` | Yes | Raw bytes of the video file (as returned by the backend). |
| `offset_seconds` | `float` | Yes | Seconds into the source to start sampling. Must be non-negative. |
| `duration_seconds` | `float` | Yes | Seconds of source to sample. Must be > 0. |
| `sampling_rate` | `float` | Yes | Frames per second to emit. > 0. |

## Returns

`list[ContentBlock]`

Interleaved content blocks: a text header introducing each frame

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/_video.py#L119)
