# Worked example — Sustainable-Investment Mandate Assessment Agent

**SYNTHETIC / RESEARCH_ONLY. All company, portfolio, instrument and outcome values are fictional. No capital should be deployed from this example.**

## Investment-relevant observation
With 55% confirmed qualifying, 20% confirmed non-qualifying and 25% unknown, the qualifying share is bounded by **55%–80%**. Against the fictional user-supplied 70% threshold, the result is **UNKNOWN**.

## Reproduce the arithmetic
From the repository root:
```bash
python -m sf_agent calc --operation mandate_bounds --arguments examples/calculation-arguments.json
```

### Inputs
```json
{
  "confirmed_pass_weight": 0.55,
  "confirmed_fail_weight": 0.2,
  "unknown_weight": 0.25,
  "minimum_weight": 0.7
}
```

### Recomputed result
```json
{
  "lower_bound": 0.55,
  "upper_bound": 0.8,
  "minimum": 0.7,
  "result": "UNKNOWN",
  "legal_certification": false
}
```

## What the result does not establish
The 70% input is a demonstration, not a universal SFDR threshold. Obtain the fund-specific signed mandate, denominator conventions and applicable rules. Contribution, DNSH, governance and any separate taxonomy requirement need their own evidence; this one arithmetic bound cannot certify the fund.

## Diligence handoff
Fictional fund: 55% confirmed qualifying, 20% non-qualifying and 25% unknown against a user-supplied 70% test produces UNKNOWN, not a pass.

Register source-backed inputs, contrary evidence, material data gaps and the investment constraints before replacing this illustrative result with actual research. Unit, boundary, timing, attribution and legal judgments are not supplied by arithmetic alone. No human research approval is recorded for this example.
