a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], 'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], 'H':['','']}

a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], 'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], 'H':['','']}


def taille(arbre, lettre):
    fils_g = arbre[lettre][0]
    fils_d = arbre[lettre][1]
    
    if fils_g == '' and fils_d == '':
        return 1
    
    if fils_g == '':
        return 1 + taille(arbre, fils_d)

    if fils_d == '':
        return 1 + taille(arbre, fils_g)

    return 1 + taille(arbre, fils_d) + taille(arbre, fils_g)


assert taille(a, 'F') == 9