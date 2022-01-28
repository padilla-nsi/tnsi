def chercher(T, n, i, j):
    if i < 0 or j >= len(T) :
        print("Erreur")
        return None
    if i > j :
        return None
    m = (i + j) // 2
    if T[m] < n :
        return chercher(T, n, m + 1 , j)
    elif n < T[m] :
        return chercher(T, n, i , m - 1 )
    else :
        return m


assert chercher([1,5,6,6,9,12],7,0,10) == None
assert chercher([1,5,6,6,9,12],7,0,5) == None
assert chercher([1,5,6,6,9,12],9,0,5) == 4
assert chercher([1,5,6,6,9,12],6,0,5) == 2