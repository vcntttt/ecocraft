from classes.animal.carnivoro import Carnivoro
from constants import cocodriloSprite, cellSize

class Cocodrilo(Carnivoro):
    def __init__(self, ecosistema):
        self.hp = 150
        self.energy = 80
        self.attack = 50
        self.especie = 'cocodrilo'
        self.attackRange = 3 * cellSize
        self.visionRange = 6 * cellSize

        super().__init__(
            cocodriloSprite,
            self.hp,
            self.energy, 
            self.attackRange, 
            self.visionRange, 
            self.attack, 
            self.especie, 
            ecosistema)