import s17.solutions.exo1 as exo
import unittest
from random import randint


def nombre_de_mots(phrase: str) -> int:
    """Nombre de mots d'une phrase

    Args:
        phrase (str): phrase avec des mots : 
        * séparés par un seul caractère espace et
        * se fini par :
            un point collé au dernier mot
            OU par un point d'exclamation/interrogation 
               séparé du dernier mot un espace.

    Returns:
        int: nombre de mots de la phrase

    Tests et Exemples:
    >>> nombre_de_mots('Le point d exclamation est separe !')
    6
    >>> nombre_de_mots('Il y a un seul espace entre les mots !')
    9
    >>> nombre_de_mots('Le point final est colle au dernier mot.')
    8
    >>> nombre_de_mots('Gilbouze macarbi acra cor ed filbuzine ?')
    6
    """
    # on va compter le nombre de caractères espace
    n_espace = 0
    n = len(phrase)
    for i in range(n):
        lettre_courante = phrase[i]
        if lettre_courante == ' ':
            n_espace = n_espace + 1
    
    # si le dernier caractère est un point, il manque un caractère 
    # espace pour compter correctement le nombre de mots
    # sinon le nombre de mots est égal au nombre d'espaces
    if lettre_courante == '.':
        n_mot = n_espace + 1
    else:
        n_mot = n_espace

    return n_mot


def get_mot(n):
    """Génère un mot de taille n

    Args:
        n (int): longueur du mot à générer
    """
    mot = ""
    for i in range(n):
        mot += chr(ord('a') + randint(0, 25))
    
    return mot


def get_phrase(n):
    """Génère une phrase de n mots.

    Args:
        n (int): nombre de mots de la phrase
    """
    phrase = ""
    for i in range(n):
        phrase += get_mot(randint(1, 10)) + " "
    
    # fin de phrase
    tirage = randint(0, 2)
    if tirage == 0:
        phrase += "!"
    elif tirage == 1:
        phrase += "?"
    else:
        phrase = phrase[:-1] + "."
        
    # majuscule
    phrase = chr(ord('A') + randint(0, 25)) + phrase[1:]

    return phrase


class Validation(unittest.TestCase):
    def test_exemple_1(self):
        print("Test sur exemple numero 1")
        phrase = "Le point d exclamation est separe !"
        rep_prof = nombre_de_mots(phrase)
        rep_exo  = exo.nombre_de_mots(phrase)

        info = "Erreur sur le calcul avec la valeur de l'enonce:"
        info += "\n=> nombre_de_mots('"+phrase+"') doit renvoyer "
        info += str(rep_prof)
        self.assertEqual(rep_prof, rep_exo, msg=info)

    def test_exemple_2(self):
        print("Test sur exemple numero 2")
        phrase = "Il y a un seul espace entre les mots !"
        rep_prof = nombre_de_mots(phrase)
        rep_exo  = exo.nombre_de_mots(phrase)

        info = "Erreur sur le calcul avec la valeur de l'enonce:"
        info += "\n=> nombre_de_mots('"+phrase+"') doit renvoyer "
        info += str(rep_prof)
        self.assertEqual(rep_prof, rep_exo, msg=info)

    def test_exemple_3(self):
        print("Test sur exemple numero 3")
        phrase = "Le point final est colle au dernier mot."
        rep_prof = nombre_de_mots(phrase)
        rep_exo  = exo.nombre_de_mots(phrase)

        info = "Erreur sur le calcul avec la valeur de l'enonce:"
        info += "\n=> nombre_de_mots('"+phrase+"') doit renvoyer "
        info += str(rep_prof)
        self.assertEqual(rep_prof, rep_exo, msg=info)

    def test_exemple_4(self):
        print("Test sur exemple numero 4")
        phrase = "Gilbouze macarbi acra cor ed filbuzine ?"
        rep_prof = nombre_de_mots(phrase)
        rep_exo  = exo.nombre_de_mots(phrase)

        info = "Erreur sur le calcul avec la valeur de l'enonce:"
        info += "\n=> nombre_de_mots('"+phrase+"') doit renvoyer "
        info += str(rep_prof)
        self.assertEqual(rep_prof, rep_exo, msg=info)

    def test_random_1_10x(self):
        for i in range(10):
            n = randint(1, 50)
            phrase = get_phrase(n)
            rep_exo = exo.nombre_de_mots(phrase)

            info = "Erreur sur le calcul avec des phrases aleatoires:"
            info += "\n=> nombre_de_mots('"+phrase+"') doit renvoyer "
            info += str(n)
            self.assertEqual(rep_exo, n, msg=info)

    def test_random_0_10x(self):
        for i in range(10):
            n = randint(1, 50)
            phrase = get_phrase(n)
            rep_exo = exo.nombre_de_mots(phrase)

            info = "Erreur sur le calcul avec des phrases aleatoires:"
            info += "\n=> nombre_de_mots('"+phrase+"') doit renvoyer "
            info += str(n)
            self.assertEqual(rep_exo, n, msg=info)

    def test_random_1_10x(self):
        for i in range(10):
            n = randint(1, 50)
            phrase = get_phrase(n)
            rep_exo = exo.nombre_de_mots(phrase)

            info = "Erreur sur le calcul avec des phrases aleatoires:"
            info += "\n=> nombre_de_mots('"+phrase+"') doit renvoyer "
            info += str(n)
            self.assertEqual(rep_exo, n, msg=info)

    def test_random_2_10x(self):
        for i in range(10):
            n = randint(1, 50)
            phrase = get_phrase(n)
            rep_exo = exo.nombre_de_mots(phrase)

            info = "Erreur sur le calcul avec des phrases aleatoires:"
            info += "\n=> nombre_de_mots('"+phrase+"') doit renvoyer "
            info += str(n)
            self.assertEqual(rep_exo, n, msg=info)

    def test_random_3_10x(self):
        for i in range(10):
            n = randint(1, 50)
            phrase = get_phrase(n)
            rep_exo = exo.nombre_de_mots(phrase)

            info = "Erreur sur le calcul avec des phrases aleatoires:"
            info += "\n=> nombre_de_mots('"+phrase+"') doit renvoyer "
            info += str(n)
            self.assertEqual(rep_exo, n, msg=info)

    def test_random_4_10x(self):
        for i in range(10):
            n = randint(1, 50)
            phrase = get_phrase(n)
            rep_exo = exo.nombre_de_mots(phrase)

            info = "Erreur sur le calcul avec des phrases aleatoires:"
            info += "\n=> nombre_de_mots('"+phrase+"') doit renvoyer "
            info += str(n)
            self.assertEqual(rep_exo, n, msg=info)


if __name__ == '__main__':
    unittest.main()