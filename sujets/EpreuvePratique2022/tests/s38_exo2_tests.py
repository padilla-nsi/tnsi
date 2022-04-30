import unittest
import s38.solutions.exo2 as exo
from random import randint, choice, random, Random
from unittest import mock
from io import StringIO


def plus_ou_moins(seed):
    randint     = Random(seed).randint
    nb_mystere = randint(1,99)
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = 1

    while nb_mystere != nb_test and compteur < 10 :
        compteur = compteur + 1
        if nb_mystere > nb_test:
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))

    if nb_mystere == nb_test:
        print ("Bravo ! Le nombre etait ", nb_mystere)
        print("Nombre d'essais: ", compteur)
    else:
        print ("Perdu ! Le nombre etait ", nb_mystere)



class validation(unittest.TestCase):
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_random_1_x20(self, mock_stdout):
        for _ in range(20):
            mock_stdout.truncate(0)
            mock_stdout.seek(0)

            from random import randint
            seed = randint(1, 1000)

            n_max = 9
            nombres = [-1 for _ in range(n_max)]

            exo.randint = Random(seed).randint
            randint     = Random(seed).randint
            
            nombres += [Random(seed).randint(1, 99)]

            with mock.patch('builtins.input', side_effect=nombres):
                exo.plus_ou_moins()
                essai = mock_stdout.getvalue()
            
            mock_stdout.truncate(0)
            mock_stdout.seek(0)

            with mock.patch('builtins.input', side_effect=nombres):
                plus_ou_moins(seed)
                correct = mock_stdout.getvalue()

            self.assertEqual(correct, essai)


    
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_random_2_x20(self, mock_stdout):
        for i in range(20):
            mock_stdout.truncate(0)
            mock_stdout.seek(0)

            from random import randint
            seed = randint(1, 1000)

            n_max = randint(1, 9)
            nombres = [randint(1, 99) for _ in range(n_max)]

            exo.randint = Random(seed).randint
            randint     = Random(seed).randint

            nombres += [Random(seed).randint(1, 99)]    

            with mock.patch('builtins.input', side_effect=nombres):
                exo.plus_ou_moins()
                essai = mock_stdout.getvalue()
            
            mock_stdout.truncate(0)
            mock_stdout.seek(0)

            with mock.patch('builtins.input', side_effect=nombres):
                plus_ou_moins(seed)
                correct = mock_stdout.getvalue()

            self.assertEqual(correct, essai)




if __name__ == '__main__':
    unittest.main()
