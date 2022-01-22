from doctest import testmod


def conv_bin(n):
    """ Convertir un entier en binaire et dénombrer les bits.

    Args:
        n (int): entier positif à convertir

    Returns:
        tuple: couple de la forme (b: list, bit: int) avec
          * b un tableau d'entier correspondant à la rep binaire de n
          * bit le nombre de bits qui constituent b
    
    Tests et Exemples:
    >>> conv_bin(9)
    ([1, 0, 0, 1], 4)
    """
    b = []
    bits = 0
    while n > 0:
        current_b = n % 2
        n = n // 2
        bits += 1
        b.append(current_b)
    b.reverse()
    return (b, bits)


assert conv_bin(9) == ([1, 0, 0, 1], 4)
testmod()