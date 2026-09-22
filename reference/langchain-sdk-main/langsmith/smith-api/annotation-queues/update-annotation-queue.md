---
title: "Update annotation queue"
description: "/langsmith/langsmith-platform-openapi.json patch /api/v1/annotation-queues/{queue_id}"
source: "https://docs.langchain.com/langsmith/smith-api/annotation-queues/update-annotation-queue"
category: "docs"
tags: [docs, langsmith, smith-api, annotation-queues, update-annotation-queue]
---

# Update annotation queue

## OpenAPI

**/langsmith/langsmith-platform-openapi.json patch /api/v1/annotation-queues/{queue_id}**

````yaml
openapi: 3.1.0
info:
  title: LangSmith
  description: >+
    The LangSmith API is used to programmatically create and manage LangSmith
    resources.

    ## Host

    https://api.smith.langchain.com

    ## Authentication

    To authenticate with the LangSmith API, set the `X-Api-Key` header

    to a valid [LangSmith API
    key](https://docs.langchain.com/langsmith/create-account-api-key#create-an-api-key).

  version: 0.1.0
servers:
  - url: /
security: []
tags:
  - name: run
    x-group: Tracing
  - name: runs
    x-group: Tracing
  - name: sessions
    x-group: Tracing
  - name: tracer-sessions
    x-group: Tracing
  - name: threads
    x-group: Threads
  - name: datasets
    x-group: Datasets
  - name: examples
    x-group: Datasets
  - name: evaluators
    x-group: Evaluation
  - name: experiment-view-overrides
    x-group: Evaluation
  - name: experiments
    x-group: Evaluation
  - name: annotation-queues
    x-group: Feedback & Annotation
  - name: annotation_queues
    x-group: Feedback & Annotation
  - name: feedback
    x-group: Feedback & Annotation
  - name: feedback-configs
    x-group: Feedback & Annotation
  - name: alert_rules
    x-group: Monitoring
  - name: bulk-exports
    x-group: Monitoring
  - name: charts
    x-group: Monitoring
  - name: commits
    x-group: Prompts & Playground
  - name: directories
    x-group: Prompts & Playground
  - name: hub_environments
    x-group: Prompts & Playground
  - name: playground-settings
    x-group: Prompts & Playground
  - name: prompt-webhooks
    x-group: Prompts & Playground
  - name: prompts
    x-group: Prompts & Playground
  - name: tag-transitions
    x-group: Prompts & Playground
  - name: comments
    x-group: Prompt Hub
  - name: likes
    x-group: Prompt Hub
  - name: optimization-jobs
    x-group: Prompt Hub
  - name: ownerships
    x-group: Prompt Hub
  - name: repos
    x-group: Prompt Hub
  - name: settings
    x-group: Prompt Hub
  - name: tags
    x-group: Prompt Hub
  - name: integrations
    x-group: Integrations & Tools
  - name: mcp
    x-group: Integrations & Tools
  - name: mcp_vendors
    x-group: Integrations & Tools
  - name: oauth
    x-group: Integrations & Tools
  - name: tools
    x-group: Integrations & Tools
  - name: gateway-policies
    x-group: LLM Gateway
  - name: sandboxes
    x-group: Sandboxes
  - name: issues
    x-group: Issues
  - name: issues-agent
    x-group: Issues
  - name: Organizations
    x-group: Administration
  - name: SCIM Tokens
    x-group: Administration
  - name: TTL Settings
    x-group: Administration
  - name: access_policies
    x-group: Administration
  - name: api-key
    x-group: Administration
  - name: audit-logs
    x-group: Administration
  - name: auth
    x-group: Administration
  - name: aws_marketplace
    x-group: Administration
  - name: data_planes
    x-group: Administration
  - name: me
    x-group: Administration
  - name: orgs
    x-group: Administration
  - name: service-accounts
    x-group: Administration
  - name: tenant
    x-group: Administration
  - name: ttl-settings
    x-group: Administration
  - name: usage-limits
    x-group: Administration
  - name: workspaces
    x-group: Administration
  - name: ace
    x-group: System
  - name: backfills
    x-group: System
  - name: features
    x-group: System
  - name: info
    x-group: System
  - name: model-price-map
    x-group: System
  - name: public
    x-group: System
  - name: fleet orgs
  - name: fleet secrets
  - name: fleet tenants
  - name: fleet threads
    x-hidden: true
  - name: fleet users
  - name: productfeedback
    x-hidden: true
paths:
  /api/v1/annotation-queues/{queue_id}:
    patch:
      tags:
        - annotation-queues
      summary: Update annotation queue
      operationId: update_annotation_queue_api_v1_annotation_queues__queue_id__patch
      parameters:
        - name: queue_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
            title: Queue Id
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AnnotationQueueUpdateSchema'
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema: {}
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
    AnnotationQueueUpdateSchema:
      properties:
        name:
          anyOf:
            - type: string
            - type: 'null'
          title: Name
        description:
          anyOf:
            - type: string
            - type: 'null'
          title: Description
        default_dataset:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Default Dataset
        num_reviewers_per_item:
          anyOf:
            - type: integer
            - $ref: '#/components/schemas/Missing'
            - type: 'null'
          title: Num Reviewers Per Item
          default: 1
        enable_reservations:
          type: boolean
          title: Enable Reservations
          default: true
        reservation_minutes:
          anyOf:
            - type: integer
            - type: 'null'
          title: Reservation Minutes
        rubric_items:
          anyOf:
            - items:
                $ref: '#/components/schemas/AnnotationQueueRubricItemSchema'
              type: array
            - type: 'null'
          title: Rubric Items
        rubric_instructions:
          anyOf:
            - type: string
            - type: 'null'
          title: Rubric Instructions
        metadata:
          anyOf:
            - additionalProperties: true
              type: object
            - $ref: '#/components/schemas/Missing'
            - type: 'null'
          title: Metadata
          default:
            __missing__: __missing__
        reviewer_access_mode:
          anyOf:
            - type: string
              enum:
                - any
                - assigned
            - type: 'null'
          title: Reviewer Access Mode
      type: object
      title: AnnotationQueueUpdateSchema
      description: AnnotationQueue update schema.
    HTTPValidationError:
      properties:
        detail:
          items:
            type: string
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    Missing:
      properties:
        __missing__:
          type: string
          const: __missing__
          title: Missing
      type: object
      required:
        - __missing__
      title: Missing
    AnnotationQueueRubricItemSchema:
      properties:
        feedback_key:
          type: string
          title: Feedback Key
        description:
          anyOf:
            - type: string
            - type: 'null'
          title: Description
        value_descriptions:
          anyOf:
            - type: object
              additionalProperties:
                type: string
            - type: 'null'
          title: Value Descriptions
        score_descriptions:
          anyOf:
            - type: object
              additionalProperties:
                type: string
            - type: 'null'
          title: Score Descriptions
        is_required:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Is Required
        is_assertion:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Is Assertion
        regex_validator:
          anyOf:
            - anyOf:
                - type: string
                - $ref: '#/components/schemas/Missing'
              maxLength: 500
            - type: 'null'
          title: Regex Validator
          default:
            __missing__: __missing__
      type: object
      required:
        - feedback_key
      title: AnnotationQueueRubricItemSchema
  securitySchemes:
    API Key:
      type: apiKey
      in: header
      name: X-API-Key
    Tenant ID:
      type: apiKey
      in: header
      name: X-Tenant-Id
    Bearer Auth:
      type: http
      description: >-
        Bearer tokens are used to authenticate from the UI. Must also specify
        x-tenant-id or x-organization-id (for org scoped apis).
      scheme: bearer

````
