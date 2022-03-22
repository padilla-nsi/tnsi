

def fusion(tab1: list, tab2: list) -> list:
    """Fusionne (merge) deux tableaux triées en un seul trié

    Args:
        tab1 (list): tableau triée
        tab2 (list): tableau trié

    Returns:
        list: tableau ordonné contenant tous les éléments de tab1 et tab2
    """
    i = 0
    n1 = len(tab1)
    j = 0
    n2 = len(tab2)
    tab_fusion = [None] * (n1 + n2)
    for k in range(n1 + n2):
        if j == n2:
            tab_fusion[k] = tab1[i]
            i = i + 1
        elif i == n1:
            tab_fusion[k] = tab2[j]
            j = j + 1
        elif tab1[i] <= tab2[j]:
            tab_fusion[k] = tab1[i]
            i = i + 1
        else:
            tab_fusion[k] = tab2[j]
            j = j + 1
    return tab_fusion


# def fusion_rec(tab1, tab2):
#     if tab1 == []:
#         return tab2
#     if tab2 == []:
#         return tab1
#     if tab1[0] <= tab2[0]:
#         return [tab1[0]] + fusion_rec(tab1[1:], tab2)
#     else:
#         return [tab2[0]] + fusion_rec(tab1, tab2[1:])


def tri_fusion(tab):    
    n = len(tab)
    if n <= 1:
        return tab
    
    # taille >= 2
    i_median = (n+1) // 2
    tab1 = tri_fusion(tab[:i_median])
    tab2 = tri_fusion(tab[i_median:])
    return fusion(tab1, tab2)


tab = [1,6,2,3,7,5,4,6]
result = tri_fusion(tab)
print(result)

tailles = [2, 4, 8, 16, 32, 64, 128]
from time import time

for taille in tailles:
    lg = taille * 10_000
    tab = [(lg - i) for i in range(lg)]
    t0 = time()
    result = tri_fusion(tab)
    t1 = time()
    duree = t1 - t0
    print(taille, "\t", duree)


# from math import inf
# def fusion(tab, p, q, r):
#     tab1 = tab[p:q] + [inf]
#     print(tab1)
#     tab2 = tab[q:r+1] + [inf]
#     print(tab2)
#     i = 0
#     j = 0
#     for k in range(p, r+1):
#         if tab1[i] <= tab2[j]:
#             tab[k] = tab1[i]
#             i = i + 1
#         else:
#             tab[k] = tab2[j]
#             j = j + 1

# tab = [2, 4, 6, 1, 3, 5]
# # fusion(tab, 0, 3, 5)
# print(tab)

# def tri_fusion(tab, p, r):
#     if p < r:
#         i_median = (p+r)//2
#         tri_fusion(tab, p, i_median)
#         print(tab)
#         tri_fusion(tab, i_median + 1, r)
#         print(tab)
#         fusion(tab, p, i_median, r)


# tri_fusion(tab, 0, len(tab)-1)
# print(tab)
