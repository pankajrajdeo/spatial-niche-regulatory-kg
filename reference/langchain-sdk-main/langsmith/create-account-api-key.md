---
title: "Create an account and API key"
description: "To get started with LangSmith, you need to create an account. You can sign up for a free account in the LangSmith UI. LangSmith supports sign in with Google, GitHub, and email."
source: "https://docs.langchain.com/langsmith/create-account-api-key"
category: "docs"
tags: [docs, langsmith, create-account-api-key]
---

# Create an account and API key

To get started with LangSmith, you need to create an account. You can sign up for a free account in the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-create-account-api-key). LangSmith supports sign in with Google, GitHub, and email.

## API keys

LangSmith supports two types of API keys. You can use both types of token to authenticate requests to the LangSmith API, but they have different use cases:

* [**Personal Access Tokens (PATs)**](administration-overview.md#personal-access-tokens-pats) inherit the permissions of the user who created them. Use PATs for personal scripts or tools.
* [**Service keys**](administration-overview.md#service-keys) scope to specific [workspaces](administration-overview.md#workspaces) or the entire [organization](administration-overview.md#organizations). Use service keys for applications and production services.

To log [traces](observability-concepts.md#traces) and run [evaluations](evaluation.md) with LangSmith, create an API key to authenticate your requests.

### Open API Keys settings
Navigate to the [**Settings** page](https://smith.langchain.com/settings) and select the **API Keys** section.

### Configure the key type
For service keys, choose between an organization-scoped and workspace-scoped key. If the key is workspace-scoped, you must specify the workspaces.

[Enterprise](pricing-plans.md) users can also [assign specific workspace roles](administration-overview.md#workspace-roles-rbac) to service keys, which adjusts their permissions independently of any user.

### Set expiration
Set the key's expiration. The key becomes unusable after the number of days chosen, or never, if that is selected.

### Create the key
Click **Create API Key.** LangSmith will display the API key only once, so make sure to copy it and store it in a safe place.

> [!TIP]
> To revoke or delete a key, navigate to the [**Settings** page](https://smith.langchain.com/settings), find the key in the **API Keys** section, and select the trash icon  in the **Actions** column. For a personal access token, type the key's name, then select **Revoke** to stop the token from authenticating while keeping its record, or **Delete** to remove the record entirely. Neither action can be undone. Service keys can only be deleted.

> [!TIP]
> [Organization Admins](rbac.md#organization-admin) and [Organization Operators](rbac.md#organization-operator) can view, revoke, and delete every member's personal access tokens. In the **API Keys** section of the [**Settings** page](https://smith.langchain.com/settings), open the **Personal** tab and switch the scope from **My keys** to **All members**.

> [!TIP]
> [Enterprise](pricing-plans.md) Organization Admins can edit the [role](administration-overview.md#workspace-roles-rbac) on an existing service key without rotating the key. On the [**Settings** page](https://smith.langchain.com/settings) **API Keys** section, switch to the **Service** tab and click any service key row to open the edit dialog. Update the workspace role (and, for organization-scoped keys, the org role) and click **Save**. The key string itself is unchanged.

## Configure the SDK

Install the SDK for your language:

#### Python
**pip**

```bash
pip install langsmith
```

**uv**

```bash
uv add langsmith
```

#### TypeScript
```bash
npm install langsmith
```

For full details, refer to the [Python SDK](smith-python-sdk.md) or [JS/TS SDK](smith-js-ts-sdk.md) reference.

Then, set your API key and enable tracing:

```bash
export LANGSMITH_API_KEY=<your-api-key>
export LANGSMITH_TRACING=true
```

You may also need the following additional environment variables:

* `LANGSMITH_ENDPOINT` controls which LangSmith server the SDK sends data to. It defaults to `https://api.smith.langchain.com` (GCP US). Set it only if you are on a different deployment. For regional SaaS, set it to the API URL for your region:

  <table>
    <thead>
      <tr>
        <th>Region</th>

        <th>
          {protocol_0 === false ? "Host" : "URL"}
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td>GCP US</td>

        <td>
          <code>
            {`${protocol_0 === false ? "" : "https://"}${prefix_0 || "api.smith"}.langchain.com${suffix_0 || ""}`}
          </code>
        </td>
      </tr>

      <tr>
        <td>GCP EU</td>

        <td>
          <code>
            {`${protocol_0 === false ? "" : "https://"}eu.${prefix_0 || "api.smith"}.langchain.com${suffix_0 || ""}`}
          </code>
        </td>
      </tr>

      <tr>
        <td>GCP APAC</td>

        <td>
          <code>
            {`${protocol_0 === false ? "" : "https://"}apac.${prefix_0 || "api.smith"}.langchain.com${suffix_0 || ""}`}
          </code>
        </td>
      </tr>

      <tr>
        <td>AWS US</td>

        <td>
          <code>
            {`${protocol_0 === false ? "" : "https://"}aws.${prefix_0 || "api.smith"}.langchain.com${suffix_0 || ""}`}
          </code>
        </td>
      </tr>
    </tbody>
  </table>

* `LANGSMITH_WORKSPACE_ID` is required only if your API key is scoped to more than one [workspace](administration-overview.md#workspaces). Find your Workspace ID on the [**Settings** page](https://smith.langchain.com/settings) under **General**:

  `LANGSMITH_WORKSPACE_ID=`

To reuse endpoint, API key, and workspace settings across local shells or remote runtimes, refer to [Profile configuration](profile-configuration.md).

## Use API keys outside of the SDK

See [instructions for managing your organization via API](manage-organization-by-api.md).

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/create-account-api-key.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
