import exo2 as exo
import unittest

class validation(unittest.TestCase):
    def test_exemple_valeur(self):
        """ 20 ème carte du paquet est un 8 """
        paquet = exo.PaquetDeCarte()
        paquet.remplir()
        carte = paquet.getCarteAt(20)
        self.assertEqual(carte.getNom(), '8')


    def test_exemple_couleur(self):
        """ 20ème carte du paquet est un coeur """
        paquet = exo.PaquetDeCarte()
        paquet.remplir()
        carte = paquet.getCarteAt(20)
        self.assertEqual(carte.getCouleur(), 'coeur')

    
    def test_paquet_taille(self):
        """ 52 cartes dans un paquet """
        paquet = exo.PaquetDeCarte()
        paquet.remplir()
        self.assertEqual(len(paquet.contenu), 52)


    def test_toutes_les_cartes_dans_paquet(self):
        """ 
            chaque carte est unique dans le paquet 
            et toutes les cartes y sont 
        """
        paquet = exo.PaquetDeCarte()
        paquet.remplir()
        pioche = {'pique': [], 'coeur': [], 'carreau': [], 'trefle': []}
        for carte in paquet.contenu:
            couleur = carte.getCouleur()
            nom = carte.getNom()
            self.assertNotIn(nom, pioche[couleur])
            pioche[couleur].append(nom)

        for couleur in ['pique', 'coeur', 'carreau', 'trefle']:
            for nom in ['As', '2', '3', '4', '5', '6', '7','8', 
                        '9', '10', 'Valet', 'Dame', 'Roi']:
                self.assertIn(nom, pioche[couleur])

    def test_carte_couleur_non_valide(self):
        """ couleurs de cartes : 1, 2, 3 ou 4 """
        for c in [0, 5, 6, 7, 8, 9, 10]:
            self.assertRaises(AssertionError, exo.Carte, c, 1)

    def test_carte_valeur_non_valide(self):
        """ nom de cartes 1..13 """
        for n in range (-100, 1):
            self.assertRaises(AssertionError, exo.Carte, 1, n)

        for n in range (14, 100):
            self.assertRaises(AssertionError, exo.Carte, 1, n)

    def test_getCard_hors_limite(self):
        """ getCard ne fonctionne pas au dessus de 51 """
        paquet = exo.PaquetDeCarte()
        paquet.remplir()
        for i in range(52, 100):
            self.assertRaises(AssertionError, paquet.getCarteAt, i)


unittest.main()
