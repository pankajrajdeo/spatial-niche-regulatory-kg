---
title: "Get Oauth Provider"
description: "Get a specific OAuth provider."
source: "https://docs.langchain.com/api-reference/auth-service-v2/get-oauth-provider"
category: "docs"
tags: [docs, api-reference, auth-service-v2, get-oauth-provider]
---

# Get Oauth Provider

> Get a specific OAuth provider.

## OpenAPI

**https://api.host.langchain.com/openapi.json get /v2/auth/providers/{provider_id}**

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
  /v2/auth/providers/{provider_id}:
    get:
      tags:
        - Auth Service (v2)
      summary: Get Oauth Provider
      description: Get a specific OAuth provider.
      operationId: get_oauth_provider_v2_auth_providers__provider_id__get
      parameters:
        - name: provider_id
          in: path
          required: true
          schema:
            type: string
            description: OAuth provider ID
            title: Provider Id
          description: OAuth provider ID
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OAuthProviderResponse'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
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
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
        input:
          title: Input
        ctx:
          type: object
          title: Context
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError

````
