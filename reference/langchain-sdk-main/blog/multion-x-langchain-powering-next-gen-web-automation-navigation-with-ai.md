---
title: "MultiOn x LangChain: Powering Next-Gen Web Automation &amp; Navigation with AI"
description: "Automate web tasks with MultiOn&#39;s AI agent for LangChain. Book flights, order dinner, fill forms &amp; navigate websites in just 3 lines of code."
source: "https://www.langchain.com/blog/multion-x-langchain-powering-next-gen-web-automation-navigation-with-ai"
category: "blog"
published: "2023-08-15T18:49:00.000Z"
author: "LangChain Accounts"
tags: [blog, multion-x-langchain-powering-next-gen-web-automation-navigation-with-ai]
---

# MultiOn x LangChain: Powering Next-Gen Web Automation &amp; Navigation with AI

*Editor's Note: This post was written in collaboration with *[*MultiOn*](https://www.multion.ai/?ref=blog.langchain.com)*. We're really excited about the way they're using Agents to* *automate and streamline online interactions. They are one of the first real world, production agent applications that we know of. Their integration with LangChain as a Toolkit makes it quick and easy to personalize and automate everyday web tasks.*

## MultiOn: Your Personal AI Agent Now on LangChain

Whether it's searching for information, filling out forms, or navigating complex websites, daily web tasks can often be tedious and time-consuming. That's why we're thrilled to introduce MultiOn, a next-generation personal AI assistant designed to interact with the web, to handle these tasks on your behalf.

Operating much like the sci-fi concept of JARVIS, MultiOn leverages cutting-edge AI technology to interact with your browser to perform tasks for you in real-time, from [ordering you dinner](https://youtu.be/2pF5SNhduTc?ref=blog.langchain.com), [booking flights](https://youtu.be/Lh6c8Evo-kY?ref=blog.langchain.com), [scheduling](https://youtu.be/KgH7I7Y59G8?ref=blog.langchain.com), finding information online, [to even filling out forms](https://youtu.be/zP0Ug9BVvhk?ref=blog.langchain.com). And the best part? MultiOn is now integrated directly within LangChain as a Toolkit, making it even easier to automate your everyday web tasks & build custom agents and applications that can take actions on the web.

## Seamless Integration with LangChain

With MultiOn directly integrated into LangChain, the power of Autonomous Web AI Agents is now at the fingertips of all users.

The integration unlocks numerous advantages. It provides LangChain users with an AI-powered tool that can automate a variety of everyday web tasks, from information retrieval to interaction with web services on their behalf. This integration not only enhances the functionality of LangChain but also takes the Action ability of agents to the next level - to now interact with any website!

Here is a glimpse of how you can use MultiOn within LangChain to interact with the website in just **3 Lines of Code 🔥:**

Import MultiOn as a LangChain Toolkit to add it to any custom Agent:

`# IMPORTS
from langchain import OpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.agents.agent_toolkits import MultionToolkit
import multion
multion.login() # MultiOn -&gt; Login to the MultiOn Website
# Initialize Agent
agent = initialize_agent(
 tools=MultionToolkit().get_tools(),
 llm=OpenAI(temperature=0),
 agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
 verbose = True
)
print(agent.run("Show Beautiful Pictures of New York"))
`

Get more samples at the [MultiOn API repository](https://www.google.com/url?q=https://github.com/MULTI-ON/api&sa=D&source=docs&ust=1692134001253806&usg=AOvVaw0xFKlpwYs8u8vulVJ77IvW).

LangChain Agent Demo:

Other

- [MultiOn Scheduler App](https://github.com/MULTI-ON/api/tree/main/examples/task_scheduler?ref=blog.langchain.com): Schedule recurring tasks that run periodically, such as “wishing happy birthday to friends on fb” everyday.
- [Group Dinner reservation Agent](https://github.com/MULTI-ON/api/tree/main/examples/restaurant-bot?ref=blog.langchain.com): Add MultiOn to a sms group chat and ask it to help book a group dinner on Opentable

## **Join the MultiOn Community!**

We’re very enthusiastic about the potential for Autonomous Web AI Agents, and more broadly, exploring new ways to harness the power of AI to improve online experiences. We believe that Actions are key to building powerful AI applications, and we want to empower developers & the open source community to build AI that can interact with the Web by building on top of MultiOn. Please check [our documentation](https://docs.multion.ai/?ref=blog.langchain.com), [contribute to adding examples](https://github.com/MULTI-ON/api/tree/main/examples?ref=blog.langchain.com), and join our Discord to experience the future of web task automation!

Stay tuned for more updates on our journey, and don't hesitate to reach us out at info@multion.ai if you have any questions or suggestions. We're always looking to hear from users and improve MultiOn to best serve your needs 🚀
