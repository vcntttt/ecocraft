from classes.animal.animal import Animal
from classes.animal.herviboro import Herviboro
import math
class Descomponedor(Animal):
    def __init__(self,sprite, hp, nrg, attackRange, visionRange, attack, speed):
        super().__init__(sprite, hp, nrg, 3, attackRange, visionRange, attack, speed)