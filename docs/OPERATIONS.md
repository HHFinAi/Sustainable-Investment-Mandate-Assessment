# Executable operation catalogue

Every operation requires supplied assumptions/provenance. No market or issuer data are inferred.

## `combine_mandatory_rules`
```python
combine_mandatory_rules(rules: 'list[dict]') -> 'dict'
```
See source code and domain methodology for assumptions.

Input units: `{"rules": "rule_records"}`. Output unit/type: `mandatory_rule_result`.

## `dscr`
```python
dscr(cash_available: 'float', debt_service: 'float') -> 'float'
```
See source code and domain methodology for assumptions.

Input units: `{"cash_available": "$money", "debt_service": "$money"}`. Output unit/type: `multiple`.

## `holding_period_return`
```python
holding_period_return(initial_dirty_price: 'float', exit_dirty_price: 'float', cash_income: 'float', funding_cost: 'float', transaction_cost: 'float') -> 'float'
```
See source code and domain methodology for assumptions.

Input units: `{"initial_dirty_price": "$money", "exit_dirty_price": "$money", "cash_income": "$money", "funding_cost": "$money", "transaction_cost": "$money"}`. Output unit/type: `decimal_return`.

## `mandate_bounds`
```python
mandate_bounds(confirmed_pass_weight: 'float', confirmed_fail_weight: 'float', unknown_weight: 'float', minimum_weight: 'float') -> 'dict'
```
See source code and domain methodology for assumptions.

Input units: `{"confirmed_pass_weight": "decimal", "confirmed_fail_weight": "decimal", "unknown_weight": "decimal", "minimum_weight": "decimal"}`. Output unit/type: `mandate_bounds`.

## `npv`
```python
npv(cashflows: 'list[float]', annual_discount: 'float') -> 'float'
```
Periodic NPV; cashflows[0] is at time zero, then annual periods.

Input units: `{"cashflows": "$money", "annual_discount": "decimal"}`. Output unit/type: `$money`.

## `post_trade_fraction`
```python
post_trade_fraction(current_nav: 'float', current_qualifying: 'float', sale_qualifying: 'float', purchase_qualifying: 'float', net_flow: 'float') -> 'dict'
```
See source code and domain methodology for assumptions.

Input units: `{"current_nav": "$money", "current_qualifying": "$money", "sale_qualifying": "$money", "purchase_qualifying": "$money", "net_flow": "$money"}`. Output unit/type: `post_trade_qualifying_fraction`.

## `scale`
```python
scale(value: 'float', factor: 'float') -> 'float'
```
Explicit arithmetic conversion; external unit semantics need human review.

Input units: `{"value": "$input_unit", "factor": "conversion_factor"}`. Output unit/type: `$output_unit`.
