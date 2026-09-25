# Methodology and model boundaries

This is evidence and arithmetic support, not legal advice, automatic SFDR classification, fund certification or a full EU Taxonomy calculator. Unknown evidence is not a pass. Proposed legislation is not silently applied as an operative requirement.

## Analytical outputs
- Versioned mandate and binding-elements register
- Issuer contribution, DNSH and governance dossier
- Portfolio lower/upper compliance bounds
- Exception log and compliance-review packet

## Calculation library
The implementation is in `sf_agent/analytics.py`; generic helpers are in `sf_agent/maths.py`. Every exposed operation has argument-unit and result-unit metadata and is callable with `python -m sf_agent calc`. Arguments are not sourced automatically. See the operation inventory below, the worked example and domain regression tests.

### Mandate calculations
`mandate_bounds` requires confirmed pass, confirmed fail and unknown weights to sum to one. Lower bound=confirmed pass; upper bound=pass+unknown. A threshold is MET_ARITHMETICALLY only when the lower bound already satisfies it; NOT_MET when even the upper bound fails; otherwise UNKNOWN. Missing evidence is never itself a pass. This is one supplied threshold, not a whole legal or fund-classification test.

`combine_mandatory_rules` combines reviewed declarations: FAIL dominates UNKNOWN; PASS_DECLARED_TESTS requires all applicable tests to pass. NOT_APPLICABLE requires a rationale, but applicability is not independently proved. `post_trade_fraction` uses a constant-price, zero-fee book with net external flow and supplied qualifying buys/sales; it does not model derivatives, look-through, price movements or exact statutory denominator conventions. No hardcoded Article 8/9 minimum allocation or universal SDR classification is supplied.


## Evidence status
Causal and legal interpretations remain human judgments. The software is not a complete implementation or certification of the referenced standards. Read the exact applicable original documents; the dated source register gives the verification scope. Proposed changes and future validation dates must not be applied retrospectively or represented as current law.
