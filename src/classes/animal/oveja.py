from classes.animal.herviboro import Herviboro
from constants import ovejaSprite, cellSize

class Oveja(Herviboro):
    def __init__(self, ecosistema):
        self.hp = 100
        self.energy = 50
        self.attack = 10
        self.especie = 'oveja'
        self.attackRange = 2 * cellSize
        self.visionRange = 6 * cellSize
        
        super().__init__(
            ovejaSprite,
            self.hp,
            self.energy, 
            self.attackRange, 
            self.visionRange, 
            self.attack, 
            self.especie, 
            ecosistema)