import s40.solutions.exo2 as exo
import unittest 

class validation(unittest.TestCase):

    def correcte(self, nom):
        if nom in exo.resultats:
            notes = exo.resultats[nom]
            total_points = 0
            total_coefficients = 0
            for valeurs  in notes.values():
                note , coefficient = valeurs
                total_points = total_points + note * coefficient
                total_coefficients = total_coefficients + coefficient
            return round(total_points / total_coefficients , 1 )
        else:
            return -1


    def test_present(self):
        self.assertEqual(exo.moyenne('Dupont'), 14.5, msg="\nErreur:\nvaleurs de l'exemple incorrecte avec 'Dupont'")
        self.assertEqual(exo.moyenne('Durand'), 9.2, msg="\nErreur:\nvaleurs de l'exemple incorrecte avec 'Durand'")

    def test_absent(self):
        self.assertEqual(exo.moyenne('Dupond'), -1, msg="\nErreur:\nun nom inconnu doit renvoyer '-1'")


    def test_alea(self):
        from random import randint
        sauv = exo.resultats.copy()
        exo.resultats = {'test':{
                            'DS1' : [randint(0, 20), randint(1, 4)],
                            'DM1' : [randint(0, 20), randint(1, 4)],
                            'DS2' : [randint(0, 20), randint(1, 4)],
                            'PROJET1' : [randint(0, 20), randint(1, 4)],
                            'DS3' : [randint(0, 20), randint(1, 4)]}
                            }


        self.assertEqual(exo.moyenne('test'), self.correcte('test'), msg="\nErreur:\ncalcul de moyenne incorrecte avec" + str(exo.resultats))
        
        exo.resultats = sauv.copy()
        

if __name__=='__main__':
    unittest.main() 