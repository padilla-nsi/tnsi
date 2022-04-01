"""
Author: Pascal Padilla
Source: correction de l'exercice 2 du sujet 11 des épreuves pratiques NSI 2022
"""

from doctest import testmod


# définition de toutes les lettres acceptables
# dans une chaîne de caractère
# (qui se parcourt avec la même syntaxe que les tableaux)
#
# écrire une variable en majuscule pour
# signifier que c'est une constante
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def position_alphabet(lettre):
    """Indice de `lettre` si elle est présente et -1 sinon

    Args:
        lettre (str): lettre à chercher

    Returns:
        int: indice de la lettre dans ALPHABET
                ou -1 si elle n'y est pas
    """
    # la méthode `find` s'applique sur les chaînes de caractères
    return ALPHABET.find(lettre)


def cesar(message, decalage):
    """
    Exemples et doctests
    >>> cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !',4)
    'FSRNSYV E XSYW. ZMZI PE QEXMIVI RWM !'
    >>> cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !',-5)
    'BONJOUR A TOUS. VIVE LA MATIERE NSI !'
    """
    # initialisation du message codé
    resultat = ''

    # parcourt toutes les lettres de message, une par une
    # en commençant par la gauche.
    # la lettre courante est dans la variable `lettre`
    for lettre in message :

        # la lettre doit être codée
        if lettre in ALPHABET :

            # ajoute à l'indice de la lettre dans
            #   l'alphabet un décalage
            # l'appel à modulo 26 permet en cas de débordement
            #   de repartir à l'indice 0
            indice = ( position_alphabet(lettre) + decalage )%26

            # ajoute la lettre codée dans le codage du message
            resultat = resultat + ALPHABET[indice]

        # la lettre n'est pas dans l'alphabet et
        # ne doit donc pas être codée : on la laisse
        # donc inchangée (cas du `!` par exemple)
        else:
            resultat = resultat + lettre

    # renvoie du message codé
    return resultat


# Exemples
print(cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !',4))
print(cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !',-5) )


# Tests avec des assertions
assert cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !',4) == 'FSRNSYV E XSYW. ZMZI PE QEXMIVI RWM !'
assert cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !',-5) == 'BONJOUR A TOUS. VIVE LA MATIERE NSI !'


# Tests avec la bibliothèque doctest
testmod()
