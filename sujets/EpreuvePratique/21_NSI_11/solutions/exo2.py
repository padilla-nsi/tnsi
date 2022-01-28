def tri_bulles(T):
    n = len(T)
    for i in range(n-1, -1, -1):
        for j in range(i):
            if T[j] > T[j+1]:
                temp = T[j]
                T[j] = T[j+1]
                T[j+1] = temp
    return T


def tri_bulles(T):
    n = len(T)
    for i in range(n-1):
        for j in range(n-1-i):
            if T[j] > T[j+1]:
                temp = T[j]
                T[j] = T[j+1]
                T[j+1] = temp
    return T


assert tri_bulles([10, 4, 3, 9, -10, 100]) == [-10, 3, 4, 9, 10, 100]