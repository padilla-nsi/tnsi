from doctest import testmod

def recherche(tab: list, n: int) -> int:
    """Indice de la dernière occurence de n
    dans tab, longueur de tab sinon

    Args:
        tab (list): tableau dans lequel chercher n
        n (int): valeur à chercher

    Returns:
        int: indice de la dernière occurence de n
    
    Exemples:
    >>> recherche([5, 3], 1)
    2
    >>> recherche([2, 4], 2)
    0
    >>> recherche([2, 3, 5, 2, 3], 2)
    3
    """
    indice = -1
    taille = len(tab)
    
    for i in range(taille):
        if tab[i] == n:
            indice = i

    if indice == -1:
        return taille
    else:
        return indice


if __name__ == '__main__':
    testmod(verbose=True)