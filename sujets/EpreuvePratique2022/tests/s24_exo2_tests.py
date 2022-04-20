import s24.solutions.exo2 as exo
import unittest


from random import randint, random, choice


class Pile:
    """ Classe définissant une pile """
    def __init__(self):
        self.valeurs = []

    def est_vide(self):
        """Renvoie True si la pile est vide, False sinon"""
        return self.valeurs == []

    def empiler(self, c):
        """Place l’élément c au sommet de la pile"""
        self.valeurs.append(c)

    def depiler(self):
        """Supprime l’élément placé au sommet de la pile, à condition qu’elle soit non vide"""
        if self.est_vide() == False:
            self.valeurs.pop()


def parenthesage (ch):
    """Renvoie True si la chaîne ch est bien parenthésée et False sinon"""
    p = Pile()
    for c in ch:
        if c == '(':
            p.empiler(c)
        elif c == ')':
            if p.est_vide():
                return False
            else:
                p.depiler()
    return p.est_vide()


def generer_mot(taille):
    mot = ""
    pile = []
    reserve = ['('] * taille

    for i in range (taille * 2):
        if pile:
            if reserve and random() < 0.5:
                    pile.append('(')
                    reserve.pop()
                    mot += '('
            else:
                pile.pop()
                mot += ')'
        else:
            pile.append('(')
            reserve.pop()
            mot += '('
    return mot


def generer_mot_mauvais(taille):
    mot_correct = generer_mot(taille)
    i = randint(0, taille - 1)
    mot_faux = mot_correct[:i]
    mot_faux += '(' if mot_correct[i] == ')' else ')'
    mot_faux += mot_correct[i+1:]
    return mot_faux




class Validation(unittest.TestCase):
    def test_exemple_1(self):
        mot = "((()())(()))"
        calcul_juste = parenthesage(mot)
        calcul_eleve = exo.parenthesage(mot)
        txt = "\nErreur avec un exemple de l'enonce"
        txt += "\nla chaine '" + str(mot)
        txt += "' doit renvoyer " + str(calcul_juste)
        self.assertEqual(calcul_eleve, calcul_juste, msg=txt)
        

    def test_exemple_2(self):
        mot = "())(()"
        calcul_juste = parenthesage(mot)
        calcul_eleve = exo.parenthesage(mot)
        txt = "\nErreur avec un exemple de l'enonce"
        txt += "\nla chaine '" + str(mot)
        txt += "' doit renvoyer " + str(calcul_juste)
        self.assertEqual(calcul_eleve, calcul_juste, msg=txt)
        

    def test_exemple_3(self):
        mot = "(())(()"
        calcul_juste = parenthesage(mot)
        calcul_eleve = exo.parenthesage(mot)
        txt = "\nErreur avec un exemple de l'enonce"
        txt += "\nla chaine '" + str(mot)
        txt += "' doit renvoyer " + str(calcul_juste)
        self.assertEqual(calcul_eleve, calcul_juste, msg=txt)
    

    def test_random_6(self):
        for i in range(20):
            taille = 3
            mot = generer_mot(taille) if random() < 0.8 else generer_mot_mauvais(taille)

            calcul_juste = parenthesage(mot)
            calcul_eleve = exo.parenthesage(mot)
            txt = "\nErreur avec la chaine '" + str(mot)
            txt += "' qui doit renvoyer " + str(calcul_juste)
            self.assertEqual(calcul_eleve, calcul_juste, msg=txt)


    def test_random_n(self):
        for i in range(20):
            taille = randint(3, 50)
            mot = generer_mot(taille) if random() < 0.8 else generer_mot_mauvais(taille)

            calcul_juste = parenthesage(mot)
            calcul_eleve = exo.parenthesage(mot)
            txt = "\nErreur avec la chaine '" + str(mot)
            txt += "' qui doit renvoyer " + str(calcul_juste)
            self.assertEqual(calcul_eleve, calcul_juste, msg=txt)



if __name__ == '__main__':
    unittest.main()
