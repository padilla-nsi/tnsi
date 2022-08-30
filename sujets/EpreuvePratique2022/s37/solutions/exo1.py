"""
Author: Pascal Padilla
Source: correction de l'exercice 1 du sujet 37 des épreuves pratiques NSI 2022

Remarques:
    * je propose deux version, boucle FOR et boucle WHILE
"""


def verifie(tab: list) -> bool:
    """ Renvoie vrai <=> est trié dans l'ordre croissant

    Tests et exemples:
    >>> verifie([0, 5, 8, 8, 9])
    True
    >>> verifie([8, 12, 4])
    False
    >>> verifie([-1, 4])
    True
    >>> verifie([5])
    True
    """
    # Cas des tableaux vide et de taille 1: renvoie vrai car triés
    if len(tab) <= 1:
        return True

    # BOUCLE:
    # -> invariant: la zone tab[0 .. i-1] du tableau est triée
    # c'est-à-dire que pour tout i de [1 .. i-1], tab[i-1] <= tab[i]
    # -> initialisation: i commence à 1 (et pas à 0 car on appelle tab[i-1])
    for i in range(1, len(tab)):
        # l'invariant n'est pas maintenu: le tableau entier n'est pas trié
        if tab[i] < tab[i-1]:
            return False

    # fin BOUCLE: le tableau entier est trié
    return True



def verifie_while(tab: list) -> bool:
    """ Renvoie vrai <=> est trié dans l'ordre croissant

    Tests et exemples:
    >>> verifie_while([0, 5, 8, 8, 9])
    True
    >>> verifie_while([8, 12, 4])
    False
    >>> verifie_while([-1, 4])
    True
    >>> verifie_while([5])
    True
    """
    # Cas des tableaux vide et de taille 1: renvoie vrai car triés
    if len(tab) <= 1:
        return True

    # BOUCLE:
    # -> invariant: la zone tab[0 .. i-1] du tableau est triée
    # c'est-à-dire que pour tout i de [1 .. i-1], tab[i-1] <= tab[i]
    # -> initialisation: i commence à 1 (et pas à 0 car on appelle tab[i-1])
    i = 1
    # -> condition d'arrêt: tout le tableau a été parcouru et i > dernier indice
    # -> condition d'arrêt: le successeur est inférieur au prédécesseur
    while not(i == len(tab) or tab[i] < tab[i-1]):
        i = i+1
    
    # cas de tout le tableau parcouru
    if i == len(tab):
        return True
    # cas où une partie du tableau n'est pas bien triée
    else:
        return False



# Vérification avec des assertions
assert verifie([0, 5, 8, 8, 9]) == True
assert verifie([8, 12, 4])      == False
assert verifie([-1, 4])         == True
assert verifie([5])             == True

# # Vérification avec des affichages
print(verifie([0, 5, 8, 8, 9]))
print(verifie([8, 12, 4]))
print(verifie([-1, 4]))
print(verifie([5]))

# Vérification avec doctest
from doctest import testmod
testmod()
