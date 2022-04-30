"""
Author: Pascal Padilla
Source: correction de l'exercice 2 du sujet 40 des épreuves pratiques NSI 2022

Remarques:
    * bien comprendre le parcours de dictionnaire `for valeurs in dico.values()`
    À chaque tour de boucle, `valeurs` vaut la valeur de la clé courante
    Ce parcours ne s'intéresse donc pas à la clé,
    mais parcourt le dictionnaire quand même.
"""



resultats = {'Dupont':{'DS1' : [15.5, 4],
                       'DM1' : [14.5, 1],
                       'DS2' : [13, 4],
                       'PROJET1' : [16, 3],
                       'DS3' : [14, 4]},
             'Durand':{'DS1' : [6 , 4],
                       'DM1' : [14.5, 1],
                       'DS2' : [8, 4],
                       'PROJET1' : [9, 3],
                       'IE1' : [7, 2],
                       'DS3' : [8, 4],
                       'DS4' :[15, 4]}}


def moyenne(nom):
    # cas de la clé nom qui est présente dans le dictionnaire
    # c'est-à-dire que le prof a bien l'élève dans ses résultats
    if nom in resultats:
        # création d'un dictionnaire contenant
        # toutes les évaluations de l'élève `nom`
        notes = resultats[nom]

        # BOUCLE: parcours de toutes les notes pour
        #         calculer le total des points et des coefficients
        # -> invariant: total_point est le cumul de tous les (points × coef) 
        #               de la zone parcourue jusqu'à présent
        total_points = 0
        # -> invariant: total_coefficients est le cumul des coef
        #               de la zone parcourue jusqu'à présent
        total_coefficients = 0
        # -> condition d'arrêt: après la dernière évaluation
        for valeurs in notes.values():
            # comme valeurs est une évaluation, c'est un tableau
            # de deux élèments: (1) la note et (2) le coefficient
            # la ligne suivante est une pythonnerie qui équivaut à :
            #   note = valeurs[0]
            #   coefficient = valeurs[1]
            note , coefficient = valeurs

            # maintient des deux invariants
            total_points = total_points + note * coefficient
            total_coefficients = total_coefficients + coefficient
        
        # fin BOUCLE: toutes les évaluations sont parcourues

        # formule de la moyenne coefficientée
        return round( total_points / total_coefficients , 1 )
    
    # cas d'un élève qui n'a aucune évaluation
    # (et donc n'est pas dans le dictionnaire)
    else:
        return -1


# Vérification avec des assertions
assert moyenne('Dupont') == 14.5
assert moyenne('Dupond') == -1

# Vérification avec des affichages
print(moyenne('Dupont'))    # 14.5
print(moyenne('Dupond'))    # -1
