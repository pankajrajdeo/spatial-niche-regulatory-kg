---
title: "reference/python/deepagents/profiles/harness/_nvidia_nemotron_3_ultra"
description: "Index of 16 pages and 15 subdirectories under reference/python/deepagents/profiles/harness/_nvidia_nemotron_3_ultra."
category: "index"
tags: [index, reference, python, deepagents, profiles, harness, nvidia_nemotron_3_ultra]
---

# reference/python/deepagents/profiles/harness/_nvidia_nemotron_3_ultra

16 pages here, 68 pages including subdirectories.

## Directories

- [ChatNVIDIAMessageCompatibilityMiddleware/](ChatNVIDIAMessageCompatibilityMiddleware/_index.md) - 3 pages
- [EntityResolutionGuardMiddleware/](EntityResolutionGuardMiddleware/_index.md) - 6 pages
- [EntityResolutionGuardState/](EntityResolutionGuardState/_index.md) - 2 pages
- [FinalAnswerGuardMiddleware/](FinalAnswerGuardMiddleware/_index.md) - 4 pages
- [FinalAnswerGuardState/](FinalAnswerGuardState/_index.md) - 1 page
- [FollowupDisciplineMiddleware/](FollowupDisciplineMiddleware/_index.md) - 4 pages
- [FollowupDisciplineState/](FollowupDisciplineState/_index.md) - 1 page
- [ModelRateLimitRetryMiddleware/](ModelRateLimitRetryMiddleware/_index.md) - 3 pages
- [NemotronPolicyNudgeMiddleware/](NemotronPolicyNudgeMiddleware/_index.md) - 6 pages
- [NemotronPolicyNudgeState/](NemotronPolicyNudgeState/_index.md) - 4 pages
- [NemotronProgressBudgetMiddleware/](NemotronProgressBudgetMiddleware/_index.md) - 6 pages
- [NemotronReasoningTagCleanupMiddleware/](NemotronReasoningTagCleanupMiddleware/_index.md) - 3 pages
- [NemotronTextToolCallParser/](NemotronTextToolCallParser/_index.md) - 3 pages
- [NemotronToolCallShim/](NemotronToolCallShim/_index.md) - 3 pages
- [ReadFileContinuationNoticeMiddleware/](ReadFileContinuationNoticeMiddleware/_index.md) - 3 pages

## Files

- [ChatNVIDIAMessageCompatibilityMiddleware](ChatNVIDIAMessageCompatibilityMiddleware.md) - Mirror standard LangChain tool-call fields into ChatNVIDIA payload metadata.
- [EntityResolutionGuardMiddleware](EntityResolutionGuardMiddleware.md) - Send Ultra3 back once when it finalizes with unresolved or mis-bound IDs.
- [EntityResolutionGuardState](EntityResolutionGuardState.md) - State schema for EntityResolutionGuardMiddleware.
- [FinalAnswerGuardMiddleware](FinalAnswerGuardMiddleware.md) - Send Ultra3 back once when a final answer drops obvious required details.
- [FinalAnswerGuardState](FinalAnswerGuardState.md) - State schema for FinalAnswerGuardMiddleware.
- [FollowupDisciplineMiddleware](FollowupDisciplineMiddleware.md) - Send Ultra3 back once when it asks redundant follow-up questions.
- [FollowupDisciplineState](FollowupDisciplineState.md) - State schema for FollowupDisciplineMiddleware.
- [ModelRateLimitRetryMiddleware](ModelRateLimitRetryMiddleware.md) - Retry transient provider 429s around model calls.
- [NemotronPolicyNudgeMiddleware](NemotronPolicyNudgeMiddleware.md) - Inject lightweight policy nudges for common Ultra3 agent-control misses.
- [NemotronPolicyNudgeState](NemotronPolicyNudgeState.md) - State schema for one-shot Nemotron policy nudges.
- [NemotronProgressBudgetMiddleware](NemotronProgressBudgetMiddleware.md) - Stop Ultra3-specific tool loops before they consume runaway context.
- [NemotronReasoningTagCleanupMiddleware](NemotronReasoningTagCleanupMiddleware.md) - Remove preserved blocks from normal assistant content.
- [NemotronTextToolCallParser](NemotronTextToolCallParser.md) - Repair tool calls emitted as text content instead of structured calls.
- [NemotronToolCallShim](NemotronToolCallShim.md) - Repair small Nemotron filesystem tool-call and tool-result quirks.
- [ReadFileContinuationNoticeMiddleware](ReadFileContinuationNoticeMiddleware.md) - Append a continuation notice to exactly-at-limit read_file results.
- [register](register.md) - Register the built-in Nemotron 3 Ultra harness profile.
