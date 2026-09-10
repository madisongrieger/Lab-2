from math import log
def maturity(time, temp, ratio):
  """
  positive whole number positive whole number positive whole number positive whole number-> number 
  takes values and gives the maturity
 
  >>> maturity(1,2,3)
  24.805938295994117
  >>> maturity(2,4,6)
  191.40590457685655
  """
  answer= 23.7 * (time**3) + (temp / 273) + log(ratio)
  print(answer)
maturity(1,2,3)
