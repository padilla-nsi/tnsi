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



mon_arbre = Noeud(Noeud(None, "B", Noeud(None, "C", None)), "A", Noeud(None, "D", None))

arbre1 = Noeud(None, "A", None)
arbre2 = Noeud(None, "A", None)

print( arbre1 == arbre2 )
print( arbre1.__eq__(arbre2))