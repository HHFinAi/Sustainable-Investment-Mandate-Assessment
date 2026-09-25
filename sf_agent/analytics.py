"""User-supplied mandate arithmetic, not a legal rulebook or automatic certification."""
from __future__ import annotations
from .maths import COMMON_OPERATIONS, checked, fraction, number, operation, positive, require
from .validation import sequence, mapping, text

@operation({'confirmed_pass_weight':'decimal','confirmed_fail_weight':'decimal','unknown_weight':'decimal','minimum_weight':'decimal'},'mandate_bounds')
def mandate_bounds(confirmed_pass_weight: float,confirmed_fail_weight: float,unknown_weight: float,minimum_weight: float) -> dict:
    p=fraction(confirmed_pass_weight,'confirmed_pass_weight');f=fraction(confirmed_fail_weight,'confirmed_fail_weight');u=fraction(unknown_weight,'unknown_weight');m=fraction(minimum_weight,'minimum_weight')
    require(abs(p+f+u-1)<=1e-9,'weights must reconcile to one under the supplied denominator')
    status='MET_ARITHMETICALLY' if p+1e-12>=m else ('NOT_MET' if p+u+1e-12<m else 'UNKNOWN')
    return {'lower_bound':p,'upper_bound':p+u,'minimum':m,'result':status,'legal_certification':False}

@operation({'rules':'rule_records'},'mandatory_rule_result')
def combine_mandatory_rules(rules: list[dict]) -> dict:
    sequence(rules,'rules',True);ids=set();fails=[];unknown=[];tested=0
    for r in rules:
        mapping(r,'rule');rid=text(r.get('id'),'rule.id');require(rid not in ids,'duplicate rule id');ids.add(rid)
        result=r.get('result');require(result in {'PASS','FAIL','UNKNOWN','NOT_APPLICABLE'},'invalid rule result')
        text(r.get('basis'),'rule basis');text(r.get('source_ref'),'rule source_ref')
        if result=='NOT_APPLICABLE':text(r.get('non_applicability_reason'),'non-applicability reason')
        else:tested+=1
        if result=='FAIL':fails.append(rid)
        if result=='UNKNOWN':unknown.append(rid)
    status='FAIL' if fails else ('UNKNOWN' if unknown or tested==0 else 'PASS_DECLARED_TESTS')
    return {'result':status,'failed_rules':fails,'unknown_rules':unknown,'applicable_rules':tested,'legal_certification':False}

@operation({'current_nav':'$money','current_qualifying':'$money','sale_qualifying':'$money','purchase_qualifying':'$money','net_flow':'$money'},'post_trade_qualifying_fraction')
def post_trade_fraction(current_nav: float,current_qualifying: float,sale_qualifying: float,purchase_qualifying: float,net_flow: float) -> dict:
    nav=positive(current_nav,'current_nav');q=checked(current_qualifying,'current_qualifying',0,nav)
    sale=checked(sale_qualifying,'sale_qualifying',0,q);buy=checked(purchase_qualifying,'purchase_qualifying',0);flow=number(net_flow,'net_flow')
    newnav=positive(nav+flow,'post-flow NAV');newq=q-sale+buy
    require(newq<=newnav+1e-9,'qualifying amount exceeds post-flow NAV')
    return {'post_trade_qualifying_amount':newq,'post_flow_nav':newnav,'fraction':newq/newnav,
            'assumes_trades_at_book_value_no_costs':True}
OPERATIONS=dict(COMMON_OPERATIONS)
OPERATIONS.update({f.__name__:f for f in (mandate_bounds,combine_mandatory_rules,post_trade_fraction)})
