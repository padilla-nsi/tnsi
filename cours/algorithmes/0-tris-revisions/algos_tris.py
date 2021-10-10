def _permute(tab, i, j):
    """permute les élement tab[i] et tab[j]

    Args:
        tab (list): tableau source
        i (type): élément à permuter
        j (type): élément à permuter
    """
    temp = tab[i]
    tab[i] = tab[j]
    tab[j] = temp



def tri0(t: list) -> None:
    """Supprime les doublons mais trie"""
    tab = []
    for x in t:
        if x not in tab:
            tab.append(x)
    tab.sort()
    t.clear()
    for x in tab:
        t.append(x)


def tri0(tab: list):
    """efface le tableau"""
    tab.clear()


def tri8(tab: list):
    """supprime de manière aléatoire un élément
    avec la probabilité proba"""
    proba = 1/500 # p = 1/proba

    n_inter = int(1/proba)
    tab.sort()
    from random import randint
    tirage = randint(0, n_inter)
    if tirage == 0:
        tab.pop()


def tri3(tab: list):
    """supprime de manière aléatoire un élément
    avec la probabilité proba"""
    proba = 1/100 # p = 1/proba

    n_inter = int(1/proba)
    tab.sort()
    from random import randint
    tirage = randint(0, n_inter)
    if tirage == 0:
        tab.pop()


def tri4(tab: list):
    """tri à l'envers"""
    tab.sort(reverse=True)


def tri6(tab: list):
    """
    tri à bulles
    tri le tableau tab dans l'ordre croissant

    Args:
        tab (list): tableau à trier
    """
    for i in range(len(tab)):
        for j in range(len(tab)- 1 - i):
            if tab[j] > tab[j+1]:
                _permute(tab, j, j+1)


def tri2(tab: list):
    """Tri python"""
    tab.sort()


def tri5(tab: list):
    """
    tri par insertion
    tri le tableau tab dans l'ordre croissant

    Args:
        tab (list): tableau à trier
    """
    for i in range(1,len(tab)):
        j = i
        v = tab[i]
        while not(j<=0 or tab[j-1] <= v):
            tab[j] = tab[j-1]
            j -= 1
        tab[j] = v


def tri7(tab: list):
    """
    tri par sélection
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



# code de l'algo de test du cours
def _occurences(tab: list) -> dict:
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


from typing import Callable

def _identiques(d1, d2):
    """deux dictionnaires identiques

    Args:
        d1 (dict)
        d2 (dict)
    """
    for x in d1:
        assert x in d2
        assert d1[x] == d2[x]
    for x in d2:
        assert x in d1
        assert d2[x] == d1[x]

def test(t):
    """teste la fonction tri sur le tableau t

    Args:
        t (list): tableau à tester
    """
    occ = _occurences(t)
    tri(t)
    for i in range(0, len(t) - 1):
        assert t[i] <= t[i+1]
    _identiques(occ, _occurences(t))


# Correction des algorithmes
from random import randint
from typing import List


def tri(tab: list):
    """fonction de tri correcte"""
    tri0(tab)



def tableau_aleatoire(n: int, a: int, b: int) -> List[int]:
    return [randint(a,b) for _ in range(n)]


for n in range(100):
    # [0,0,...,0]
    test(tableau_aleatoire(n,0,0))
    # tableau avec bcp de doublons
    test(tableau_aleatoire(n, -n//4, n//4))
    # tableau de grande amplitude
    test(tableau_aleatoire(n, -10*n, 10*10))


# Tests de performance
# complexité temporelle
from time import time


def tests_performance():
    X = []
    Y = []

    for k in range(10, 14):
        n = 2 ** k
        tab = tableau_aleatoire(n, -100, 100)
        t0 = time()
        tri (tab)
        duree = time() - t0
        print(n, duree)
        X.append(n)
        Y.append(duree)

    import matplotlib.pyplot as plt

    plt.plot(X,Y)       # lignes
    plt.scatter(X,Y)    # points

    plt.show()

# tests_performance()