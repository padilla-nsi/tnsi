"""
Author: Pascal Padilla
Source: correction de l'exercice 1 du sujet 36 des épreuves pratiques NSI 2022

Remarques:
    * /!\ attention ici c'est la occurrence qui est recherchée !
"""


def recherche(tab, n):
    """ Recherche la valeur de la dernière occurrence
    de n dans le tableau tab.

    Args:
        tab (list): tableau non vide de nb entiers
        n (int) : nombre entier à rechercher

    Returns:
        int : indice de la dernière valeur recherchée ou 
              -1 si absent du tableau

    Tests et Exemples:
    >>> recherche([5, 3], 1)
    2
    >>> recherche([2, 4], 2)
    0
    >>> recherche([2, 3, 5, 2, 4], 2)
    3
    """
    longueur = len(tab)

    # BOUCLE
    # -> invariant: i_n est l'indice de la dernière apparition de n
    # dans la zone tab[0 .. i-1] ou la longueur du tableau si n n'y est pas
    i_n = longueur

    # -> condition d'arrêt: après la boucle i <- n
    for i in range(longueur):
        if tab[i] == n:
            i_n = i

    # fin BOUCLE
    # tout le tableau est parcouru
    return i_n


# vérification avec des assertions
assert recherche([5, 3], 1) == 2
assert recherche([2, 4], 2) == 0
assert recherche([2, 3, 5, 2, 4], 2) == 3

# vérification avec des affichages
print(recherche([5, 3], 1))
print(recherche([2, 4], 2))
print(recherche([2, 3, 5, 2, 4], 2))

# vérification avec doctest
from doctest import testmod
testmod()
