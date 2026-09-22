---
title: "List Connections"
description: "https://api.host.langchain.com/openapi.json get /v2/auth/agents/{agent_id}/connections"
source: "https://docs.langchain.com/api-reference/agent-connections-v2/list-connections"
category: "docs"
tags: [docs, api-reference, agent-connections-v2, list-connections]
---

# List Connections

## OpenAPI

**https://api.host.langchain.com/openapi.json get /v2/auth/agents/{agent_id}/connections**

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
  /v2/auth/agents/{agent_id}/connections:
    get:
      tags:
        - Agent Connections (v2)
      summary: List Connections
      operationId: list_connections_v2_auth_agents__agent_id__connections_get
      parameters:
        - name: agent_id
          in: path
          required: true
          schema:
            type: string
            description: Agent ID
            title: Agent Id
          description: Agent ID
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AgentConnectionListResponse'
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
    AgentConnectionListResponse:
      properties:
        data:
          items:
            $ref: '#/components/schemas/AgentConnectionResponse'
          type: array
          title: Data
      type: object
      required:
        - data
      title: AgentConnectionListResponse
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    AgentConnectionResponse:
      properties:
        id:
          type: string
          title: Id
        agent_id:
          type: string
          title: Agent Id
        oauth_token_id:
          type: string
          title: Oauth Token Id
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
        expires_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Expires At
        created_by:
          type: string
          title: Created By
        created_at:
          type: string
          format: date-time
          title: Created At
      type: object
      required:
        - id
        - agent_id
        - oauth_token_id
        - provider_id
        - provider_account_label
        - scopes
        - expires_at
        - created_by
        - created_at
      title: AgentConnectionResponse
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
