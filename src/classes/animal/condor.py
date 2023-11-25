from classes.animal.descomponedor import Descomponedor
from constants import condorSprite, cellSize

class Condor(Descomponedor):
    def __init__(self):
        self.hp = 150
        self.energy = 80
        self.attack = 50
        self.especie = 'condor'
        self.attackRange = 1 * cellSize
        self.visionRange = 10 * cellSize
        self.speed = 2
        super().__init__(condorSprite, self.hp, self.energy, self.attackRange, self.visionRange, self.attack, self.speed)
    
    def detectOrgs(self,orgs):
        if self.energy == self.maxEnergy: return
        for org in orgs:
            if org != self and org.isAlive:
                if self.isAlive:
                    distance , direction = self.getDirection(org)
                    if org.isDecomposing:
                        if distance < self.visionRange:
                            self.target = org
                            self.chase(org,direction)
                            return