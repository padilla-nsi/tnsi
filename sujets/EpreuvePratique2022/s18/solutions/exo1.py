"""
Author: Pascal Padilla
Source: correction de l'exercice 1 du sujet 18 des épreuves pratiques NSI 2022
"""


from doctest import testmod


def mini(releve, date):
    """
    Fonction qui renvoie la plus petite valeur relevée dans le
    tableau `releve` et l'année correspondante issue du tableau `date`.

    Args:
        releve (List[float]): tableau de températures (flottants)
        date (List[int]): tableau de nombres entiers (les années)

    Returns:
        tuple: couple (valeur minimale, année associée)

    Tests:
    >>> t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
    >>> annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]
    >>> mini(t_moy, annees)
    (12.5, 2016)
    """
    # BOUCLE
    # invariant:
    #   → `i_min`: est l'indice de la valeur minimale de la
    #      portion de tableau releve[0 .. i-1]
    # initialisation:
    #   → `i_min`: est fixé à 0 (première case du tableau)
    #   → `i`: indice courant de la boucle fixé à 1
    i_min = 0

    # condition d'arrêt: tout le tableau parcouru
    #   → i == len(releve)
    nb_releves = len(releve)

    for i in range(1, nb_releves):
        # mise à jour de l'invariant si une valeur plus
        # petite est trouvée
        if releve[i] < releve[i_min]:
            i_min = i

    # POST boucle
    # i_min est l'indice de la valeur minimale
    releve_min = releve[i_min]
    date_min = date[i_min]
    return (releve_min, date_min)



# tests avec une assertion
t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]
assert mini(t_moy, annees) == (12.5, 2016)


# tests avec des affichages
print(mini(t_moy, annees))


# tests avec doctest
testmod()
