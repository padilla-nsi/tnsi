

def occurrence_max(chaine):
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    occurrence = [0] * 26

    for lettre in chaine:
        if lettre not in alphabet:
            continue

        i = 0
        while alphabet[i] != lettre:
            i = i + 1
        occurrence[i] = occurrence[i] + 1

    i_max = 0
    v_max = occurrence[0]

    for i in range(26):
        if occurrence[i] > v_max:
            i_max = i
            v_max = occurrence[i]

    return alphabet[i_max]


# version avec dictionnaire
# plus classique
def occurrence_max_dic(chaine):
    occurrence = {}
    for lettre in chaine:
        if lettre == ' ': continue

        if lettre in occurrence:
            occurrence[lettre] += 1
        else:
            occurrence[lettre] = 1
    
    v_max = -1
    for lettre in occurrence:
        if occurrence[lettre] > v_max:
            lettre_max = lettre
            v_max = occurrence[lettre]
    
    return lettre_max




ch = 'je suis en terminale et je passe le bac et je souhaite poursuivre des etudes pour devenir expert en informatique'
assert occurrence_max_dic(ch) == 'e'
from random import randint
alea = ' '.join([chr(randint(97,110)), chr(randint(97,110)), chr(randint(97,110)), chr(randint(97,110)), chr(randint(97,110)), chr(randint(97,110)), chr(randint(97,110)), chr(randint(97,110)), chr(randint(97,110)), chr(randint(97,110)), chr(randint(97,110)), chr(randint(97,110)), chr(randint(97,110)), chr(randint(97,110)), chr(randint(97,110)), chr(randint(97,110)), chr(randint(97,110)), chr(randint(97,110)), chr(randint(97,110)), chr(randint(97,110))])
print(alea)
print(occurrence_max(alea))
