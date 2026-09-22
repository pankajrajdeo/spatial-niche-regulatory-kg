---
title: "langsmith/smith-api/oauth"
description: "Index of 19 pages and 0 subdirectories under langsmith/smith-api/oauth."
category: "index"
tags: [index, langsmith, smith-api, oauth]
---

# langsmith/smith-api/oauth

19 pages here.

## Files

- [Approve OAuth2 authorization request](approve-oauth2-authorization-request.md) - Issues an authorization code after the authenticated user approves the request. Called by the frontend consent page. Requires authentication.
- [Authorize a device code](authorize-a-device-code.md) - Marks a device code as authorized for the authenticated user. Called by the /activate page when the user enters their user code. Requires authentication.
- [Create an oauth client](create-an-oauth-client.md) - Registers a new OAuth 2.0 / OIDC client owned by the caller's organization. For confidential clients the response includes a client_secret that is shown only once.
- [Delete an oauth client](delete-an-oauth-client.md) - /langsmith/langsmith-platform-openapi.json delete /api/v1/platform/oauth/clients/{id}
- [Exchange grant for OAuth2 tokens](exchange-grant-for-oauth2-tokens.md) - Token endpoint that dispatches by grant_type: authorization_code, urn:ietf:params:oauth:grant-type:device_code, or refresh_token.
- [Get an oauth client](get-an-oauth-client.md) - /langsmith/langsmith-platform-openapi.json get /api/v1/platform/oauth/clients/{id}
- [Get OAuth2 authorization server metadata](get-oauth2-authorization-server-metadata.md) - Returns OAuth2 authorization server metadata per RFC 8414, including supported endpoints, grant types, and response types.
- [Get openid connect provider configuration](get-openid-connect-provider-configuration.md) - Returns the OpenID Connect discovery document (OpenID Connect Discovery 1.0), advertising the authorization, token, userinfo, and JWKS endpoints plus supported scopes, response types, and signing...
- [Get openid connect userinfo](get-openid-connect-userinfo.md) - Returns identity claims for the user represented by a LangSmith access token whose audience is the identity resource or the API resource. The token is passed as a Bearer credential in the...
- [Get public OAuth2 client metadata](get-public-oauth2-client-metadata.md) - Returns the display metadata (name, logo, homepage/terms/privacy links) for a registered OAuth2 client. Used by the consent screen to show a human-readable client identity instead of the raw...
- [Initiate OAuth2 authorization](initiate-oauth2-authorization.md) - Validates authorization request parameters and redirects to the frontend consent page per RFC 6749.
- [List authorized applications](list-authorized-applications.md) - Lists the third-party applications the authenticated user has authorized to sign in with LangSmith.
- [List oauth clients](list-oauth-clients.md) - Lists the OAuth clients owned by the caller's organization.
- [Register an OAuth2 dynamic client](register-an-oauth2-dynamic-client.md) - Public RFC 7591 Dynamic Client Registration endpoint. Only mints public clients with allowed loopback, HTTPS, or native client redirect URIs. Body limit 8 KB.
- [Request OAuth2 device authorization](request-oauth2-device-authorization.md) - Issues a device code and user code for the device authorization flow per RFC 8628.
- [Revoke an authorized application](revoke-an-authorized-application.md) - Revokes the authenticated user's authorization for an application and invalidates that application's active tokens for the user.
- [Revoke an OAuth2 token](revoke-an-oauth2-token.md) - Revokes an access token or refresh token per RFC 7009. Always returns 200 regardless of whether the token was found.
- [Rotate an oauth client secret](rotate-an-oauth-client-secret.md) - Generates a new client secret for a confidential client, invalidating the previous one. The new secret is shown only once.
- [Update an oauth client](update-an-oauth-client.md) - /langsmith/langsmith-platform-openapi.json patch /api/v1/platform/oauth/clients/{id}
