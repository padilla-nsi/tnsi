"""
Author: Pascal Padilla
Source: correction de l'exercice 2 du sujet 18 des épreuves pratiques NSI 2022
"""


def inverse_chaine(chaine):
    # initialisation avec une chaîne vide
    result = ''

    # boucle qui parcourt les symboles de la chaîne de
    # caractère un par un
    # `caractete` vaut le symbole courant
    for caractere in chaine:

        # concaténation du caractère courant au **début** de
        # la chaîne résultat qui sera renvoyée
        result = caractere + result

    return result


def est_palindrome(chaine):
    # inverse contient la chaîne inversée
    inverse = inverse_chaine(chaine)

    # tests booléen qui vaut: 
    # Vrai ←→ la chaine et son inverse sont égales
    #
    # la fonction renvoie le résultat du test booléen
    return chaine == inverse


def est_nbre_palindrome(nbre):
    # transforme le nbre en chaîne de caractère
    chaine = str(nbre)
    return est_palindrome(chaine)


# tests avec des assertions
assert inverse_chaine('bac') == 'cab'
assert est_palindrome('NSI') == False
assert est_palindrome('ISN-NSI') == True
assert est_nbre_palindrome(214312) == False
assert est_nbre_palindrome(213312) == True


# tests avec des affichages
print(inverse_chaine('bac'))
print(est_palindrome('NSI'))
print(est_palindrome('ISN-NSI'))
print(est_nbre_palindrome(214312))
print(est_nbre_palindrome(213312))
