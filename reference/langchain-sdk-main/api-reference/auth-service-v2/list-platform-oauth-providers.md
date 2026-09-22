---
title: "List Platform Oauth Providers"
description: "List platform-level OAuth providers available to all workspaces."
source: "https://docs.langchain.com/api-reference/auth-service-v2/list-platform-oauth-providers"
category: "docs"
tags: [docs, api-reference, auth-service-v2, list-platform-oauth-providers]
---

# List Platform Oauth Providers

> List platform-level OAuth providers available to all workspaces.

## OpenAPI

**https://api.host.langchain.com/openapi.json get /v2/auth/platform-providers**

````yaml
openapi: 3.1.0
info:
  title: LangSmith Deployment Control Plane API
  description: >
    The LangSmith Deployment Control Plane API is used to programmatically
    create and manage

    Agent Server deployments. For example, the APIs can be orchestrated to

    create custom CI/CD workflows.

    ## Host

    https://api.host.langchain.com

    ## Authentication

    To authenticate with the LangSmith Deployment Control Plane API, set the
    `X-Api-Key` header

    to a valid [LangSmith API
    key](https://docs.langchain.com/langsmith/create-account-api-key#create-an-api-key).

    ## Versioning

    Each endpoint path is prefixed with a version (e.g. `v1`, `v2`).

    ## Quick Start

    1. Call `POST /v2/deployments` to create a new Deployment. The response body
    contains the Deployment ID (`id`) and the ID of the latest (and first)
    revision (`latest_revision_id`).

    1. Call `GET /v2/deployments/{deployment_id}` to retrieve the Deployment.
    Set `deployment_id` in the URL to the value of Deployment ID (`id`).

    1. Poll for revision `status` until `status` is `DEPLOYED` by calling `GET
    /v2/deployments/{deployment_id}/revisions/{latest_revision_id}`.

    1. Call `PATCH /v2/deployments/{deployment_id}` to update the deployment.
  version: 0.1.0
servers: []
security: []
paths:
  /v2/auth/platform-providers:
    get:
      tags:
        - Auth Service (v2)
      summary: List Platform Oauth Providers
      description: List platform-level OAuth providers available to all workspaces.
      operationId: list_platform_oauth_providers_v2_auth_platform_providers_get
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                items:
                  $ref: '#/components/schemas/OAuthProviderResponse'
                type: array
                title: >-
                  Response List Platform Oauth Providers V2 Auth Platform
                  Providers Get
      security:
        - API Key: []
        - Tenant ID: []
        - Bearer Auth: []
components:
  schemas:
    OAuthProviderResponse:
      properties:
        id:
          type: string
          title: Id
        organization_id:
          type: string
          title: Organization Id
        provider_id:
          type: string
          title: Provider Id
        name:
          type: string
          title: Name
        client_id:
          type: string
          title: Client Id
        auth_url:
          type: string
          title: Auth Url
        token_url:
          type: string
          title: Token Url
        uses_pkce:
          type: boolean
          title: Uses Pkce
        code_challenge_method:
          anyOf:
            - type: string
            - type: 'null'
          title: Code Challenge Method
        provider_type:
          anyOf:
            - type: string
            - type: 'null'
          title: Provider Type
        mcp_server_url:
          anyOf:
            - type: string
            - type: 'null'
          title: Mcp Server Url
        token_endpoint_auth_method:
          type: string
          title: Token Endpoint Auth Method
          default: client_secret_post
        authorization_params:
          additionalProperties:
            type: string
          type: object
          title: Authorization Params
        is_dynamic_client:
          type: boolean
          title: Is Dynamic Client
          default: false
        allowed_redirect_uris:
          items:
            type: string
          type: array
          title: Allowed Redirect Uris
        default_redirect_uri:
          anyOf:
            - type: string
            - type: 'null'
          title: Default Redirect Uri
        created_at:
          type: string
          format: date-time
          title: Created At
        updated_at:
          type: string
          format: date-time
          title: Updated At
      type: object
      required:
        - id
        - organization_id
        - provider_id
        - name
        - client_id
        - auth_url
        - token_url
        - uses_pkce
        - code_challenge_method
        - created_at
        - updated_at
      title: OAuthProviderResponse
      description: Response model for OAuth provider.

````
