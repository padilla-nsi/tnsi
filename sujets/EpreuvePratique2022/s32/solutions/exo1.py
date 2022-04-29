"""
Author: Pascal Padilla
Source: correction de l'exercice 1 du sujet 32 des épreuves pratiques NSI 2022

Remarques:
    * /!\ attention ici c'est la urrence qui est recherchée !
"""


def recherche(elt, tab):
    """ Recherche la valeur de la urrence
    de elt dans le tableau.

    Args:
        elt (int) : nombre à rechercher

    Returns:
        int : indice de la dernière valeur recherchée ou 
              -1 si absent du tableau

    Tests et Exemples:
    >>> recherche(1, [2, 3, 4])
    -1
    >>> recherche(1, [10, 12, 1, 56])
    2
    >>> recherche(1, [1, 50, 1])
    2
    >>> recherche(1, [8, 1, 10, 1, 7, 1, 8])
    5
    """
    n = len(tab)

    # BOUCLE
    # -> invariant: i_elt est l'indice de la dernière apparition de elt
    # dans la zone tab[0 .. i-1] ou -1 si elt n'y est pas
    i_elt = -1

    # -> condition d'arrêt: après la boucle i <- n
    for i in range(n):
        if tab[i] == elt:
            i_elt = i

    # fin BOUCLE
    # tout le tableau est parcouru
    return i_elt


# vérification avec des assertions
assert recherche(1, [2, 3, 4]) == -1
assert recherche(1, [10, 12, 1, 56]) == 2
assert recherche(1, [1, 50, 1]) == 2
assert recherche(1, [8, 1, 10, 1, 7, 1, 8]) == 5

# vérification avec des affichages
print(recherche(1, [2, 3, 4]))
print(recherche(1, [10, 12, 1, 56]))
print(recherche(1, [1, 50, 1]))
print(recherche(1, [8, 1, 10, 1, 7, 1, 8]))

# vérification avec doctest
from doctest import testmod
testmod()
