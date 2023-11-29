from classes.planta.planta import Planta
from constants import matorralSprite

class Matorral(Planta):
    def __init__(self, ecosistema):
        self.hp = 100
        self.energy = 50
        self.attack = 10

        super().__init__(
            matorralSprite,
            self.hp,
            self.energy,
            ecosistema)