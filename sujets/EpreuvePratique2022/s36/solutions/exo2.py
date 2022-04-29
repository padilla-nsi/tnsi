"""
Author: Pascal Padilla
Source: correction de l'exercice 2 du sujet 36 des épreuves pratiques NSI 2022

Remarques:
"""


from math import sqrt   # import de la fonction racine carrée

def distance(point1, point2): 
    """ Calcule et renvoie la distance entre deux points. """
    # ajout des assertions pour point1
    assert isinstance(point1, tuple)    # point1 est bien un tuple
    assert len(point1) == 2             #        de taille 2 (un couple)
    assert isinstance(point1[0], int)   # la première coordonnée de point1 est un nb entier
    assert isinstance(point1[1], int)   # la deuxième coordonnée de point1 est un nb entier
    
    # ajout des assertions pour point2
    assert isinstance(point2, tuple)    # idem
    assert len(point2) == 2             # idem
    assert isinstance(point2[0], int)   # idem
    assert isinstance(point2[1], int)   # idem

    # calcul puis renvoie de la distance
    return sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

assert distance((1, 0), (5, 3)) == 5.0, "erreur de calcul"


def plus_courte_distance(tab, depart):
    """ Renvoie le point du tableau tab se trouvant à la plus     
    courte distance du point depart."""
    point = tab[0]
    min_dist = distance(point, depart)
    for i in range (1, len(tab)):
        if distance(tab[i], depart) < min_dist:
            point = tab[i]
            min_dist = distance(tab[i], depart)
    return point

assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (0, 0)) == (2, 5), "erreur"
