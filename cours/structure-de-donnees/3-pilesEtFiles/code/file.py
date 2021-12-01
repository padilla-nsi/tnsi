from doctest import testmod
from maillon import Maillon


class File:
    def __init__(self):
        """
        Exemples et tests:
        >>> f = File()
        >>> print(f.tete)
        None
        >>> print(f.queue)
        None
        """
        self.tete  = None
        self.queue = None


    def est_vide(self):
        """
        Est ce que la file est vide?

        Returns:
            bool: True ssi la file est vide
        
        Exemples et tests:
        >>> f = File()
        >>> print(f.est_vide())
        True
        >>> f.tete = Maillon(1, None)
        >>> print(f.est_vide())
        False
        """
        return self.tete is None
    

    def enfiler(self, valeur):
        """
        Ajoute la valeur à la fin de la file

        Args:
            valeur (T): valeur à ajouter
        
        Exemples et tests:
        >>> f = File()
        >>> f.enfiler(1)
        >>> print(f.tete.valeur)
        1
        >>> print(f.queue.valeur)
        1
        >>> f.enfiler(2)
        >>> f.enfiler(3)
        >>> print(f.tete.valeur)
        1
        >>> print(f.queue.valeur)
        3
        """
        nouveau = Maillon(valeur, None)

        if self.est_vide():
            self.tete = nouveau
        else:
            self.queue.suivant = nouveau
        
        self.queue = nouveau


    def defiler(self):
        """
        Supprime et renvoie le premier élément de la file

        Raises:
            IndexError: si la file est vide

        Returns:
            T: valeur du premier élément de la file
        
        Exemples et tests:
        >>> f = File()
        >>> f.enfiler(1)
        >>> f.enfiler(2)
        >>> f.enfiler(3)
        >>> print( f.defiler() )
        1
        >>> assert f.queue.valeur == 3
        >>> print( f.defiler() )
        2
        >>> assert f.queue.valeur == 3
        >>> print( f.defiler() )
        3
        >>> assert f.tete  == None
        >>> assert f.queue == None
        >>> f.defiler()
        Traceback (most recent call last):
        IndexError: defiler sur une file vide
        """
        if self.est_vide():
            raise IndexError("defiler sur une file vide")
        
        valeur = self.tete.valeur
        self.tete = self.tete.suivant

        if self.tete is None:
            self.queue = None

        return valeur


    

if __name__=='__main__':
    testmod(verbose=True)