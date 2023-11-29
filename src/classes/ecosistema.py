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
        self.initCSV()
        self.bornCount = 0
        self.dieCount = 0
        self.cicloCount = 0
        
    def initOrgs(self):
        for _ in range(2):
            animal = Puma(self)
            self.orgsGroup.add(animal)
        for _ in range(8):
            animal = Oveja(self)
            self.orgsGroup.add(animal)
        for _ in range(6):
            planta = Planta(self)
            self.orgsGroup.add(planta)
        
        condor = Condor(self)
        self.orgsGroup.add(condor)
        
    def update(self, gameHour):
        for org in self.orgsGroup:
            if (isinstance(org, Animal)):
                    org.detectOrgs(self.orgsGroup)
                    org.detectOrgsToCoito(self.orgsGroup)
            if isinstance(org, Planta):
                org.fotosintesis(gameHour)

    def initCSV(self):
        with open('data/natalidad.csv', 'w') as file:
            file.write('ciclo,bornCount,dieCount\n')

        with open('data/censo.csv', 'w') as file:
            file.write('ciclo,especie,cantidad\n')

    def updateCSV(self):
        self.cicloCount += 1
        with open('data/natalidad.csv', 'a') as file:
            file.write(f'{self.cicloCount},{self.bornCount},{self.dieCount}\n')

        with open('data/censo.csv', 'a') as file:
            for org in self.orgsGroup:
                if isinstance(org, Animal):
                    file.write(f'gola\n')

    def newOrg(self, org):
        self.orgsGroup.add(org)