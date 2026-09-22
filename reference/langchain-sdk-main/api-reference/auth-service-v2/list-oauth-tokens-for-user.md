---
title: "List Oauth Tokens For User"
description: "List the calling user's tokens for a provider."
source: "https://docs.langchain.com/api-reference/auth-service-v2/list-oauth-tokens-for-user"
category: "docs"
tags: [docs, api-reference, auth-service-v2, list-oauth-tokens-for-user]
---

# List Oauth Tokens For User

> List the calling user's tokens for a provider.

## OpenAPI

**https://api.host.langchain.com/openapi.json get /v2/auth/tokens**

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
  /v2/auth/tokens:
    get:
      tags:
        - Auth Service (v2)
      summary: List Oauth Tokens For User
      description: List the calling user's tokens for a provider.
      operationId: list_oauth_tokens_for_user_v2_auth_tokens_get
      parameters:
        - name: provider_id
          in: query
          required: false
          schema:
            anyOf:
              - type: string
              - type: 'null'
            description: OAuth provider ID
            title: Provider Id
          description: OAuth provider ID
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/OAuthTokenSummary'
                title: Response List Oauth Tokens For User V2 Auth Tokens Get
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
    OAuthTokenSummary:
      properties:
        id:
          type: string
          title: Id
        provider_id:
          type: string
          title: Provider Id
        provider_account_label:
          anyOf:
            - type: string
            - type: 'null'
          title: Provider Account Label
        scopes:
          items:
            type: string
          type: array
          title: Scopes
          default: []
        expires_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Expires At
        is_default:
          type: boolean
          title: Is Default
          default: false
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
        - provider_id
        - created_at
        - updated_at
      title: OAuthTokenSummary
      description: Public-facing token summary — no sensitive data.
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
