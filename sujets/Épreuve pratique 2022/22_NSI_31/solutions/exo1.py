def recherche(a, t):
    occurences = 0
    for x in t:
        if x == a:
            occurences += 1
    return occurences


assert recherche(5,[]) == 0
assert recherche(5,[-2, 3, 4, 8]) == 0
assert recherche(5,[-2, 3, 1, 5, 3, 7, 4]) == 1
assert recherche(5,[-2, 5, 3, 5, 4, 5]) == 3
