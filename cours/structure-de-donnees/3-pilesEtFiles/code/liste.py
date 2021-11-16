"""
classe Liste du cours liste chaînées TNSI
"""

from maillon import Maillon
from operations_base import longueur, nieme_element, renverser, concatener


class Liste:
    """ Une liste chaînées """

    def __init__(self):
        """
        Constructeur d'une liste vide.

        Exemples :
        >>> lst = Liste()
        >>> print(lst.tete)
        None
        """
        self.tete = None


    def est_vide(self) -> bool:
        """ Est ce que la liste est vide ?

        Returns:
            bool: True si et seulement si la liste est vide

        Exemples :
        >>> lst = Liste()
        >>> print(lst.est_vide())
        True

        >>> lst = Liste()
        >>> lst.tete = Maillon(1, None)
        >>> print(lst.est_vide())
        False
        """
        return self.tete is None


    def ajoute(self, valeur):
        """
        Ajouter un nouveau maillon en tête de liste

        Args:
            valeur (type): valeur du nouveau maillon

        Exemples :
        >>> lst = Liste()
        >>> lst.ajoute(1)
        >>> print(lst.tete.valeur)
        1
        >>> lst.ajoute(2)
        >>> print(lst.tete.valeur)
        2
        >>> print(lst.tete.suivant.valeur)
        1
        """
        self.tete = Maillon(valeur, self.tete)


    def longueur(self) -> int:
        """
        Longueur d'une liste chaînée

        Returns:
            int: longueur de la liste

        Exemples:
        >>> lst = Liste()
        >>> assert lst.longueur() == 0
        >>> lst.ajoute(4)
        >>> assert lst.longueur() == 1
        >>> lst.ajoute(2)
        >>> assert lst.longueur() == 2
        >>> lst.ajoute(1)
        >>> assert lst.longueur() == 3
        """
        return longueur(self.tete)


    def __len__(self):
        """
        Permet d'utiliser :
            - la fonction len avec les Liste
            - une instance de Liste comme une expression booléenne :
                True  si et seulement si l'instance est de longueur > 0
                False si et seulement si l'instance est de longueur nulle

        Exemples:
        >>> lst = Liste()
        >>> assert len(lst) == 0
        >>> if lst: print("expression booléenne évaluée à False")
        >>> lst.ajoute(4)
        >>> assert len(lst) == 1
        >>> if lst: print("expression booléenne évaluée à True")
        expression booléenne évaluée à True
        """
        return longueur(self.tete)


    def __getitem__(self, index):
        """ Permet d'utiliser la syntaxe des listes

        Exemples:
        >>> lst = Liste()
        >>> lst.ajoute(4)
        >>> lst.ajoute(2)
        >>> lst.ajoute(1)
        >>> assert lst[0] == 1
        >>> assert lst[1] == 2
        >>> assert lst[2] == 4
        """
        return nieme_element(index, self.tete)


    def __add__(self, liste):
        """
        Permet d'utiliser l'opérateur + entre instances de Liste

        Exemples:
        >>> lst_1 = Liste()
        >>> lst_1.ajoute(1)
        >>> lst_2 = Liste()
        >>> lst_2.ajoute(3)
        >>> lst_2.ajoute(2)
        >>> lst_3 = lst_1 + lst_2
        >>> assert lst_3[0] == 1     # lst_3 concaténée !
        >>> assert lst_3[1] == 2
        >>> assert lst_3[2] == 3
        """
        somme = Liste()
        somme.tete = concatener(self.tete, liste.tete)
        return somme


    def reverse(self):
        """
        Renverse la liste en place

        Exemples:
        >>> lst = Liste()
        >>> lst.ajoute(3)
        >>> lst.ajoute(2)
        >>> lst.ajoute(1)
        >>> lst.reverse()
        >>> assert lst[0] == 3
        >>> assert lst[1] == 2
        >>> assert lst[2] == 1
        """
        self.tete = renverser(self.tete)


if __name__ == '__main__':
    from doctest import testmod
    testmod(verbose=True)
