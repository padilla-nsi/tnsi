import s14.solutions.exo1 as exo
import unittest
from random import *


def correspond(mot: str, mot_a_trous: str) -> bool:
    """Est ce que mot_a_trou peut correspondre à mot ?

    Args:
        mot (str): chaîne de caractère majuscule
        mot_a_trous (str): chaîne à trous (majuscule + '*')

    Returns:
        bool: True si on peut obtenir mot en remplaçant convenablement
        les caractères '*' de mot_a_trous

    Tests et Exemples:
    >>> correspond('INFORMATIQUE', 'INFO*MA*IQUE')
    True
    
    >>> correspond('AUTOMATIQUE', 'INFO*MA*IQUE')
    False
    """
    n = len(mot)
    # compteur pour parcourir les chaînes 0..n-1
    i = 0
    # booléen qui indique que mot et mot_a_trous sont identiques
    est_egal = True

    # condition d'arrêt de la boucle :
    #  * le compteur i dépasse la longueur du mot
    #  * les chaînes sont incompatibles
    while not (i >= n or est_egal == False):
        # jusqu'à présent les chaînes ont été compatibles
        if mot_a_trous[i] !=  '*':
            if mot_a_trous[i] != mot[i]:
                # les caractères sont différents et 
                # ce n'est pas un joker '*'
                # donc les chaines sont désormais incompatibles
                est_egal = False
        i = i + 1

    return est_egal



class Validation(unittest.TestCase):
    def test_exemple_1(self):
        print("\nValidation automatique sur l'exemple 1 de l'énoncé")
        rep_prof = correspond('INFORMATIQUE', 'INFO*MA*IQUE')
        rep_exo  = exo.correspond('INFORMATIQUE', 'INFO*MA*IQUE')

        info = "Erreur la fonction fait un calcul incorrect avec les valeurs de l'énoncé\ncorrespond('INFORMATIQUE', 'INFO*MA*IQUE') doit renvoyer "+ str(rep_prof)+"!"
        self.assertEqual(rep_prof, rep_exo, msg=info)
    
    def test_exemple_2(self):
        print("\nValidation automatique sur l'exemple 2 de l'énoncé")
        rep_prof = correspond('AUTOMATIQUE', 'INFO*MA*IQUE')
        rep_exo  = exo.correspond('AUTOMATIQUE', 'INFO*MA*IQUE')

        info = "Erreur la fonction fait un calcul incorrect avec les valeurs de l'énoncé\ncorrespond('AUTOMATIQUE', 'INFO*MA*IQUE') doit renvoyer "+ str(rep_prof)+"!"
        self.assertEqual(rep_prof, rep_exo, msg=info)

    def test_val_alea_1(self):
        print("\nValidation automatique sur 50 valeurs aléatoires")
        
        for _ in range(50):
            ch = ''.join([chr(randint(ord('A'), ord('Z'))) for _ in range(randint(5, 20))])        
            ch2 = ""
            for char in ch:
                if randint(0, 3) == 0:
                    ch2 += '*'
                elif randint(0, 40) == 0:
                    # sinon 1/40 de chance de changer la lettre ;)
                    ch2 += chr(randint(ord('A'), ord('Z')))
                else:
                    ch2 += char

            rep_prof = correspond(ch, ch2)
            rep_exo  = correspond(ch, ch2)

            info = "Erreur la fonction fait un calcul incorrect avec des aléatoires\ncorrespond("+ch+", "+ch2+") doit renvoyer "+ str(rep_prof)+"!"
            self.assertEqual(rep_prof, rep_exo, msg=info)
            print(rep_prof, ch, ch2)



if __name__ == '__main__':
    unittest.main(testRunner=unittest.TextTestRunner(verbosity=0))