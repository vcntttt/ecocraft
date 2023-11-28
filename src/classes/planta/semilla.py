from classes.organismo import Organismo
from constants import *
import random
class Semilla(Organismo):
    def __init__(self, ecosistema):
        self.ecosistema = ecosistema
        self.crecimientoTime = 40
        self.crecimientoProgress = 0
        super().__init__(
            seedSprite,
            1,
            1,
            0
        )
        self.status = 'seed'
    def update(self,orgs):
        self.crecimientoProgress += 1
        self.drawBar(lighBlue, self.crecimientoProgress, self.crecimientoTime)
        if self.crecimientoProgress >= self.crecimientoTime:
            self.transformar()

    def transformar(self):
        from classes.planta.planta import Planta
        if random.randint(0,3) == 0:
            newPlanta = Planta(self.ecosistema)
            newPlanta.rect.topleft = self.rect.topleft
            self.ecosistema.newOrg(newPlanta)
            self.kill()