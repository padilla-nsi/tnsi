class Chrono:
    """
    Une classe pour représenter un temps mesuré
    en heures, minutes et secondes."""
    def __init__(self, h, m, s):
        self.heures = h
        self.minutes = m
        self.secondes = s

    def texte(self):
        return (  str(self.heures)   + 'h '
                + str(self.minutes)  + 'min '
                + str(self.secondes) + 's'   )

    def avance(self, s):
        """Avance un chrono de s secondes

        Args:
            s (int): nombre de seconde à ajouter
        """
        self.secondes += s
        
        # dépassement secondes
        self.minutes += self.secondes // 60
        self.secondes = self.secondes %  60

        # dépassement minutes
        self.heures += self.minutes // 60
        self.minutes = self.minutes %  60

t = Chrono(24,59,56)
print( t.texte() )
t.avance(12005)
print(t.texte())