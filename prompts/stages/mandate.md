# Mandate and investable decision

## Decision context
Does the evidence support the stated fund mandate under the versioned prospectus and applicable rulebook, and where is the result unknown?

## Assignment
Identify decision owner, objective, benchmark, time horizon, currency, jurisdiction, risk budget and instrument. Specify whether output supports equity, credit, portfolio constraints or a private contract. A research theme is not a security. Missing material instructions require NEEDS_DATA. Do not execute trades or communicate externally.

## Required output sections
- `decision_question`: substantive analysis linked to claim IDs.
- `instrument_boundary`: substantive analysis linked to claim IDs.
- `mandate_constraints`: substantive analysis linked to claim IDs.

## Evidence and methodology
Use the mandate and registered primary evidence with edition, applicability, date and limitations. Source references are in `references/standards.json` from the repository root.

## Return contract
Return the structured artifact in `schemas/artifact.schema.json`; copy run_id, input_digest, stage_id and revision from the current packet. Never recycle IDs from a demo. Source uncertainty is not resolved by lowering confidence alone: preserve a gap or issue.

## Domain boundary
This is evidence and arithmetic support, not legal advice, automatic SFDR classification, fund certification or a full EU Taxonomy calculator. Unknown evidence is not a pass. Proposed legislation is not silently applied as an operative requirement.
