from classes.organismo import Organismo
from classes.planta.semilla import Semilla
from constants import *
import random
class Planta (Organismo):
    def __init__(self,ecosistema):
        self.reproduccionNRG = 50
        self.reproduccionTime = 40
        self.reproduccionProgress = 0
        self.ecosistema = ecosistema
        self.enReposo = False
        super().__init__(
            plantaSprite, 
            50, 
            10, 
            0)
    
    def fotosintesis(self,gameHour):
            if 10 <= gameHour <= 19:
                self.energy += 5
                if self.energy >= self.reproduccionNRG:
                    self.energy = 5
                    self.enReposo = True
                    if random.random() < 0.5:
                        self.reproducir()

    def reproducir(self):
        nSemillas = random.randint(1,2)
        for i in range(nSemillas):
            newSeed = Semilla(self.ecosistema)
            newSeed.rect.topleft = (
                self.rect.x + random.randint(-cellSize *2,cellSize *2),
                self.rect.y + random.randint(-cellSize *2,cellSize *2)
            )
            from classes.ecosistema import Ecosistema
            if isinstance(self.ecosistema, Ecosistema):
                self.ecosistema.newOrg(newSeed)
            else: continue
            self.ecosistema.bornCount += 1
        self.finishReproduction()

    def finishReproduction(self):
        self.enReposo = False
        self.die()