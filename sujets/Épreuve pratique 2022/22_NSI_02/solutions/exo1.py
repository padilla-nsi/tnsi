from doctest import testmod


def moyenne(tab: list) -> float:
    """ Calcul une moyenne pondérée.

    Args:
        tab (list): tableau de couples de notes 
        de la forme (note: int, coefficient: int)

    Returns:
        float: moyenne pondérée
    
    Tests et Exemples:
    >>> moyenne([(15, 2), (9, 1), (12, 3)])
    12.5
    >>> moyenne([(10, 2)])
    10.0
    """
    somme = 0
    coef_total = 0

    n_notes = len(tab)
    for i in range(n_notes):
        couple = tab[i]
        note = couple[0]
        coefficient = couple[1]

        somme = somme + note*coefficient
        coef_total = coef_total + coefficient
    
    return somme / coef_total


assert moyenne([(15,2),(9,1),(12,3)]) == 12.5
assert moyenne([(10, 2)]) == 10

testmod()