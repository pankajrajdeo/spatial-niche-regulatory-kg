---
title: "Capture a snapshot from a sandbox"
description: "Create a snapshot by capturing the current state of a sandbox or promoting an existing checkpoint."
source: "https://docs.langchain.com/langsmith/smith-api/sandboxes/capture-a-snapshot-from-a-sandbox"
category: "docs"
tags: [docs, langsmith, smith-api, sandboxes, capture-a-snapshot-from-a-sandbox]
---

# Capture a snapshot from a sandbox

> Create a snapshot by capturing the current state of a sandbox or promoting an existing checkpoint.

## OpenAPI

**/langsmith/langsmith-platform-openapi.json post /api/v2/sandboxes/boxes/{name}/snapshot**

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
  /api/v2/sandboxes/boxes/{name}/snapshot:
    post:
      tags:
        - sandboxes
      summary: Capture a snapshot from a sandbox
      description: >-
        Create a snapshot by capturing the current state of a sandbox or
        promoting an existing checkpoint.
      parameters:
        - description: Sandbox display name
          name: name
          in: path
          required: true
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/sandboxes.CaptureSnapshotPayload'
      responses:
        '201':
          description: Created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/sandboxes.SnapshotResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/sandboxes.ErrorResponse'
        '403':
          description: Forbidden
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/sandboxes.ErrorResponse'
        '404':
          description: Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/sandboxes.ErrorResponse'
        '409':
          description: sandbox must be running for Docker image export
          headers:
            X-Should-Retry:
              description: false for deterministic state conflicts
              schema:
                type: string
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/shared.ProblemDetails'
        '422':
          description: Unprocessable Entity
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/sandboxes.ErrorResponse'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/sandboxes.ErrorResponse'
      security:
        - API Key: []
        - Tenant ID: []
        - Bearer Auth: []
components:
  schemas:
    sandboxes.CaptureSnapshotPayload:
      type: object
      required:
        - name
      properties:
        checkpoint:
          description: if omitted, creates a fresh checkpoint from the running VM
          type: string
        description:
          description: >-
            Description says what this snapshot's image can do, so a caller can
            hand it to an agent as a capability summary. At most 1024
            characters.
          type: string
          maxLength: 1024
        docker_image:
          description: sandbox-local Docker image to export
          type: string
        fs_capacity_bytes:
          description: required for Docker image export unless the sandbox has a capacity
          type: integer
        include_memory:
          description: >-
            IncludeMemory, when true, captures a full VM memory snapshot

            alongside the filesystem clone. Only honored when the sandbox is
            running

            AND Checkpoint is omitted (i.e. a fresh in-VM checkpoint is
            requested).

            Defaults to false to keep snapshots small unless memory restore is

            explicitly desired.
          type: boolean
        labels:
          description: Labels seed the captured snapshot's labels.
          allOf:
            - $ref: '#/components/schemas/sandboxes.Labels'
        name:
          type: string
        run_config:
          description: >-
            RunConfig overrides the runtime configuration the snapshot carries:
            for a

            docker_image export, the image's USER, WORKDIR and ENV; for a
            capture of

            the running VM, the sandbox's own. user and work_dir replace,
            env_vars

            merge.
          allOf:
            - $ref: '#/components/schemas/sandboxapi.RunConfig'
        tag:
          description: mutable Docker-style tag; defaults to "latest"
          type: string
    sandboxes.SnapshotResponse:
      type: object
      properties:
        created_at:
          type: string
        created_by:
          type: string
        description:
          description: >-
            Description says what this snapshot's image can do, so a caller can
            hand it to an agent as a capability summary.
          type: string
        docker_image:
          type: string
        fs_capacity_bytes:
          type: integer
        fs_used_bytes:
          type: integer
        id:
          type: string
        image_digest:
          type: string
        labels:
          $ref: '#/components/schemas/sandboxes.Labels'
        memory_snapshot_size_bytes:
          description: >-
            MemorySnapshotSizeBytes is non-nil iff the snapshot was captured
            with

            VM memory state. A non-nil value is the canonical signal that this

            snapshot can warm-restore from memory; nil means rootfs only.
          type: integer
        name:
          type: string
        registry_id:
          type: string
        run_config:
          description: >-
            RunConfig is what sandboxes from this snapshot boot with. Absent on

            snapshots built before it was recorded, which run as root with their
            own env.
          allOf:
            - $ref: '#/components/schemas/sandboxapi.RunConfig'
        source_sandbox_id:
          type: string
        status:
          type: string
        status_message:
          type: string
        tags:
          description: >-
            Tags currently resolving to this snapshot, under Name. A snapshot
            with no

            tags is dangling — addressable only by id.
          type: array
          items:
            type: string
        updated_at:
          type: string
    sandboxes.ErrorResponse:
      type: object
      properties:
        detail:
          type: object
          properties:
            error:
              type: string
            error_id:
              type: string
            message:
              type: string
    shared.ProblemDetails:
      description: RFC 7807 problem details returned on V2 API errors.
      type: object
      properties:
        detail:
          type: string
        details:
          description: >-
            Details is a LangSmith extension carrying structured fields for
            ErrorClass.
          allOf:
            - $ref: '#/components/schemas/shared.ParseErrorDetails'
        error_class:
          description: |-
            ErrorClass is a LangSmith extension sub-categorizing a status code.
            Additional values require expanding this enum and adding a oneOf
            discriminator on Details to keep the class↔details contract typed.
          type: string
          enum:
            - PARSE_FAILURE
        instance:
          type: string
        remedy:
          description: Remedy is a LangSmith extension for user-recoverable errors.
          type: string
        status:
          type: integer
        title:
          type: string
        type:
          type: string
    sandboxes.Labels:
      type: object
      additionalProperties:
        type: string
    sandboxapi.RunConfig:
      type: object
      properties:
        env_vars:
          type: object
          additionalProperties:
            type: string
        user:
          type: string
        work_dir:
          type: string
    shared.ParseErrorDetails:
      description: Structured fields describing an adapter parse failure.
      type: object
      required:
        - adapter
        - item_type
      properties:
        adapter:
          type: string
        item_type:
          type: string
        run_id:
          type: string
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
