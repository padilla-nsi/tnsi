import s32.solutions.exo2 as exo
import unittest

class Validation(unittest.TestCase):

    def test_constructeur(self):
        """ vérifie que le constructeur est correct """
        try:
            exo.AdresseIP('192.0.0.1')
        except:
            raise EnvironmentError('\nErreur: \nconstructeur AdresseIP() invalide')
        
        adresse1 = exo.AdresseIP('192.168.0.1')
        self.assertIsInstance(adresse1, exo.AdresseIP, msg="\nErreur:\nconstucteur non valide")
        self.assertEqual(adresse1.adresse, '192.168.0.1', 
                        msg="\nErreur:\nattribut 'adresse' non conforme")

    def test_liste_octet(self):
        try:
            adresse1 = exo.AdresseIP('192.0.0.1')
            liste = adresse1.liste_octet()
        except:
            raise EnvironmentError("\nErreur: \nméthode 'liste_octet()' inaccessible")
        
        self.assertIsInstance(liste, list, msg="\nErreur:\n'liste_octet()' ne renvoie pas un type 'list'")

    def test_est_reservee(self):
        try:
            adresse1 = exo.AdresseIP('192.168.0.1')
            reservee = adresse1.est_reservee()
        except:
            raise EnvironmentError("\nErreur: \nméthode 'est_reservee()' inaccessible")

        self.assertIsInstance(reservee, bool,
                    msg="\nErreur:\nméthode 'est_reservee()' ne renvoie pas un booléen")
        for adr in range(1,255):
            ip = '192.168.0.' + str(adr)
            self.assertFalse(exo.AdresseIP(ip).est_reservee(),
                    msg="\nErreur:\nl'adresse "+ip+" ne doit pas être réservée")
        for adr in [0, 255]:
            ip = '192.168.0.' + str(adr)
            self.assertTrue(exo.AdresseIP(ip).est_reservee(),
                    msg="\nErreur:\nl'adresse "+ip+" doit être réservée")

        
    def test_adresse_suivante(self):
        try:
            adresse1 = exo.AdresseIP('192.168.0.1')
            adresse2 = adresse1.adresse_suivante()
        except:
            raise EnvironmentError("\nErreur: \nméthode 'adresse_suivante()' inaccessible")


        for adr in range(254):
            ip = '192.168.0.' + str(adr)
            adresse = exo.AdresseIP(ip)
            adresse_suiv = adresse.adresse_suivante()
            ip_suiv = adresse_suiv.adresse
            ip_suiv_ok = ip = '192.168.0.' + str(adr+1)

            self.assertEqual(ip_suiv, ip_suiv_ok, 
                    msg="\nErreur:\nadresse suivante non conforme")
        
if __name__ == '__main__':
    unittest.main()