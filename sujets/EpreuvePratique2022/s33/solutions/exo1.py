"""
Author: Pascal Padilla
Source: correction de l'exercice 1 du sujet 33 des épreuves pratiques NSI 2022

Remarques:
    * calcul à l'aide des valeurs `0` et `1` du tableau :
    tableau  : [1, 0, 1, 0, 0, 1, 1]
    nb_decimal = 1×2^6 + 0×2^5 + 1×2^4 + 0×2^3 + 0×2^2 + 1×2^1 + 1×2^0

    * difficulté: les indices du tableau ne correspondent PAS aux exposants
    tableau  : [1, 0, 1, 0, 0, 1, 1]
    indices  :  0  1  2  3  4  5  6
    exposants:  6  5  4  3  2  1  0

    * 2 méthodes :
        1. trouver une relation entre indice et exposant
        2. trouver une astuce algorithmique

    * Méthode 1.
    Il faut se servir de la taille (ici `7`).
    indices  :      0|    1|    2|    3|    4|    5|    6
    exposants:      6|    5|    4|    3|    2|    1|    0
    exposants:  7-1-0|7-1-1|7-1-2|7-1-3|7-1-4|7-1-5|7-1-6

    comme cela on a la relation: exposant = 7-1 - indice

    * Méthode 2.
    Il faut arriver à récupérer les valeurs du tableau par la fin.
    Ohhhh ! c'est une pile.
    Et c'est exactement ce que fait la méthode .pop() sur les tableaux !
"""



def convertir(T):
    """
    MÉTHODE 1. relation mathématique

    T est un tableau d'entiers, dont les éléments sont 0 ou 1 et
    représentant un entier écrit en binaire. Renvoie l'écriture
    décimale de l'entier positif dont la représentation binaire
    est donnée par le tableau T

    Tests et exemples:
    >>> convertir([1, 0, 1, 0, 0, 1, 1])
    83
    >>> convertir([1, 0, 0, 0, 0, 0, 1, 0])
    130
    """
    nb_decimal = 0
    n = len(T)
    for i in range(n):
        nb_decimal += T[i] * 2**(n - i - 1)
    return nb_decimal



def convertir(T):
    """
    MÉTHODE 2. voir un tableau comme un pile

    T est un tableau d'entiers, dont les éléments sont 0 ou 1 et
    représentant un entier écrit en binaire. Renvoie l'écriture
    décimale de l'entier positif dont la représentation binaire
    est donnée par le tableau T

    Tests et exemples:
    >>> convertir([1, 0, 1, 0, 0, 1, 1])
    83
    >>> convertir([1, 0, 0, 0, 0, 0, 1, 0])
    130
    """
    nb_decimal = 0
    n = len(T)
    for i in range(n):
        coef = T.pop()
        nb_decimal += coef * 2**i
    
    return nb_decimal


# vérification avec des assertions
assert convertir([1, 0, 1, 0, 0, 1, 1]) == 83
assert convertir([1, 0, 0, 0, 0, 0, 1, 0]) == 130

# vérification avec des affichages
print(convertir([1, 0, 1, 0, 0, 1, 1]))
print(convertir([1, 0, 0, 0, 0, 0, 1, 0]))

# vérification avec doctest
from doctest import testmod
testmod()
