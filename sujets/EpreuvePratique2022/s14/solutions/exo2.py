"""
Author: Pascal Padilla
Source: correction de l'exercice 2 du sujet 14 des épreuves pratiques NSI 2022

Remarque : j'aime pas les noms de variable en majuscule : 'N'
"""

def est_cyclique(plan):
    '''
    Prend en paramètre un dictionnaire `plan` correspondant
    à un plan d'envoi de messages entre `N` personnes A, B, C,
    D, E, F ...(avec N <= 26).
    Renvoie True si le plan d'envoi de messages est cyclique
    et False sinon.
    '''
    # initialisation de la clé du dictionnaire
    # avec la valeur initiale : 'A'
    personne = 'A'

    # initialisation de la longueur du plan
    N = len(plan)

    # explorer au plus les N - 1 successeurs
    for i in range(N - 1):
        if plan[personne] == 'A':
            # un des successeur est 'A', il y a donc au
            # moins 2 cycles
            return False
        else:
            # prochain successeur à explorer
            personne = plan[personne]

    # tous les successeurs ont été exploré
    # et aucun n'a bouclé sur 'A'. Il n'y a donc qu'un cycle
    return True


# Tests et Exemples:
plan_a = {'A':'E', 'B':'F', 'C':'D', 'D':'C', 'E':'B', 'F':'A'}
assert est_cyclique(plan_a) == False
plan_b = {'A':'C', 'B':'F', 'C':'E', 'D':'A', 'E':'B', 'F':'D'}
assert est_cyclique(plan_b) == True
