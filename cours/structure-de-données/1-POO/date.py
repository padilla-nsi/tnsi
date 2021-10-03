# version avec des test unitaire

from doctest import testmod


class Date:

    mois_fr = [ None, 
            'janvier', 'février', 'mars',
            'avril', 'mai', 'juin',
            'juillet', 'août', 'septembre',
            'octobre', 'novembre', 'décembre']

    def __init__(self, j, m, a):
        self.jour  = j
        self.mois  = m
        self.annee = a

    def __str__(self):
        """Affiche une date en français.
        Par exemple '8 mai 1945'.

        Returns:
            str
        
        Exemple:
        >>> print(Date(8,5,1945))
        8 mai 1945
        >>> print(Date(5,6,1977))
        5 juin 1977
        """
        date  = str(self.jour) + " "
        date += Date.mois_fr[self.mois] + " "
        date += str(self.annee)
        return date

    def __lt__(self, date):
        """Est ce que la date est antérieure à date?

        Args:
            date (Date)

        Returns:
            bool: True ssi est strictement antérieure à date
        
        Exemples:
        >>> Date(5,6,1978) < Date(4,6,1978)
        False
        >>> Date(5,6,1978) < Date(7,6,1978)
        True
        >>> Date(1,1,2006) < Date(1,1,2006)
        False
        >>> Date(1,1,2004) < Date(1,1,2006)
        True
        >>> Date(1,4,2003) < Date(1,5,2003)
        True
        """
        if self.annee < date.annee:
            return True
        if self.annee > date.annee:
            return False
        if self.mois < date.mois:
            return True
        if self.mois > date.mois:
            return False
        if self.jour < date.jour:
            return True
        return False    


testmod()