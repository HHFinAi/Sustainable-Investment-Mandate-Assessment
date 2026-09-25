---
name: mandate-compliance
description: Independent interpretation and sign-off preparation for institutional sustainable-finance research; return evidence-linked findings, assumptions, gaps and reviewable outputs.
license: MIT
metadata:
  author: HHFinAi
  version: "0.2.0"
---
# Independent interpretation and sign-off preparation

Read `../../AGENTS.md` and `../../prompts/stages/compliance.md` relative to this skill directory. Obtain the current stage packet using the repository CLI. Do not create or claim unavailable source access.

## Task
Produce a dated dossier with every rule, source, observation and uncertainty. Any unresolved interpretation remains NEEDS_DATA or a declared issue. No automatic public disclosure, reclassification or claim of compliance. Queue human compliance/legal review.

## Deliverable
Return the fields in `../../schemas/artifact.schema.json`; use the current run ID and input digest. Required sections: exceptions_and_breaches, remediation_options, disclosure_consistency, compliance_review. Include source IDs, scope, periods, methods and material gaps. Call only allowlisted calculations with explicit provenance; missing evidence means NEEDS_DATA, not invented values.

## Limit
This is evidence and arithmetic support, not legal advice, automatic SFDR classification, fund certification or a full EU Taxonomy calculator. Unknown evidence is not a pass. Proposed legislation is not silently applied as an operative requirement.
