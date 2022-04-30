import unittest
import s37.solutions.exo2 as exo
from random import randint, choice, random


def depouille(urne):
    # initialisation: un dictionnaire vide
    resultat = {}
    # parcours de chaque élément (appelé `bulletin`) de l'urne
    for bulletin in urne:
        # cas où la clé `bulletin` existe déjà dans le dictionnaire `resultat`
        if bulletin in resultat:
            resultat[bulletin] = resultat[bulletin] + 1
        # cas de la première apparition de la clé `bulletin`
        # initialisation de la clé avec un premier vote
        else:
            resultat[bulletin] = 1

    # fin BOUCLE: toute l'urne est parcourue
    # resultat contient l'ensemble de tous les résultats
    return resultat

def vainqueur(election):
    # BOUCLE:
    # -> invariant: nmax est le nb maxi de bulletins d'un (ou plusieurs) candidats
    #               du tableau `election` parcouru jusqu'à présent

    # initialisation: pas de vainqueur et nmax vaut 0
    vainqueur = ''
    nmax = 0
    # parcours du dictionnaire dépouillé: clé = candidant et valeur = effectifs
    for candidat in election:
        # cas d'un candidat a plus de bulletins que le meilleur jusqu'à présent
        # `candidat` est la clé du dictionnaire et sa valeur est le nb de bulletins
        if election[candidat] > nmax :
            nmax = election[candidat]
            vainqueur = candidat
    liste_finale = [nom for nom in election if election[nom] == nmax]
    return liste_finale



class validation(unittest.TestCase):
    def test_exemple_depouille(self):
        urne = ['A', 'A', 'A','B', 'C', 'B', 'C','B', 'C', 'B']

        txt = "\nErreur tests enonce: fonction `depouille` incorrecte"
        self.assertEqual(depouille(urne), exo.depouille(urne), msg=txt)

    def test_exemple_vainqueur(self):
        urne = ['A', 'A', 'A','B', 'C', 'B', 'C','B', 'C', 'B']
        election = depouille(urne)

        txt = "\nErreur tests enonces: fonction `vainqueur` incorrecte"
        self.assertEqual(vainqueur(election), exo.vainqueur(election), msg=txt)
    
    def test_random_depouille(self):
        for _ in range(20):
            nb_candidats = randint(1, 10)
            candidats = [chr(randint(65, 90)) for _ in range(nb_candidats)]
            nb_bulletins = randint(1, 100)
            urne = [choice(candidats) for _ in range(nb_bulletins)]

            txt = "\nErreur tests aleatoires: fonction `depouille` incorrecte"

            self.assertEqual(depouille(urne), exo.depouille(urne), msg=txt)
    
    def test_random_vainqueur(self):
        for _ in range(20):
            nb_candidats = randint(1, 10)
            candidats = [chr(randint(65, 90)) for _ in range(nb_candidats)]
            nb_bulletins = randint(1, 100)
            urne = [choice(candidats) for _ in range(nb_bulletins)]
            election = depouille(urne)

            txt = "\nErreur tests aleatoires: fonction `vainqueur` incorrecte"
            self.assertEqual(vainqueur(election), exo.vainqueur(election), msg=txt)

        


if __name__ == '__main__':
    unittest.main()
