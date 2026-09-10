import math
def circle_area(radius):
  """
  positive whole number-> positive whole number
  takes the radius and finds the area
  
  >>> circle_area(10)
  314.1592653589793
  >>> circle_area(4)
  50.26548245743669
  """
  return math.pi * (radius**2)

def square_area(side):
   """
   positive whole number -> positive whole number
   takes a number and finds the area
   
   >>> square_area(3)
   9
   >>> square_area(10)
   100
   """
   return side **2

def inscribed_area(side):
   """
   positive whole number ->positive whole number
   takes the areas and subtracts one by the other
   
   >>> inscribed_area(12)
   30.902664470767448
   >>> inscribed_area(30)
   193.14165294229656
   """
   return square_area(side) - circle_area(side/2)
inscribed_area(12)
