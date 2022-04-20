import s23.solutions.exo2 as exo
import unittest


from random import randint, random, choice


class Pile:
    """Classe définissant une structure de pile."""
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        """Renvoie le booléen True si la pile est vide, False sinon."""
        return self.contenu == []

    def empiler(self, v):
        """Place l'élément v au sommet de la pile"""
        self.contenu.append(v)

    def depiler(self):
        """
        Retire et renvoie l’élément placé au sommet de la pile,
        si la pile n’est pas vide.
        """
        if not self.est_vide():
            return self.contenu.pop()


def eval_expression(tab):
    p = Pile()
    for element in tab:
        if element != '+' and element != '*':
            p.empiler(element)
        
        else:
            if element == '+':
                resultat = p.depiler() + p.depiler()
            else:
                resultat = p.depiler() * p.depiler()
            p.empiler(resultat)
    return p.depiler()



def creer_ops(taille):
    mini = -50
    maxi = 50

    if taille == 1:
        tab  = [randint(mini, maxi)]
        tab += [randint(mini, maxi)]
        tab += [choice(['+', '*'])]
        return  tab
    
    tab  = [randint(mini, maxi)]
    tab += [choice(['+', '*'])]
    return creer_ops(taille - 1) + tab



class Validation(unittest.TestCase):
    def test_exemple_1(self):
        ops = [2, 3, '+', 5, '*']
        resultat = eval_expression(ops)
        txt  = "\nErreur avec l'exemple de l'enonce"
        txt += "\nle tableau " + str(ops) + " doit renvoyer "
        txt += str(resultat)
        self.assertEqual(exo.eval_expression(ops), resultat, msg=txt)


    def test_exemple_2(self):
        ops = [3, 2, '*', 5, '+']
        resultat = eval_expression(ops)
        txt  = "\nErreur avec l'exemple de l'enonce"
        txt += "\nle tableau " + str(ops) + " doit renvoyer "
        txt += str(resultat)
        self.assertEqual(exo.eval_expression(ops), resultat, msg=txt)


    def test_alea_2(self):
        for i in range(20):
            ops = creer_ops(2)

            resultat_juste = eval_expression(ops)
            resultat_eleve = exo.eval_expression(ops)
            txt  = "\nErreur avec l'exemple de l'enonce"
            txt += "\nle tableau " + str(ops) + " doit renvoyer "
            txt += str(resultat_juste)
            self.assertEqual(resultat_eleve, resultat_juste, msg=txt)


    def test_alea_n(self):
        for i in range(20):
            ops = creer_ops(randint(2, 15))

            resultat_juste = eval_expression(ops)
            resultat_eleve = exo.eval_expression(ops)
            txt  = "\nErreur avec l'exemple de l'enonce"
            txt += "\nle tableau " + str(ops) + " doit renvoyer "
            txt += str(resultat_juste)
            self.assertEqual(resultat_eleve, resultat_juste, msg=txt)



if __name__ == '__main__':
    unittest.main()
