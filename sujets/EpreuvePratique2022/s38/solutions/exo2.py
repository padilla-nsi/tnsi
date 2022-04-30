"""
Author: Pascal Padilla
Source: correction de l'exercice 2 du sujet 38 des épreuves pratiques NSI 2022

Remarques:
    * ERREUR dans l'énoncé: attention dans les affichages à la fin.
    Dans l'énoncé on peut lire `était` et dans le fichier .py on lit `etait`.
    Pour les tests, j'ai fait comme le fichier : sans accent
    * dans `randint(a, b)`, b est INCLUS ! ce n'est pas comme `range(a, b)` !!!
    * pour pouvoir tester, ajouter un affichage pour tricher qui montre
    le nombre mystère... /!\ :supprimer cet affichage pour les TESTS automatisés ;)
"""


from random import randint

def plus_ou_moins():
    # nb aléatoire entre 1 et 99 inclus
    nb_mystere = randint(1, 99)

    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    # -> invariant: compteur est le nombre d'essais effectués
    # -> initialisation: premier essai
    compteur = 1

    # -> condition d'arrêt:
    #   * le nombre est trouvé
    #   * le compteur arrive à 10 essais effectués 
    while nb_mystere != nb_test and compteur < 10 :

        compteur = compteur + 1
        # cas d'un essai inférieur au nb mystère
        if nb_mystere > nb_test:
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))

    if nb_mystere == nb_test:
        # affichage du nombre mystère
        print ("Bravo ! Le nombre etait ", nb_mystere)
        # et du nombre de tentatives
        print("Nombre d'essais: ", compteur)
    else:
        # affichage du nombre mystère
        print ("Perdu ! Le nombre etait ", nb_mystere)


# vérification avec des essais dans le terminal
# plus_ou_moins()
