import s05.solutions.exo2 as exo

import unittest


class validation(unittest.TestCase):
    def test_exemple_valeur(self):
        """ 20 eme carte du paquet est un 8 """
        paquet = exo.PaquetDeCarte()
        paquet.remplir()
        carte = paquet.getCarteAt(20)
        self.assertEqual(carte.getNom(), '8',
                         msg="\nErreur: \nla 20eme carte doit être un '8'")


    def test_exemple_couleur(self):
        """ 20eme carte du paquet est un coeur """
        paquet = exo.PaquetDeCarte()
        paquet.remplir()
        carte = paquet.getCarteAt(20)
        self.assertEqual(carte.getCouleur(), 'coeur',
                         msg="\nErreur: \nla 20eme carte doit être un 'coeur'")

    
    def test_paquet_taille(self):
        """ 52 cartes dans un paquet """
        paquet = exo.PaquetDeCarte()
        paquet.remplir()
        self.assertEqual(len(paquet.contenu), 52,
                         msg="\nErreur: \nun paquet remplit doit avoir 52 cartes")


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
            self.assertNotIn(nom, pioche[couleur],
                             msg="\nErreur: \ncarte " + str(nom) + " de " + str(couleur) + " en double dans le paquet rempli")
            pioche[couleur].append(nom)

        for couleur in ['pique', 'coeur', 'carreau', 'trefle']:
            for nom in ['As', '2', '3', '4', '5', '6', '7','8', 
                        '9', '10', 'Valet', 'Dame', 'Roi']:
                info = "\neErreur:\nla carte " + str(nom) + " de " + str(couleur) + " manque dans le paquet rempli"
                self.assertIn(nom, pioche[couleur],
                              msg=info)

    def test_carte_couleur_non_valide(self):
        """ couleurs de cartes : 1, 2, 3 ou 4 """
        for c in [0, 5, 6, 7, 8, 9, 10]:
            with self.assertRaises(AssertionError,
                      msg = "\nErreur: \nassertion sur les couleurs incorrecte dans le constructeur 'Carte'\nla couleur '"+str(c)+"' doit lever une exception"):
                exo.Carte(c, 1)


    def test_carte_valeur_non_valide(self):
        """ nom de cartes 1..13 """
        for n in range (-100, 1):
            with self.assertRaises(AssertionError,
                      msg = "\nErreur: \nassertion sur les noms incorrecte dans le constructeur 'Carte'\nla valeur de carte "+str(n)+" doit lever une exception"):
                exo.Carte(1, n)

        for n in range (14, 100):
            self.assertRaises(AssertionError, exo.Carte, 1, n)


    def test_getCard_hors_limite(self):
        """ getCard ne fonctionne pas au dessus de 51 """
        paquet = exo.PaquetDeCarte()
        paquet.remplir()
        for i in range(52, 100):
            self.assertRaises(AssertionError, paquet.getCarteAt, i)


        

if __name__ == '__main__':
    unittest.main()


