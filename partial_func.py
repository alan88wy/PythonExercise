# Partial function - enable you to recreate function with specif value
from functools import partial

def power(base, exponent):
    return base ** exponent

# Example 1: Define a square
square = partial(power, exponent=2)

print("Square 3 : ",square(3))

cube = partial(power, exponent = 3)

print("Cube 2 : ", cube(2))
