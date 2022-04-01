from doctest import testmod


def fusion(L1: list, L2: list) -> list:
    """Fusionne deux listes triées en une seule triée.

    Args:
        L1 (list): tableau trié de nombres entiers
        L2 (list): idem

    Returns:
        list: fusion des deux tableaus en argument
            en un nouveau tableau trié

    Tests et Exemples:
    >>> fusion([1,6,10],[0,7,8,9])
    [0, 1, 6, 7, 8, 9, 10]
    """
    n1 = len(L1)
    n2 = len(L2)

    # initialisation du tableau fusion
    # de taille n1 + n2
    L12 = [0]*(n1+n2)

    # initialisation des compteurs de L1 et de L2
    i1 = 0
    i2 = 0

    # initialisation du compteur de L12
    i = 0

    # première boucle qui rempli L12
    # tant que l'on n'a pas parcouru entièrement 
    # l'un des deux tableaux 
    while i1 < n1 and i2 < n2 :
        if L1[i1] < L2[i2]:
            # Ajoute la plus petite valeur dans L12
            # qui est celle de L1
            L12[i] = L1[i1]
            # met à jour le compteur de L1 pour traiter
            # sa valeur suivante
            i1 = i1 + 1
        else:
            # Ajoute la plus petite valeur dans L12
            # qui est celle de L2
            L12[i] = L2[i2]
            # met à jour le compteur de L2 pour traiter
            # sa valeur suivante
            i2 = i2 + 1
        i += 1

    # deuxième boucle qui finit de remplir L12 avec les
    # valeurs ordonnées de L1
    # cette boucle ne s'exécute pas si L1 est déjà
    # complètement parcouru (i1 == n1)
    while i1 < n1:
    	L12[i] = L1[i1]
    	i1 = i1 + 1
    	i = i + 1
    
    # deuxième boucle qui finit de remplir L12 avec les
    # valeurs ordonnées de L2
    # cette boucle ne s'exécute pas si L2 est déjà
    # complètement parcouru (i2 == n2)
    while i2 < n2:
    	L12[i] = L2[i2]
    	i2 = i2 + 1
    	i = i + 1
    
    # L12 contient désormais toutes les valeurs de L1
    # et de L2, ordonnées.
    # L'intérêt de cet algorithme est que son temps
    # d'exécution dans le pire des cas est proportionnel
    # à n1 + n2. C'est une complexité linéaire
    return L12


assert fusion([1,6,10],[0,7,8,9]) == [0, 1, 6, 7, 8, 9, 10]
testmod()