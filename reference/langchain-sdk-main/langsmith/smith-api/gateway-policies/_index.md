---
title: "langsmith/smith-api/gateway-policies"
description: "Index of 6 pages and 0 subdirectories under langsmith/smith-api/gateway-policies."
category: "index"
tags: [index, langsmith, smith-api, gateway-policies]
---

# langsmith/smith-api/gateway-policies

6 pages here.

## Files

- [Create a gateway policy](create-a-gateway-policy.md) - Creates a gateway policy for the calling organization.
- [Delete a gateway policy](delete-a-gateway-policy.md) - Deletes a gateway policy. Subsequent reads return 404.
- [Get a gateway policy](get-a-gateway-policy.md) - Returns a single gateway policy by id. Cross-org access is rejected with 404
- [List gateway policies](list-gateway-policies.md) - Returns every gateway policy in the current organization. The response includes both admin-created policies and runtime-materialized children of default_spend_cap and default_rate_limit policies...
- [Search gateway policies by subject value set](search-gateway-policies-by-subject-value-set.md) - Batch variant of GET /v1/platform/gateway-policies for fetching policies that match a set of subject_matcher_values under one subject_matcher_key. Accepts the values in a JSON body so callers can...
- [Update a gateway policy](update-a-gateway-policy.md) - Partially updates a gateway policy. Only fields present in the request body are applied; absent fields are left unchanged. policy_type is immutable — to change a policy's type, delete it and create a...
