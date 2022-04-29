"""
Author: Pascal Padilla
Source: correction de l'exercice 2 du sujet 30 des épreuves pratiques NSI 2022

Remarques:
    * l'argument `nombre` est trompeur : ce n'est pas un entier mais
    une chaîne de caractère (c'est un nombre...romain ;))
    * attention au sens de la soustraction pour le cas de la soustraction
"""


def rom_to_dec (nombre):

    """ Renvoie l’écriture décimale du nombre donné en chiffres romains """

    # correspondance entre un caractère romain (la clé) et sa valeur
    dico = {"I":1, "V":5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    # cas de base : il n'y a pas d'addition ou de soustraction à faire
    if len(nombre) == 1:
        # renvoie de la valeur du caractère
        return dico[nombre]

    else:
        ### on supprime le premier caractère de la chaîne contenue dans la variable nombre
		### et cette nouvelle chaîne est enregistrée dans la variable nombre_droite
        nombre_droite = nombre[1:]

        # cas où il faut additionner (chiffre de gauche >= au chiffre de droite)
        if dico[nombre[0]] >= dico[nombre[1]]:
            # appel récursif: la valeur décimale est égale à la somme
            # de la valeur du chiffre de gauche et de la valeur de
            # l'ensemble des chiffres romains de droite
            return dico[nombre[0]] + rom_to_dec(nombre_droite)

        # cas de la soustraction: la valeur finale est égale à la
        # différence de la valeur de l'ensemble de droite
        # par la valeur du chiffre de gauche
        else:
            return rom_to_dec(nombre_droite) - dico[nombre[0]]



# Vérification par une assertion
assert rom_to_dec("CXLII") == 142

# Vérification par un affichage
print(rom_to_dec("CXLII"))
