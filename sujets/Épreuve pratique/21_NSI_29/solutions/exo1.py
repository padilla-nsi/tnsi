def calcul(n):
    liste = []
    u0 = n
    while u0 != 1:
        liste.append(u0)
        if u0 % 2 == 0:
            u0 = u0 // 2
        else:
            u0 = 3 * u0 + 1
    liste.append(u0)
    return liste


assert calcul(7) == [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]