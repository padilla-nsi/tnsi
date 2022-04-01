from doctest import testmod


def recherche(tab):
    """ Recherche les couples d'entiers consécutifs d'un tableau.

    Args:
        tab (list): tableau d'entiers

    Returns:
        list: tableau de couples d'entiers consécutifs

    Tests et Exemples:
    >>> recherche([1, 4, 3, 5])
    []
    >>> recherche([1, 4, 5, 3])
    [(4, 5)]
    >>> recherche([7, 1, 2, 5, 3, 4])
    [(1, 2), (3, 4)]
    >>> recherche([5, 1, 2, 3, 8, -5, -4, 7])
    [(1, 2), (2, 3), (-5, -4)]
    """
    couple_consecutifs = []

    n = len(tab)
    for i in range(1, n):
        pred = tab[i-1]
        suiv = tab[i]

        if suiv == pred + 1:
            couple_consecutifs.append( (pred, suiv) )

    return couple_consecutifs




assert recherche([1, 4, 3, 5]) == []
assert recherche([1, 4, 5, 3]) == [(4, 5)]
assert recherche([7, 1, 2, 5, 3, 4]) == [(1, 2), (3, 4)]
assert recherche([5, 1, 2, 3, 8, -5, -4, 7]) == [(1, 2), (2, 3), (-5, -4)]

testmod()