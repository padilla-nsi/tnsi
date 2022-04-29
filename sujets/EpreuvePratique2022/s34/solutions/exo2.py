"""
Author: Pascal Padilla
Source: correction de l'exercice 2 du sujet 34 des épreuves pratiques NSI 2022

Remarques:
    * l'image est dans un tableau à deux dimensions : [[...], [...], ...]
    * c'est un tableau de tableaux
"""

def nbLig(image):
    '''renvoie le nombre de lignes de l'image'''
    # le nombre de ligne est égal au nombre de cases du tableau image
    return len(image)

def nbCol(image):
    '''renvoie la largeur de l'image'''
    # le nombre de colonne est égal au nombre de case de chaque élément
    # de l'image.
    # on prend ici la première case de image : image[0] et on calcule
    #  sa taille
    return len(image[0])

def negatif(image):
    '''renvoie le négatif de l'image sous la forme
       d'une liste de listes'''
    # on créé une image de 0 aux mêmes dimensions que le paramètre image
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))]

    # parcours de l'image où i est l'indice de la ligne courante
    for i in range(len(image)):
        # parcours de la ligne ou j est l'indice de la colonne courante
        for j in range(nbCol(image)):
            # l'énoncé dit que: pixel_negatif + pixel_normal = 255
            # ce qui se traduit par:   x_n + x_i = 255
            # on a donc l'affectation: x_n <- 255 - x_i
            L[i][j] = 255 - image[i][j]
    return L

def binaire(image, seuil):
    '''renvoie une image binarisée de l'image sous la forme
       d'une liste de listes contenant des 0 si la valeur
       du pixel est strictement inférieure au seuil
       et 1 sinon'''
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))] # on crée une image de 0 aux mêmes dimensions que le paramètre image
    for i in range(len(image)):
        for j in range(nbCol(image)):

            # cas du pixel inférieur strictement au seuil
            if image[i][j] < seuil :
                L[i][j] = 0
            # cas du pixel supérieur ou égal au seuil
            else:
                L[i][j] = 1
    return L


img=[[20, 34, 254, 145, 6], [23, 124, 287, 225, 69], [197, 174, 207, 25, 87], [255, 0, 24, 197, 189]]

# vérification avec des assertions
assert nbLig(img) == 4
assert nbCol(img) == 5
assert negatif(img) == [[235, 221, 1, 110, 249], [232, 131, -32, 30, 186], [58, 81, 48, 230, 168], [0, 255, 231, 58, 66]]
assert binaire(img,120) == [[0, 0, 1, 1, 0], [0, 1, 1, 1, 0], [1, 1, 1, 0, 0], [1, 0, 0, 1, 1]]

# vérification avec des affichages
print(nbLig(img))
print(nbCol(img))
print(negatif(img))
print(binaire(img,120))
