alphabet = "abcdefghijklmnopqrstuvwxyz"


def is_pangram(s):
    """Kata URL : https://www.codewars.com/kata/545cedaa9943f7fe7b000048"""
    for letter in alphabet:
        if letter not in s.lower():
            return False
    return True
