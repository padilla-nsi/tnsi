import unittest
import s36.solutions.exo2 as exo


from random import randint



from math import sqrt   # import de la fonction racine carrée

def distance(point1, point2): 
    """ Calcule et renvoie la distance entre deux points. """
    return sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

def plus_courte_distance(tab, depart):
    """ Renvoie le point du tableau tab se trouvant à la plus     
    courte distance du point depart."""
    point = tab[0]
    min_dist = distance(point, depart)
    for i in range (1, len(tab)):
        if distance(tab[i], depart) < min_dist:
            point = tab[i]
            min_dist = distance(tab[i], depart)
    return point



class validation(unittest.TestCase):
    def test_distance_assert_tuple1(self):
        a, b, c, d = [randint(-100, 100) for _ in range(4)]
        self.assertRaises( AssertionError, exo.distance, [a, b], (c, d) )
        self.assertRaises( AssertionError, exo.distance, (a, b), [c, d] )

    def test_distance_assert_couple(self):
        a, b, c, d, e = [randint(-100, 100) for _ in range(5)]
        self.assertRaises(AssertionError, exo.distance, (a, b, c), (d, e))
        self.assertRaises(AssertionError, exo.distance, (a, b), (c, d, e))
    
    def test_distance_assert_int(self):
        a = chr(randint(65, 90))
        n1, n2, n3 = [randint(-100, 100) for _ in range(3)]
        self.assertRaises(AssertionError, exo.distance, (a, n1), (n2, n3))
        self.assertRaises(AssertionError, exo.distance, (n1, a), (n2, n3))
        self.assertRaises(AssertionError, exo.distance, (n1, n2), (a, n3))
        self.assertRaises(AssertionError, exo.distance, (n1, n2), (n3, a))
    
    def test_exemple_enonce_1(self):
        tab = [(7, 9), (2, 5), (5, 2)]
        point = (0, 0)
        rep = (2, 5)
        self.assertEqual(exo.plus_courte_distance(tab, point), rep)

        
    def test_exemple_enonce_2(self):
        point1 = (1, 0)
        point2 = (5, 3)
        rep = 5
        self.assertEqual(exo.distance(point1, point2), rep)


    def test_random_plus_courte_distance(self):
        for _ in range(50):
            n = randint(1, 20)
            tab = [(randint(0, 15), randint(0, 15)) for _ in range(n)]
            point = ( (randint(0, 15), randint(0, 15)) )
            rep = plus_courte_distance(tab, point)
            self.assertEqual(exo.plus_courte_distance(tab, point), rep)

    def test_random_distance(self):
        point1 = ( (randint(0, 15), randint(0, 15)) )
        point2 = ( (randint(0, 15), randint(0, 15)) )
        rep = distance(point1, point2)
        self.assertEqual(exo.distance(point1, point2), rep)



if __name__ == '__main__':
    unittest.main()
