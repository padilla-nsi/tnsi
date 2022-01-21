def recherche(elt, tab):
    n = len(tab)
    for i in range(n):
        if tab[i] == elt:
            return i
    return -1


assert recherche(1, [2, 3, 4]) == -1
assert recherche(1, [10, 12, 1, 56]) == 2
assert recherche(50, [1, 50, 1]) == 1
assert recherche(15, [8, 9, 10, 15]) == 3
