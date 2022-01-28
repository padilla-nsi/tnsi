def maxi(tab):
    i_max = 0
    v_max = tab[0]

    n = len(tab)
    for i in range(1, n):
        if tab[i] > v_max:
            i_max = i
            v_max = tab[i]
    return (v_max, i_max)

assert maxi([1,5,6,9,1,2,3,7,9,8]) == (9,3)
