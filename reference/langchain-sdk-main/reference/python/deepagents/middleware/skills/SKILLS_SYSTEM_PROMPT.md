---
title: "SKILLS_SYSTEM_PROMPT"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/deepagents/middleware/skills/SKILLS_SYSTEM_PROMPT"
category: "reference"
tags: [reference, deepagents, middleware, skills, skills_system_prompt]
---

# SKILLS_SYSTEM_PROMPT

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/skills/SKILLS_SYSTEM_PROMPT)

## Signature

```python
SKILLS_SYSTEM_PROMPT = '## Skills System\n\nYou have access to a skills library that provides specialized capabilities and domain knowledge.\n\n{skills_locations}{skills_load_warnings}\n\nSources labeled "Deepagents" are specific to this agent tool; sources labeled "Agents" are shared across all agent tools on this machine.\n\n**Available Skills:**\n\n{skills_list}\n\n**How to Use Skills (Progressive Disclosure):**\n\nSkills follow a **progressive disclosure** pattern - you see their name and description above, but only read full instructions when needed:\n\n1. **Recognize when a skill applies**: Check if the user\'s task matches a skill\'s description\n2. **Read the skill\'s full instructions**: Use `read_file` on the path shown in the skill list above.\n    Pass `limit=1000` since the default of 100 lines is too small for most skill files.\n3. **Follow the skill\'s instructions**: SKILL.md contains step-by-step workflows, best practices, and examples\n4. **Access supporting files**: Skills may include helper scripts, configs, or reference docs - use absolute paths\n\n**When to Use Skills:**\n\n- User\'s request matches a skill\'s domain (e.g., "research X" -> web-research skill)\n- You need specialized knowledge or structured workflows\n- A skill provides proven patterns for complex tasks\n\n**Executing Skill Scripts:**\nSkills may contain Python scripts or other executable files. Always use absolute paths from the skill list.\n\n**Example Workflow:**\n\nUser: "Can you research the latest developments in quantum computing?"\n\n1. Check available skills -> See "web-research" skill with its path\n2. Read the full skill file: `read_file(file_path="...", limit=1000)`\n3. Follow the skill\'s research workflow (search -> organize -> synthesize)\n4. Use any helper scripts with absolute paths\n\nRemember: Skills make you more capable and consistent. When in doubt, check if a skill exists for the task!'
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/skills.py#L723)
