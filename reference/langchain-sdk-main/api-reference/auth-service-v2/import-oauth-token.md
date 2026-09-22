---
title: "Import Oauth Token"
description: "Persist a directly-obtained OAuth token (no authorization-code exchange)."
source: "https://docs.langchain.com/api-reference/auth-service-v2/import-oauth-token"
category: "docs"
tags: [docs, api-reference, auth-service-v2, import-oauth-token]
---

# Import Oauth Token

> Persist a directly-obtained OAuth token (no authorization-code exchange).

The Slack managed-install flow receives a bot token inline from
``apps.managedInstall`` instead of through the browser OAuth redirect. This
stores it (Fernet-encrypted at rest, via ``create_oauth_token``) for the
caller's org/user against an existing provider. Requiring the provider to
already exist in the caller's org scopes the write and blocks cross-org
token creation. The token value is never logged or returned.

## OpenAPI

**https://api.host.langchain.com/openapi.json post /v2/auth/tokens/import**

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
  /v2/auth/tokens/import:
    post:
      tags:
        - Auth Service (v2)
      summary: Import Oauth Token
      description: >-
        Persist a directly-obtained OAuth token (no authorization-code
        exchange).

        The Slack managed-install flow receives a bot token inline from

        ``apps.managedInstall`` instead of through the browser OAuth redirect.
        This

        stores it (Fernet-encrypted at rest, via ``create_oauth_token``) for the

        caller's org/user against an existing provider. Requiring the provider
        to

        already exist in the caller's org scopes the write and blocks cross-org

        token creation. The token value is never logged or returned.
      operationId: import_oauth_token_v2_auth_tokens_import_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/OAuthTokenImportRequest'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OAuthTokenImportResponse'
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
    OAuthTokenImportRequest:
      properties:
        provider_id:
          type: string
          title: Provider Id
        access_token:
          type: string
          title: Access Token
        refresh_token:
          anyOf:
            - type: string
            - type: 'null'
          title: Refresh Token
        expires_in_seconds:
          anyOf:
            - type: integer
            - type: 'null'
          title: Expires In Seconds
        scopes:
          items:
            type: string
          type: array
          title: Scopes
          default: []
        metadata:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Metadata
        is_default:
          type: boolean
          title: Is Default
          default: true
      type: object
      required:
        - provider_id
        - access_token
      title: OAuthTokenImportRequest
      description: >-
        Import a directly-obtained OAuth token (no authorization-code exchange).

        Used by the Slack managed-install flow, which receives a bot token
        inline

        from ``apps.managedInstall`` rather than via the browser OAuth redirect.
        The

        token is persisted for the caller's org/user against ``provider_id``
        (which

        must already exist in the caller's org).
    OAuthTokenImportResponse:
      properties:
        token_id:
          type: string
          title: Token Id
      type: object
      required:
        - token_id
      title: OAuthTokenImportResponse
      description: Response for a token import — the created token id only, no secrets.
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
