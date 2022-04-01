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
    # compteur pour parcourir les chaînes 0..n-1
    i = 0
    # booléen qui indique que mot et mot_a_trous sont identiques
    est_egal = True

    # condition d'arrêt de la boucle :
    #  * le compteur i dépasse la longueur du mot
    #  * les chaînes sont incompatibles
    while not (i >= n or est_egal == False):
        # jusqu'à présent les chaînes ont été compatibles
        if mot_a_trous[i] !=  '*':
            if mot_a_trous[i] != mot[i]:
                # les caractères sont différents et 
                # ce n'est pas un joker '*'
                # donc les chaines sont désormais incompatibles
                est_egal = False
        i = i + 1

    return est_egal


if __name__ == '__main__':
    testmod()