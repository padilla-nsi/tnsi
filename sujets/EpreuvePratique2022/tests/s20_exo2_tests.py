import s20.solutions.exo2 as exo
import unittest


from random import randint, random


class Carre:
    def __init__(self, tableau = [[]]):
        self.ordre = len(tableau)
        self.valeurs = tableau

    def affiche(self):
        '''Affiche un carré'''
        for i in range(self.ordre):
            print(self.valeurs[i])

    def somme_ligne(self, i):
        '''Calcule la somme des valeurs de la ligne i'''
        return sum(self.valeurs[i])

    def somme_col(self, j):
        '''calcule la somme des valeurs de la colonne j'''
        return sum([self.valeurs[i][j] for i in range(self.ordre)])

def est_magique(carre):
    n = carre.ordre
    s = carre.somme_ligne(0)

    #test de la somme de chaque ligne
    for i in range(1, n):
        if carre.somme_ligne(i) != s:
            return False

    #test de la somme de chaque colonne
    for j in range(n):
        if carre.somme_col(j) != s:
            return False

    #test de la somme de chaque diagonale
    if sum([carre.valeurs[k][k] for k in range(n)]) != s:
        return False
    if sum([carre.valeurs[k][n-1-k] for k in range(n)]) != s:
        return False

    return True


class Validation(unittest.TestCase):
    def test_exemple_c2(self):
        c2 = exo.Carre([[1, 1], [1, 1]])
        txt="\nErreur avec exemple c2 de l'enonce (True est attendu)"
        self.assertTrue(exo.est_magique(c2), msg=txt)

    def test_exemple_c3(self):
        c3 = Carre([[2, 9, 4], [7, 5, 3], [6, 1, 8]])
        txt="\nErreur avec exemple c3 de l'enonce (True est attendu)"
        self.assertTrue(exo.est_magique(c3), msg=txt)

    def test_exemple_c4(self):
        c4 = Carre([[4, 5, 16, 9], [14, 7, 2, 11], [3, 10, 15, 6], [13, 12, 8, 1]])
        txt="\nErreur avec exemple c4 de l'enonce (False est attendu)"
        self.assertFalse(exo.est_magique(c4), msg=txt)

    def test_ordre_3(self):
        for i in range(20):
            p = 0.05
            alea_1 = 1 if random() < p else 0
            alea_2 = 1 if random() < p else 0
            alea_3 = 1 if random() < p else 0
            a = randint(20, 100)
            b = randint(20, 100)
            c = randint(20, 100)
            c3 = Carre([[c+a+alea_1, c-a-b, c+b],
                        [c-a+b, c+alea_2, c+a-b],
                        [c-b, c+a+b, c-a+alea_3]])

            txt = "\nErreur avec des carres magiques aleatoire"
            txt += "\npour le carre " + str(c3.valeurs) + " " + str(est_magique(c3))
            txt += " etait attendu..."
            self.assertEqual(exo.est_magique(c3), est_magique(c3), msg=txt)


if __name__ == '__main__':
    unittest.main()
