import math


def square(side):
    if isinstance(side, int):
        return side ** 2
    else:
     return math.ceil (side ** 2)