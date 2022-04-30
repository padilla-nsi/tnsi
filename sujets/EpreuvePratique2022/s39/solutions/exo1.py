"""
Author: Pascal Padilla
Source: correction de l'exercice 1 du sujet 39 des épreuves pratiques NSI 2022

Remarques:
"""


def moyenne(tab: list) -> float:
    """ renvoie la moyenne de tab

    Exemples et tests:
    >>> moyenne([10, 20, 30, 40, 60, 110])
    45.0
    """
    nb_valeurs = len(tab)
    # BOUCLE: parcours du tableau pour calculer la somme des valeurs
    # -> invariant: somme est égal au cumul des valeurs parcourus jusqu'à présent
    somme = 0
    for val in tab:
        # maintient de l'invariant
        # mise à jour de la somme
        somme += val

    # fin BOUCLE: somme contient le cumul de toutes les valeurs du tableau

    # formule de la moyenne
    return somme / nb_valeurs


# vérification avec des assertions
assert moyenne([10, 20, 30, 40, 60, 110]) == 45.0

# vérification avec des affichages
print(moyenne([10, 20, 30, 40, 60, 110]))   # 45.0

# vérification avec doctest
from doctest import testmod
testmod()
