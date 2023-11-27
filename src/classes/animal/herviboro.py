from classes.animal.animal import Animal

class Herviboro(Animal):
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
            speed=0.15):
        
        super().__init__(
            sprite, 
            hp, 
            nrg, 
            1, #nTrofico
            attackRange, 
            visionRange,
            attack, 
            especie, 
            ecosistema,
            speed)