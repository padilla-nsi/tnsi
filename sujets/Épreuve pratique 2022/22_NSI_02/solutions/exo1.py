def moyenne(tab):
    somme = 0
    somme_coef = 0
    for couple in tab:
        note = couple[0]
        coefficient = couple[1]
        somme = somme + note*coefficient
        somme_coef = somme_coef + coefficient
    return somme / somme_coef


assert moyenne([(15,2),(9,1),(12,3)]) == 12.5
assert moyenne([(10, 2)]) == 10