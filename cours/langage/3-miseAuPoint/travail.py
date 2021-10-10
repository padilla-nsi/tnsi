

## Activité 6

# Différentes fonctions de tris 
# qui sont correctes ou incorrecte

# fichier utilisé comme fichier source dans capytale


# tris incorrects

def tri6(t: list) -> None:
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



def tri5(tab: list):
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


def tri1(tab: list):
    """Tri python"""
    tab.sort()


def tri2(tab: list):
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


## Activité 7


### différentes implémentations de la multiplication

# implémentations correctes :

def mult_python(x: int,y: int):
    return x*y


def mult_naif(x: int,y: int) -> int:
    signe = 1
    if x <= 0:
        x = -x
        signe *= -1
    if y <= 0:
        y = -y
        signe *= -1
    
    r = 0
    while x >0:
        r += y
        x -= 1
    return signe * r


def mult_russe(x: int,y: int):
    signe = 1
    if x <= 0:
        x = -x
        signe *= -1
    if y <= 0:
        y = -y
        signe *= -1
    
    r = 0
    while x != 0:
        if x % 2 == 1:
            r = r + y
            x = x - 1
        x = x // 2
        y = y * 2
    return signe * r


def mult_russe_rapide(x: int,y: int):
    signe = 1
    if x <= 0:
        x = -x
        signe *= -1
    if y <= 0:
        y = -y
        signe *= -1
    
    r = 0
    while x != 0:
        if x&1:
            r = r + y
            x = x - 1
        x = x>>1
        y = y<<1
    return signe * r


def non_mult_neg(x: int, y: int) -> int:
    return abs(x*y)


def non_mult_xy_yx(x: int, y: int) -> int:
    if x <= y:
        return x*y
    return int( str(abs(x)) + str(abs(y)) )


def non_mult_add(x: int, y: int) -> int:
    return x + y


def non_mult_alea(x, y):
    from random import randint
    if randint(0, 20) == 0:
        return x+y
    return x*y 


def non_mult_alea_rare(x, y):
    from random import randint
    if randint(0, 250) == 0:
        return x+y
    return x*y 


mults= [non_mult_neg, mult_python, non_mult_xy_yx, mult_naif, non_mult_alea, mult_russe, mult_russe_rapide, non_mult_add, non_mult_alea_rare]