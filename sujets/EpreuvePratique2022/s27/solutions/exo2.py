"""
Author: Pascal Padilla
Source: correction de l'exercice 2 du sujet 27 des épreuves pratiques NSI 2022

Remarques:
    * ce tri ressemble beaucoup au tri à bulles
    * l'énoncé ne le dit pas, mais les nombres sont forcéments positifs
    (sinon imax = 0 n'est pas une bonne façon d'initialiser)
"""



def tri_iteratif(tab):
    # parcours du tableau :
    #  de la dernière case (inclue) à 0 (exclue)
    #  en allant de -1 en -1 (à l'envers donc !)
    for k in range(len(tab)-1 ,0, -1):
        imax = 0

        # parcours de la zone non triée
        #  de 0 à k (exclu)
        for i in range(0, k):
            if tab[i] > tab[imax] :
                imax = i

        # imax est l'indice de la valeur maxi de la zone non triée
        #
        # l'indice est juste après la zone non triée et donc:
        #  permutation entre tab[k] et tab[imax] si besoin
        if tab[imax] > tab[k] :
            tab[k] , tab[imax] = tab[imax] , tab[k]
    return tab


# vérification avec une assertion
assert tri_iteratif([41, 55, 21, 18, 12, 6, 25]) == [6, 12, 18, 21, 25, 41, 55]


# vérification avec un affichage
print(tri_iteratif([41, 55, 21, 18, 12, 6, 25]))