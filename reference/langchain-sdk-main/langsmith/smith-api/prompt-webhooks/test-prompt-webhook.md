---
title: "Test prompt webhook"
description: "Test a specific prompt webhook."
source: "https://docs.langchain.com/langsmith/smith-api/prompt-webhooks/test-prompt-webhook"
category: "docs"
tags: [docs, langsmith, smith-api, prompt-webhooks, test-prompt-webhook]
---

# Test prompt webhook

> Test a specific prompt webhook.

## OpenAPI

**/langsmith/langsmith-platform-openapi.json post /api/v1/prompt-webhooks/test**

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
  /api/v1/prompt-webhooks/test:
    post:
      tags:
        - prompt-webhooks
      summary: Test prompt webhook
      description: Test a specific prompt webhook.
      operationId: test_prompt_webhook_api_v1_prompt_webhooks_test_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PromptWebhookTest'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                additionalProperties:
                  type: string
                type: object
                title: Response Test Prompt Webhook Api V1 Prompt Webhooks Test Post
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
    PromptWebhookTest:
      properties:
        webhook:
          $ref: '#/components/schemas/PromptWebhookBase'
        payload:
          $ref: '#/components/schemas/PromptWebhookPayload'
      type: object
      required:
        - webhook
        - payload
      title: PromptWebhookTest
      description: Schema for testing a prompt webhook.
    HTTPValidationError:
      properties:
        detail:
          items:
            type: string
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    PromptWebhookBase:
      properties:
        url:
          type: string
          minLength: 1
          format: uri
          title: Url
        headers:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Headers
        include_prompts:
          anyOf:
            - items:
                type: string
                format: uuid
              type: array
            - type: 'null'
          title: Include Prompts
        exclude_prompts:
          anyOf:
            - items:
                type: string
                format: uuid
              type: array
            - type: 'null'
          title: Exclude Prompts
        triggers:
          items:
            $ref: '#/components/schemas/EPromptWebhookTrigger'
          type: array
          title: Triggers
      type: object
      required:
        - url
      title: PromptWebhookBase
      description: Base schema for prompt webhooks.
    PromptWebhookPayload:
      properties:
        prompt_id:
          type: string
          title: Prompt Id
        prompt_name:
          type: string
          title: Prompt Name
        manifest:
          additionalProperties: true
          type: object
          title: Manifest
        commit_hash:
          type: string
          title: Commit Hash
        created_at:
          type: string
          title: Created At
        created_by:
          type: string
          title: Created By
        event:
          $ref: '#/components/schemas/EPromptWebhookTrigger'
        tag_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Tag Name
      type: object
      required:
        - prompt_id
        - prompt_name
        - manifest
        - commit_hash
        - created_at
        - created_by
        - event
      title: PromptWebhookPayload
    EPromptWebhookTrigger:
      type: string
      enum:
        - commit
        - tag:create
        - tag:update
      title: EPromptWebhookTrigger
      description: Valid trigger types for prompt webhooks.
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
