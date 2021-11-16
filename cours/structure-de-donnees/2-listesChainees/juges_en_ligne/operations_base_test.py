""" tests unitaires de la fonction concatener """
import unittest
from random import randint
import operations_base as exo


class Maillon:
    """un maillon d'une liste chaînée"""

    def __init__(self, valeur, suivant):
        self.valeur = valeur
        self.suivant = suivant


def longueur(lst):
    """ longueur d'une liste chaînée """
    if lst is None:
        return 0
    return 1 + longueur(lst.suivant)


def nieme_element(index, lst):
    """ nieme element d'une liste chaînée
        version itérative
    """
    if index >= longueur(lst):
        raise IndexError('index out of range')

    maillon_actuel = lst
    for _ in range(index):
        maillon_actuel = maillon_actuel.suivant
    return maillon_actuel.valeur


def concatener(start_lst, end_lst):
    """ concaténer deux liste de façon récursive """
    if longueur(start_lst) == 0:
        return end_lst
    premier_element = start_lst
    reste = concatener(start_lst.suivant, end_lst)
    premier_element.suivant = reste
    return premier_element


def renverser(lst):
    """ renvoyer une nouvelle liste chainée renversée """
    n = longueur(lst)
    new_lst = None
    for i in range(n):
        valeur = nieme_element(i, lst)
        new_lst = Maillon(valeur, new_lst)
    return new_lst


class MaillonValidator(unittest.TestCase):
    """ tests unitaires du constructeur Maillon """

    def test_constructeur(self):
        """
            Vérifie que le constructeur pour Maillon
            est correct
        """
        text_error = '\nErreur:\nconstructeur Maillon() invalide'
        try:
            m_3 = exo.Maillon(3, None)
            m_2 = exo.Maillon(2, m_3)
            m_1 = exo.Maillon(1, m_2)
        except:
            raise NameError(text_error)

        self.assertIsInstance(m_1, exo.Maillon, msg=text_error)
        self.assertEqual(m_1.valeur, 1, msg=text_error)
        self.assertEqual(m_1.suivant, m_2, msg=text_error)

    def test_aleatoire(self):
        """ tests sur des listes chaînées aléatoires """
        for n in range(50, 100):
            valeurs = [randint(-50, 50) for _ in range(n)]
            maillons = [exo.Maillon(valeurs[0], None)]
            for i in range(1, n):
                maillons.append(exo.Maillon(valeurs[i], maillons[i-1]))

            text_error = '\nErreur:\nle test aléatoire ne fonctionne pas...'

            tete = maillons[n-1]
            for i in range(n):
                self.assertEqual(tete.valeur, valeurs[n-i-1], msg=text_error )
                tete = tete.suivant


class LongueurValidator(unittest.TestCase):
    """ tests unitaires de la fonction longueur """

    def test_exemple(self):
        """ tests des exempels de l'énoncé """
        text_error = '\nErreur:\nles exemples ne fonctionnent pas ! :('
        self.assertEqual(exo.longueur(Maillon(42, None)), 1, msg=text_error)

        m_3 = Maillon(3, None)
        m_2 = Maillon(2, m_3)
        m_1 = Maillon(1, m_2)
        self.assertEqual(exo.longueur(None), 0, msg=text_error)
        self.assertEqual(exo.longueur(m_3), 1, msg=text_error)
        self.assertEqual(exo.longueur(m_1) , 3, msg=text_error)

    def test_aleatoire(self):
        """ tests sur des listes chaînées aléatoires """
        n = randint(10, 100)
        valeurs = [randint(-50, 50) for _ in range(n)]
        maillons = [Maillon(valeurs[0], None)]
        for i in range(1, n):
            maillons.append(Maillon(valeurs[i], maillons[i-1]))

        text_error = '\nErreur:\nle test aléatoire ne fonctionne pas...'
        for i in range(n):
            self.assertEqual(exo.longueur(maillons[i]), i + 1, msg=text_error )


class NiemeElementValidator(unittest.TestCase):
    """ Tests unitaires """

    def test_exemples(self):
        """ vérifier les exemples de l'énoncé """
        text_error = "\nErreur:\nles exemples ne fonctionnent pas"
        # levée de l'exception IndexError
        def fail_function():
            exo.nieme_element(1, Maillon(42, None))

        self.assertRaises(IndexError, fail_function)

        # valeur correcte
        self.assertEqual(exo.nieme_element(1, Maillon(1, Maillon(2, Maillon(3, None)))),
                                       2, msg=text_error)

    def test_aleatoire(self):
        """ faire des tests sur une liste chaînée de taille arbitraire """
        text_error = '\nErreur:\nle test aléatoire ne fonctionne pas...'

        n = randint(10, 100)
        valeurs = [randint(-50, 50) for _ in range(n)]
        maillons = [Maillon(valeurs[0], None)]
        for i in range(1, n):
            maillons.append(Maillon(valeurs[i], maillons[i-1]))

        lst = maillons[n-1]
        for i in range(n):
            self.assertEqual(exo.nieme_element(i, lst), valeurs[n-i-1], msg=text_error)



class ConcatenerValidator(unittest.TestCase):
    """ Validation de la fonction concatener """

    def test_exemples(self):
        """ tests sur les exemples de l'énoncé """
        text_error = '\nErreur:\nles exemples ne fonctionnent pas...'

        l_1 = Maillon(1, Maillon(2, Maillon(3, None)))
        self.assertEqual(longueur(l_1), 3)

        l_2 = Maillon(4, Maillon(5, None))
        self.assertEqual(longueur(l_2), 2)

        l_3 = exo.concatener(l_1, l_2)
        self.assertEqual(longueur(l_3),
                         longueur(l_1) + longueur(l_2),
                         msg = text_error)

        n_1 = longueur(l_1)
        for i in range(n_1):
            self.assertEqual(nieme_element(i, l_1),
                             nieme_element(i, l_3),
                             msg = text_error)
        n_2 = longueur(l_2)
        for i in range(n_2):
            self.assertEqual(nieme_element(i, l_2),
                             nieme_element(i + n_1, l_3),
                             msg = text_error)

    def test_aleatoire(self):
        """ faire des tests sur une liste chaînée de taille arbitraire """
        text_error = '\nErreur:\nle test aléatoire ne fonctionne pas...'

        n_1 = randint(0, 100)
        l_1 = None
        for _ in range(n_1):
            valeur = randint(-50, 50)
            l_1 = Maillon(valeur, l_1)

        n_2 = randint(0, 100)
        l_2 = None
        for i in range(n_2):
            valeur = randint(-50, 50)
            l_2 = Maillon(valeur, l_2)

        self.assertEqual(longueur(l_1), n_1)
        self.assertEqual(longueur(l_2), n_2)

        l_3 = exo.concatener(l_1, l_2)
        self.assertEqual(longueur(l_3), n_1 + n_2, msg=text_error)

        for i in range(n_1):
            self.assertEqual(nieme_element(i, l_1),
                             nieme_element(i, l_3),
                             msg = text_error)

        for i in range(n_2):
            self.assertEqual(nieme_element(i, l_2),
                             nieme_element(i + n_1, l_3),
                             msg = text_error)


class RenverserValidator(unittest.TestCase):
    """ valider la fonction renverser """
    def test_exemple(self):
        """ tester les exemples de l'énoncé """
        text_error = '\nErreur:\nles exemples sont incorrects...'
        l_1 = Maillon(1, Maillon(2, Maillon(3, None)))
        l_2 = exo.renverser(l_1)

        for i in range(3):
            self.assertEqual(nieme_element(i, l_1),
                             nieme_element(3-i-1, l_2),
                             msg=text_error)

    def tests_aleatoires(self):
        """ tests sur une listes chainée aléatoire """
        text_error = '\nErreur:\nle test aléatoire ne fonctionne pas...'

        n_1 = randint(0, 100)
        l_1 = None
        for _ in range(n_1):
            valeur = randint(-50, 50)
            l_1 = Maillon(valeur, l_1)

        l_2 = exo.renverser(l_1)

        for i in range(n_1):
            self.assertEqual(nieme_element(i, l_1),
                             nieme_element(n_1-i-1, l_2),
                             msg=text_error)


if __name__ == '__main__':
    unittest.main()
