---
name: mandate-rulebook
description: Mandate and applicability register for institutional sustainable-finance research; return evidence-linked findings, assumptions, gaps and reviewable outputs.
license: MIT
metadata:
  author: HHFinAi
  version: "0.2.0"
---
# Mandate and applicability register

Read `../../AGENTS.md` and `../../prompts/stages/rulebook.md` relative to this skill directory. Obtain the current stage packet using the repository CLI. Do not create or claim unavailable source access.

## Task
Extract exact binding commitments from the signed prospectus/IMA and applicable legal text. Record jurisdiction, publication/effective dates, fund scope, denominator conventions and reviewer. Label proposed or negotiating texts separately; do not call issuers Article 8 or Article 9.

## Deliverable
Return the fields in `../../schemas/artifact.schema.json`; use the current run ID and input digest. Required sections: prospectus_binding_elements, jurisdiction_version_dates, product_vs_issuer, interpretation_log. Include source IDs, scope, periods, methods and material gaps. Call only allowlisted calculations with explicit provenance; missing evidence means NEEDS_DATA, not invented values.

## Limit
This is evidence and arithmetic support, not legal advice, automatic SFDR classification, fund certification or a full EU Taxonomy calculator. Unknown evidence is not a pass. Proposed legislation is not silently applied as an operative requirement.
