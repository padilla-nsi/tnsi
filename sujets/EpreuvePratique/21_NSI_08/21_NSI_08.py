pieces = [100,50,20,10,5,2,1]                           # modification sujet
def rendu_glouton(arendre, solution=[], i=0):
       if arendre == 0:
       return ...
    p = pieces[i]
    if p <= ... :
        solution.append(...)                            # modification sujet
        return rendu_glouton(arendre - p, solution,i)   # modification sujet
    else :
        return rendu_glouton(arendre, solution, ...)
