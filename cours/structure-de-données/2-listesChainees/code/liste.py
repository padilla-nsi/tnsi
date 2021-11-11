"""
classe Liste du cours liste chaînées TNSI
"""

from doctest import testmod
from maillon import Maillon

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

        longueur = 0
        tete_courante = self.tete
        while tete_courante is not None:
            longueur += 1
            tete_courante = tete_courante.suivant
        return longueur


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
        return self.longueur()


    def nieme_element(self, index):
        """nieme element d'une liste chaînée
        version itérative

        Args:
            index (int): rang du maillon dont on veut récupérer la valeur
            lst (Liste): [description]

        Raises:
            IndexError: si index n'est pas dans la liste

        Returns:
            type: valeur du maillon de rang index

        Exemples:
        >>> lst = Liste()
        >>> lst.ajoute(4)
        >>> lst.ajoute(2)
        >>> lst.ajoute(1)
        >>> assert lst.nieme_element(0) == 1
        >>> assert lst.nieme_element(1) == 2
        >>> assert lst.nieme_element(2) == 4
        """
        if index >= self.longueur():
            raise IndexError('index out of range')

        maillon_actuel = self.tete
        for _ in range(index):
            maillon_actuel = maillon_actuel.suivant
        return maillon_actuel.valeur


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
        return self.nieme_element(index)



    def concatener(self, liste):
        """
        Renvoyer la concaténation de self avec liste

        Exemple:
        >>> lst1 = Liste()
        >>> lst1.ajoute(1)
        >>> lst2 = Liste()
        >>> lst2.ajoute(3)
        >>> lst2.ajoute(2)
        >>> lst3 = lst1.concatener(lst2)
        >>> assert lst3[0] == 1
        >>> assert lst3[1] == 2
        >>> assert lst3[2] == 3
        """
        concatenation = Liste()

        n_2 = len(liste)
        for i in range(n_2):
            concatenation.ajoute(liste[n_2 - i - 1])

        n_1 = len(self)
        for i in range(n_1):
            concatenation.ajoute(self[n_1 - i - 1])

        return concatenation

    def __add__(self, liste):
        """ Permet d'utiliser l'opérateur + entre instances de Liste"""

        return self.concatener(liste)


    def renverser(self):
        """
        Renvoyer une nouvelle liste chainée renversée

        Exemples:
        >>> lst = Liste()
        >>> lst.ajoute(3)
        >>> lst.ajoute(2)
        >>> lst.ajoute(1)
        >>> lst_r = lst.renverser()
        >>> assert lst_r[0] == 3    # lst_r inversée
        >>> assert lst_r[1] == 2
        >>> assert lst_r[2] == 1
        >>> assert lst[0] == 1      # lst inchangée
        >>> assert lst[1] == 2
        >>> assert lst[2] == 3
        """
        renverse = Liste()
        taille = self.longueur()
        for i in range(taille):
            renverse.ajoute(self[i])

        return renverse


testmod()