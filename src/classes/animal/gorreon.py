from classes.animal.herviboro import Herviboro
from constants import gorreonSprite, cellSize

class Gorreon(Herviboro):
    def __init__(self, ecosistema):
        self.hp = 100
        self.energy = 50
        self.attack = 10
        self.especie = 'gorren'
        self.attackRange = 2 * cellSize
        self.visionRange = 6 * cellSize
        
        super().__init__(
            gorreonSprite,
            self.hp,
            self.energy, 
            self.attackRange, 
            self.visionRange, 
            self.attack, 
            self.especie, 
            ecosistema)