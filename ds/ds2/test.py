def affiche_rec(tab: list):
    if len(tab) == 0:
        return
    print(tab[0])
    affiche_rec(tab[1:])

def min_rec(tab: list):
    if len(tab) == 0:
        return None
    if len(tab) == 1:
        return tab[0]
    
    return min( tab[0], min_rec(tab[1:]))

def nbchiffre_rec(n: int):
    if n <= 9:
        return 1
    return 1 + nbchiffre_rec(n//10)


def listeAnagramme(mot) :
    if mot == '' : return ['']
    else :
        liste = []
        for anagr in listeAnagramme(mot[1:]) :
            for k in range(len(mot)) :
                liste.append(anagr[:k] + mot[0] + anagr[k:])
        return liste

def ecrire_nb_rec(debut, fin):
    if debut > fin:
        return
    
    print(debut)
    ecrire_nb_rec(debut+1, fin)
    
ecrire_nb_rec(4, 12)

# tab = [1,3,5,7,9,10]
# print( tab[3:0:-1] )
# print(min_rec(tab))
# affiche_rec(tab)

print(nbchiffre_rec(10345))

class Voiture():
    def __init__(self, nb_porte, couleur, annee):
        self.nb_porte = nb_porte
        self.couleur  = couleur
        self.annee    = annee

    def info(self):
        texte = "année : " + str(self.annee) + ", couleur : " + self.couleur
        return texte

class Voiture():
    def __init__(self, nb_porte: int, couleur: str, annee: int):
        self.nb_porte = nb_porte
        self.couleur  = couleur
        self.annee    = annee

    def info(self) -> str:
        texte = "année : " + str(self.annee) + ", couleur : " + self.couleur
        return texte

