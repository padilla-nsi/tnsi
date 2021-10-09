def _permute(tab, i, j):
    temp = tab[i]
    tab[i] = tab[j]
    tab[j] = temp


def tri_bulle(tab: list):
    for i in range(len(tab)):
        for j in range(len(tab)- 1 - i):
            if tab[j] > tab[j+1]:
                _permute(tab, j, j+1)



def tri_insertion(tab: list):
    pass


def tri_selection(tab: list):
    """
    tri le tableau tab dans l'ordre croissant

    Args:
        tab (list): tableau à trier
    """
    for i in range(len(tab)):
        i_min = i
        for j in range(i+1, len(tab)):
            if tab[j] < tab[i_min]:
                i_min = j
        _permute(tab, i, i_min)


def _occurence(tab: list) -> dict:
    """
    copie les éléments de tab dans un dictionnaire tel que :
      key   : éléments distincts de tab
      value : nombre d'occurence de la clé dans tab

    exemple :
    >>> _occurence([1,1,1,2,3,4,4])
    {1: 3, 2: 1, 3: 1, 4: 2}
    >>> _occurence([])
    {}
    """
    dic = {}
    for elem in tab:
        if elem not in dic:
            dic[elem]  = 1
        else:
            dic[elem] += 1
    return dic


def _identique(dic1: dict, dic2: dict) -> bool:
    """
    est ce que dic1 et dic2 sont identiques?

    Exemples:
    >>> _identique({1: 1, 2: 5}, {2: 5, 1: 1})
    True
    >>> _identique({1: 1, 2: 5}, {1:1})
    False
    """
    for k in dic1:
        if k not in dic2 or dic1[k] != dic2[k]:
            return False
    for k in dic2:
        if k not in dic1 or dic2[k] != dic1[k]:
            return False
    return True

from typing import Callable

def test(tab: list, func_tri: Callable) -> bool:
    occ0 = _occurence(tab)
    func_tri(tab)
    for i in range(len(tab)-1):
        if tab[i] > tab[i+1]:
            return False

    return _identique(occ0, _occurence(tab))


print(test([0,4,1,2,0,2,10,8,19], tri_selection))