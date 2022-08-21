from datetime import datetime, timedelta


def get_investiments(inventiments, cashflows):
    for investment in inventiments:
        date_obj = datetime.strptime(investment["created_at"], '%Y-%m-%d')
        investment_amount = (-float(investment["amount"]))
        if date_obj in cashflows:
            cashflows[date_obj] += investment_amount
        else:
            cashflows[date_obj] = investment_amount
    return cashflows


def get_installments(installments, cashflows):
    for installment in installments:
        date_obj = datetime.strptime(installment["due_date"], '%Y-%m-%d')
        installment_amount = (float(installment["amount"]))
        if date_obj in cashflows:
            cashflows[date_obj] += installment_amount
        else:
            cashflows[date_obj] = installment_amount
    return cashflows


def complete_day_intervall(cashflows):
    min_day = min(cashflows.keys())
    max_day = max(cashflows.keys())

    database = min_day
    while database < max_day:
        if database not in cashflows:
            cashflows[database] = 0.0
        database += timedelta(days=1)
    cashflows = dict(sorted(cashflows.items()))
    return cashflows
