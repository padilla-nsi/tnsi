"""
Author: Pascal Padilla
Source: correction de l'exercice 1 du sujet 25 des épreuves pratiques NSI 2022
"""


def selection_enclos(dic_animaux: dict, num_enclos: int) -> dict:
    """
    Sélection dans un dictionnaire de données en fonction 
    de l'identifiant de l'enclos

    Args:
        dic_animaux (dict): données avec au moins la clé 'enclos'
        num_enclos (int): identifiant de l'enclos à sélectionner

    Returns:
        dict: dictionnaire de données filtré par num_enclos

    Tests et exemples:
    >>> animaux = [ {'nom':'Medor', 'espece':'chien', 'age':5, 'enclos':2}, \
                    {'nom':'Titine', 'espece':'chat', 'age':2, 'enclos':5}, \
                    {'nom':'Tom', 'espece':'chat', 'age':7, 'enclos':4},    \
                    {'nom':'Belle', 'espece':'chien', 'age':6, 'enclos':3}, \
                    {'nom':'Mirza', 'espece':'chat', 'age':6, 'enclos':5}]
    >>> selection_enclos(animaux, 5)
    [{'nom': 'Titine', 'espece': 'chat', 'age': 2, 'enclos': 5}, {'nom': 'Mirza', 'espece': 'chat', 'age': 6, 'enclos': 5}]
    >>> selection_enclos(animaux, 2)
    [{'nom': 'Medor', 'espece': 'chien', 'age': 5, 'enclos': 2}]
    >>> selection_enclos(animaux, 7)
    []
    """
    # resultat qui sera renvoyé en sortie
    # (tableau de dictionnaire(s))
    resultat_requete = []

    # parcourir tout le dictionnaire dans une boucle
    for entite in dic_animaux:

        # ajouter l'entité courante si l'identifiant correspond
        if entite['enclos'] == num_enclos:
            resultat_requete.append(entite)
    
    # renvoyer le résultat de la sélection
    return resultat_requete



# tests avec des affichages
animaux = [ {'nom':'Medor', 'espece':'chien', 'age':5, 'enclos':2},
            {'nom':'Titine', 'espece':'chat', 'age':2, 'enclos':5},
            {'nom':'Tom', 'espece':'chat', 'age':7, 'enclos':4},
            {'nom':'Belle', 'espece':'chien', 'age':6, 'enclos':3},
            {'nom':'Mirza', 'espece':'chat', 'age':6, 'enclos':5}]
            
print(selection_enclos(animaux, 5))
print(selection_enclos(animaux, 2))
print(selection_enclos(animaux, 7))


# tests avec des assertions
animaux = [ {'nom':'Medor', 'espece':'chien', 'age':5, 'enclos':2}, \
                    {'nom':'Titine', 'espece':'chat', 'age':2, 'enclos':5}, \
                    {'nom':'Tom', 'espece':'chat', 'age':7, 'enclos':4},    \
                    {'nom':'Belle', 'espece':'chien', 'age':6, 'enclos':3}, \
                    {'nom':'Mirza', 'espece':'chat', 'age':6, 'enclos':5}]
assert selection_enclos(animaux, 5) == [{'nom': 'Titine', 'espece': 'chat', 'age': 2, 'enclos': 5}, {'nom': 'Mirza', 'espece': 'chat', 'age': 6, 'enclos': 5}]
assert selection_enclos(animaux, 2) == [{'nom': 'Medor', 'espece': 'chien', 'age': 5, 'enclos': 2}]
assert selection_enclos(animaux, 7) == []


# tests avec doctest
from doctest import testmod
testmod()


[ {'nom':'a', 'espece':'chien', 'age':5, 'enclos':2}, {'nom':'Titine', 'espece':'chat', 'age':2, 'enclos':5}, {'nom':'Tom', 'espece':'chat', 'age':7, 'enclos':4}, {'nom':'Belle', 'espece':'chien', 'age':6, 'enclos':3}, {'nom':'Mirza', 'espece':'chat', 'age':6, 'enclos':5}]

from random import randint
dico = [{'nom': chr(i), 'enclos': randint(0,5)} for i in range(97,107)]
print(dico)
print(ord('z'))