"""
    concaténation de deux listes chaînées
    Author: Pascal Padilla
"""


from doctest import testmod
from maillon import Maillon


def longueur(lst):
    """ longueur d'une liste chaînée
    
    Exemples et tests:
    >>> lst = Maillon(42, None)
    >>> assert longueur(lst) == 1

    >>> lst = None
    >>> assert longueur(lst) == 0

    >>> lst = Maillon(1, Maillon(2, Maillon(3, None)))
    >>> assert longueur(lst) == 3
    """
    if lst == None:
        return 0
    return 1 + longueur(lst.suivant)


def longueur(lst):
    """ longueur d'une liste chaînée
    
    Exemples et tests:
    >>> lst = Maillon(42, None)
    >>> assert longueur(lst) == 1

    >>> lst = None
    >>> assert longueur(lst) == 0

    >>> lst = Maillon(1, Maillon(2, Maillon(3, None)))
    >>> assert longueur(lst) == 3
    """
    longueur_actuelle = 0
    maillon_actuel = lst

    while maillon_actuel is not None:
        longueur_actuelle = longueur_actuelle + 1
        maillon_actuel = maillon_actuel.suivant
    
    return longueur_actuelle


def nieme_element(n, lst):
    """ nieme element d'une liste chaînée
        version itérative
    
    Exemples et tests:
    >>> lst = Maillon(1, Maillon(2, Maillon(3, None)))
    >>> assert nieme_element(0, lst) == 1
    >>> assert nieme_element(1, lst) == 2
    >>> assert nieme_element(2, lst) == 3

    >>> assert nieme_element(3, lst) == 3
    Traceback (most recent call last):
    IndexError: index out of range
    """
    if n >= longueur(lst):
        raise IndexError('index out of range')

    maillon_actuel = lst
    for _ in range(n):
        maillon_actuel = maillon_actuel.suivant
    return maillon_actuel.valeur



def nieme_element(n, lst):
    """ nieme element d'une liste chaînée
        version itérative
    
    Exemples et tests:
    >>> lst = Maillon(1, Maillon(2, Maillon(3, None)))
    >>> assert nieme_element(0, lst) == 1
    >>> assert nieme_element(1, lst) == 2
    >>> assert nieme_element(2, lst) == 3

    >>> assert nieme_element(3, lst) == 3
    Traceback (most recent call last):
    IndexError: index out of range
    """
    if n >= longueur(lst):
        raise IndexError('index out of range')

    if n == 0:
        return lst.valeur

    return nieme_element(n - 1, lst.suivant)



def concatener(start_lst, end_lst):
    """ concaténer deux liste de façon récursive
    
    Exemples et tests:
    >>> l1 = Maillon(1, Maillon(2, Maillon(3, None)))
    >>> l2 = Maillon(4, Maillon(5, None))
    >>> l3 = concatener(l1, l2)
    >>> assert nieme_element(0, l3) == 1
    >>> assert nieme_element(1, l3) == 2
    >>> assert nieme_element(2, l3) == 3
    >>> assert nieme_element(3, l3) == 4
    >>> assert nieme_element(4, l3) == 5

    >>> nieme_element(5, l3)
    Traceback (most recent call last):
    IndexError: index out of range

    """
    if longueur(start_lst) == 0:
        return end_lst

    premier_element = Maillon(start_lst.valeur, None)
    reste = concatener(start_lst.suivant, end_lst)
    premier_element.suivant = reste
    return premier_element


def renverser(lst):
    """ renvoyer une nouvelle liste chainée renversée
    
    Exemples et tests:
    >>> l1 = Maillon(1, Maillon(2, Maillon(3, None)))
    >>> l2 = renverser(l1)
    >>> assert nieme_element(0, l2) == 3
    >>> assert nieme_element(1, l2) == 2
    >>> assert nieme_element(2, l2) == 1

    >>> nieme_element(3, l2)
    Traceback (most recent call last):
    IndexError: index out of range
    """
    n = longueur(lst)
    new_lst = None
    for i in range(n):
        valeur = nieme_element(i, lst)
        new_lst = Maillon(valeur, new_lst)
    return new_lst


if __name__ == '__main__':
    testmod(verbose=True)