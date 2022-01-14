class Noeud:
    def __init__(self, g, v, d):
        self.gauche = g
        self.droit  = d
        self.valeur = v

    def __eq__(self, a):
        if a is None :
            return False

        reponse = self.gauche == a.gauche
        reponse = reponse and (self.valeur == a.valeur)
        reponse = reponse and (self.droit == a.droit)

        return reponse


def taille(a):
    if a is None:
        return 0

    max = 0

    taille_g = taille(a.gauche)
    if taille_g > max:
        max = taille_g
    
    taille_d = taille(a.droit)
    if taille_d > max:
        max = taille_d

    return 1 + max

mon_arbre = Noeud(Noeud(None, "B", Noeud(None, "C", None)), "A", Noeud(None, "D", None))

print(taille(mon_arbre))
