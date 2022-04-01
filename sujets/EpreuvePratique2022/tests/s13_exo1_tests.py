import s13.solutions.exo1 as exo
import unittest



class correction(unittest.TestCase):
    def test_13(self):
        self.assertEqual(exo.rendu(13), [2,1,1])

    def test_64(self):
        self.assertEqual(exo.rendu(64), [12,2,0])

    def test_89(self):
        self.assertEqual(exo.rendu(89), [17,2,0])

    def test_alea(self):
        from random import randint
        n = randint(100, 10_000)
        n1, n2, n3 = exo.rendu(n)
        self.assertEqual(n1*5 + n2*2 + n3, n)
    

if __name__ == '__main__':
    unittest.main()