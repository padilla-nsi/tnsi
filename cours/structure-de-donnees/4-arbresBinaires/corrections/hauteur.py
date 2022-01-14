class Noeud:
    def __init__(self, g, v, d):
        self.gauche = g
        self.droit  = d
        self.valeur = v


mon_arbre = Noeud(Noeud(None, "B", Noeud(None, "C", None)), "A", Noeud(None, "D", None))

