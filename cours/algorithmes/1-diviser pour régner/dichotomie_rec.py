""" 
auteur : Pascal Padilla
"""


def recherche_dichotomique_rec(tab: list, elem, borne_g, borne_d) -> int:
    """Recherche dichotomique dans la portion tab[borne_g:borne_d+1]
    d'un tableau trié.

    Args:
        tab (list): tableau dans lequel on cherche
        elem (type): élément à rechercher
        borne_g (int): borne inférieure de la portion à explorer
        borne_d (int): borne supérieure de la portion à explorer

    Returns:
        int:  * si trouvé     : indice de l'élément
              * si non trouvé : None
    """
    # cas de base : portion vide
    if borne_g > borne_d:
        return None
    
    i_median = (borne_d + borne_g) // 2
    val_median = tab[i_median]

    # trouvé !
    if elem == val_median:
        return i_median

    # elem  non trouvé
    # explore la portion inférieure
    if elem < val_median:
        return recherche_dichotomique_rec(tab, elem, borne_g, i_median - 1)
    # explore la portion supérieure
    else:
        return recherche_dichotomique_rec(tab, elem, i_median + 1, borne_d)


def recherche_dichotomique(tab:list, elem) -> int:
    """Recherche dichotomique dans un tableau trie.

    Args:
        tab (list): tableau à explorer
        elem (_type_): élément à rechercher

    Returns:
        int: si trouvé     → indice de l'élément
             si non trouvé → `None`
    """
    return recherche_dichotomique_rec(tab, elem, 0, len(tab)-1)


elem = 10
tab = [i for i in range(elem)]
print(tab)

print(recherche_dichotomique(tab, 5))