import math
def cylinder_volume(radius, height):
    """ 
    positive whole number positive whole number -> number
    takes the radius and height and outputs volume
    
    >>> cylinder_volume(1,2)
    6.283185307179586
    >>> cylinder_volume(3,4)
    113.09733552923255
    """
    volume= math.pi * (radius**2) * height
    print(volume)
cylinder_volume(1,2)
