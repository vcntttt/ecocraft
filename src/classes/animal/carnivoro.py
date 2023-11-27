from classes.animal.animal import Animal
from classes.animal.herviboro import Herviboro
import math
class Carnivoro(Animal):
    def __init__(
            self,
            sprite, 
            hp, 
            nrg, 
            attackRange, 
            visionRange, 
            attack, 
            especie, 
            ecosistema,
            speed=0.15, ):
        
        super().__init__(
            sprite, 
            hp, 
            nrg, 
            2, #nTrofico
            attackRange, 
            visionRange, 
            attack, 
            especie, 
            ecosistema,
            speed)