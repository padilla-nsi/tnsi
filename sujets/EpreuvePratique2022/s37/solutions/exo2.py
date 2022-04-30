"""
Author: Pascal Padilla
Source: correction de l'exercice 2 du sujet 37 des épreuves pratiques NSI 2022

Remarques:
    * erreur dans l'énoncé: 
    page 3, Exemple d'utilisation : `election` doit renvoyer
    {'A': 3, 'B': 4, 'C': 3} ou {'B': 4, 'A': 3, 'C': 3}
"""


urne = ['A', 'A', 'A','B', 'C', 'B', 'C','B', 'C', 'B']

def depouille(urne):
    # initialisation: un dictionnaire vide
    resultat = {}
    # parcours de chaque élément (appelé `bulletin`) de l'urne
    for bulletin in urne:
        # cas où la clé `bulletin` existe déjà dans le dictionnaire `resultat`
        if bulletin in resultat:
            resultat[bulletin] = resultat[bulletin] + 1
        # cas de la première apparition de la clé `bulletin`
        # initialisation de la clé avec un premier vote
        else:
            resultat[bulletin] = 1

    # fin BOUCLE: toute l'urne est parcourue
    # resultat contient l'ensemble de tous les résultats
    return resultat

def vainqueur(election):
    # BOUCLE:
    # -> invariant: nmax est le nb maxi de bulletins d'un (ou plusieurs) candidats
    #               du tableau `election` parcouru jusqu'à présent

    # initialisation: pas de vainqueur et nmax vaut 0
    vainqueur = ''
    nmax = 0
    # parcours du dictionnaire dépouillé: clé = candidant et valeur = effectifs
    for candidat in election:
        # cas d'un candidat a plus de bulletins que le meilleur jusqu'à présent
        # `candidat` est la clé du dictionnaire et sa valeur est le nb de bulletins
        if election[candidat] > nmax :
            nmax = election[candidat]
            vainqueur = candidat
    liste_finale = [nom for nom in election if election[nom] == nmax]
    return liste_finale


# Vérification par des affichages
election = depouille(urne)
print(election)             # {'B': 4, 'A': 3, 'C': 3}
print(vainqueur(election))  # ['B']

# Vérification avec des assertions
election = depouille(urne)
assert election == {'B': 4, 'A': 3, 'C': 3}
assert vainqueur(election) == ['B']
