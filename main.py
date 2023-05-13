"""You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth."""

customers = [[2, 145,60], [8, 118, 170], [12, 33, 97]]

def get_richest_customer(customers):
  account_totals = []
  for account in customers:
    account_totals.append(sum(account))
  print(account_totals)
  return account_totals.index(max(account_totals))



