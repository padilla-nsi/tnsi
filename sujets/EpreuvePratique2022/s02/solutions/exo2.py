"""
Author: Pascal Padilla
Source: correction de l'exercice 2 du sujet 2 des épreuves pratiques NSI 2022

Remarques:
"""


def pascal(n):
    """ Générer une liste correspondant au triangle de Pascal.

    Args:
        n (int): hauteur du triangle de Pascal (moins 1...)

    Returns:
        list: tableau contenant les listes des coefficients, ligne par ligne

    Tests et Exemples:
    >>> pascal(4)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    >>> pascal(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
    """
    C = [[1]]
    for k in range(1, n + 1):
        # on doit ajouter n lignes au tableau C
        Ck = [1]
        for i in range(1, k):
            # on ajoute k coefficients à la ligne Ck
            # le coef à ajouter est égal à la somme des deux 
            #   coefficients situés au dessus de lui
            Ck.append(C[k-1][i-1] + C[k-1][i])

        # on termine la ligne Ck
        #   en ajoutant la dernière valeur qui vaut toujours 1
        Ck.append(1)
        # on ajoute la ligne Ck au tableau C
        C.append(Ck)
    return C


# Tests avec des affichages
print(pascal(4))    # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
print(pascal(5))    # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]


# Tests avec des assertions
assert pascal(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
assert pascal(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]


# Tests avec doctest
from doctest import testmod
testmod()