import s13.solutions.exo2 as exo
import unittest


class correction(unittest.TestCase):
    def test_creation(self):
        F = exo.File()
        self.assertEqual(F.est_vide(), True)

    def test_enfile(self):
        F = exo.File()
        F.enfile(2)
        self.assertEqual(F.est_vide(), False)

    def test_defile(self):
        F = exo.File()
        F.enfile(2)
        F.enfile(5)
        F.enfile(7)
        self.assertEqual(F.defile(), 2)
        self.assertEqual(F.defile(), 5)
        self.assertEqual(F.defile(), 7)
        self.assertEqual(F.est_vide(), True)


    def test_alea(self):
        from random import randint
        n = 1000
        tab = [randint(-1000, 1000) for _ in range(n)]
        F = exo.File()
        for x in tab:
            F.enfile(x)
            self.assertEqual(F.est_vide(), False)
        for x in tab:
            self.assertEqual(x, F.defile())
        self.assertEqual(F.est_vide(), True)


if __name__ == '__main__':
    unittest.main()
