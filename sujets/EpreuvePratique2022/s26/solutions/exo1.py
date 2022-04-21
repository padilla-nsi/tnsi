"""
Author: Pascal Padilla
Source: correction de l'exercice 1 du sujet 26 des épreuves pratiques NSI 2022

Remarques:
  * pas de noms de fonctions avec des majuscules
  * les noms doivent respecter le format snake_case : 
  RechercheMin -> recherche_min
"""


def RechercheMin(tab: list) -> int:
    """Renvoie l'indice de la première occurence du minimum

    Args:
        tab (list): tableau d'entiers relatifs

    Returns:
        int: indice du min du tableau

    Tests et exemples:
    >>> RechercheMin([5])
    0
    >>> RechercheMin([2, 4, 1])
    2
    >>> RechercheMin([5, 3, 2, 2, 4])
    2
    """
    # clause de garde (non demandée)
    n = len(tab)
    if n == 0:
        return None

    # BOUCLE
    # invariant
    #  -> i_min est l'indice du min de la zone tab[0 .. i-1]
    #  -> v_min est la valeur minimale de la zone tab[0 .. i-1]
    #  -> i est l'indice en cours d'analyse
    #
    # initialisation
    #  -> avec la première valeur du tableau
    #  (qui existe grâce à la clause de garde)
    #  -> i_min <- 0 et v_min <- tab[0]
    #  -> commencer à partir de la 2ème case: i <- 1
    i_min = 0
    v_min = tab[0]  # pas utile mais rend le code plus lisible !

    # condition d'arrêt:
    #  -> i sort du tableau: i >= n
    for i in range(1, n):
        # conservation de l'invariant
        # lorsqu'un élément plus petit est trouvé
        if tab[i] < v_min:
            i_min = i
            v_min = tab[i]

    # renvoie de l'indice de la valeur minimale
    return i_min


# tests avec des affichages
print(RechercheMin([5]))
print(RechercheMin([2, 4, 1]))
print(RechercheMin([5, 3, 2, 2, 4]))


# tests avec des assertions
assert RechercheMin([5]) == 0
assert RechercheMin([2, 4, 1]) == 2
assert RechercheMin([5, 3, 2, 2, 4]) == 2


# tests avec doctest
from doctest import testmod
testmod()
