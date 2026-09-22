---
title: "How to design an Agent for Production"
description: "Build production-ready AI agents with LangChain. Technical guide covering OpenAI functions, tools, prompts, and architecture for Cal.ai&#39;s scheduling assistant."
source: "https://www.langchain.com/blog/how-to-design-an-agent-for-production"
category: "blog"
published: "2023-10-15T19:25:59.000Z"
author: "LangChain Accounts"
tags: [blog, how-to-design-an-agent-for-production]
---

# How to design an Agent for Production

***Editor's Note: This post is written by ***[***Dexter Storey***](https://twitter.com/StoreyDexter?ref=blog.langchain.com)***, ***[***Sarim Malik***](https://twitter.com/sarimrmalik?ref=blog.langchain.com)***, and ***[***Ted Spare***](https://twitter.com/TedSpare?ref=blog.langchain.com)*** from the ***[***Rubric Labs***](https://rubriclabs.com)*** team. ***

# Important Links

- [GitHub repository](https://github.com/calcom/cal.com/tree/main/apps/ai?ref=blog.langchain.com)
- [OpenAI Functions Agent by LangChain](https://js.langchain.com/docs/modules/agents/agent_types/openai_functions_agent?ref=blog.langchain.com)
- [Install Cal.ai](https://app.cal.com/apps/cal-ai?ref=blog.langchain.com)

# Goal

The purpose of this guide is to explain the underlying tech and logic used to deploy a scheduling agent, [Cal.ai](http://cal.ai/?ref=blog.langchain.com), in production using [LangChain](https://www.langchain.com/?ref=blog.langchain.com).

# Context

Recently, our team at [Rubric Labs](https://rubriclabs.com) had the opportunity to build [Cal.com](https://cal.com/?ref=blog.langchain.com)'s AI-driven email assistant. For context, we’re a team of builders who love to tackle challenging engineering problems.

The vision for the project was to simplify the complex world of calendar management. Some of the core features we had in mind included:

- **Turning informal emails into bookings:** "Want to meet tomorrow at 2?"
- **Listing and rearranging bookings:** "Cancel my next meeting"
- **Answering basic questions:** "How does my Tuesday look?"

and more. In summary, we wanted to build a personal, AI-powered scheduling assistant that can offer a complete suite of [CRUD](https://www.codecademy.com/article/what-is-crud?ref=blog.langchain.com) operations to the end user, all within the confines of their email client using natural language.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb129504e43f6295a2d4c_Untitled--11-.png)Emailing [Cal.ai](http://cal.ai/?ref=blog.langchain.com)

# Architecture

We decided to achieve this using an AI agent, particularly an [OpenAI functions agent](https://js.langchain.com/docs/modules/agents/agent_types/openai_functions_agent?ref=blog.langchain.com) which is better at dealing with structured data, given [Cal.com's API](https://cal.com/docs/enterprise-features/api/api-reference?ref=blog.langchain.com) exposes a set of booking operations with clear inputs. The underlying architecture is explained below.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb129504e43f6295a2d43_Untitled--12-.png)Agent architecture. A scratchpad is a type of memory where the AI tries to write itself.

## Input

A [Cal.com](http://cal.com/?ref=blog.langchain.com) user may email `username@cal.ai` (e.g ted@cal.ai) with a request such as “Can you book a meeting with sarim@rubriclabs.com sometime tomorrow?”.

The incoming email is cleaned and routed in the [receive route](https://github.com/calcom/cal.com/blob/main/apps/ai/src/app/api/receive/route.ts?ref=blog.langchain.com) using [MailParser](https://nodemailer.com/extras/mailparser/?ref=blog.langchain.com) and the addresses are verified by [DKIM record](https://support.google.com/a/answer/174124?hl=en&ref=blog.langchain.com), making it hard to spoof them.

Here we also make additional checks, such as ensuring that the email is from a [Cal.com](http://cal.com/?ref=blog.langchain.com) user to prevent misuse. After the email has been verified and parsed, it is passed to the agent loop.

## Agent

The agent is a LangChain [OpenAI functions agent](https://js.langchain.com/docs/modules/agents/agent_types/openai_functions_agent?ref=blog.langchain.com) which uses fine-tuned versions of GPT models. This agent is passed pre-defined functions or tools and is able to detect when a function should be called. This allows us to specify the required inputs and desired output.

The agent is documented in [the agent loop](https://github.com/calcom/cal.com/blob/main/apps/ai/src/app/api/agent/route.ts?ref=blog.langchain.com).

There are two required inputs for an OpenAI functions agent:

1. Tools — a tool is simply a Javascript function with a name, description, and input schema
2. Chat model — a [chat model](https://python.langchain.com/docs/modules/model_io/models/chat/?ref=blog.langchain.com) is a variation of an LLM model that uses an interface where "chat messages" are the inputs and outputs

In addition to the tools and the chat model, we also pass a prefix prompt to add context for the model. Let’s look into each of the inputs.

👉

Let’s use an analogy for clarity. The agent is an electrician named Peer. Peer is unlike any other electrician, Peer has access to deep intelligence using years of training and learning (the model). However, when presented with a problem (the input), Peer’s work (the output) doesn’t always align with the client’s expectations. One day, a client name Bailey decides to hire Peer and offers him a limited set of tools — a soldering gun, battery, wires, and bulb. Peer uses his knowledge and the provided tools to come up with a solution exactly aligned with Bailey’s expectations.

### Prompt

A prompt is a way to program the model by providing context. The user’s information (`userId`, `user.username`, `user.timezone`, etc.) is used to construct a prompt which is passed to the agent.

`const prompt = `You are Cal.ai - a bleeding edge scheduling assistant that interfaces via email.
Make sure your final answers are definitive, complete and well formatted.
Sometimes, tools return errors. In this case, try to handle the error
intelligently or ask the user for more information.
Tools will always handle times in UTC, but times sent to users should be
formatted per that user's timezone.

The primary user's id is: ${userId}
The primary user's username is: ${user.username}
The current time in the primary user's timezone is: ${now(user.timeZone)}
The primary user's time zone is: ${user.timeZone}
The primary user's event types are: ${user.eventTypes}
The primary user's working hours are: ${user.workingHours}
...
``

find the full prompt [here](https://github.com/calcom/cal.com/blob/59faffe0d5596f3b1e14ff34ab9fcbbdea8ed616/apps/ai/src/utils/agent.ts?ref=blog.langchain.com#L52C7-L52C13).

### Chat Model

A [chat model](https://js.langchain.com/docs/modules/model_io/models/chat/?ref=blog.langchain.com) is a variation of a language model which exposes chat messages as the input and output. For this project, we use the `GPT-4` model by OpenAI which can be accessed using an `OPENAI_API_KEY` ([read here](https://platform.openai.com/docs/api-reference/authentication?ref=blog.langchain.com) to generate an API key).

For better adoption, we knew that the user experience had to be lightning fast. We experimented with `gpt-3.5-turbo` but, interestingly, it would often take longer overall by completing tasks in more roundabout ways.

The [temperature](https://platform.openai.com/docs/guides/gpt/how-should-i-set-the-temperature-parameter?ref=blog.langchain.com) is set to 0 to generate more consistent output. A higher temperature leads to a more creative, inconsistent output.

`const model = new ChatOpenAI({
 modelName: "gpt-4",
 openAIApiKey: env.OPENAI_API_KEY,
 temperature: 0,
 });`

### Tools

A tool is composed of a Javascript function, name, input schema (using [Zod](https://github.com/colinhacks/zod?ref=blog.langchain.com)), and description, and is designed to work with structured data.

The tools used for this project are of type [DynamicStructuredTool](https://js.langchain.com/docs/api/tools/classes/DynamicStructuredTool?ref=blog.langchain.com) which are designed to work with structured data. A dynamic structured tool is an extension of LangChain’s `StructuredTool` class which basically overrides the `_call` method with the function provided. See the schema below for a `DynamicStructuredTool`.

`DynamicStructuredTool({
 description: "Creates a booking on the primary user's calendar.", // Description
 func: createBooking(), // Function
 name: "createBooking", // Name
 schema: z.object({ // Schema
 from: z.string().describe("ISO 8601 datetime string"),
 ...
 }),
 });`

Inputs for a DynamicStructuredTool, [the complete example can be seen here](https://github.com/calcom/cal.com/blob/a87d82fd4731dd163fd227da2dcc10c301c2e31a/apps/ai/src/tools/createBooking.ts?ref=blog.langchain.com#L85)

By creating a suite of tools, we are giving the agent extra capabilities to perform pre-defined actions. [All tools used for this project are documented here](https://github.com/calcom/cal.com/tree/main/apps/ai/src/tools?ref=blog.langchain.com) and listed below. Each tool has complex logic that allows it to understand the user’s request, interact with the [Cal.com](http://cal.com/?ref=blog.langchain.com) API by performing a CRUD task, and handle the response.

`const tools = [
 createBooking(apiKey, userId, users),
 deleteBooking(apiKey),
 getAvailability(apiKey),
 getBookings(apiKey, userId),
 sendBookingLink(apiKey, user, users, agentEmail),
 updateBooking(apiKey, userId),
];`

The inputs to the tools above are variables we don’t want the AI agent to have access to and thus, they are injected to the tool, bypassing the agent loop.

Using the dynamic prompt and the chat model, the tool parser is able to select the most appropriate tool to handle the user’s request and then run in a loop until it’s able to meet the desired behaviour. This follows iterative learning, even allowing fallbacks by picking an alternative tool in case there is an error.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb129504e43f6295a2d4f_Untitled--13-.png)tools architecture

### Executor

Finally, the tools, chat model, and prompt are used to [initialize an agent](https://js.langchain.com/docs/modules/agents/agent_types/openai_functions_agent?ref=blog.langchain.com) and run the executor to generate a response.

`const executor = await initializeAgentExecutorWithOptions(tools, model, {
 agentArgs: { prefix: prompt },
 agentType: "openai-functions",
 verbose: true,
});`

## Response

After the agent runs through a loop utilizing the different tools, chatting with LLM model and interacting with the [Cal.com](http://cal.com/?ref=blog.langchain.com) API, it comes to an end and concludes with a final response. This response is then emailed to the user using an emailing service, such as [Sendgrid](https://sendgrid.com/?ref=blog.langchain.com) or [Resend](https://resend.com/?ref=blog.langchain.com). The email will either be a confirmation or an error.

# Tech Stack

- [Typescript](https://www.typescriptlang.org/?ref=blog.langchain.com)
- [Next.js 13](https://nextjs.org/?ref=blog.langchain.com)
- [Vercel Serverless Functions](https://vercel.com/docs/functions/serverless-functions?ref=blog.langchain.com)
- [LangChain](https://www.langchain.com/?ref=blog.langchain.com)
- [OpenAI GPT-4](https://openai.com/research/gpt-4?ref=blog.langchain.com)
- [Zod](https://zod.dev/?ref=blog.langchain.com)
- [Sendgrid](https://sendgrid.com/?ref=blog.langchain.com)
- [Cal.com API](https://cal.com/docs/enterprise-features/api/api-reference?ref=blog.langchain.com)

# Conclusion

It’s clear that AI agents with scoped tools is a really powerful combination. Combining the knowledge of an LLM model with structured tools helps tackle natural language problems with structured data, increasing the reliability of said agents. We’re extremely excited about the future of AI agents as they continue to evolve and hope that our partnership with [Cal.com](http://cal.com/?ref=blog.langchain.com) and LangChain to create an open-source agent in production will serve as a template for future projects.

💬

If you have feedback on this post, please reach out to us at *hello@rubriclab.com*
