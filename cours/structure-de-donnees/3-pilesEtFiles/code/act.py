
def creer_pile():
    """
    structure de pile avec les tableaux dynamiques pythons list
    """
    return []

def est_vide(pile):
    return pile == []

def empiler(pile, element):
    pile.append(element)

def depiler(pile):
    assert pile != []
    return pile.pop()


def creer_file():
    """
    structure de file avec les tableaux dynamiques python : list
    """
    return []

def enfiler(file, element):
    file.append(element)

def defiler(file):
    return file.pop(0)


# exemple de pile d'appel : bouton retour du navigateur Web

def aller_a(adresse_cible):
    global adresse_courante # j'aime pas, mauvais exemple....
    empiler(adresses_precedentes, adresse_courante)
    adresse_courante = adresse_cible

def retour():
    global adresse_courante # j'aime pas, mauvais exemple....
    if not est_vide(adresses_precedentes):
        adresse_courante = depiler(adresses_precedentes)


adresse_courante = ""
adresses_precedentes = creer_pile()

print(adresse_courante, adresses_precedentes)
aller_a("amada.fr")
print(adresse_courante, adresses_precedentes)
aller_a("bertrand.com")
print(adresse_courante, adresses_precedentes)
aller_a("cherine.org")
print(adresse_courante, adresses_precedentes)

retour()
print(adresse_courante, adresses_precedentes)
retour()
print(adresse_courante, adresses_precedentes)


# exemple d'utilisation des files : la bataille

paquet_amada = creer_file()
paquet_bertrand = creer_file()

# distribution

def tour():
    # si le joueur n'a plus de carte, il perd
    if est_vide(paquet_amada):
        print("Amada perd")
    
    else:

        a = defiler(paquet_amada)
        b = defiler(paquet_bertrand)
        if valeur(a) > valeur(b):
            # amada gagne les cartes
            enfiler(paquet_amada, a)
            enfiler(paquet_amada, b)
        elif valeur(a) < valeur(b):
            enfiler(paquet_bertrand, b)
            enfiler(paquet_bertrand, a)
        ...


class Maillon:
    """ Maillon d'une liste chaînée """
    def __init__(self, valeur, suivant):
        self.valeur  = valeur
        self.suivant = suivant

class Pile:
    """
    Encapsulation des piles à l'aide des Maillons de listes chaînées.
    """
    def __init__(self):
        """
        Constructeur de Pile.

        Exemple et tests:
        >>> p = Pile()
        >>> print(p.contenu)
        None
        """
        self.contenu = None

    def est_vide(self) -> bool:
        """
        Est ce que la pile est vide ?

        Returns:
            bool: True si et seulement si la pile est vide

        Exemple et test:
        >>> p = Pile()
        >>> print(p.est_vide())
        True
        >>> p.contenu = Maillon(1, None)
        >>> print(p.est_vide())
        False
        """
        return self.contenu is None


    def empiler(self, valeur):
        """
        Empile valeur dans la pile courante.

        Args:
            valeur (T): valeur à empiler

        Exemple et tests:
        >>> p = Pile()
        >>> p.empiler(1)
        >>> assert not p.est_vide()
        >>> print(p.contenu.valeur)
        1
        >>> p.empiler(2)
        >>> print(p.contenu.valeur)
        2
        """
        tete_courante = self.contenu
        tete_nouvelle = Maillon(valeur, tete_courante)
        self.contenu = tete_nouvelle

        # version courte ;)
        # self.contenu = Maillon(valeur, self.contenu)

    def depiler(self):
        """
        Dépile la valeur de tête de la pile.

        Raises:
            IndexError: si la pile est vide

        Returns:
            T: valeur de tête de la pile

        Exemple et tests:
        >>> p = Pile()
        >>> p.empiler(1)
        >>> p.empiler(2)
        >>> v = p.depiler()
        >>> print(v)
        2
        >>> v = p.depiler()
        >>> print(v)
        1
        >>> v = p.depiler()
        Traceback (most recent call last):
        IndexError: depiler sur une pile vide
        """
        if self.est_vide():
            raise IndexError("depiler sur une pile vide")
        
        tete = self.contenu
        valeur_tete = tete.valeur
        maillon_suivant = tete.suivant
        self.contenu = maillon_suivant
        
        return valeur_tete


if __name__ == '__main__':
    from doctest import testmod
    testmod(verbose=False)