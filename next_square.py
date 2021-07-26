from math import *


def find_next_square(sq):
    """Kata URL : https://www.codewars.com/kata/56269eb78ad2e4ced1000013"""
    return (sqrt(sq)+1)**2 if sqrt(sq) % 1 == 0 else -1
