"""
Author: Pascal Padilla
Source: correction de l'exercice 2 du sujet 35 des épreuves pratiques NSI 2022

Remarques:
    * version itérative de la recherche dichotomique
    * le renvoie `return False, 1` renvoie en fait un tuple : `return (False, 1)
    * la distinction des trois cas False (avec 1, 2 e 3) permet
    de bien mettre en évidence pourquoi l'élément n'y est pas :
      -> cas 1 : tableau vide
      -> cas 2 : valeur hors limite
      -> cas 3 : recherche effectuée mais infructueuse
"""



def dichotomie(tab, x):
    """
        tab : tableau trié dans l’ordre croissant
        x : nombre entier
        La fonction renvoie True si tab contient x et False sinon
    """
    # cas du tableau vide
    if tab == [] :
        # renvoie et donc fin de la fonction
        return False, 1

    # cas où x n'est pas compris entre les valeurs extrêmes
    if (x < tab[0]) or (x > tab[len(tab)-1]):
        # renvoie et donc fin de la fonction
        return False, 2
    
    debut = 0
    fin = len(tab) - 1

    # condition d'arrêt :
    #  -> la zone de recherche tab[debut .. fin] est un tableau vide
    #     et donc debut devient supérieur à fin
    while debut <= fin:
        # valeur médiane :
        m = (debut + fin) // 2

        # l'élément cherché est égale à la valeur médiane : trouvé !
        if x == tab[m]:
            # renvoie et fin de la fonction
            return True

        # recherche dans la partie supérieure à la case médiane
        if x > tab[m]:
            debut = m + 1

        # recherche dans la partie inférieure à la case médiane
        else:
            fin = m - 1

    # SORTIE de boucle
    #  la zone de recherche est vide
    #  et l'élément n'a pas encore été trouvé

    # renvoie infructueux associé au cas numéro 3
    return False, 3


# vérification par des assertions
assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],28) == True
assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],27) == (False, 3)
assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],1) == (False, 2)
assert dichotomie([],28) == (False, 1)

# vérification par des affichages

print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],28))
print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],27))
print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],1))
print(dichotomie([],28))
