"""
Author: Pascal Padilla
Source: correction de l'exercice 1 du sujet 30 des épreuves pratiques NSI 2022

Remarques:
    * algorithme classique au cœur du tri fusion ! (merge sort)
"""


def fusion(tab1: list, tab2: list) -> list:
    """
    Tests et Exemples:
    >>> fusion([3, 5], [2, 5])
    [2, 3, 5, 5]
    >>> fusion([-2, 4], [-3, 5, 10])
    [-3, -2, 4, 5, 10]
    >>> fusion([4], [2, 6])
    [2, 4, 6]
    """
    # nombre d'éléments de chaque tableaux
    n_1 = len(tab1)
    n_2 = len(tab2)

    # création d'un tableau de taille égale à n1 + n2
    # intialement remplis avec des `None`
    tab_fusion = [None] * (n_1 + n_2)

    # BOUCLE: parcours de tab1 et tab2
    # -> invariant:
    #   * tab1[0 .. i-1] a été parcouru
    #   * tab2[0 .. j-1] a été parcouru
    #   * tab_fusion[0 .. i+j-1] est bien rempli
    i = 0
    j = 0

    # -> condition d'arrêt: 
    #   * tab1 est complètement parcouru ET tab2 aussi
    #   * => donc i vaut n1 ET j vaut n2
    while not(i == n_1 and j == n_2):
        # cas où tab1 est complètement parcouru
        if i == n_1:
            # remplissage avec tab2
            tab_fusion[i+j] = tab2[j]
            j = j + 1
        
        # cas où tab2 est complètement parcouru
        elif j == n_2:
            # remplissage avec tab1
            tab_fusion[i+j] = tab1[i]
            i = i + 1
        
        # cas où tab1 et tab2 ne sont pas entièrement parcouru
        else:
            # l'élément courant de tab1 et plus petit que celui de tab2
            if tab1[i] < tab2[j]:
                tab_fusion[i+j] = tab1[i]
                i = i + 1
            
            # l'élément courant de tab2 est plus petit ou égal à celui de tab1
            else:
                tab_fusion[i+j] = tab2[j]
                j = j + 1

    # fin BOUCLE
    # tab1 et tab2 sont entièrement parcouru
    # et tab_fusion est correct
    return tab_fusion



# Vérification par doctest
from doctest import testmod
testmod()


print(sorted([1,3,2]))

from random import choice

txt = ''.join([choice(["I", "V", "X", "L", "C", "D", "M"]) for _ in range(5)])

print(txt)