from classes.animal.herviboro import Herviboro
from constants import ovejaSprite

class Oveja(Herviboro):
    def __init__(self):
        super().__init__(ovejaSprite)
        self.especie = 'oveja'
        self.rango = 0