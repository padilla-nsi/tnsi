"""
Author: Pascal Padilla
Source: correction de l'exercice 2 du sujet 21 des épreuves pratiques NSI 2022

Remarque:
    * lorsque la valeur cherchée est présente dans le tableau, la
    fonction ne renvoie pas l'indice (ce qui est classique) mais True.
    La fonction indique si l'élément est présent ou pas dans le tableau
"""


def dichotomie(tab, x):
    """
        tab : tableau d’entiers trié dans l’ordre croissant
        x : nombre entier
        La fonction renvoie True si tab contient x et False sinon
    """
    # début de la zone à explorer
    debut = 0
    # fin de la zone à explorer
    fin = len(tab) - 1

    # tant que la zone à explorer n'est pas vide
    while debut <= fin:
        # indice médian de la zone à explorer
        m = (fin + debut) // 2

        # la valeur cherchée est égale à la valeur médiane
        # alors c'est trouvé : renvoyer True
        if x == tab[m]:
            return True

        # si présente, la valeur cherchée est après la valeur médiane
        # changement de zone de recherche en modifiant le début
        if x > tab[m]:
            debut = m + 1

        # si présente, la valeur est avant la valeur médiane
        # changement de la zone de recherche en modifiant la fin
        else:
             fin = m - 1

    # si on sort de la boucle c'est que la zone de recherche est 
    # désormais vide et donc l'élément cherché n'y est pas
    return False


# tests avec des assertions
assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],28) is True
assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],27) is False

# tests avec des affichages
print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],28))
print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],27))
