def maturity(time, temp, ratio):
  from math import log
answer= 23.7 * (time**3) + (temp / 273) + log(ratio)
print(answer)
