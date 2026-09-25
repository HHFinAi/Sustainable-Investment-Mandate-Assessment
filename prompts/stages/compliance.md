# Independent interpretation and sign-off preparation

## Decision context
Does the evidence support the stated fund mandate under the versioned prospectus and applicable rulebook, and where is the result unknown?

## Assignment
Produce a dated dossier with every rule, source, observation and uncertainty. Any unresolved interpretation remains NEEDS_DATA or a declared issue. No automatic public disclosure, reclassification or claim of compliance. Queue human compliance/legal review.

## Required output sections
- `exceptions_and_breaches`: substantive analysis linked to claim IDs.
- `remediation_options`: substantive analysis linked to claim IDs.
- `disclosure_consistency`: substantive analysis linked to claim IDs.
- `compliance_review`: substantive analysis linked to claim IDs.

## Evidence and methodology
Use SFDR-BASE, FCA-SDR with edition, applicability, date and limitations. Source references are in `references/standards.json` from the repository root.

## Return contract
Return the structured artifact in `schemas/artifact.schema.json`; copy run_id, input_digest, stage_id and revision from the current packet. Never recycle IDs from a demo. Source uncertainty is not resolved by lowering confidence alone: preserve a gap or issue.

## Domain boundary
This is evidence and arithmetic support, not legal advice, automatic SFDR classification, fund certification or a full EU Taxonomy calculator. Unknown evidence is not a pass. Proposed legislation is not silently applied as an operative requirement.
