# Différentes fonctions de tris 
# qui sont correctes ou incorrecte

# fichier utilisé comme fichier source dans capytale


# tris incorrects

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


# tris corrects

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


