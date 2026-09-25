# Investment committee and accountable review

## Decision context
Does the evidence support the stated fund mandate under the versioned prospectus and applicable rulebook, and where is the result unknown?

## Assignment
Integrate findings without changing their qualification. Separate facts, inferences, assumptions and calculations; cite evidence IDs and dates. Preserve unknown conclusions. Complete the domain-assessment declarations, register unresolved material issues, and submit for human research review. Do not certify legal compliance or investment performance.

## Required output sections
- `investment_question_and_answer`: substantive analysis linked to claim IDs.
- `financial_vs_sustainability_conclusions`: substantive analysis linked to claim IDs.
- `evidence_and_calculations`: substantive analysis linked to claim IDs.
- `decision_conditions_and_limits`: substantive analysis linked to claim IDs.

## Evidence and methodology
Use the mandate and registered primary evidence with edition, applicability, date and limitations. Source references are in `references/standards.json` from the repository root.

## Return contract
Return the structured artifact in `schemas/artifact.schema.json`; copy run_id, input_digest, stage_id and revision from the current packet. Never recycle IDs from a demo. Source uncertainty is not resolved by lowering confidence alone: preserve a gap or issue.

## Domain boundary
This is evidence and arithmetic support, not legal advice, automatic SFDR classification, fund certification or a full EU Taxonomy calculator. Unknown evidence is not a pass. Proposed legislation is not silently applied as an operative requirement.

Required typed domain-assessment fields (declarations, not automated truth verification):
```json
{
  "rulebook_verified": [
    "verified_for_scope",
    "not_verified"
  ],
  "issuer_not_product_classification": [
    true
  ],
  "unknown_not_pass": [
    true
  ],
  "legal_certification": [
    false
  ],
  "proposal_as_law": [
    false
  ]
}
```
