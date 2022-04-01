"""
Author: Pascal Padilla
Source: correction de l'exercice 2 du sujet 15 des épreuves pratiques NSI 2022
"""


def binaire(a):
    # initialise la chaîne de caractère finale
    # avec le dernier caractère : le reste de la
    # division euclidienne du nombre 'a' par 2
    # (qui vaut '0' si 'a' est paire et '1' sinon)
    bin_a = str(a % 2)

    # met à jour 'a' avec le quotient de la division
    # ce quotient devient le nouveau nombre à diviser
    a = a // 2

    # condition d'arrêt de la boucle : le nouveau nombre à diviser
    # (c'est-à-dire le quotient de la division précédente)
    # est nul. C'est donc la fin des divisions successives
    while a != 0 :
        # la chaîne de caractère est mise à jour
        # pour cela on utilise l'opérateur '+' qui permet
        # de concaténer des chaînes
        # on écrit le reste de la division (converti en
        # chaîne de caractère) avant ce qui était
        # déjà écrit dans la chaîne
        bin_a = str(a % 2) + bin_a

        # mise à jour du quotient pour la prochaine division
        a = a // 2

    # renvoie de la chaîne complète
    return bin_a


# Tests de l'énoncé
assert binaire(0) == '0'
assert binaire(77) == '1001101'
