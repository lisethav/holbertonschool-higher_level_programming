#!/usr/bin/python3
"""
This is the add_integer module
If an input is a float, it is cast automatically to an integer.
Return the add of two integers
"""

def add_integer(a, b):
    """
    Function add_integer:
    First check if the input is correct,
    if then cast both into ints and return the sum of the result.
    """
    try:
        if isinstance(a, (int, float)) is False:
            raise TypeError('a must be an integer')
        elif isinstance(b, (int, float)) is False:
            raise TypeError('b must be an integer')
        return(int(a) + int(b))
    except:
        raise
