"""
Author: Pascal Padilla
Source: correction de l'exercice 1 du sujet 38 des épreuves pratiques NSI 2022

Remarques:
    * toujours délicat car il y a deux boucles !
"""


def tri_selection(tab: list) -> list:
    """ Tri par sélection du tableau tab

    Exemples et tests:
    >>> tri_selection([1,52,6,-9,12])
    [-9, 1, 6, 12, 52]
    """
    nb_elements = len(tab)
    # BOUCLE 1: parcourir tout le tableau (sauf la dernière case, ce n'est pas la peine)
    # pour mettre au fur et à mesure les plus petits éléments devant, triés
    # -> invariant: tab[0 .. i-1] est trié avec les plus petits éléments de tab
    for i in range(nb_elements - 1):
        # BOUCLE 2: parcourir la zone tab[i .. dernière case] à la recherche
        # de l'indice du plus petit élément
        # -> invariant: i_min est l'indice du plus petit élément de la zone tab[i .. j-1]
        i_min = i
        # -> initialisation: j <- i+1 (et donc i_min est correct)
        # -> condition d'arrêt: après la boucle j <- indice de la dernière case (nb_element-1)
        for j in range(i+1, nb_elements):
            # maintien de l'invariant si un élément plus petit est trouvé
            if tab[j] < tab[i_min]:
                # mise à jour de l'indice du plus petit élément
                i_min = j
        
        # fin BOUCLE 2: i_min est l'indice du plus petit élément de tab[i .. dernier]

        # permutation entre élément d'indice `i` et `i_min`
        tab[i], tab[i_min] = tab[i_min], tab[i]
    
    # fin BOUCLE 1: tout le tableau est parcouru sauf la dernière case
    # toutes les cases avant la dernière sont donc triées et inférieures à la dernière case
    # le tableau est donc trié en entier (c'est pour cela que ce n'est pas la peine de 
    # faire un tour de boucle supplémentaire)
    
    # tableau trié correctement: renvoie
    return tab



# vérification avec des assertions
assert tri_selection([1,52,6,-9,12]) == [-9, 1, 6, 12, 52]

# vérification avec des affichages
print(tri_selection([1,52,6,-9,12])) # [-9, 1, 6, 12, 52]

# Vérification avec doctest
from doctest import testmod
testmod()
