from classes.animal.carnivoro import Carnivoro
from constants import zorroSprite, cellSize

class Zorro(Carnivoro):
    def __init__(self, ecosistema):
        self.hp = 120
        self.energy = 80
        self.attack = 50
        self.especie = 'zorro'
        self.attackRange = 2 * cellSize
        self.visionRange = 4 * cellSize

        super().__init__(
            zorroSprite,
            self.hp,
            self.energy, 
            self.attackRange, 
            self.visionRange, 
            self.attack, 
            self.especie, 
            ecosistema)