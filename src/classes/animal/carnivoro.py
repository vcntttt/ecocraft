from classes.animal.animal import Animal

class Carnivoro(Animal):
    def __init__(self,sprite):
        super().__init__(sprite)
        self.tipo = 1