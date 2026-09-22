---
title: "langsmith/smith-api/orgs"
description: "Index of 57 pages and 0 subdirectories under langsmith/smith-api/orgs."
category: "index"
tags: [index, langsmith, smith-api, orgs]
---

# langsmith/smith-api/orgs

57 pages here.

## Files

- [Add basic auth members to current org](add-basic-auth-members-to-current-org.md) - Batch add up to 500 users to the org and specified workspaces in basic auth mode.
- [Add member to current org](add-member-to-current-org.md) - /langsmith/langsmith-platform-openapi.json post /api/v1/orgs/current/members
- [Add members to current org batch](add-members-to-current-org-batch.md) - Batch invite up to 500 users to the current org.
- [Change payment plan](change-payment-plan.md) - /langsmith/langsmith-platform-openapi.json post /api/v1/orgs/current/plan
- [Claim pending organization invite](claim-pending-organization-invite.md) - /langsmith/langsmith-platform-openapi.json post /api/v1/orgs/pending/{organization_id}/claim
- [Create customers and get stripe setup intent](create-customers-and-get-stripe-setup-intent.md) - /langsmith/langsmith-platform-openapi.json post /api/v1/orgs/current/setup
- [Create org personal access token](create-org-personal-access-token.md) - /langsmith/langsmith-platform-openapi.json post /api/v1/orgs/current/personal-access-tokens
- [Create org service key](create-org-service-key.md) - Create org-scoped service key. If workspaces is None, key is org-wide.
- [Create organization roles](create-organization-roles.md) - /langsmith/langsmith-platform-openapi.json post /api/v1/orgs/current/roles
- [Create organization](create-organization.md) - /langsmith/langsmith-platform-openapi.json post /api/v1/orgs
- [Create SSO settings](create-sso-settings.md) - Create SSO provider settings for the current organization.
- [Create stripe account links endpoint](create-stripe-account-links-endpoint.md) - Kick off a Stripe account link flow.
- [Create stripe checkout sessions endpoint](create-stripe-checkout-sessions-endpoint.md) - Kick off a Stripe checkout session flow.
- [Delete current org pending member](delete-current-org-pending-member.md) - When an admin deletes a pending member invite.
- [Delete org personal access token](delete-org-personal-access-token.md) - Delete a personal access token, removing the record entirely.
- [Delete org service key](delete-org-service-key.md) - /langsmith/langsmith-platform-openapi.json delete /api/v1/orgs/current/service-keys/{api_key_id}
- [Delete organization roles](delete-organization-roles.md) - /langsmith/langsmith-platform-openapi.json delete /api/v1/orgs/current/roles/{role_id}
- [Delete pending organization invite](delete-pending-organization-invite.md) - /langsmith/langsmith-platform-openapi.json delete /api/v1/orgs/pending/{organization_id}
- [Delete SSO settings](delete-sso-settings.md) - Delete SSO provider settings for the current organization.
- [Export granular usage csv](export-granular-usage-csv.md) - Export granular usage data as CSV.
- [Get company info](get-company-info.md) - /langsmith/langsmith-platform-openapi.json get /api/v1/orgs/current/business-info
- [Get current active org members](get-current-active-org-members.md) - /langsmith/langsmith-platform-openapi.json get /api/v1/orgs/current/members/active
- [Get current org members](get-current-org-members.md) - /langsmith/langsmith-platform-openapi.json get /api/v1/orgs/current/members
- [Get current organization info](get-current-organization-info.md) - /langsmith/langsmith-platform-openapi.json get /api/v1/orgs/current/info
- [Get current pending org members](get-current-pending-org-members.md) - /langsmith/langsmith-platform-openapi.json get /api/v1/orgs/current/members/pending
- [Get current SSO settings](get-current-sso-settings.md) - Get SSO provider settings for the current organization.
- [Get current user login methods](get-current-user-login-methods.md) - Get login methods for the current user.
- [Get dashboard](get-dashboard.md) - /langsmith/langsmith-platform-openapi.json get /api/v1/orgs/current/dashboard
- [Get granular usage](get-granular-usage.md) - Get granular usage data with flexible grouping.
- [Get org usage](get-org-usage.md) - /langsmith/langsmith-platform-openapi.json get /api/v1/orgs/current/billing/usage
- [Get organization billing info](get-organization-billing-info.md) - /langsmith/langsmith-platform-openapi.json get /api/v1/orgs/current/billing
- [Get organization info](get-organization-info.md) - /langsmith/langsmith-platform-openapi.json get /api/v1/orgs/current
- [List all org personal access tokens](list-all-org-personal-access-tokens.md) - List every organization member's personal access tokens.
- [List org members with workspace roles](list-org-members-with-workspace-roles.md) - Returns a paginated list of org members (active and pending) enriched with workspace memberships.
- [List org personal access tokens](list-org-personal-access-tokens.md) - /langsmith/langsmith-platform-openapi.json get /api/v1/orgs/current/personal-access-tokens
- [List org service keys](list-org-service-keys.md) - /langsmith/langsmith-platform-openapi.json get /api/v1/orgs/current/service-keys
- [List organization roles](list-organization-roles.md) - /langsmith/langsmith-platform-openapi.json get /api/v1/orgs/current/roles
- [List organizations](list-organizations.md) - Get all orgs visible to this auth
- [List pending organization invites](list-pending-organization-invites.md) - Get all pending orgs visible to this auth
- [List permissions](list-permissions.md) - /langsmith/langsmith-platform-openapi.json get /api/v1/orgs/permissions
- [List TTL settings](list-ttl-settings.md) - List out the configured TTL settings for a given org (org-level and tenant-level).
- [On payment method created](on-payment-method-created.md) - /langsmith/langsmith-platform-openapi.json post /api/v1/orgs/current/payment-method
- [Patch current org pending member](patch-current-org-pending-member.md) - Update the role on a pending org member invite.
- [Reinstate org personal access token](reinstate-org-personal-access-token.md) - Lift a revocation, so the personal access token authenticates again.
- [Remove member from current org](remove-member-from-current-org.md) - Remove a user from the current organization.
- [Revoke org personal access token](revoke-org-personal-access-token.md) - Revoke a personal access token, so it stops working but its record remains.
- [Set company info](set-company-info.md) - /langsmith/langsmith-platform-openapi.json post /api/v1/orgs/current/business-info
- [Set default SSO provision](set-default-sso-provision.md) - Set the current organization as the default for SSO provisioning in self-hosted environments.
- [Set role restriction](set-role-restriction.md) - /langsmith/langsmith-platform-openapi.json put /api/v1/orgs/current/roles/{role_id}/restriction
- [Update allowed login methods](update-allowed-login-methods.md) - Update allowed login methods for the current organization.
- [Update current org member](update-current-org-member.md) - This is used for updating a user's role (all auth modes) or full_name/password (basic auth)
- [Update current organization info](update-current-organization-info.md) - /langsmith/langsmith-platform-openapi.json patch /api/v1/orgs/current/info
- [Update current user](update-current-user.md) - Update a user's full_name/password (basic auth only)
- [Update org service key](update-org-service-key.md) - Update an API key's role(s) in place without rotating the key.
- [Update organization roles](update-organization-roles.md) - /langsmith/langsmith-platform-openapi.json patch /api/v1/orgs/current/roles/{role_id}
- [Update SSO settings](update-sso-settings.md) - Update SSO provider settings defaults for the current organization.
- [Upsert TTL settings](upsert-ttl-settings.md) - /langsmith/langsmith-platform-openapi.json put /api/v1/orgs/ttl-settings
