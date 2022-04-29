"""
Author: Pascal Padilla
Source: correction de l'exercice 1 du sujet 34 des épreuves pratiques NSI 2022

Remarques:
    * 'occurrence' = nombre d'apparition
    * cet exercice est DIFFICILE (trois boucles !) car on nous impose de 
    travailler avec des tableaux. Après le code, j'ai ajouté la 
    version simplifiée grâce aux dictionnaires ! 

    * on nous demande de travailler avec deux tableaux en parallèle
      et d'utiliser l'indice pour 
       - dans le premier tableau : récupérer la lettre concernée
       - dans le deuxième tableau: récupérer le nombre d'apparition
    * pour parcourir `chaine`, deux façons :
       - pythonnesque: `for lettre in chaine:...`
       - classique:    `for i in range(len(chaine)):...

    * algo:
       - d'abord parcourir la chaine lettre par lettre
          - pour chaque lettre, parcourir tout le tableau de lettre
          pour idenfier l'indice
          - augmenter la valeur occurrence de l'indice trouvé
       - parcourir le tableau d'occurrence et identifier la valeur max
       - renvoyer la valeur max
"""



def occurrence_max(chaine):
    """
    Exemples et tests:
    >>> ch = 'je suis en terminale et je passe le bac et je souhaite poursuivre des etudes pour devenir expert en informatique'
    >>> occurrence_max(ch)
    'e'
    """
    # initialisation du tableau contenant les lettres
    alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
              'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
              's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # BOUCLE 1 : parcours de la chaine lettre par lettre
    #  -> invariant : pour la zone parcourue jusqu'à présent,
    #  le tableau occurrence contient le nombre d'apparition
    #  de chaque lettre
    #
    #  -> initialement: rien n'a été parcouru donc 26 fois le `0`
    occurrence = [0] * 26

    #  -> condition d'arrêt: toute la chaine est parcourue
    for lettre in chaine:

        # BOUCLE 2: parcours du tableau alphabet
        #  -> invariant: la lettre a été cherchée dans alphabet[0 .. i-1]
        #  -> initialisation: i=0
        i = 0

        # condition d'arrêt :
        #  -> tout le tableau est parcouru: i == 26
        # OU
        #  -> la lettre est trouvée
        #
        # /!\ attention: si on inverse les conditions, il y a une erreur
        #     pourquoi...
        #     ...
        #     car si i vaut 26, alors alphabet[i] n'existe pas !
        #
        #     Mais si i vaut 26 ET que le test dans le bon sens,
        #     alors la condition s'arrête IMMÉDIATEMENT avant le OU
        #     (car i vaut 26)
        #     (et la suite n'est pas évaluée (heureusement ouf !))
        while not (i == 26 or alphabet[i] == lettre):
            i = i + 1

        # FIN BOUCLE 2
        # soit i vaut 26: la lettre n'est pas dans le tableau
        # soit i < 26: la lettre est dans le tableau
        #              et i est son indice (VICTOIRE !)

        if i < 26:
            # i est l'indice de la lettre courante
            # mise à jour du compteur d'occurrence de la lettre de la case i
            occurrence[i] = occurrence[i] + 1

    # BOUCLE 3: recherche de la valeur maximale du tableau occurrence
    #  -> invariant: i_max est l'indice de la valeur maxi de
    #                la zone occurrence[0 .. i-1]
    i_max = 0

    #   -> condition d'arrêt: après le tour de boucle i == 25
    for i in range(26):
        # mise à jour invariant si une valeur supérieure est trouvée
        if occurrence[i] > occurrence[i_max]:
            i_max = i

    # renvoie de la lettre d'indice i_max
    # et donc de la lettre avec la plus grande occurrence
    return alphabet[i_max]


ch = 'je suis en terminale et je passe le bac et je souhaite poursuivre des etudes pour devenir expert en informatique'

# vérification avec une assertion
assert occurrence_max(ch) == 'e'

# vérification avec un affichage
print(occurrence_max(ch))

# vérification avec doctest
from doctest import testmod
testmod()



# pour information :
# version plus classique avec dictionnaire
# 
# def occurrence_max_dic(chaine):
#     occurrence = {}
#     for lettre in chaine:
#         if lettre == ' ': continue
#
#         if lettre in occurrence:
#             occurrence[lettre] += 1
#         else:
#             occurrence[lettre] = 1
#
#     v_max = -1
#     for lettre in occurrence:
#         if occurrence[lettre] > v_max:
#             lettre_max = lettre
#             v_max = occurrence[lettre]
#
#     return lettre_max
