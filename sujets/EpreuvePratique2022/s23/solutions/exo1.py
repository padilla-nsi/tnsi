"""
Author: Pascal Padilla
Source: correction de l'exercice 1 du sujet 23 des épreuves pratiques NSI 2022
"""


from doctest import testmod


def max_dico(dico: dict) -> tuple[str, int]:
    """_summary_

    Args:
        dico (dict): _description_

    Returns:
        tuple[str, int]: _description_

    Tests et exemples:
    >>> max_dico({'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50})
    ('Ada', 201)
    >>> max_dico({'Alan': 222, 'Ada': 201, 'Eve': 220, 'Tim': 50})
    ('Alan', 222)
    """
    # initialisation de valeur maximale et clé associée
    # avec des valeurs impossible
    # (un nombre négatif et un None)
    val_max = -1
    cle_max = None

    # parcours de tout le dictionnaire par couple clé/valeur
    for cle, valeur in dico.items():
        # une valeur maximale est trouvée
        if valeur > val_max:
            # mise à jour de la clé max et de sa valeur max associée
            val_max = valeur
            cle_max = cle

    # renvoie du couple clé_max et valeur_max
    return (cle_max, val_max)


# tests avec des affichages
print(max_dico({'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50}))
print(max_dico({'Alan': 222, 'Ada': 201, 'Eve': 220, 'Tim': 50}))


# tests avec des assertions
assert max_dico({'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50}) == ('Ada', 201)
assert max_dico({'Alan': 222, 'Ada': 201, 'Eve': 220, 'Tim': 50}) == ('Alan', 222)


# tests avec doctest
testmod()

''.join([chr(i) for i in range(10)])