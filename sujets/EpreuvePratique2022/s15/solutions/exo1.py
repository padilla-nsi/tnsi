"""
Author: Pascal Padilla
Source: correction de l'exercice 1 du sujet 15 des épreuves pratiques NSI 2022

Remarque: une version plus 'pythonesque' du code consiste à remplacer
'for i in range(len(tab)):' par → 'for val in tab:'
et du coup 'tab[i]' devient → 'val'.
"""


from doctest import testmod


def nb_repetitions(elt, tab: list) -> int:
    """Renvoie le nombre de fois où l'élément 'elt' apparaît
    dans le tableau 'tab'.capitalize()

    Args:
        elt (_type_): élément à dénombrer
        tab (list): tableau contenant (ou pas) l'élément

    Returns:
        int: nombre d'occurrences de 'elt'.

    Tests et exemples:
    >>> nb_repetitions(5,[2, 5, 3, 5, 6, 9, 5])
    3
    >>> nb_repetitions('A',[ 'B', 'A', 'B', 'A', 'R'])
    2
    >>> nb_repetitions(12,[1, '! ', 7, 21, 36, 44])
    0
    """
    # boucle FOR
    # invariant de boucle:
    #   * somme est égale au nombre d'occurrence de 'elt'
    #   dans la partie tab[0 .. i-1] du tableau
    # condition d'arrêt
    #   * i vaut n - 1 (avec n = longueur de 'tab')
    somme = 0
    for i in range(len(tab)):
        if tab[i] == elt:
            somme = somme + 1

    # variante pythonesque de la boucle:
    # somme = 0
    # for val in tab:
    #     if val == elt:
    #         somme = somme + 1

    return somme


# exemples de l'énoncé
assert nb_repetitions(5,[2, 5, 3, 5, 6, 9, 5]) == 3
assert nb_repetitions('A',[ 'B', 'A', 'B', 'A', 'R']) == 2
assert nb_repetitions(12,[1, '! ', 7, 21, 36, 44]) == 0


# tests de l'énoncé avec la bibliothèque doctest
testmod()
