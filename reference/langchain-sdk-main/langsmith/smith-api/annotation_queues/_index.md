---
title: "langsmith/smith-api/annotation_queues"
description: "Index of 9 pages and 0 subdirectories under langsmith/smith-api/annotation_queues."
category: "index"
tags: [index, langsmith, smith-api, annotation_queues]
---

# langsmith/smith-api/annotation_queues

9 pages here.

## Files

- [Add a reviewer to an annotation queue](add-a-reviewer-to-an-annotation-queue.md) - Assigns a single identity as a reviewer for the queue. Idempotent.
- [Add annotation queue items](add-annotation-queue-items.md) - Add RUN or THREAD items to a single annotation queue. RUN items require run_id unless they are created from a suggested example. THREAD items require thread_id and project_id.
- [Create annotation queue item status](create-annotation-queue-item-status.md) - Log the caller's reviewer status for a RUN or THREAD annotation queue item. A null status re-shows the item for this reviewer.
- [Delete annotation queue items](delete-annotation-queue-items.md) - Remove RUN or THREAD items from a single annotation queue by item ID.
- [Get annotation queue item placement](get-annotation-queue-item-placement.md) - Resolve a RUN or THREAD item to its current review section and zero-based position for deep linking. The returned cursor counts RUN and THREAD items together, so it is only valid for a list request...
- [Get the annotation queue item count](get-the-annotation-queue-item-count.md) - Returns the number of annotation queue items in one status bucket. The two time windows are independent: start_time/end_time bound when an item was archived, min_start_time/max_start_time bound when...
- [List annotation queue items](list-annotation-queue-items.md) - List RUN and THREAD items in a single annotation queue for one review status section, with opaque cursor pagination. Optional item_type=RUN|THREAD filters the page. Optional...
- [Remove a reviewer from an annotation queue](remove-a-reviewer-from-an-annotation-queue.md) - Unassigns an identity as a reviewer for the queue. Idempotent.
- [Update an annotation queue item](update-an-annotation-queue-item.md) - Partially update mutable timestamps (added_at, last_reviewed_time) for a RUN or THREAD annotation queue item. Omit a field, or pass JSON null, to leave it unchanged.
