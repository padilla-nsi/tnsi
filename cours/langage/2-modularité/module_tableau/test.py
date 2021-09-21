from tableau import tranche, concatenation

t1 = [0,2,4,6,8,10]
t2 = [1,3,5,7,9,11]

t3 = tranche(t1,2,5)
t4 = concatenation (t1,t2)

print(t4)