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
        
    def initOrgs(self):
        for i in range(2):
            animal = Puma()
            self.orgsGroup.add(animal)
        for i in range(8):
            animal = Oveja()
            self.orgsGroup.add(animal)
            planta = Planta(plantaSprite)
            self.orgsGroup.add(planta)
        condor = Condor()
        self.orgsGroup.add(condor)
        
    def update(self):
        for org in self.orgsGroup:
            if (isinstance(org, Animal)):
                org.detectOrgs(self.orgsGroup)