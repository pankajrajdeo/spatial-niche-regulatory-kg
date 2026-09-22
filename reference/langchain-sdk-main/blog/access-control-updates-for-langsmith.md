---
title: "Access Control Updates for LangSmith"
description: "LangSmith&#39;s Role Based Access Control (RBAC) helps enterprises manage resource access with custom roles and API keys."
source: "https://www.langchain.com/blog/access-control-updates-for-langsmith"
category: "blog"
published: "2024-05-08T15:30:00.000Z"
author: "LangChain Accounts"
tags: [blog, access-control-updates-for-langsmith]
---

# Access Control Updates for LangSmith

Access management can be a pain for large engineering teams as they build LLM applications. To avoid playing a game of whodunit or over/under-provisioning permissions, you need to systematically determine who can access your resources and to what capacity.

LangSmith now has new Access Control features to help enterprises manage access to their resources. This includes **Role Based Access Control (RBAC)**, which lets you specify custom roles and can better support users with limited permissions via API Keys.

## Role Based Access Control (RBAC)

💡

RBAC is currently only accessible for teams on the Enterprise plan. For more plan details, check out our [pricing page](https://www.langchain.com/pricing?ref=blog.langchain.com).

With Role Based Access Control (RBAC), administrators can now assign roles to users within their workspace or organization. Each role represents a group of permissions. By default, there are three built-in system roles:

- `Admin` - has full access to all resources within the workspace or organization
- `Viewer` - has read-only access to all resources within the workspace or organization
- `Editor` - has full permissions except for workspace management (adding/removing users, changing roles, configuring service keys)

A [workspace](https://docs.smith.langchain.com/concepts/admin?ref=blog.langchain.com#workspaces) logically groups together users and resources in an organization and you can now [set up a workspace](../langsmith/set-up-hierarchy.md) in LangSmith. This adds another layer of separation between the project and organization, helping isolate relevant resources to the right folks.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbafdb45ae5be594316da2_Screenshot-2024-05-07-at-4.57.30-PM.png)

Administrators can also create/edit custom roles with granular permissions on each set of LangSmith entities within a workspace or organization. This lessens the risk to vulnerabilities by reducing the surface area of what users can touch, such that users have just the permissions necessary to perform their job functions and critical tasks.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbafdb45ae5be594316dc0_Screenshot-2024-05-08-at-2.07.59-PM.png)

Get started with Role Based Access Control by [following these docs.](../langsmith/user-management.md)

## API Key Updates

To better support access control, there are now two types of API Keys: **Personal Access Tokens** and **Service Keys**.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbafdb45ae5be594316da5_Screenshot-2024-05-07-at-4.56.08-PM.png)

All users can create personal access tokens. Personal Access Tokens are attached to the user who creates them. These keys will have the same permissions as the user. Note that if a user is deleted from an organization, their personal access tokens will also be deleted. These keys are meant to be used by users when talking to the LangSmith API. These PATs are especially useful for users who cannot configure service keys, ensuring that non-admins can still access LangSmith via the API.

Service Keys are keys that act as service principals. These keys are granted administrator privileges and are meant to to be used by services that want to talk to the LangSmith API. (Additional permission configuration will be coming soon). Since these keys are associated with a service, they will not be impacted by organizational changes like users leaving. Only workspace admins will be able to create service keys.

[Read the docs](https://docs.smith.langchain.com/how_to_guides/setup/create_account_api_key?ref=blog.langchain.com) to get started with our new API keys.

💡

Old `ls__` API keys have been migrated to service keys. Note that we will be removing support for these `ls__` API keys on July 1st, 2024

**You can **[**try out these features on LangSmith**](https://smith.langchain.com/?ref=blog.langchain.com)** today. And feel free to reach out to us at ****support@langchain.dev**** for any questions or feedback!**
