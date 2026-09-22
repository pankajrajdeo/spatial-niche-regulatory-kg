---
title: "Get Engine Picker Session Endpoint"
description: "Get a Forge GitHub App installation picker session."
source: "https://docs.langchain.com/api-reference/integrations-v2/get-engine-picker-session-endpoint"
category: "docs"
tags: [docs, api-reference, integrations-v2, get-engine-picker-session-endpoint]
---

# Get Engine Picker Session Endpoint

> Get a Forge GitHub App installation picker session.

## OpenAPI

**https://api.host.langchain.com/openapi.json get /v2/integrations/forge-github/picker-sessions/{session_id}**

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
  /v2/integrations/forge-github/picker-sessions/{session_id}:
    get:
      tags:
        - Integrations (v2)
      summary: Get Engine Picker Session Endpoint
      description: Get a Forge GitHub App installation picker session.
      operationId: >-
        get_engine_picker_session_endpoint_v2_integrations_forge_github_picker_sessions__session_id__get
      parameters:
        - name: session_id
          in: path
          required: true
          schema:
            type: string
            title: Picker session ID
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EnginePickerSessionResponse'
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
    EnginePickerSessionResponse:
      properties:
        installs:
          items:
            $ref: '#/components/schemas/EnginePickerInstallOption'
          type: array
          title: Installs
        return_to:
          anyOf:
            - type: string
            - type: 'null'
          title: Return To
      type: object
      required:
        - installs
      title: EnginePickerSessionResponse
      description: |-
        Payload for GET /forge/github/picker-session/{id}. The FE renders
        `installs` plus a hardcoded "Install on a new GitHub org" affordance.
        `return_to` round-trips back through the select endpoint so the final
        result page lands the user back on their originating view.
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    EnginePickerInstallOption:
      properties:
        installation_id:
          type: integer
          title: Installation Id
        account_login:
          type: string
          title: Account Login
        account_type:
          type: string
          title: Account Type
        already_in_org:
          type: boolean
          title: Already In Org
          default: false
      type: object
      required:
        - installation_id
        - account_login
        - account_type
      title: EnginePickerInstallOption
      description: |-
        One row of the post-OAuth picker. Each one is an Engine install the
        user has GitHub-side access to via the OAuth token captured at the
        callback.
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
