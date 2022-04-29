"""
Author: Pascal Padilla
Source: correction de l'exercice 1 du sujet 35 des épreuves pratiques NSI 2022

Remarques:

"""


def moyenne(tab):
    '''
        moyenne(list) -> float
        Entrée : un tableau non vide d'entiers
        Sortie : nombre de type float
        Correspondant à la moyenne des valeurs présentes dans le
        tableau

    Tests et exemples:
    >>> moyenne([1])
    1.0
    >>> moyenne([1,2,3,4,5,6,7])
    4.0
    >>> moyenne([1,2])
    1.5
    '''
    # nombre de cases du tableau :
    nb_valeurs = len(tab)

    # initialisation invariant
    #  -> somme contient la somme des valeurs de tab[0 .. i-1]
    somme = 0

    # initialisation
    #  -> i = 0
    # condition d'arrêt
    #  -> i == n
    for i in range(0, nb_valeurs):
        somme += tab[i]

    # après la boucle
    #  -> tout le tableau est parcouru
    #  -> donc somme contient la somme des valeurs de TOUT le tableau

    # calcul de la moyenne
    return somme/nb_valeurs


# vérification avec des assertions
assert moyenne([1]) == 1
assert moyenne([1,2,3,4,5,6,7]) == 4
assert moyenne([1,2]) == 1.5

# vérification avec des affichagges
print(moyenne([1]))
print(moyenne([1,2,3,4,5,6,7]))
print(moyenne([1,2]))

# vérification avec doctest
from doctest import testmod
testmod()
