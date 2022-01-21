from doctest import testmod


def recherche(caractere: str, mot: str) -> int:
    """
    Exemples et tests:
    >>> recherche('e', "sciences")
    2
    >>> recherche('i', "mississippi")
    4
    >>> recherche('a', "mississippi")
    0
    """
    total = 0
    n_mot = len(mot)
    for i in range(n_mot):
        carac_courant = mot[i]
        if carac_courant == caractere:
            total = total + 1
    return total


assert recherche('e', "sciences") == 2
assert recherche('i',"mississippi") == 4
assert recherche('a',"mississippi") == 0

testmod()