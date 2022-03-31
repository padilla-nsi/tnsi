"""
Author: Pascal Padilla
Source: correction de l'exercice 2 du sujet 12 des épreuves pratiques NSI 2022
"""

from doctest import testmod


def tri(tab):
    """Tri un tableau de bits en plaçant les 0 au début
    et les 1 à la fin.

    Args:
        tab (list): tableau de 0 et de 1

    Returns:
        list: tableau trié

    Tests et Exemples:
    >>> tri([0,1,0,1,0,1,0,1,0])
    [0, 0, 0, 0, 0, 1, 1, 1, 1]
    """
    #i est le premier indice de la zone non triée, j le dernier indice.
    #Au debut, la zone non triée est le tableau entier.

    # La boucle en détail...
    # invariants en arrivant à chaque tour de boucle:
    #   * i est l'indice du début de la zone non triée
    #   * j est l'indice de fin de la zone non triée
    # initialisation:
    #   * i ← 0
    #   * j ← indice du dernier élément du tableau
    i= 0
    j= len(tab) - 1

    # condition d'arrêt:
    #   * la zone non triée est vide : i et j égaux
    while i != j :
        # cas d'un `0` trouvé :
        if tab[i]== 0:
            i= i + 1

        # cas d'un `1` et donc il faut procéder à une permutation
        else :
            valeur = tab[j]
            tab[j] = 1
            tab[i] = valeur
            j= j - 1
    # variants qui assure que la boucle s'arrête:
    #   * i incrémenté ou j décrémenté → la zone non triée diminue

    return tab


# Exemples
print(tri([0,1,0,1,0,1,0,1,0]))


# Tests
testmod()
