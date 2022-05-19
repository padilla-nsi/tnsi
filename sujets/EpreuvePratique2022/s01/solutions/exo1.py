"""
Author: Pascal Padilla
Source: correction de l'exercice 1 du sujet 1 des épreuves pratiques NSI 2022

Remarques:
"""


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
    # Invariant -> `total` vaut le nombre d'occurrences de 'caractere' rencontrés
    for i in range(n_mot):
        carac_courant = mot[i]
        if carac_courant == caractere:
            total = total + 1
    return total


# Tests avec des assertions
assert recherche('e', "sciences") == 2
assert recherche('i',"mississippi") == 4
assert recherche('a',"mississippi") == 0

# Tests avec doctest
from doctest import testmod
testmod()