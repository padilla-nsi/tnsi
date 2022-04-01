from doctest import testmod


def occurrence_lettres(phrase: str) -> dict:
    """Occurrence de chaque lettre qui compose la phrase.

    Args:
        phrase (str): phrase à analyser

    Returns:
        dict: dictionnaire dont 
            * les clés sont les lettres et 
            * les valeurs leurs occurrences
    
    Tests et Exemples:
    >>> occurrence_lettres('Hello world !')
    {'H': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 2, 'w': 1, 'r': 1, 'd': 1, '!': 1}
    """
    # initialisation du dictionnaire à renvoyer
    occurrences = {}

    # parcours de la phrase, lettre par lettre
    for lettre in phrase:
        if lettre in occurrences:
            # la lettre est déjà apparue donc
            # ajoute 1 à l'occurrence de la lettre
            occurrences[lettre] += 1
        else:
            # première apparition de la lettre donc
            # initialise son occurrence à 1
            occurrences[lettre] = 1

    return occurrences


assert occurrence_lettres('Hello world !') == {'H': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 2, 'w': 1, 'r': 1, 'd': 1, '!': 1}
testmod()