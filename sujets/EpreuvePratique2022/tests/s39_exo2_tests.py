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


def generer_dessin(ligne, col):
    dessin = [[randint(0, 1) for _ in range (col)] for _ in range(ligne)]
    return dessin


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
    def test_exemple_coeur(self):
        grille = coeur
        zoom = 3
        test = exo.zoomDessin(grille, zoom)
        ok   =     zoomDessin(grille, zoom)

        txt = "\nErreur test exemple: fonction 'zoomGrille()' incorrecte sur le coeur avec zoom=3"
        self.assertEqual(test, ok, msg = txt)


    def test_random_zoomListe_x20(self):
        for _ in range(20):
            zoom = randint(1, 4)
            liste = [randint(0, 1) for _ in range(randint(1, 20))]
            test = exo.zoomListe(liste, zoom)
            ok   = zoomListe(liste, zoom)

            txt = "\nErreur test aleatoire:"
            txt += "\nfonction 'zoomListe("+ str(liste) +", "+ str(zoom) +")' incorrecte"
            self.assertEqual(test, ok, msg = txt)


    def test_random_zoomDessin_x20(self):
        for _ in range(20):
            grille = generer_dessin(10, 10)
            for zoom in range(1,4):
                test = exo.zoomDessin(grille, zoom)
                ok   =     zoomDessin(grille, zoom)
                txt = "\nErreur test aleatoire:"
                txt += "\nfonction 'zoomGrille("+ str(grille) +", "+ str(zoom) +")' incorrecte !"
                self.assertEqual(test, ok, msg = txt)


if __name__ == '__main__'      :
    unittest.main()