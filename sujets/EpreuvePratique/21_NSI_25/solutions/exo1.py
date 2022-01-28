def recherche(tab):
    couple_consecutifs = []

    n = len(tab)
    for i in range(1, n):
        prev = tab[i-1]
        next = tab[i]
        if next == prev + 1:
            couple_consecutifs.append((prev, next))
    return couple_consecutifs




assert recherche([1, 4, 3, 5]) == []
assert recherche([1, 4, 5, 3]) == [(4, 5)]
assert recherche([7, 1, 2, 5, 3, 4]) == [(1, 2), (3, 4)]
assert recherche([5, 1, 2, 3, 8, -5, -4, 7]) == [(1, 2), (2, 3), (-5, -4)]
