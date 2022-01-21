from doctest import testmod


def recherche(gene, seq_adn):
    """ Recherche la présence de la chaîne gene dans la chaîne seq_adn.

    Args:
        gene (str): chaîne de caractère à rechercher
        seq_adn (str): chaîne de caractère à explorer

    Returns:
        bool: True ssi gene est présent dans seq_adn

    Tests et Exemples:
    >>> recherche("AATC", "GTACAAATCTTGCC")
    True
    >>> recherche("AGTC", "GTACAAATCTTGCC")
    False
    """
    n = len(seq_adn)
    g = len(gene)
    # compteur de la lettre courante dans seq_adn
    i = 0
    trouve = False
    # la boucle se perpétue tant que : 
    # * le compteur i ne dépasse pas la valeur limite
    # * ET que le gène na pas encore été trouvé
    while i < n - g + 1 and trouve == False :
        j = 0
        while j < g and gene[j] == seq_adn[i+j]:
            # pour les j premières recherche, le gene correspond
            # et donc on va explorer le caractère suivant
            j = j + 1
        if j == g:
            trouve = True
        # l'exploration du caractère i est terminée
        # que gene ai été trouvé ou pas, on va tenter
        # d'explorer le caractère suivant
        i = i + 1
    
    return trouve


assert recherche("AATC", "GTACAAATCTTGCC") == True
assert recherche("AGTC", "GTACAAATCTTGCC") == False

testmod()