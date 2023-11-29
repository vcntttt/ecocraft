from classes.animal.herviboro import Herviboro
from constants import nanduSprite, cellSize

class Nandu(Herviboro):
    def __init__(self, ecosistema):
        self.hp = 80
        self.energy = 60
        self.attack = 10
        self.especie = 'nandu'
        self.attackRange = 2 * cellSize
        self.visionRange = 6 * cellSize
        
        super().__init__(
            nanduSprite,
            self.hp,
            self.energy, 
            self.attackRange, 
            self.visionRange, 
            self.attack, 
            self.especie, 
            ecosistema)