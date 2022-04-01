"""
Author: Pascal Padilla
Source: correction de l'exercice 1 du sujet 14 des épreuves pratiques NSI 2022
"""

from doctest import testmod


def correspond(mot: str, mot_a_trous: str) -> bool:
    """Est ce que mot_a_trou peut correspondre à mot ?

    Args:
        mot (str): chaîne de caractère majuscule
        mot_a_trous (str): chaîne à trous (majuscule + '*')

    Returns:
        bool: True si on peut obtenir mot en remplaçant convenablement
        les caractères '*' de mot_a_trous

    Tests et Exemples:
    >>> correspond('INFORMATIQUE', 'INFO*MA*IQUE')
    True

    >>> correspond('AUTOMATIQUE', 'INFO*MA*IQUE')
    False
    """
    n = len(mot)

    # BOUCLE tant que
    # invariant:
    #   * les i premiers caractères de 'mot' et 'mot_a_trou'
    #     sont compatibles : 'est_egal' est donc vrai
    # condition d'arrêt de la boucle :
    #  * le compteur i dépasse la longueur 'n' du mot
    #  * les chaînes sont incompatibles → 'est_egal' est faux
    est_egal = True
    i = 0
    while not (i >= n or (not est_egal)):
        # cas d'un caractère autre qu'un joker '*'
        if mot_a_trous[i] !=  '*':
            if mot_a_trous[i] != mot[i]:
                # les caractères sont différents
                # comme ce n'est pas un joker '*', les chaines
                # sont désormais incompatibles → est_egal devient faux
                # (ce qui est une des conditions d'arrêt)
                est_egal = False

        # mise à jour du variant qui nous assure que la boucle
        # va bien finir par s'arrêter un jour
        i = i + 1

    return est_egal


# Tests de l'énoncé à l'aide de la bibliothèque doctest
testmod()
