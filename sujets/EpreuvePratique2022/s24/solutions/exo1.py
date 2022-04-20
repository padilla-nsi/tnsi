"""
Author: Pascal Padilla
Source: correction de l'exercice 1 du sujet 24 des épreuves pratiques NSI 2022
"""


from doctest import testmod


def maxliste(tab: list[int]) -> int:
    """Renvoie le plus grand élément d'un tableau.

    Args:
        tab (list[int]): tableau d'entiers relatifs

    Returns:
        int: valeur maximale du tableau

    Tests et Exemples:
    >>> maxliste([98, 12, 104, 23, 131, 9])
    131
    >>> maxliste([-27, 24, -3, 15])
    24
    """
    # BOUCLE qui va parcourir tout le tableau
    # à partir de la 2ème case
    # -> invariant:
    #   * valeur_max est la plus grande valeur de la
    #   portion tab[0..i-1] du tableau
    # -> initialisation:
    #   * valeur_max: première valeur du tableau
    #   * i: 1 pour commencer à la 2ème case
    valeur_max = tab[0]

    taille = len(tab)
    for i in range(1, taille):
        # maintient de l'invariant si la valeur
        # courante est plus grande que val_max
        if tab[i] > valeur_max:
            valeur_max = tab[i]

    return valeur_max


# Tests avec des affichages
print(maxliste([98, 12, 104, 23, 131, 9]))
print(maxliste([-27, 24, -3, 15]))


# Tests avec des assertions:
assert maxliste([98, 12, 104, 23, 131, 9]) == 131
assert maxliste([-27, 24, -3, 15]) == 24


# Tests avec doctest
testmod()
