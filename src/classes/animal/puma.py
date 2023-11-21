from classes.animal.carnivoro import Carnivoro
from constants import pumaSprite, cellSize

class Puma(Carnivoro):
    def __init__(self):
        super().__init__(pumaSprite)
        self.especie = 'puma'
        self.attackRange = 2 * cellSize