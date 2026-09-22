---
title: "LangChain + Zapier Natural Language Actions (NLA)"
description: "Connect LangChain agents to 5,000+ apps via Zapier&#39;s NLA API. Automate Gmail, Slack, Salesforce and more with natural language commands."
source: "https://www.langchain.com/blog/langchain-zapier-nla"
category: "blog"
published: "2023-03-16T14:48:06.000Z"
author: "LangChain Accounts"
tags: [blog, langchain-zapier-nla]
---

# LangChain + Zapier Natural Language Actions (NLA)

We are super excited to team up with Zapier and integrate their new [Zapier NLA API](https://zapier.com/l/natural-language-actions?ref=blog.langchain.com) into LangChain, which you can now use with your agents and chains. With this integration, you have access to the **5k+ apps and 20k+ actions** on Zapier's platform through a natural language API interface. This is extremely powerful and gives your LangChain agents seemingly limitless possibilities. Big shoutout to Mike Knoop and the rest of the Zapier team for helping with this integration. You can request access in the link shared above. What will you build?

# **Zapier NLA**

NLA supports apps like Gmail, Salesforce, Trello, Slack, Asana, HubSpot, Google Sheets, Microsoft Teams, and thousands more apps: [https://zapier.com/apps](https://zapier.com/apps?ref=blog.langchain.com)

Zapier NLA handles ALL the underlying API auth and translation from natural language -&gt; underlying API call -&gt; return simplified output for LLMs. The key idea is you expose a set of actions via an oauth-like setup window, which you can then query and execute via a REST API.

NLA offers both API Key and OAuth for signing NLA API requests.

1. Server-side (API Key): for quickly getting started, testing, and production scenarios where LangChain will only use actions exposed in the developer's Zapier account (and will use the developer's connected accounts on [Zapier.com](http://zapier.com/?ref=blog.langchain.com))
2. User-facing (Oauth): for production scenarios where you are deploying an end-user facing application and LangChain needs access to end-user's exposed actions and connected accounts on [Zapier.com](http://zapier.com/?ref=blog.langchain.com)

Review [full docs](https://nla.zapier.com/api/v1/dynamic/docs?ref=blog.langchain.com) or reach out to nla@zapier.com for user-facing oauth developer support.

# **LangChain Integration**

We've integrated Zapier NLA into a LangChain `Tool` and `Toolkit` in both Python ([docs](https://python.langchain.com/docs/modules/agents/tools/integrations/zapier?ref=blog.langchain.com)) and typescript ([docs](https://hwchase17.github.io/langchainjs/docs/modules/agents/zapier_agent?ref=blog.langchain.com)). This gives your agents and chains superpowers.

To use, simply retrieve an NLA API Key (see above), set the `ZAPIER_NLA_API_KEY` environment variable, then create a `Toolkit` and `agent`:

`llm = OpenAI(temperature=0)
zapier = ZapierNLAWrapper()
toolkit = ZapierToolkit.from_zapier_nla_wrapper(zapier)
agent = initialize_agent(toolkit.get_tools(), llm, agent="zero-shot-react-description", verbose=True)
`

‌It's really that simple! The `ZapierToolkit` automatically registers all of your enabled Zapier actions as tools with the correct name and descriptions.

You can also register an individual action as a tool manually using the `ZapierNLARunAction` tool.

To see this in action, look at the example below. This agent now has access to my email and slack, and is able to do some amazing feats. In this example, it’s summarizing the latest email I received from a certain bank and sending it to a slack channel.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb24bb02f04cb69c6086d_screenshot-2023-03-14-at-9.42.03-pm.png)

# **Next Steps**

We’re hoping to make this as seamless an integration as possible so let us know if you have any feedback for hit any issues!
