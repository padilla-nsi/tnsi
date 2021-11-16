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
        """
        self.valeur = valeur
        self.suivant = suivant
