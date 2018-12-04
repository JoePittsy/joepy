#!/usr/bin/python3
# By Joseph Pitts

import math
    
def clamp(value, minimum, maximum):
    """ Clamps a value between a minimum and a maximum

    >>> clamp(20, 40, 50)
    40
    >>> clamp(90, 40, 50)
    50
    """
    if value < minimum:
        return minimum
    elif value > maximum:
        return maximum
    else:
        return value

def scale(value, lower_bound, upper_bound, target_lower, target_upper):
    """ Re-maps a number from one range to another. 
    >>> scale(0.5, 0, 10, 0, 100)
    5.0
    """
    return ((value-lower_bound)/(upper_bound-lower_bound))*(target_upper-target_lower)+target_lower

def dist(x1, y1, x2, y2):
    '''Calculates the distance between two points.
    >>> dist(0, 0, 20 , 0)
    20.0
    >>> dist(1, 3.7, 6 , 94)
    90.43832152356654
    '''
    a = x2 - x1
    b = y2 - y1
    return math.sqrt(
            a*a +
            b*b)

def lerp(value_one, value_two, amount):
    """ Step from one value too another
    >>> lerp(0, 20, 0.5) 
    10.0
    """
    if amount < 0 or amount > 1:
            raise AttributeError("Lerp ammount must be between 0 and 1!")
    else:
        
        return (1 - amount) * value_one + amount * value_two
      
if __name__ == "__main__":
    import doctest
    doctest.testmod()

