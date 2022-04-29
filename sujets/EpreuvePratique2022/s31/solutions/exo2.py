"""
Author: Pascal Padilla
Source: correction de l'exercice 1 du sujet 31 des épreuves pratiques NSI 2022

Remarques:
    * algo glouton classique:
        un algorithme glouton est un algorithme qui fait un choix
        glouton à chaque tour de boucle.
        Ce choix peut éviter pleins de calculs.
        Ici, le choix glouton c'est de rendre, quand c'est possible
        la pièce la plus grande. Et si ne ce n'est pas possible, 
        de rendre la pièce d'un montant juste inférieur.
"""


def rendu_monnaie_centimes(s_due, s_versee):
    pieces = [1, 2, 5, 10, 20, 50, 100, 200]
    # -> initialisation: tableau vide (rien à rendre)
    rendu = []

    # -> initialisation de la somme à rendre
    a_rendre = s_versee - s_due

    # -> invariant: i est l'indice de la piece qu'on essaye de rendre
    i = len(pieces) - 1

    # -> condition d'arrêt: il n'y a plus rien à rendre
    while a_rendre > 0 :
        # il est possible de rendre une piece courante piece[i]
        if pieces[i] <= a_rendre :
            # ajout de la pièce dans le tableau de l'argent rendu
            rendu.append(pieces[i])
            # mise à jour de la somme à rendre
            a_rendre = a_rendre - pieces[i]
        
        # la pièce courante est plus grande que la somme à rendre
        # on passe donc à une pièce d'un montant juste inférieur
        else :
            i = i - 1
    
    # fin BOUCLE
    # il n'y a plus rien à rendre 
    # et rendu contient les pièces rendues
    return rendu



# Vérification par des assertions
assert rendu_monnaie_centimes(452, 500) == [20, 20, 5, 2, 1]
assert rendu_monnaie_centimes(700,700) == []
assert rendu_monnaie_centimes(112,500) == [200, 100, 50, 20, 10, 5, 2, 1]

# Vérification par des affichages
print(rendu_monnaie_centimes(452, 500))
print(rendu_monnaie_centimes(700,700))
print(rendu_monnaie_centimes(112,500))
