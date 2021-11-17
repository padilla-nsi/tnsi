
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



# File avec liste chaînée mutable


class Maillon:
    """ Maillon d'une liste chaînée """
    def __init__(self, valeur, suivant):
        self.valeur  = valeur
        self.suivant = suivant

class File:
    def __init__(self):
        """
        Exemples et tests:
        >>> f = File()
        >>> print(f.tete)
        None
        >>> print(f.queue)
        None
        """
        self.tete  = None
        self.queue = None


    def est_vide(self):
        """
        Est ce que la file est vide?

        Returns:
            bool: True ssi la file est vide
        
        Exemples et tests:
        >>> f = File()
        >>> print(f.est_vide())
        True
        >>> f.tete = Maillon(1, None)
        >>> print(f.est_vide())
        False
        """
        return self.tete is None
    

    def enfiler(self, valeur):
        """
        Ajoute la valeur à la fin de la file

        Args:
            valeur (T): valeur à ajouter
        
        Exemples et tests:
        >>> f = File()
        >>> f.enfiler(1)
        >>> print(f.tete.valeur)
        1
        >>> print(f.queue.valeur)
        1
        >>> f.enfiler(2)
        >>> f.enfiler(3)
        >>> print(f.tete.valeur)
        1
        >>> print(f.queue.valeur)
        3
        """
        nouveau = Maillon(valeur, None)

        if self.est_vide():
            self.tete = nouveau
        else:
            self.queue.suivant = nouveau
        
        self.queue = nouveau


    def defiler(self):
        """
        Supprime et renvoie le premier élément de la file

        Raises:
            IndexError: si la file est vide

        Returns:
            T: valeur du premier élément de la file
        
        Exemples et tests:
        >>> f = File()
        >>> f.enfiler(1)
        >>> f.enfiler(2)
        >>> f.enfiler(3)
        >>> print( f.defiler() )
        1
        >>> assert f.queue.valeur == 3
        >>> print( f.defiler() )
        2
        >>> assert f.queue.valeur == 3
        >>> print( f.defiler() )
        3
        >>> assert f.tete  == None
        >>> assert f.queue == None
        >>> f.defiler()
        Traceback (most recent call last):
        IndexError: defiler sur une file vide
        """
        if self.est_vide():
            raise IndexError("defiler sur une file vide")
        
        valeur = self.tete.valeur
        self.tete = self.tete.suivant

        if self.tete is None:
            self.queue = None

        return valeur


    



# activité
# implémentation de Pile avec les `list` Python

class Pile:
    def __init__(self):
        """        
        Exemples et tests :
        >>> p = Pile()
        >>> print(p.contenu)
        []
        """
        self.contenu = []
    
    def est_vide(self):
        """
        Exemples et tests :
        >>> p = Pile()
        >>> print(p.est_vide())
        True
        """
        return self.contenu == []
    
    def empiler(self, valeur):
        """
        Exemples et tests :
        >>> p = Pile()
        >>> p.empiler(1)
        >>> print(p.est_vide())
        False
        >>> print(p.contenu)
        [1]
        >>> p.empiler(2)
        >>> p.empiler(3)
        >>> print(p.contenu)
        [1, 2, 3]
        """
        self.contenu.append(valeur)

    def depiler(self):
        """
        Exemples et tests :
        >>> p = Pile()
        >>> p.empiler(1)
        >>> p.empiler(2)
        >>> p.empiler(3)
        >>> v = p.depiler()
        >>> print(v)
        3
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
        return self.contenu.pop()



if __name__ == '__main__':
    from doctest import testmod
    testmod(verbose=False)