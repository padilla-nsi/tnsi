def cree():
    tr = {'n':0 , 't':[None]*8}
    return tr

def lit(tr, i):
    return tr['t'][i]

def ecrit(tr, i, x):
    if i > tr['n'] :
        raise IndexError('Tableau trop petit')
    tr['t'][i] = x 

def ajoute(tr, x):
    capacite = len (tr ['t'])
    taille = tr['n']

    if  capacite == taille :
        _double(tr)

    fin = tr['n']
    tr['t'] [fin] = x 
    tr['n'] += 1

def _double(tr):
    taille = tr['n']
    tmp = [None] * (2 * taille)

    for i in range(taille):
        tmp[i] = tr['t'][i]

    tr['t'] = tmp 