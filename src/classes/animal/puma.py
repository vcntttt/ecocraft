from classes.animal.carnivoro import Carnivoro
from constants import pumaSprite
class Puma(Carnivoro):
    def __init__(self):
        self.especie = 'puma'
        self.rango = 2
        self.sprite = pumaSprite
        super().__init__(self.sprite)