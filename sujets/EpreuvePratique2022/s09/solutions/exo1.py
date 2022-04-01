from doctest import testmod


def calcul(n):
    """Définition d'une suite.
    Args:
        n (int): nombre entier de départ

    Returns:
        list: tableau contenant toutes les étapes de calcul
    
    Tests et Exemples:
    >>> calcul(7)
    [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    liste = []
    u0 = n
    while u0 != 1:
        # condition d'arrêt : u0 == 1
        liste.append(u0)

        # détermination du prochain terme
        if u0 % 2 == 0:
            u0 = u0 // 2
        else:
            u0 = 3 * u0 + 1
    
    # ajout de la dernière valeur '1' qui a 
    # terminée la boucle
    liste.append(u0)
    return liste


assert calcul(7) == [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
testmod()