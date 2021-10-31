def recherche(tab, n):
    i = 0
    j = len(tab) - 1

    while i < j:
        m = (i + j) // 2
        if tab[m] == n:
            return m
        if n > tab[m]:
            i = m + 1
        else:
            j = m - 1
    return -1


assert recherche([2, 3, 4, 5, 6], 5) == 3
assert recherche([2, 3, 4, 6, 7], 5) == -1
