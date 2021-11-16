def tri_bulle(tab):
    for i in range(len(tab)):
        for j in range(len(tab)- 1 - i):
            if tab[j] > tab[j+1]:
                tab[j], tab[j+1] = tab[j+1], tab[j]

tab = [9,9,8,7,6,5,4] 
tri_bulle(tab)

def tri_insertion(tab: list):
    pass

def tri_selection(tab: list):
    for i in range(len(tab)-1):
        mini = tab[i]
        for j in range(i, len(tab)):
            if tab[j] < mini:
                mini, tab[j] = tab[j], mini
        tab[i] = mini

tab = [9,9,8,7,6,5,4] 
tri_selection(tab)
tab