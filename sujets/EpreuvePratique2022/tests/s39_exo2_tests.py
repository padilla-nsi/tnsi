import s39.solutions.exo2 as exo 
import unittest

from random import randint
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


def zoomListe(liste_depart,k):
    '''renvoie une liste contenant k fois chaque 
       élément de liste_depart'''
    liste_zoom = []
    for elt in liste_depart :
        for i in range(k):
            liste_zoom.append(elt)
    return liste_zoom


def zoomDessin(grille,k):
    '''renvoie une grille où les lignes sont zoomées k fois 
       ET répétées k fois'''
    grille_zoom=[]
    for elt in grille:
        liste_zoom = zoomListe(elt, k)
        for i in range(k):
            grille_zoom.append(liste_zoom)
    return grille_zoom


class Validation(unittest.TestCase):
    def test_zoomListe(self):
        for zoom in range(1,4):
            liste = [randint(0, 1), randint(0, 1), randint(0, 1)]
            test = exo.zoomListe(liste, zoom)
            ok   = zoomListe(liste, zoom)
            self.assertEqual(test, ok,
                    msg="\nErreur:\nfonction 'zoomListe("+ str(liste) +", "+ str(zoom) +")' incorrecte")
        
    def test_zoomDessin(self):

        grille = coeur
        zoom = 3
        test = exo.zoomDessin(grille, zoom)
        ok   =     zoomDessin(grille, zoom)
        self.assertEqual(test, ok,
                    msg="\nErreur:\nfonction 'zoomGrille()' incorrecte sur l'exemple (coeur avec zoom=3)")
        
        grille = [[randint(0, 1) for _ in range(3)] for _ in range(3)]
        for zoom in range(1,4):
            test = exo.zoomDessin(grille, zoom)
            ok   =     zoomDessin(grille, zoom)
            self.assertEqual(test, ok,
                    msg="\nErreur:\nfonction 'zoomGrille("+ str(grille) +", "+ str(zoom) +")' incorrecte")

if __name__ == '__main__'      :
    unittest.main()