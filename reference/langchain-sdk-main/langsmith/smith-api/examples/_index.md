---
title: "langsmith/smith-api/examples"
description: "Index of 15 pages and 0 subdirectories under langsmith/smith-api/examples."
category: "index"
tags: [index, langsmith, smith-api, examples]
---

# langsmith/smith-api/examples

15 pages here.

## Files

- [Count examples](count-examples.md) - Count all examples by query params
- [Create example](create-example.md) - Create a new example.
- [Create examples](create-examples.md) - Create bulk examples.
- [Delete example](delete-example.md) - Soft delete an example. Only deletes the example in the 'latest' version of the dataset.
- [Delete examples](delete-examples.md) - Soft delete examples. Only deletes the examples in the 'latest' version of the dataset.
- [Hard delete examples](hard-delete-examples.md) - This endpoint hard deletes all versions of a dataset example(s). Deletion is performed by setting inputs, outputs, and metadata to null and deleting attachment files while keeping the example ID...
- [Legacy update examples](legacy-update-examples.md) - Legacy update examples in bulk. For update involving attachments, use PATCH /v1/platform/datasets/{dataset_id}/examples instead.
- [Read example](read-example.md) - Get a specific example.
- [Read examples](read-examples.md) - Get all examples by query params
- [Update example](update-example.md) - Update a specific example.
- [Update examples](update-examples.md) - This endpoint allows clients to update existing examples in a specified dataset by sending a multipart/form-data PATCH request. Each form part contains either JSON-encoded data or binary attachment...
- [Upload examples from csv](upload-examples-from-csv.md) - Upload examples from a CSV file.
- [Upload examples](upload-examples.md) - This endpoint allows clients to upload examples to a specified dataset by sending a multipart/form-data POST request. Each form part contains either JSON-encoded data or binary attachment files...
- [Validate example](validate-example.md) - Validate an example.
- [Validate examples](validate-examples.md) - Validate examples in bulk.
