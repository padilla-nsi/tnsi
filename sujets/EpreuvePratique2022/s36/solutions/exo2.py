"""
Author: Pascal Padilla
Source: correction de l'exercice 2 du sujet 36 des épreuves pratiques NSI 2022

Remarques:
    * 8 assertions ajoutées (dans la fonction `distance`)
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
    # BOUCLE
    # -> invariant: `point` est le point le plus proche de `depart`
    #               parmis tous les points de tab[0 .. i-1] 
    # -> invariant: min_dist est la distance entre `depart` et `point`
    # -> initialisation: i <- 1
    # -> initialisation: point et min_dist invariants pour la zone
    #                    tab[0..0] du tableau
    point = tab[0]
    min_dist = distance(point, depart)
    # -> condition d'arrêt: après la boucle i <- dernier indice de `tab`
    for i in range (1, len(tab)):
        # maintient de l'invariant si le point courant est plus proche
        # de `depart` que `point`
        if distance(tab[i], depart) < min_dist:
            # mise à jour de `point` et de la distance minimale associée
            point = tab[i]
            min_dist = distance(tab[i], depart)
    
    # fin BOUCLE: parmis tous les points de tab, `point` est le plus proche
    return point

assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (0, 0)) == (2, 5), "erreur"
