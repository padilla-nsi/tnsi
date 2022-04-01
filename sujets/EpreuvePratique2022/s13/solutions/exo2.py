"""
Author: Pascal Padilla
Source: correction de l'exercice 2 du sujet 13 des épreuves pratiques NSI 2022

Remarques:
Je ne veux pas vous embrouiller, mais pour mieux comprendre
cet exercice, je me suis forcé à remplacer tous les
'suivant' du code par des 'precedent'.
En effet, dans ma tête en faisant monMaillon.suivant
je me dis que je vais vers la fin de la file : vers son dernier élément.
Et en faisant monMaillon.precedent, j'ai l'impression de remonter
la file et de me diriger vers son premier élément.
...
Par exemple, avec les notations officielle de l'énoncé,
on remonte la file du dernier maillon vers le premier à l'aide
d'une boucle qui calcule 'maillon.suivant'.
Personnellement, je remonte une file du dernier vers le premier
en faisant plutôt une boucle 'maillon.precedent'
...
Bon, ok, je chipote mais je n'arrivais pas à comprendre tant que
je n'avais pas réalisé cela... Et pour cause : c'est juste le contraire !
"""

class Maillon:
    """
    Maillon composé d'une valeur et d'un lien vers son
    maillon suivant.
    """ 
    def __init__(self, v):
        self.valeur = v
        self.suivant = None

class File:
    """ File de maillons possédant comme attribut un lien
    vers son dernier maillon (le dernier maillon arrivé)
    """
    def __init__(self):
        self.dernier_file = None

    def enfile(self, element):
        # création d'un nouveau maillon qui deviendra le dernier
        # ce maillon contient la valeur element
        nouveau_maillon = Maillon(element)

        # on définit le maillon suivant du nouveau
        # maillon comme étant le dernier maillon de la file
        # ceci permet "d'accrocher" le nouveau maillon à la file 
        nouveau_maillon.suivant = self.dernier_file

        # on définit le nouveau maillon comme étant le dernier
        self.dernier_file = nouveau_maillon

    def est_vide(self):
        return self.dernier_file == None

    def affiche(self):
        """ Affiche toutes les valeurs des maillons de
        la file en commençant par le dernier arrivé
        """
        maillon = self.dernier_file

        # condition d'arrêt de la boucle : 
        #   il n'y a plus de maillon à afficher
        while maillon != None:
            print(maillon.valeur)
            # on remonte dans la file
            maillon = maillon.suivant

    def defile(self):
        if not self.est_vide():
            # cas du dernier maillon qui n'a pas de suivant
            # la file ne contient donc qu'un seul élément
            if self.dernier_file.suivant == None:
                # enregistrer la valeur du dernier maillon...
                resultat = self.dernier_file.valeur
                # ...avant de l'effacer
                # la file est donc maintenant vide
                self.dernier_file = None
                # renvoyer le résultat enregistré
                return resultat

            # on va remonter dans la file en commençant par le dernier
            # maillon (dont on est certain qu'il possède un suivant)
            maillon = self.dernier_file

            # remonter dans la file de maillon en maillon
            # jusqu'à atteindre le deuxième maillon de la file
            # (c'est à dire le maillon dont son suivant est le premier)
            # (c'est à dire le maillon dont le suivant de son suivant est vide)
            # (et oui !)
            while maillon.suivant.suivant != None:
                maillon = maillon.suivant

            # ok : maillon contient le deuxième élément


            # le résultat à renvoyer est donc la valeur de
            # son maillon suivant
            # on enregistre ce résultat
            resultat = maillon.suivant.valeur

            # puis on efface la connection entre le premier
            # maillon et le deuxième
            # ceci permet de "décrocher" le premier maillon
            # et du coup, le deuxième maillon devient le nouveau premier maillon
            maillon.suivant = None

            # on renvoie la valeur enregistrée qui est bien celle de
            # l'ancien premier maillon
            return resultat

        # cas de la file vide
        # dans ce cas, on renvoie le vide
        return None


# tests de l'énoncé
F = File()
print( F.est_vide() )

F.enfile(2)
F.affiche()
print( F.est_vide() )

F.enfile(5)
F.enfile(7)
F.affiche()

print( F.defile() )
print( F.defile() )
F.affiche()
