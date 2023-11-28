from classes.animal.animal import Animal
from classes.animal.puma import Puma
from classes.animal.condor import Condor
from classes.animal.oveja import Oveja
from classes.planta.planta import Planta
from constants import *

class Ecosistema:
    def __init__(self):
        self.orgsGroup = pygame.sprite.Group()
        self.initOrgs()
        self.bornCount = 0
        self.dieCount = 0

    def initOrgs(self):
        for _ in range(8):
            animal = Puma(self)
            self.orgsGroup.add(animal)
        for _ in range(20):
            animal = Oveja(self)
            self.orgsGroup.add(animal)
        for _ in range(10):
            planta = Planta(self)
            self.orgsGroup.add(planta)
        # condor = Condor(self)
        # self.orgsGroup.add(condor)
        
    def update(self, gameHour):
        for org in self.orgsGroup:
            if (isinstance(org, Animal)):
                    org.detectOrgs(self.orgsGroup)
                    org.detectOrgsToCoito(self.orgsGroup)
            if isinstance(org, Planta):
                org.fotosintesis(gameHour)

    def saveData(self):
        pass

    def newOrg(self, org):
        self.orgsGroup.add(org)