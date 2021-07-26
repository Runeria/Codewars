def nb_year(p0, percent, aug, final):
    """Kata URL : https://www.codewars.com/kata/563b662a59afc2b5120000c6"""
    year = 0
    more = p0
    pourcent = percent / 100
    while more < final:
        more = int(more + more * pourcent + aug)
        year += 1
    return year
