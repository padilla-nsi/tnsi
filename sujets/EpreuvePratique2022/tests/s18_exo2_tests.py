import s18.solutions.exo2 as exo
import unittest

from random import randint

class Validation(unittest.TestCase):
    def inverse_chaine(chaine):
        result = ''
        for caractere in chaine:
            result = caractere + result
        return result

    def est_palindrome(chaine):
        inverse = Validation.inverse_chaine(chaine)
        return chaine == inverse
        
    def est_nbre_palindrome(nbre):
        chaine = str(nbre)
        return Validation.est_palindrome(chaine)

    def chaine_aleatoire(n):
        texte = ''.join([chr(randint(65,90)) for _ in range(n) ])
        return texte

    def test_inverse_chaine(self):
        """ renvoie bien la chaine inversée """
        self.assertEqual(exo.inverse_chaine('bac'),'cab',
                         msg="inverse_chaine -> pb avec l'exemple")

        n = randint(20, 100)
        texte = Validation.chaine_aleatoire(n)
        self.assertEqual(exo.inverse_chaine(texte),
                Validation.inverse_chaine(texte),
                msg="inverse_chaine -> pb avec chaîne aléatoire")

    def test_est_palindrome(self):
        self.assertEqual(exo.est_palindrome('NSI'), False,
                         msg="est_palindrome -> pb avec l'exemple")

        self.assertEqual(exo.est_palindrome('ISN-NSI'), True,
                         msg="est_palindrome -> pb avec l'exemple")

        n = randint(20, 100)
        texte = Validation.chaine_aleatoire(n)
        txt_palindrome = Validation.inverse_chaine(texte) + texte
        self.assertEqual(exo.est_palindrome(txt_palindrome), True,
                         msg="est_palindrome -> chaîne aléatoire")

        txt_non_palindrome = 'A' + txt_palindrome + 'Z'
        self.assertEqual(exo.est_palindrome(txt_non_palindrome), False,
                         msg="est_palindrome -> chaîne aléatoire")

    def test_est_nbre_palindrome(self):
        self.assertEqual(exo.est_nbre_palindrome(214312), False,
                         msg="est_nbre_palindrome -> pb avec l'exemple")

        self.assertEqual(exo.est_nbre_palindrome(213312), True,
                         msg="est_nbre_palindrome -> pb avec l'exemple")

        
        nb_non_palindrome = randint(10, 10**30)
        while Validation.est_nbre_palindrome(nb_non_palindrome):
            nb_non_palindrome = randint(10, 10**30)
        self.assertEqual(exo.est_nbre_palindrome(nb_non_palindrome), False,
                         msg="est_nbre_palindrome -> pb avec nb aléatoire")
        
        nb_palindrome = int(str(nb_non_palindrome) + Validation.inverse_chaine(str(nb_non_palindrome)))
        self.assertEqual(exo.est_nbre_palindrome(nb_palindrome), True,
                         msg="est_nbre_palindrome -> pb avec nb aléatoire")
        

if __name__ == '__main__':
    unittest.main()