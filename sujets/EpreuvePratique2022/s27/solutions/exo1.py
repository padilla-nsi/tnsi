"""
Author: Pascal Padilla
Source: correction de l'exercice 1 du sujet 27 des épreuves pratiques NSI 2022

Remarques:
    * programmation récursive
    * algorithme identique à celui de l'énoncé
"""




def taille(arbre, lettre):
    """Taille d'un arbre binaire

    Args:
        arbre (list): arbre binaire
        lettre (str): sommet de l'arbre

    Returns:
        int: taille (nombre de nœuds)
    
    Exemples et tests:
    >>> a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], 'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], 'H':['','']}
    >>> taille(a, 'F')
    9
    """
    fils_g = arbre[lettre][0]
    fils_d = arbre[lettre][1]
    
    if fils_g == '' and fils_d == '':
        return 1
    
    if fils_g == '':
        return 1 + taille(arbre, fils_d)

    if fils_d == '':
        return 1 + taille(arbre, fils_g)

    return 1 + taille(arbre, fils_d) + taille(arbre, fils_g)



a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], 'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], 'H':['','']}

# vérification avec une assertion
assert taille(a, 'F') == 9

# vérification avec un affichage
print(taille(a, 'F'))

# vérification avec doctest
from doctest import testmod
testmod()