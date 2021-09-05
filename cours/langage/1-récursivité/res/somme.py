
def somme(n):
    """
    Calcule la somme des n premiers entiers.
    
    params:
    * n (int) : dernier entier à ajouter
    
    exemples:
    >>> somme (0) 
    0
    >>> somme (5)
    15
    >>> somme(10)
    55
    """
    if n==0:
        return 0
    else:
        return n + somme(n-1)

print("exemple pour n=10 :", somme(10) )