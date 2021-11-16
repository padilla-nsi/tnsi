from doctest import testmod


class Fraction:

    def __init__(self, num, denom):
        """Nombre rationnel définit par la fraction
        num/denom avec denom > 0

        Args:
            num (int): numérateur
            denom (int): dénominateur > 0
        
        Exemples:
        >>> nb = Fraction(1,2)
        >>> print(nb.num)
        1
        >>> print(nb.denom)
        2
        """
        if denom <= 0:
            raise ValueError("le dénominateur doit être strictement positif")
        self.num = num
        self.denom = denom

    
    def __str__(self):
        """Affichage de la classe Fraction

        Exemple :
        >>> print(Fraction(1,2))
        1 / 2
        >>> print(Fraction(5,1))
        5
        """
        if self.denom == 1:
            return str(self.num)

        texte = str(self.num) + " / " + str(self.denom)
        return texte


    def __eq__ (self, frac):
        """Est ce que le nombre rationnel est égal à frac?

        Args:
            frac (Fraction): nombre rationnel à comparer
        
        Exemples:
        >>> Fraction(1,2) == Fraction(1,2)
        True
        >>> Fraction(1,2) == Fraction (2,1)
        False
        >>> Fraction(1,2) == Fraction(5,10)
        True
        """
        if self.denom == frac.denom:
            return self.num == frac.num
        
        # méthode du produit en croix pour tester égalité
        # l'avantage est de ne comparer que des nombres entiers
        # et pas des float
        return self.num * frac.denom == self.denom * frac.num


    def __lt__(self, frac):
        """Est ce que le nombre rationnel est inférieur à frac?

        Args:
            frac (Fraction): nombre rationnel à comparer

        Returns:
            bool: True si inférieur à frac

        Exemple:
        >>> Fraction(5,7) < Fraction(6,7)
        True
        >>> Fraction(5,7) < Fraction(4,7)
        False
        >>> Fraction(5,7) < Fraction(10,14)
        False
        >>> Fraction(3,4) < Fraction(1,2)
        False
        """
        if self.denom == frac.denom:
            return self.num < frac.num
        
        # méthode de comparaison par le produit en croix
        # manipulation d'entiers (moins de pb que les float)
        return self.num * frac.denom < self.denom * frac.num


    def __mul__(self, frac):
        """résultat du produit par frac

        Args:
            frac (Fraction): nb rationnel avec lequel on multiplie

        Returns:
            Fraction: nb rationnel produit des deux fractions

        Exemple:
        >>> Fraction(1,3) * Fraction(3,5) == Fraction(1,5)
        True
        """
        num = self.num * frac.num
        denom = self.denom * frac.denom
        return Fraction(num, denom)
    

    def __add__(self, frac):
        """
        >>> Fraction(1,2) + Fraction(3,5) == Fraction(11,10)
        True
        >>> Fraction(1,2) + Fraction(50,50) == Fraction(3,2)
        True
        """
        denom = self.denom * frac.denom
        num = self.num * frac.denom + frac.num * self.denom
        return Fraction(num, denom)


testmod()