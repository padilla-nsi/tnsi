def cree():
    """
    Crée et renvoie un ensemble de dates vide.
    Une date est un entier de 1..365

    Returns:
        obj: ensemble de dates
    """
    return [False] * 366


def contient(s,x):
    """
    Renvoie `True` si et seulement si
    l'ensemble `s` contient la date `x`.

    Args:
        s (obj): ensemble de date
        x (int): date (nombre entier 1..365)

    Returns:
        (bool): True si x in s
                False sinon
    """
    return s[x]


def ajoute(s,x):
    """
    Ajoute la date `x` à l'ensemble `s`.

    Args:
        s (obj): ensemble de dates
        x (int): date (1..365)
    """
    s[x] = True