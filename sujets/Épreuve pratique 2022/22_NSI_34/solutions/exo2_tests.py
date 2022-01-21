import unittest
import exo2 as exo


from random import randint

class Validation(unittest.TestCase):

    def negatif(image):
        L = [[0 for k in range(len(image[0]))] for i in range(len(image))]
        for i in range(len(image)):
            for j in range(len(image[0])):
                L[i][j] = 255 - image[i][j]
        return L

    def binaire(image, seuil):
        L = [[0 for k in range(len(image[0]))] for i in range(len(image))]
        for i in range(len(image)):
            for j in range(len(image[0])):
                if image[i][j] < seuil :
                    L[i][j] = 0
                else:
                    L[i][j] = 1
        return L


    def test_nbLigne(self):
        img=[[20, 34, 254, 145, 6],
             [23, 124, 287, 225, 69],
             [197, 174, 207, 25, 87],
             [255, 0, 24, 197, 189]]
        self.assertEqual(exo.nbLig(img), 4, 
                msg="\nErreur:\nfonction 'nbLig()' incorrecte")
        
        nb_lig = randint(5, 20)
        nb_col = randint(5, 20)
        img_alea = [[randint(0, 255) for _ in range(nb_col)] for _ in range(nb_lig)]
        
        self.assertEqual(exo.nbLig(img_alea), nb_lig, 
                msg="\nErreur:\nfonction 'nbLig()' incorrecte")


    def test_nbColone(self):
        img=[[20, 34, 254, 145, 6],
             [23, 124, 287, 225, 69],
             [197, 174, 207, 25, 87],
             [255, 0, 24, 197, 189]]
        self.assertEqual(exo.nbCol(img), 5, 
                msg="\nErreur:\nfonction 'nbCol()' incorrecte")
        
        nb_lig = randint(5, 20)
        nb_col = randint(5, 20)
        img_alea = [[randint(0, 255) for _ in range(nb_col)] for _ in range(nb_lig)]
        
        self.assertEqual(exo.nbCol(img_alea), nb_col, 
                msg="\nErreur:\nfonction 'nbCol()' incorrecte")


    def test_negatif(self):
        img=[[20, 34, 254, 145, 6],
             [23, 124, 287, 225, 69],
             [197, 174, 207, 25, 87],
             [255, 0, 24, 197, 189]]
        neg_test = exo.negatif(img)
        neg_ok = Validation.negatif(img)
        self.assertEqual(neg_test, neg_ok,
                msg="\nErreur:\nfonction 'negatif()' incorrecte")

        
        nb_lig = randint(5, 20)
        nb_col = randint(5, 20)
        img_alea = [[randint(0, 255) for _ in range(nb_col)] for _ in range(nb_lig)]
        neg_test = exo.negatif(img_alea)
        neg_ok = Validation.negatif(img_alea)
        
        self.assertEqual(neg_test, neg_ok,
                msg="\nErreur:\nfonction 'negatif()' incorrecte")


    def test_binaire(self):
        img=[[20, 34, 254, 145, 6],
             [23, 124, 287, 225, 69],
             [197, 174, 207, 25, 87],
             [255, 0, 24, 197, 189]]
        bin_test = exo.binaire(img, 120)
        bin_ok = Validation.binaire(img, 120)
        self.assertEqual(bin_test, bin_ok,
                msg="\nErreur:\nfonction 'binairef()' incorrecte")

        
        nb_lig = randint(5, 20)
        nb_col = randint(5, 20)
        img_alea = [[randint(0, 255) for _ in range(nb_col)] for _ in range(nb_lig)]
        seuil = randint(10, 245)
        bin_test = exo.binaire(img_alea, seuil)
        bin_ok = Validation.binaire(img_alea, seuil)
        
        self.assertEqual(bin_test, bin_ok,
                msg="\nErreur:\nfonction 'binaire()' incorrecte")
                

unittest.main()