from classes.animal.descomponedor import Descomponedor
from constants import condorSprite, cellSize

class Condor(Descomponedor):
    def __init__(self,ecosistema):
        self.hp = 150
        self.energy = 80
        self.attack = 50
        self.especie = 'condor'
        self.attackRange = 2 * cellSize
        self.visionRange = 10 * cellSize
        self.speed = 2
        super().__init__(condorSprite, self.hp, self.energy, self.attackRange, self.visionRange, self.attack,self.especie, ecosistema,self.speed)