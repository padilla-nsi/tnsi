class Noeud:
    def __init__(self, g, v, d):
        self.gauche = g
        self.droit  = d
        self.valeur = v

def affiche(a):
    if a is None:
        return ""

    texte = ""
    texte = texte + "("

    texte = texte + affiche(a.gauche)
    texte = texte + str(a.valeur)
    texte = texte + affiche(a.droit)

    texte = texte + ")"

    return texte

mon_arbre = Noeud(Noeud(None, "B", Noeud(None, "C", None)), "A", Noeud(None, "D", None))

print(affiche(mon_arbre))