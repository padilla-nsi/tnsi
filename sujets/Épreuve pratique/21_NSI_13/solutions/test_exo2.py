import exo2 as exo
import unittest

from unittest import mock
from random import Random
from io import StringIO





class validation(unittest.TestCase):

    
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test1(self, mock_stdout): 
        mock_stdout.truncate(0)
        mock_stdout.seek(0)
        
        from random import randint

        n_max = 9

        nombres = [-1 for _ in range(n_max)]

        seed = randint(1, 1000)
        
        exo.randint = Random(seed).randint
        randint     = Random(seed).randint
        
        nombres += [Random(seed).randint(1, 99)]


        def plus_ou_moins_ok():
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
                print ("Bravo ! Le nombre était ", nb_mystere)
                print("Nombre d'essais: ", compteur)
            else:
                print ("Perdu ! Le nombre était ", nb_mystere)


        with mock.patch('builtins.input', side_effect=nombres):
            exo.plus_ou_moins()
            essai = mock_stdout.getvalue()
        
        mock_stdout.truncate(0)
        mock_stdout.seek(0)

        with mock.patch('builtins.input', side_effect=nombres):
            plus_ou_moins_ok()
            correct = mock_stdout.getvalue()

        self.assertEqual(correct, essai)


    
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test2(self, mock_stdout):        
        mock_stdout.truncate(0)
        mock_stdout.seek(0)

        from random import randint

        n_max = randint(1, 9)

        nombres = [randint(1, 99) for _ in range(n_max)]

        seed = randint(1, 1000)
        
        exo.randint = Random(seed).randint
        randint     = Random(seed).randint
        
        nombres += [Random(seed).randint(1, 99)]


        def plus_ou_moins_ok():
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
                print ("Bravo ! Le nombre était ", nb_mystere)
                print("Nombre d'essais: ", compteur)
            else:
                print ("Perdu ! Le nombre était ", nb_mystere)

    

        with mock.patch('builtins.input', side_effect=nombres):
            exo.plus_ou_moins()
            essai = mock_stdout.getvalue()
        
        mock_stdout.truncate(0)
        mock_stdout.seek(0)

        with mock.patch('builtins.input', side_effect=nombres):
            plus_ou_moins_ok()
            correct = mock_stdout.getvalue()

        self.assertEqual(correct, essai)


unittest.main()