---
title: "List Deployment Log Entries"
description: "List build or deploy log entries for a deployment."
source: "https://docs.langchain.com/api-reference/deployments-v2/list-deployment-log-entries"
category: "docs"
tags: [docs, api-reference, deployments-v2, list-deployment-log-entries]
---

# List Deployment Log Entries

> List build or deploy log entries for a deployment.

## OpenAPI

**https://api.host.langchain.com/openapi.json get /v2/deployment-logs**

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
  /v2/deployment-logs:
    get:
      tags:
        - Deployments (v2)
      summary: List Deployment Log Entries
      description: List build or deploy log entries for a deployment.
      operationId: list_deployment_log_entries_v2_deployment_logs_get
      parameters:
        - name: deployment_id
          in: query
          required: true
          schema:
            type: string
            format: uuid
            title: Deployment Id
        - name: revision_id
          in: query
          required: false
          schema:
            anyOf:
              - type: string
                format: uuid
              - type: 'null'
            title: Revision Id
        - name: log_type
          in: query
          required: false
          schema:
            enum:
              - BUILD
              - DEPLOY
            type: string
            default: DEPLOY
            title: Log Type
        - name: start_time
          in: query
          required: false
          schema:
            anyOf:
              - type: string
                format: date-time
              - type: 'null'
            title: Start Time
        - name: end_time
          in: query
          required: false
          schema:
            anyOf:
              - type: string
                format: date-time
              - type: 'null'
            title: End Time
        - name: sort_order
          in: query
          required: false
          schema:
            enum:
              - asc
              - desc
            type: string
            default: asc
            title: Sort Order
        - name: page_size
          in: query
          required: false
          schema:
            type: integer
            maximum: 100
            minimum: 1
            default: 20
            title: Page Size
        - name: cursor
          in: query
          required: false
          schema:
            anyOf:
              - type: string
              - type: 'null'
            title: Cursor
        - name: query
          in: query
          required: false
          schema:
            anyOf:
              - type: string
              - type: 'null'
            title: Query
        - name: level
          in: query
          required: false
          schema:
            anyOf:
              - enum:
                  - DEBUG
                  - INFO
                  - WARNING
                  - ERROR
                  - CRITICAL
                type: string
              - type: 'null'
            title: Level
        - name: run_id
          in: query
          required: false
          schema:
            anyOf:
              - type: string
              - type: 'null'
            title: Run Id
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DeploymentLogsList'
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
    DeploymentLogsList:
      properties:
        items:
          items:
            additionalProperties: true
            type: object
          type: array
          title: Items
        next_cursor:
          anyOf:
            - type: string
            - type: 'null'
          title: Next Cursor
      type: object
      title: DeploymentLogsList
      description: Canonical cursor-paginated deployment-log collection.
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
