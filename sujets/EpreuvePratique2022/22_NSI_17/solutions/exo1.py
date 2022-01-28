from doctest import testmod


def nombre_de_mots(phrase: str) -> int:
    """Nombre de mots d'une phrase

    Args:
        phrase (str): phrase avec des mots : 
        * séparés par un seul caractère espace et
        * se fini par :
            un point collé au dernier mot
            OU par un point d'exclamation/interrogation 
               séparé du dernier mot un espace.

    Returns:
        int: nombre de mots de la phrase

    Tests et Exemples:
    >>> nombre_de_mots('Le point d exclamation est separe !')
    6
    >>> nombre_de_mots('Il y a un seul espace entre les mots !')
    9
    >>> nombre_de_mots('Le point final est colle au dernier mot.')
    8
    >>> nombre_de_mots('Gilbouze macarbi acra cor ed filbuzine ?')
    6
    """
    # on va compter le nombre de caractères espace
    n_espace = 0
    n = len(phrase)
    for i in range(n):
        lettre_courante = phrase[i]
        if lettre_courante == ' ':
            n_espace = n_espace + 1
    
    # si le dernier caractère est un point, il manque un caractère 
    # espace pour compter correctement le nombre de mots
    # sinon le nombre de mots est égal au nombre d'espaces
    if lettre_courante == '.':
        n_mot = n_espace + 1
    else:
        n_mot = n_espace

    return n_mot


if __name__ == '__main__':
    testmod()
