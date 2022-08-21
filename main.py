from cashflow import get_investiments, get_installments, complete_day_intervall
from investments import investments
from installments import installments
import numpy_financial as npf

cashflows = {}


def calc_irr():
    data = []
    get_investiments(investments, cashflows)
    get_installments(installments, cashflows)
    complete_day_intervall(cashflows)

    for amount in cashflows.values():
        data.append(amount)

    irr = round(npf.irr(data), 2)
    print("TIR:", irr)


if __name__ == "__main__":
    calc_irr()
