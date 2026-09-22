---
title: "Delete Deployment"
description: "Delete a deployment by ID."
source: "https://docs.langchain.com/api-reference/deployments-v2/delete-deployment"
category: "docs"
tags: [docs, api-reference, deployments-v2, delete-deployment]
---

# Delete Deployment

> Delete a deployment by ID.

## OpenAPI

**https://api.host.langchain.com/openapi.json delete /v2/deployments/{deployment_id}**

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
  /v2/deployments/{deployment_id}:
    delete:
      tags:
        - Deployments (v2)
      summary: Delete Deployment
      description: Delete a deployment by ID.
      operationId: delete_deployment_v2_deployments__deployment_id__delete
      parameters:
        - name: deployment_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
            title: Deployment ID
        - name: delete_tracing_project
          in: query
          required: false
          schema:
            type: boolean
            description: >-
              Optionally delete tracing project for the deployment. Ignored in
              agent mode, which preserves the tracing project.
            default: false
            title: Delete Tracing Project
          description: >-
            Optionally delete tracing project for the deployment. Ignored in
            agent mode, which preserves the tracing project.
        - name: force
          in: query
          required: false
          schema:
            type: boolean
            description: >-
              Force delete the deployment's control-plane metadata, skipping
              Kubernetes resource cleanup. Only works on a deployment that has
              already been soft-deleted by a prior delete call; force-deleting a
              still-active deployment returns 400. Use to clear stale
              deployments whose runtime is already gone. This is unrecoverable
              and may orphan remaining cluster-side resources. Reusing the
              deployment name after a force delete is unsupported and may attach
              a new deployment to those orphaned resources; use a different
              name.
            default: false
            title: Force
          description: >-
            Force delete the deployment's control-plane metadata, skipping
            Kubernetes resource cleanup. Only works on a deployment that has
            already been soft-deleted by a prior delete call; force-deleting a
            still-active deployment returns 400. Use to clear stale deployments
            whose runtime is already gone. This is unrecoverable and may orphan
            remaining cluster-side resources. Reusing the deployment name after
            a force delete is unsupported and may attach a new deployment to
            those orphaned resources; use a different name.
      responses:
        '204':
          description: Successful Response
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
