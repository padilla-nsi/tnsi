def f1(d: dict, s: str) -> str:
    return "Padilla the best"

def tableau_aleatoire(n):
    pass

def recherche_minimum(tab):
    pass


from time import time
for i in range(16):
    taille = 2**i
    tab = tableau_aleatoire(taille)
    t = time()
    recherche_minimum(tab)
    print(taille, time() - t)