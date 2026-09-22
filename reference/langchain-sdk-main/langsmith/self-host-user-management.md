---
title: "Customize user management"
description: "This guide assumes you have read the admin guide and organization setup guide."
source: "https://docs.langchain.com/langsmith/self-host-user-management"
category: "docs"
tags: [docs, langsmith, self-host-user-management]
---

# Customize user management

> [!NOTE]
> This guide assumes you have read the [admin guide](administration-overview.md) and [organization setup guide](set-up-hierarchy.md#set-up-an-organization).

LangSmith offers additional customization features for user management using feature flags.

## Features

### Workspace level invites to an organization

The default behavior in LangSmith requires a user to be an Organization Admin in order to invite new users to an organization. For self-hosted customers that would like to delegate this responsibility to workspace Admins, a feature flag may be set that enables workspace Admins to invite new users to the organization as well as their specific workspace **at the workspace level**.

Once this feature is enabled via the configuration option below, workspace Admins may add new users in the `Workspace members` tab under `Settings` > `Workspaces`. Both of the following cases are supported when inviting at the workspace level, while the organization level invite functions the same as before.

1. Invite users who are NOT already active in the organization: this will add the users as pending to the organization and specific workspace
2. Invite users who ARE already active in the organization: adds the users directly to the workspace as an active member (no pending state).

Admins may invite users for both cases at the same time.

#### Configuration

**Helm**

```yaml
config:
  workspaceScopeOrgInvitesEnabled: true
```

### SSO new member login flow

As of helm **v0.11.10**, self-hosted deployments using OAuth SSO will no longer need to manually add members in LangSmith settings for them to join. Deployments will have a <b>default</b> organization, to which new users will automatically be added upon their first login to LangSmith.

For your **default** organization, you can set which workspace(s) and workspace role is assigned to new members. For **non-default** organizations, the invitation flow remains the same.
Once a user joins an organization, any changes to their workspaces or roles beyond the default organization settings must be managed either through LangSmith settings (as before) or via SCIM.

> [!NOTE]
> By default, all new users are added to the organization’s initially provisioned workspace (**Workspace 1** by default) with the **Workspace Editor** role.

<img src="https://mintcdn.com/langchain-5e9cc07a/QEp_iTXiY5U9rQvE/langsmith/images/sso-member-settings-update.png?fit=max&auto=format&n=QEp_iTXiY5U9rQvE&q=85&s=e7274ed7fdd47fe7c4c1f514d78f3ac7" alt="Update SSO Member Settings" width="1769" height="1251" data-path="langsmith/images/sso-member-settings-update.png" />

> [!NOTE]
> To change your default organization, use **Set Default Organization** in the organization selector dropdown. (Org Admin permissions required in both the source and target organization.)

### SSO Groups Sync

> [!NOTE]
> SSO Groups Sync on self-hosted requires LangSmith chart version **0.15.0-rc.3** (application version **0.15.2rc1**) or later.

[SSO Groups Sync](user-management.md#sso-groups-sync-alternative) reads group memberships from the OIDC ID token and assigns org and workspace roles using the [SCIM naming convention](user-management.md#group-naming-convention). It is a simpler alternative to [SCIM](user-management.md#set-up-scim-for-your-organization) for self-hosted organizations whose IdP can include groups in the OIDC token but cannot easily run SCIM provisioning.

For IdP-side configuration (claim, scope) refer to the [SSO Groups Sync section in the OIDC SSO setup guide](self-host-sso.md#sso-groups-sync). For settings reference and behavior, see the [main SSO Groups Sync documentation](user-management.md#sso-groups-sync-alternative).

### Disabling organization creating

By default, any user can create an organization in LangSmith. For self-hosted customers, an admin may want to restrict this ability after setting up initial organizations. This feature flag allows an admin to disable the ability for users to create new organizations.

#### Configuration

> [!NOTE]
> The `userOrgCreationDisabled` feature flag is set to `true` by default for organizations using [basic auth](self-host-basic-auth.md) or [SSO](self-host-sso.md).

**Helm**

```yaml
config:
  userOrgCreationDisabled: true
```

### Disabling personal organizations

By default, any user who logs in to LangSmith will have a personal organization created for them. For self-hosted customers, an admin may want to restrict this ability. This feature flag allows an admin to disable the ability for users to create personal organizations.

#### Configuration

> [!NOTE]
> The `personalOrgsDisabled` feature flag is set to `true` by default for organizations using [basic auth](self-host-basic-auth.md) or [SSO](self-host-sso.md).

**Helm**

```yaml
config:
  personalOrgsDisabled: true
```

### Disabling personal access token creation

> [!NOTE]
> This feature requires Helm chart version 0.13.12 (application version 0.13.12) or later.

By default, users can create Personal Access Tokens (PATs) in any organization. For self-hosted customers, an admin may want to globally disable PAT creation across all organizations. This environment variable allows an admin to prevent users from creating new PATs in any organization on the instance.

To disable PAT creation for a single organization instead, see the [per-organization API option](manage-organization-by-api.md#security-settings).

#### Configuration

**Helm**

```yaml
commonEnv:
  - name: PAT_CREATION_DISABLED
    value: "true"
```

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/self-host-user-management.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
