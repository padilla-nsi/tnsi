from dates import cree, contient, ajoute
from random import randint


def contient_doublon(t):
    """le tableau t contient-il un doublon ?"""
    s = cree()
    for x in t:
        if contient(s,x):
            return True
        ajoute(s,x)
    return False


n_doublons = 0

for _ in range(1000):
    t = [None] * 23
    for j in range(23):
        t[j] = randint(1,365)
    if contient_doublon(t):
        n_doublons += 1

print (n_doublons,"doublons sur 1000 tirages")
print ("fréquence : ", n_doublons/1000)