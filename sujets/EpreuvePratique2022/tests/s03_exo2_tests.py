import s03.solutions.exo2 as exo
import unittest


class Noeud:
    def __init__(self, g, v, d):
        self.gauche = g
        self.valeur = v
        self.droit = d

    def __str__(self):
        return str(self.valeur)

    def est_une_feuille(self):
        '''Renvoie True si et seulement si le noeud est une feuille'''
        return self.gauche is None and self.droit is None




def expression_infixe(e):
    """Parcours infixe d'un arbre pour afficher les noeuds
    séparés par des parenthèses.

    Args:
        e (Noeud): racine de l'arbre

    Returns:
        str: expression bien formée par des parenthèses de l'abre e
    
    Tests et Exemples:
    >>> e = Noeud(Noeud(Noeud(None, 3, None), '*', Noeud(Noeud(None, 8, None), '+', Noeud(None, 7, None))), '-', Noeud(Noeud(None, 2, None), '+', Noeud(None, 1, None)))
    >>> expression_infixe(e)
    '((3*(8+7))-(2+1))'
    """
    # initialisation de la chaine à renvoyer
    s = ""
    if e.gauche is not None:
        # appel récursif pour afficher d'abord le sous arbre gauche
        s = s + expression_infixe(e.gauche)
    # ajout de la valeur du noeud
    # en utilisant la méthode dédiée
    s = s + str(e)
    if e.droit is not None:
        # appel récursif pour afficher d'abord le sous arbre gauche
        # s'il est non vide
        s = s + expression_infixe(e.droit)
    
    # cas de base : le noeud est une feuille
    if e.est_une_feuille():
        # afficher la valeur sans les parenthèses
        return s


    return '('+ s +')'


class validation(unittest.TestCase):
    def test_exemple_valeur(self):
        print("Tests automatiques avec les exemples de l'énoncé...")
        e = Noeud(Noeud(Noeud(None, 3, None), '*', Noeud(Noeud(None, 8, None), '+', Noeud(None, 7, None))), '-', Noeud(Noeud(None, 2, None), '+', Noeud(None, 1, None)))
        print(e)
        rep_prof = expression_infixe(e)
        rep_exo  = exo.expression_infixe(e)
        
        info = "Erreur avec ton code sur l'exemple. Le résultat de ton calcul est différent du résultat attendu"
        self.assertEqual(rep_prof, rep_exo, msg=info)


    def test_aleatoire(self):
        from random import choice, randint
        ops = ['+', '-', '*', '/']

        f = [Noeud(None, randint(-999, 999) , None) for _ in range(5)]

        op_0 = Noeud(f[0], choice(ops), f[1])
        op_1 = Noeud(f[2], choice(ops), f[3])

        op_2 = Noeud(f[4], choice(ops), op_0)
        
        e = Noeud(op_1, choice(ops), op_2)

        rep_prof = expression_infixe(e)
        rep_exo  = exo.expression_infixe(e)
        
        info = 'Erreur avec ton code sur des valeurs aléatoires. Le résultat de ton calcul est différent du résultat attendu'
        self.assertEqual(rep_prof, rep_exo, msg=info)


if __name__ == '__main__':
    unittest.main()
