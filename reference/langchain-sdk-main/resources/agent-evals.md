---
title: "Evaluating AI Agents at the Run, Trace, and Thread Level"
description: "An agent can pass every test and still be fragile in production. The answers look great at first. But when a user asks a question your test suite already covers, the agent can take a different route..."
source: "https://www.langchain.com/resources/agent-evals"
category: "resources"
published: "2026-06-23"
author: "LangChain"
tags: [resources, agent-evals]
---

# Evaluating AI Agents at the Run, Trace, and Thread Level

An agent can pass every test and still be fragile in production. The answers look great at first. But when a user asks a question your test suite already covers, the agent can take a different route. It calls the wrong tool, loops through retrieval when it should not, and still lands on the right answer. The next time it takes that same flawed route, it breaks.

That is the trap. If you only score the final output, your agentic systems may look healthier than they are. A correct answer can mask an unstable, inefficient, or risky execution path. To catch these failures, agent evaluation has to treat the output, the tool path, the context used, and the conversation state as a single release surface.

The root cause is architectural. AI agents are non-deterministic systems that operate across multiple steps. Decisions about tool choice, arguments, and how intermediate results get interpreted compound within a single request. When something goes wrong, there is no stack trace to point to the exact step where things drifted.

Most teams still evaluate agents the way they evaluate prompt chains. They check the final output, maybe run an LLM-as-a-judge on the response, and call it a day. [LangChain's State of Agent Engineering survey](https://www.langchain.com/state-of-agent-engineering) found that 89% of organizations have implemented observability, but only 52% run offline evals on test sets and just 37% run online evals. The tooling to see what agents are doing has outpaced the tooling to judge whether they're doing it well.

The solution is a different type of evaluation architecture, one that checks the reasoning path alongside the output, bridges offline testing with production monitoring, and calibrates automated judges against human expertise.

## Three levels of agent evaluation

Agent evaluation has to match the structure of agent execution. A prompt eval checks one input-output pair. An agent eval has to check decisions at multiple levels, because failures can occur at any of them.

We use three levels of evaluation mapped directly to three observability primitives:

- **Runs**: a single LLM call or tool invocation
- **Traces**: the complete execution of one agent turn
- **Threads**: a multi-turn conversation grouping multiple traces over time

**Single-step evaluation** validates individual runs. Did the agent call the right tool at this step? Did it pass the correct arguments? About half of our agent test cases are single-step tests because they're fast, cheap, and give a targeted signal on specific decisions. We can isolate a single step using techniques like [LangGraph's](https://www.langchain.com/langgraph) `interrupt_before` to constrain the agent loop to one action, then assert on the tool choice, the arguments, or the intermediate output.

**Full-turn evaluation** validates complete traces across three dimensions:

- **Final response**: Is the output correct?
- **Trajectory**: Did the agent take a reasonable path?
- **State changes**: Did the agent create the right artifacts or side effects?

A calendar scheduling agent, for example, might need to assert that it called `edit_file` on the correct document, that its final message confirmed the update, and that the file actually contains the new preference. Each assertion can use a different evaluator type.

Trajectory evaluation often breaks down because it is too rigid. It is tempting to assert that an agent followed a specific sequence of tool calls in a specific order. In practice, agents often reach the right result through valid paths that an evaluator did not anticipate.

Instead, score what matters: the outcome and the quality of the decisions that produced it. Allow partial credit when the agent makes measurable progress even if the exact path differs from your expected plan. Reserve strict, ordered tool-call matching for the cases where the sequence is required for correctness or safety.

**Multi-turn evaluation** validates threads. This is where most evaluation platforms fall short. An AI agent that handles individual turns well can still struggle with context switching, memory management, or multi-step reasoning across a full conversation. Thread-level evaluation reveals patterns that run-level scoring misses.

Multi-turn evals score three things once a thread completes:

- **Semantic intent**: what the user was actually trying to do
- **Semantic outcomes**: whether the task was completed, and if not, why
- **Agent trajectory**: the full interaction, including tool calls and decisions

Single-turn metrics often don't correlate with actual user success. An agent can score well on 90% of individual turns and still fail to resolve the user's problem across the whole conversation.

One practical pattern for multi-turn testing is N-1 testing, which takes real conversation prefixes from production (the first N-1 turns) and lets the agent generate only the final turn. This avoids hardcoded conversation scripts that fall apart when the agent takes a valid but unplanned path. For more complex flows, you can use conditional logic: run the first turn, check the output, and move to the next turn only if it meets expectations. If it does not, stop early and mark the test as a failure.

| Evaluation level | What it checks | When to use | Example |
| --- | --- | --- | --- |
| Single-step (run) | One tool call or LLM decision | Targeted debugging, regression on specific decisions | Did the agent select the correct API endpoint? |
| Full-turn (trace) | Final response + trajectory + state changes | Release gating, regression testing | Did the agent complete the task via a reasonable path? |
| Multi-turn (thread) | Semantic intent, outcome, and trajectory across the conversation | Conversational agents, multi-session workflows | Did the agent resolve the user's issue across all turns? |

These three levels work together. Full-turn and multi-turn evals show us *whether* the agent broke, while single-step evals show us *where* it broke. A reliable eval suite needs both the end-to-end and the component-level view.

## Offline and online evaluation

Knowing what to evaluate at each level solves only half the problem. The other half is deciding *when* to evaluate.

Offline evaluations run against curated datasets with reference outputs. We control the examples and can check correctness against ground truth because we've defined what correct looks like for each input. This is where [regression testing](https://www.langchain.com/articles/llm-evals) happens. We build a dataset of known scenarios, run the agent against it, then verify that changes don't break existing behavior. [monday.com](http://monday.com)[built a code-first evaluation strategy on LangSmith](https://www.langchain.com/blog/customers-monday), and they describe offline evals as "the safety net," testing core logic like groundedness, retrieval accuracy, and tool-calling, plus edge cases like knowledge base conflicts.

Online evaluations monitor production traffic without reference outputs. They reveal what an AI agent actually does when real users interact with it. Online evaluation catches issues a test suite can’t anticipate:

- Unexpected inputs from real user behavior
- Edge cases you didn't think to test for
- Gradual performance degradation as usage patterns shift

Neither approach works on its own. When teams over-index on offline testing, they can spend weeks building exhaustive pre-deployment suites for edge cases that only show up once real users interact with the system. When teams rely too heavily on production monitoring, they often try to score correctness without ground truth, asking “is this right?” when the more appropriate questions are “is this safe?” and “is this coherent?”

In practice, offline evals validate known scenarios before deployment, and online evals surface unknown issues after deployment. A typical setup runs offline checks on every change, then monitors key metrics in production to catch what slipped through.

For online evaluation, cost management is important to take into consideration. Start with a 10% sampling rate on production traces to control LLM-as-a-judge costs, and trigger LLM-based checks only when deterministic checks show drops in quality. This keeps costs manageable while still catching subjective issues.

Production does more than surface missed bugs. It shows us what to test for offline. A problematic trace caught in production can seed a dataset, and that dataset becomes the ground truth for regression testing, turning production failures into future test coverage.

|  | Offline evals | Online evals |
| --- | --- | --- |
| Data source | Curated datasets with reference outputs | Sampled production traces |
| What they test | Correctness, regression, known edge cases | Quality patterns, safety, drift, unexpected behavior |
| Evaluator types | Code-based, LLM-as-a-judge (reference-based), human | Code-based, LLM-as-a-judge (reference-free), user feedback |
| When they matter | Before every deployment, during CI | Continuously in production |
| Limitation | Cannot anticipate real user behavior | No ground truth for correctness checks |

## Calibrating the judges

When eval costs creep up to more than running the agent itself and the judges are still unreliable, the common temptation is to skip evaluation entirely. The better path forward is to make the judges trustworthy.

[LLM-as-a-judge](https://www.langchain.com/articles/llm-as-a-judge) is the practical default for agent evaluation at scale. Human reviewers can meaningfully assess 50-100 traces per hour, so at 1,000 requests per day, full manual review would require 10-20 dedicated hours daily. LLM judges fill the gap, but they carry well-documented failure modes:

- Verbosity bias, where longer outputs score higher regardless of quality
- Scoring drift over time as model behavior shifts
- Contradictory results depending on whether outputs are scored individually or side-by-side

[Academic benchmarks](https://www.langchain.com/resources/llm-evaluation-benchmarks) like[MT-Bench](https://arxiv.org/abs/2402.14762) found that strong LLM judges achieve over 80% agreement with human evaluators, comparable to the agreement rate between human annotators themselves. In practice, that baseline erodes on domain-specific agent tasks that fall outside what MT-Bench measures. Calibration against your own labeled examples is what closes the gap.

The right evaluator type depends on the check:

- **Code-based evaluators** for objectively correct answers. Did the agent call the expected tool? Does the output match a regex or schema? Deterministic comparison eliminates the inconsistency of LLM scoring for objective checks and gives a cleaner signal.
- **LLM-as-a-judge** for subjective assessments. Is the response helpful? Is the tone appropriate? Is the trajectory reasonable? Reserve LLM judges for questions that require semantic understanding.
- **Human review** for ambiguous cases, high-stakes decisions, and calibration of the automated judges themselves.
- **Pairwise evaluation** for version comparison. When we need to know whether version B is better than version A, pairwise scoring is more reliable than absolute scoring.

For LLM-as-a-judge, prefer binary pass/fail over numeric scales. A 1-5 scale introduces subjective differences between adjacent scores and requires larger sample sizes for statistical significance. Binary scoring gives a cleaner signal with less data.

Calibration makes the judge’s quality measurable. It connects rubric changes to observable improvements in agreement and consistency, instead of relying on intuition about whether the evaluator prompt is “better.”[Align Evals](https://www.langchain.com/blog/introducing-align-evals) replaces that loop with a systematic process. It collects human corrections, iterates on the evaluator prompt against labeled examples, and tracks agreement over time. We tend to start with 20 or more labeled examples and add more over time to avoid overfitting. We recommend including reasoning in the judge's output so you can diagnose disagreements. It’s important to recalibrate regularly, because judges drift just like the agents they evaluate.

## Human review that scales

Automated evaluation handles volume while human review handles judgment, and the question is how to connect them without burning reviewer time on traces that don't need human eyes.

[Annotation Queues](../langsmith/annotation-queues.md) solve this by routing specific subsets of traces to domain experts for review. Rather than asking humans to review everything, you define rules that filter for the traces most likely to need expert judgment. Routing choices have real tradeoffs. Annotation Queues require dedicated reviewer time and can add latency. They work best when focused on specific high-value traces rather than attempting broad coverage.

For specialized domains like law, medicine, or finance, expected output quality requires subject matter expertise that automated methods can't replicate. The bottleneck in these domains is rarely the willingness of domain experts to weigh in. It's giving them a workflow that doesn't require engineering handholding for every trace they touch. Annotation Queues give those reviewers a structured place to label and correct complex traces, so the experts who actually understand the domain stay in the loop without becoming a release-blocking dependency.

This human feedback feeds directly into the evaluation system in two ways:

- First, corrected traces become ground truth. When a subject matter expert corrects an agent's output in an Annotation Queue, that corrected trace can be added to a dataset for future regression tests.
- Second, corrections calibrate automated judges. The human corrections become few-shot examples that align LLM-as-a-judge evaluators with expert judgment through the Align Evals workflow. Over time, the judge gets better at catching the same errors the expert would catch, which means fewer traces need human review in the first place.

The goal is to have humans teach the system what good looks like, then verify that the system is learning.

**When to route to human review vs. automated scoring:**

- An online evaluator returned a strongly negative score on a production trace
- The trace involves a high-stakes domain decision (financial, medical, legal)
- A user explicitly flagged the interaction as incorrect or unhelpful
- The trace triggered an edge case current evaluators aren't equipped to judge
- We're calibrating a new LLM-as-a-judge evaluator and need ground truth labels

## Closing the loop

So far, we’ve covered four essential pieces: the three evaluation levels, the two evaluation stages, calibrated judges, and human review. Each one matters, but no single method is enough on its own. Teams ship with confidence when they connect these methods into a continuous system, rather than treating them as isolated checks.

After working with hundreds of organizations deploying AI agents, we've seen one pattern distinguish the teams that iterate fastest. They treat production traces as the starting point for [LLM evaluation](https://www.langchain.com/resources/llm-evals). Production traces feed the observability layer, [Insights](../langsmith/insights.md) extracts usage patterns from those traces, those findings shape datasets, and datasets power the evaluations that drive the next round of improvements. We call this the [Agent Development Lifecycle](https://www.langchain.com/blog/the-agent-development-lifecycle).

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a38a5a2fbf903a6eafa95fc_40.png)

When an online evaluator flags a problematic trace, they can add it to a dataset with a single click. That dataset becomes the ground truth for regression testing. Once a bug is fixed, it stays fixed because the failing scenario is now permanently in the test suite. Automations can trigger this workflow without manual intervention, auto-triggering dataset updates, routing traces to Annotation Queues, and running online evaluations on incoming trace data.

Picture a cluster of production traces where users keep hitting the same outdated guardrail, scattered across millions of unrelated traces. Insights groups those traces into a recognizable pattern, the team identifies the issue, and the fix ships. Without automated clustering, that failure mode stays buried.

For teams starting from scratch, three implementation phases build on each other:

1. **Establish the foundation.** Set up tracing. Add deterministic checks for the basics (right tools, right order, format compliance). Build a first dataset from 20-50 manually reviewed production traces. Run a first offline eval.
2. **Gate releases on regression tests.** Start converting production failures into dataset examples using the trace-to-dataset workflow. Establish a baseline on the core dataset and run experiments to compare outputs before and after every prompt change or model swap. For high-stakes changes, use Annotation Queues so domain experts can validate that improvements in one area don't introduce regressions elsewhere.
3. **Monitor continuously.** Deploy online evaluators on sampled production traffic. Add thread-level Multi-turn Evals for conversational agents. Set up alerting for spikes in negative scores, latency, or error rates. Feed flagged traces back into datasets and Annotation Queues to keep the loop turning.

Each phase builds on the previous one. A small dataset with deterministic checks will catch regressions that no amount of manual review can sustain at scale.

## What this looks like in LangSmith

[LangSmith](https://www.langchain.com/langsmith-platform), our framework-agnostic agent engineering platform, uses the same traces for debugging and evaluation. That means you do not need a second instrumentation pass or a separate evaluation pipeline. When you spot a problematic trace in the observability layer, you can move it into a dataset and write the assertions that should have caught it. The next regression run will include that scenario automatically. Over time, each trace that surfaces a bug becomes the test that prevents it from coming back.

Here's how each aspect of agent evals maps to LangSmith capabilities:

| Method | What it measures | Best for | Key tradeoff | How it runs in LangSmith |
| --- | --- | --- | --- | --- |
| Reference-based metrics | Overlap with a reference answer (BLEU, ROUGE, F1, exact match, BERTScore) | Structured tasks with ground truth | Surface similarity can miss meaning | Evaluators scored against dataset reference outputs |
| Reference-free metrics | Intrinsic output properties (perplexity, fluency, length) | Screening when no ground truth exists | Says little about task success | Evaluators that run without reference outputs, including on live traces |
| LLM-as-a-Judge | Rubric-graded quality such as helpfulness and faithfulness | Nuanced quality at scale | Bias and variance until calibrated | LLM-as-Judge evaluators calibrated with Align Evals |
| Code/functional evaluators | Deterministic pass/fail checks | Outputs with strict, checkable formats | Cannot judge nuance | Code evaluators returning structured feedback |
| Human annotation | Expert judgment and golden labels | Expert-judgment tasks and golden labels | Slow and expensive at volume | Annotation Queues routing traces to reviewers |

For teams getting started, the `openevals` package provides off-the-shelf LLM-as-a-judge and structured output evaluators you can wire into experiments without writing custom scoring code. The `agentevals` package handles trajectory evaluation, including strict tool-call matching for cases where order and arguments matter, and LLM-as-a-judge trajectory scoring for cases where reasonable variation is expected. Both packages work standalone, so you can adopt the framework piece by piece: start with offline evals on a small dataset, layer online evals on sampled production traffic, then bring in Annotation Queues and Align Evals as the volume of human review grows.

And because LangSmith is framework agnostic, you get full trace visibility on whatever you have already built, whether that is [LangChain](https://www.langchain.com/langchain), [LangGraph](https://www.langchain.com/langgraph), [Deep Agents](https://www.langchain.com/deep-agents), another framework, or custom code.
