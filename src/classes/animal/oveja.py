from classes.animal.herviboro import Herviboro
from constants import ovejaSprite

class Oveja(Herviboro):
    def __init__(self):
        self.especie = 'oveja'
        self.rango = 0
        self.sprite = ovejaSprite
        super().__init__(self.sprite)