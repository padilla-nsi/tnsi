class Maillon:
    def __init__(self, valeur, suivant):
        self.valeur = valeur
        self.suivant = suivant


class File:
    def __init__(self):
        self.tete  = None
        self.queue = None 

    def est_vide(self):
        return self.tete == None

    def enfiler(self, valeur):
        queue = Maillon(valeur, None)

        if self.est_vide():
            self.tete = queue
            self.queue = queue
        else:
            self.queue.suivant = queue
            self.queue = queue
    
    def defiler(self):
        if self.est_vide():
            raise IndexError("defiler sur file vide")
        
        valeur = self.tete.valeur
        self.tete = self.tete.suivant
        return valeur

    def __str__(self):
        """
        Affiche la file.
        
        Exemple :
        la file [4, 3, +, 5, *] sera affichée :
        <<[4, 3, +, 5, *[<
        """
        texte = "<<["
        courant = self.tete
        while courant is not None:
            if len(texte) > 3:
                texte += ', '
            texte += str(courant.valeur)
            courant = courant.suivant        
        texte += "]<"
        return texte


class Pile:
    def __init__(self):
        self.tete = None

    def est_vide(self):
        return self.tete is None

    def empiler(self, valeur):
        sommet = Maillon(valeur, self.tete)
        self.tete = sommet

    def depiler(self):
        if self.est_vide():
            raise IndexError("depiler sur pile vide")
        val = self.tete.valeur
        self.tete = self.tete.suivant
        return val

    def __str__(self):
        """
        Affiche la pile.
        
        Exemple :
        la pile [4, 3, +, 5, *] sera affichée :
        <>[*, 5, +, 3, 4]X
        """
        texte = "<>["
        courant = self.tete
        while courant is not None:
            if len(texte) > 3:
                texte += ', '
            texte += str(courant.valeur)
            courant = courant.suivant        
        texte += "]X"
        return texte




# expression = [4, 3, '+', 5, '*']



saisies = File()
operandes = Pile()

# saisie clavier
saisie = input("Saisir opérateur/opérande (ou rien pour terminer) : ")
while saisie != "":    
    if saisie not in ['+', '-', '*', '/']:
        # cas des opérande (nombres entiers)
        saisie = int(saisie)
    saisies.enfiler(saisie)
    saisie = input("Saisir opérateur/opérande (ou rien pour terminer) : ")


print(f"saisies  : {saisies}")
print(f"operandes: {operandes}")


while not saisies.est_vide():
    symbole = saisies.defiler()
    if symbole not in ['+', '-', '*', '/']:
        # cas des opérandes
        operandes.empiler(symbole)
    else:
        op2 = operandes.depiler()
        op1 = operandes.depiler()
        
        if symbole == '+':
            resultat = op1 + op2
        elif symbole == '*':
            resultat = op1 * op2
        elif symbole == '/':
            resultat = op1 / op2
        else:
            resultat = op1 - op2

        operandes.empiler(resultat)

    print(f"saisies  : {saisies}")
    print(f"operandes: {operandes}")

print(operandes.depiler())