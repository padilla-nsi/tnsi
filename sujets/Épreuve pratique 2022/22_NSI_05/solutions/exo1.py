def rechercheMinMax(tab):
    n = len(tab)
    if n == 0:
        return {'min': None, 'max': None}
    
    v_min = tab[0]
    v_max = tab[0]
    for i in range(1, n):
        if tab[i] > v_max:
            v_max = tab[i]
        elif tab[i] < v_min:
            v_min = tab[i]
    
    return {'min': v_min, 'max': v_max}


assert rechercheMinMax([0, 1, 4, 2, -2, 9, 3, 1, 7, 1]) == {'min': -2, 'max': 9}

assert rechercheMinMax([]) == {'min': None, 'max': None}
