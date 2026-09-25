---
name: mandate-valuation
description: Portfolio thresholds and uncertainty for institutional sustainable-finance research; return evidence-linked findings, assumptions, gaps and reviewable outputs.
license: MIT
metadata:
  author: HHFinAi
  version: "0.2.0"
---
# Portfolio thresholds and uncertainty

Read `../../AGENTS.md` and `../../prompts/stages/valuation.md` relative to this skill directory. Obtain the current stage packet using the repository CLI. Do not create or claim unavailable source access.

## Task
Reconcile cash, derivatives, look-through, hedging, sovereign treatment and double counting to the user-approved rulebook. Calculate lower/upper bounds for a single confirmed-weight threshold; compute mandatory-gate results separately. The generic helper does not supply statutory thresholds or definitions.

## Deliverable
Return the fields in `../../schemas/artifact.schema.json`; use the current run ID and input digest. Required sections: denominator_reconciliation, confirmed_vs_unknown, mandatory_gates, exceptions. Include source IDs, scope, periods, methods and material gaps. Call only allowlisted calculations with explicit provenance; missing evidence means NEEDS_DATA, not invented values.

## Limit
This is evidence and arithmetic support, not legal advice, automatic SFDR classification, fund certification or a full EU Taxonomy calculator. Unknown evidence is not a pass. Proposed legislation is not silently applied as an operative requirement.
