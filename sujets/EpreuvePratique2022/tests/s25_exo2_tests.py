import s25.solutions.exo2 as exo
import unittest


from random import randint, random, choice



def generer_intrus(pos):
    """ générer un tableau avec un intrus à la position pos"""   
    v_min = -50
    v_max = 50 
    i = 0
    tab = []
    while i < pos:
        tab += [randint(v_min, v_max)] * 3
        i += 1

    tirage = randint(v_min, v_max)
    if pos != 0:
        pred = tab[3 * pos - 1] 
        while not tirage != pred:
            tirage = randint(v_min, v_max)
    tab += [tirage]

    for i in range(randint(0, 10)):
        if i == 0:
            succ = randint(v_min, v_max)
            while not tirage != succ:
                succ = randint(v_min, v_max)
            tab += [succ] * 3
        else:
            tab += [randint(v_min, v_max)] * 3
    
    return tab



def trouver_intrus(tab, g, d):
    if g == d:
        return tab[g]
    else:
        nombre_de_triplets = (d - g) // 3
        indice = g + 3 * (nombre_de_triplets // 2)
        if tab[indice] == tab[indice + 1] :
            return trouver_intrus(tab, indice + 3, d)
        else:
            return trouver_intrus(tab, g, indice)


class Validation(unittest.TestCase):
    def test_exemple_1(self):
        tab = [3, 3, 3, 9, 9, 9, 1, 1, 1, 7, 2, 2, 2, 4, 4, 4, 8, 8, 8, 5, 5, 5]
        start = 0
        end = 21
        prop_eleve = exo.trouver_intrus(tab, start, end)
        resultat = trouver_intrus(tab, start, end)

        txt = "\nErreur avec l'exemple de l'enonce:"
        txt += "\nl'appel: trouver_intrus(" + str(tab) + ", " + str(start) + ", " + str(end) + ")"
        txt += "\ndevrait renvoyer la valeur: " + str(resultat)
        self.assertEqual(prop_eleve, resultat, msg=txt)


    def test_exemple_2(self):
        tab = [8, 5, 5, 5, 9, 9, 9, 18, 18, 18, 3, 3, 3]
        start = 0
        end = 12
        prop_eleve = exo.trouver_intrus(tab, start, end)
        resultat = trouver_intrus(tab, start, end)

        txt = "\nErreur avec l'exemple de l'enonce:"
        txt += "\nl'appel: trouver_intrus(" + str(tab) + ", " + str(start) + ", " + str(end) + ")"
        txt += "\ndevrait renvoyer la valeur: " + str(resultat)
        self.assertEqual(prop_eleve, resultat, msg=txt)


    def test_exemple_3(self):
        tab = [5, 5, 5, 1, 1, 1, 0, 0, 0, 6, 6, 6, 3, 8, 8, 8]
        start = 0
        end = 15
        prop_eleve = exo.trouver_intrus(tab, start, end)
        resultat = trouver_intrus(tab, start, end)

        txt = "\nErreur avec l'exemple de l'enonce:"
        txt += "\nl'appel: trouver_intrus(" + str(tab) + ", " + str(start) + ", " + str(end) + ")"
        txt += "\ndevrait renvoyer la valeur: " + str(resultat)
        self.assertEqual(prop_eleve, resultat, msg=txt)


    def test_random_0(self):
        for i in range(20):
            pos = 0
            tab = generer_intrus(pos)
            start = 0
            end = len(tab) - 1
            prop_eleve = exo.trouver_intrus(tab, start, end)
            resultat = trouver_intrus(tab, start, end)

            txt = "\nErreur avec intrus aléatoire place en position " + str(pos)
            txt += "\nl'appel: trouver_intrus(" + str(tab) + ", " + str(start) + ", " + str(end) + ")"
            txt += "\ndevrait renvoyer la valeur: " + str(resultat)
            self.assertEqual(prop_eleve, resultat, msg=txt)

    def test_random_2(self):
        for i in range(20):
            pos = 2
            tab = generer_intrus(pos)
            start = 0
            end = len(tab) - 1
            prop_eleve = exo.trouver_intrus(tab, start, end)
            resultat = trouver_intrus(tab, start, end)

            txt = "\nErreur avec intrus aléatoire place en position " + str(pos)
            txt += "\nl'appel: trouver_intrus(" + str(tab) + ", " + str(start) + ", " + str(end) + ")"
            txt += "\ndevrait renvoyer la valeur: " + str(resultat)
            self.assertEqual(prop_eleve, resultat, msg=txt)


    def test_random_n(self):
        for i in range(20):
            pos = randint(0, 20)
            tab = generer_intrus(pos)
            start = 0
            end = len(tab) - 1
            prop_eleve = exo.trouver_intrus(tab, start, end)
            resultat = trouver_intrus(tab, start, end)

            txt = "\nErreur avec intrus aléatoire place en position " + str(pos)
            txt += "\nl'appel: trouver_intrus(" + str(tab) + ", " + str(start) + ", " + str(end) + ")"
            txt += "\ndevrait renvoyer la valeur: " + str(resultat)
            self.assertEqual(prop_eleve, resultat, msg=txt)



if __name__ == '__main__':
    unittest.main()
