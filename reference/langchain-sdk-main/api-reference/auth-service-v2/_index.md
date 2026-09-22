---
title: "api-reference/auth-service-v2"
description: "Index of 23 pages and 0 subdirectories under api-reference/auth-service-v2."
category: "index"
tags: [index, api-reference, auth-service-v2]
---

# api-reference/auth-service-v2

23 pages here.

## Files

- [Authenticate](authenticate.md) - Get OAuth token or start authentication flow if needed.
- [Check Oauth Token Exists](check-oauth-token-exists.md) - Return whether the current user has any tokens for a given provider (across agents).
- [Check Oauth Tokens Exist Batch](check-oauth-tokens-exist-batch.md) - Batch token-presence check: per requested provider, whether the current user has any token.
- [Check Workspace Slack Tokens Exist](check-workspace-slack-tokens-exist.md) - Check if the workspace has any Slack tokens.
- [Create Mcp Oauth Provider](create-mcp-oauth-provider.md) - Create an OAuth provider via MCP auto-discovery.
- [Create Oauth Provider](create-oauth-provider.md) - Create a new OAuth provider manually.
- [Delete Oauth Provider](delete-oauth-provider.md) - Delete an OAuth provider.
- [Delete Oauth Tokens For User](delete-oauth-tokens-for-user.md) - Delete all tokens for the current user for the given provider (across agents).
- [Delete Single Oauth Token](delete-single-oauth-token.md) - Delete a specific OAuth token, revoking it at the provider first.
- [Get Oauth Provider](get-oauth-provider.md) - Get a specific OAuth provider.
- [Get Platform Oauth Provider](get-platform-oauth-provider.md) - Get a platform-level OAuth provider available to all workspaces.
- [Import Oauth Token](import-oauth-token.md) - Persist a directly-obtained OAuth token (no authorization-code exchange).
- [List Oauth Providers](list-oauth-providers.md) - List OAuth providers.
- [List Oauth Tokens For User](list-oauth-tokens-for-user.md) - List the calling user's tokens for a provider.
- [List Platform Oauth Providers](list-platform-oauth-providers.md) - List platform-level OAuth providers available to all workspaces.
- [List Token Events For User](list-token-events-for-user.md) - List the calling user's OAuth connection audit events, newest first.
- [Oauth Callback Get](oauth-callback-get.md) - Handle OAuth callback redirect from OAuth providers.
- [Oauth Callback](oauth-callback.md) - Finalize an OAuth flow.
- [Oauth Setup Callback](oauth-setup-callback.md) - Handle OAuth setup callback redirect from GitHub Apps.
- [Revoke All Slack Tokens For Workspace](revoke-all-slack-tokens-for-workspace.md) - Revoke ALL Slack tokens for the workspace. Admin-only action that disconnects Slack entirely.
- [Update Oauth Provider](update-oauth-provider.md) - Update an OAuth provider.
- [Update Token Label](update-token-label.md) - Update a token's provider_account_label. Only the token owner can update.
- [Wait For Auth Completion](wait-for-auth-completion.md) - Wait for OAuth authentication completion.
