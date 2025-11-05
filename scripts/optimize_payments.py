def prioritize_payments(debts, liquidity):
    sorted_debts = sorted(debts, key=lambda x: x['interest_rate'], reverse=True)
    payments = []
    for debt in sorted_debts:
        if liquidity <= 0:
            break
        pay = min(debt['amount_due'], liquidity)
        payments.append({'card': debt['card_name'], 'payment': pay})
        liquidity -= pay
    return payments
  add optimize_payments.py script
