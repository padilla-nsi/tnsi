def rendu(somme_a_rendre):
    n1, n2, n3 = 0, 0, 0
    while somme_a_rendre >= 5:
        n1 += 1
        somme_a_rendre -= 5
    while somme_a_rendre >= 2:
        n2 += 1
        somme_a_rendre -= 2
    while somme_a_rendre >= 1:
        n3 += 1
        somme_a_rendre -= 1
    return [n1, n2, n3]


import unittest

class correction(unittest.TestCase):
    def test_13(self):
        self.assertEqual(rendu(13), [2,1,1])

    def test_64(self):
        self.assertEqual(rendu(64), [12,2,0])

    def test_89(self):
        self.assertEqual(rendu(89), [17,2,0])

    def test_alea(self):
        from random import randint
        n = randint(100, 10_000)
        n1, n2, n3 = rendu(n)
        self.assertEqual(n1*5 + n2*2 + n3, n)
        

if __name__ == '__main__':
    unittest.main()