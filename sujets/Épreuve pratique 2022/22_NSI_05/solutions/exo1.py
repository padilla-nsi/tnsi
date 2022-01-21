from doctest import testmod


def rechercheMinMax(tab):
    """ Recherche du min et du max d'un tableau.

    Args:
        tab (list): tableau non trié de nombres entiers

    Returns:
        dict: dictionnaire ayant pour clés :
        'min' pour la valeur minimale
        'max' pour la valeur maximale
    
    Tests et Exemples:
    >>> tableau = [0, 1, 4, 2, -2, 9, 3, 1, 7, 1]
    >>> resultat = rechercheMinMax(tableau)
    >>> resultat
    {'min': -2, 'max': 9}

    >>> tableau = []
    >>> resultat = rechercheMinMax(tableau)
    >>> resultat
    {'min': None, 'max': None}
    """
    n_tab = len(tab)
    if n_tab == 0:
        return {'min': None, 'max': None}

    # initialisation des valeurs maximales et minimales 
    # avec le premier élément du tableau
    v_min = tab[0]
    v_max = tab[0]
    for i in range(1, n_tab):
        # parcours de tous les éléments non visités du tableau
        if tab[i] > v_max:
            # mise àjour de la valeur max
            v_max = tab[i]
        elif tab[i] < v_min:
            # mise à jour de la valeur min
            v_min = tab[i]

    # résultat sous la forme de dictionnaire
    return {'min': v_min, 'max': v_max}


assert rechercheMinMax([0, 1, 4, 2, -2, 9, 3, 1, 7, 1]) == {'min': -2, 'max': 9}
assert rechercheMinMax([]) == {'min': None, 'max': None}

testmod()