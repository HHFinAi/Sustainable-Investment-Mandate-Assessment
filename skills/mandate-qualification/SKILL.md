---
name: mandate-qualification
description: Issuer sustainable-investment evidence for institutional sustainable-finance research; return evidence-linked findings, assumptions, gaps and reviewable outputs.
license: MIT
metadata:
  author: HHFinAi
  version: "0.2.0"
---
# Issuer sustainable-investment evidence

Read `../../AGENTS.md` and `../../prompts/stages/qualification.md` relative to this skill directory. Obtain the current stage packet using the repository CLI. Do not create or claim unavailable source access.

## Task
Keep contribution, do-no-significant-harm and good governance separately supported under the approved methodology. Taxonomy eligibility is not alignment. Do not infer sustainable-investment qualification solely from an ESG rating, sector label or SDG mapping.

## Deliverable
Return the fields in `../../schemas/artifact.schema.json`; use the current run ID and input digest. Required sections: contribution_test, dnsh_adverse_impacts, governance, taxonomy_separate. Include source IDs, scope, periods, methods and material gaps. Call only allowlisted calculations with explicit provenance; missing evidence means NEEDS_DATA, not invented values.

## Limit
This is evidence and arithmetic support, not legal advice, automatic SFDR classification, fund certification or a full EU Taxonomy calculator. Unknown evidence is not a pass. Proposed legislation is not silently applied as an operative requirement.
