from doctest import testmod


def insere(a, tab):
    """Fait une copie d'un tableau trié par ordre
    croissant en y insérant la valeur a.

    Args:
    a (int): valeur à insérer
    tab (list): tableau trié

    Returns:
    list: copie du tableau tab avec 
    la valeur a insérée

    Tests et Exemples:
    >>> insere(3,[1,2,4,5])
    [1, 2, 3, 4, 5]
    >>> insere(10,[1,2,7,12,14,25])
    [1, 2, 7, 10, 12, 14, 25]
    >>> insere(1,[2,3,4])
    [1, 2, 3, 4]
    """
    l = list(tab) #l contient les mêmes éléments que tab

    # l'algorithme choisi ressemble au tri à bulle :
    #   on ajoute la valeur à insérer à la fin du tableau 
    #   puis on la fait descendre petit à petit jusqu'à sa place correcte
    l.append(a)

    # initialisation de la boucle avec la première valeur
    # à tester, c'est-à-dire la case située à gauche de a
    i = len(l) - 2

    # Précondition : 
    #  * a est à la position i+1
    #  * a est < que toutes les valeurs des cases
    #  situées après lui (i+2, i+3, ...)
    # Condition d'arrêt :
    #  * il n'y a plus de case avant a
    # OU
    #  * a >= à la valeur située avant lui
    while a < l[i] and i >= 0: 
        # puisque a est plus petit que l[i]
        # permuter l[i] et a
        l[i+1] = l[i]
        l[i] = a
        
        # mise à jour du compteur de boucle
        i = i - 1
    
    return l


assert insere(3,[1,2,4,5]) == [1, 2, 3, 4, 5]
assert insere(10,[1,2,7,12,14,25]) == [1, 2, 7, 10, 12, 14, 25]
assert insere(1,[2,3,4]) == [1, 2, 3, 4]
testmod()