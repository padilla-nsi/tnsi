# Importation des modules string, turtle et time.
import string
import turtle
import time


# La classe "L_Systeme" prend en attribut un axiome, un ensemble de règles, un angle et un nombre de générations en entrée et renvoie
# une chaîne de caractères représentant le L-Systeme et un dessin du L-Systeme
class L_Systeme():
    def __init__(self, axiome, regles, angle):
        """
        La fonction __init__() est une fonction spéciale dans les classes Python. Il est connu comme un
        constructeur dans les concepts orientés objet. Cette fonction est appelée lorsqu'un objet est créé à
        partir d'une classe et elle permet à la classe d'initialiser les attributs de la classe
      
        Args:
          axiome: la chaîne de départ
          regles: un dictionnaire de règles, où la clé est le caractère à remplacer et la valeur est la
        chaîne de remplacement.
          angle: l'angle de rotation de chaque branche
        """
        self.axiome = axiome
        self.regles = regles
        self.angle = angle
        
    
    def generation(self, n):
        """
        La fonction prend une chaîne comme axiome, un dictionnaire comme règle et un entier comme nombre
        de générations. Il renvoie une chaîne des nième générations
        
        Args:
          n: le nombre de générations
        
        Returns:
          La chaîne de l'axiome
        """
        t0 = time.time()
        gen_p = self.axiome
        for _ in range(n):
            gen_s = ''.join(self.regles.get(c, c) for c in gen_p)
            gen_p = gen_s
        print(gen_s)
        print(f'Code en {time.time()-t0} secondes')
        return gen_s
    
    def construction(self, n, pas = 10,  position_initiale = (-850, -450), orientation_initial = 270):
        """
        Dessine un fractal en utilisant un système Lindenmayer
        
        Args:
          n: le nombre d'itérations
          pas: la longueur de chaque segment de ligne. 10 par défaut
          position_initiale: La position initiale de la tortue.
          orientation_initial: L'orientation initiale de la tortue. 270 par défaut
        """
        t0 = time.time()
        t = turtle.Turtle()
        wn = turtle.Screen()
        wn.bgcolor('black')

        t.color('orange')
        t.pensize(1)
        t.penup()
        t.setpos(position_initiale)
        t.pendown()
        t.speed(0)
        
        mot = self.generation(n)
        def show(j):
            count = len(mot)-2
            x = int(60*j/count)
            print("\r%s[%s%s] %i/%i\r" % (f'{round((i/(len(mot)-2))*100)}% ', "#"*x, "."*(60-x), j, count), end="")
        t.penup()
        t.setheading(orientation_initial)
        t.pendown()
        pile = []
        i = 0
        print("mot:", mot)
        for c in mot:
            if c in string.ascii_letters:
                t.bk(pas)
            elif c == '+':
                t.right(self.angle)
            elif c == '-':
                t.left(self.angle)
            elif c == '[':
                pile.append([t.position (), t.heading ()])
            elif c == ']':
                pos, cap = pile.pop()
                t.penup()
                t.goto(pos)
                t.setheading(cap)
                t.pendown()
            show(i)
            i += 1
        print(f'\nDessin en {time.time()-t0} secondes')
        wn.exitonclick()


# Création d'un L-Systeme avec l'axiome 'A', les règles {'A':'B+A+B', 'B': 'A-B-A'} et l'angle 60.
# Affichage du L-Systeme avec 5 générations.
sierpinski_arrowhead_flocon_de_koch = L_Systeme('B', {'A':'A-A++A-A', 'B':'A++A++A'} , 60)
sierpinski_arrowhead_courbe_de_koch = L_Systeme('B', {'A':'A-A++A-A', 'B':'A'} , 60)
sierpinski_arrowhead_t = L_Systeme('A', {'A':'B+A+B', 'B': 'A-B-A'} , 60)

print(sierpinski_arrowhead_flocon_de_koch.construction(1,pas=50, position_initiale=(0,0)))

