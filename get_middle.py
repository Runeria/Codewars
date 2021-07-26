def get_middle(word):

    """ Kata URL : https://www.codewars.com/kata/56747fd5cb988479af000028. """

    if len(word) % 2 == 0:
        i = len(word) // 2 - 1
        return word[i:i + 2]

    else:
        i = len(word) // 2
        return word[i]