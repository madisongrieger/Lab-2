def sum_coins(num_pennies, num_nickels, num_dimes, num_quaters):
 total_dollars=(num_pennies*.01+ num_nickels*.05+ num_dimes*.10+ num_quaters*.25)
 return total_dollars







def return_amount(amount_paid, amount_owed):
  """ float, float -> float
  amount_paid and amount_owed are dollar amounts
  Takes in the amount of money paid, subtracts the amount owed, in order to calculate the amount due back to the customer
  """
  amount_left= amount_paid-amount_owed
  return amount_left
