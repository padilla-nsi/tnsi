def nb_repetitions(elt, tab):
    somme = 0
    for x in tab:
        if x == elt:
            somme = somme + 1
    return somme

assert nb_repetitions(5,[2, 5, 3, 5, 6, 9, 5]) == 3
assert nb_repetitions('A',[ 'B', 'A', 'B', 'A', 'R']) == 2
assert nb_repetitions(12,[1, '! ', 7, 21, 36, 44]) == 0
