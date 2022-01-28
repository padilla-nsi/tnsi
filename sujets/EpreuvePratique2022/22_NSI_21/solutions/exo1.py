def multiplication(n1, n2):
    if n1 == 0 or n2 == 0:
        return 0
    
    if n1 == 1:
        return n2
    
    if n1 > 1:
        return n2 + multiplication(n1 - 1, n2)
    else:
        return multiplication(n1 + 1, n2) - n2

print(multiplication(3, -5))