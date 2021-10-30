def recherche(caractere: str, mot: str) -> int:
    total = 0
    for c in mot:
        if c == caractere:
            total = total + 1
    return total

assert recherche('e', "sciences") == 2
assert recherche('i',"mississippi") == 4
assert recherche('a',"mississippi") == 0