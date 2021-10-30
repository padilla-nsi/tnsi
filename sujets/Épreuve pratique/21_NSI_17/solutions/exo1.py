def indice_du_min(tab):
    n = len(tab)
    if n == 0:
        return None
    
    i_min = 0
    v_min = tab[0]

    for i in range(1, n):
        if tab[i] < v_min:
            i_min = i
            v_min = tab[i]

    return i_min
    

assert indice_du_min([5]) == 0
assert indice_du_min([2, 4, 1]) == 2
assert indice_du_min([5, 3, 2, 2, 4]) == 2

