"""
Author: Pascal Padilla
Source: correction de l'exercice 1 du sujet 17 des épreuves pratiques NSI 2022

Remarque: l'énoncé demande de remarque que :
si la phrase se termine par un '!' ou un '?'
    alors il y a autant de mots que d'espaces
si la phrase se termine par un '.'
    alors il y a un mot de plus que le nombre d'espaces
"""


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
    # puis ensuite (grâce à la remarque) on déterminera
    # le nombre de mots (2 cas possibles)

    # BOUCLE
    # invariants:
    #   * n_espace contient le nombre d'espace de la phrase
    #       entre les caractères 0 .. i-1

    # initialisation:
    #   * n_espace ← 0
    #   * i ← -1
    n_espace = 0

    # condition d'arrêt (toute la phrase est parcourue):
    #   * i == len(phrase)
    for i in range(len(phrase)):
        # lecture de la lettre courante de la phrase
        lettre_courante = phrase[i]

        # mise à jour de n_espace si la lettre courante
        # est un espace
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


# Tests de l'énoncé avec doctest:
testmod()
