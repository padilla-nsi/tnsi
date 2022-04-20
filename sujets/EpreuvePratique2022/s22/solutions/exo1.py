"""
Author: Pascal Padilla
Source: correction de l'exercice 1 du sujet 22 des épreuves pratiques NSI 2022

Remarque : je propose 2 versions supplémentaires
"""


from doctest import testmod


def renverse(chaine: str) -> str:
    """
    renvoie une chaîne de caractères en inversant `chaine`

    Args:
        chaine (str): chaîne de caractères non vide

    Returns:
        str: chaine écrite inversée

    Tests et exemple:
    >>> renverse("informatique")
    'euqitamrofni'
    """
    # initialisation de la sortie avec une chaine vide
    chaine_inverse = ""

    # parcours de chaque lettre de chaine du début vers la fin
    for i in range(len(chaine)):
        lettre = chaine[i]

        # ajout de la lettre courante au début de la chaine inversée
        chaine_inverse = lettre + chaine_inverse

    return chaine_inverse


def renverse_pythonnesque_1(chaine):
    """
    renvoie une chaîne de caractères en inversant `chaine`

    Args:
        chaine (str): chaîne de caractères non vide

    Returns:
        str: chaine écrite inversée

    Tests et exemple:
    >>> renverse_pythonnesque_1("informatique")
    'euqitamrofni'
    """
    return chaine[::-1] # hors programme


def renverse_pythonnesque_2(chaine):
    """
    renvoie une chaîne de caractères en inversant `chaine`

    Args:
        chaine (str): chaîne de caractères non vide

    Returns:
        str: chaine écrite inversée

    Tests et exemple:
    >>> renverse_pythonnesque_2("informatique")
    'euqitamrofni'
    """
    chaine_inverse = ""
    for lettre in chaine:
        chaine_inverse = lettre + chaine_inverse

    return chaine_inverse


# tests avec des affichages
print(renverse("informatique"))


# tests avec des assertions
assert renverse("informatique") == 'euqitamrofni'


# tests avec doctest
testmod()
