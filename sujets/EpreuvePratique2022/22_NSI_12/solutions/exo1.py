"""
Author: Pascal Padilla
Source: correction de l'exercice 1 du sujet 12 des épreuves pratiques NSI 2022
"""

from doctest import testmod


def moyenne(tab: list):
    """ Calculer la moyenne d'un tableau passé en argument.

    Args:
        tab (list): tableau de nombres

    Returns:
        float: valeur moyenne

    Tests et Exemples:
    >>> moyenne([5,3,8])
    5.333333333333333
    >>> moyenne([1,2,3,4,5,6,7,8,9,10])
    5.5
    >>> moyenne([])
    'erreur'
    """
    # clause de garde pour éviter les tableaux vides
    if tab == []:
        return 'erreur'

    # en cours, on a aussi vu le mot clé 'assert'
    # mais ce n'est pas exactement ce qui est demandé dans
    # l'énoncé, alors, je commente la ligne suivante

    # assert tab != [], 'erreur'

    # initialisation de la longueur du tableau et de l'accumulateur
    n = len(tab)
    somme = 0

    # invariant : à chaque arrivée dans la boucle, 'somme' contient le cumul
    #   des valeurs parcourues jusqu'à i-1

    for i in range(n):
        somme += tab[i]

    # à la sortie de la boucle, somme contient le cumul
    # de toutes les valeurs du tableau

    return somme / n


# Tests et exemples
print(moyenne([5,3,8]))
print(moyenne([1,2,3,4,5,6,7,8,9,10]))
print(moyenne([]))


# Utilisation de doctest
testmod()
