---
title: "How Klarna&#39;s AI assistant redefined customer support at scale for 85 million active users"
description: "Klarna&#39;s AI assistant is revolutionizing the personal shopping experience, including customer service and productivity. See how they used LangGraph and LangSmith to achieve 80% faster customer..."
source: "https://www.langchain.com/blog/customers-klarna"
category: "blog"
published: "2025-02-12T15:00:55.000Z"
author: "LangChain Accounts"
tags: [blog, customers-klarna]
---

# How Klarna&#39;s AI assistant redefined customer support at scale for 85 million active users

[Klarna](https://www.klarna.com/?ref=blog.langchain.com) has reshaped global commerce with its consumer-centric, AI-powered payment and shopping solutions. With over 85 million active users and 2.5 million daily transactions on its platform, Klarna is a fintech leader that simplifies shopping while empowering consumers with smarter, more flexible financial solutions.

Klarna’s flagship AI Assistant is revolutionizing the shopping and payments experience. Built on [LangGraph](https://langchain.com/langgraph?ref=blog.langchain.com) and powered by [LangSmith](https://www.langchain.com/langsmith?ref=blog.langchain.com), the AI Assistant handles tasks ranging from customer payments, to refunds, to other payment escalations.

With 2.5 million conversations to date, the AI Assistant is more than just a chatbot; it’s a transformative [agent](../oss/langchain/agents.md) that performs the work equivalent of 700 full-time staff, delivering results quickly and improving company efficiency.

## **The Challenge: Scaling Customer Support & Handling Escalations**

### **Overcoming escalation overload**

Klarna faced growing challenges in managing multi-departmental escalations. To meet rising consumer expectations, Klarna needed a solution that could combine speed, accuracy, and accessibility while scaling across global markets.

> *"LangChain has been a great partner in helping us realize our vision for an AI-powered assistant, scaling support and delivering superior customer experiences across the globe."*— **Sebastian Siemiatkowski**, CEO and Co-Founder, Klarna

## **The Solution: Powered by LangGraph and LangSmith**

### **A partnership driving precision and performance**

Klarna turned to LangGraph and LangSmith to evolve their AI Assistant into a reliable, scalable [multi-agent](../langchain/multi-agent.md) system. Key improvements included:

1. **Controllable agent architecture**: Klarna’s AI assistant [routed requests and handled different tasks](../langgraph/workflows-agents.md) using the LangGraph framework. This helped decrease latency, improve reliability, and cut operational costs.
2. **Context-aware intelligence**: By dynamically [tailoring prompts](../langsmith/prompt-engineering.md) to specific scenarios, Klarna ensured that their AI assistant consistently delivered relevant, context-aware responses while reducing token costs and latency.
3. **Test-driven development**: With LangSmith, Klarna could [pinpoint what issues arose by seeing step-by-step how their AI assistant behaved](../langsmith/observability.md). Leveraging LangSmith, Klarna rigorously tested critical use cases for their AI assistant, then validated and refined agent performance with [LLM evaluations](../langsmith/evaluation.md) and prompt iteration.
4. **Prompt optimization: **Klarna’s insights in turn improved LangSmith’s prompt engineering features – notably, Klarna helped inspire and design advanced capabilities like meta-prompting. Meta-prompting allows users to suggest specific improvements to the prompts,* by prompting them* and seeing how the optimized prompt impacted response quality.

## **The Impact**

Built with LangGraph and refined with LangSmith, Klarna’s AI assistant has empowered their teams to handle customer escalations more effectively. They’ve achieved the following results in the past 9 months:

- **Faster resolutions**: Reduced average customer query resolution time by 80%, enabling faster responses to user queries and saving analysts and engineers hours a week of investigation time.
- **Increased AI automation for chat handling**: Automated ~70% of repetitive support tasks, freeing up customer service agents to handle complex, high-value interactions
- **Improved accuracy**: Improved root cause identification for rejection, leading to a significant reduction in customer escalations.
