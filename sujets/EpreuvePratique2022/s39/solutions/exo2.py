"""
Author: Pascal Padilla
Source: correction de l'exercice 2 du sujet 39 des épreuves pratiques NSI 2022

Remarques:
"""

# un tableau à deux dimensions : un tableau de tableau !
# pour accéder à la 3ème ligne : coeur[2]
# pour accéder à la 5ème colonne de la 3ème ligne : coeur[2][4] 
coeur = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
         [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0], \
         [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0], \
         [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0], \
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], \
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], \
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], \
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0], \
         [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0], \
         [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], \
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], \
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def affiche(dessin):
    ''' affichage d'une grille : les 1 sont représentés par
        des "*" , les 0 par deux espaces "  " '''
    # parcours le dessin, ligne par ligne
    for ligne in dessin:
        # pour chaque ligne, colonne par colonne
        for col in ligne:
            # cas d'un pixel égal à '1'
            if col == 1:
                # afficher une ' *'
                print(" *",end="")
            else:
                # afficher des espaces
                print("  ",end="")
        print()


def zoomListe(liste_depart,k):
    '''renvoie une liste contenant k fois chaque
       élément de liste_depart'''
    # BOUCLE 1: parcours de la liste en dupliquant k fois chaque pixel
    # -> invariant: liste_zoom contient k fois chaque élément
    #               de la zone parcourue jusqu'à présent
    liste_zoom = []
    # -> condition d'arrêt: après le dernier pixel de la liste_depart
    for elt in liste_depart :
        # BOUCLE 2: duplication du pixel courant
        # -> invariant: le pixel a été dupliqué i fois
        # -> condition d'arrêt: après la boucle i <- k-1
        for i in range(k):
            # ajout d'une copie du pixel
            liste_zoom.append(elt)
        # fin BOUCLE 2
    # fin BOUCLE 1: tous les pixel ont été dupliqués
    return liste_zoom

def zoomDessin(grille,k):
    '''renvoie une grille où les lignes sont zoomées k fois
       ET répétées k fois'''
    # BOUCLE 1: grossit toutes les lignes (en largeur et en hauteur)
    # -> invariant: grille_zoom contient les lignes grossies en largeur 
    #               et en hauteur de la zone parcourue de la grille
    grille_zoom=[]
    # -> condition d'arrêt: après la boucle traitant la dernière ligne
    for elt in grille:
        # BOUCLE 2: grossit en largeur et en hauteur la ligne courante
        # -> invariant: grille_zoom possède à la fin i copies du zoom
        #               de la ligne courante
        liste_zoom = zoomListe(elt, k)
        # -> condition d'arrêt: après le tour de boucle i <- k-1
        for i in range(k):
            # ajout d'une ligne zoomée de la ligne courante supplémentaire
            grille_zoom.append(liste_zoom)
        
        # fin BOUCLE 2: la ligne courante est complètement ajoutée à grille_zoom
    
    # fin BOUCLE 1: toutes les lignes sont parcours donc
    # toutes les lignes sont sont toutes ajoutées grossies dans grille_zoom

    # grille_zoom est correct
    return grille_zoom

affiche(coeur)
affiche(zoomDessin(coeur,3))
