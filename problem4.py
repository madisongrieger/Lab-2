def sum_coins(num_pennies, num_nickels, num_dimes, num_quaters):
  """
  number -> number
  takes the number of coins and finds the total sum
  >>> sum_coins(1,2,3,4)
  1.41
  >>> sum_coins(2,4,6,8)
  2.82
  """ 
  total_dollars=(num_pennies*.01+ num_nickels*.05+ num_dimes*.10+ num_quaters*.25)
  return total_dollars

def return_amount(amount_paid, amount_owed):
  """
  number -> number 
  takes the number paid and substracts the number owed
  >>> return_amount(12,4)
  8
  >>> return_amount(25,5)
  20
  """
  amount_left= amount_paid-amount_owed
  return amount_left
 sum_coins(1,2,3,4)
 return_amount(12,4) 
