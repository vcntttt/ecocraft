from classes.planta.planta import Planta
from constants import amapolaSprite

class Amapola(Planta):
    def __init__(self, ecosistema):
        self.hp = 100
        self.energy = 50
        self.attack = 10

        super().__init__(
            amapolaSprite,
            self.hp,
            self.energy,
            ecosistema)