"""
Author: Pascal Padilla
Source: correction de l'exercice 2 du sujet 22 des épreuves pratiques NSI 2022
"""


def crible(N):
    """renvoie un tableau contenant tous les nombres premiers plus petit que N"""
    # tableau de nombres premiers initialement vide
    premiers = []

    # initialisation du tableau de booléens
    tab = [True] * N
    tab[0], tab[1] = False, False

    # parcours du tableau à partir de la 3ème case 
    # (car 0 et 1 sont traités)
    for i in range(2, N):
        # le nombre courant est premier
        if tab[i] == True:
            # ajoute le nombre courant dans le tableau à renvoyer
            # (attention: c'est le nombre i qu'il faut ajouter
            #  et pas tab[i] qui vaut 'True'...)
            premiers.append(i)

            # met à False tous les multiples à venir du nombre courant
            # partie délicate:
            #  -> pour accéder aux multiples, on parcours tous les
            #     nombres de 2i à la fin (N) MAIS pas de 1 en 1 !
            #     Il faut les parcours de i en i. 
            #     Ainsi, en commençant à 2i, on arrive à 2i + i => 3i
            #                                       puis 3i + i => 4i
            #                                       etc.
            for multiple in range(2*i, N, i):
                # on met chaque multiple à faux car il n'est pas premier
                # (ben ouaip, c'est un multiple !)
                tab[multiple] = False

    # renvoyer le tableau des nombres premiers complété au fur et à mesure
    return premiers


assert crible(40) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]


# tests avec un affichage
print(crible(40))
