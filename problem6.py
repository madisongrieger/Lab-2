def BMI(height, weight):
    """
    positive whole number, positive number -> positive number
    takes in height and weight to calculate BMI

    >>> BMI(68,150)
    22.80493079584775
    >>> BMI(75,180)
    22.496000000000002
    """
    Index=(weight/ height**2) * 703
    return Index
BMI(68,150)    
    
