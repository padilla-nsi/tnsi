from doctest import testmod


class Intervalle:
    def __init__(self, debut, fin):
        """Intervalle d'extrémité [a ; b]

        Args:
            debut (int): borne inf de l'intervalle
            fin (int): borne sup de l'intervalle
        
        Exemples:
        >>> inter = Intervalle(5,12)
        >>> inter.a
        5
        >>> inter.b
        12
        """
        self.a = debut
        self.b = fin


    def est_vide(self):
        """Est ce que l'intervalle est vide?
        Est considéré vide un intervalle 
        [a,b] dont b ≤ a.

        Returns:
            bool: True si intervalle vide

        Exemple:
        >>> inter1 = Intervalle(5,12)
        >>> inter1.est_vide()
        False
        >>> inter2 = Intervalle(5, 3)
        >>> inter2.est_vide()
        True
        """
        return self.b < self.a


    def __len__(self):
        """Longueur d'un intervalle.

        Returns:
            int: longueur de l'intervalle [a,b]

        Exemple:
        >>> len(Intervalle(5,12))
        7
        >>> len(Intervalle(5,3))
        0
        """
        if self.est_vide() :
            return 0
        return self.b - self.a 


    def __contains__(self, x):
        """Est ce que la valeur x appartient
        à l'intervalle [a,b]?

        Args:
            x (float/int): nombre

        Returns:
            bool: True ssi x in [a,b]

        Exemples:
        >>> 6 in Intervalle(5,12)
        True
        >>> 5 in Intervalle(5,12)
        True
        >>> 4.9 in Intervalle(5,12)
        False
        """
        if self.est_vide():
            return False
        if x > self.b or  x < self.a:
            return False
        return True


    def __eq__(self, inter):
        """Est ce que l'intervalle est 
        égale à l'intervalle inter

        Args:
            inter2 (Intervalle): Intervalle à comparer

        Returns:
            bool: True ssi les deux intervalles ont les
            mêmes bornes

        Exemple:
        >>> Intervalle(5,12) == Intervalle(5,7)
        False
        >>> Intervalle(5,12) == Intervalle(5,12)
        True
        >>> Intervalle(5,3) == Intervalle(7,2)
        True
        """
        if self.est_vide() and inter.est_vide():
            return True
        
        if self.a == inter.a and self.b == inter.b:
            return True

        return False 


    def __le__(self, inter):
        """Est ce que l'intervalle est inclu
        dans l'intervalle inter?

        Args:
            inter (Intervalle): Intervalle [a,b]

        Returns:
            bool: True ssi l'intervalle est inclus dans inter
        
        Exemples:
        >>> Intervalle(4,10) <= Intervalle(5,12)
        False
        >>> Intervalle(5,12) <= Intervalle(4,10)
        False
        >>> Intervalle(6,10) <= Intervalle(5,12)
        True
        """
        if self.est_vide():
            return True

        return self.a >= inter.a and self.b <= inter.b


    def intersection(self, inter):
        """Intersection avec l'intervalle inter.

        Args:
            inter (Intervalle)

        Returns:
            Intervalle: égal à l'intersection de self 
            avec inter.
        
        Exemples:
        >>> Intervalle(4,6).intersection(Intervalle(5,10)) == Intervalle(5,6)
        True
        """
        if self.est_vide():
            return self
        
        if inter.est_vide():
            return inter

        tmp_a = max(self.a, inter.a)
        tmp_b = min(self.b, inter.b)

        return Intervalle( tmp_a, tmp_b )

    
    def reunion(self, inter):
        """Réunion avec l'intervalle inter. Si la réunion
        n'est pas un intervalle, renvoie le plus petit
        des deux intervalles.

        Args:
            inter (Intervalle)

        Returns:
            Intervalle: réunion avec inter

        Exemples :
        >>> Intervalle(4,6).reunion(Intervalle(9,10)) == Intervalle(9,10)
        True
        >>> Intervalle(4,6).reunion(Intervalle(5,8)) == Intervalle(4,8)
        True
        """
        if self.est_vide():
            return inter
        if inter.est_vide():
            return self
        
        intersec = self.intersection(inter)
        if intersec.est_vide():
            if len(self) <= len(inter):
                return self
            else:
                return inter
        
        tmp_a = min(self.a, inter.a)
        tmp_b = max(self.b, inter.b)

        return Intervalle(tmp_a, tmp_b)


testmod()
