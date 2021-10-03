from doctest import testmod

class TableauIndex():
    def __init__(self, imin, imax, v):
        """Tableau d'indices quelconque.

        Args:
            imin (int): indice de début
            imax (int): indice de fin de tableau
            v (object): valeur initiale de toutes les cellules du tableau

        Exemples:
        >>> t = TableauIndex(-10, 9, 42)
        >>> t.contenu
        [42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42]
        """
        self.premier = imin
        longueur = imax - imin + 1
        self.contenu = [v] * longueur


    def __len__(self):
        """
        Exemples:
        >>> t = TableauIndex(-10, 9, 42)
        >>> len(t)
        20
        """
        return len(self.contenu)

    
    def __getitem__(self, i):
        """Exemples:
        >>> t = TableauIndex(-10, 9, 42)
        >>> t[-10]
        42
        """
        if i < self.premier or i >= self.premier + len(self):
            raise IndexError (i)

        indice = i + self.premier
        return self.contenu[indice]
    
    def __setitem__(self, i, v):
        """Exemples:
        >>> t = TableauIndex(-10, 9, 42)
        >>> t[-10] = 12
        >>> t[-10]
        12
        >>> t[-9]
        42
        """
        if i < self.premier or i >= self.premier + len(self):
            raise IndexError (i)

        indice = i - self.premier
        self.contenu[indice] = v

    def __str__(self):
        """Exemples:
        >>> t = TableauIndex(5,9,10)
        >>> print(t)
        [10, 10, 10, 10, 10]
        """
        return str(self.contenu)


testmod()