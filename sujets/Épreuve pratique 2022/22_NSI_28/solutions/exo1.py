def moyenne(tab):
    somme = 0
    n = len(tab)
    for i in range(n):
        somme = somme + tab[i]
    
    return somme/n

assert moyenne([1.0]) == 1.0
assert moyenne([1.0, 2.0, 4.0]) == 2.3333333333333335
