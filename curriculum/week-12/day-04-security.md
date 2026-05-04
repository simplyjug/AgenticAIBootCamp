# Day 4: Security & data privacy

## Learning objectives

- Threat-model **prompt injection** leading to **data exfiltration** via tools.
- Plan **PII** handling: redact logs, minimize retention, regional storage.

## Hands-on

1. Draw STRIDE-lite table for your agent (Spoofing, Tampering, Repudiation, Info disclosure, DoS, Elevation).
2. Write **tool allowlist** — anything not on list returns HTTP 403.
3. Document **secrets** handling: env vars, rotation, never in prompts.

## Concepts

- **Indirect injection** via retrieved documents — sanitize or isolate retrieval context.

## Done when

- [ ] Threat model one-pager.
- [ ] Two mitigations mapped to threats.

## Resources

- Simon Willison — prompt injection posts / talks (search)
