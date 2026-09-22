---
title: "Create a sandbox"
description: "Create a new sandbox from a snapshot. Provide at most one of snapshot_id or snapshot_name; if neither is provided, the server uses the default snapshot. snapshot_name accepts a Docker-style name or..."
source: "https://docs.langchain.com/langsmith/smith-api/sandboxes/create-a-sandbox"
category: "docs"
tags: [docs, langsmith, smith-api, sandboxes, create-a-sandbox]
---

# Create a sandbox

> Create a new sandbox from a snapshot. Provide at most one of `snapshot_id` or `snapshot_name`; if neither is provided, the server uses the default snapshot. `snapshot_name` accepts a Docker-style `name` or `name:tag` reference (a bare name resolves to `name:latest`).

## OpenAPI

**/langsmith/langsmith-platform-openapi.json post /api/v2/sandboxes/boxes**

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
  /api/v2/sandboxes/boxes:
    post:
      tags:
        - sandboxes
      summary: Create a sandbox
      description: >-
        Create a new sandbox from a snapshot. Provide at most one of
        `snapshot_id` or `snapshot_name`; if neither is provided, the server
        uses the default snapshot. `snapshot_name` accepts a Docker-style `name`
        or `name:tag` reference (a bare name resolves to `name:latest`).
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/sandboxes.CreateSandboxPayload'
      responses:
        '201':
          description: Created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/sandboxes.SandboxResponse'
        '400':
          description: Snapshot not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/sandboxes.ErrorResponse'
        '409':
          description: Name already exists
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/sandboxes.ErrorResponse'
        '422':
          description: Validation error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/sandboxes.ErrorResponse'
        '429':
          description: Quota exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/sandboxes.ErrorResponse'
        '500':
          description: Sandbox creation failed or internal error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/sandboxes.ErrorResponse'
        '504':
          description: Sandbox did not become ready in time
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/sandboxes.ErrorResponse'
      security:
        - API Key: []
        - Tenant ID: []
        - Bearer Auth: []
        - X-Service-Key: []
components:
  schemas:
    sandboxes.CreateSandboxPayload:
      type: object
      properties:
        cpu_millicores:
          description: >-
            CPUMillicores optionally requests CPU at millicore granularity (e.g.
            500 = 0.5 vCPU); takes precedence over VCPUs. Fractional (sub-vCPU)
            values are not available for every sandbox.
          type: integer
        delete_after_stop_seconds:
          type: integer
        env_vars:
          type: object
          additionalProperties:
            type: string
        fs_capacity_bytes:
          type: integer
        idle_ttl_seconds:
          type: integer
          maximum: 2147483640
          minimum: 0
        labels:
          description: >-
            Labels are free-form key/value metadata persisted with the sandbox
            and returned on reads. Labels from the source snapshot are inherited
            unless overridden here.
          allOf:
            - $ref: '#/components/schemas/sandboxes.Labels'
        mem_bytes:
          description: >-
            Memory for the sandbox, in bytes. Memory is tied to CPU at 4 GiB per
            vCPU: omit it and it follows that ratio; set it and it must stay
            within 50% of the ratio for the requested CPU, so a 1 vCPU sandbox
            accepts 2-6 GiB. Setting memory without CPU derives the CPU from the
            same ratio. Maximum 64 GiB.
          type: integer
        mount_config:
          $ref: '#/components/schemas/sandboxes.SandboxMountConfig'
        name:
          type: string
        preserve_memory_on_stop:
          description: >-
            PreserveMemoryOnStop, when true, suspends the sandbox's memory on a

            voluntary stop (idle timeout or explicit stop) so the next start
            resumes

            from where it left off. Default false discards memory and keeps only
            the

            filesystem, so the next start is a cold boot. Restarts triggered by

            infrastructure maintenance always preserve memory regardless of this
            setting.
          type: boolean
        proxy_config:
          $ref: '#/components/schemas/sandboxes.ProxyConfig'
        restore_memory:
          description: >-
            RestoreMemory selects how the sandbox handles a snapshot's captured
            memory:

              nil   → if-present: resume from memory when the snapshot has it, else cold-boot (default).
              true  → always: resume from memory; rejected if the snapshot has none.
              false → never: always cold-boot.

            Applies to this request only.
          type: boolean
        run_config:
          description: >-
            RunConfig overrides the snapshot's run config for this sandbox: user
            and

            work_dir replace the snapshot's, env_vars merge over it. The result
            is

            what the sandbox boots with, and what a snapshot captured from it
            carries.
          allOf:
            - $ref: '#/components/schemas/sandboxapi.RunConfig'
        snapshot:
          description: >-
            Snapshot is a Docker-style name or name:tag reference to boot from.
            A bare name resolves to name:latest.
          type: string
        snapshot_id:
          type: string
        snapshot_name:
          description: >-
            SnapshotName is a synonym for Snapshot, accepted for compatibility
            with clients that predate it. Set one or the other.
          type: string
        tag_value_ids:
          items:
            type: string
          type: array
        vcpus:
          type: integer
    sandboxes.SandboxResponse:
      type: object
      properties:
        cpu_millicores:
          type: integer
        created_at:
          type: string
        created_by:
          type: string
        dataplane_url:
          type: string
        delete_after_stop_seconds:
          type: integer
        fs_capacity_bytes:
          type: integer
        id:
          type: string
        idle_ttl_seconds:
          type: integer
        labels:
          $ref: '#/components/schemas/sandboxes.Labels'
        mem_bytes:
          type: integer
        mount_config:
          $ref: '#/components/schemas/sandboxes.SandboxMountConfig'
        name:
          type: string
        preserve_memory_on_stop:
          type: boolean
        proxy_config:
          $ref: '#/components/schemas/sandboxes.ProxyConfig'
        run_config:
          description: >-
            RunConfig is what the sandbox's commands run with: the user, working
            directory and base env beneath env_vars.
          allOf:
            - $ref: '#/components/schemas/sandboxapi.RunConfig'
        size_class:
          type: string
        snapshot_id:
          type: string
        status:
          type: string
        status_message:
          type: string
        stopped_at:
          type: string
        updated_at:
          type: string
        updated_by:
          type: string
        vcpus:
          type: integer
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
    sandboxes.Labels:
      type: object
      additionalProperties:
        type: string
    sandboxes.SandboxMountConfig:
      type: object
      properties:
        auth:
          $ref: '#/components/schemas/sandboxes.SandboxMountAuthConfig'
        mounts:
          type: array
          items:
            $ref: '#/components/schemas/sandboxapi.MountSpec'
    sandboxes.ProxyConfig:
      type: object
      properties:
        access_control:
          $ref: '#/components/schemas/sandboxes.AccessControl'
        callbacks:
          type: array
          items:
            $ref: '#/components/schemas/sandboxes.Callback'
        description:
          description: >-
            Description says what this configuration as a whole lets the sandbox
            reach, complementing the per-rule descriptions. At most 1024
            characters.
          type: string
          maxLength: 1024
        no_proxy:
          items:
            type: string
          type: array
        rules:
          type: array
          items:
            $ref: '#/components/schemas/sandboxes.ProxyRule'
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
    sandboxes.SandboxMountAuthConfig:
      type: object
      properties:
        aws:
          $ref: '#/components/schemas/sandboxes.SandboxAWSMountAuthConfig'
        gcp:
          $ref: '#/components/schemas/sandboxes.SandboxGCPMountAuthConfig'
    sandboxapi.MountSpec:
      type: object
      required:
        - id
        - mount_path
        - type
      properties:
        cache:
          $ref: '#/components/schemas/sandboxapi.MountCacheSpec'
        contexthub:
          $ref: '#/components/schemas/sandboxapi.ContextHubMountSpec'
        gcs:
          $ref: '#/components/schemas/sandboxapi.GCSMountSpec'
        git:
          $ref: '#/components/schemas/sandboxapi.GitMountSpec'
        id:
          type: string
          maxLength: 64
        mount_path:
          type: string
        read_only:
          type: boolean
        s3:
          $ref: '#/components/schemas/sandboxapi.S3MountSpec'
        type:
          enum:
            - s3
            - gcs
            - git
            - contexthub
          allOf:
            - $ref: '#/components/schemas/sandboxapi.MountKind'
      discriminator:
        mapping:
          s3:
            $ref: '#/components/schemas/sandboxapi.S3BucketMountSpec'
          gcs:
            $ref: '#/components/schemas/sandboxapi.GCSBucketMountSpec'
          git:
            $ref: '#/components/schemas/sandboxapi.GitRepoMountSpec'
          contexthub:
            $ref: '#/components/schemas/sandboxapi.ContextHubRepoMountSpec'
        propertyName: type
      oneOf:
        - $ref: '#/components/schemas/sandboxapi.S3BucketMountSpec'
        - $ref: '#/components/schemas/sandboxapi.GCSBucketMountSpec'
        - $ref: '#/components/schemas/sandboxapi.GitRepoMountSpec'
        - $ref: '#/components/schemas/sandboxapi.ContextHubRepoMountSpec'
    sandboxes.AccessControl:
      type: object
      properties:
        allow_list:
          items:
            type: string
          type: array
        deny_list:
          items:
            type: string
          type: array
    sandboxes.Callback:
      type: object
      required:
        - match_hosts
        - ttl_seconds
        - url
      properties:
        full_request:
          type: boolean
        match_hosts:
          type: array
          minItems: 1
          items:
            type: string
        request_headers:
          type: array
          items:
            $ref: '#/components/schemas/sandboxes.ProxyHeader'
        ttl_seconds:
          type: integer
          maximum: 3600
          minimum: 60
        url:
          type: string
    sandboxes.ProxyRule:
      type: object
      required:
        - name
      properties:
        aws:
          $ref: '#/components/schemas/sandboxes.ProxyAWSConfig'
        description:
          description: >-
            Description says what this rule lets the sandbox reach, so an agent
            driving the sandbox can be told its capabilities. At most 1024
            characters.
          type: string
          maxLength: 1024
        enabled:
          type: boolean
        env_vars:
          description: >-
            EnvVars are plaintext env vars set for every command in the sandbox
            while this rule is enabled. Use them for tools that refuse to run
            unless a credential env var is present (e.g. gh needs GH_TOKEN) even
            though this rule injects the real credential on the wire — set a
            dummy value here so the command starts. Explicit per-sandbox
            env_vars win over these, and provider-managed (AWS/GCP) vars win
            over both.
          type: object
          additionalProperties:
            type: string
        gcp:
          $ref: '#/components/schemas/sandboxes.ProxyGCPConfig'
        headers:
          type: array
          items:
            $ref: '#/components/schemas/sandboxes.ProxyHeader'
        match_hosts:
          description: >-
            MatchHosts is only accepted for header injection rules. Provider
            auth

            rules use built-in host matching.
          type: array
          items:
            type: string
        match_paths:
          items:
            type: string
          type: array
        name:
          type: string
        type:
          type: string
    sandboxes.SandboxAWSMountAuthConfig:
      type: object
      oneOf:
        - $ref: '#/components/schemas/sandboxes.SandboxAWSMountRoleAuthConfig'
        - $ref: '#/components/schemas/sandboxes.SandboxAWSMountStaticAuthConfig'
    sandboxes.SandboxGCPMountAuthConfig:
      type: object
      required:
        - service_account_json
      properties:
        service_account_json:
          $ref: '#/components/schemas/sandboxes.ProxySecretValue'
    sandboxapi.MountCacheSpec:
      type: object
      properties:
        max_size_bytes:
          type: integer
          minimum: 0
        writeback_seconds:
          type: integer
          minimum: 0
    sandboxapi.ContextHubMountSpec:
      type: object
      required:
        - repo
      properties:
        initial_pull_only:
          description: >-
            InitialPullOnly syncs the repo once at startup instead of polling
            for

            updates for the sandbox's lifetime.
          type: boolean
        repo:
          description: |-
            Repo is the Context Hub repository to sync, as "owner/repo"
            (e.g. "-/my-agent", where "-" is the current workspace). The repo's
            latest commit tree is mirrored into the mount path.
          type: string
    sandboxapi.GCSMountSpec:
      type: object
      required:
        - bucket
      properties:
        bucket:
          type: string
        prefix:
          type: string
    sandboxapi.GitMountSpec:
      type: object
      required:
        - remote_url
      properties:
        ref:
          $ref: '#/components/schemas/sandboxapi.GitMountRefSpec'
        refresh_interval_seconds:
          type: integer
          minimum: 1
        remote_url:
          type: string
    sandboxapi.S3MountSpec:
      type: object
      required:
        - bucket
        - region
      properties:
        bucket:
          type: string
        endpoint_url:
          type: string
        path_style:
          type: boolean
        prefix:
          type: string
        region:
          type: string
    sandboxapi.MountKind:
      type: string
      enum:
        - s3
        - gcs
        - git
        - contexthub
      x-enum-varnames:
        - MountKindS3
        - MountKindGCS
        - MountKindGit
        - MountKindContextHub
    sandboxapi.S3BucketMountSpec:
      type: object
      required:
        - id
        - mount_path
        - type
        - s3
      properties:
        cache:
          $ref: '#/components/schemas/sandboxapi.MountCacheSpec'
        id:
          type: string
          maxLength: 64
        mount_path:
          type: string
        read_only:
          type: boolean
        s3:
          $ref: '#/components/schemas/sandboxapi.S3MountSpec'
        type:
          enum:
            - s3
          allOf:
            - $ref: '#/components/schemas/sandboxapi.MountKind'
      not:
        anyOf:
          - required:
              - gcs
          - required:
              - git
          - required:
              - contexthub
    sandboxapi.GCSBucketMountSpec:
      type: object
      required:
        - id
        - mount_path
        - type
        - gcs
      properties:
        cache:
          $ref: '#/components/schemas/sandboxapi.MountCacheSpec'
        gcs:
          $ref: '#/components/schemas/sandboxapi.GCSMountSpec'
        id:
          type: string
          maxLength: 64
        mount_path:
          type: string
        read_only:
          type: boolean
        type:
          enum:
            - gcs
          allOf:
            - $ref: '#/components/schemas/sandboxapi.MountKind'
      not:
        anyOf:
          - required:
              - s3
          - required:
              - git
          - required:
              - contexthub
    sandboxapi.GitRepoMountSpec:
      type: object
      required:
        - id
        - mount_path
        - type
        - git
      properties:
        git:
          $ref: '#/components/schemas/sandboxapi.GitMountSpec'
        id:
          type: string
          maxLength: 64
        mount_path:
          type: string
        read_only:
          type: boolean
        type:
          enum:
            - git
          allOf:
            - $ref: '#/components/schemas/sandboxapi.MountKind'
      not:
        anyOf:
          - required:
              - s3
          - required:
              - gcs
          - required:
              - contexthub
    sandboxapi.ContextHubRepoMountSpec:
      type: object
      required:
        - id
        - mount_path
        - type
        - contexthub
      properties:
        contexthub:
          $ref: '#/components/schemas/sandboxapi.ContextHubMountSpec'
        id:
          type: string
          maxLength: 64
        mount_path:
          type: string
        read_only:
          type: boolean
        type:
          enum:
            - contexthub
          allOf:
            - $ref: '#/components/schemas/sandboxapi.MountKind'
      not:
        anyOf:
          - required:
              - s3
          - required:
              - gcs
          - required:
              - git
    sandboxes.ProxyHeader:
      type: object
      required:
        - name
        - type
      properties:
        is_set:
          type: boolean
        name:
          type: string
        type:
          enum:
            - plaintext
            - opaque
            - workspace_secret
          allOf:
            - $ref: '#/components/schemas/sandboxes.HeaderType'
        value:
          type: string
    sandboxes.ProxyAWSConfig:
      type: object
      oneOf:
        - $ref: '#/components/schemas/sandboxes.ProxyAWSRoleConfig'
        - $ref: '#/components/schemas/sandboxes.ProxyAWSStaticConfig'
    sandboxes.ProxyGCPConfig:
      type: object
      required:
        - scopes
        - service_account_json
      properties:
        scopes:
          type: array
          minItems: 1
          items:
            type: string
        service_account_json:
          $ref: '#/components/schemas/sandboxes.ProxySecretValue'
    sandboxes.SandboxAWSMountRoleAuthConfig:
      type: object
      properties:
        role_arn:
          description: >-
            IAM role to assume with permissions scoped to the configured S3
            mounts.

            Mutually exclusive with static credentials. Configure only at
            creation.
          type: string
          minLength: 1
      required:
        - role_arn
      additionalProperties: false
    sandboxes.SandboxAWSMountStaticAuthConfig:
      type: object
      properties:
        access_key_id:
          $ref: '#/components/schemas/sandboxes.ProxySecretValue'
        role_arn:
          description: >-
            IAM role to assume with permissions scoped to the configured S3
            mounts.

            Mutually exclusive with static credentials. Configure only at
            creation.
          type: string
          enum:
            - ''
        secret_access_key:
          $ref: '#/components/schemas/sandboxes.ProxySecretValue'
      required:
        - access_key_id
        - secret_access_key
    sandboxes.ProxySecretValue:
      type: object
      required:
        - type
      properties:
        is_set:
          type: boolean
        type:
          enum:
            - plaintext
            - opaque
            - workspace_secret
          allOf:
            - $ref: '#/components/schemas/sandboxes.HeaderType'
        value:
          type: string
    sandboxapi.GitMountRefSpec:
      type: object
      required:
        - name
        - type
      properties:
        name:
          type: string
        type:
          type: string
          enum:
            - branch
            - tag
    sandboxes.HeaderType:
      type: string
      enum:
        - plaintext
        - opaque
        - workspace_secret
      x-enum-varnames:
        - HeaderTypePlaintext
        - HeaderTypeOpaque
        - HeaderTypeWorkspaceSecret
    sandboxes.ProxyAWSRoleConfig:
      type: object
      properties:
        role_arn:
          description: >-
            RoleARN selects automatically renewed IAM-role credentials instead
            of static keys.

            Access follows the role's effective AWS permissions, not the
            sandbox's mount scope.

            Configure at creation; the role cannot be changed afterward.
          type: string
          minLength: 1
      required:
        - role_arn
      not:
        anyOf:
          - required:
              - access_key_id
          - required:
              - secret_access_key
    sandboxes.ProxyAWSStaticConfig:
      type: object
      properties:
        access_key_id:
          $ref: '#/components/schemas/sandboxes.ProxySecretValue'
        role_arn:
          description: >-
            RoleARN selects automatically renewed IAM-role credentials instead
            of static keys.

            Access follows the role's effective AWS permissions, not the
            sandbox's mount scope.

            Configure at creation; the role cannot be changed afterward.
          type: string
          enum:
            - ''
        secret_access_key:
          $ref: '#/components/schemas/sandboxes.ProxySecretValue'
      required:
        - access_key_id
        - secret_access_key
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
