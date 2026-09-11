def BMI(height, weight):
    """
    positive whole number, positive number -> positive number
    takes in height and weight to calculate BMI

    >>> BMI(68,150)
    22.80925605536332
    >>> BMI(75,180)
    12.497777777777777.
    """
    Index=(weight/ height**2) * 703
    return Index
BMI(68,150)    
    
