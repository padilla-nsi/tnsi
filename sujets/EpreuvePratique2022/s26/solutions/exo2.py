"""
Author: Pascal Padilla
Source: correction de l'exercice 2 du sujet 26 des épreuves pratiques NSI 2022

Remarque:
    l'algorithme fait penser à la dichotomie car il partage le tableau en plusieurs zones

    l'algorithme partage le tableau en 3 zones grâce aux indices i et j:
      * celle qui ne contient que des '0' (du début jusqu'à i-1)
      * celle qui ne contient que des '1' (de j+1 à la fin)
      * celle qui n'est pas encore triée  (entre i et j)
"""


def separe(tab):
    # BOUCLE
    # invariants
    #  -> tab[0.. i-1]  contient que des '0'
    #  -> tab[j+1..fin] contient que des '1'
    #  -> tab[i..j] contient un mélange de '0' et de '1' non triés
    # initialisation
    #  -> le tableau entier n'est pas encore trié:
    #     i <- 0 et j <- dernier indice
    i = 0
    j = len(tab) - 1

    # condition d'arrêt
    #  -> la zone à trier est vide : i et j se 'croisent'
    while i < j :
        # le premier élément non trié est un '0'
        if tab[i] == 0 :
            # ne rien faire et diminuer le début de la zone non triée
            # tab [0..i] ne contient que des '0'
            i = i + 1
        
        # le premier élément non trié est un '1'
        else :
            #  permuter le premier élément avec le dernier non trié
            tab[i], tab[j] = tab[j], tab[i]
            # puis diminuer la fin de la zone non triée
            # tab[j..fin] contient que des '1'
            j = j - 1
    
    # le tableau tab est trié
    return tab


# tests avec des assertions
assert separe([1, 0, 1, 0, 1, 0, 1, 0]) == [0, 0, 0, 0, 1, 1, 1, 1]
assert separe([1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0]) == [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]


# tests avec des affichages
print(separe([1, 0, 1, 0, 1, 0, 1, 0]))
print(separe([1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0]))
