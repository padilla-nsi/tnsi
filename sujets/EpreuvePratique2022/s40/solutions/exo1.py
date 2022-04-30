"""
Author: Pascal Padilla
Source: correction de l'exercice 1 du sujet 40 des épreuves pratiques NSI 2022

Remarques:
    * bien lire l'énoncé : on veut un tableau d'indices
"""



def recherche(elt, tab: list) -> list:
    """ Renvoie le tableau des indices de elt dans tab
    
    Exemples et tests:
    >>> recherche(3, [3, 2, 1, 3, 2, 1])
    [0, 3]
    >>> recherche(4, [1, 2, 3])
    []
    """
    # BOUCLE: parcour de tout le tableau à la recherche de elt
    #-> invariant: `indices` est le tableau de tous les indices de elt
    #           dans la zone parcourue jusqu'à présent : tab[0 .. i-1]
    indices = []
    # -> condition d'arrêt: après la boucle i <- dernier indice de tab
    for i in range(len(tab)):
        # maintient de l'invariant
        # cas où l'élément courant correspond à `elt`
        if tab[i] == elt:
            # ajout de l'indice courant dans `indices`
            indices.append(i)
    
    # fin BOUCLE: tout le tableau est parcouru + invariant
    # => indices est correct
    return indices


# Vérification avec des assertions
assert  recherche(3, [3, 2, 1, 3, 2, 1]) == [0, 3]
assert recherche(4, [1, 2, 3]) == []

# Vérifications avec des affichages
print(recherche(3, [3, 2, 1, 3, 2, 1]))     # [0, 3]
print(recherche(4, [1, 2, 3]))              # []

# Vérification avec doctest et testmod
from doctest import testmod
testmod()
