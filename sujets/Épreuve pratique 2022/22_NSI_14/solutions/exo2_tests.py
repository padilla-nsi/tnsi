import exo2 as exo
import unittest
from random import randint, choice

def est_cyclique(plan):
    '''
    Prend en paramètre un dictionnaire `plan` correspondant
    à un plan d'envoi de messages entre `N` personnes A, B, C,
    D, E, F ...(avec N <= 26).
    Renvoie True si le plan d'envoi de messages est cyclique
    et False sinon.

    Tests et Exemples:
    >>> plan_a = {'A':'E', 'B':'F', 'C':'D', 'D':'C', 'E':'B', 'F':'A'}
    >>> est_cyclique(plan_a)
    False
    >>> plan_b = {'A':'C', 'B':'F', 'C':'E', 'D':'A', 'E':'B', 'F':'D'}
    >>> est_cyclique(plan_b)
    True
    '''
    # initialisation de la clé avec la 
    # valeur initiale : 'A'
    personne = 'A'
    # longueur du plan
    N = len(plan)
    # inspecter au plus les n-1 successeurs
    for i in range(N - 1):
        if plan[personne] == 'A':
            # un des successeur est 'A', il y a donc au
            # moins 2 cycles
            return False
        else:
            # prochain successeur à explorer
            personne = plan[personne]
    
    # tous les successeurs ont été exploré
    # et aucun n'a bouclé sur 'A'. Il n'y a donc qu'un cycle
    return True


def gen_cycle(n):
    """Génère un plan cyclique de taille n.

    Args:
        n (int): longueur du plan <= 26
    """
    plan = {}
    alphabet = [chr(ord('A')+i) for i in range(1, 26)]
    key = 'A'
    for i in range(n - 1):
        suivant = alphabet.pop( randint(0, len(alphabet)-1) )
        plan[key] = suivant
        key = suivant
    
    plan[key] = 'A'
    return plan


def gen_no_cycle(n):
    """Génère un plan non cyclique de taille n.

    Args:
        n (int): longueur du plan 1 < n <= 26
    """
    plan = gen_cycle(n)
    est_modifie = False

    while not est_modifie:
        key = choice(list(plan.keys()))
        if plan[key] != 'A':
            plan[key] = 'A'
            est_modifie = True

    return plan

    
class Validation(unittest.TestCase):
    def test_exemple_1(self):
        plan = {'A':'E', 'F':'A', 'C':'D', 'E':'B', 'B':'F', 'D':'C'}
        rep_prof = est_cyclique(plan)
        rep_exo  = exo.est_cyclique(plan)

        info = "\nErreur sur les exemples de l'énoncé."
        info += "\navec " + str(plan) + " est_cyclique doit renvoyer " + str(rep_prof)
        self.assertEqual(rep_prof, rep_exo, msg=info)


    def test_exemple_2(self):
        plan = {'A':'E', 'F':'C', 'C':'D', 'E':'B', 'B':'F', 'D':'A'}
        rep_prof = est_cyclique(plan)
        rep_exo  = exo.est_cyclique(plan)

        info = "\nErreur sur les exemples de l'énoncé."
        info += "\navec " + str(plan) + " est_cyclique doit renvoyer " + str(rep_prof)
        self.assertEqual(rep_prof, rep_exo, msg=info)


    def test_exemple_3(self):
        plan = {'A':'B', 'F':'C', 'C':'D', 'E':'A', 'B':'F', 'D':'E'}
        rep_prof = est_cyclique(plan)
        rep_exo  = exo.est_cyclique(plan)

        info = "\nErreur sur les exemples de l'énoncé."
        info += "\navec " + str(plan) + " est_cyclique doit renvoyer " + str(rep_prof)
        self.assertEqual(rep_prof, rep_exo, msg=info)


    def test_exemple_4(self):
        plan = {'A':'B', 'F':'A', 'C':'D', 'E':'C', 'B':'F', 'D':'E'}
        rep_prof = est_cyclique(plan)
        rep_exo  = exo.est_cyclique(plan)

        info = "\nErreur sur les exemples de l'énoncé."
        info += "\navec " + str(plan) + " est_cyclique doit renvoyer " + str(rep_prof)
        self.assertEqual(rep_prof, rep_exo, msg=info)

    def test_random_50x(self):
        for _ in range(50):
            n = randint(2, 26)

            if randint(0, 1) == 0:
                plan = gen_cycle(n)
            else:
                plan = gen_no_cycle(n)

            rep_prof = est_cyclique(plan)
            rep_exo  = exo.est_cyclique(plan)
            
            info = "\nErreur avec le plan aléatoire"
            info += "\nest_cyclique(" + str(plan) + ") doit renvoyer " + str(rep_prof)
            self.assertEqual(rep_prof, rep_exo, msg=info)


if __name__ == '__main__':
    unittest.main()