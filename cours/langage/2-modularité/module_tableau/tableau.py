import doctest

def tranche(t,i,j):
    """Renvoie un extrait de t entre les indices
    i inclus et j exclus

    Args:
        t (list): tableau
        i (int): indice de départ
        j (int): indice de fin (exclu)

    Returns:
        list: extrait de t
    """
    if j <= i:
        return []
    tmp = []
    for k in range(i,j):
        tmp.append(t[k])

    return tmp


def concatenation(t1, t2) -> list:
    """
    Renvoie un nouveau tableau avec dans l'ordre
    les éléments de t1 puis ceux de t2.

    Args:
        t1 (list): premier tableau
        t2 (list): deuxième tableau

    Returns:
        list: t1 + t2
    
    Exemples:
    >>> concatenation([1,2], [3,4])
    [1, 2, 3, 4]
    >>> concatenation([1,2], [])
    [1, 2]
    >>> concatenation([], [3,4])
    [3, 4]
    """
    l1 = len(t1)
    l2 = len(t2)

    tab = [None] * (l1+l2)

    for i in range(l1):
        tab[i] = t1[i]
    for i in range(l2):
        tab[l1+i] = t2[i]
    
    return tab


doctest.testmod()