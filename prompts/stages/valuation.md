# Portfolio thresholds and uncertainty

## Decision context
Does the evidence support the stated fund mandate under the versioned prospectus and applicable rulebook, and where is the result unknown?

## Assignment
Reconcile cash, derivatives, look-through, hedging, sovereign treatment and double counting to the user-approved rulebook. Calculate lower/upper bounds for a single confirmed-weight threshold; compute mandatory-gate results separately. The generic helper does not supply statutory thresholds or definitions.

## Required output sections
- `denominator_reconciliation`: substantive analysis linked to claim IDs.
- `confirmed_vs_unknown`: substantive analysis linked to claim IDs.
- `mandatory_gates`: substantive analysis linked to claim IDs.
- `exceptions`: substantive analysis linked to claim IDs.

## Evidence and methodology
Use SFDR-BASE, FCA-SDR with edition, applicability, date and limitations. Source references are in `references/standards.json` from the repository root.

## Return contract
Return the structured artifact in `schemas/artifact.schema.json`; copy run_id, input_digest, stage_id and revision from the current packet. Never recycle IDs from a demo. Source uncertainty is not resolved by lowering confidence alone: preserve a gap or issue.

## Domain boundary
This is evidence and arithmetic support, not legal advice, automatic SFDR classification, fund certification or a full EU Taxonomy calculator. Unknown evidence is not a pass. Proposed legislation is not silently applied as an operative requirement.

A domain calculation must pass recomputation. The minimal runnable illustration is `mandate_bounds`; other needed specialist models must remain explicitly external and independently reviewed.
