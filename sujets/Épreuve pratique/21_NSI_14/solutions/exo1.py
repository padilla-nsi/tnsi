def recherche(elt, tab):
    indices = []
    n = len(tab)
    for i in range(n):
        if tab[i] == elt:
            indices.append(i)
    return indices

assert  recherche(3, [3, 2, 1, 3, 2, 1]) == [0, 3]
assert recherche(4, [1, 2, 3]) == []
