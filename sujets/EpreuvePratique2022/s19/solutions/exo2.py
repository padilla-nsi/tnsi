"""
Author: Pascal Padilla
Source: correction de l'exercice 2 du sujet 19 des épreuves pratiques NSI 2022

Remarques :
    * quelques corrections d'espaces après les virgules
"""


def chercher(T, n, i, j):
    # cas de débordement de la zone de recherche
    # → début de la zone (i) avant 0
    # → fin de la zone (j) après le dernier élément 
    if i < 0 or j >= len(T) :
        print("Erreur")
        return None

    # la zone de recherche est vide car i "croise" j
    if i > j :
        return None

    # indice médian de la zone de recherche
    m = (i + j) // 2

    # cas où la valeur médiane est plus petit que
    # la valeur recherchée n
    # et donc on va chercher dans la zone au dessus de médiane
    # (on met à jour le début de la zone de recherche i) 
    if T[m] < n :
        return chercher(T, n, m + 1 , j)
    
    # cas de la valeur médiane plus grande que n
    # et donc on recherche dans la zone avant la médiane
    # et donc on met à jour la fin de la zone j
    elif n < T[m] :
        return chercher(T, n, i , m - 1)

    # la valeur médiane est égale à n : trouvé !
    # et donc on renvoie l'indice correspondant
    else :
        return m


# tests avec des assertions:
assert chercher([1,5,6,6,9,12],7,0,10) == None
assert chercher([1,5,6,6,9,12],7,0,5) == None
assert chercher([1,5,6,6,9,12],9,0,5) == 4
assert chercher([1,5,6,6,9,12],6,0,5) == 2


# tests avec des affichages:
print(chercher([1,5,6,6,9,12],7,0,10))
print(chercher([1,5,6,6,9,12],7,0,5))
print(chercher([1,5,6,6,9,12],9,0,5))
print(chercher([1,5,6,6,9,12],6,0,5))
