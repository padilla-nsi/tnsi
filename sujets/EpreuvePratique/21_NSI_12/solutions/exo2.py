def recherche(gene, seq_adn):
    n = len(seq_adn)
    g = len(gene)
    i = 0
    trouve = False
    while i < n - g + 1 and trouve == False :
        j = 0
        while j < g and gene[j] == seq_adn[i+j]:
            j = j + 1
        if j == g:
            trouve = True
        i = i + 1
    return trouve


assert recherche("AATC", "GTACAAATCTTGCC") == True
assert recherche("AGTC", "GTACAAATCTTGCC") == False


from random import choice

T = [choice(['A','G','T','C']) for _ in range(10)]
print(T)