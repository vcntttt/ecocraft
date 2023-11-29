from classes.animal.carnivoro import Carnivoro
from constants import pumaSprite, cellSize

class Puma(Carnivoro):
    def __init__(self, ecosistema):
        self.hp = 150
        self.energy = 80
        self.attack = 50
        self.especie = 'puma'
        self.attackRange = 3 * cellSize
        self.visionRange = 6 * cellSize

        super().__init__(
            pumaSprite,
            self.hp,
            self.energy, 
            self.attackRange, 
            self.visionRange, 
            self.attack, 
            self.especie, 
            ecosistema)