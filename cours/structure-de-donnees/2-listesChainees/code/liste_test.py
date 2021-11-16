import unittest

from operations_base import *
from liste2 import *

import liste2 as eleve


msg_exemple = "l'exemple de l'enonce ne fonctionne pas :( "


class Constructeur_tests(unittest.TestCase):
    def test_exemple(self):
        lst = eleve.Liste()
        self.assertIsNone(lst.tete, msg=msg_exemple)


class Est_vide_tests(unittest.TestCase):
    def test_exemple_1(self):
        lst = eleve.Liste()
        self.assertTrue(lst.est_vide(),
            msg= msg_exemple + " Avec la liste vide, la methode doit renvoyer True, mais elle renvoie " + str(lst.est_vide()))
        
    def test_exemple_2(self):
        lst = eleve.Liste()
        lst.tete = Maillon(1, None)
        self.assertFalse(lst.est_vide(),
            msg=msg_exemple + " La liste avec un maillon n'est pas vide. La methode doit renvoyer False, mais elle renvoie " + str(lst.est_vide()))
    
class Ajoute_tests(unittest.TestCase):
    def test_exemple_1(self):
        lst = eleve.Liste()
        lst.ajoute(1)
        self.assertEqual(lst.tete.valeur, 1, 
            msg=msg_exemple + " La liste contient un maillon avec la valeur 1. L'attribut tete.valeur doit donc être egal a 1, mais il vaut " + str(lst.tete.valeur))
        
    def test_exemple_2(self):
        lst = eleve.Liste()
        lst.ajoute(1)        
        lst.ajoute(2)
        self.assertEqual(lst.tete.valeur, 2, 
            msg=msg_exemple + " Apres avoir ajoute dans cet ordre 1 puis 2, la liste contient deux valeurs. L'attribut tete.valeur doit être egal a 2, mais il vaut " + str(lst.tete.valeur))
       
    def test_exemple_3(self):
        lst = eleve.Liste()
        lst.ajoute(1)        
        lst.ajoute(2)
        self.assertEqual(lst.tete.suivant.valeur, 1, 
            msg=msg_exemple + " Apres avoir ajoute dans cet ordre 1 puis 2, la liste contient deux valeurs. L'attribut tete.suivant.valeur doit être egal a 1, mais il vaut " + str(lst.tete.suivant.valeur))

class Getitem_tests(unittest.TestCase):
    def test_exemple_0(self):
        lst = eleve.Liste()
        lst.ajoute(4)
        lst.ajoute(2)
        lst.ajoute(1)
        self.assertEqual(lst[0], 1, 
            msg=msg_exemple + " Apres avoir ajoute a la liste 4, puis 2, puis 1, le maillon lst[0] doit être egal a 1, mais il vaut " + str(lst[0]))
            
    def test_exemple_1(self):
        lst = eleve.Liste()
        lst.ajoute(4)
        lst.ajoute(2)
        lst.ajoute(1)
        self.assertEqual(lst[1], 2, 
            msg=msg_exemple + " Apres avoir ajoute a la liste 4, puis 2, puis 1, le maillon lst[1] doit être egal a 2, mais il vaut " + str(lst[1]))
            
    def test_exemple_2(self):
        lst = eleve.Liste()
        lst.ajoute(4)
        lst.ajoute(2)
        lst.ajoute(1)
        self.assertEqual(lst[2], 4, 
            msg=msg_exemple + " Apres avoir ajoute a la liste 4, puis 2, puis 1, le maillon lst[2] doit être egal a 4, mais il vaut " + str(lst[2]))

class Reverse_tests(unittest.TestCase):
  

    def test_exemple_3(self):
        lst = eleve.Liste()
        lst.ajoute(3)
        lst.ajoute(2)
        lst.ajoute(1)
        lst.reverse()
        self.assertEqual(lst[0], 3, msg=msg_exemple + 
            "\n\nApres avoir ajoute 3, puis 2 puis 1, si on applique reverse a la liste.\nMais attention, la liste initiale ne doit pas avoir change ! Or ici, au lieu de valeur 3,\non a lst[0] == " + str(lst[0]))   

    def test_exemple_4(self):
        lst = eleve.Liste()
        lst.ajoute(3)
        lst.ajoute(2)
        lst.ajoute(1)
        lst.reverse()
        self.assertEqual(lst[1], 2, msg=msg_exemple + 
            "\n\nApres avoir ajoute 3, puis 2 puis 1, si on applique reverse a la liste.\nMais attention, la liste initiale ne doit pas avoir change ! Or ici, au lieu de valeur 2,\non a lst[1] == " + str(lst[1]))   

    def test_exemple_5(self):
        lst = eleve.Liste()
        lst.ajoute(3)
        lst.ajoute(2)
        lst.ajoute(1)
        lst.reverse()
        self.assertEqual(lst[2], 1, msg=msg_exemple + 
            "\n\nApres avoir ajoute 3, puis 2 puis 1, si on applique reverse a la liste.\nMais attention, la liste initiale ne doit pas avoir change ! Or ici, au lieu de valeur 1,\non a lst[2] == " + str(lst[2]))



class Add_tests(unittest.TestCase):
    def test_exemple_0(self):
        lst1 = eleve.Liste()
        lst1.ajoute(1)
        lst2 = eleve.Liste()
        lst2.ajoute(3)
        lst2.ajoute(2)
        lst3 = lst1  + lst2
        self.assertEqual(lst3[0], 1, msg=msg_exemple + 
            " Il faut que lst3[0] == 1, or ici il vaut " + str(lst3[0]))

    def test_exemple_1(self):
        lst1 = eleve.Liste()
        lst1.ajoute(1)
        lst2 = eleve.Liste()
        lst2.ajoute(3)
        lst2.ajoute(2)
        lst3 = lst1  + lst2
        self.assertEqual(lst3[1], 2, msg=msg_exemple + 
            " Il faut que lst3[1] == 2, or ici il vaut " + str(lst3[1]))

    def test_exemple_2(self):
        lst1 = eleve.Liste()
        lst1.ajoute(1)
        lst2 = eleve.Liste()
        lst2.ajoute(3)
        lst2.ajoute(2)
        lst3 = lst1  + lst2
        self.assertEqual(lst3[2], 3, msg=msg_exemple + 
            " Il faut que lst3[2] == 3, or ici il vaut " + str(lst3[2]))



unittest.main()