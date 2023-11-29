from classes.planta.planta import Planta
from constants import girasolSprite

class Girasol(Planta):
    def __init__(self, ecosistema):
        self.hp = 100
        self.energy = 50
        self.attack = 10

        super().__init__(
            girasolSprite,
            self.hp,
            self.energy,
            ecosistema)