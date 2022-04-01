from doctest import testmod


def tri_bulles(T: list) -> list:
    """ Tri d'un tableau suivant l'algo de tri à bulles

    Args:
        T (list): tableau d'entiers

    Returns:
        list: permutation de T triée

    Tests et Exemples:
    >>> tri_bulles([10, 4, 3, 9, -10, 100])
    [-10, 3, 4, 9, 10, 100]
    """
    n = len(T)
    # parcours du tableau 
    # en commençant par la dernière valeur (inclue)
    # et se terminant à la case 0 (inclue)
    # et en parcourant à l'envers, ie en allant de -1 en -1
    #
    # il y a deux idées :
    # (1) placer à la dernière case de la partie non triée
    #     la valeur la plus grande
    # (2) permuter la valeur la plus grande case par case
    #     pour l'amener successivement à la dernière case non triée

    # parcours à l'envers
    for i in range(n - 1, -1, -1):
        for j in range(i):
            if T[j] > T[j + 1]:
                # lorsque la valeur courante est plus grande
                # que la valeur suivante : on les permute
                temp = T[j]
                T[j] = T[j + 1]
                T[j + 1] = temp
    return T


assert tri_bulles([10, 4, 3, 9, -10, 100]) == [-10, 3, 4, 9, 10, 100]
testmod()