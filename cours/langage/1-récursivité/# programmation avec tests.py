# programmation avec tests
import doctest

def syracuse(u_n):
    """
    Affiche les termes de la suite de Syracuse.
    
    exemple :
    >>> syracuse(5)
    5
    16
    8
    4
    2
    1
    """
    print(u_n)
    if u_n > 1:
        if u_n % 2 == 0:
            syracuse(u_n//2)
        else:
            syracuse(3*u_n+1)

# programmation défensive
doctest.testmod()