from classes.animal.herviboro import Herviboro
from constants import conejoSprite, cellSize

class Conejo(Herviboro):
    def __init__(self, ecosistema):
        self.hp = 60
        self.energy = 50
        self.attack = 10
        self.especie = 'conejo'
        self.attackRange = 2 * cellSize
        self.visionRange = 4 * cellSize
        
        super().__init__(
            conejoSprite,
            self.hp,
            self.energy, 
            self.attackRange, 
            self.visionRange, 
            self.attack, 
            self.especie, 
            ecosistema)