class Fraction:
    """
    Classe utilisée pour représenter des nombres rationnels
    """

    def __init__(self, numerateur, denominateur):
        if denominateur <= 0:
            raise ValueError("hop hop hop : dénominateur > 0 !")
        self.num = numerateur
        self.denom = denominateur

    def __str__(self):
        if self.denom == 1:
            return str(self.num)
        return str(self.num) + " / " + str(self.denom)

    def __eq__(self, autre_fraction):
        return self.num * autre_fraction.denom == self.denom * autre_fraction.num


frac1 = Fraction(2,4)
frac2 = Fraction(10,20)
print(frac2)
print( frac1 == 2/4 )