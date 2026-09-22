---
title: "reference/python/langchain/agents/middleware/_redaction"
description: "Index of 14 pages and 4 subdirectories under reference/python/langchain/agents/middleware/_redaction."
category: "index"
tags: [index, reference, python, langchain, agents, middleware, redaction]
---

# reference/python/langchain/agents/middleware/_redaction

14 pages here, 28 pages including subdirectories.

## Directories

- [PIIDetectionError/](PIIDetectionError/_index.md) - 2 pages
- [PIIMatch/](PIIMatch/_index.md) - 4 pages
- [RedactionRule/](RedactionRule/_index.md) - 4 pages
- [ResolvedRedactionRule/](ResolvedRedactionRule/_index.md) - 4 pages

## Files

- [BUILTIN_DETECTORS](BUILTIN_DETECTORS.md) - Registry of built-in detectors keyed by type name.
- [Detector](Detector.md) - Callable signature for detectors that locate sensitive values.
- [PIIDetectionError](PIIDetectionError.md) - Raised when configured to block on detected sensitive values.
- [PIIMatch](PIIMatch.md) - Represents an individual match of sensitive data.
- [RedactionRule](RedactionRule.md) - Configuration for handling a single PII type.
- [RedactionStrategy](RedactionStrategy.md) - Supported strategies for handling detected sensitive values.
- [ResolvedRedactionRule](ResolvedRedactionRule.md) - Resolved redaction rule ready for execution.
- [apply_strategy](apply_strategy.md) - Apply the configured strategy to matches within content.
- [detect_credit_card](detect_credit_card.md) - Detect credit card numbers in content using Luhn validation.
- [detect_email](detect_email.md) - Detect email addresses in content.
- [detect_ip](detect_ip.md) - Detect IPv4 or IPv6 addresses in content.
- [detect_mac_address](detect_mac_address.md) - Detect MAC addresses in content.
- [detect_url](detect_url.md) - Detect URLs in content using regex and stdlib validation.
- [resolve_detector](resolve_detector.md) - Return a callable detector for the given configuration.
