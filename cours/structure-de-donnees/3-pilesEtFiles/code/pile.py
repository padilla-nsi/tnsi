from doctest import testmod

from maillon import Maillon


class Pile:
    """
    Encapsulation des piles à l'aide des Maillons de listes chaînées.
    """
    def __init__(self):
        """
        Constructeur de Pile.

        Exemple et tests:
        >>> p = Pile()
        >>> print(p.contenu)
        None
        """
        self.contenu = None

    def est_vide(self) -> bool:
        """
        Est ce que la pile est vide ?

        Returns:
            bool: True si et seulement si la pile est vide

        Exemple et test:
        >>> p = Pile()
        >>> print(p.est_vide())
        True
        >>> p.contenu = Maillon(1, None)
        >>> print(p.est_vide())
        False
        """
        return self.contenu is None


    def empiler(self, valeur):
        """
        Empile valeur dans la pile courante.

        Args:
            valeur (T): valeur à empiler

        Exemple et tests:
        >>> p = Pile()
        >>> p.empiler(1)
        >>> assert not p.est_vide()
        >>> print(p.contenu.valeur)
        1
        >>> p.empiler(2)
        >>> print(p.contenu.valeur)
        2
        """
        tete_courante = self.contenu
        tete_nouvelle = Maillon(valeur, tete_courante)
        self.contenu = tete_nouvelle

        # version courte ;)
        # self.contenu = Maillon(valeur, self.contenu)

    def depiler(self):
        """
        Dépile la valeur de tête de la pile.

        Raises:
            IndexError: si la pile est vide

        Returns:
            T: valeur de tête de la pile

        Exemple et tests:
        >>> p = Pile()
        >>> p.empiler(1)
        >>> p.empiler(2)
        >>> v = p.depiler()
        >>> print(v)
        2
        >>> v = p.depiler()
        >>> print(v)
        1
        >>> v = p.depiler()
        Traceback (most recent call last):
        IndexError: depiler sur une pile vide
        """
        if self.est_vide():
            raise IndexError("depiler sur une pile vide")
        
        tete = self.contenu
        valeur_tete = tete.valeur
        maillon_suivant = tete.suivant
        self.contenu = maillon_suivant
        
        return valeur_tete


if __name__=='__main__':
    testmod(verbose=True)