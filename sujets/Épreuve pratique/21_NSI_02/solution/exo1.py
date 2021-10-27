def moyenne(tab: list):
    assert tab != [], 'erreur'
    
    n = len(tab)
    somme = 0
    for i in range(n):
        somme += tab[i]
    return somme / n

print(moyenne([5,3,8]))
print(moyenne([1,2,3,4,5,6,7,8,9,10]))
# print(moyenne([]))


import unittest


class validation(unittest.TestCase):
    def test_assertion(self):
        self.assertRaises(AssertionError, moyenne, [])

    def test1(self):
        self.assertEqual(moyenne([1,2,3,4,5,6,7,8,9,10]), 5.5)
    
    def test2(self):
        self.assertEqual(moyenne([5, 3, 8]), (5+3+8)/3)

    def test_alea(self):
        def moyenne_sol(tab: list):
            n = len(tab)
            somme = 0
            for i in range(n):
                somme += tab[i]
            return somme / n
        
        from random import randint
        for i in range(1, 100):
            tab = [randint(-100, 100) for _ in range(i)]        
            self.assertEqual(moyenne(tab), moyenne_sol(tab))

# unittest.main()

moyenne([])