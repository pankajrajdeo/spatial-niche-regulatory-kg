---
title: "langsmith/smith-api/sandboxes"
description: "Index of 34 pages and 0 subdirectories under langsmith/smith-api/sandboxes."
category: "index"
tags: [index, langsmith, smith-api, sandboxes]
---

# langsmith/smith-api/sandboxes

34 pages here.

## Files

- [Batch delete sandboxes](batch-delete-sandboxes.md) - Delete multiple sandboxes by name or UUID in a single request.
- [Capture a snapshot from a sandbox](capture-a-snapshot-from-a-sandbox.md) - Create a snapshot by capturing the current state of a sandbox or promoting an existing checkpoint.
- [Create a registry](create-a-registry.md) - Create a sandbox registry for pulling private images.
- [Create a sandbox](create-a-sandbox.md) - Create a new sandbox from a snapshot. Provide at most one of snapshot_id or snapshot_name; if neither is provided, the server uses the default snapshot. snapshot_name accepts a Docker-style name or...
- [Create a snapshot](create-a-snapshot.md) - Create a snapshot from a Docker image (async build).
- [Delete a registry](delete-a-registry.md) - Delete a sandbox registry by name.
- [Delete a sandbox](delete-a-sandbox.md) - Delete a sandbox by name or UUID. Tears down the sandbox runtime and removes the DB record.
- [Delete a snapshot](delete-a-snapshot.md) - Delete a snapshot by ID or by a Docker-style name[:tag] reference. The underlying storage is reclaimed asynchronously.
- [Download a sandbox file](download-a-sandbox-file-1.md) - Download file contents from a sandbox filesystem path. Supports HTTP range requests: send a Range header (for example bytes=0-1023) to receive a 206 with only that byte range. Every response carries...
- [Download a sandbox file](download-a-sandbox-file.md) - Download file contents from a sandbox filesystem path. Supports HTTP range requests: send a Range header (for example bytes=0-1023) to receive a 206 with only that byte range. Every response carries...
- [Execute a sandbox command over WebSocket](execute-a-sandbox-command-over-websocket.md) - Open a WebSocket connection for streaming command execution inside a sandbox.
- [Execute a sandbox command](execute-a-sandbox-command.md) - Execute a command inside a sandbox and return stdout, stderr, and exit code. Use the streaming execute endpoints for long-running commands that may exceed the synchronous request deadline.
- [Generate a sandbox file download link](generate-a-sandbox-file-download-link.md) - Generate a tokenized link that downloads a single file from a sandbox with no further authentication. This mints a token rather than creating an addressable resource, so it returns 200 with no...
- [Generate a service access token](generate-a-service-access-token.md) - Create a short-lived JWT for accessing an HTTP service running on a specific port inside a sandbox. Returns a browser_url (sets auth cookie via redirect), a service_url (for use with the...
- [Get a registry](get-a-registry.md) - Get a sandbox registry by name.
- [Get a sandbox](get-a-sandbox.md) - Retrieve a sandbox by name. Stale provisioning sandboxes are auto-failed.
- [Get a snapshot name](get-a-snapshot-name.md) - Get a snapshot name and every tag under it, with the snapshot each tag resolves to. To fetch one snapshot, use /api/v2/sandboxes/snapshots/{snapshot_id}.
- [Get a snapshot](get-a-snapshot.md) - Get a sandbox snapshot by ID or by a Docker-style reference. A bare name means name:latest, falling back to the newest ready untagged snapshot of that name. To list the tags under a name, use...
- [Get sandbox resource usage](get-sandbox-resource-usage.md) - Get current sandbox resource usage and quota limits for the workspace
- [Get sandbox status](get-sandbox-status.md) - Retrieve the lightweight status of a sandbox for polling.
- [Glob a sandbox filesystem](glob-a-sandbox-filesystem.md) - Find files under a root path matching a glob pattern (supports ). Entries are returned in lexical order by path.
- [Grep a sandbox filesystem](grep-a-sandbox-filesystem.md) - Search files under a root path for a literal text pattern (not a regex).
- [List hourly sandbox usage costs](list-hourly-sandbox-usage-costs.md) - Returns priced usage per sandbox or snapshot and UTC hour in the half-open requested interval. LCU uses the recorded compute amount for sandboxes; snapshots have zero LCU. LSU allocates the recorded...
- [List registries](list-registries.md) - List sandbox registries for pulling private images.
- [List sandboxes](list-sandboxes.md) - List sandboxes for the authenticated tenant, with optional filtering, sorting, and pagination. Page with page_size and cursor: replay the response's next_cursor until it comes back null, which is the...
- [List snapshots](list-snapshots.md) - List sandbox snapshots for the authenticated tenant, with optional filtering, sorting, and pagination. Page with page_size and cursor: replay the response's next_cursor until it comes back null...
- [Open a sandbox TCP tunnel](open-a-sandbox-tcp-tunnel.md) - Open a WebSocket tunnel to a specific port inside a sandbox.
- [Resume a streamed sandbox command](resume-a-streamed-sandbox-command.md) - Continue streaming a command started by the stream start endpoint. The offsets are also the ack for everything below them, which frees the sandbox's output buffer and unpauses a command waiting for...
- [Start a sandbox](start-a-sandbox.md) - Start a stopped or failed sandbox. This endpoint is not idempotent.
- [Start a streamed sandbox command](start-a-streamed-sandbox-command.md) - Execute a command inside a sandbox and stream stdout/stderr as Server-Sent Events with base64 payloads. Requires a sandbox on the v2 runtime. Passing a command_id reuses a running command instead of...
- [Stop a sandbox](stop-a-sandbox.md) - Stop a ready sandbox. This endpoint is not idempotent; the filesystem is preserved for later restart.
- [Update a registry](update-a-registry.md) - Update a sandbox registry's name and/or credentials.
- [Update a sandbox](update-a-sandbox.md) - Update a sandbox's display name, retention, resources, tags, or proxy configuration. The name must be unique within the tenant. Proxy configuration sent to a sandbox that is not running is stored and...
- [Upload a sandbox file](upload-a-sandbox-file.md) - Upload a file to a sandbox filesystem path.
