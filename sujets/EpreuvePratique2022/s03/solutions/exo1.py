from doctest import testmod


def delta(tab: list) -> list:
    """ Codage par différence du tableau tab.

    Args:
        tab (list): tableau non vide de nombres entiers

    Returns:
        list: tableau de valeurs entières compressées par différence

    Tests et Exemples:!
    >>> delta([1000, 800, 802, 1000, 1003])
    [1000, -200, 2, 198, 3]
    >>> delta([42])
    [42]
    """
    diff = [tab[0]]

    n = len(tab)
    for i in range(1, n):
        delta = tab[i] - tab[i - 1]
        diff.append(delta)

    return diff


testmod()