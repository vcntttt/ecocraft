from classes.animal.herviboro import Herviboro
from constants import ovejaSprite, cellSize

class Oveja(Herviboro):
    def __init__(self):
        self.hp = 100
        self.energy = 50
        self.attack = 10
        self.especie = 'oveja'
        self.attackRange = 0 * cellSize
        self.visionRange = 2 * cellSize
        super().__init__(ovejaSprite, self.hp, self.energy, self.attackRange, self.visionRange)