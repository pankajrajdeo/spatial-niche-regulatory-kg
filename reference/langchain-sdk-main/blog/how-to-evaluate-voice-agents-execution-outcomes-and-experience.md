---
title: "How to evaluate voice agents: execution, outcomes, and experience"
description: "Learn how to evaluate voice agents across execution, outcomes, and caller experience using LangSmith traces, code evaluators, LLM judges, and human review."
source: "https://www.langchain.com/blog/how-to-evaluate-voice-agents-execution-outcomes-and-experience"
category: "blog"
published: "2026-08-04T17:00:00.000Z"
author: "LangChain Accounts"
tags: [blog, how-to-evaluate-voice-agents-execution-outcomes-and-experience]
---

# How to evaluate voice agents: execution, outcomes, and experience

Building voice agents is hard because a good one must feel natural to talk to, be capable of resolving the user’s issue, and deliver the business outcome it was designed for.

A call might include long pauses from the agent that sound awkward but still resolve the user’s issue. Or, an agent could follow its instructions exactly yet fail the customer because it lacks the context required to answer the customer’s request.

Both scenarios reveal room for improvement. Evaluations help teams identify those weaknesses and measure whether changes actually make the agent better.

That’s why we recommend evaluating voice agents across three dimensions:

1. **Execution:** Did the agent follow its instructions?
2. **Outcome:** Did the interaction achieve its intended goal?
3. **Experience:** Was the conversation a smooth experience for the caller?

The dimensions are related, but they are not interchangeable. And to evaluate them well, you need more than a transcript. In LangSmith, you can trace the full interaction, score it with multiple evaluators, inspect the recording and tool activity, and compare changes over time.

## Execution: Did the agent follow its instructions?

Execution measures whether the agent adhered to its design.

- Did it call the right tools with the right arguments and in the right order?
- Did it follow the privacy, disclosure, and consent policies in its prompts?
- Did it collect and confirm the required information before taking action?
- Did it give the caller accurate information based on the context available?

Execution covers both the final response and the path the agent took to produce it. A voice agent might eventually give the right answer while calling unnecessary tools, skipping a required confirmation, or accessing information it should not have used. For a single invocation of the agent this might be ok, but with repeated interactions these mistakes can create bad user experiences.

### Use deterministic evaluators for explicit requirements

Some execution requirements can be evaluated with straightforward rules. For an appointment-scheduling agent, you can check whether:

- `check_availability` was called before `book_appointment`
- `book_appointment` received the confirmed date, time, and timezone
- A required disclosure appeared in the transcript
- A tool call returned a success or error response
- A tool was called more times than expected

These checks work well when the correct behavior can be defined explicitly. They are also fast and inexpensive because they do not require an additional model call.

In LangSmith, this is where [code evaluators](../langsmith/evaluation-types.md#code-evaluators) are especially useful. You can trace the call and then check deterministic rules against the trace.

### Use LLM judges for semantic requirements

Other requirements depend on meaning rather than exact values. An LLM judge can evaluate whether the agent:

- Followed a policy written in natural language
- Answered the caller’s question accurately based on the information available
- Requested the information required by its instructions
- Explained the next step clearly enough for the caller to understand it
- Used professional and context-appropriate language
- Recognized an ambiguous request and asked an appropriate clarifying question

LLM judges work best when the task is narrow and the criteria are explicit. A broad question such as “Was this response good?” will produce noisy results. A specific rubric is more repeatable:

> Pass if the agent confirms the appointment date, time, and timezone before calling the booking tool. Fail if any field is missing or if the booking occurs before confirmation.

In LangSmith, this is where an [LLM judge](../langsmith/evaluation-types.md#llm-as-a-judge) can score a conversation against a precise rubric. For example, you can score whether the agent asked for the missing timezone before proceeding, or whether it handled a policy-sensitive request correctly.

LLM judges work well because narrow judging tasks are easier than generating the original response, especially when the judge receives an explicit rubric and the complete trace.

## Outcome: Did the interaction achieve its goal?

Suppose a scheduling agent is instructed to collect a date and time, check availability, and book an appointment. It completes all three steps. But the workflow never tells it to confirm the caller’s timezone, so the appointment is booked for the wrong time. In this case, the agent followed its instructions accurately, but still failed the user. This distinction separates instruction adherence from outcome effectiveness, and is critically important for assessing whether a voice agent is working.

### Evaluate qualitative outcomes with LLM judges

An LLM judge can help determine whether the interaction achieved its intended goal:

- Was the caller’s underlying request resolved?
- Did the agent complete the requested task rather than only explain how to complete it?
- If the task could not be completed, did the agent take the appropriate fallback action?
- Did the agent have enough context, knowledge, and tool access to succeed?

These evaluations point to the appropriate intervention. A failure might require updating the knowledge base, adding a tool, clarifying the instructions, or defining behavior for a scenario the developers did not anticipate.

For example, in LangSmith you could score a scheduling conversation on whether a user who called the agent to book an appointment ended the call with a scheduled booking.

Production calls can also expose failures indirectly. A caller might say, “I called earlier, but the appointment was booked for the wrong time.” That signal can reveal an outcome failure that was not obvious in the original conversation.

### Measure downstream business outcomes

Whenever possible, measure the downstream result instead of inferring success from the conversation alone. A scheduling agent should be evaluated against the appointment record, a support agent against resolution and ticket reopen data, and a transfer agent against whether the caller reached the correct destination.

For example:

- **Scheduling:** Was the appointment booked for the correct person, time, location, and timezone?
- **Customer support:** Was the issue resolved, or was the case reopened later?
- **Transfers:** Did the destination answer, and was it the correct destination?
- **Sales or onboarding:** Did the intended next step or meeting happen?

Useful outcome metrics may include booking success rate, resolution rate, escalation rate, transfer success rate, reopened issue rate, conversion rate, or abandonment rate. The right metric depends on the workflow.

In LangSmith, you can connect these business signals back to the original trace and score the conversation against the actual outcome. That makes it easier to see whether a new prompt improved the flow while also improving the real business result.

## Experience: Did the conversation work well for the caller?

A voice agent represents your business to its customers. Callers experience not only what the agent says, but also how quickly it responds, how clearly it speaks, and how naturally it participates in the conversation. A correct and effective agent can still be a poor voice agent.

### Measure responsiveness

Latency is one of the most noticeable characteristics of a voice interaction. The primary user-perceived measure is often end-of-turn latency: the time from the end of the caller’s turn to the beginning of the agent’s response.

A typical voice pipeline includes voice activity detection, speech-to-text, model inference, tool calls, and text-to-speech. Measuring each component separately helps identify whether a delay comes from transcription, reasoning, an external system, or audio generation.

Useful measurements include:

- Time to first audio
- Speech-to-text latency
- Model time to first token
- Tool latency
- Text-to-speech latency
- P50, P95, and P99 latency for each relevant measurement

The same awkward pause can have different causes. The model might be slow, a tool might be blocking, or speech generation might wait until the entire response has been produced. LangSmith traces help identify which component contributed to the delay instead of treating latency as a single black-box number.

### Evaluate naturalness and clarity

Naturalness includes more than whether the generated voice sounds human. It can include:

- Pronunciation
- Pacing and cadence
- Vocal tone
- Volume consistency
- Expressiveness
- Awkward pauses
- Robotic repetition
- Whether the voice matches the conversational context

These properties can be scored by an audio-capable model. A transcript-only judge can evaluate whether the wording was clear or friendly, but it cannot reliably determine whether the agent sounded clear or friendly. Claims about vocal delivery require access to the audio.

In LangSmith, this is where audio-aware [LLM judges](../langsmith/evaluation-types.md#llm-as-a-judge) become useful. For example, you might score whether the agent’s pronunciation was understandable, whether it interrupted too aggressively, or whether the pacing felt natural for a support call.

### Measure conversational friction

The structure of a conversation can reveal usability problems. Useful signals include:

- The caller asking the agent to repeat itself
- The agent asking the caller to repeat information
- Repeated clarification loops
- The agent interrupting the caller
- The caller interrupting the agent
- Long silences
- Overlapping speech
- Abnormally long calls
- Early termination or abandonment
- Failure to recover after an interruption

These signals need context. A clarifying question can be good behavior when a request is ambiguous. The problem is unnecessary clarification, repeated clarification, or failure to use information the caller already provided.

Similarly, an interruption is not automatically bad. Callers expect to be able to interrupt a voice agent. The more useful question is whether the agent stopped speaking, preserved the relevant context, and responded appropriately.

In LangSmith, you can turn these into practical evaluators too. For example, you can score whether a call had repeated clarification loops, excessive silence, or failed recovery after an interruption.

## Match the evaluator to the signal

No single evaluation method works for every dimension. Choose the method based on the evidence required:

| Method | Best for | Example |
| --- | --- | --- |
| Code evaluators | Explicit, deterministic, machine-verifiable behavior | Tool order, required arguments, latency thresholds |
| LLM judges | Narrow semantic criteria | Whether the caller’s request was resolved |
| Audio-aware LLM judges | Properties present in the recording | Pronunciation, pacing, overlapping speech |
| Business-system checks | Real-world results | Reopened cases, completed transfers, attended meetings |

MethodBest forExampleCode evaluatorsExplicit, deterministic, machine-verifiable behaviorTool order, required arguments, latency thresholdsLLM judgesNarrow semantic criteriaWhether the caller’s request was resolvedAudio-aware LLM judgesProperties present in the recordingPronunciation, pacing, overlapping speechBusiness-system checksReal-world resultsReopened cases, completed transfers, attended meetings

Human review remains important for ambiguous and high-stakes behavior. Reviewers can determine whether a written policy is clear, whether an automated evaluator is applying it correctly, and whether an unusual conversation represents a legitimate exception.

Human labels also help calibrate LLM judges. If reviewers frequently disagree with the evaluator, its rubric or prompt may need work. If reviewers disagree with one another, the evaluation criterion itself may be underspecified.

In LangSmith, human review is supported with [annotation queues](../langsmith/annotation-queues.md): use them to validate the evaluator, sharpen the rubric, and improve the next version of the trace-based workflow.

## Build a continuous evaluation loop in LangSmith

In LangSmith, you can turn representative conversations into a dataset and define expected behavior for each scenario. A useful dataset might include:

- Common customer requests
- Known production failures
- Ambiguous requests
- Tool errors
- Transfers and escalations
- Unusual but important edge cases
- Calls with challenging audio conditions

You can then run experiments to compare prompts, models, tools, or workflow changes against the same dataset.

Because execution, outcome, and experience remain separate, an experiment can reveal that a new prompt improves instruction adherence while reducing resolution rate. It might show that a workflow change increases successful bookings while introducing more policy violations, or that a faster model lowers latency but handles interruptions less reliably. These tradeoffs disappear inside a single aggregate quality score.

Production evaluation can also reveal patterns that individual call reviews miss. Evaluators can attach structured feedback to traces, including intent, resolution status, failure reason, sentiment, or conversational-friction indicators. These labels make it possible to identify common intents, recurring failures, and unmet customer needs across many conversations.

A practical workflow looks like this:

1. **Trace the complete interaction.** Capture the recording alongside speech-to-text, model, tool, and text-to-speech operations. In LangSmith, this gives you the full call history in one place.
2. **Evaluate production conversations.** Apply execution, outcome, and experience evaluators to a representative sample of calls.
3. **Track metrics over time.** Monitor trends in resolution, latency, escalation, policy adherence, and conversational friction in LangSmith dashboards.
4. **Compare changes against consistent criteria.** When you update the prompt, model, tools, or workflow, rerun the same evaluators against the same dataset.
5. **Inspect failures in context.** Use the trace and recording to locate the component responsible for the failure.
6. **Add human review where needed.** Use annotation queues for uncertain or high-impact examples and to calibrate automated judges.
7. **Repeat.** Evaluations are most useful as part of the development loop, not as a one-time launch checklist.

With LangSmith, you can score voice agents consistently across frameworks and platforms, so you can compare behavior even when the underlying stack changes.

A voice agent is simultaneously a software system, a goal-directed workflow, and a customer experience. To understand whether the agent actually worked beyond simply knowing that the call completed requires evaluating all three.

To get started: [sign up](https://smith.langchain.com/) | [read the docs](../langsmith/trace-openai-realtime.md)
