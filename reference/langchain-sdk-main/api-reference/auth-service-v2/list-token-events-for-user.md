---
title: "List Token Events For User"
description: "List the calling user's OAuth connection audit events, newest first."
source: "https://docs.langchain.com/api-reference/auth-service-v2/list-token-events-for-user"
category: "docs"
tags: [docs, api-reference, auth-service-v2, list-token-events-for-user]
---

# List Token Events For User

> List the calling user's OAuth connection audit events, newest first.

Backs the frontend "your connection dropped, reconnect" surface. Scoped to
the authenticated user + org; both come from the auth context, never from
request input.

## OpenAPI

**https://api.host.langchain.com/openapi.json get /v2/auth/token-events**

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
  /v2/auth/token-events:
    get:
      tags:
        - Auth Service (v2)
      summary: List Token Events For User
      description: >-
        List the calling user's OAuth connection audit events, newest first.

        Backs the frontend "your connection dropped, reconnect" surface. Scoped
        to

        the authenticated user + org; both come from the auth context, never
        from

        request input.
      operationId: list_token_events_for_user_v2_auth_token_events_get
      parameters:
        - name: provider_id
          in: query
          required: false
          schema:
            anyOf:
              - type: string
              - type: 'null'
            description: Filter to one OAuth provider
            title: Provider Id
          description: Filter to one OAuth provider
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            maximum: 200
            minimum: 1
            description: Max events to return
            default: 50
            title: Limit
          description: Max events to return
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/TokenEventSummary'
                title: Response List Token Events For User V2 Auth Token Events Get
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
    TokenEventSummary:
      properties:
        id:
          type: string
          title: Id
        provider_id:
          type: string
          title: Provider Id
        agent_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Agent Id
        event_type:
          type: string
          title: Event Type
        reason:
          anyOf:
            - type: string
            - type: 'null'
          title: Reason
        source:
          anyOf:
            - type: string
            - type: 'null'
          title: Source
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
        detail:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Detail
        acknowledged_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Acknowledged At
        created_at:
          type: string
          format: date-time
          title: Created At
      type: object
      required:
        - id
        - provider_id
        - event_type
        - created_at
      title: TokenEventSummary
      description: >-
        A single OAuth connection audit event, for the calling user.

        Surfaces why/when a connection was removed so the UI can prompt a
        reconnect.

        Carries no token or secret material.
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
