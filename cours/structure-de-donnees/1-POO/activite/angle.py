# version avec tests unitaires
# de toutes les méthodes
from doctest import testmod


class Angle:
    """Angles compris entre 0 et 360°
    """

    def __init__(self, mesure):
        """Angle de mesure entière comprise entre 0 et 360.

        Args:
            mesure (int): mesure de l'angle

        Exemple:
        >>> a = Angle(90)
        >>> a.angle
        90
        >>> a = Angle(365)
        >>> a.angle
        5
        """
        mesure = Angle._ajuste(mesure)
        self.angle = mesure
    

    def _ajuste(angle):
        """Méthode de classe auxiliaire (hors interface)
        utilisée dans le constructeur __init__ pour 
        vérifier, quoi qu'il arrive la contrainte d'un 
        angle compris entre 0 et 360.

        Renvoie la valeur angle restreinte à 
        l'intervalle [0 ; 360[.

        Args:
            angle (int): mesure d'un angle

        Returns:
            int: valeur ajustée de l'angle

        >>> Angle._ajuste(360)
        0
        >>> Angle._ajuste(365)
        5
        >>> Angle._ajuste(90)
        90
        """
        return angle % 360


    def __str__(self):
        """Affiche un angle sous la forme
        '90 degrés'

        Returns:
            str: 
        
        Exemples:
        >>> print(Angle(90))
        90 degrés
        >>> print(Angle(390))
        30 degrés
        """
        return str(self.angle) + " degrés"


    def ajoute(self, obj):
        """Ajoute l'angle actuel avec un autre antre obj

        Args:
            obj (Angle): angle à ajouter

        Returns:
            Angle: Angle de mesure égale à la somme des deux angles

        Exemples:
        >>> a1 = Angle(90)
        >>> a2 = Angle(350)
        >>> print( a1.ajoute(a2) )
        80 degrés
        """
        mesure = self.angle + obj.angle
        return Angle(mesure)


    def _radian(mesure):
        """Methode de classe auxiliaire utilisée
        dans cos et sin.
        Convertit la mesure en degré en radian

        Args:
            mesure (int): valeur en degré

        Returns:
            float: valeur en radian

        Exemple:
        >>> round( Angle._radian(90) ,5)
        1.5708
        """
        from math import pi
        return mesure * pi / 180


    def cos(self):
        """Cosinus de l'angle.

        Returns:
            float: cosinus de la mesure de l'angle

        Exemple :
        >>> round( Angle(45).cos() ,5)
        0.70711
        """
        from math import cos
        return cos( Angle._radian(self.angle) )


    def sin(self):
        """Sinus de l'angle

        Returns:
            float: sinus de la mesure de l'angle

        Exemple:
        >>> round ( Angle(45).sin() ,5 )
        0.70711
        """
        from math import sin
        return sin( Angle._radian (self.angle) )


testmod()