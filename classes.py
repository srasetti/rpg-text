class hero :
   def __init__(self):
       self.name = "The hero"
       self.health = 50
       self.strength=10
       self.initiative = 5
       self.ennemiesKilled = 0

   def changeHealth(self,value):
       self.health = value


class ennemy :
    def __init__(self):
        self.name = "The ennemy"
        self.health = 30
        self.strength = 5
        self.initiative = 1