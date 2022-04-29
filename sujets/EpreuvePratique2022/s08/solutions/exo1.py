"""
Author: Pascal Padilla
Source: correction de l'exercice 1 du sujet 8 des épreuves pratiques NSI 2022

Remarques:
"""


def recherche(elt, tab):
    """ Recherche la valeur elt dans le tableau.

    Args:
        elt (int) : nombre à rechercher
    
    Returns:
        int : indice de la valeur recherchée ou 
            -1 si absent du tableau
    
    Tests et Exemples:
    >>> recherche(1, [2, 3, 4])
    -1
    >>> recherche(1, [10, 12, 1, 56])
    2
    >>> recherche(50, [1, 50, 1])
    1
    >>> recherche(15, [8, 9, 10, 15])
    3
    """
    n = len(tab)
    for i in range(n):
        if tab[i] == elt:
            return i
    return -1


# vérification avec des assertions
assert recherche(1, [2, 3, 4]) == -1
assert recherche(1, [10, 12, 1, 56]) == 2
assert recherche(50, [1, 50, 1]) == 1
assert recherche(15, [8, 9, 10, 15]) == 3

# vérification avec des affichages
print(recherche(1, [2, 3, 4]))
print(recherche(1, [10, 12, 1, 56]))
print(recherche(50, [1, 50, 1]))
print(recherche(15, [8, 9, 10, 15]))

# vérification avec doctest
from doctest import testmod
testmod()