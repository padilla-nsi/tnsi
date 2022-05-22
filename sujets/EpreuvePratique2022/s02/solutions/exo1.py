"""
Author: Pascal Padilla
Source: correction de l'exercice 1 du sujet 2 des épreuves pratiques NSI 2022

Remarques:
"""


def moyenne(tab: list) -> float:
    """ Calcul une moyenne pondérée.

    Args:
        tab (list): tableau de couples de notes 
        de la forme (note: int, coefficient: int)

    Returns:
        float: moyenne pondérée
    
    Tests et Exemples:
    >>> moyenne([(15, 2), (9, 1), (12, 3)])
    12.5
    >>> moyenne([(10, 2)])
    10.0
    """
    somme = 0
    coef_total = 0

    # Invariant: `somme` est le cumul des notes pondérées par les coefficients parcourues
    # Invariant: `coef_total` est la somme de tous les coefficients parcourus
    for i in range(len(tab)):
        couple = tab[i]
        note = couple[0]
        coefficient = couple[1]

        somme = somme + note * coefficient
        coef_total = coef_total + coefficient

    return somme / coef_total



# Tests avec des affichages
print(moyenne([(15,2),(9,1),(12,3)]))   # 12.5 espéré
print(moyenne([(10, 2)]))               # 10 espéré


# Tests avec des assertions
assert moyenne([(15,2),(9,1),(12,3)]) == 12.5
assert moyenne([(10, 2)]) == 10


# Tests avec doctest
from doctest import testmod
testmod()
