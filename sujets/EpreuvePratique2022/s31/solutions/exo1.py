"""
Author: Pascal Padilla
Source: correction de l'exercice 1 du sujet 31 des épreuves pratiques NSI 2022

Remarques:
"""

def recherche(element, tab):
    """
    Tests et exemples:
    >>> recherche(5,[])
    0
    >>> recherche(5,[-2, 3, 4, 8])
    0
    >>> recherche(5,[-2, 3, 1, 5, 3, 7, 4])
    1
    >>> recherche(5,[-2, 5, 3, 5, 4, 5])
    3
    """
    # BOUCLE
    # -> invariant: occurrence contient le nb d'apparition
    #               de element dans la zone déjà parcourue de tab
    # -> initialisation: au départ, rien n'est parcouru
    occurrence = 0

    # -> condition d'arrêt: après la dernière case du tableau
    for elt_courant in tab:
        # maintien de l'invariant si la valeur element est trouvée
        if elt_courant == element:
            # incrémenter le compteur `occurrence`
            occurrence = occurrence + 1
    
    # fin de BOUCLE
    # tout le tableau est parcouru et occurrence est correct
    return occurrence


# Vérification par des assertions
assert recherche(5,[]) == 0
assert recherche(5,[-2, 3, 4, 8]) == 0
assert recherche(5,[-2, 3, 1, 5, 3, 7, 4]) == 1
assert recherche(5,[-2, 5, 3, 5, 4, 5]) == 3

# Vérification par des affichages
print(recherche(5,[]))
print(recherche(5,[-2, 3, 4, 8]))
print(recherche(5,[-2, 3, 1, 5, 3, 7, 4]))
print(recherche(5,[-2, 5, 3, 5, 4, 5]))

# Vérification par doctest
from doctest import testmod
testmod()