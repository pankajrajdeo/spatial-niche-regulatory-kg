---
title: "LangSmith Incident on May 1, 2025"
description: "Full post-mortem of the May 1, 2025 LangSmith API outage: root cause analysis, incident timeline, and steps we&#39;re taking to improve reliability and monitoring."
source: "https://www.langchain.com/blog/langsmith-incident-on-may-1-2025"
category: "blog"
published: "2025-05-07T18:48:28.000Z"
author: "LangChain Accounts"
tags: [blog, langsmith-incident-on-may-1-2025]
---

# LangSmith Incident on May 1, 2025

Requests to the [US LangSmith API](https://api.smith.langchain.com/redoc?ref=blog.langchain.com) from both the [web application](https://smith.langchain.com/?ref=blog.langchain.com) and SDKs experienced an elevated error rate for 28 minutes on May 1, 2025 (starting at 14:35 UTC and ending at 15:03 UTC). During the incident window, approximately 55% of all API requests failed with a connection error. This impacted all endpoints accessible through the API, including endpoints for run ingestion and data fetching.

A conflicting DNS record was accidentally left over during a migration between certificate renewal automation technologies at the end of January. This conflicting record caused renewal to fail all attempts at rotation during the month of April. Once the certificate expired, the LangSmith UI showed "Your connection is not private" when loaded, and all new connection attempts to the LangSmith API failed if they verified SSL.

Once the root cause was identified, the conflicting DNS record was deleted and a manual SSL certificate renewal was triggered, which restored SSL connectivity.

This incident happened due to a combination of human error and lack of observability for cert renewal automation and SSL certificate expiry. The incident was not initially discovered with proactive monitoring - it was instead first reported by both internal and external users. This further pointed to observability gaps that needed closing.

# Incident timeline

💡

All timestamps are in UTC

| **Time** | **Event** |
| --- | --- |
| January 31, 2025 13:35 | Migration to new certificate renewal automation completed, new certificates issued |
| January 31, 2025 16:07 | Conflicting DNS record created via dangling Terraform code |
| April 1, 2025 | Certificate renewal automation begins failed attempts to renew |
| May 1, 2025 14:35 | Certificate expired |
| May 1, 2025 14:41 | Initial user report of certificate expiry error |
| May 1, 2025 14:47 | Root cause identified. |
| May 1, 2025 14:49 | Conflicting DNS record deleted. Manual request to renew certificate issued. |
| May 1, 2025 14:54 | Public incident status page published. |
| May 1, 2025 15:03 | New certificate issuance completed, availability restored. |

# Analysis

The indicators of certificate renewal failures included a certificate resource stuck in "pending" status and error logs in the component managing the renewal.

# Resolution

Once we identified the root cause, we were able to restore availability quickly by deleting the conflicting DNS record and manually requesting certificate renewal.

# Next Steps

The human error component of this incident involved:

- Missing deleting the conflicting Google-managed SSL certificate in Terraform code
- An incorrect assumption that we had certificate expiry monitors in place that would remain valid after migration

There were a few contributing factors to the duration of this incident and the slowness of our public response:

- Recent change of log destinations for Kubernetes system components omitted the new component, so manual troubleshooting was required
- Migration between status page providers in progress at the time - this delayed status page publishing

With all of this in mind, we have taken steps to prevent this failure — and others like it — from happening again:

1. Added certificate expiry monitors for LangSmith domains
2. Added monitors for significant drops in run ingestion volume
3. Ensured all Kubernetes system component logs are ingested
4. **In Progress**: Monitor error logs from all Kubernetes system namespaces
5. **In Progress**: Building an internal dashboard for critical Kubernetes system workflows like certificate renewal

We take the reliability of our platform seriously, and we will invest in this area and others to continue improving our incident response process and reliability.
