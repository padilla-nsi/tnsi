def tri_selection(tab):
    n = len(tab)
    for i in range(n):
        i_min = i
        v_min = tab[i]
        for j in range(i, n):
            if tab[j] < v_min:
                i_min = j
                v_min = tab[j]
        temp = tab[i]
        tab[i] = v_min
        tab[i_min] = temp
    return tab


assert tri_selection([1,52,6,-9,12]) == [-9, 1, 6, 12, 52]
