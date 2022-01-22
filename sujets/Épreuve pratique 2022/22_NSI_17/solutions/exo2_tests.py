import exo2 as exo
import unittest
from random import randint


class Noeud:
    '''
    Classe implémentant un noeud d'arbre binaire 
    disposant de 3 attributs :
    - valeur : la valeur de l'étiquette,
    - gauche : le sous-arbre gauche.
    - droit : le sous-arbre droit.
    '''
    def __init__(self, v, g, d):
        self.valeur = v
        self.gauche = g
        self.droite = d


class ABR:
    '''
    Classe implémentant une structure
    d'arbre binaire de recherche.
    '''

    def __init__(self):
        '''Crée un arbre binaire de recherche vide'''
        self.racine = None

    def est_vide(self):
        '''Renvoie True si l'ABR est vide et False sinon.'''
        return self.racine is None

    def parcours(self, tab = []):
        '''
	    Renvoie la liste tab complétée avec tous les
        éléments de l'ABR triés par ordre croissant.

        Tests et Exemples:
        >>> a = ABR()
        >>> a.insere(7)
        >>> a.insere(3)
        >>> a.insere(9)
        >>> a.insere(1)
        >>> a.insere(9)
        >>> a.parcours()
        [1, 3, 7, 9, 9]
        '''
        if self.est_vide():
            return tab
        else:
            self.racine.gauche.parcours(tab)
            # ajoute la valeur de la racine au tableau
            tab.append(self.racine.valeur)
            # parcours récursif à droite
            self.racine.droite.parcours(tab)
            return tab
        
    def insere(self, element):
        '''Insère un élément dans l'arbre binaire de recherche.'''
        if self.est_vide():
            self.racine = Noeud(element, ABR(), ABR())
        else:
            if element < self.racine.valeur:
                self.racine.gauche.insere(element)
            else :
                self.racine.droite.insere(element)

    def recherche(self, element):
        '''
        Renvoie True si element est présent dans l'arbre 
        binaire et False sinon.

        Tests et Exemples:
        >>> a = ABR()
        >>> a.insere(7)
        >>> a.insere(3)
        >>> a.insere(9)
        >>> a.insere(1)
        >>> a.insere(9)
        >>> a.recherche(4)
        False
        >>> a.recherche(3)
        True
	    '''
        if self.est_vide():
            # si l'ABR est vide, element ne peut pas s'y trouver !
            return False
        else:
            if element < self.racine.valeur:
                # recherche récursive dans le sous ABR de gauche
                return self.racine.gauche.recherche(element)
            elif element > self.racine.valeur:
                # recherche récursive dans le sous ABR de droite
                return self.racine.droite.recherche(element)
            else:
                # si element n'est ni > ni < à valeur
                # c'est qu'ils sont égaux !
                return True


class Validation(unittest.TestCase):
    def test_exemple_1_parcours(self):
        print("Test sur l'exemple de parcours de l'enonce")
        a = ABR()
        a.insere(7)
        a.insere(3)
        a.insere(9)
        a.insere(1)
        a.insere(9)
        rep_prof = a.parcours()

        b = exo.ABR()
        b.insere(7)
        b.insere(3)
        b.insere(9)
        b.insere(1)
        b.insere(9)
        rep_exo = b.parcours()

        info = "Erreur avec l'exemple de l'enonce"
        info += "\n=> a.parcours() doit renvoyer [1, 3, 7, 9, 9]"
        self.assertEqual(rep_prof, rep_exo, msg=info)


    def test_exemple_2_recherche(self):
        print("Test sur l'exemple de recherche(4) de l'enonce")
        a = exo.ABR()
        a.insere(7)
        a.insere(3)
        a.insere(9)
        a.insere(1)
        a.insere(9)
        rep_exo = a.recherche(4)

        info = "Erreur avec l'exemple de l'enonce"
        info += "\n=> a.recherche(4) doit renvoyer False"
        self.assertFalse(rep_exo, msg=info)


    def test_exemple_3_recherche(self):
        print("Test sur l'exemple de recherche(3) de l'enonce")
        a = exo.ABR()
        a.insere(7)
        a.insere(3)
        a.insere(9)
        a.insere(1)
        a.insere(9)
        rep_exo = a.recherche(3)

        info = "Erreur avec l'exemple de l'enonce"
        info += "\n=> a.recherche(3) doit renvoyer True"
        self.assertTrue(rep_exo, msg=info)

    def test_random_1_20x(self):
        for _ in range(20):
            a = ABR()
            b = exo.ABR()
            for i in range(20):
                val = randint(-20, 20)
                a.insere(val)
                b.insere(val)

            n = randint(-20, 20)

            rep_prof = a.recherche(n)
            rep_exo  = b.recherche(n)
            info = "Erreur avec un ABR aleatoire"
            info += "\nla methode a.recherche(" + str(n) + ") devait renvoyer "+str(rep_prof)
            self.assertEqual(rep_prof, rep_exo, msg=info)

    def test_random_2_20x(self):
        for _ in range(20):
            a = ABR()
            b = exo.ABR()
            for i in range(20):
                val = randint(-20, 20)
                a.insere(val)
                b.insere(val)

            n = randint(-20, 20)

            rep_prof = a.recherche(n)
            rep_exo  = b.recherche(n)
            info = "Erreur avec un ABR aleatoire"
            info += "\nla methode a.recherche(" + str(n) + ") devait renvoyer "+str(rep_prof)
            self.assertEqual(rep_prof, rep_exo, msg=info)

    def test_random_3_20x(self):
        for _ in range(20):
            a = ABR()
            b = exo.ABR()
            for i in range(20):
                val = randint(-20, 20)
                a.insere(val)
                b.insere(val)

            n = randint(-20, 20)

            rep_prof = a.recherche(n)
            rep_exo  = b.recherche(n)
            info = "Erreur avec un ABR aleatoire"
            info += "\nla methode a.recherche(" + str(n) + ") devait renvoyer "+str(rep_prof)
            self.assertEqual(rep_prof, rep_exo, msg=info)


if __name__ == '__main__':
    unittest.main()