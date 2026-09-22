---
title: "List Revision Logs"
description: "List build or deploy logs for a specific revision of a deployment."
source: "https://docs.langchain.com/api-reference/deployments-v2/list-revision-logs"
category: "docs"
tags: [docs, api-reference, deployments-v2, list-revision-logs]
---

# List Revision Logs

> List build or deploy logs for a specific revision of a deployment.

## OpenAPI

**https://api.host.langchain.com/openapi.json get /v2/deployments/{deployment_id}/revisions/{revision_id}/logs**

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
  /v2/deployments/{deployment_id}/revisions/{revision_id}/logs:
    get:
      tags:
        - Deployments (v2)
      summary: List Revision Logs
      description: List build or deploy logs for a specific revision of a deployment.
      operationId: >-
        list_revision_logs_v2_deployments__deployment_id__revisions__revision_id__logs_get
      parameters:
        - name: deployment_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
            title: Deployment ID
        - name: revision_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
            title: Revision ID
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
        - name: order
          in: query
          required: false
          schema:
            enum:
              - asc
              - desc
            type: string
            default: asc
            title: Order
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            maximum: 1000
            minimum: 1
            default: 50
            title: Limit
        - name: offset
          in: query
          required: false
          schema:
            anyOf:
              - type: string
              - type: 'null'
            title: Offset
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
        - name: type
          in: query
          required: true
          schema:
            enum:
              - build
              - deploy
            type: string
            description: 'Which logs to return: build-time or deploy-time.'
            title: Type
          description: 'Which logs to return: build-time or deploy-time.'
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/LogsResponse'
        '404':
          description: Not Found
          content:
            application/json:
              example:
                detail: Deployment ID {deployment_id} not found.
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
    LogsResponse:
      properties:
        logs:
          items:
            additionalProperties: true
            type: object
          type: array
          title: Logs
          default: []
        next_offset:
          anyOf:
            - type: string
            - type: 'null'
          title: Next Offset
      type: object
      title: LogsResponse
      description: Log lines plus a pagination cursor.
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
