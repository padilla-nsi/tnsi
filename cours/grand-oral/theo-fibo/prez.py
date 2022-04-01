# O(n²)
def fibonacci_rec(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_rec(n-1)+fibonacci_rec(n-2)

# O(n)
def fibonacci_it(n):
    a, b, cpt = 0, 1, 0
    while cpt <= n:
        if cpt < 2:
            c = cpt
        else:
            c = a + b
            a = b
            b = c
        cpt += 1
    return c
