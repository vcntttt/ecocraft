from classes.animal.herviboro import Herviboro
from constants import cabraSprite, cellSize

class Cabra(Herviboro):
    def __init__(self, ecosistema):
        self.hp = 80
        self.energy = 60
        self.attack = 10
        self.especie = 'cabra'
        self.attackRange = 2 * cellSize
        self.visionRange = 6 * cellSize
        
        super().__init__(
            cabraSprite,
            self.hp,
            self.energy, 
            self.attackRange, 
            self.visionRange, 
            self.attack, 
            self.especie, 
            ecosistema)