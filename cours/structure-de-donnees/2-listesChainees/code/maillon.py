from doctest import testmod

"""
classe Maillon du cours liste chaînées TNSI
"""

class Maillon:
    """
    Une classe pour représenter le maillon d'une liste

    Attributs
    ---------
    valeur : type
        valeur contenue dans le maillon
    suivant : maillon
        maillon suivant ou None si pas de maillon
    """

    def __init__(self, valeur, suivant):
        """Constructeur de classe

        Args:
            valeur (type): valeur stockée dans le maillon
            suivant (maillon): maillon suivant ou None

        Exemples et tests:
        >>> l3 = Maillon(3, None)
        >>> assert (l3.valeur == 3)
        >>> assert (l3.suivant == None)
        
        >>> l2 = Maillon(2, l3)
        >>> assert (l2.valeur == 2)
        >>> assert (l2.suivant.valeur == 3)

        >>> l1 = Maillon(1, l2)
        >>> assert (l1.valeur == 1)
        >>> assert (l1.suivant.valeur == 2)
        >>> assert (l1.suivant.suivant.valeur == 3)
        >>> assert (l1.suivant.suivant.suivant == None)
        
        >>> l1.suivant.suivant.suivant.valeur
        Traceback (most recent call last):
        AttributeError: 'NoneType' object has no attribute 'valeur'
        """
        self.valeur = valeur
        self.suivant = suivant


if __name__ == '__main__':
    testmod(verbose=True)