def fusion(tab1, tab2):
    n1 = len(tab1)
    n2 = len(tab2)
    
    tab_trie = [None] * (n1 + n2)

    i = 0
    j = 0
    for k in range(0, n1 + n2):
        if   i == n1:
            tab_trie[k] = tab2[j]
            j = j + 1
        elif j == n2:
            tab_trie[k] = tab1[i]
            i = i + 1
        elif tab1[i] < tab2[j]:
            tab_trie[k] = tab1[i]
            i = i + 1
        else:
            tab_trie[k] = tab2[j]
            j = j + 1
    
    return tab_trie    


# tests et exemples
tab1 = [1, 2, 3]
tab2 = [1, 2, 3, 4]
tab = fusion(tab1, tab2)
print(tab)

def tri_fusion(tab):
    n = len(tab)

    if n == 0:
        return []
    if n == 1:
        return tab
    
    i_med = n // 2
    
    # tab_gauche = tab[:i_med]
    # tab_droite = tab[i_med:]
    tab_gauche = [tab[i] for i in range(0, i_med)]
    tab_droite = [tab[j] for j in range(i_med, n)]

    tab1 = tri_fusion(tab_gauche)
    tab2 = tri_fusion(tab_droite)

    tab_trie = fusion(tab1, tab2)

    return tab_trie



tab = [2, 1]
tab_trie = tri_fusion(tab)
print(tab_trie)