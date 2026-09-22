---
title: "Customer Experience (CX) Agents in Production"
description: "Lessons from Lyft, Vodafone, and LATAM Airlines"
source: "https://www.langchain.com/resources/customer-experience-cx-agents-in-production"
category: "resources"
published: "2026-08-04"
author: "LangChain"
tags: [resources, customer-experience-cx-agents-in-production]
---

# Customer Experience (CX) Agents in Production

Customer experience has become one of the fastest-moving categories for agents, partly because the ROI is relatively easy to measure. Faster responses can improve conversion, fewer escalations can reduce the cost per contact, and more successful resolutions can help retain customers.

As CX agents move into production, the challenge shifts from building them to improving how they operate. Teams are learning from real interactions, refining agent behavior, and deciding when a conversation should become a structured workflow. Increasingly, they are also using those interactions to improve the broader customer experience.

The teams furthest along treat agents as production systems that require continuous testing, deployment, monitoring, and iteration. This piece looks at how that approach is taking shape across three companies:

- **Lyft, **which built a self-serve platform that allows non-technical operations teams and product managers to configure and launch support agents
- **Fastweb + Vodafone, **which built Super TOBi and Super Agent to support both customer-facing conversations and internal call-center teams
- **LATAM Airlines, **which built Concierge, its travel-assistance agent, and Compass, a system that turns unstructured conversations into structured signals

Drawing on additional examples from Cisco and Podium, we’ll explore the use cases emerging across customer experience, the technical and operational challenges teams encounter in production, and how LangSmith, Deep Agents, and LangGraph support continuous improvement throughout the [Agent Development Lifecycle](https://www.langchain.com/blog/the-agent-development-lifecycle).

## The emerging patterns in Customer Experience agents

**Consumer-facing self-service agents** are often the most visible starting point. They interact directly with customers through chat or voice, helping with tasks such as billing, account access, claims, and appointment scheduling. Their value is relatively easy to measure: faster responses can improve conversion, while more successful resolutions can reduce escalations and lower support costs. Podium’s AI Employee, for example, responds to inbound leads for car dealerships, HVAC contractors, and other local businesses. For these companies, responding within five minutes produces a 46% higher lead-conversion rate than responding within an hour.

**Frontline and rep copilots **can be an even higher-leverage use case. Rather than speaking directly to customers, these agents work alongside human representatives and surface the next best action. Cisco’s CX organization uses this approach for network engineers. Its system narrows thousands of potential findings down to the handful that matter most, so even a vague request like “help” can be routed toward the right issue.

**Self-serve platforms emerge **when engineering can no longer build every agent. Lyft’s platform allows operations teams and product managers to create a prompt and configuration file, then launch a new support agent without involving a machine learning engineer. Podium built a similar system around the same primitives it uses internally. This lets one underlying architecture support a wide range of use cases, from automotive sales to HVAC warranty support.

**Semantic routing and triage **become critical when customer requests are incomplete or ambiguous. LATAM Airlines saw this with Concierge. Initially, 13% of messages were classified as out of scope. After reviewing the conversations, the team found that 95% were legitimate passenger needs the agent had not yet been designed to handle, including check-in and baggage questions. Adding a customer-care specialist reduced the out-of-scope rate from 13% to 1%.

**Evals become a shared language **across technical and domain teams**.** As more people contribute to building agents, teams need a consistent way to define what good behavior looks like and determine whether an agent is ready to ship. Evals turn domain expertise into concrete, testable criteria that engineers, product managers, and operations teams can use to review performance and guide improvements.

Lyft encountered this after opening agent development to non-engineers. The platform was no longer the primary constraint; prompt and evaluation quality were. The team introduced a structured prompt-writing framework and automated checks to catch contradictory instructions and incomplete conversation paths before they reached production.

Together, these patterns show how the work changes once CX agents reach production. The following three teams illustrate how organizations are designing, evaluating, and improving these systems at scale.

## Three teams with CX agents in production

### **Lyft: Turning support engineering into a self-serve platform**

Lyft’s AI Assist supports riders and drivers across issues such as account access, damage claims, charge reviews, and earnings disputes. The volume of trips Lyft facilitates necessitates an agentic system for support. Lyft facilitates 79 million trips each month, while AI Assist handles roughly 270,000 monthly interactions across seven or more production agents. The system has achieved a 65% deflection rate and a 35% AI resolution rate.

Lyft sets an intentionally high bar for resolution, requiring the agent to solve an issue end to end rather than simply prevent the customer from reaching a human. For complex workflows such as driver damage claims, that can include collecting information and photos, retrieving data through tools, applying fraud signals, making a decision, and explaining the outcome to the driver (all within 15 minutes).

#### Agent architecture

Lyft’s current system uses a router-based, multi-agent architecture built on **LangGraph**. A meta-agent classifies each incoming request and routes it to a specialized subagent, with separate paths for riders and drivers. Each subagent is itself a complete LangGraph state graph registered as a subgraph node.

When an intent agent determines mid-conversation that a request requires a more specialized handler (e.g. moving from a general driver-intent agent to a damage-claim agent), it returns control to the meta-agent for rerouting. This prevents the conversation from being forced down the wrong path.

Lyft divides its agents into two categories:

- **Specialized agents** are built by machine learning engineers for complex, high-stakes workflows, such as damage claims involving image processing and fraud detection
- **Configurable agents** are the self-serve layer. They are initialized at runtime using a JSON configuration and a prompt from **LangSmith’s Prompt Hub**, which can be written by a domain expert rather than an engineer

**This approach reduced the time required to develop an agent from roughly six months for Lyft’s first driver agent to about two weeks for a new configurable agent.**

#### How Lyft builds evals

As the platform became easier to use, prompt and evaluation quality started to become bottlenecks.

Lyft built an evaluation flywheel that connects development and production. Before launch, the team runs simulated, multi-turn conversations in which an LLM role-plays the customer against the agent. Each simulation is defined around a task, user persona, and environment that reflects what the agent is likely to encounter in production. The resulting trajectory can be evaluated using a combination of code-based assertions and LLM judges, including whether the agent granted the correct concession, escalated appropriately, or resolved the issue within the expected number of turns.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a714a62bdc07f789825f3ab_Offline%20Simulation%20Eval%20%E2%80%94%20Guide%20Header%402x%201.png)

The diversity of those offline scenarios is important. Lyft uses offline evaluation as a launch gate, allowing the team to move quickly without treating real customers as test cases. An agent only progresses toward production when it meets the required quality threshold.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a714a7bf98dbc2e0f60797f_Dev%20%E2%86%92%20Production%20Lifecycle%402x%201.png)

The team learned early on that generic evaluation metrics weren’t enough. Initial measures such as response helpfulness, conversation naturalness, tool-use appropriateness, and conversation completeness produced scores, but didn’t tell the team what to change.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a714a8d061c8e36f0c7fd2a_Average%20Score%20by%20Metric%20%E2%80%94%20Chart%402x%201.png)

Lyft instead worked with operations and quality experts to build narrow, behavior-specific rubrics based on how support interactions should actually unfold. The team also moved from broad scalar scores to simpler pass-or-fail outcomes.

For example, an education rubric checks whether the agent provides useful educational content when it can solve the issue, but escalates once it becomes clear that it cannot. The agent fails if it repeats the same education too many times, escalates before making a reasonable attempt to help, or includes a factual error.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a714aa31d5773e92a76c8db_Education%20Rubric%20%E2%80%94%20Card%402x%201.png)

A separate escalation rubric defines the expected behavior when a user asks for a human. The agent should push back once, then escalate after a repeated request. It fails if it escalates immediately, refuses to escalate after the second request, escalates before providing necessary information, or continues for several turns after it is clear that it cannot help.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a714aae42d016cbd709d270_Escalation%20Rubric%20%E2%80%94%20Card%402x%201.png)

These rubrics are more useful than generic quality scores because each failure points toward a specific product, prompt, or workflow change.

Lyft also calibrates its LLM judges against human reviewers. The team collects human labels and iterates on each judge until it achieves a sufficiently high agreement rate. This gives the team confidence that automated scores reflect the standards its operations and quality teams would apply themselves.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a714a0e8f7394aaec5e09a0_Golden%20Dataset%20%E2%86%92%20Alignment%20Process%402x%201.png)

The simulated user requires the same level of calibration. Lyft’s first LLM-generated customers were too articulate, patient, and cooperative, producing offline pass rates above 90% that did not reflect production behavior. Real users often write in fragments, omit context, repeat themselves, or arrive with a specific goal such as securing a refund or bypassing the agent.

To make offline evaluation more realistic, Lyft fine-tuned its simulated user on real customer verbatims and introduced personas such as refund seekers, AI skeptics, and users determined to reach a human. Making the simulated customer less polished made the evaluation harder, but also made offline results more predictive of production performance.

Once an agent launches, the same evaluation loop continues online. Every invocation is traced in **LangSmith** across development, staging, and production, including the agent’s reasoning, the educational content it retrieved, and the tools it called. This allows the team to identify whether a failure came from routing, context, tool execution, or the final response.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a71492e1f41db20ee45d5a0_7cd01df8.png)

LangSmith also makes the evaluation process accessible beyond the machine learning team. Product managers and operations specialists can define pass-or-fail criteria, write rubrics, and configure LLM judges directly. That brings the people who understand the support experience most deeply into the evaluation process rather than requiring engineers to translate every requirement for them.

Lyft has configured automations that send failed production traces into an [annotation queue](../langsmith/annotation-queues.md). Product managers and quality reviewers then label the failure mode in free-form language, turning individual bad interactions into structured product insights. Those findings feed back into prompts, workflows, datasets, and future offline tests.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a71492e1f41db20ee45d5a3_b3d0dc36.png)

#### What’s next

The team is now working toward a more standardized evaluation harness. Today, many offline tests still begin as one-off scripts or notebooks. Lyft wants to replace those with versioned primitives (e.g. tasks, datasets, personas, and scorers) that teams can share and run automatically.

That would make it possible to regression-test every prompt change, compare models on the same scenarios, and maintain an evaluation set that grows easily.

Over time, Lyft also sees these traces becoming more than evaluation data. Successful trajectories can become supervised fine-tuning examples. The longer-term goal is for production feedback to improve not only the prompts and workflows around the model, but also the model itself.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a714ac7f88c41e60d8f5650_Dev%20%E2%86%92%20Production%20Lifecycle%20v2%20(Eval%20Harness%20%2B%20Model%20Training)%402x%201.png)

The broader lesson from Lyft is that opening agent development to more people does not eliminate the need for rigor, but it shifts that rigor into the systems surrounding prompt creation, evaluation, and production feedback. The self-serve platform makes agents faster to build, while the eval flywheel makes them safe to ship and steadily better over time.

Learn more: Lyft User Story ([Blog](https://www.langchain.com/blog/lyft-built-a-self-serve-ai-agent-platform-for-customer-support-with-langgraph-and-langsmith)), Lyft Interrupt Talk ([YouTube](https://www.youtube.com/watch?v=UVeeNW_z068))

### **Fastweb + Vodafone: Two agents driving Customer Experience**

Fastweb + Vodafone, part of the Swisscom Group, serves millions of telecommunications customers across Italy. Customer service at that scale involves a wide range of needs, from billing and roaming to service activation and technical support, often with customers expecting resolution in a single interaction.

Its existing chatbot, TOBi, could handle straightforward requests, but more complex cases required deeper context, access to multiple systems, and coordination across several steps. Call-center consultants faced a similar challenge internally: they needed to quickly understand a customer’s history, identify the issue, and determine the right next action across multiple systems and knowledge sources.

Fastweb + Vodafone set out to support both sides of the experience: a customer-facing agent capable of resolving more complex requests end to end, and an internal agent that could help consultants work more quickly and consistently.

#### Agent architecture

Fastweb + Vodafone chose **LangGraph** and **LangChain **as the foundation for their AI transformation because their customer service process naturally mapped to a graph-based decision-making flow. Their implementation centers around two flagship projects: Super TOBi and Super Agent.

*Super TOBi*

Super TOBi is the agentic evolution of Fastweb + Vodafone’s existing chatbot. It now serves nearly 9.5 million customers across the Customer Companion App and voice channels, handling use cases such as cost control, active offers, roaming, sales, and billing.

The system has achieved a 90% correctness rate, an 82% resolution rate, and a Customer Effort Score of 5.2 out of 7, helping reduce response times and transfers to human operators.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a714aefeec9cb9d8d2b3940_Agent%20Architecture%20%E2%80%94%20LangSmith%20Tracing%402x%201.png)

Its architecture is organized around two types of LangGraph agents: a *Supervisor* and a set of specialized *Use Case* agents.

The* Supervisor *acts as the entry point for every request. It applies guardrails, validates and shapes the input, and handles common scenarios such as greetings, conversation endings, and handoffs to human operators. It then routes the request to the appropriate Use Case agent or asks a clarifying question when the intent is unclear.

Each *Use Case *agent is responsible for a specific category of customer need and has access to a defined set of APIs. Following the LLM Compiler pattern, it can determine which APIs to call, coordinate a multistep plan, and generate a response tailored to the customer’s context.

Some Use Case agents can also return structured action tags rather than only natural-language responses. These tags allow the chatbot to complete transactions directly in the conversation, such as activating an offer, disabling a service, or updating a payment method.

This allows Super TOBi to move beyond answering questions. It can plan and execute the steps required to resolve a request, combining dialogue, data retrieval, API calls, and transactional actions within the same interaction.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a714c141399fc5dd9151686_LLMCompiler%20Workflow%20Timeline%402x%201.png)

*Super Agent*

Super Agent is Fastweb + Vodafone’s internally facing AI system for call-center consultants. Unlike Super TOBi, it does not interact directly with customers. Instead, it gives consultants instant diagnostics, policy-compliant guidance, source-backed explanations, and a recommended next step. This approach has helped drive One-Call Resolution rates above 86%.

The system combines LangChain’s composable tools with LangGraph’s orchestration and stores operational knowledge in a living graph in Neo4j.

Business specialists begin by documenting troubleshooting and informational procedures in structured templates, defining the relevant steps, conditions, and actions. An automated pipeline built with LangGraph and task-specific agents then parses those documents, identifies the APIs needed to verify each step, checks the procedures for consistency, and refines the definitions.

The resulting content is stored in Neo4j as a knowledge graph, where procedural steps are linked to their conditions, actions, and supporting APIs. A CI/CD pipeline handles validation and deployment, allowing updated procedures to reach production within hours and without downtime.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a714b21c651a4e7b9757b80_ETL%20Pipeline%20%E2%86%92%20Neo4j%402x%201.png)

When a consultant submits a request, a LangGraph Supervisor first determines whether it matches a structured troubleshooting procedure or requires an open-ended answer. CRM data is injected at this stage so the system can identify the correct customer and tailor the response to their context.

For troubleshooting and fault-isolation requests, the Supervisor activates a procedural subgraph. The system retrieves the relevant procedure from Neo4j, then moves through it step by step. At each stage, it calls the required APIs to test the associated conditions. Once a condition is met, the system identifies the issue and generates a response using the prescribed action and the customer context gathered along the way. If no condition is met, it proceeds to the next step until it finds the likely problem and resolution.

Open-ended questions about company knowledge follow a different path. These are routed to a hybrid retrieval pipeline that combines a vector store with the Neo4j knowledge graph. The vector store retrieves a broad set of relevant passages, while the knowledge graph grounds the answer in the correct business context, adds source citations, and helps ensure the response follows company policy.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a714afb447b938c54579b25_Agent%20Architecture%20v2%20%E2%80%94%20Dual%20Use%20Case%402x%201.png)

#### Agent monitoring

Fastweb + Vodafone implemented LangSmith from day one of development, recognizing the critical importance of monitoring and evaluation in production AI systems.

*“You can’t run agentic systems in production without deep observability. LangSmith gave us end-to-end visibility into how our LangGraph workflows reason, route, and act, turning what would otherwise be a black box into an operational system we can continuously improve.” — Pietro Capra, Chat Engineering Chapter Lead, Fastweb + Vodafone*

The team has developed sophisticated evaluation processes that run daily, automatically classifying chatbot responses and providing structured feedback for continuous improvement:

Daily Evaluation Process:

- Collect traces in LangSmith datasets from daily interactions
- Perform automated evaluation using [LangSmith Evaluators SDK](../langsmith/manage-evaluators-sdk.md) during overnight processing
- Analyze user queries, chatbot responses, context, and grading guidelines
- Generate structured output including scores (1-5), explanations, and violated guidelines

This automated evaluation system enables business stakeholders to review daily performance metrics, provide strategic input, and communicate with the technical team to make prompt adjustments to maintain the 90% correctness rate target. The combination of automated monitoring and human oversight ensures Super TOBi consistently delivers value to customers while identifying areas for improvement.

*As Lucia Barbieri, Fastweb + Vodafone AI Customer Channels Lead, explains, “Automated evaluation has been crucial to scaling effectively, enabling us to quickly identify improvement areas and enhance experience, driving continuous growth and refinement.”*

#### What’s next

Fastweb + Vodafone continues expanding both Super TOBi and Super Agent capabilities while maintaining its core value proposition: delivering exceptional customer experiences through intelligent automation. Looking ahead, Fastweb + Vodafone plans to leverage its early success with LangGraph and LangSmith to explore building additional AI applications across its telecommunications operations.

Learn more: Fastweb + Vodafone User Story ([Blog](https://www.langchain.com/blog/customers-vodafone-italy))

### **LATAM Airlines: Building a feedback loop from conversations to knowledge**

LATAM is the largest airline in Latin America, transporting 87 million passengers a year while operating on margins of just 3%-5%. Fuel alone accounts for roughly 31 cents of every operating dollar. In that environment, tech infrastructure spending competes directly with the cost of operating flights, making efficiency a core part of the business model.

LATAM builds its agents on Cosmos, an internal AI platform that provides infrastructure, CI/CD, model access, reusable templates, and observability through **LangSmith**. Cosmos now supports more than 120 generative AI products across 20 business domains, including Concierge, LATAM’s customer-facing travel-planning agent.

Concierge lives in the LATAM app, where it helps passengers find flights, explore destinations and activities, and book hotels or rental cars. It reached 52,000 users in its first month of beta and, after more than a year in production, now serves roughly 4,000 daily active users.

#### Agent architecture

‍

*Concierge Agent*

The Concierge agent is built on** LangGraph** using a tool-per-agent architecture. A supervisor remains in control of the conversation and delegates work to specialists for flights, bookings, destinations, activities, insurance, trip planning, and customer care. Each specialist returns what it finds, while the supervisor synthesizes the information and formats the final response for the passenger.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a714b591dff583d3253d205_Supervisor%20Fan-out%20%E2%80%94%20Travel%20Agents%402x%20(1)%201.png)

This was not LATAM’s original design; Concierge initially used a triage agent that classified each request and handed control directly to the appropriate specialist. Each specialist then produced its own structured output, with its own schema and formatter prompt.

The system worked, but production traces in LangSmith showed that it was repeatedly structuring information even when no downstream component required it. LATAM measured roughly 15% overhead in latency and token consumption from this pattern.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a714b081399fc5dd914d6ee_Before%20%E2%80%94%20Multi-hop%20LLM%20Chain%402x%201.png)

The team redesigned the architecture so the supervisor remained in control and structured the output only once, immediately before returning the final response. The change preserved output quality while reducing cost by around 15%. While this inefficiency was difficult to spot in an aggregate dashboard, it became clear when the team examined individual traces.

Production conversations surfaced a second issue. 13% of messages were being classified as out of scope. The team initially assumed that users were testing the agent or asking unrelated questions. But when it reviewed the traces, it found that 95% of those messages reflected legitimate passenger needs, including questions about check-in, baggage, LATAM Pass, special services, and travel requirements.

LATAM then added a customer-care specialist to handle those requests, reducing the out-of-scope rate from 13% to 1%. The change also improved the return rate by 6%, and roughly 12% of daily messages now flow through the customer-care agent.

These findings demonstrated the value of trace-level observability, but they also revealed its limits. At tens of thousands of conversations a month, the question cannot remain only, “What happened in this conversation?” Teams also need to understand what is happening across the entire body of conversations: which topics drive escalations, what new needs are emerging, which interactions may predict churn, and what preferences passengers reveal along the way.

‍

*Compass Agent*

LATAM built Compass to answer those broader questions.

Compass is an ontology-driven pipeline that turns unstructured sources (agent conversations, UX research interviews, contact-center calls, and legal documents) into structured knowledge stored in BigQuery Graph.

The pipeline has three main stages. A parser prepares multimodal inputs for the model. A mapper uses Gemini to identify the entities and relationships defined by a domain-specific ontology. A modeler then writes that information into a knowledge graph. An ontology registry defines what the system should extract for each domain, while an evaluation layer measures the quality of the resulting semantic extractions.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a714b6c53cce7044f57780f_Pipeline%20%E2%80%94%20Parser%20_%20Mapper%20_%20Modeler%402x%201.png)

The same underlying pipeline can support very different use cases simply by changing the ontology. For UX research, the ontology might define pain points, feature requests, and user segments. For legal contracts, it might define parties, clauses, obligations, and expiration dates.

The model can be replaced or upgraded over time, while the ontology (the business-specific definition of what matters and how concepts relate) is the proprietary asset the company owns.

In one UX research workflow, Compass replaced a manual process in which teams prompted ChatGPT against individual transcripts and categorized the results in spreadsheets. Once the team defined the ontology, Compass could process each new transcript consistently and send the structured output directly to BigQuery. Work that previously took weeks now could be completed in days.

Across its active use cases, Compass has achieved ontology coverage of roughly 85% to 98%, processed around 8,000 documents, and reduced processing costs to approximately one cent per document.

Compass can also reveal where the business itself has not been precise about its categories. When extraction results are inconsistent, the issue may not be the model. Different teams may use the same term differently or lack a shared definition of how concepts relate. Building the ontology therefore becomes a way to clarify the organization’s own knowledge, not just extract it.

LATAM initially evaluated Spanner Graph as the system of record. Although it was technically well suited to the workload, most of the company’s existing data already lived in BigQuery. Maintaining both systems would have introduced federated queries, additional latency, and another operational dependency.

The team instead moved to BigQuery Graph, keeping the knowledge graph alongside the rest of LATAM’s data lake and allowing most users to query it through familiar columnar SQL. The decision reflected a broader principle: ecosystem reality matters more than technical purity.

#### What’s next

Compass is now beginning to connect signals across the passenger journey. Concierge contributes information about intent, destination, travel companions, and preferences before a trip. Contact-center conversations add issue types, resolutions, channels, policies, and follow-up actions during the day of travel. Future post-trip and next-trip interactions can add further context without requiring a new processing pipeline.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a714bddf88c41e60d8f8c28_Concierge%20%2B%20Contact%20Center%20%3D%20Knowledge%20Graph%402x%201.png)

The result is a shared graph in which every agent conversation contributes new knowledge and every agent can benefit from what the others learn. Agents interact with passengers, **LangSmith **shows what is and is not working, and Compass extracts structured intelligence from the resulting conversation corpus. That intelligence can then improve the agents and uncover opportunities beyond the original interaction.

Learn more: LATAM Interrupt Talk ([YouTube](https://www.youtube.com/watch?v=RnLCl3ilRgo))

## What's top of mind for customer experience agent builders

Five themes keep coming up with the CX teams we work with.

### 1. As agent development expands beyond engineering teams, prompt quality becomes the bottleneck

Once more people can build and configure agents, the primary challenge often shifts from infrastructure to instruction design. Domain experts understand the workflows, policies, and edge cases their agents need to handle, but translating that knowledge into prompts an LLM can follow consistently is a separate discipline. The difficulty is not getting the agent to work along the happy path, but rather making its behavior reliable across ambiguous requests, conflicting instructions, and uncommon scenarios.

Lyft encountered this shift after opening agent development to non-engineers. The platform, graph, and tool bindings were not the main constraint. The harder problem was helping domain experts turn their knowledge into precise, durable instructions. That led the team to introduce a structured prompt-writing framework and automated checks designed to catch contradictions and incomplete conversation paths before deployment.

Podium arrived at a similar approach, using structured, versioned prompts and reviewable evaluation datasets to make agent behavior easier to test and improve over time.

### 2. Observability needs to be in place before the feedback arrives

Once an agent reaches production, feedback accumulates quickly through user reactions, failed traces, tool errors, and incomplete resolutions. Without observability in place from the start, teams are left trying to figure out failures after the fact.

As adoption grows, manual review also stops scaling. Cisco addressed this by building a triage agent that pulls failing traces from LangSmith’s MCP server, groups related issues, and automatically opens Jira tickets. Humans still design and implement fixes, but they no longer have to sort through every trace manually.

Across these teams, observability became the foundation for turning production feedback into a repeatable improvement process.

### 3. Architecture is often discovered through production use

Agent architectures are usually designed around the workflows teams can anticipate before launch. Production exposes the rest: ambiguous requests, inefficient handoffs, unnecessary model calls, and use cases the system was not built to handle.

LATAM discovered through production traces that each specialist agent was independently formatting its own response, adding unnecessary latency and token usage. Moving to a supervisor pattern preserved quality while reducing cost. Lyft’s router-based architecture and its split between specialized and configurable agents evolved in a similar way, in response to constraints revealed by the previous system. In both cases, tracing helped to understand the tradeoffs. The architecture improved because the teams could see where cost, latency, and failures were accumulating.

### 4. The greatest value often appears when agents become part of the workflow

Chat is often the starting point, but agents become more valuable when they help carry out the work behind the conversation. That can mean guiding a representative to the next best action, coordinating a multistep process, or taking responsibility for recurring tasks. At that point, the agent is no longer just an interface, but has become part of the operating workflow.

Cisco describes this as moving from a chatbot to a “teammate” with responsibility for delegated tasks and workflows. Vodafone’s Super Agent follows a similar model, helping call-center consultants identify the right troubleshooting procedure and next step. The broader opportunity is not only to answer questions, but to embed agents into how customer issues are actually resolved.

### 5. Conversations are becoming a source of business intelligence

Customer conversations reveal more than the question being asked. They contain preferences, recurring problems, unmet needs, and gaps in existing products or services.

Historically, extracting those signals required manual sampling and categorization. Agents now make it more practical to analyze large volumes of unstructured conversations and turn them into structured data.

LATAM’s Compass pipeline does this across agent conversations, contact-center transcripts, UX interviews, and other sources. A passenger asking about an Italian restaurant, for example, may also reveal a destination, preference, trip context, and future need. At scale, these signals can inform product decisions, improve customer experience, and make other agents more effective. The conversation becomes a reusable source of knowledge.

## Closing

The most important shift in customer experience is that interactions can now be observed, evaluated, and improved continuously.

The teams making the most progress build the systems around the agent: structured prompts, realistic evaluations, trace-level observability, clear boundaries between deterministic workflows and model reasoning, and feedback loops that turn production behavior into better prompts, architectures, and products.

As these systems mature, the role of the agent expands as well. What begins as a conversational interface can become part of the operating workflow, help human teams make better decisions, and turn large volumes of unstructured interactions into reusable business intelligence.

The broader pattern emerging across customer experience is that an agent’s value comes not only from the conversations it can handle today, but from how effectively the system learns from those interactions and improves over time.

‍

‍
