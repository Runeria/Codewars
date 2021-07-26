from math import *


def is_square(n):
    """"Kata URL : https://www.codewars.com/kata/59441520102eaa25260000bf """
    if n < 0:
        return False
        print(f"{n}: Negative numbers cannot be square numbers")

    elif sqrt(n) % 1 == 0:
        return True
        print(f"{n} is a square number ({sqrt(n)} * {sqrt(n)})")

    else:
        return False
        print(f"{n} is not a square number")
