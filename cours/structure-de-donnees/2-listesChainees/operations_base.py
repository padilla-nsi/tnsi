"""
    concaténation de deux listes chaînées
    Author: Pascal Padilla
"""
class Maillon:
    """un maillon d'une liste chaînée"""

    def __init__(self, valeur, suivant):
        self.valeur = valeur
        self.suivant = suivant


def longueur(lst):
    """ longueur d'une liste chaînée """
    if lst == None:
        return 0
    return 1 + longueur(lst.suivant)


def nieme_element(index, lst):
    """ nieme element d'une liste chaînée
        version itérative
    """
    if index >= longueur(lst):
        raise IndexError('index out of range')

    maillon_actuel = lst
    for _ in range(index):
        maillon_actuel = maillon_actuel.suivant
    return maillon_actuel.valeur


def concatener(start_lst, end_lst):
    """ concaténer deux liste de façon récursive """
    if longueur(start_lst) == 0:
        return end_lst

    premier_element = Maillon(start_lst.valeur, None)
    reste = concatener(start_lst.suivant, end_lst)
    premier_element.suivant = reste
    return premier_element


def renverser(lst):
    """ renvoyer une nouvelle liste chainée renversée """
    n = longueur(lst)
    new_lst = None
    for i in range(n):
        valeur = nieme_element(i, lst)
        new_lst = Maillon(valeur, new_lst)
    return new_lst
