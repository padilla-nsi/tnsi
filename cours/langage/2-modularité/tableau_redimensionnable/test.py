from tableauRedimensionnable import cree, lit

tab = cree()

tab = {'n': 6, 't': [3, 1, 4, 1, 5, 9, None, None]}
print(tab)
print(lit(tab,3))

