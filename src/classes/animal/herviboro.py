from classes.animal.animal import Animal
from classes.planta.planta import Planta
class Herviboro(Animal):
    def __init__(self,sprite, hp, nrg, attackRange, visionRange, attack):
        super().__init__(sprite, hp, nrg, 1, attackRange, visionRange, attack)
