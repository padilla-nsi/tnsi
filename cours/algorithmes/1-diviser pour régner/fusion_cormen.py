from math import inf
def fusion(tab, p, q, r):
    tab1 = tab[p:q+1] + [inf]
    tab2 = tab[q+1:r+1] + [inf]
    i = 0
    j = 0
    for k in range(p, r+1):
        if tab1[i] <= tab2[j]:
            tab[k] = tab1[i]
            i = i + 1
        else:
            tab[k] = tab2[j]
            j = j + 1

# tab = [2, 4, 6, 1, 3, 5]
# fusion(tab, 0, 3, 5)
# print(tab)

def tri_fusion(tab, p, r):
    if p < r:
        i_median = (p+r)//2
        tri_fusion(tab, p, i_median)
        tri_fusion(tab, i_median + 1, r)
        fusion(tab, p, i_median, r)


# tri_fusion(tab, 0, len(tab)-1)
# print(tab)


from random import 
# tab = [1,6,2,3,7,5,4,6]
# result = tri_fusion(tab)
# print(result)

tailles = [2, 4, 8, 16, 32, 64, 128]
from time import time

for taille in tailles:
    lg = taille * 10_000
    tab = [(lg - i) for i in range(lg)]
    t0 = time()
    result = tri_fusion(tab, 0, lg-1)
    t1 = time()
    duree = t1 - t0
    print(taille, "\t", duree)